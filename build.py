#!/usr/bin/env python3
"""Guide Atlas hub assembler.

三层分离:
  框架层 = 本脚本 + hub/ 壳(总站页面模板与样式)+ hub/native.py、hub/mdlite.py(原生内容渲染)
           + hub/snapshot.py(快照游戏套壳:正文沿用子站产出,外壳统一)
  配置层 = config/hub.json(品牌、base_url、游戏清单、剥离/映射规则)+ config/i18n/<lang>.json(界面文字)
  内容层 = sources/<game>/(各子站静态快照,原样不改,变换只发生在 out/)
           content/<game>/*.md(kind=native 的游戏:Markdown 即真相源,构建时渲染)
           data/<game>/entities.json(可选;有就渲染右栏实体速查框,没有就不渲染)

用法:  python3 build.py            # 组装到 out/
       python3 build.py --base https://xxx.vercel.app   # 覆盖 base_url
"""
import hashlib, json, re, shutil, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from hub import shell  # noqa: E402
from hub.mdlite import esc  # noqa: E402
from hub.native import NativeGame  # noqa: E402
from hub.pageindex import SiteIndex  # noqa: E402
from hub.snapshot import SnapshotGame  # noqa: E402
CFG = json.loads((ROOT / "config" / "hub.json").read_text())
if "--base" in sys.argv:
    CFG["base_url"] = sys.argv[sys.argv.index("--base") + 1].rstrip("/")
BASE = CFG["base_url"].rstrip("/")
# 旧 Vercel 预览域名:换正式域名后仍要把它 301/308 到新域名,防止旧外链/书签/历史索引失效。
# 写死而不派生自 CFG——base_url 换了之后这个值还得继续指向"曾经用过的" vercel.app 子域,
# 不能跟着 base_url 一起变(否则规则形同虚设)。base_url 万一又指回它本身,下面的 gen_vercel_json
# 会跳过这条规则,不然会把新域名自己也 301 掉,造成跳转环。
LEGACY_VERCEL_HOST = "lootlore-ten.vercel.app"
OUT = ROOT / "out"
TODAY = datetime.date.today().isoformat()
SENT = "@@HUB@@"  # 信任页映射后的哨兵前缀,防止被通用子路径改写二次加前缀
LASTMOD = {}  # route -> lastmod(原生内容页按 reviewed ?? updated ?? date;其余页用构建日)
T = json.loads((ROOT / "config" / "i18n" / "en.json").read_text())  # 总站界面文字(英文默认)
INDEX = SiteIndex()  # 全站索引:页清单 / 栏目 / 更新日,全部从真实文件统计


def nav_games():
    """一级导航第一栏(实体型):6 个游戏 + 缩略图,数据全来自配置层的 card。"""
    rows = []
    for g in CFG["games"]:
        c = g.get("card", {})
        rows.append({"slug": g["slug"], "label": g["short"], "href": game_home(g),
                     "thumb": c.get("img", ""), "thumb_alt": c.get("img_alt", ""),
                     "genre": c.get("genre", "")})
    return rows


def nav_intents():
    """一级导航第二栏(意图型):label 是 i18n key,链接在配置层。"""
    return [(T[k], h) for k, h in CFG.get("intent_nav", [])]


def font_links():
    css = CFG.get("font_css")
    if not css:
        return ""
    return ('<link rel="preconnect" href="https://fonts.googleapis.com">'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            f'<link rel="stylesheet" href="{esc(css)}">')


def is_native(g: dict) -> bool:
    return g.get("kind") == "native"


def game_home(g: dict) -> str:
    return f'/{g["slug"]}{g.get("default_path", "/").rstrip("/") or "/"}'

