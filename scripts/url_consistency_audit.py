#!/usr/bin/env python3
"""url_consistency_audit —— 全站 URL 规范写法一致性审计(只读,纯标准库)。

规范:全站页面 URL 一律「带尾斜杠」一种写法(首页是 https://<host>/);带扩展名的文件 URL
(sitemap.xml / robots.txt / *.css / *.png …)不加斜杠。判定规则与 Vercel `trailingSlash: true`
同口径 —— path 最后一段不含「.」的就是页面 URL,必须以「/」结尾。

为什么要有它(2026-10-08):GSC「备用网页(有适当的规范标记)」报 /privacy-policy/、
/beast-of-reincarnation/{it,fr,ja}/ 未收录。根因是同一页有带斜杠 / 不带斜杠两个 200 网址,
canonical、hreflang、sitemap、站内链接各写各的。这个脚本把「各写各的」变成可数的数字。

两种模式:
  --out out/                 审构建产物(CI 门禁用;任何一项门禁计数 ≠ 0 退出码 1)
  --live https://lootwiki.com  审线上:读线上 sitemap 全量 URL 逐个抓(不跟随跳转),
                             并逐个探测「不带斜杠变体」的状态码与 Location
  --probe URL [URL…]         只探测给定网址(需配合 --live 指定站点):状态码 / canonical /
                             不带斜杠变体的状态码与 Location

用法:
  python3 scripts/url_consistency_audit.py --out out
  python3 scripts/url_consistency_audit.py --live https://lootwiki.com --json after.json
  python3 scripts/url_consistency_audit.py --live https://lootwiki.com --probe /privacy-policy/ /about/
"""
import argparse
import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

UA = "Mozilla/5.0 (compatible; lootlore-url-audit/1.0)"
LOC_RE = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>")
XLINK_RE = re.compile(r'<xhtml:link\b[^>]*\bhref="([^"]+)"', re.I)
# 内联脚本(非 JSON-LD)里引号包着的站内路径 / 绝对地址
JS_STR_RE = re.compile(r"""(["'`])((?:https?://[^"'`\s<>\\]+)|(?:/[A-Za-z0-9_\-][^"'`\s<>\\]*))\1""")
HREF_IN_TEXT_RE = re.compile(r"""href\s*=\s*(["'])(.*?)\1""", re.I | re.S)

# ---------------------------------------------------------------- URL 规则


def split_url(u: str):
    """→ (path, suffix)。suffix = 从第一个 ? 或 # 起的尾巴(斜杠只能加在 path 末尾,不能加在它后面)。"""
    m = re.search(r"[?#]", u)
    return (u, "") if not m else (u[:m.start()], u[m.start():])


def is_page_path(path: str) -> bool:
    """path 最后一段不含「.」= 页面 URL(与 Vercel trailingSlash 的判定同口径)。"""
    last = path.rsplit("/", 1)[-1]
    return "." not in last


def internal_path(u: str, base: str):
    """站内 URL → 根相对 path(不含 ?#);不是站内 URL 返回 None。"""
    u = (u or "").strip()
    if not u:
        return None
    path, _ = split_url(u)
    host = base.split("//", 1)[1]
    for pre in (base, "http://" + host, "https://www." + host, "http://www." + host):
        if path == pre:
            return ""            # 裸域名(没有任何 path)
        if path.startswith(pre + "/"):
            return path[len(pre):]
    if path.startswith("/") and not path.startswith("//"):
        return path
    return None


def lacks_slash(path) -> bool:
    """站内页面 URL 且没有以 / 结尾(裸域名也算:规范写法是 https://host/)。"""
    if path is None:
        return False
    if path == "":
        return True
    return is_page_path(path) and not path.endswith("/")


def canon_path(path: str) -> str:
    """任一写法 → 规范 path(页面 URL 补尾斜杠)。"""
    if path in ("", "/"):
        return "/"
    return path + "/" if (is_page_path(path) and not path.endswith("/")) else path


