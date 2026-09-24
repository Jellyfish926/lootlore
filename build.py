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
       LOOTLORE_BUILD_DATE=2026-09-22 python3 build.py  # 把构建日期钉住(产物可复现)
"""
import hashlib, json, os, re, shutil, sys, datetime
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


def build_date() -> str:
    """构建日期。这个值会写进 12 个文件(11 个总站自有页的 Last reviewed、
    sitemap.xml 的 lastmod 兜底),所以不钉住的话「重建产物再比 diff」在提交日的次日起天天误红。
    先认环境变量 LOOTLORE_BUILD_DATE(CI 从仓库根的 build-stamp.json 里取),取不到才用今天。"""
    v = os.environ.get("LOOTLORE_BUILD_DATE", "").strip()
    if not v:
        return datetime.date.today().isoformat()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
        raise SystemExit(f"LOOTLORE_BUILD_DATE={v!r} 格式不对:必须是零填充的 YYYY-MM-DD,构建中止")
    try:
        datetime.date.fromisoformat(v)
    except ValueError as e:
        raise SystemExit(f"LOOTLORE_BUILD_DATE={v!r} 不是真实存在的日期({e}),构建中止")
    return v


TODAY = build_date()
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


def request_ctx() -> dict:
    """提需求弹窗(hub/shell.py:request_*)的站级参数。key 为空时弹窗仍渲染,只是提交禁用。"""
    return {"games": [(g["slug"], g["name"]) for g in CFG["games"]],
            "key": CFG.get("web3forms_key", "") or "",
            "email": CFG["contact_email"], "brand": CFG["brand"]}


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


# Consent Mode v2 默认值只对这些地区设 denied(其余地区兜底 granted)。
# 口径 = EEA 30 国(EU 27 + 冰岛 IS / 列支敦士登 LI / 挪威 NO)+ 英国 GB + 瑞士 CH,
# 即 Google 自家 CMP(AdSense「欧洲法规消息」)会弹窗的那一组 —— CMP 只更新弹窗用户的同意状态,
# 非弹窗地区的默认值必须由站点自己设,所以两条 default 缺一不可。
# region 写法按 Google 文档 https://developers.google.com/tag-platform/security/guides/consent
# 用 ISO 3166-2(国家级即 alpha-2),更具体的 region 优先、无 region 的那条覆盖其余访客。
CONSENT_DENIED_REGIONS = [
    # EU 27
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT",
    "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE",
    # EEA 非 EU 三国
    "IS", "LI", "NO",
    # 英国 + 瑞士
    "GB", "CH",
]


def consent_default_snippet() -> str:
    """Consent Mode v2 默认值。必须在 gtag.js、AdSense(adsbygoogle.js)与任何 gtag('config')
    之前执行(Google:「call gtag('consent','default') on every page before any commands that
    send measurement data」),所以 dataLayer / gtag 的定义也提到这里,GA 片段不再重复定义。
    wait_for_update=500:给 CMP 500ms 调 gtag('consent','update') 再放行标签(文档示例值)。"""
    regions = ",".join(f"'{r}'" for r in CONSENT_DENIED_REGIONS)
    return (
        "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}\n"
        "gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',"
        f"analytics_storage:'denied',wait_for_update:500,region:[{regions}]}});\n"
        "gtag('consent','default',{ad_storage:'granted',ad_user_data:'granted',ad_personalization:'granted',"
        "analytics_storage:'granted'});</script>\n"
    )


def hub_ga_snippet() -> str:
    """GA4:只剩 gtag.js 外链 + js/config;dataLayer/gtag 的定义在 consent_default_snippet() 里。"""
    gid = CFG.get("ga4_id", "")
    if not gid:
        return ""
    return (
        f'<script async src="https://www.googletagmanager.com/gtag/js?id={gid}"></script>\n'
        f"<script>gtag('js',new Date());gtag('config','{gid}');</script>\n"
    )


def head_scripts(ads: bool = True) -> str:
    """每页 <head> 里的三方脚本,顺序固定:consent default → AdSense → gtag.js → config。
    ga4_id 为空时 consent 段照常输出(AdSense 也吃 consent 信号),只是没有 GA 片段。
    ads=False 用于 404 页:AdSense 政策不许错误页带广告代码(提审前检查会阻塞),
    consent 段与 GA 片段照常保留 —— 404 也要统计。"""
    ads_line = (f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
                f'?client=ca-{CFG["adsense_pub"]}" crossorigin="anonymous"></script>\n') if ads else ""
    return consent_default_snippet() + ads_line + hub_ga_snippet()


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


def breadcrumb_ld(base: str, brand: str, crumbs: list, current: str = "") -> dict:
    """crumbs: [(name, path_or_None)] 最后一项是当前页。
    Google 只允许最后一项省略 item;这里最后一项也显式给 item = current(页面 canonical),
    和 hub/shell.py:crumbs() 的规则保持一致,不让「省略」这条路径存在。"""
    items = []
    for i, (label, path) in enumerate(crumbs, start=1):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if i == len(crumbs) and current:
            entry["item"] = current
        elif path is not None:
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
        graphs.append(breadcrumb_ld(base, brand, [(brand, None)], current=f"{base}/"))
    elif name == "about":
        graphs.append({
            "@context": "https://schema.org", "@type": "AboutPage",
            "name": f"About {brand}", "url": f"{base}/about",
            "isPartOf": {"@type": "WebSite", "name": brand, "url": f"{base}/"},
        })
        graphs.append(breadcrumb_ld(base, brand, [(brand, "/"), ("About", None)], current=f"{base}/about"))
    elif name == "contact":
        graphs.append({
            "@context": "https://schema.org", "@type": "ContactPage",
            "name": f"Contact {brand}", "url": f"{base}/contact",
            "isPartOf": {"@type": "WebSite", "name": brand, "url": f"{base}/"},
        })
        graphs.append(breadcrumb_ld(base, brand, [(brand, "/"), ("Contact", None)], current=f"{base}/contact"))
    elif name in ("guides", "reviews", "updates", "tools"):
        label = {"guides": "Guides", "reviews": "Reviews", "updates": "Updates",
                 "tools": "Tools"}[name]
        graphs.append({
            "@context": "https://schema.org", "@type": "CollectionPage",
            "name": label, "url": f"{base}/{name}",
            "isPartOf": {"@type": "WebSite", "name": brand, "url": f"{base}/"},
        })
        graphs.append(breadcrumb_ld(base, brand, [(brand, "/"), (label, None)], current=f"{base}/{name}"))
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
        graphs.append(breadcrumb_ld(base, brand, [(brand, "/"), (label, None)], current=f"{base}/{name}"))

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


# ---------------------------------------------------------------- 首页卡片模块(全部靠真实统计)
def card_img(im) -> str:
    """卡片缩略图。src 已经是小图变体(见 pageindex._content_image / native.card_image /
    配置层 shots),所以不出 srcset —— 也就不写 sizes(没有 srcset 的 sizes 是空属性)。
    width/height 与 src 的真实尺寸一致,配合 CSS 的 aspect-ratio 双保险占位;
    首屏 hero 之外一律 lazy。alt 一律用素材自己的描述,这里不生成 alt。"""
    if not im or not im.get("src"):
        return ""
    return (f'<img src="{esc(im["src"])}" width="{im["w"]}" height="{im["h"]}"'
            f' alt="{esc(im.get("alt", ""))}" loading="lazy" decoding="async">')


def tool_pages(gi):
    """该游戏的互动工具页:标题命中 config/hub.json → tools_match 的关键词。
    匹配规则在配置层,框架层不写任何游戏专属文字。"""
    keys = [k.lower() for k in CFG.get("tools_match", [])]
    return sorted((p for p in gi.pages
                   if p.lang == gi.default_lang and any(k in p.title.lower() for k in keys)),
                  key=lambda p: p.title)


def start_here_pick(gi):
    """该游戏的入门页:按 config/hub.json → start_here_match(有序偏好表)匹配路由末段。
    与 tools_match 同一机制 —— 规则在配置层,可解释、可改、不写死清单。
    匹配不到就不出这个游戏,绝不随便挑一页充当入门页。"""
    order = [k.lower() for k in CFG.get("start_here_match", [])]
    seen = {}
    for p in gi.pages:
        if p.lang != gi.default_lang:
            continue
        seg = p.route.rstrip("/").rsplit("/", 1)[-1].lower()
        if seg in order:
            seen.setdefault(seg, p)
    return next((seen[k] for k in order if k in seen), None)


def featured_pages(gi, n=6):
    """一个游戏的精选攻略。只从该游戏自己已有的分组里取,不发明「热门」排序。

    真相源 = hub/pageindex.py 推导出的栏目 —— 快照站取自它 hub 页自己的卡片网格分组
    或子站面包屑目录,原生站取自内容层的栏目定义。规则:
      1) 候选栏目 = 去掉兜底桶 `_more`(那不是策展分组,是「剩下的页」)。
         一个游戏全部页都落在兜底桶的极端情况下才退回用它,否则它一条都出不来。
      2) 栏目顺序沿用 pageindex 排好的顺序(按真实页数从多到少),不另设权重。
      3) 栏目内部按「页面自己记录的复核日」降序,同日按标题 —— 复核日是事实,构建稳定。
         栏目自己的落地页不进来(它已经被上面的栏目胶囊链接了)。
      4) 各栏目轮转取,取满 n 条为止 —— 精选因此横跨该游戏的各个真实栏目,
         不是某一个栏目的前 n 条。
    我们没有任何访问量/点击数据,所以这里没有也不会有 Popular / 最受欢迎排序。"""
    secs = [s for s in gi.sections if s.key != "_more"] or list(gi.sections)
    lands = {s.route.rstrip("/") for s in gi.sections if s.route}
    queues = []
    for s in secs:
        ps = [p for p in s.pages
              if p.lang == gi.default_lang and p.route.rstrip("/") not in lands]
        ps.sort(key=lambda p: (p.date, p.title), reverse=True)
        queues.append((s, ps))
    out, seen, i, guard = [], set(), 0, 0
    while queues and len(out) < n and guard < 500:
        guard += 1
        s, q = queues[i % len(queues)]
        i += 1
        while q:
            p = q.pop(0)
            if p.route not in seen:
                seen.add(p.route)
                out.append((s, p))
                break
        if not any(q for _s, q in queues):
            break
    return out


def game_stats(gi):
    """一行统计,每个数字都来自实际统计:页数 / 栏目数 / 工具数 / 语种数 / 最后复核日。
    统计不出来的项直接不显示(没有估算,也没有写死的数)。"""
    bits = [f'<b>{gi.page_count}</b>&nbsp;{esc(T["stat_guides"])}']
    if gi.sections:
        bits.append(f'<b>{len(gi.sections)}</b>&nbsp;{esc(T["stat_sections"])}')
    nt = len(tool_pages(gi))
    if nt:
        bits.append(f'<b>{nt}</b>&nbsp;{esc(T["stat_tools" if nt > 1 else "stat_tool"])}')
    nl = len({p.lang for p in gi.pages})
    if nl > 1:
        bits.append(f'<b>{nl}</b>&nbsp;{esc(T["stat_languages"])}')
    if gi.updated:
        bits.append(f'<time datetime="{gi.updated}">{esc(T["updated_on"].format(d=gi.updated))}</time>')
    return f'<p class="stats">{" &middot; ".join(bits)}</p>'


def distinct_image(gi, page, used: set):
    """同一个模块里不重复用同一张图。先要这一页自己的配图,撞车了就从该游戏的截图池里
    换一张没用过的 —— 池里都是该游戏的官方素材,alt 写的是画面里实际有什么,
    所以换图不改变任何事实陈述。池子全用过了就照旧用重复的那张(宁可重复,不留空位)。"""
    im = gi.image_for(page)
    if im and im.get("src") in used:
        alt_im = next((x for x in gi.shot_pool if x.get("src") not in used), None)
        im = alt_im or im
    if im:
        used.add(im.get("src"))
    return im


def recent_cards_html(n=6):
    """最近更新:卡片网格。缩略图 = 该页自己的官方配图,没有配图的页走该游戏的官方截图池
    (见 GameIndex.image_for),同模块内再去重。只取 n 条,全量时间流在 /updates。"""
    by_slug = {g.slug: g for g in INDEX.games}
    out, used = [], set()
    for p in INDEX.recent(n, lang="en"):
        gi = by_slug[p.game]
        im = distinct_image(gi, p, used)
        out.append(
            f'<li class="rcard">'
            f'<a class="rc-shot" href="{esc(p.route)}" tabindex="-1" aria-hidden="true">'
            f'{card_img(im)}</a>'
            f'<div class="rc-b">'
            f'<p class="rc-g">{esc(gi.short)}</p>'
            f'<h3><a href="{esc(p.route)}">{esc(p.title)}</a></h3>'
            f'<p class="rc-d"><time datetime="{esc(p.date)}">'
            f'{esc(T["reviewed_on"].format(d=p.date))}</time></p>'
            f'</div></li>')
    return f'<ul class="rcards">{"".join(out)}</ul>'


def start_cards_html():
    """Start here:每个游戏一张入门卡。匹配不到入门页的游戏不出卡。
    每张卡带两个真实数字,跟 game_stats() 同一套字段、同一套 T[] 文案,不是为这
    张卡新估的:gi.page_count 是该游戏默认语种的实际页数;p.date 是这张入门页
    自己记录的复核日(modified ?? published)。两个都算不出来才会少一项,绝不
    补一个假数字充数。"""
    out = []
    for gi in INDEX.games:
        p = start_here_pick(gi)
        if not p:
            continue
        im = gi.image_for(p)
        bits = [f'<b>{gi.page_count}</b>&nbsp;{esc(T["stat_guides"])}']
        if p.date:
            bits.append(f'<time datetime="{esc(p.date)}">{esc(T["reviewed_on"].format(d=p.date))}</time>')
        out.append(
            f'<li class="scard"><a href="{esc(p.route)}">'
            f'<span class="sc-shot">{card_img(im)}</span>'
            f'<span class="sc-b"><span class="sc-g">{esc(gi.short)}</span>'
            f'<b>{esc(p.title)}</b>'
            f'<span class="sc-stats">{" &middot; ".join(bits)}</span></span></a></li>')
    return f'<ul class="scards">{"".join(out)}</ul>' if out else ""


def tool_cards_html():
    """Tools:把仓里真能用的互动页提到首页。空了就不渲染这个模块(/tools 页那边会构建失败)。"""
    out, used = [], set()
    for gi in INDEX.games:
        for p in tool_pages(gi):
            im = distinct_image(gi, p, used)
            out.append(
                f'<li class="tcard">'
                f'<a class="tc-shot" href="{esc(p.route)}" tabindex="-1" aria-hidden="true">'
                f'{card_img(im)}</a>'
                f'<div class="tc-b"><p class="tc-g">{esc(gi.short)}</p>'
                f'<h3><a href="{esc(p.route)}">{esc(p.title)}</a></h3>'
                + (f'<p class="tc-d">{esc(clip(p.description, 110))}</p>' if p.description else "")
                + "</div></li>")
    return f'<ul class="tcards">{"".join(out)}</ul>' if out else ""


def by_game_html():
    """首页主体:每个游戏一条带。封面 + 真实统计 + 栏目胶囊(带真实页数)+ 精选攻略 +
    「全部 N 篇」入口。全量索引在 /guides,首页不再平铺全站链接。"""
    out = []
    for gi in INDEX.games:
        g = next(x for x in CFG["games"] if x["slug"] == gi.slug)
        c = gi.card
        cover = {"src": c["img"], "w": c["img_w"], "h": c["img_h"], "alt": c["img_alt"]}
        chips = "".join(
            f'<a href="{esc(s.route)}">{esc(s.label)}<span>{s.count}</span></a>' if s.route
            else f'<span class="chip-off">{esc(s.label)}<span>{s.count}</span></span>'
            for s in gi.sections)
        picks = "".join(
            f'<li><a href="{esc(p.route)}"><b>{esc(p.title)}</b>'
            f'<span class="gb-m">{esc(s.label)}'
            + (f' &middot; <time datetime="{esc(p.date)}">{esc(p.date)}</time>' if p.date else "")
            + "</span></a></li>"
            for s, p in featured_pages(gi, 6))
        credit = g.get("shots_credit") or c.get("img_credit", "")
        out.append(
            f'<article class="gband" id="g-{esc(gi.slug)}">'
            f'<a class="gb-shot" href="{esc(gi.home_route)}" tabindex="-1" aria-hidden="true">'
            f'{card_img(cover)}</a>'
            f'<div class="gb-b">'
            f'<p class="gb-genre">{esc(c["genre"])}</p>'
            f'<h3><a href="{esc(gi.home_route)}">{esc(gi.name)}</a></h3>'
            f'{game_stats(gi)}'
            f'<div class="gb-chips">{chips}</div>'
            f'<ul class="gb-list">{picks}</ul>'
            f'<p class="gb-more"><a href="{esc(gi.home_route)}">'
            f'{esc(T["all_n_guides"].format(n=gi.page_count, game=gi.short))} &rarr;</a>'
            f'<span class="credit">{esc(credit)}</span></p>'
            f'</div></article>')
    return f'<div class="gbands">{"".join(out)}</div>'


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
    out, total = [], 0
    for gi in INDEX.games:
        hit = tool_pages(gi)
        if not hit:
            continue
        total += len(hit)
        lis = "".join(f'<li><a href="{esc(p.route)}">{esc(p.title)}</a>'
                      + (f"<span>{esc(clip(p.description, 150))}</span>" if p.description else "")
                      + "</li>" for p in hit)
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
    # 同一份名单,每个名字链到该游戏 hub 的默认入口(config: slug + default_path)
    links = [f'<a href="/{g["slug"]}{g["default_path"]}">{esc(g["name"])}</a>' for g in CFG["games"]]
    s = s.replace("{{GAME_LINKS}}", ", ".join(links[:-1]) + " and " + links[-1] if n > 1 else "".join(links))
    return re.sub(r"\{\{T:(\w+)\}\}", lambda m: esc(T[m.group(1)]), s)


def hub_sizes_html():
    """各 hub 的规模一句话:页数来自全站索引的实际统计(与首页卡片同口径),语种列表来自配置层
    card.langs(与卡片上显示的一致)。手写数字必然过期,所以这里不接受任何硬编码。"""
    parts = []
    for gi in INDEX.games:
        langs = (gi.card or {}).get("langs", "")
        n = gi.page_count
        parts.append(f'<a href="{esc(gi.home_route)}">{esc(gi.name)}</a> &mdash; '
                     f'{n} {esc(T["pages_count"].format(n="").strip())}'
                     + (f' ({esc(langs)})' if langs else ""))
    return "; ".join(parts)


def render_hub_pages(site):
    write_hub_css()
    tpl = load(ROOT / "hub" / "hub_page.html")
    header = shell.site_nav(brand=CFG["brand"], games=site["nav_games"], intents=site["nav_intents"],
                            search=shell.search_form(action="/guides", index_url="/search-index.json",
                                                     lang="en", t=T,
                                                     placeholder=T["search_all_placeholder"]), t=T)
    ft_links = [(T[k], h) for k, h in CFG["intent_nav"]] + [
        (n, h) for n, h in T["trust"] if h not in dict(CFG["intent_nav"]).values()]
    req = site["request"]
    ft = shell.footer(brand=CFG["brand"], year=TODAY[:4], links=ft_links, note=T["footer_note"],
                      extra=shell.request_link(email=req["email"], brand=req["brand"], t=T))
    req_block = shell.request_block(games=req["games"], current="", lang="en", key=req["key"],
                                    email=req["email"], brand=req["brand"], t=T)

    for page in sorted((ROOT / "hub" / "pages").glob("*.html")):
        name = page.stem
        meta, body = page_meta(fill(load(page)))
        body = (body.replace("{{GAMES_GRID}}", game_cards_html())
                    .replace("{{RECENT_CARDS}}", recent_cards_html(6))
                    .replace("{{START_CARDS}}", start_cards_html())
                    .replace("{{TOOL_CARDS}}", tool_cards_html())
                    .replace("{{BY_GAME}}", by_game_html())
                    .replace("{{ALL_GUIDES}}", all_guides_html())
                    .replace("{{UPDATES_FEED}}", feed_html(INDEX.recent(80, lang="en")))
                    .replace("{{UPDATES_STATS}}", updates_stats_html())
                    .replace("{{HUB_SIZES}}", hub_sizes_html())
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
                                           label=T["breadcrumb"], current=page_url)
            bl = shell.byline(author=T["site_author"], author_href="/about", reviewed=TODAY, t=T)
            # 这些页没有右栏(no-rail):「提需求」入口只走页脚链接 + 浮动按钮(桌面端也显示,同首页),
            # 不为一张卡片硬加一个右栏。
            main = (f'<main class="layout no-nav no-rail" id="main">\n{crumb_html}\n'
                    f'<div class="doc-hd"><h1>{esc(meta["h1"])}</h1>{bl}</div>\n'
                    f'<div class="doc"><div class="prose">{body}</div></div>\n</main>')

        html = (tpl.replace("{{LANG}}", "en")
                .replace("{{HEAD}}", "\n".join(head))
                .replace("{{FONTS}}", site["font_links"])
                .replace("{{HEAD_EXTRA}}", head_scripts(ads=(name != "404")))
                .replace("{{HEADER}}", header)
                .replace("{{MAIN}}", main)
                .replace("{{SCRIPTS}}", req_block + shell.SEARCH_JS)
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
    canon_re = re.compile(r'<link\s+rel="canonical"[^>]*\bhref="([^"]*)"', re.I)
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
        # <loc> 必须等于页面自己的 canonical:总站自有页 canonical 是 /about(无尾斜杠),
        # beast 语种根是 /beast-of-reincarnation/fr(子站产出),而 index.html 按目录算出来的是 /about/。
        # 两者不一致时 Google 抓 sitemap 里那条,再按 canonical 归并 → GSC 报「备用网页(有适当的规范标记)」
        # (2026-09-24:/privacy-policy/ /beast-of-reincarnation/fr/ /beast-of-reincarnation/ja/ 就是这么来的)。
        lastmod = LASTMOD.get(loc, TODAY)  # LASTMOD 按目录路由记,先取再改写 loc
        m = canon_re.search(p.read_text(encoding="utf-8")[:6000])
        href = m.group(1).strip() if m else ""
        if href.startswith(BASE + "/") and href[len(BASE):] != loc:
            loc = href[len(BASE):]
        urls.append(f"  <url><loc>{BASE}{loc}</loc><lastmod>{lastmod}</lastmod></url>")
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


def gen_build_stamp():
    """构建日期锚。CI 先读它、再用同一个日期重建产物,才能拿 git diff 校验「提交的 out/ 是否
    等于新鲜构建」—— 不钉住日期的话,写着构建日的那 12 个文件会让次日之后每次校验都误红。
    写在仓库根而不是 out/:进了 out/ 就多出一个对外可访问的 URL,还会扰动 check_sitemap
    (PAGE_NOT_IN_SITEMAP)与 link_check。跟上面的 gen_vercel_json 一个路子,必须提交进库。"""
    (ROOT / "build-stamp.json").write_text(
        json.dumps({"build_date": TODAY}, indent=2) + "\n", encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    site = {
        "base": BASE, "today": TODAY, "year": TODAY[:4],
        "head_extra": head_scripts(),
        "nav_games": nav_games(),
        "nav_intents": nav_intents(),
        "font_links": font_links(),
        "request": request_ctx(),
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
    gen_build_stamp()
    n = len(list(OUT.rglob("*.html")))
    print(f"  索引: {len(INDEX.games)} 个游戏 · {INDEX.page_count} 个攻略页 · 搜索索引 {rows} 条")
    print(f"built {n} html pages → {OUT}  (base={BASE})")


if __name__ == "__main__":
    main()