# ---------------- 剥离规则(按站点快照实测的三方脚本形态写的正则) ----------------
STRIP_PATTERNS = [
    # GA4: 注释行 + 外链 gtag.js + 内联 dataLayer 配置块
    re.compile(r"<!--\s*Google (?:Analytics|tag)[^>]*-->\s*", re.I),
    re.compile(r'<script async src="https://www\.googletagmanager\.com/gtag/js[^"]*"></script>\s*'),
    re.compile(r"<script>\s*window\.dataLayer\s*=\s*window\.dataLayer.*?</script>\s*", re.S),
    # Microsoft Clarity: 注释 + IIFE
    re.compile(r"<!--\s*Microsoft Clarity[^>]*-->\s*", re.I),
    re.compile(r'<script type="text/javascript">\s*\(function\(c,l,a,r,i,t,y\).*?</script>\s*', re.S),
    # Adsterra 装载器引用(hub 暂不接 Adsterra,接的时候由 hub 统一注入)
    re.compile(r'<script[^>]*src="/ads\.js"[^>]*>\s*</script>\s*'),
    # Next.js 静态导出的运行时(三个 Next 站):不剥离则 React 水合会用 RSC payload 里的原站路径覆盖已改写的链接
    re.compile(r'<script src="/_next/static/chunks/[^"]*"[^>]*></script>'),
    re.compile(r'<script>\(self\.__next_f.*?</script>', re.S),
    re.compile(r'<script>self\.__next_f\.push.*?</script>', re.S),
    re.compile(r'<link rel="preload"[^>]*href="/_next/static/chunks/[^"]*"[^>]*/?>\s*'),
    # 对已剥离服务的预连接
    re.compile(r'<link rel="(?:preconnect|dns-prefetch)" href="https://(?:www\.googletagmanager\.com|www\.clarity\.ms)"[^>]*>\s*'),
]

ATTR_RE = re.compile(r'((?:href|src|content|action|poster|data-src)=")(/[^"]*)(")')
# 单引号属性:子站内联脚本里拼出来的链接(如 tools 页 innerHTML 里的 href='/endings/')
# 也要加子路径前缀,否则在总站是死链。
ATTR_SQ_RE = re.compile(r"((?:href|src|content|action|poster|data-src)=')(/[^']*)(')")
# srcset / srcSet / imageSrcSet:三个 Next 站的静态导出用的是 React 的驼峰写法,
# 大小写不敏感地匹配,否则子站的 /images/... 候选图在总站是 404(首屏大图直接空)。
SRCSET_RE = re.compile(r'((?:image)?srcset=")([^"]*)(")', re.I)


