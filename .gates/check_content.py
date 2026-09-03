#!/usr/bin/env python3
"""check_content —— 对构建产物(HTML 目录)做内容 lint。八道门禁之一,跑在产物上,不看源码。

规则(E = 阻塞,W = 警告):
  E H1_COUNT       每页 H1 必须恰好 1 个
  E IMG_ALT        <img> 必须有非空 alt(装饰图用 alt="" + role="presentation" 可豁免)
  E DEAD_INTERNAL  站内链接必须能解析到产物里的文件(尊重 trailingSlash / cleanUrls)
  E PLACEHOLDER    正文出现占位语(coming soon / being verified / 待补充 / TBD …)
  W HEADING_SKIP   标题层级跳级(H2 → H4)
  W FEW_LINKS      正文站内链接 < N 条(默认 3)
  W LOCALE_LINK    小语种页面里的站内链接指向了主语种页,而对应小语种页存在
  W LANG_ATTR      <html lang> 与所在语种目录不一致

用法:
  python3 check_content.py <html_dir> [--locales de,es,fr,it,ja] [--default en] [--min-links 3]
                           [--trailing-slash auto|yes|no] [--json] [--exclude 404,privacy-policy,terms]
退出码:有 E 则 1,否则 0。
"""
import argparse, json, os, re, sys, html
from html.parser import HTMLParser

PLACEHOLDER_CS = re.compile(r"\bTBD\b|\bTODO\b")
PLACEHOLDER = re.compile(r"coming soon|being verified|will be verified|to be confirmed|待补充|稍后补|稍后更新|即将上线|lorem ipsum", re.I)
TRUST = {"about", "contact", "privacy-policy", "privacy", "terms", "terms-of-service", "disclaimer", "editorial-policy", "404", "500", "search"}


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h = []; self.imgs = []; self.links = []; self.lang = None; self.in_main = 0; self.main_seen = False
        self.text = []; self._skip = 0; self.in_head = False; self.noindex = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = (a.get("lang") or "").split("-")[0].lower()
        if tag == "head": self.in_head = True
        if tag == "meta" and (a.get("name") or "").lower() == "robots" and "noindex" in (a.get("content") or "").lower(): self.noindex = True
        if tag in ("main", "article") and not self.main_seen: self.in_main += 1; self.main_seen = True
        if tag in ("script", "style", "nav", "header", "footer", "aside"): self._skip += 1
        if self._skip: return
        if re.fullmatch(r"h[1-6]", tag): self.h.append((int(tag[1]), self.getpos()[0]))
        if tag == "img": self.imgs.append((a.get("alt"), a.get("role"), a.get("src", "")))
        if tag == "a" and a.get("href"): self.links.append((a["href"], self.in_main > 0))

    def handle_endtag(self, tag):
        if tag == "head": self.in_head = False
        if tag in ("script", "style", "nav", "header", "footer", "aside") and self._skip: self._skip -= 1
        if tag in ("main", "article") and self.in_main: self.in_main -= 1

    def handle_data(self, d):
        if not self._skip and not self.in_head: self.text.append(d)


def route_of(path, root):
    rel = os.path.relpath(path, root).replace(os.sep, "/")
    if rel.endswith("/index.html"): rel = rel[:-len("index.html")]
    elif rel.endswith(".html"): rel = rel[:-5]
    return "/" + rel.strip("/") + ("/" if rel.endswith("/") or rel == "" else "")