# ---------------------------------------------------------------- 单页解析
class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.canonicals = []
        self.og_urls = []
        self.alternates = []     # [(hreflang, href)]
        self.a_hrefs = []
        self.other_hrefs = []    # [(tag, attr, value)]:form action / link prev|next / area / data-* 等
        self.ld_raw = []
        self.js_raw = []
        self.robots = ""
        self.h1 = 0
        self._script = None
        self._buf = []

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "link":
            rel = a.get("rel", "").lower()
            if rel == "canonical":
                self.canonicals.append(a.get("href", ""))
            elif rel == "alternate" and a.get("hreflang"):
                self.alternates.append((a["hreflang"], a.get("href", "")))
            elif rel in ("prev", "next"):
                self.other_hrefs.append((tag, "href:" + rel, a.get("href", "")))
        elif tag == "meta":
            if a.get("property", "").lower() == "og:url":
                self.og_urls.append(a.get("content", ""))
            elif a.get("name", "").lower() == "twitter:url":
                self.other_hrefs.append((tag, "twitter:url", a.get("content", "")))
            elif a.get("name", "").lower() == "robots":
                self.robots = a.get("content", "")
        elif tag == "a":
            if "href" in a:
                self.a_hrefs.append(a["href"])
        elif tag == "area" and "href" in a:
            self.other_hrefs.append((tag, "href", a["href"]))
        elif tag == "form" and "action" in a:
            self.other_hrefs.append((tag, "action", a["action"]))
        elif tag == "h1":
            self.h1 += 1
        elif tag == "script":
            self._script = "ld" if "ld+json" in a.get("type", "").lower() else "js"
            self._buf = []
        # 任意标签上的 data-href / data-url 之类(站内跳转有时藏在这里)
        for k, v in a.items():
            if k.startswith("data-") and k in ("data-href", "data-url", "data-link", "data-route"):
                self.other_hrefs.append((tag, k, v))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_data(self, data):
        if self._script:
            self._buf.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._script:
            (self.ld_raw if self._script == "ld" else self.js_raw).append("".join(self._buf))
            self._script = None


def ld_urls(raw_blocks, base):
    """JSON-LD 里所有指向本站的 URL:整串就是 URL 的字符串值 + 文本值里内嵌的 href。"""
    out, bad = [], 0

    def walk(o):
        if isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        elif isinstance(o, str):
            s = o.strip()
            if "<" in s and "href" in s:
                for m in HREF_IN_TEXT_RE.finditer(s):
                    if internal_path(m.group(2), base) is not None:
                        out.append(m.group(2))
            elif " " not in s and internal_path(s, base) is not None and (
                    s.startswith(base) or s.startswith("/")):
                # 根相对的字符串只认「像路径」的(避免把 "/" 开头的普通文本当 URL);绝对地址一律算
                if s.startswith(base) or re.fullmatch(r"/[\w\-./%#?=&~+]*", s):
                    out.append(s)
    for raw in raw_blocks:
        try:
            walk(json.loads(raw))
        except Exception:
            bad += 1
    return out, bad


def analyze(html: str, base: str) -> dict:
    p = Page()
    try:
        p.feed(html)
        p.close()
    except Exception:
        pass
    lds, ld_bad = ld_urls(p.ld_raw, base)
    js = []
    for raw in p.js_raw:
        for m in JS_STR_RE.finditer(raw):
            if internal_path(m.group(2), base) is not None:
                js.append(m.group(2))
    return {"canonicals": p.canonicals, "og_urls": p.og_urls, "alternates": p.alternates,
            "a_hrefs": p.a_hrefs, "other": p.other_hrefs, "ld": lds, "ld_bad": ld_bad,
            "js": js, "robots": p.robots, "h1": p.h1}


