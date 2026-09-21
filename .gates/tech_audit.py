#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
技术 SEO 项审计脚本(只查不改,不写任何文件)。

输入:构建产物目录(HTML)——脚本内 SITES 字典登记「站名 → {html_root, base_url,
     multilang, public_root}」,跑之前把要审的站改成自己的路径;不是命令行参数。
输出:每站 11 项统计(title / description / canonical / JSON-LD / OpenGraph /
     hreflang / img alt-宽高 / h1 / 内链孤儿页 / robots+sitemap / 404与信任页六件套)
     汇总成一份 JSON 打到 stdout,人工核对或另写脚本转成 Markdown 表格都可以。
运行: python3 scripts/tech-audit.py > tech-audit-raw.json
      python3 .gates/tech_audit.py --out out --base https://域名 [--prefix /<game>/] [--summary]
      (lootlore 版:命令行传产物目录;--prefix 只统计该子树的页,内链/入链仍按全站算)

lootlore 本地改动(2026-09-17,待并回 seo-jianzhan/scripts/tech-audit.py):
  1. title / description 长度按「显示宽度」算:CJK/全角字符记 2,其余记 1
     (中文 title 30 字 ≈ 60 宽;按字符数会把中文长标题判成合格、把正常中文 description 判成过短)。
  2. 新增 description 过短(<70 宽)计数;新增正文词数(拉丁词 + CJK 字符/2)与 <800 薄页计数。
  3. og:image 指向外部域名(如商店页官方截图热链)时不按本地文件查,单独计 og_image_external。
依赖: 仅标准库(json/os/re/sys/collections/urllib.parse/html.parser),无需 pip install。

🔴 只读审计,绝不改动构建产物。改动/修复请求见 SKILL.md ⑥「技术 SEO 审计(只查不改)」——
   修复后必须重跑本脚本核对结果,不能沿用修复前的报告数字(报告数字与实测可能偏差很大)。
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from urllib.parse import urlparse, urljoin
from html.parser import HTMLParser
from pathlib import Path

ROOT = "/home/claude/work"

def _hub_base():
    for c in (Path.cwd() / "config" / "hub.json", Path(__file__).resolve().parent.parent / "config" / "hub.json"):
        try:
            return json.loads(c.read_text(encoding="utf-8"))["base_url"].rstrip("/")
        except Exception:
            continue
    return None


SITES = {
    "sephiria-wiki": {
        "html_root": f"{ROOT}/sephiria-wiki/out",
        "base_url": "https://sephiriawiki.site",
        "multilang": False,
        "public_root": f"{ROOT}/sephiria-wiki/out",
    },
    "dragonsword-guide": {
        "html_root": f"{ROOT}/dragonsword-guide/out",
        "base_url": None,  # 从页面里探测
        "multilang": False,
        "public_root": f"{ROOT}/dragonsword-guide/out",
    },
    "orc-problem-guide": {
        "html_root": f"{ROOT}/orc-problem-guide/out",
        "base_url": None,
        "multilang": False,
        "public_root": f"{ROOT}/orc-problem-guide/out",
    },
    "Beast-of-Reincarnation": {
        "html_root": f"{ROOT}/Beast-of-Reincarnation",
        "base_url": None,
        "multilang": True,
        "public_root": f"{ROOT}/Beast-of-Reincarnation",
        "flat": True,  # 手写扁平 en/slug.html 结构
    },
    "shift-at-midnight-wiki": {
        "html_root": f"{ROOT}/shift-at-midnight-wiki/public",
        "base_url": None,
        "multilang": False,
        "public_root": f"{ROOT}/shift-at-midnight-wiki/public",
    },
    "lootlore": {
        "html_root": f"{ROOT}/lootlore/out",
        # 域名不写死:优先读仓内 config/hub.json(唯一真相源),命令行 --base 仍可覆盖
        "base_url": _hub_base(),
        "multilang": True,  # 仅 beast-of-reincarnation 子目录
        "public_root": f"{ROOT}/lootlore/out",
    },
}