def load(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def hub_ga_snippet() -> str:
    gid = CFG.get("ga4_id", "")
    if not gid:
        return ""
    return (
        f'<script async src="https://www.googletagmanager.com/gtag/js?id={gid}"></script>\n'
        "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
        f"gtag('js',new Date());gtag('config','{gid}');</script>\n"
    )


def transform_urls(html: str, game: dict) -> str:
    """把一个子站快照页的链接改写到总站:剥三方脚本 → 原站域名换成总站域名 + 子路径 →
    信任页链接指到总站信任页 → 其余根相对链接加 /<slug> 前缀。

    只改链接,不碰正文文字,也不再注入任何外壳 —— 外壳由 hub/snapshot.py 重新渲染。
    套壳前先做这一步,所以 head 元数据与正文里的链接进外壳时已经是总站 URL,不需要二次改写。"""
    slug = game["slug"]
    origin = game["origin"].rstrip("/")
    host = origin.split("//", 1)[1]

    for pat in STRIP_PATTERNS:
        html = pat.sub("", html)

    # 绝对地址:原站域名 → 总站域名 + 子路径(canonical/og/hreflang/JSON-LD 一次全对)
    html = html.replace(origin, f"{BASE}/{slug}")
    html = html.replace(host, f"{BASE.split('//',1)[1]}/{slug}")

    # 信任页链接 → 总站信任页(打哨兵,防止后面被加子路径前缀)
    for src, dst in sorted(game["trust_map"].items(), key=lambda kv: -len(kv[0])):
        html = html.replace(f'href="{src}"', f'href="{SENT}{dst}"')
        html = html.replace(f"href='{src}'", f"href='{SENT}{dst}'")

    # 其余根相对链接 → 加 /<slug> 前缀
    def prefix(m):
        return f"{m.group(1)}/{slug}{m.group(2)}{m.group(3)}"

    html = ATTR_RE.sub(lambda m: m.group(0) if m.group(2).startswith(f"{SENT}") else prefix(m), html)
    html = ATTR_SQ_RE.sub(lambda m: m.group(0) if m.group(2).startswith(f"{SENT}") else prefix(m), html)

    def fix_srcset(m):
        parts = [p.strip() for p in m.group(2).split(",")]
        parts = [(f"/{slug}" + p) if p.startswith("/") else p for p in parts]
        return m.group(1) + ", ".join(parts) + m.group(3)

    html = SRCSET_RE.sub(fix_srcset, html)
    return html.replace(SENT, "")


def render_snapshot_games(site):
    """快照游戏:正文沿用子站产出,外壳换成 hub 统一外壳(与 /valheim/ 同一套)。"""
    stats = []
    for g in CFG["games"]:
        if is_native(g):
            continue
        sg = SnapshotGame(ROOT, g, CFG, site)
        assets = sg.copy_assets(OUT)
        LASTMOD.update(sg.build(OUT, transform_urls))
        INDEX.add(sg.index())
        s = sg.stats
        print(f"  [{g['slug']}] snapshot: {s['langs']} 语种 · {s['pages']} 页 · "
              f"{s['sections']} 个栏目 · 实体信息框 {s['entity_boxes']} 页 · 资源 {assets} 个")
        stats.append((g["slug"], s))
    shutil.copy2(ROOT / "hub" / "snapshot.css", OUT / "snapshot.css")
    return stats


def hero_game() -> dict:
    """首页 hero / og:image 用哪个游戏的官方截图:配置层一处开关。"""
    slug = CFG.get("hero_game") or CFG["games"][0]["slug"]
    return next(g for g in CFG["games"] if g["slug"] == slug)


def og_image_snippet() -> str:
    c = hero_game()["card"]
    return (f'<meta property="og:image" content="{esc(c["img"])}">\n'
            f'<meta property="og:image:width" content="{c["img_w"]}">\n'
            f'<meta property="og:image:height" content="{c["img_h"]}">\n'
            f'<meta property="og:image:alt" content="{esc(c["img_alt"])}">')


def breadcrumb_ld(base: str, brand: str, crumbs: list) -> dict:
    """crumbs: [(name, path_or_None)] 最后一项通常是当前页(path=None 时不设 item,允许作最终节点省略)"""
    items = []
    for i, (label, path) in enumerate(crumbs, start=1):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if path is not None:
            entry["item"] = f"{base}{path}"
        items.append(entry)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def hub_jsonld(name: str, cfg: dict) -> str:
    base = cfg["base_url"].rstrip("/")
    brand = cfg["brand"]
    email = cfg["contact_email"]
    graphs = []

    if name == "index":
        graphs.append({
            "@context": "https://schema.org", "@type": "WebSite",
            "name": brand, "url": f"{base}/",
            "description": cfg["tagline"],
            "potentialAction": {
                "@type": "SearchAction",
                "target": f"{base}/?q={{search_term_string}}",
                "query-input": "required name=search_term_string",
            },
        })
        graphs.append({
            "@context": "https://schema.org", "@type": "Organization",
            "name": brand, "url": f"{base}/",
            "logo": f"{base}/favicon.svg",
            "email": email,
        })
        graphs.append(breadcrumb_ld(base, brand, [(brand, None)]))
    elif name == "about":
        graphs.append({
            "@context": "https://schema.org", "@type": "AboutPage",
            "name": f"About {brand}", "url": f"{base}/about",
            "isPartOf": {"@type": "WebSite", "name": brand, "url": f"{base}/"},
        })
        graphs.append(breadcrumb_ld(base, brand, [(brand, "/"), ("About", None)]))
    elif name == "contact":
        graphs.append({
            "@context": "https://schema.org", "@type": "ContactPage",
            "name": f"Contact {brand}", "url": f"{base}/contact",
            "isPartOf": {"@type": "WebSite", "name": brand, "url": f"{base}/"},
        })
        graphs.append(breadcrumb_ld(base, brand, [(brand, "/"), ("Contact", None)]))
    elif name in ("guides", "reviews", "updates", "tools"):
        label = {"guides": "Guides", "reviews": "Reviews", "updates": "Updates",
                 "tools": "Tools"}[name]
        graphs.append({
            "@context": "https://schema.org", "@type": "CollectionPage",
            "name": label, "url": f"{base}/{name}",
            "isPartOf": {"@type": "WebSite", "name": brand, "url": f"{base}/"},
        })
        graphs.append(breadcrumb_ld(base, brand, [(brand, "/"), (label, None)]))
    elif name == "404":
        graphs.append({
            "@context": "https://schema.org", "@type": "WebPage",
            "name": "Page Not Found", "url": f"{base}/404",
            "isPartOf": {"@type": "WebSite", "name": brand, "url": f"{base}/"},
        })
    else:
        labels = {
            "terms": "Terms of Use", "privacy-policy": "Privacy Policy",
            "disclaimer": "Disclaimer", "editorial-policy": "Editorial Policy",
        }
        label = labels.get(name, name.replace("-", " ").title())
        graphs.append({
            "@context": "https://schema.org", "@type": "WebPage",
            "name": label, "url": f"{base}/{name}",
            "isPartOf": {"@type": "WebSite", "name": brand, "url": f"{base}/"},
        })
        graphs.append(breadcrumb_ld(base, brand, [(brand, "/"), (label, None)]))

    return "\n".join(f'<script type="application/ld+json">{json.dumps(g, ensure_ascii=False)}</script>' for g in graphs)


NUM_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}