# ---------------------------------------------------------------- 审计主体(两种模式共用)
def audit(pages: dict, sitemap_locs: list, sitemap_xlinks: list, base: str, exists, search_rows=None,
          describe=None):
    """pages: {规范 path: html};exists(规范 path) → 该站内 URL 是否是一个真实存在的页面/文件。
    返回 (counts, samples)。所有计数的口径两种模式完全相同。"""
    C, S = Counter(), {}
    describe = describe or (lambda cp: "")

    def hit(key, sample, n=1):
        C[key] += n
        S.setdefault(key, [])
        if len(S[key]) < 12 and sample not in S[key]:
            S[key].append(sample)

    for k in ("sitemap_total", "sitemap_loc_no_slash", "sitemap_xlink_no_slash", "sitemap_loc_dup",
              "pages_audited", "canonical_missing", "canonical_multiple", "canonical_no_slash",
              "canonical_not_self", "og_url_missing", "og_url_not_self",
              "hreflang_total", "hreflang_no_slash", "hreflang_target_missing", "hreflang_asymmetric",
              "hreflang_no_self",
              "jsonld_internal_urls", "jsonld_no_slash", "jsonld_target_missing", "jsonld_parse_error",
              "a_href_internal", "a_href_no_slash", "a_href_target_missing",
              "other_attr_no_slash", "inline_js_no_slash", "search_index_no_slash"):
        C[k] += 0

    # ---- sitemap
    C["sitemap_total"] = len(sitemap_locs)
    seen = set()
    for u in sitemap_locs:
        ip = internal_path(u, base)
        if lacks_slash(ip):
            hit("sitemap_loc_no_slash", u)
        key = canon_path(ip) if ip is not None else u
        if key in seen:
            hit("sitemap_loc_dup", u)
        seen.add(key)
    for u in sitemap_xlinks:
        if lacks_slash(internal_path(u, base)):
            hit("sitemap_xlink_no_slash", u)

    # ---- 逐页
    info = {path: analyze(html, base) for path, html in pages.items()}
    C["pages_audited"] = len(info)
    alt_sets = {}
    for path, d in info.items():
        self_url = base + path
        cs = [c.strip() for c in d["canonicals"]]
        if not cs:
            hit("canonical_missing", path)
        else:
            if len(cs) > 1:
                hit("canonical_multiple", path)
            c = cs[0]
            if lacks_slash(internal_path(c, base)):
                hit("canonical_no_slash", f"{path} -> {c}")
            if c != self_url:
                hit("canonical_not_self", f"{path} -> {c}")
        og = [o.strip() for o in d["og_urls"]]
        if not og:
            hit("og_url_missing", path)
        elif og[0] != self_url:
            hit("og_url_not_self", f"{path} -> {og[0]}")

        targets = set()
        has_self = False
        for code, href in d["alternates"]:
            C["hreflang_total"] += 1
            ip = internal_path(href, base)
            if lacks_slash(ip):
                hit("hreflang_no_slash", f"{path} [{code}] -> {href}")
            if ip is not None:
                cp = canon_path(ip)
                if not exists(cp):
                    hit("hreflang_target_missing", f"{path} [{code}] -> {href}{describe(cp)}")
                if cp == path:
                    has_self = True
                if code.lower() != "x-default":
                    targets.add(cp)
        if d["alternates"] and not has_self:
            hit("hreflang_no_self", path)
        alt_sets[path] = targets

        C["jsonld_internal_urls"] += len(d["ld"])
        C["jsonld_parse_error"] += d["ld_bad"]
        for u in d["ld"]:
            ip = internal_path(u, base)
            if lacks_slash(ip):
                hit("jsonld_no_slash", f"{path} :: {u}")
            if ip is not None and not exists(canon_path(ip)):
                hit("jsonld_target_missing", f"{path} :: {u}{describe(canon_path(ip))}")

        for h in d["a_hrefs"]:
            ip = internal_path(h, base)
            if ip is None:
                continue
            C["a_href_internal"] += 1
            if lacks_slash(ip):
                hit("a_href_no_slash", f"{path} :: {h}")
            if not exists(canon_path(ip)):
                hit("a_href_target_missing", f"{path} :: {h}{describe(canon_path(ip))}")
        for tag, attr, v in d["other"]:
            if lacks_slash(internal_path(v, base)):
                hit("other_attr_no_slash", f"{path} :: <{tag} {attr}> {v}")
        for u in d["js"]:
            if lacks_slash(internal_path(u, base)):
                hit("inline_js_no_slash", f"{path} :: {u}")

    # ---- hreflang 互指:A 声明了 B,B 也必须声明 A(x-default 不参与)
    for a_path, targets in alt_sets.items():
        for b in targets:
            if b == a_path:
                continue
            if b not in alt_sets:
                continue         # 目标不在审计集合里 → 已经记进 hreflang_target_missing
            if a_path not in alt_sets[b]:
                hit("hreflang_asymmetric", f"{a_path} -> {b}(对方没有回指)")

    for row in (search_rows or []):
        u = row.get("url", "") if isinstance(row, dict) else ""
        if lacks_slash(internal_path(u, base)):
            hit("search_index_no_slash", u)
    return C, S