CJK_WIDE = re.compile(r"[\u1100-\u115f\u2e80-\ua4cf\uac00-\ud7a3\uf900-\ufaff\ufe30-\ufe4f\uff00-\uff60\uffe0-\uffe6]")
CJK_CHAR = re.compile(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7a3\uf900-\ufaff]")


def display_len(s):
    """CJK/全角字符记 2,其余记 1 —— SERP 截断按像素宽度,1 个汉字约等于 2 个拉丁字符。"""
    return sum(2 if CJK_WIDE.match(c) else 1 for c in s)


def word_count(text):
    """audit-rules「CJK 词数计算」:拉丁词按空格分 + CJK 字符数 / 2。"""
    latin = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’-]*", CJK_CHAR.sub(" ", text)))
    return latin + len(CJK_CHAR.findall(text)) // 2


TRUST_PAGES = ["about", "contact", "privacy", "privacy-policy", "disclaimer", "editorial-policy", "author"]


def find_html_files(root):
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # 排除 next 静态资源目录、图片目录
        dirnames[:] = [d for d in dirnames if d not in ("_next", "images", "node_modules")]
        for fn in filenames:
            if fn.endswith(".html"):
                files.append(os.path.join(dirpath, fn))
    return sorted(files)


def url_path_for(root, filepath):
    """把文件路径转成站内 url path，比如 out/guides/index.html -> /guides/"""
    rel = os.path.relpath(filepath, root)
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    if rel.endswith(".html"):
        # 扁平文件比如 en/foo.html -> /en/foo (Beast 站) 或 404.html -> /404.html
        return "/" + rel[:-5] if rel != "404.html" else "/404.html"
    return "/" + rel


