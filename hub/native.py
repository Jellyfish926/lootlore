"""native —— 原生内容游戏(config/hub.json 里 kind=native)的渲染器。框架层。

输入:<game.content>/*.md(frontmatter + 正文,正文自带 H1)+ <game.content>/_images.json
     + config/i18n/<lang>.json(界面文字)+ hub.json 该游戏的 native 配置块。
输出:out/<slug>/index.html(游戏 hub)与 out/<slug>/<page>/index.html。

本文件不含任何具体游戏的文字;换游戏只动配置层与内容层。
页型由 frontmatter.type 决定:home / category / article / author。
draft: true 的页不生成、不进 sitemap、不进栏目列表与 hub 清单、不进关联阅读;
正文里指向草稿的站内链接降级为纯文本(否则就是死链)。
"""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

from hub import mdlite
from hub.mdlite import esc


class NativeError(Exception):
    pass


def ld_script(obj) -> str:
    """统一 JSON-LD 输出:紧凑 JSON + 转义 < > &,防止正文里的字符提前闭合 <script>。"""
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    s = s.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return f'<script type="application/ld+json">{s}</script>'


def _host(url: str) -> str:
    return (urlparse(url).hostname or "").lower()


class Page:
    def __init__(self, path: Path, fm: dict, body: str):
        self.path, self.fm, self.body = path, fm, body
        self.slug = str(fm.get("slug") or path.stem)
        self.type = fm.get("type") or "article"
        self.draft = fm.get("draft") is True

    def get(self, k, default=""):
        v = self.fm.get(k)
        return default if v is None or v == "" else v