# 门禁项:--out 模式下任一 ≠ 0 即红
GATE_KEYS = ["sitemap_loc_no_slash", "sitemap_xlink_no_slash", "sitemap_loc_dup", "sitemap_loc_no_file",
             "sitemap_count_ne_pages",
             "canonical_missing", "canonical_multiple", "canonical_no_slash", "canonical_not_self",
             "og_url_not_self",
             "hreflang_no_slash", "hreflang_target_missing", "hreflang_asymmetric", "hreflang_no_self",
             "jsonld_no_slash", "jsonld_target_missing", "jsonld_parse_error",
             "a_href_no_slash", "a_href_target_missing", "other_attr_no_slash", "inline_js_no_slash",
             "search_index_no_slash",
             "page_slug_with_dot",
             "vercel_trailing_slash_off", "vercel_redirect_dest_no_slash", "vercel_redirect_dest_missing",
             "vercel_redirect_source_no_slash_variant", "game_root_unresolved", "robots_sitemap_bad",
             "llms_txt_no_slash"]

LABELS = {
    "sitemap_total": "sitemap <loc> 条数",
    "sitemap_loc_no_slash": "sitemap <loc> 不带尾斜杠(不含带扩展名的)",
    "sitemap_xlink_no_slash": "sitemap xhtml:link 不带尾斜杠",
    "sitemap_loc_dup": "sitemap 重复条目(同一页两种写法)",
    "sitemap_loc_no_file": "sitemap <loc> 在产物里没有对应页面",
    "sitemap_count_ne_pages": "sitemap 条数 ≠ 可索引页数(差值)",
    "pages_audited": "审计页数",
    "canonical_missing": "缺 canonical 的页数",
    "canonical_multiple": "canonical 多于一条的页数",
    "canonical_no_slash": "canonical 不带尾斜杠的页数",
    "canonical_not_self": "canonical ≠ 页面自身规范 URL 的页数",
    "og_url_missing": "缺 og:url 的页数(只报告)",
    "og_url_not_self": "og:url ≠ 页面自身规范 URL 的页数",
    "hreflang_total": "hreflang 条数",
    "hreflang_no_slash": "hreflang href 不带尾斜杠的条数",
    "hreflang_target_missing": "hreflang 指向不存在 / 非 200 的条数",
    "hreflang_asymmetric": "hreflang 互指不对称的条数",
    "hreflang_no_self": "有 hreflang 但没有自指的页数",
    "jsonld_internal_urls": "JSON-LD 内本站 URL 条数",
    "jsonld_no_slash": "JSON-LD 内本站页面 URL 不带尾斜杠的条数",
    "jsonld_target_missing": "JSON-LD 内本站 URL 指向不存在 / 非 200 的条数",
    "jsonld_parse_error": "JSON-LD 解析失败块数",
    "a_href_internal": "站内 <a href> 条数",
    "a_href_no_slash": "站内 <a href> 指向不带尾斜杠页面 URL 的条数",
    "a_href_target_missing": "站内 <a href> 指向不存在 / 非 200 的条数",
    "other_attr_no_slash": "其他属性(form action / link prev,next / data-*)不带尾斜杠的条数",
    "inline_js_no_slash": "内联脚本里站内页面 URL 不带尾斜杠的条数",
    "search_index_no_slash": "search-index.json 里 url 不带尾斜杠的条数",
    "page_slug_with_dot": "页面路径末段含「.」的页数(会被 Vercel 当成文件、不走尾斜杠)",
    "vercel_trailing_slash_off": "vercel.json 未开 trailingSlash:true",
    "vercel_redirect_dest_no_slash": "vercel.json redirects 目的地不带尾斜杠的条数",
    "vercel_redirect_dest_missing": "vercel.json redirects 目的地在产物里不存在的条数",
    "vercel_redirect_source_no_slash_variant": "vercel.json redirects 源地址缺「带尾斜杠」写法的条数",
    "game_root_unresolved": "游戏根目录 /<slug>/ 既无页面也无重定向的个数",
    "robots_sitemap_bad": "robots.txt 的 Sitemap 行不是 <base>/sitemap.xml",
    "llms_txt_no_slash": "llms.txt 里本站页面 URL 不带尾斜杠的条数",
    "live_sitemap_200": "(live) sitemap URL 直接 200 的条数",
    "live_sitemap_redirect": "(live) sitemap URL 发生跳转的条数",
    "live_sitemap_other": "(live) sitemap URL 既非 200 也非跳转的条数",
    "live_slash_200": "(live) 带斜杠写法直接 200 的页数",
    "live_noslash_200": "(live) 不带斜杠变体也直接 200 的页数(= 双网址)",
    "live_noslash_308_to_slash": "(live) 不带斜杠变体 308 → 带斜杠版(单跳)的页数",
    "live_noslash_other": "(live) 不带斜杠变体其他结果的页数",
    "live_fetch_failed": "(live) 重试后仍抓不到的请求数",
    "live_game_root_not_ok": "(live) 游戏根目录 /<slug>/ 既非 200 也非一跳到 200 的个数",
}