def render_native_games(site):
    """原生内容游戏(目前 /valheim/):渲染页面并把索引回填进全站索引。"""
    for g in CFG["games"]:
        if not is_native(g):
            continue
        ng = NativeGame(ROOT, g, CFG, site)
        LASTMOD.update(ng.build(OUT))
        INDEX.add(ng.index())
    shutil.copy2(ROOT / "hub" / "native.css", OUT / "native.css")


def write_hub_css():
    """out/hub.css = 配置层的 token(:root)+ 框架层的样式表。改主题只动 config/hub.json。"""
    tokens = ";".join(f"--{k}:{v}" for k, v in CFG["theme"].items())
    css = (f"/* tokens: config/hub.json -> theme (build-time) */\n:root{{{tokens}}}\n\n"
           + load(ROOT / "hub" / "style.css"))
    (OUT / "hub.css").write_text(css, encoding="utf-8")


# ---------------------------------------------------------------- 首页 / 索引模块
def hero_html(meta):
    c = hero_game()["card"]
    return (
        '<section class="hero"><div class="hero-in">'
        f'<figure class="hero-fig"><img src="{esc(c["img"])}" width="{c["img_w"]}" height="{c["img_h"]}"'
        f' alt="{esc(c["img_alt"])}" loading="eager" fetchpriority="high" decoding="async"></figure>'
        '<div class="hero-c">'
        f'<p class="kicker">{esc(meta["kicker"])}</p>'
        f'<h1>{esc(meta["h1"])}</h1>'
        f'<p class="lede">{esc(meta["lede"])}</p>'
        '<div class="hero-cta">'
        f'<a href="#games">{esc(T["hub_games_heading"])} &darr;</a>'
        f'<a href="/updates">{esc(T["nav_updates"])}</a></div>'
        f'</div><p class="hero-credit">{esc(c["img_credit"])}</p>'
        "</div></section>")