def resolve(href, root, trailing):
    """站内 href → 产物文件是否存在。返回 (exists, normalized_route)"""
    h = href.split("#")[0].split("?")[0]
    if not h or h.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "//", "data:")): return True, None
    h = html.unescape(h)
    if not h.startswith("/"): return True, None  # 相对路径不判(少见)
    p = h.strip("/")
    cands = [os.path.join(root, p), os.path.join(root, p, "index.html"), os.path.join(root, p + ".html")] if p else [os.path.join(root, "index.html")]
    ok = any(os.path.isfile(c) for c in cands)
    return ok, "/" + p + ("/" if trailing else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root"); ap.add_argument("--locales", default=""); ap.add_argument("--default", default="en")
    ap.add_argument("--min-links", type=int, default=3); ap.add_argument("--trailing-slash", default="auto")
    ap.add_argument("--json", action="store_true"); ap.add_argument("--exclude", default="")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    locales = [x for x in a.locales.split(",") if x]
    exclude = set(TRUST) | {x for x in a.exclude.split(",") if x}
    trailing = a.trailing_slash
    if trailing == "auto":
        # 有 x/index.html 结构 → trailing;全是 x.html → clean
        idx = sum(1 for dp, _, fs in os.walk(root) for f in fs if f == "index.html")
        flat = sum(1 for dp, _, fs in os.walk(root) for f in fs if f.endswith(".html") and f != "index.html")
        trailing = "yes" if idx >= flat else "no"
    trailing = trailing == "yes"
    E, W = [], []
    pages = 0
    for dp, _, fs in os.walk(root):
        if "/_next" in dp or "/node_modules" in dp: continue
        for f in fs:
            if not f.endswith(".html"): continue
            path = os.path.join(dp, f)
            route = route_of(path, root)
            slug = route.strip("/").split("/")[-1] if route.strip("/") else "home"
            first = route.strip("/").split("/")[0] if route.strip("/") else ""
            if slug in exclude or first in exclude: continue
            p = P()
            try: p.feed(open(path, encoding="utf-8", errors="replace").read())
            except Exception as e: E.append(("PARSE", route, str(e)[:80])); continue
            if p.noindex: continue
            pages += 1
            h1 = [x for x in p.h if x[0] == 1]
            if len(h1) != 1: E.append(("H1_COUNT", route, f"H1 数量 {len(h1)}"))
            prev = 1
            for lvl, line in p.h:
                if lvl > prev + 1: W.append(("HEADING_SKIP", route, f"H{prev}→H{lvl} @line {line}")); break
                prev = lvl
            for alt, role, src in p.imgs:
                if (alt is None or not alt.strip()) and role != "presentation": E.append(("IMG_ALT", route, src[:80]))
            body = " ".join(p.text)
            m = PLACEHOLDER.search(body) or PLACEHOLDER_CS.search(body)
            if m: E.append(("PLACEHOLDER", route, f"「{m.group(0)}」"))
            internal_main = 0
            page_locale = first if first in locales else a.default
            for href, in_main in p.links:
                ok, norm = resolve(href, root, trailing)
                if norm is None: continue
                if not ok: E.append(("DEAD_INTERNAL", route, href[:100])); continue
                if in_main or not p.main_seen: internal_main += 1
                if page_locale != a.default:
                    seg = norm.strip("/").split("/")[0]
                    if seg not in locales and seg not in exclude:
                        loc_path = os.path.join(root, page_locale, norm.strip("/"))
                        if os.path.isfile(os.path.join(loc_path, "index.html")) or os.path.isfile(loc_path + ".html"):
                            W.append(("LOCALE_LINK", route, f"{href} 指向主语种页,但 /{page_locale}{norm} 存在"))
            if internal_main < a.min_links: W.append(("FEW_LINKS", route, f"正文站内链接 {internal_main} < {a.min_links}"))
            if p.lang and page_locale and p.lang != page_locale.lower(): W.append(("LANG_ATTR", route, f"<html lang={p.lang}> 但目录语种 {page_locale}"))
    if a.json:
        print(json.dumps({"pages": pages, "errors": E, "warnings": W}, ensure_ascii=False, indent=1))
    else:
        print(f"check_content: {pages} 页 · {len(E)} 阻塞 · {len(W)} 警告 (trailingSlash={'yes' if trailing else 'no'})")
        for k, r, m in E: print(f"  ❌ {k:14} {r}  {m}")
        for k, r, m in W[:200]: print(f"  ⚠  {k:14} {r}  {m}")
        if len(W) > 200: print(f"  … 另 {len(W)-200} 条警告")
    sys.exit(1 if E else 0)


if __name__ == "__main__":
    main()