# ---------------------------------------------------------------- --out
def run_out(out_dir: Path, base: str):
    out_dir = out_dir.resolve()
    root = out_dir.parent
    if not base:
        cfg = root / "config" / "hub.json"
        base = json.loads(cfg.read_text(encoding="utf-8"))["base_url"].rstrip("/")
    files = {}
    for p in sorted(out_dir.rglob("*.html")):
        rel = p.relative_to(out_dir).as_posix()
        if rel == "index.html":
            path = "/"
        elif rel.endswith("/index.html"):
            path = "/" + rel[:-len("index.html")]
        else:
            path = "/" + rel[:-5] + "/"
        files[path] = p
    assets = {"/" + p.relative_to(out_dir).as_posix() for p in out_dir.rglob("*") if p.is_file()}
    vj = root / "vercel.json"
    vercel = json.loads(vj.read_text(encoding="utf-8")) if vj.is_file() else {}
    redirects = vercel.get("redirects", [])
    # 页面级重定向的源地址(按 host 匹配的整站跳转不算):引用它不是死链,线上是 3xx
    redirect_sources = {r.get("source", "") for r in redirects if not r.get("has")}

    def exists(cp: str) -> bool:
        return cp in files or cp in assets or cp in redirect_sources

    pages = {path: p.read_text(encoding="utf-8") for path, p in files.items()}
    sm = (out_dir / "sitemap.xml").read_text(encoding="utf-8") if (out_dir / "sitemap.xml").is_file() else ""
    locs, xlinks = LOC_RE.findall(sm), XLINK_RE.findall(sm)
    rows = []
    si = out_dir / "search-index.json"
    if si.is_file():
        rows = json.loads(si.read_text(encoding="utf-8"))
    C, S = audit(pages, locs, xlinks, base, exists, rows)

    def hit(key, sample, n=1):
        C[key] += n
        S.setdefault(key, [])
        if len(S[key]) < 12:
            S[key].append(sample)

    for k in ("sitemap_loc_no_file", "sitemap_count_ne_pages", "page_slug_with_dot",
              "vercel_trailing_slash_off", "vercel_redirect_dest_no_slash", "vercel_redirect_dest_missing",
              "vercel_redirect_source_no_slash_variant", "game_root_unresolved", "robots_sitemap_bad",
              "llms_txt_no_slash"):
        C[k] += 0
    # sitemap ↔ 产物
    for u in locs:
        ip = internal_path(u, base)
        if ip is None or canon_path(ip) not in files:
            hit("sitemap_loc_no_file", u)
    indexable = [pth for pth, html in pages.items()
                 if pth != "/404/" and not re.search(r'<meta\s+name="robots"[^>]*noindex', html[:6000], re.I)]
    C["indexable_pages"] = len(indexable)
    if len(indexable) != len(locs):
        hit("sitemap_count_ne_pages", f"可索引页 {len(indexable)} vs sitemap {len(locs)}",
            abs(len(indexable) - len(locs)))
    for pth in files:
        segs = [s for s in pth.strip("/").split("/") if s]
        if any("." in s for s in segs):
            hit("page_slug_with_dot", pth)
    # robots / llms
    rb = out_dir / "robots.txt"
    lines = [l.split(":", 1)[1].strip() for l in (rb.read_text(encoding="utf-8").splitlines() if rb.is_file() else [])
             if l.lower().startswith("sitemap:")]
    if lines != [f"{base}/sitemap.xml"]:
        hit("robots_sitemap_bad", str(lines))
    lt = out_dir / "llms.txt"
    if lt.is_file():
        for u in re.findall(r"\((https?://[^)\s]+)\)", lt.read_text(encoding="utf-8")):
            if lacks_slash(internal_path(u, base)):
                hit("llms_txt_no_slash", u)
    # vercel.json
    if vj.is_file():
        v = vercel
        if v.get("trailingSlash") is not True:
            hit("vercel_trailing_slash_off", f"trailingSlash={v.get('trailingSlash')!r}")
        sources = redirect_sources
        for r in redirects:
            if r.get("has"):
                continue          # 按 host 匹配的整站跳转(旧预览域名),不是页面级规则
            src, dst = r.get("source", ""), r.get("destination", "")
            dp = internal_path(dst, base)
            if dp is not None and ":" not in dp:
                if lacks_slash(dp):
                    hit("vercel_redirect_dest_no_slash", f"{src} -> {dst}")
                if canon_path(dp) not in files and canon_path(dp) not in assets:
                    hit("vercel_redirect_dest_missing", f"{src} -> {dst}")
            elif dp is not None and lacks_slash(dp):
                hit("vercel_redirect_dest_no_slash", f"{src} -> {dst}")
            # trailingSlash:true 下请求先被补斜杠,源地址只写不带斜杠的那条永远匹配不上
            sp, _ = split_url(src)
            if is_page_path(sp) and not sp.endswith("/") and (sp + "/") not in sources:
                hit("vercel_redirect_source_no_slash_variant", src)
    cfgf = root / "config" / "hub.json"
    if cfgf.is_file():
        rsrc = redirect_sources
        for g in json.loads(cfgf.read_text(encoding="utf-8")).get("games", []):
            rp = f"/{g['slug']}/"
            if rp not in files and rp not in rsrc:
                hit("game_root_unresolved", rp)
    return base, C, S, {}