def game_cards_html():
    """首页游戏卡片网格。页数与更新日来自全站索引的实际统计,没有数据的项不显示。"""
    out = []
    for gi in INDEX.games:
        g = next(x for x in CFG["games"] if x["slug"] == gi.slug)
        c = gi.card
        hls = [(t, u) for t, u in c["highlights"]
               if (OUT / u.strip("/") / "index.html").is_file() or (OUT / (u.strip("/") + ".html")).is_file()]
        hi = "".join(f'<a class="hl" href="{esc(u)}">{esc(t)}</a>' for t, u in hls)
        stats = [f'<b>{gi.page_count}</b> {esc(T["pages_count"].format(n="").strip())}']
        if gi.updated:
            stats.append(f'<time datetime="{gi.updated}">{esc(T["updated_on"].format(d=gi.updated))}</time>')
        lang_attr = ' lang="en"'
        out.append(
            f'<li class="gcard" id="{esc(gi.slug)}">'
            f'<a class="shot" href="{esc(gi.home_route)}" tabindex="-1" aria-hidden="true">'
            f'<img src="{esc(c["img"])}" alt="{esc(c["img_alt"])}" width="{c["img_w"]}"'
            f' height="{c["img_h"]}" loading="lazy" decoding="async"></a>'
            f'<div class="b"><p class="genre">{esc(c["genre"])}</p>'
            f'<h3><a href="{esc(gi.home_route)}">{esc(gi.name)}</a></h3>'
            f'<p class="meta">{esc(c["studio"])} &middot; Released {esc(c["released"])}<br>{esc(c["platforms"])}</p>'
            f'<p class="blurb">{esc(c["blurb"])}</p>'
            f'<div class="hls">{hi}</div>'
            f'<p class="stats">{" &middot; ".join(stats)} &middot; <span{lang_attr}>{esc(c["langs"])}</span></p>'
            f'<p class="credit">{esc(c["img_credit"])}</p></div></li>')
    return f'<ul class="gcards">{"".join(out)}</ul>'


def feed_html(rows):
    """最近更新列表。rows = PageRef;日期是页面自己记录的复核日,没有日期的页不进来。"""
    by_slug = {g.slug: g for g in INDEX.games}
    lis = []
    for p in rows:
        g = by_slug.get(p.game)
        lis.append(f'<li><time datetime="{esc(p.date)}">{esc(p.date)}</time>'
                   f'<a href="{esc(p.route)}">{esc(p.title)}</a>'
                   f'<span class="g">{esc(g.short if g else p.game)}</span></li>')
    return f'<ul class="feed">{"".join(lis)}</ul>'


def all_guides_html():
    """全量攻略索引:游戏 → 栏目 → 页。整份由 hub/pageindex.py 从真实文件发现。"""
    out = []
    for gi in INDEX.games:
        meta = [T["pages_count"].format(n=gi.page_count)]
        if gi.updated:
            meta.append(T["updated_on"].format(d=gi.updated))
        secs = []
        for s in gi.sections:
            links = "".join(f'<li><a href="{esc(p.route)}">{esc(p.title)}</a></li>' for p in s.pages)
            head = (f'<a href="{esc(s.route)}">{esc(s.label)}</a>' if s.route else esc(s.label))
            secs.append(f'<div class="index-s"><p>{head}</p><ul class="linklist">{links}</ul></div>')
        out.append(f'<div class="index-g"><h3><a href="{esc(gi.home_route)}">{esc(gi.name)}</a></h3>'
                   f'<p>{" &middot; ".join(esc(x) for x in meta)}</p>'
                   + "".join(secs) + "</div>")
    return "".join(out)


def clip(text, n):
    """按词边界截断,超了才加省略号 —— 不在词中间断开。"""
    t = " ".join((text or "").split())
    if len(t) <= n:
        return t
    cut = t[:n].rsplit(" ", 1)[0]
    return cut.rstrip(",.;:—-") + "\u2026"


def tools_html():
    """/tools/ 页:按配置的关键词匹配真实存在的互动工具页。匹配不到就构建失败,不出空页。"""
    keys = [k.lower() for k in CFG.get("tools_match", [])]
    out, total = [], 0
    for gi in INDEX.games:
        hit = [p for p in gi.pages if p.lang == "en"
               and any(k in p.title.lower() for k in keys)]
        if not hit:
            continue
        total += len(hit)
        lis = "".join(f'<li><a href="{esc(p.route)}">{esc(p.title)}</a>'
                      + (f"<span>{esc(clip(p.description, 150))}</span>" if p.description else "")
                      + "</li>" for p in sorted(hit, key=lambda x: x.title))
        out.append(f'<div class="index-g"><h3><a href="{esc(gi.home_route)}">{esc(gi.name)}</a></h3>'
                   f'<ul class="toollist">{lis}</ul></div>')
    if not total:
        raise SystemExit("tools: 没有匹配到任何工具页,请改 config/hub.json 的 tools_match 或删掉 /tools 入口")
    return "".join(out)


