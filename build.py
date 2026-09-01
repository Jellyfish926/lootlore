#!/usr/bin/env python3
"""Guide Atlas hub assembler.

三层分离:
  框架层 = 本脚本 + hub/ 壳(总站页面模板与样式)
  配置层 = config/hub.json(品牌、base_url、游戏清单、剥离/映射规则)
  内容层 = sources/<game>/(各子站静态快照,原样不改,变换只发生在 out/)

用法:  python3 build.py            # 组装到 out/
       python3 build.py --base https://xxx.vercel.app   # 覆盖 base_url
"""
import json, re, shutil, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CFG = json.loads((ROOT / "config" / "hub.json").read_text())
if "--base" in sys.argv:
    CFG["base_url"] = sys.argv[sys.argv.index("--base") + 1].rstrip("/")
BASE = CFG["base_url"].rstrip("/")
OUT = ROOT / "out"
TODAY = datetime.date.today().isoformat()
SENT = "@@HUB@@"  # 信任页映射后的哨兵前缀,防止被通用子路径改写二次加前缀

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
    # 对已剥离服务的预连接
    re.compile(r'<link rel="(?:preconnect|dns-prefetch)" href="https://(?:www\.googletagmanager\.com|www\.clarity\.ms)"[^>]*>\s*'),
]

ATTR_RE = re.compile(r'((?:href|src|content|action|poster|data-src)=")(/[^"]*)(")')
SRCSET_RE = re.compile(r'(srcset=")([^"]*)(")')


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


def hubbar_html(active_slug: str = "") -> str:
    links = "".join(
        f'<a href="{SENT}/{g["slug"]}{g["default_path"].rstrip("/") or "/"}"'
        + (' class="on"' if g["slug"] == active_slug else "")
        + f'>{g["short"]}</a>'
        for g in CFG["games"]
    )
    return (
        f'<div class="ga-hubbar"><div class="ga-hubbar-in">'
        f'<a class="ga-hubbrand" href="{SENT}/">◆ {CFG["brand"]}</a>'
        f'<nav class="ga-hublinks">{links}<a href="{SENT}/#games">All games</a></nav>'
        f"</div></div>"
    )


HUBBAR_CSS = """<style>
.ga-hubbar{background:#0b0d12;border-bottom:1px solid #23262f;font:13px/1.4 system-ui,-apple-system,Segoe UI,sans-serif}
.ga-hubbar-in{max-width:1100px;margin:0 auto;padding:7px 16px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.ga-hubbrand{color:#e8b64c;text-decoration:none;font-weight:700;letter-spacing:.04em}
.ga-hublinks{display:flex;gap:12px;flex-wrap:wrap}
.ga-hublinks a{color:#9aa3b2;text-decoration:none}
.ga-hublinks a:hover{color:#e6e9ef}
.ga-hublinks a.on{color:#e6e9ef;font-weight:600}
</style>
"""


def transform_page(html: str, game: dict) -> str:
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

    # 其余根相对链接 → 加 /<slug> 前缀
    def prefix(m):
        return f"{m.group(1)}/{slug}{m.group(2)}{m.group(3)}"

    html = ATTR_RE.sub(lambda m: m.group(0) if m.group(2).startswith(f"{SENT}") else prefix(m), html)

    def fix_srcset(m):
        parts = [p.strip() for p in m.group(2).split(",")]
        parts = [(f"/{slug}" + p) if p.startswith("/") else p for p in parts]
        return m.group(1) + ", ".join(parts) + m.group(3)

    html = SRCSET_RE.sub(fix_srcset, html)

    # 注入总站导航条 + 样式 + hub GA
    inj_head = HUBBAR_CSS + hub_ga_snippet()
    html = html.replace("</head>", inj_head + "</head>", 1)
    html = re.sub(r"<body([^>]*)>", lambda m: f"<body{m.group(1)}>\n" + hubbar_html(slug), html, count=1)

    # 摘哨兵
    html = html.replace(SENT, "")
    return html