# ---------------------------------------------------------------- --live
class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


_OPENER = urllib.request.build_opener(_NoRedirect)


def fetch(url: str, tries: int = 4, body: bool = True):
    """不跟随跳转。返回 (status, location, text)。status 0 = 网络层失败(重试后)。"""
    err = ""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
            with _OPENER.open(req, timeout=30) as r:
                return r.status, "", (r.read().decode("utf-8", "replace") if body else "")
        except urllib.error.HTTPError as e:
            if e.code in (500, 502, 503, 504) and i < tries - 1:
                time.sleep(1.5 * (i + 1))
                continue
            return e.code, e.headers.get("Location", "") or "", ""
        except Exception as e:          # noqa: BLE001
            err = repr(e)
            time.sleep(1.5 * (i + 1))
    return 0, err, ""


def pmap(fn, items, workers):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(fn, items))


def abs_loc(base: str, loc: str) -> str:
    return base + loc if loc.startswith("/") else loc


def run_live(base: str, workers: int):
    base = base.rstrip("/")
    st, _, sm = fetch(base + "/sitemap.xml")
    if st != 200:
        raise SystemExit(f"拿不到 sitemap:{base}/sitemap.xml HTTP {st}")
    locs, xlinks = LOC_RE.findall(sm), XLINK_RE.findall(sm)
    paths = []
    for u in locs:
        ip = internal_path(u, base)
        if ip is not None:
            paths.append(ip)
    canon = sorted({canon_path(p) for p in paths})

    # 1) sitemap 里写的那个 URL 原样抓(状态码 / 是否跳转)
    as_listed = dict(zip(locs, pmap(lambda u: fetch(u, body=False)[:2], locs, workers)))
    # 2) 每页的带斜杠写法(取 HTML 做审计)与不带斜杠变体
    slash = dict(zip(canon, pmap(lambda p: fetch(base + p), canon, workers)))
    noslash_paths = [p[:-1] for p in canon if p != "/"]
    noslash = dict(zip(noslash_paths, pmap(lambda p: fetch(base + p), noslash_paths, workers)))

    pages, failed = {}, 0
    for p in canon:
        s, _, html = slash[p]
        if s == 200:
            pages[p] = html
        elif p != "/" and noslash[p[:-1]][0] == 200:
            pages[p] = noslash[p[:-1]][2]     # 带斜杠版拿不到时退用不带斜杠版的 HTML
        if s == 0:
            failed += 1

    status_cache = {p: slash[p][0] for p in canon}

    def exists(cp: str) -> bool:
        if cp not in status_cache:
            status_cache[cp] = fetch(base + cp, body=False)[0]
        return status_cache[cp] == 200

    # 先把页面里引用到、但不在 sitemap 里的站内目标批量探一遍(并发),exists() 就只查缓存
    want = set()
    for html in pages.values():
        d = analyze(html, base)
        for _c, h in d["alternates"]:
            ip = internal_path(h, base)
            if ip is not None:
                want.add(canon_path(ip))
        for h in d["a_hrefs"] + d["ld"]:
            ip = internal_path(h, base)
            if ip is not None:
                want.add(canon_path(ip))
    todo = sorted(w for w in want if w not in status_cache)
    for w, r in zip(todo, pmap(lambda p: fetch(base + p, body=False)[0], todo, workers)):
        status_cache[w] = r

    st, _, si = fetch(base + "/search-index.json")
    rows = []
    if st == 200:
        try:
            rows = json.loads(si)
        except Exception:
            rows = []
    C, S = audit(pages, locs, xlinks, base, exists, rows,
                 describe=lambda cp: f"  [HTTP {status_cache.get(cp, '?')}]")

    def hit(key, sample, n=1):
        C[key] += n
        S.setdefault(key, [])
        if len(S[key]) < 12:
            S[key].append(sample)

    for k in ("live_sitemap_200", "live_sitemap_redirect", "live_sitemap_other", "live_slash_200",
              "live_noslash_200", "live_noslash_308_to_slash", "live_noslash_other", "live_fetch_failed",
              "live_game_root_not_ok"):
        C[k] += 0
    C["live_fetch_failed"] = failed
    rowsout = []
    for u in locs:
        s, loc = as_listed[u]
        if s == 200:
            C["live_sitemap_200"] += 1
        elif 300 <= s < 400:
            hit("live_sitemap_redirect", f"{u} {s} -> {loc}")
        else:
            hit("live_sitemap_other", f"{u} {s}")
    for p in canon:
        s = slash[p][0]
        if s == 200:
            C["live_slash_200"] += 1
        row = {"page": p, "slash_status": s, "slash_location": slash[p][1] if s != 200 else ""}
        if p != "/":
            ns, nloc, _ = noslash[p[:-1]]
            row.update(noslash_status=ns, noslash_location=nloc)
            if ns == 200:
                hit("live_noslash_200", p[:-1])
            elif ns == 308 and abs_loc(base, nloc) == base + p and s == 200:
                C["live_noslash_308_to_slash"] += 1
            else:
                hit("live_noslash_other", f"{p[:-1]} {ns} -> {nloc}")
        rowsout.append(row)
    C["sitemap_200_rate_pct"] = round(100.0 * C["live_sitemap_200"] / max(1, len(locs)), 2)

    extra = {"per_page": rowsout}
    # 游戏根目录 /<slug>/:要么直接 200,要么一跳重定向到一个 200 的页
    cfgf = Path(__file__).resolve().parent.parent / "config" / "hub.json"
    roots = []
    if cfgf.is_file():
        for g in json.loads(cfgf.read_text(encoding="utf-8")).get("games", []):
            rp = f"/{g['slug']}/"
            s1, loc1, _ = fetch(base + rp, body=False)
            row = {"root": rp, "status": s1, "location": loc1 if s1 != 200 else ""}
            ok = s1 == 200
            if 300 <= s1 < 400 and loc1:
                s2, loc2, _ = fetch(abs_loc(base, loc1), body=False)
                row.update(target_status=s2, target_location=loc2 if s2 != 200 else "")
                ok = s2 == 200
            ns, nloc, _ = fetch(base + rp[:-1], body=False)
            row.update(noslash_status=ns, noslash_location=nloc)
            if not ok:
                hit("live_game_root_not_ok", f"{rp} HTTP {s1} {loc1}")
            roots.append(row)
    extra["game_roots"] = roots
    st, _, rob = fetch(base + "/robots.txt")
    extra["robots"] = {"status": st, "sitemap_lines": [l.split(":", 1)[1].strip() for l in rob.splitlines()
                                                      if l.lower().startswith("sitemap:")]}
    extra["sitemap_xml_status"] = 200
    return base, C, S, extra