def updates_stats_html():
    dated = [p for g in INDEX.games for p in g.pages if p.date and p.lang == "en"]
    newest = max(p.date for p in dated) if dated else ""
    line = (f"{len(dated)} English guide pages across {len(INDEX.games)} games carry a recorded "
            f"review date; the most recent revision is")
    return (f'<p class="sub">{line} <strong><time datetime="{newest}">{newest}</time></strong>.</p>'
            if newest else "")


# ---------------------------------------------------------------- 总站自有页面
META_RE = re.compile(r"^<!--\n(.*?)\n-->\n", re.S)


def page_meta(text):
    m = META_RE.match(text)
    if not m:
        raise SystemExit("hub/pages: 片段缺少 <!-- title/description/path/h1 --> 头")
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    return meta, text[m.end():]


def fill(s: str) -> str:
    names = [g["name"] for g in CFG["games"]]
    n = len(names)
    s = s.replace("{{BASE}}", BASE).replace("{{BRAND}}", CFG["brand"])
    s = s.replace("{{TAGLINE}}", CFG["tagline"]).replace("{{EMAIL}}", CFG["contact_email"])
    s = s.replace("{{PUB}}", CFG["adsense_pub"]).replace("{{TODAY}}", TODAY)
    s = s.replace("{{GAME_COUNT}}", NUM_WORDS.get(n, str(n)))
    s = s.replace("{{GAME_COUNT_CAP}}", NUM_WORDS.get(n, str(n)).capitalize())
    s = s.replace("{{GAME_NAMES}}", ", ".join(names[:-1]) + " and " + names[-1] if n > 1 else "".join(names))
    return re.sub(r"\{\{T:(\w+)\}\}", lambda m: esc(T[m.group(1)]), s)


def render_hub_pages(site):
    write_hub_css()
    ads = (f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
           f'?client=ca-{CFG["adsense_pub"]}" crossorigin="anonymous"></script>')
    head_extra = ads + "\n" + hub_ga_snippet()
    tpl = load(ROOT / "hub" / "hub_page.html")
    header = shell.site_nav(brand=CFG["brand"], games=site["nav_games"], intents=site["nav_intents"],
                            search=shell.search_form(action="/guides", index_url="/search-index.json",
                                                     lang="en", t=T,
                                                     placeholder=T["search_all_placeholder"]), t=T)
    ft_links = [(T[k], h) for k, h in CFG["intent_nav"]] + [
        (n, h) for n, h in T["trust"] if h not in dict(CFG["intent_nav"]).values()]
    ft = shell.footer(brand=CFG["brand"], year=TODAY[:4], links=ft_links, note=T["footer_note"])

    for page in sorted((ROOT / "hub" / "pages").glob("*.html")):
        name = page.stem
        meta, body = page_meta(fill(load(page)))
        body = (body.replace("{{GAMES_GRID}}", game_cards_html())
                    .replace("{{RECENT}}", feed_html(INDEX.recent(12, lang="en")))
                    .replace("{{ALL_GUIDES}}", all_guides_html())
                    .replace("{{UPDATES_FEED}}", feed_html(INDEX.recent(80, lang="en")))
                    .replace("{{UPDATES_STATS}}", updates_stats_html())
                    .replace("{{TOOLS_LIST}}", tools_html() if name == "tools" else ""))
        path = meta["path"]
        page_url = BASE + (path if path != "/" else "/")
        head = [f'<title>{esc(meta["title"])}</title>',
                f'<meta name="description" content="{esc(meta["description"])}">',
                f'<link rel="canonical" href="{esc(page_url)}">',
                '<meta property="og:type" content="website">',
                f'<meta property="og:site_name" content="{esc(CFG["brand"])}">',
                f'<meta property="og:title" content="{esc(meta["title"])}">',
                f'<meta property="og:description" content="{esc(meta["description"])}">',
                f'<meta property="og:url" content="{esc(page_url)}">',
                og_image_snippet(),
                '<meta name="twitter:card" content="summary_large_image">',
                hub_jsonld(name, CFG)]
        if name == "404":
            head.insert(3, '<meta name="robots" content="noindex">')

        if name == "index":
            main = ('<main class="home" id="main">\n'
                    + body.replace("{{HERO}}", hero_html(meta)) + "\n</main>")
        else:
            crumb_html, _ld = shell.crumbs([(CFG["brand"], "/"), (meta["h1"], None)], BASE,
                                           label=T["breadcrumb"])
            bl = shell.byline(author=T["site_author"], author_href="/about", reviewed=TODAY, t=T)
            main = (f'<main class="layout no-nav no-rail" id="main">\n{crumb_html}\n'
                    f'<div class="doc-hd"><h1>{esc(meta["h1"])}</h1>{bl}</div>\n'
                    f'<div class="doc"><div class="prose">{body}</div></div>\n</main>')

        html = (tpl.replace("{{LANG}}", "en")
                .replace("{{HEAD}}", "\n".join(head))
                .replace("{{FONTS}}", site["font_links"])
                .replace("{{HEAD_EXTRA}}", head_extra)
                .replace("{{HEADER}}", header)
                .replace("{{MAIN}}", main)
                .replace("{{SCRIPTS}}", shell.SEARCH_JS)
                .replace("{{FOOTER}}", ft))
        if name == "index":
            (OUT / "index.html").write_text(html, encoding="utf-8")
        elif name == "404":
            (OUT / "404.html").write_text(html, encoding="utf-8")
        else:
            d = OUT / name
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(html, encoding="utf-8")
    shutil.copy2(ROOT / "hub" / "favicon.svg", OUT / "favicon.svg")
    if (ROOT / "serve_preview.py").exists():
        shutil.copy2(ROOT / "serve_preview.py", OUT / "serve_preview.py")