class NativeGame:
    def __init__(self, root: Path, game: dict, cfg: dict, site: dict):
        self.root, self.g, self.cfg, self.site = root, game, cfg, site
        self.nc = game.get("native", {})
        self.gslug = game["slug"]
        self.base = site["base"]
        self.warnings = []
        lang = game.get("lang", "en")
        self.t = json.loads((root / "config" / "i18n" / f"{lang}.json").read_text(encoding="utf-8"))
        self.content = root / game["content"]
        img_file = self.content / "_images.json"
        self.images = json.loads(img_file.read_text(encoding="utf-8")) if img_file.is_file() else {}
        self.official = [d.lower() for d in self.nc.get("official_domains", [])]
        self._load()

    # ------------------------------------------------------------ loading
    def _load(self):
        defaults = self.nc.get("defaults", {})
        self.pages = {}
        for p in sorted(self.content.glob("*.md")):
            if p.name.startswith("_"):
                continue
            fm, body = mdlite.split_frontmatter(p.read_text(encoding="utf-8"))
            for k, v in defaults.items():
                if fm.get(k) in (None, ""):
                    fm[k] = v
            # 日期回退链:updated ← date;reviewed ← checkedAt(资料核对日)
            if not fm.get("updated"):
                fm["updated"] = fm.get("date", "")
            if not fm.get("reviewed") and fm.get("checkedAt"):
                fm["reviewed"] = fm["checkedAt"]
            pg = Page(p, fm, body)
            if pg.slug in self.pages:
                raise NativeError(f"{p.name}: slug 重复 {pg.slug}")
            self.pages[pg.slug] = pg
            want = self.route(pg)
            if fm.get("url") and fm["url"] != want:
                raise NativeError(f"{p.name}: frontmatter url={fm['url']} 与路由规则 {want} 不一致")
            if fm.get("language") and fm["language"] != self.g.get("lang"):
                self.warnings.append(f"{p.name}: language={fm['language']} 与游戏 lang={self.g.get('lang')} 不同")
        self.pub = {s: p for s, p in self.pages.items() if not p.draft}
        homes = [p for p in self.pages.values() if p.type == "home"]
        if len(homes) != 1:
            raise NativeError(f"{self.content}: 需要恰好 1 个 type=home 的页,实际 {len(homes)}")
        self.home = homes[0]
        if self.home.draft:
            raise NativeError(f"{self.home.path.name}: 游戏 hub 页不能是 draft")
        authors = [p for p in self.pub.values() if p.type == "author"]
        self.author_page = authors[0] if authors else None

        # 栏目:nav 配置 ↔ category 页 ↔ 文章 category 字段(三处一致,缺一处就报错)
        cats = {p.get("category"): p for p in self.pages.values() if p.type == "category"}
        by_slug = {p.slug: p for p in cats.values()}
        for s in self.nc.get("nav", []):
            if s not in by_slug:
                raise NativeError(f"native.nav 登记了 {s},但内容目录里没有 type=category 且 slug={s} 的页")
        for s in by_slug:
            if s not in self.nc.get("nav", []):
                self.warnings.append(f"栏目页 {s} 未在 native.nav 登记,不会进导航")
        self.cat_by_name = cats
        for p in self.pages.values():
            if p.type == "article" and p.get("category") not in cats:
                raise NativeError(f"{p.path.name}: category={p.get('category')!r} 没有对应的栏目页")
            for r in p.fm.get("related") or []:
                if r not in self.pages:
                    raise NativeError(f"{p.path.name}: related 指向不存在的页 {r}")

        # 栏目成员:栏目页正文里的卡片顺序在前,其余按主分类补齐;只收已发布文章
        self.members = {}
        arts = [p for p in self.pages.values() if p.type == "article"]
        for s in self.nc.get("nav", []):
            cp = by_slug[s]
            order = []
            for b in mdlite.parse(cp.body):
                if b["t"] == "h" and b["level"] >= 3:
                    tgt = self._card_target(b["text"])
                    if tgt and tgt not in order:
                        order.append(tgt)
            for a in arts:
                if a.get("category") == cp.get("category") and a.slug not in order:
                    order.append(a.slug)
            self.members[s] = [x for x in order if x in self.pub and self.pub[x].type == "article"]
        # 空栏目不上导航、不生成(空列表页 = thin content)
        self.nav = []
        for s in self.nc.get("nav", []):
            cp = by_slug[s]
            if cp.draft:
                continue
            if not self.members[s]:
                self.warnings.append(f"栏目 {s} 没有已发布文章,不生成、不进导航")
                continue
            self.nav.append(cp)
        self.live_cats = {c.slug for c in self.nav}

    def is_live(self, slug: str) -> bool:
        p = self.pub.get(slug)
        if not p:
            return False
        return p.type != "category" or slug in self.live_cats

    def _card_target(self, text):
        sl = mdlite.sole_link(text)
        if not sl:
            return None
        return self._internal_slug(sl[1])

    def _internal_slug(self, href):
        pre = f"/{self.gslug}/"
        h = href.split("#")[0]
        if not h.startswith(pre):
            return None
        rest = h[len(pre):].strip("/")
        return rest or self.home.slug

    # ------------------------------------------------------------ helpers
    def route(self, p) -> str:
        if isinstance(p, str):
            p = self.pages[p]
        return f"/{self.gslug}/" if p.type == "home" else f"/{self.gslug}/{p.slug}/"

    def url(self, p) -> str:
        return self.base + self.route(p)

    def image_for(self, p):
        shots = self.images.get("shots", {})
        key = self.images.get("pages", {}).get(p.slug) or self.images.get("default")
        return shots.get(key) if key else None

    def cat_of(self, p):
        return self.cat_by_name.get(p.get("category"))

    def author_name(self, p):
        return p.get("author") or self.nc.get("author", {}).get("name", "")

    def author_url(self):
        return self.url(self.author_page) if self.author_page else ""

    # ------------------------------------------------------------ components
    def link_cb_factory(self, page, ext_labels):
        def cb(href, inner):
            if href.startswith("#"):
                return f'<a href="{esc(href)}">{inner}</a>'
            tgt = self._internal_slug(href)
            if tgt is not None:
                if tgt not in self.pages:
                    raise NativeError(f"{page.path.name}: 站内链接指向不存在的页 {href}")
                if not self.is_live(tgt):
                    self.warnings.append(f"{page.path.name}: 链接 {href} 指向未发布页,已降级为纯文本")
                    return inner
                frag = "#" + href.split("#", 1)[1] if "#" in href else ""
                return f'<a href="{self.route(tgt)}{esc(frag)}">{inner}</a>'
            if href.startswith(("http://", "https://")):
                ext_labels.setdefault(href, re.sub(r"<[^>]+>", "", inner))
                return f'<a href="{esc(href)}"{self.ext_attrs(href)}>{inner}</a>'
            return f'<a href="{esc(href)}">{inner}</a>'
        return cb

    def ext_attrs(self, href):
        h = _host(href)
        official = any(h == d or h.endswith("." + d) for d in self.official)
        rel = "noopener" if official else "noopener nofollow"
        return f' target="_blank" rel="{rel}"'

    def article_cards(self, slugs, heading_level=3):
        items = []
        for s in slugs:
            p = self.pub[s]
            items.append(
                f'<li class="card"><h{heading_level} class="card-t"><a href="{self.route(p)}">{esc(p.get("title"))}</a></h{heading_level}>'
                f'<p>{esc(p.get("description"))}</p></li>'
            )
        return f'<ul class="cards">{"".join(items)}</ul>'

    def category_cards(self, labels):
        items = []
        for c in self.nav:
            name = labels.get(c.slug) or c.get("category")
            n = len(self.members[c.slug])
            items.append(
                f'<li class="card cat"><h3 class="card-t"><a href="{self.route(c)}">{esc(name)}</a></h3>'
                f'<p>{esc(c.get("description"))}</p>'
                f'<p class="count">{esc(self.t["article_count"].format(n=n))}</p></li>'
            )
        return f'<ul class="cards cats">{"".join(items)}</ul>'

    def all_articles_section(self, used_ids):
        hid = mdlite.slugify(self.t["all_articles"], used_ids)
        parts = [f'<h2 id="{hid}">{esc(self.t["all_articles"])}</h2>',
                 f'<p>{esc(self.t["all_articles_intro"])}</p>']
        for c in self.nav:
            prim = [s for s in self.members[c.slug] if self.pub[s].get("category") == c.get("category")]
            if not prim:
                continue
            parts.append(f'<h3><a href="{self.route(c)}">{esc(c.get("category"))}</a></h3>')
            parts.append("<ul class=\"linklist\">" + "".join(
                f'<li><a href="{self.route(s)}">{esc(self.pub[s].get("title"))}</a></li>' for s in prim) + "</ul>")
        return (hid, self.t["all_articles"]), "\n".join(parts)

    def byline(self, p):
        t, bits = self.t, []
        name = self.author_name(p)
        if name:
            au = self.author_url()
            nm = f'<a href="{self.route(self.author_page)}" rel="author">{esc(name)}</a>' if au else esc(name)
            bits.append(f'{esc(t["author"])} {nm}')
        for key, label in (("date", "published"), ("reviewed", "reviewed"), ("gameVersion", "game_version")):
            v = p.get(key)
            if v:
                inner = f'<time datetime="{esc(v)}">{esc(v)}</time>' if key != "gameVersion" else esc(v)
                bits.append(f'{esc(t[label])} {inner}')
        line = f'<p class="byline">{esc(t["sep"]).join(bits)}</p>' if bits else ""
        if p.type == "article" and p.get("scope"):
            line += f'<p class="scope">{esc(t["scope"])}{esc(t.get("colon", ": "))}{esc(p.get("scope"))}</p>'
        return line

    def crumbs(self, p):
        t = self.t
        items = [(t["home"], "/"), (self.nc.get("title") or self.g["name"], self.route(self.home))]
        if p.type == "article":
            c = self.cat_of(p)
            if c is not None:
                items.append((c.get("category"), self.route(c) if self.is_live(c.slug) else None))
            items.append((p.get("title"), None))
        elif p.type in ("category", "author"):
            items.append((p.get("category") if p.type == "category" else p.get("title"), None))
        else:
            items[-1] = (items[-1][0], None)
        html_items = []
        for k, (name, href) in enumerate(items):
            last = k == len(items) - 1
            if href and not last:
                html_items.append(f'<li><a href="{href}">{esc(name)}</a></li>')
            else:
                cur = ' aria-current="page"' if last else ""
                html_items.append(f'<li{cur}>{esc(name)}</li>')
        nav = (f'<nav class="crumbs" aria-label="{esc(t["breadcrumb"])}"><ol>'
               + "".join(html_items) + "</ol></nav>")
        ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": []}
        for k, (name, href) in enumerate(items, start=1):
            e = {"@type": "ListItem", "position": k, "name": name}
            if href:
                e["item"] = self.base + href
            elif k == len(items):
                e["item"] = self.url(p)
            ld["itemListElement"].append(e)
        return nav, ld

    def cover(self, p):
        im = self.image_for(p)
        if not im:
            return "", None
        srcset = ""
        if im.get("src_small"):
            srcset = (f' srcset="{esc(im["src_small"])} {im["small_w"]}w, {esc(im["src"])} {im["w"]}w"'
                      f' sizes="(max-width: 860px) 100vw, 820px"')
        credit = self.images.get("credit", "")
        fig = (f'<figure class="cover"><img src="{esc(im["src"])}"{srcset} width="{im["w"]}" height="{im["h"]}"'
               f' alt="{esc(im["alt"])}" loading="lazy" decoding="async">'
               + (f"<figcaption>{esc(credit)}</figcaption>" if credit else "") + "</figure>")
        return fig, im

    def header(self):
        t = self.t
        on = ' class="on"'
        games = "".join(
            f'<a href="{esc(h)}"{on if s == self.gslug else ""}>{esc(lbl)}</a>'
            for s, lbl, h in self.site["nav_games"])
        secs = "".join(f'<a href="{self.route(c)}">{esc(c.get("category"))}</a>' for c in self.nav)
        return (
            '<header class="hd">\n  <div class="wrap">\n'
            f'    <a class="brand" href="/"><b>&#9670;</b> {esc(self.cfg["brand"])}</a>\n'
            '    <nav class="hd-nav">\n'
            f'      <details class="gmenu"><summary>{esc(t["games"])}<span class="caret">&#9662;</span></summary>\n'
            f'        <div class="gmenu-panel">{games}<a class="all" href="/#games">{esc(t["all_games"])} &rarr;</a></div>\n'
            '      </details>\n'
            f'      <a class="gcur" href="{self.route(self.home)}">{esc(self.nc.get("title") or self.g["name"])}</a>\n'
            '    </nav>\n  </div>\n'
            f'  <nav class="secnav" aria-label="{esc(t["section_nav"])}"><div class="wrap">{secs}</div></nav>\n'
            '</header>'
        )

    def footer(self):
        t = self.t
        links = "".join(f'<a href="{esc(h)}">{esc(n)}</a>' for n, h in t["trust"])
        if self.author_page:
            links += f'<a href="{self.route(self.author_page)}">{esc(t["author"])}</a>'
        return (
            '<footer class="ft">\n  <div class="wrap">\n'
            f'    <nav>{links}</nav>\n'
            f'    <p>&copy; {self.site["year"]} {esc(self.cfg["brand"])}. {esc(t["footer_note"])}</p>\n'
            '  </div>\n</footer>'
        )

    # ------------------------------------------------------------ page build
    def build_page(self, p):
        t = self.t
        blocks = mdlite.parse(p.body)
        # 1) H1:取正文第一个 H1 做页面标题(只出一次),其余 H1 降级
        h1_text = None
        kept = []
        for b in blocks:
            if b["t"] == "h" and b["level"] == 1:
                if h1_text is None:
                    h1_text = b["text"]
                    continue
                self.warnings.append(f"{p.path.name}: 多余的 H1 已降为 H2")
                b = dict(b, level=2)
            kept.append(b)
        blocks = kept
        h1_text = h1_text or p.get("title")

        # 2) 正文末尾的「相关阅读」小节 → 由 frontmatter.related 统一渲染,不在正文里重复
        rh = self.nc.get("related_heading")
        if rh:
            for k, b in enumerate(blocks):
                if b["t"] == "h" and b["level"] == 2 and mdlite.plain(b["text"]) == rh:
                    tail = blocks[k + 1:]
                    if any(x["t"] == "h" and x["level"] <= 2 for x in tail):
                        break
                    linked = [self._internal_slug(h) for x in tail if x["t"] in ("ul", "ol", "p")
                              for it in (x.get("items") or [x.get("text", "")]) for _, h in mdlite.links_in(it)]
                    if [s for s in linked if s] != list(p.fm.get("related") or []):
                        self.warnings.append(f"{p.path.name}: 「{rh}」小节与 related 不一致,以 related 为准")
                    blocks = blocks[:k]
                    break

        # 3) 卡片块(### [标题](/game/slug/) + 说明段)→ 按数据重渲染(过滤草稿;栏目页按成员表)
        out, card_done = [], False
        i = 0
        while i < len(blocks):
            b = blocks[i]
            tgt = self._card_target(b["text"]) if b["t"] == "h" and b["level"] >= 3 else None
            if tgt and tgt in self.pages and self.pages[tgt].type == "article":
                i += 1
                if i < len(blocks) and blocks[i]["t"] == "p":
                    i += 1
                if not card_done:
                    slugs = self.members.get(p.slug) if p.type == "category" else None
                    if slugs is None:
                        slugs = [tgt] if self.is_live(tgt) else []
                    else:
                        card_done = True
                    if slugs:
                        out.append({"t": "html", "html": self.article_cards(slugs, b["level"])})
                continue
            # 4) 整个列表都是栏目页链接 → 栏目卡片
            if b["t"] in ("ul", "ol") and b["items"]:
                sl = [mdlite.sole_link(x) for x in b["items"]]
                if all(sl) and all(self.pages.get(self._internal_slug(h) or "", None) is not None
                                   and self.pages[self._internal_slug(h)].type == "category" for _, h in sl):
                    labels = {self._internal_slug(h): mdlite.plain(txt) for txt, h in sl}
                    out.append({"t": "html", "html": self.category_cards(labels)})
                    i += 1
                    continue
            out.append(b)
            i += 1
        blocks = out

        # 5) 标题锚点 + 目录
        used, toc = set(), []
        for b in blocks:
            if b["t"] == "h" and b["level"] in (2, 3):
                b["id"] = mdlite.slugify(b["text"], used)
                if b["level"] == 2:
                    toc.append((b["id"], mdlite.plain(b["text"])))

        ext_labels = {}
        body_html = mdlite.render(blocks, self.link_cb_factory(p, ext_labels), t.get("table_label", "table"))

        extra = []
        if p.type == "home":
            (hid, lbl), sec = self.all_articles_section(used)
            extra.append(sec)
            toc.append((hid, lbl))
        if p.type == "author":
            hid = mdlite.slugify(t["author_articles"], used)
            name = self.author_name(p)
            mine = [s for c in self.nav for s in self.members[c.slug]
                    if self.pub[s].get("category") == c.get("category") and self.author_name(self.pub[s]) == name]
            extra.append(f'<h2 id="{hid}">{esc(t["author_articles"].format(name=name))}</h2>'
                         + self.article_cards(mine))
            toc.append((hid, t["author_articles"].format(name=name)))

        # 来源(S001…,访问日期 = checkedAt)
        srcs = p.fm.get("sourceUrls") or []
        if srcs:
            hid = mdlite.slugify(t["sources"], used)
            acc = p.get("checkedAt")
            lis = []
            for k, u in enumerate(srcs, start=1):
                label = ext_labels.get(u) or _host(u)
                lis.append(
                    f'<li id="s{k:03d}"><span class="sid">S{k:03d}</span> '
                    f'<a href="{esc(u)}"{self.ext_attrs(u)}>{esc(label)}</a>'
                    f' <span class="shost">{esc(_host(u))}</span>'
                    + (f' <span class="sdate">{esc(t["accessed"])} <time datetime="{esc(acc)}">{esc(acc)}</time></span>' if acc else "")
                    + "</li>")
            for u in ext_labels:
                if u not in srcs:
                    self.warnings.append(f"{p.path.name}: 正文外链 {u} 不在 sourceUrls 里")
            extra.append(f'<section class="sources"><h2 id="{hid}">{esc(t["sources"])}</h2>'
                         f'<p>{esc(t["sources_intro"])}</p><ol>{"".join(lis)}</ol></section>')
            toc.append((hid, t["sources"]))

        rel = [s for s in (p.fm.get("related") or []) if self.is_live(s) and self.pub[s].type == "article"]
        if rel:
            hid = mdlite.slugify(t["related"], used)
            extra.append(f'<section class="related"><h2 id="{hid}">{esc(t["related"])}</h2>'
                         + self.article_cards(rel) + "</section>")
            toc.append((hid, t["related"]))

        toc_html = ""
        if len(toc) >= 5:
            toc_html = (f'<nav class="toc" aria-label="{esc(t["toc"])}"><p class="toc-t">{esc(t["toc"])}</p><ol>'
                        + "".join(f'<li><a href="#{esc(i)}">{esc(l)}</a></li>' for i, l in toc) + "</ol></nav>")

        crumbs_html, crumbs_ld = self.crumbs(p)
        fig, im = self.cover(p)
        h1_html = mdlite.inline(mdlite.plain(h1_text))

        main = (
            f'<main class="native">\n<div class="wrap narrow">\n{crumbs_html}\n'
            f'<article class="doc">\n<div class="doc-hd"><h1>{h1_html}</h1>\n{self.byline(p)}</div>\n'
            f'{fig}\n{toc_html}\n<div class="prose">\n{body_html}\n{"".join(extra)}\n</div>\n'
            '</article>\n</div>\n</main>'
        )

        # JSON-LD
        graphs = []
        page_url = self.url(p)
        publisher = {"@type": "Organization", "name": self.cfg["brand"], "url": self.base + "/",
                     "logo": {"@type": "ImageObject", "url": self.base + "/favicon.svg"}}
        person = {"@type": "Person", "name": self.author_name(p)}
        if self.author_url():
            person["url"] = self.author_url()
        if p.type == "article":
            art = {"@context": "https://schema.org", "@type": "Article",
                   "headline": mdlite.plain(h1_text), "description": p.get("description"),
                   "inLanguage": self.g.get("lang"), "mainEntityOfPage": page_url, "url": page_url,
                   "datePublished": p.get("date"), "dateModified": self.modified(p),
                   "author": person, "publisher": publisher,
                   "about": {"@type": "VideoGame", "name": self.g["name"]}}
            if im:
                art["image"] = {"@type": "ImageObject", "url": im["src"], "width": im["w"], "height": im["h"]}
            c = self.cat_of(p)
            if c is not None:
                art["articleSection"] = c.get("category")
            graphs.append(art)
        elif p.type == "author":
            graphs.append({"@context": "https://schema.org", "@type": "ProfilePage", "url": page_url,
                           "name": p.get("title"), "inLanguage": self.g.get("lang"),
                           "mainEntity": dict(person, jobTitle=t.get("author_role", ""))})
        else:
            cp = {"@context": "https://schema.org", "@type": "CollectionPage", "url": page_url,
                  "name": p.get("title"), "description": p.get("description"),
                  "inLanguage": self.g.get("lang"),
                  "isPartOf": {"@type": "WebSite", "name": self.cfg["brand"], "url": self.base + "/"},
                  "about": {"@type": "VideoGame", "name": self.g["name"]}}
            if p.type == "home":
                cp["dateModified"] = self.modified(p)
            graphs.append(cp)
        graphs.append(crumbs_ld)

        title = p.get("seoTitle") or mdlite.plain(h1_text)
        desc = p.get("description")
        og_type = "article" if p.type == "article" else "website"
        head = [
            f"<title>{esc(title)}</title>",
            f'<meta name="description" content="{esc(desc)}">',
            f'<link rel="canonical" href="{esc(page_url)}">',
            f'<meta property="og:type" content="{og_type}">',
            f'<meta property="og:site_name" content="{esc(self.cfg["brand"])}">',
            f'<meta property="og:locale" content="{esc(t["og_locale"])}">',
            f'<meta property="og:title" content="{esc(title)}">',
            f'<meta property="og:description" content="{esc(desc)}">',
            f'<meta property="og:url" content="{esc(page_url)}">',
        ]
        if im:
            head += [f'<meta property="og:image" content="{esc(im["src"])}">',
                     f'<meta property="og:image:width" content="{im["w"]}">',
                     f'<meta property="og:image:height" content="{im["h"]}">',
                     f'<meta property="og:image:alt" content="{esc(im["alt"])}">']
        if p.type == "article":
            head += [f'<meta property="article:published_time" content="{esc(p.get("date"))}">',
                     f'<meta property="article:modified_time" content="{esc(self.modified(p))}">']
        head.append('<meta name="twitter:card" content="summary_large_image">')
        head += [ld_script(x) for x in graphs]

        theme = self.nc.get("theme", {})
        theme_css = ""
        if theme:
            theme_css = "<style>:root{" + ";".join(f"--{k}:{v}" for k, v in theme.items()) + "}</style>"

        tpl = (self.root / "hub" / "native_page.html").read_text(encoding="utf-8")
        html = (tpl.replace("{{LANG}}", esc(t["html_lang"]))
                .replace("{{HEAD}}", "\n".join(head))
                .replace("{{THEME}}", theme_css)
                .replace("{{HEAD_EXTRA}}", self.site["head_extra"])
                .replace("{{HEADER}}", self.header())
                .replace("{{MAIN}}", main)
                .replace("{{FOOTER}}", self.footer()))
        return html

    def modified(self, p):
        """结构化数据的修改时间:取 date/updated/reviewed 中最晚的,避免早于发布日。"""
        return max(x for x in (p.get("date"), p.get("updated"), p.get("reviewed")) if x) if (
            p.get("date") or p.get("updated") or p.get("reviewed")) else ""

    def lastmod(self, p):
        return p.get("reviewed") or p.get("updated") or p.get("date") or self.site["today"]

    def build(self, out_root: Path):
        """写出全部已发布页,返回 {route: lastmod}。"""
        dst = out_root / self.gslug
        routes = {}
        for p in self.pub.values():
            if p.type == "category" and p.slug not in self.live_cats:
                continue
            html = self.build_page(p)
            target = dst / "index.html" if p.type == "home" else dst / p.slug / "index.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(html, encoding="utf-8")
            routes[self.route(p)] = self.lastmod(p)
        for w in dict.fromkeys(self.warnings):
            print(f"  [{self.gslug}] 警告: {w}")
        drafts = sorted(s for s, p in self.pages.items() if p.draft)
        print(f"  [{self.gslug}] native: 生成 {len(routes)} 页,草稿跳过 {len(drafts)}"
              + (f"({', '.join(drafts)})" if drafts else ""))
        return routes