def migrate_game(game: dict):
    src = ROOT / game["source"]
    dst = OUT / game["slug"]
    ex_files = set(game["exclude_files"])
    ex_dirs = set(game["exclude_dirs"])
    for p in src.rglob("*"):
        rel = p.relative_to(src)
        if p.is_dir():
            continue
        if rel.parts[0] in ex_dirs or rel.name in ex_files and len(rel.parts) == 1:
            continue
        if rel.name in {".DS_Store"}:
            continue
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix == ".html":
            html = load(p)
            for patch in game.get("patches", []):
                if patch["file"] == str(rel):
                    assert patch["find"] in html, f"patch find miss: {rel}"
                    html = html.replace(patch["find"], patch["find"] + patch["insert_after"], 1)
            target.write_text(transform_page(html, game), encoding="utf-8")
        else:
            shutil.copy2(p, target)


def render_hub_pages():
    style = load(ROOT / "hub" / "style.css")
    (OUT / "hub.css").write_text(style, encoding="utf-8")

    grid = []
    for g in CFG["games"]:
        c = g["card"]
        hi = "".join(f'<a class="hl" href="{u}">{t}</a>' for t, u in c["highlights"])
        grid.append(f"""
<article class="game-card" id="{g['slug']}">
  <a class="shot" href="/{g['slug']}{g['default_path'].rstrip('/') or '/'}" aria-label="{g['name']} guide hub">
    <img src="{c['img']}" alt="{c['img_alt']}" loading="lazy">
  </a>
  <div class="body">
    <p class="genre">{c['genre']}</p>
    <h3><a href="/{g['slug']}{g['default_path'].rstrip('/') or '/'}">{g['name']}</a></h3>
    <p class="meta">{c['studio']} · Released {c['released']}<br>{c['platforms']}</p>
    <p class="blurb">{c['blurb']}</p>
    <div class="hls">{hi}</div>
    <p class="stats">{c['pages']} · {c['langs']}</p>
    <p class="credit">{c['img_credit']}</p>
  </div>
</article>""")
    grid_html = "\n".join(grid)

    for page in (ROOT / "hub" / "pages").glob("*.html"):
        html = load(page)
        html = html.replace("{{BASE}}", BASE).replace("{{BRAND}}", CFG["brand"])
        html = html.replace("{{TAGLINE}}", CFG["tagline"]).replace("{{EMAIL}}", CFG["contact_email"])
        html = html.replace("{{PUB}}", CFG["adsense_pub"]).replace("{{TODAY}}", TODAY)
        html = html.replace("{{GAMES_GRID}}", grid_html)
        html = html.replace("{{GA_SNIPPET}}", hub_ga_snippet())
        name = page.stem
        if name == "index":
            (OUT / "index.html").write_text(html, encoding="utf-8")
        elif name == "404":
            (OUT / "404.html").write_text(html, encoding="utf-8")
        else:
            d = OUT / name
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(html, encoding="utf-8")
    shutil.copy2(ROOT / "hub" / "favicon.svg", OUT / "favicon.svg")


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
        urls.append(f"  <url><loc>{BASE}{loc}</loc><lastmod>{TODAY}</lastmod></url>")
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


def gen_vercel_json():
    redirects = []
    for g in CFG["games"]:
        slug = g["slug"]
        if g["default_path"] not in ("/", ""):
            redirects.append({"source": f"/{slug}", "destination": f"/{slug}{g['default_path']}", "permanent": False})
        src_vj = {
            "beast-of-reincarnation": ROOT.parent / "beast" / "vercel.json",
            "shift-at-midnight": ROOT.parent / "shift" / "vercel.json",
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
            {"source": "/(.*)\\.(css|jpg|png|svg|ico)", "headers": [
                {"key": "Cache-Control", "value": "public, max-age=86400"},
            ]},
        ],
    }
    (ROOT / "vercel.json").write_text(json.dumps(vercel, indent=2) + "\n", encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    for g in CFG["games"]:
        migrate_game(g)
    render_hub_pages()
    gen_root_files()
    gen_vercel_json()
    n = len(list(OUT.rglob("*.html")))
    print(f"built {n} html pages → {OUT}  (base={BASE})")


if __name__ == "__main__":
    main()