def gen_search_index():
    """全站搜索索引:跨全部游戏一份,每条带 game 与 lang。"""
    rows = INDEX.search_rows()
    (OUT / "search-index.json").write_text(
        json.dumps(rows, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return len(rows)


def gen_root_files():
    (OUT / "ads.txt").write_text(
        f"google.com, {CFG['adsense_pub']}, DIRECT, f08c47fec0942fa0\n", encoding="utf-8"
    )
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8"
    )
    urls = []
    for p in sorted(OUT.rglob("*.html")):
        rel = p.relative_to(OUT)
        if rel.name == "404.html":
            continue
        if rel.name == "index.html":
            loc = "/" + str(rel.parent).replace("\\", "/") + "/"
            loc = loc.replace("/./", "/")
            if loc == "//":
                loc = "/"
        else:
            loc = "/" + str(rel)[:-5]  # cleanUrls: 去掉 .html
        urls.append(f"  <url><loc>{BASE}{loc}</loc><lastmod>{LASTMOD.get(loc, TODAY)}</lastmod></url>")
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n",
        encoding="utf-8",
    )
    lines = [f"# {CFG['brand']}", "", f"> {CFG['tagline']}.", ""]
    for g in CFG["games"]:
        lines.append(f"- [{g['name']}]({BASE}/{g['slug']}{g['default_path'].rstrip('/') or '/'}): {g['card']['blurb']}")
    (OUT / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def version_assets(out_dir: Path):
    """总站自有 CSS / JS 按内容 sha1 前 8 位打 ?v=。

    为什么必须有:改了 CSS 但 URL 不变时,浏览器会把缓存了 24 小时的旧 CSS 套在新 HTML 上,
    页面直接崩(踩过)。配合 vercel.json 里 css/js 的 max-age=0, must-revalidate 两道一起用。
    子站快照引用的是各自的文件名,不受影响。"""
    stamps = {}
    for rel in ("hub.css", "native.css", "snapshot.css", "search-index.json"):
        f = out_dir / rel
        if f.is_file():
            stamps[f"/{rel}"] = hashlib.sha1(f.read_bytes()).hexdigest()[:8]
    n = 0
    for p in out_dir.rglob("*.html"):
        html = p.read_text(encoding="utf-8")
        new = html
        for url, h in stamps.items():
            new = new.replace(f'href="{url}"', f'href="{url}?v={h}"')
            new = new.replace(f'src="{url}"', f'src="{url}?v={h}"')
            new = new.replace(f'data-index="{url}"', f'data-index="{url}?v={h}"')
        if new != html:
            p.write_text(new, encoding="utf-8")
            n += 1
    print("  资源版本化: " + " ".join(f"{u.lstrip('/')}?v={h}" for u, h in stamps.items())
          + f"(改写 {n} 个 html)")
    return stamps


def gen_vercel_json():
    redirects = []
    # 全站旧域名跳转:按 host 匹配旧 vercel.app 预览域,308 跳到当前 base_url,保留路径(:path*)。
    # 放在 redirects 数组最前面优先匹配;只认 LEGACY_VERCEL_HOST 这一个 host,不会连累 base_url
    # 自己(比如 lootwiki.com / www.lootwiki.com),不会造成重定向环。
    if LEGACY_VERCEL_HOST and LEGACY_VERCEL_HOST != BASE.split("//", 1)[-1].rstrip("/"):
        redirects.append({
            "source": "/:path*",
            "has": [{"type": "host", "value": LEGACY_VERCEL_HOST}],
            "destination": f"{BASE}/:path*",
            "permanent": True,
        })
    for g in CFG["games"]:
        slug = g["slug"]
        if g["default_path"] not in ("/", ""):
            redirects.append({"source": f"/{slug}", "destination": f"/{slug}{g['default_path']}", "permanent": False})
        src_vj = {
            "beast-of-reincarnation": ROOT / "sources" / "beast" / "vercel.json",
            "shift-at-midnight": ROOT / "sources" / "shift" / "vercel.json",
        }.get(slug)
        if src_vj and src_vj.exists():
            vj = json.loads(src_vj.read_text())
            for r in vj.get("redirects", []):
                s, d = r["source"], r["destination"]
                if s == "/":  # 原站根跳转已由上面的 default_path 跳转承担
                    continue
                redirects.append({"source": f"/{slug}{s}", "destination": f"/{slug}{d}", "permanent": r.get("permanent", True)})
    vercel = {
        "$schema": "https://openapi.vercel.sh/vercel.json",
        "cleanUrls": True,
        "outputDirectory": "out",
        "redirects": redirects,
        "headers": [
            {"source": "/(.*)", "headers": [
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                {"key": "Cache-Control", "value": "public, max-age=0, must-revalidate"},
            ]},
            {"source": "/(.*)\\.(jpg|png|svg|ico)", "headers": [
                {"key": "Cache-Control", "value": "public, max-age=86400"},
            ]},
            {"source": "/(.*)\\.(css|js)", "headers": [
                {"key": "Cache-Control", "value": "public, max-age=0, must-revalidate"},
            ]},
        ],
    }
    (ROOT / "vercel.json").write_text(json.dumps(vercel, indent=2) + "\n", encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    site = {
        "base": BASE, "today": TODAY, "year": TODAY[:4],
        "head_extra": (f'<script async src="https://pagead2.googlesyndication.com/pagead/js/'
                       f'adsbygoogle.js?client=ca-{CFG["adsense_pub"]}" crossorigin="anonymous">'
                       f"</script>\n" + hub_ga_snippet()),
        "nav_games": nav_games(),
        "nav_intents": nav_intents(),
        "font_links": font_links(),
    }
    # 索引:快照游戏与原生游戏都在渲染时回填,最后按 config 顺序排回去
    render_snapshot_games(site)
    render_native_games(site)
    order = {g["slug"]: i for i, g in enumerate(CFG["games"])}
    INDEX.games.sort(key=lambda gi: order[gi.slug])
    render_hub_pages(site)
    rows = gen_search_index()
    version_assets(OUT)
    gen_root_files()
    gen_vercel_json()
    n = len(list(OUT.rglob("*.html")))
    print(f"  索引: {len(INDEX.games)} 个游戏 · {INDEX.page_count} 个攻略页 · 搜索索引 {rows} 条")
    print(f"built {n} html pages → {OUT}  (base={BASE})")


if __name__ == "__main__":
    main()