class PageParser(HTMLParser):
    """极简单趟 HTML 解析：提取 title/meta/link/script(ld+json)/img/h1/a(nav,main,footer区分)/hreflang"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = None
        self._in_title = False
        self._title_buf = []
        self.meta_description = None
        self.canonical = None
        self.hreflangs = []  # list of (hreflang, href)
        self.og = {}
        self.ld_json_blocks = []
        self._in_ldjson = False
        self._ldjson_buf = []
        self.imgs = []  # list of dict(alt_present,width_present,height_present)
        self.h1_count = 0
        self._in_h1 = False
        self._h1_buf = []
        self.h1_texts = []
        self.links = []  # (href, in_nav, in_main, in_footer)
        self._nav_depth = 0
        self._main_depth = 0
        self._footer_depth = 0
        self._tag_stack = []
        self.has_robots_noindex = False
        self.lang_attr = None
        self.body_text = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        self._tag_stack.append(tag)
        if tag == "html" and "lang" in attrs_d:
            self.lang_attr = attrs_d["lang"]
        if tag in ("script", "style", "nav", "header", "footer", "aside", "head"):
            self._skip += 1
        if tag == "nav":
            self._nav_depth += 1
        if tag == "main":
            self._main_depth += 1
        if tag == "footer":
            self._footer_depth += 1
        if tag == "title":
            self._in_title = True
            self._title_buf = []
        if tag == "h1":
            self._in_h1 = True
            self._h1_buf = []
            self.h1_count += 1
        if tag == "meta":
            name = attrs_d.get("name", "").lower()
            prop = attrs_d.get("property", "").lower()
            content = attrs_d.get("content", "")
            if name == "description":
                self.meta_description = content
            if name == "robots" and "noindex" in content.lower():
                self.has_robots_noindex = True
            if prop.startswith("og:"):
                self.og[prop] = content
        if tag == "link":
            rel = attrs_d.get("rel", "").lower()
            if rel == "canonical":
                self.canonical = attrs_d.get("href")
            if rel == "alternate" and "hreflang" in attrs_d:
                self.hreflangs.append((attrs_d.get("hreflang"), attrs_d.get("href")))
        if tag == "script":
            typ = attrs_d.get("type", "")
            if typ == "application/ld+json":
                self._in_ldjson = True
                self._ldjson_buf = []
        if tag == "img":
            self.imgs.append(
                {
                    "alt": "alt" in attrs_d and attrs_d.get("alt") is not None,
                    "alt_empty": attrs_d.get("alt", None) == "",
                    "width": "width" in attrs_d,
                    "height": "height" in attrs_d,
                    "src": attrs_d.get("src", ""),
                }
            )
        if tag == "a":
            href = attrs_d.get("href")
            if href:
                self.links.append(
                    {
                        "href": href,
                        "in_nav": self._nav_depth > 0,
                        "in_main": self._main_depth > 0,
                        "in_footer": self._footer_depth > 0,
                    }
                )

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "header", "footer", "aside", "head") and self._skip > 0:
            self._skip -= 1
        if tag == "nav" and self._nav_depth > 0:
            self._nav_depth -= 1
        if tag == "main" and self._main_depth > 0:
            self._main_depth -= 1
        if tag == "footer" and self._footer_depth > 0:
            self._footer_depth -= 1
        if tag == "title":
            self._in_title = False
            self.title = "".join(self._title_buf)
        if tag == "h1":
            self._in_h1 = False
            self.h1_texts.append("".join(self._h1_buf).strip())
        if tag == "script" and self._in_ldjson:
            self._in_ldjson = False
            raw = "".join(self._ldjson_buf)
            try:
                data = json.loads(raw)
                self.ld_json_blocks.append(data)
            except Exception:
                self.ld_json_blocks.append({"__parse_error__": True, "raw_len": len(raw)})
        if self._tag_stack and self._tag_stack[-1] == tag:
            self._tag_stack.pop()

    def handle_data(self, data):
        if not self._skip and self._main_depth > 0:
            self.body_text.append(data)
        if self._in_title:
            self._title_buf.append(data)
        if self._in_h1:
            self._h1_buf.append(data)
        if self._in_ldjson:
            self._ldjson_buf.append(data)


def extract_ld_types(blocks):
    types = []
    for b in blocks:
        if isinstance(b, dict):
            if "__parse_error__" in b:
                continue
            t = b.get("@type")
            if isinstance(t, list):
                types.extend(t)
            elif t:
                types.append(t)
            # @graph 形式
            if "@graph" in b and isinstance(b["@graph"], list):
                for g in b["@graph"]:
                    if isinstance(g, dict):
                        gt = g.get("@type")
                        if isinstance(gt, list):
                            types.extend(gt)
                        elif gt:
                            types.append(gt)
        elif isinstance(b, list):
            for item in b:
                if isinstance(item, dict):
                    t = item.get("@type")
                    if isinstance(t, list):
                        types.extend(t)
                    elif t:
                        types.append(t)
    return types


def audit_site(name, cfg):
    root = cfg["html_root"]
    files = find_html_files(root)
    pages = {}
    parse_errors = []
    for f in files:
        upath = url_path_for(root, f)
        try:
            html = open(f, encoding="utf-8", errors="replace").read()
        except Exception as e:
            parse_errors.append((f, str(e)))
            continue
        p = PageParser()
        try:
            p.feed(html)
        except Exception as e:
            parse_errors.append((f, str(e)))
            continue
        pages[upath] = {"parser": p, "file": f, "html_len": len(html)}

    result = {"site": name, "page_count": len(pages), "parse_errors": parse_errors}

    # ---- 1. title 长度分布 + 重复
    title_lens = {"<30": 0, "30-60": 0, ">60": 0, "missing": 0}
    titles = []
    for upath, d in pages.items():
        t = d["parser"].title
        if not t:
            title_lens["missing"] += 1
            continue
        tl = display_len(t.strip())
        titles.append((upath, t.strip()))
        if tl < 30:
            title_lens["<30"] += 1
        elif tl <= 60:
            title_lens["30-60"] += 1
        else:
            title_lens[">60"] += 1
    title_counter = Counter(t for _, t in titles)
    dup_titles = {t: c for t, c in title_counter.items() if c > 1}
    dup_title_pages = sum(c for c in dup_titles.values())
    result["title"] = {
        "len_dist": title_lens,
        "dup_title_groups": len(dup_titles),
        "dup_title_pages": dup_title_pages,
        "dup_title_samples": dict(list(dup_titles.items())[:10]),
    }

    # ---- 2. meta description
    desc_missing = 0
    desc_too_long = 0
    desc_too_short = 0
    descs = []
    for upath, d in pages.items():
        desc = d["parser"].meta_description
        if not desc or not desc.strip():
            desc_missing += 1
            continue
        descs.append((upath, desc.strip()))
        if display_len(desc.strip()) > 160:
            desc_too_long += 1
        if display_len(desc.strip()) < 70:
            desc_too_short += 1
    desc_counter = Counter(dd for _, dd in descs)
    dup_desc = {dd: c for dd, c in desc_counter.items() if c > 1}
    result["description"] = {
        "missing": desc_missing,
        "too_long_gt160": desc_too_long,
        "too_short_lt70": desc_too_short,
        "dup_desc_groups": len(dup_desc),
        "dup_desc_pages": sum(c for c in dup_desc.values()),
        "dup_desc_samples": dict(list(dup_desc.items())[:5]),
    }

    # ---- 3. canonical
    canon_missing = 0
    canon_mismatch = 0
    mismatch_samples = []
    base_url = cfg.get("base_url")
    for upath, d in pages.items():
        c = d["parser"].canonical
        if not c:
            canon_missing += 1
            continue
        parsed = urlparse(c)
        cpath = parsed.path
        if cpath != "" and not cpath.endswith("/") and "." not in os.path.basename(cpath):
            cpath = cpath + "/"
        # 比较路径部分（忽略 trailing slash 细微差异）
        norm_c = cpath.rstrip("/") or "/"
        norm_u = upath.rstrip("/") or "/"
        if norm_c != norm_u:
            canon_mismatch += 1
            if len(mismatch_samples) < 10:
                mismatch_samples.append({"page": upath, "canonical": c})
    result["canonical"] = {
        "missing": canon_missing,
        "mismatch": canon_mismatch,
        "mismatch_samples": mismatch_samples,
    }

    # ---- 4. JSON-LD
    ld_type_pages = defaultdict(set)
    no_ldjson = 0
    parse_error_pages = 0
    for upath, d in pages.items():
        blocks = d["parser"].ld_json_blocks
        if not blocks:
            no_ldjson += 1
            continue
        if any(isinstance(b, dict) and b.get("__parse_error__") for b in blocks):
            parse_error_pages += 1
        types = extract_ld_types(blocks)
        for t in types:
            ld_type_pages[t].add(upath)
    result["jsonld"] = {
        "no_jsonld_pages": no_ldjson,
        "parse_error_pages": parse_error_pages,
        "type_coverage": {t: len(s) for t, s in sorted(ld_type_pages.items(), key=lambda x: -len(x[1]))},
    }

    # ---- 5. Open Graph
    og_missing = {"og:title": 0, "og:description": 0, "og:image": 0}
    og_image_paths = []
    for upath, d in pages.items():
        og = d["parser"].og
        for k in og_missing:
            if k not in og or not og[k]:
                og_missing[k] += 1
        if og.get("og:image"):
            og_image_paths.append((upath, og["og:image"]))
    # 检查 og:image 文件是否存在
    pub_root = cfg["public_root"]
    og_image_missing_file = []
    og_external = 0
    own_host = urlparse(cfg.get("base_url") or "").netloc
    for upath, img in og_image_paths:
        parsed = urlparse(img)
        ipath = parsed.path
        if parsed.netloc and own_host and parsed.netloc != own_host:
            og_external += 1  # 外部热链(官方 CDN):不是本站产物文件,不按本地文件查
            continue
        if parsed.netloc:  # 绝对 URL，检查其 path 对应本地文件
            local = os.path.join(pub_root, ipath.lstrip("/"))
        else:
            local = os.path.join(pub_root, ipath.lstrip("/"))
        if not os.path.isfile(local):
            og_image_missing_file.append({"page": upath, "og_image": img})
    result["opengraph"] = {
        "missing": og_missing,
        "og_image_file_missing": len(og_image_missing_file),
        "og_image_external": og_external,
        "og_image_file_missing_samples": og_image_missing_file[:10],
    }

    # ---- 6. hreflang（仅 multilang 站点）
    if cfg.get("multilang"):
        hreflang_report = audit_hreflang(pages, name)
        result["hreflang"] = hreflang_report
    else:
        result["hreflang"] = {"note": "非多语种站，跳过"}

    # ---- 7. img alt / width / height
    img_total = 0
    img_no_alt = 0
    img_no_wh = 0
    for upath, d in pages.items():
        for img in d["parser"].imgs:
            img_total += 1
            if not img["alt"]:
                img_no_alt += 1
            if not (img["width"] and img["height"]):
                img_no_wh += 1
    result["images"] = {"total_img_tags": img_total, "missing_alt": img_no_alt, "missing_width_or_height": img_no_wh}

    # ---- 8. h1
    h1_missing = 0
    h1_multi = 0
    for upath, d in pages.items():
        c = d["parser"].h1_count
        if c == 0:
            h1_missing += 1
        elif c > 1:
            h1_multi += 1
    result["h1"] = {"missing": h1_missing, "multiple": h1_multi}

    # ---- 8b. 正文词数(CJK 折算)
    wc = {u: word_count(" ".join(d["parser"].body_text)) for u, d in pages.items()}
    if wc:
        vals = sorted(wc.values())
        result["word_count"] = {
            "min": vals[0], "median": vals[len(vals) // 2], "max": vals[-1],
            "thin_lt800": sum(1 for v in vals if v < 800),
            "thin_samples": sorted(((v, u) for u, v in wc.items() if v < 800))[:15],
        }

    # ---- 9. 内链统计（排除 nav/footer，只算 in_main 或者两者都不在时的正文链接）
    internal_counts, inbound_counts, orphan_slugs = compute_internal_links(pages, root, name)
    if internal_counts:
        sorted_counts = sorted(internal_counts.values())
        n = len(sorted_counts)
        median = sorted_counts[n // 2] if n % 2 == 1 else (sorted_counts[n // 2 - 1] + sorted_counts[n // 2]) / 2
        result["internal_links"] = {
            "outbound_min": min(sorted_counts),
            "outbound_median": median,
            "outbound_max": max(sorted_counts),
            "orphan_or_low_inbound_pages": len(orphan_slugs),
            "orphan_or_low_inbound_samples": orphan_slugs[:30],
        }
    else:
        result["internal_links"] = {"note": "未获取：解析失败或无正文链接"}

    # ---- 10. robots.txt / sitemap.xml
    result["robots_sitemap"] = audit_robots_sitemap(cfg, pages)

    # ---- 11. 404 / trust pages
    has_404 = os.path.isfile(os.path.join(root, "404.html")) or os.path.isfile(os.path.join(root, "404", "index.html"))
    trust_found = {}
    all_paths_lower = set(p.lower() for p in pages.keys())
    for tp in TRUST_PAGES:
        found = any(tp in p.lower() for p in all_paths_lower)
        trust_found[tp] = found
    result["error_trust_pages"] = {"has_404": has_404, "trust_pages": trust_found}

    return result, pages


def audit_hreflang(pages, sitename):
    """检查互指完整性与 x-default"""
    # 建 slug -> {lang: path}
    groups = defaultdict(dict)
    for upath in pages:
        # Beast: /en/slug or /de/slug ; lootlore: /beast-of-reincarnation/en/slug
        parts = [p for p in upath.split("/") if p]
        if not parts:
            continue
        if sitename == "Beast-of-Reincarnation":
            if len(parts) >= 1 and parts[0] in ("en", "de", "es", "fr", "it", "ja"):
                lang = parts[0]
                slug = "/".join(parts[1:]) or "index"
                groups[slug][lang] = upath
        elif sitename == "lootlore":
            if len(parts) >= 2 and parts[0] == "beast-of-reincarnation" and parts[1] in ("en", "de", "es", "fr", "it", "ja"):
                lang = parts[1]
                slug = "/".join(parts[2:]) or "index"
                groups[slug][lang] = upath

    missing_reciprocal = []
    missing_xdefault = 0
    checked = 0
    langs_all = set()
    for slug, langmap in groups.items():
        for lang, upath in langmap.items():
            langs_all.add(lang)
    for slug, langmap in groups.items():
        for lang, upath in langmap.items():
            checked += 1
            p = pages[upath]["parser"]
            declared_langs = set(h for h, href in p.hreflangs)
            has_xdefault = "x-default" in declared_langs
            if not has_xdefault:
                missing_xdefault += 1
            expected = set(langmap.keys())
            got = declared_langs - {"x-default"}
            if got != expected:
                if len(missing_reciprocal) < 15:
                    missing_reciprocal.append(
                        {"page": upath, "expected_langs": sorted(expected), "declared_langs": sorted(got)}
                    )

    return {
        "slug_groups": len(groups),
        "pages_checked": checked,
        "langs_found": sorted(langs_all),
        "missing_xdefault_pages": missing_xdefault,
        "reciprocal_mismatch_pages": len(missing_reciprocal),
        "reciprocal_mismatch_samples": missing_reciprocal,
    }


def compute_internal_links(pages, root, sitename):
    """统计每页正文内链数（排除 nav/footer）与每个页面的入链数"""
    all_slugs = set(pages.keys())
    outbound = {}
    inbound = Counter()
    for upath, d in pages.items():
        p = d["parser"]
        main_links = set()
        for l in p.links:
            href = l["href"]
            if l["in_nav"] or l["in_footer"]:
                continue
            if href.startswith("http://") or href.startswith("https://"):
                continue
            if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
                continue
            # normalize
            hpath = href.split("#")[0].split("?")[0]
            if not hpath:
                continue
            if not hpath.endswith("/") and "." not in os.path.basename(hpath):
                hpath = hpath + "/"
            main_links.add(hpath)
        outbound[upath] = len(main_links)
        for hp in main_links:
            norm = hp.rstrip("/") or "/"
            inbound[norm] += 1

    orphans = []
    for upath in pages:
        norm = upath.rstrip("/") or "/"
        cnt = inbound.get(norm, 0)
        if cnt <= 1:
            orphans.append({"page": upath, "inbound": cnt})
    orphans.sort(key=lambda x: x["inbound"])
    return outbound, inbound, orphans


def audit_robots_sitemap(cfg, pages):
    root = cfg["html_root"]
    pub_root = cfg["public_root"]
    result = {}
    robots_path_candidates = [os.path.join(pub_root, "robots.txt")]
    sitemap_path_candidates = [os.path.join(pub_root, "sitemap.xml")]
    robots_exists = any(os.path.isfile(p) for p in robots_path_candidates)
    sitemap_exists = any(os.path.isfile(p) for p in sitemap_path_candidates)
    result["robots_txt_exists"] = robots_exists
    result["sitemap_xml_exists"] = sitemap_exists

    sitemap_urls = []
    if sitemap_exists:
        sp = next(p for p in sitemap_path_candidates if os.path.isfile(p))
        content = open(sp, encoding="utf-8", errors="replace").read()
        sitemap_urls = re.findall(r"<loc>(.*?)</loc>", content)
    result["sitemap_url_count"] = len(sitemap_urls)
    result["actual_page_count"] = len(pages)
    result["sitemap_vs_actual_diff"] = len(sitemap_urls) - len(pages)

    # 检查 sitemap 中是否有 noindex 页
    noindex_in_sitemap = []
    url_to_path = {}
    for u in sitemap_urls:
        parsed = urlparse(u)
        p = parsed.path
        if p and not p.endswith("/") and "." not in os.path.basename(p):
            p = p + "/"
        norm = p.rstrip("/") or "/"
        url_to_path[u] = norm

    for u, norm in url_to_path.items():
        page = pages.get(norm) or pages.get(norm + "/")
        if page is None:
            # 尝试模糊匹配
            for cand in pages:
                if cand.rstrip("/") == norm:
                    page = pages[cand]
                    break
        if page is not None:
            if page["parser"].has_robots_noindex:
                noindex_in_sitemap.append(u)
    result["noindex_pages_in_sitemap"] = len(noindex_in_sitemap)
    result["noindex_in_sitemap_samples"] = noindex_in_sitemap[:10]

    return result


def main_cli(argv):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--base", default=None)
    ap.add_argument("--prefix", default="", help="只统计该路径前缀下的页(如 /<game>/)")
    ap.add_argument("--summary", action="store_true", help="打印精简摘要而不是整份 JSON")
    a = ap.parse_args(argv)
    root = os.path.abspath(a.out)
    cfg = {"html_root": root, "base_url": a.base, "multilang": True, "public_root": root}
    global find_html_files
    if a.prefix:
        _all = find_html_files
        # 内链/入链需要全站页面,先按全站解析,再只保留前缀子树参与统计
        def find_html_files(r):
            return [f for f in _all(r) if url_path_for(r, f).startswith(a.prefix)]
        # 入链统计用全站页面:把全站页面的链接计入
        full = {}
        for f in _all(root):
            p = PageParser()
            try:
                p.feed(open(f, encoding="utf-8", errors="replace").read())
            except Exception:
                continue
            full[url_path_for(root, f)] = {"parser": p, "file": f, "html_len": 0}
        _cil = globals()["compute_internal_links"]
        def compute_internal_links_prefixed(pages, r, name):
            out, inbound, _ = _cil(full, r, name)
            out = {u: v for u, v in out.items() if u in pages}
            orphans = sorted(({"page": u, "inbound": inbound.get(u.rstrip("/") or "/", 0)} for u in pages
                              if inbound.get(u.rstrip("/") or "/", 0) <= 1), key=lambda x: x["inbound"])
            return out, inbound, orphans
        globals()["compute_internal_links"] = compute_internal_links_prefixed
    res, pages = audit_site("lootlore" + (a.prefix.rstrip("/") if a.prefix else ""), cfg)
    if not a.summary:
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return
    print(f"tech_audit {a.prefix or '/'}: {res['page_count']} 页(只报告,不阻塞)")
    print(f"  title(显示宽度) {res['title']['len_dist']} · 重复组 {res['title']['dup_title_groups']}")
    d = res["description"]
    print(f"  description 缺 {d['missing']} · >160 {d['too_long_gt160']} · <70 {d['too_short_lt70']} · 重复组 {d['dup_desc_groups']}")
    c = res["canonical"]
    print(f"  canonical 缺 {c['missing']} · 路径不符 {c['mismatch']}")
    j = res["jsonld"]
    print(f"  JSON-LD 无 {j['no_jsonld_pages']} · 解析失败 {j['parse_error_pages']} · 类型 {j['type_coverage']}")
    o = res["opengraph"]
    print(f"  OG 缺 {o['missing']} · og:image 本地文件缺 {o['og_image_file_missing']} · 外部热链 {o['og_image_external']}")
    print(f"  img {res['images']} · h1 {res['h1']}")
    w = res.get("word_count", {})
    print(f"  词数(CJK/2) min {w.get('min')} · 中位 {w.get('median')} · max {w.get('max')} · <800 {w.get('thin_lt800')}")
    il = res["internal_links"]
    print(f"  正文内链 min {il.get('outbound_min')} · 中位 {il.get('outbound_median')} · 入链≤1 {il.get('orphan_or_low_inbound_pages')}")
    rs = res["robots_sitemap"]
    print(f"  robots {rs['robots_txt_exists']} · sitemap {rs['sitemap_xml_exists']} · sitemap 内 noindex {rs['noindex_pages_in_sitemap']}")


def main():
    if len(sys.argv) > 1:
        return main_cli(sys.argv[1:])
    all_results = {}
    for name, cfg in SITES.items():
        if not os.path.isdir(cfg["html_root"]):
            all_results[name] = {"error": f"未获取：目录不存在 {cfg['html_root']}"}
            continue
        try:
            res, pages = audit_site(name, cfg)
            all_results[name] = res
        except Exception as e:
            import traceback

            all_results[name] = {"error": f"未获取：脚本异常 {e}", "traceback": traceback.format_exc()}
    print(json.dumps(all_results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