def probe(base: str, urls):
    base = base.rstrip("/")
    rows = []
    for u in urls:
        full = abs_loc(base, u) if u.startswith("/") else u
        s, loc, html = fetch(full)
        canon = ""
        if s == 200:
            cs = analyze(html, base)["canonicals"]
            canon = cs[0] if cs else "(缺)"
        path, _ = split_url(full)
        row = {"url": full, "status": s, "location": loc if s != 200 else "", "canonical": canon}
        if path.endswith("/") and path != base + "/":
            ns, nloc, _ = fetch(path[:-1], body=False)
            row.update(noslash_url=path[:-1], noslash_status=ns, noslash_location=nloc)
        if 300 <= s < 400 and loc:
            s2, loc2, html2 = fetch(abs_loc(base, loc))
            cs2 = analyze(html2, base)["canonicals"] if s2 == 200 else []
            row.update(hop2_url=abs_loc(base, loc), hop2_status=s2, hop2_location=loc2 if s2 != 200 else "",
                       hop2_canonical=(cs2[0] if cs2 else ""))
        rows.append(row)
    return rows


# ---------------------------------------------------------------- 输出
def now_bj() -> str:
    return (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).strftime(
        "%Y-%m-%d %H:%M:%S 北京时间")


def main():
    ap = argparse.ArgumentParser(description="全站 URL 规范写法(带尾斜杠)一致性审计")
    ap.add_argument("--out", help="构建产物目录,如 out/")
    ap.add_argument("--live", help="线上站点,如 https://lootwiki.com")
    ap.add_argument("--base", default="", help="--out 模式下覆盖 base_url(默认读 config/hub.json)")
    ap.add_argument("--probe", nargs="+", help="只探测这些网址(配合 --live)")
    ap.add_argument("--json", dest="json_out", help="把完整结果写到这个 JSON 文件")
    ap.add_argument("--workers", type=int, default=6, help="--live 并发数(默认 6,不要超过 8)")
    ap.add_argument("--no-fail", action="store_true", help="有问题也退出 0(只做记录)")
    a = ap.parse_args()
    if bool(a.out) == bool(a.live):
        ap.error("--out 与 --live 二选一")
    started = now_bj()

    if a.probe:
        if not a.live:
            ap.error("--probe 需要 --live 指定站点")
        rows = probe(a.live, a.probe)
        for r in rows:
            print(json.dumps(r, ensure_ascii=False))
        if a.json_out:
            Path(a.json_out).write_text(json.dumps({"ran_at": started, "probe": rows}, ensure_ascii=False,
                                                   indent=2) + "\n", encoding="utf-8")
        return

    if a.out:
        mode = "out"
        base, C, S, extra = run_out(Path(a.out), a.base.rstrip("/"))
    else:
        mode = "live"
        base, C, S, extra = run_live(a.live, max(1, min(8, a.workers)))

    order = [k for k in LABELS if k in C]
    gate_fail = [k for k in GATE_KEYS if C.get(k, 0)]
    print(f"url_consistency_audit [{mode}] {base} · {started}")
    print(f"{'指标':<58}{'计数':>8}  门禁")
    for k in order:
        flag = ("红" if C[k] else "绿") if k in GATE_KEYS else "-"
        print(f"{LABELS[k]:<58}{C[k]:>8}  {flag}")
    if "sitemap_200_rate_pct" in C:
        print(f"{'(live) sitemap URL 200 率 %':<58}{C['sitemap_200_rate_pct']:>8}")
    if "indexable_pages" in C:
        print(f"{'可索引页数(产物)':<58}{C['indexable_pages']:>8}")
    for k in order:
        if C[k] and k in S and (k in GATE_KEYS or k.startswith("live_")):
            print(f"\n  [{k}] 样例(最多 12 条):")
            for s in S[k]:
                print(f"    {s}")
    result = {"mode": mode, "base": base, "ran_at": started, "finished_at": now_bj(),
              "counts": dict(C), "gate_failed": gate_fail, "samples": S}
    result.update(extra)
    if a.json_out:
        Path(a.json_out).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if mode == "out":
        print(f"\n→ 门禁项 {len(GATE_KEYS)} 个,非 0 的 {len(gate_fail)} 个" +
              (":" + ", ".join(gate_fail) if gate_fail else ""))
        sys.exit(1 if (gate_fail and not a.no_fail) else 0)


if __name__ == "__main__":
    main()
