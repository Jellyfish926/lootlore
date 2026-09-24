"""native —— 原生内容游戏(config/hub.json 里 kind=native)的渲染器。框架层。v2。

输入:<game.content>/<lang.dir>/*.md(frontmatter + 正文,正文自带 H1)
     + <game.content>/_images.json(alt/credit 按语种分 key)
     + config/i18n/<lang.i18n>.json(界面文字)
     + <native.entities> 指向的结构化数据 JSON(可选)
     + hub.json 该游戏的 native 配置块。
输出:out/<slug>/<lang.prefix>/index.html 与 out/<slug>/<lang.prefix>/<page>/index.html,
     另有 out/<slug>/search-index.json(站内搜索索引,全语种一份)。

本文件不含任何具体游戏的文字;换游戏只动配置层与内容层。
页型由 frontmatter.type 决定:home / category / article / author,外加构建期生成的 all 页。
draft: true 的页不生成、不进 sitemap、不进栏目列表与 hub 清单、不进关联阅读;
正文里指向草稿的站内链接降级为纯文本(否则就是死链)。
"""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

from hub import mdlite, shell
from hub.hubbody import HubBodyMixin
from hub.mdlite import esc
from hub.pageindex import GameIndex, PageRef, Section


class NativeError(Exception):
    pass


def ld_script(obj) -> str:
    """统一 JSON-LD 输出:紧凑 JSON + 转义 < > &,防止正文里的字符提前闭合 <script>。"""
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    s = s.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return f'<script type="application/ld+json">{s}</script>'


def _host(url: str) -> str:
    return (urlparse(url).hostname or "").lower()


# 排序表(栏目聚合表的 <th> 点击排序)。内联,压到 1KB 以内,门禁上限 3KB。
SORT_JS = (
    "<script>document.querySelectorAll('table[data-sortable]').forEach(function(t){"
    "var hs=[].slice.call(t.tHead.rows[0].cells);hs.forEach(function(th,i){"
    "th.tabIndex=0;th.setAttribute('role','button');"
    "function go(){var b=t.tBodies[0],rs=[].slice.call(b.rows),"
    "d=th.getAttribute('aria-sort')==='ascending'?-1:1;"
    "rs.sort(function(x,y){var a=x.cells[i],c=y.cells[i];"
    "var av=a.getAttribute('data-v')||a.textContent.trim(),cv=c.getAttribute('data-v')||c.textContent.trim();"
    "var an=parseFloat(av),cn=parseFloat(cv);"
    "if(!isNaN(an)&&!isNaN(cn)&&av!==''&&cv!=='')return (an-cn)*d;"
    "return av.localeCompare(cv)*d;});"
    "rs.forEach(function(x){b.appendChild(x);});"
    "hs.forEach(function(o){o.removeAttribute('aria-sort');});"
    "th.setAttribute('aria-sort',d===1?'ascending':'descending');}"
    "th.addEventListener('click',go);"
    "th.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();go();}});"
    "});});</script>"
)

# 站内搜索的前端过滤脚本由 hub/shell.py 统一提供(全站一份索引,跨全部游戏)。
SEARCH_JS = shell.SEARCH_JS
# 顶栏巨菜单的关闭行为(点外面 / Esc)。搜索关掉的页也必须有,否则菜单挂着挡正文链接。
NAV_JS = shell.NAV_JS


class Page:
    def __init__(self, path: Path, fm: dict, body: str):
        self.path, self.fm, self.body = path, fm, body
        self.slug = str(fm.get("slug") or path.stem)
        self.type = fm.get("type") or "article"
        self.draft = fm.get("draft") is True

    def get(self, k, default=""):
        v = self.fm.get(k)
        return default if v is None or v == "" else v


# ===========================================================================
#  实体信息框渲染器(原生内容页与快照套壳页共用)
# ===========================================================================
class EntityBox:
    """把一条实体数据渲染成右栏「速查」信息框。

    宿主只需提供:t(界面文字 dict)、nk(语种数据 key)、lang_keys(实体字段的语种后缀集合)、
    ents(实体表)、route_slug(slug → 路由)、is_live(slug 是否有页)。
    字段标签一律来自 config/i18n 的 f_<字段名>;没登记标签的字段不渲染 —— 框架层不认识字段含义。
    数据缺失 / 一行都凑不出来时返回空串,由调用方决定不渲染,绝不出空框或占位值。
    """

    # 通用 key/value 信息框不显示的字段:实体数据管线的元信息,不是给读者看的事实。
    KV_SKIP = ("type", "order", "page_slug", "source_urls", "accessed",
               "unverified_fields", "name", "summary")

    def loc(self, obj, key, default=""):
        """实体字段的语种回退:<key>_<nk> → <key>_en → <key>。"""
        for k in (f"{key}_{self.nk}", f"{key}_en", key):
            v = obj.get(k)
            if v not in (None, "", []):
                return v
        return default

    def _hp(self, ent):
        """hp 为 null 但给了分阶段血量时,按阶段串起来显示。"""
        if ent.get("hp") not in (None, ""):
            return ent["hp"]
        ph = ent.get("hp_phases")
        return " + ".join(str(x) for x in ph) if ph else ""

    def _list(self, rows):
        """[{en, zh}] 或 [str] → 按语种取值的纯文本列表;传进来不是列表就当空。"""
        if isinstance(rows, str):
            return [rows] if rows else []
        out = []
        for x in rows or []:
            v = (x.get(self.nk) or x.get("en") or "") if isinstance(x, dict) else str(x)
            if v:
                out.append(v)
        return out

    def _ent_names(self, rows, key="item"):
        return ", ".join(str(self.loc(r, key)) for r in rows)

    def _base_key(self, key):
        """去掉字段名上的语种后缀:hazards_en / name_zh → hazards / name。"""
        for lk in self.lang_keys:
            if lk and key.endswith(f"_{lk}"):
                return key[: -len(lk) - 1]
        return key

    def _kv_rows(self, ent):
        """实体里非 null 的标量/短列表字段 → [(标签, 文本)]。
        标签取 config/i18n 的 f_<字段名>;没有登记标签的字段不渲染(代码层不认识字段含义)。"""
        rows, seen = [], set()
        for key in ent:
            base = self._base_key(key)
            if base in self.KV_SKIP or base in seen:
                continue
            seen.add(base)
            label = self.t.get(f"f_{base}")
            v = self.loc(ent, base)
            if not label or v in (None, "", [], {}):
                continue
            if isinstance(v, (dict,)):
                continue
            if isinstance(v, bool):
                # 布尔字段按界面语言写"是/否",不许把 Python 的 True/False 漏到页面上
                v = self.t["yes"] if v else self.t["no"]
            elif isinstance(v, list):
                v = ", ".join(str(x) for x in self._list(v))
                if not v:
                    continue
            rows.append((label, str(v)))
        return rows

    def quick_facts(self, ent, first=True, generic=False):
        """generic=True:不按 type 走预设字段表,一律"summary 当引言 + 其余已登记字段列成行"。
        快照游戏的实体 schema 是各子站自己的形状(achievement / threat / turret / hero …),
        没有 boss/biome/item 那套固定字段,所以走通用路径 —— 字段含义仍由 config/i18n 的
        f_<字段名> 决定,没登记标签的字段不渲染。"""
        t = self.t
        rows = []

        def add(label, value):
            if value in (None, "", []):
                return
            if isinstance(value, list):
                value = ", ".join(str(x) for x in value)
            rows.append((label, str(value)))

        typ = ent.get("type")
        lead = ""
        if generic or typ == "mechanic":
            # 通用 key/value:字段清单来自数据,标签来自 i18n,本文件不认识任何字段的含义。
            rows = self._kv_rows(ent)
            lead = str(self.loc(ent, "summary") or "")
        elif typ == "boss":
            add(t["f_biome"], self.loc(ent, "biome"))
            add(t["f_summon"], ", ".join(
                f'{self.loc(r, "item")} ×{r["qty"]}' for r in (ent.get("summon") or [])))
            add(t["f_health"], self._hp(ent))
            add(t["f_damage"], ent.get("damage_types"))
            add(t["f_weak"], ent.get("weak"))
            add(t["f_resistant"], ent.get("resistant"))
            add(t["f_very_resistant"], ent.get("very_resistant"))
            add(t["f_immune"], ent.get("immune"))
            add(t["f_drops"], self._ent_names(ent.get("drops") or []))
            fp = ent.get("forsaken_power")
            if fp:
                add(t["f_forsaken"], f'{self.loc(fp, "name")}{t["colon"]}{self.loc(fp, "effect")}'
                    if self.loc(fp, "effect") else self.loc(fp, "name"))
            add(t["f_unlocks"], self.loc(ent, "unlocks"))
        elif typ == "biome":
            b = ent.get("boss")
            if b and b in self.ents:
                bn = self.loc(self.ents[b], "name")
                bs = self.ents[b].get("page_slug")
                add(t["f_boss"], f'<a href="{self.route_slug(bs)}">{esc(bn)}</a>'
                    if bs and self.is_live(bs) else esc(bn))
            add(t["f_key_resources"], self._list(ent.get("key_resources")))
            add(t["f_enemies"], self._list(ent.get("enemies")))
            add(t["f_unlocks"], self._list(ent.get("unlocks")))
            add(t["f_hazards"], self.loc(ent, "hazards"))
        else:
            add(t["c_entry_table"], self.loc(ent, "summary"))
            add(t["f_station"], self.loc(ent, "crafted_at") or self.loc(ent, "source"))
            add(t["f_requires"], self.loc(ent, "requires"))
            add(t["f_unlocked_by"], self.loc(ent, "unlocked_by"))
            add(t["f_usage"], self.loc(ent, "usage"))
            add(t["f_cargo"], ent.get("cargo_slots"))
            add(t["f_durability"], ent.get("durability"))
            add(t["f_crafts_quantity"], ent.get("crafts_quantity"))
            add(t["f_weight"], ent.get("weight"))
            add(t["f_stack"], ent.get("stack"))
            add(t["c_material"], ", ".join(
                f'{self.loc(r, "item")} ×{r["qty"]}' for r in (ent.get("recipe") or [])))
        if not rows and not lead:
            return ""
        body = "".join(f'<div class="qf-r"><dt>{esc(k)}</dt><dd>{v if k == t["f_boss"] else esc(v)}</dd></div>'
                       for k, v in rows)
        name = self.loc(ent, "name")
        if not str(name).strip():
            return ""
        # 移动端一律折叠(桌面由 native.css 的 ::details-content 强制展开),
        # 否则首个信息框会把正文首屏整块推下去。first 只保留给未来排序用。
        open_attr = ""
        return (f'<details class="qf"{open_attr}><summary class="qf-h">{esc(name)}</summary>'
                f'<p class="qf-sub">{esc(self.t["quick_facts"])}</p>'
                + (f'<p class="qf-lead">{esc(lead)}</p>' if lead else "")
                + f'<dl>{body}</dl></details>')


# ===========================================================================
#  单语种渲染器
# ===========================================================================
class NativeLang(EntityBox, HubBodyMixin):
    def __init__(self, game_site, spec: dict):
        self.site_game = game_site
        self.root, self.g, self.cfg, self.site = (
            game_site.root, game_site.g, game_site.cfg, game_site.site)
        self.nc = game_site.nc
        self.gslug = game_site.gslug
        self.base = game_site.base
        self.spec = spec
        self.code = spec["code"]            # <html lang> / hreflang
        self.nk = spec["dir"]               # 语种数据 key:_images.json 的 alt、entities 的 name_<nk>
        self.prefix = spec.get("prefix", "").strip("/")
        self.default = bool(spec.get("default"))
        self.warnings = game_site.warnings
        self.t = json.loads(
            (self.root / "config" / "i18n" / f'{spec["i18n"]}.json').read_text(encoding="utf-8"))
        self.images = game_site.images
        self.ents = game_site.ents
        self.lang_keys = game_site.lang_keys
        self.official = game_site.official
        self.content = self.root / self.g["content"] / spec["dir"]
        self.alternates = {}   # slug -> [(hreflang, route, label)]
        self._load()

    # ------------------------------------------------------------ loading
    def _load(self):
        defaults = self.nc.get("defaults", {})
        self.pages = {}
        for p in sorted(self.content.glob("*.md")):
            if p.name.startswith("_"):
                continue
            # 内容层写 {{BRAND}},品牌名的唯一真相源仍是 config/hub.json —— 改名不用动内容。
            raw = p.read_text(encoding="utf-8").replace("{{BRAND}}", self.cfg["brand"])
            fm, body = mdlite.split_frontmatter(raw)
            for k, v in defaults.items():
                if fm.get(k) in (None, ""):
                    fm[k] = v
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
                raise NativeError(f"{self.nk}/{p.name}: frontmatter url={fm['url']} 与路由规则 {want} 不一致")
            if fm.get("language") and fm["language"] != self.code:
                self.warnings.append(f"{self.nk}/{p.name}: language={fm['language']} 与语种 {self.code} 不同")
        self.pub = {s: p for s, p in self.pages.items() if not p.draft}
        homes = [p for p in self.pages.values() if p.type == "home"]
        if len(homes) != 1:
            raise NativeError(f"{self.content}: 需要恰好 1 个 type=home 的页,实际 {len(homes)}")
        self.home = homes[0]
        if self.home.draft:
            raise NativeError(f"{self.home.path.name}: 游戏 hub 页不能是 draft")
        authors = [p for p in self.pub.values() if p.type == "author"]
        self.author_page = authors[0] if authors else None

        cats = {p.get("category"): p for p in self.pages.values() if p.type == "category"}
        by_slug = {p.slug: p for p in cats.values()}
        for s in self.nc.get("nav", []):
            if s not in by_slug:
                raise NativeError(f"native.nav 登记了 {s},但 {self.nk}/ 里没有 type=category 且 slug={s} 的页")
        for s in by_slug:
            if s not in self.nc.get("nav", []):
                self.warnings.append(f"{self.nk}: 栏目页 {s} 未在 native.nav 登记,不会进导航")
        self.cat_by_name = cats
        for p in self.pages.values():
            if p.type == "article" and p.get("category") not in cats:
                raise NativeError(f"{self.nk}/{p.path.name}: category={p.get('category')!r} 没有对应的栏目页")
            for r in p.fm.get("related") or []:
                if r not in self.pages:
                    raise NativeError(f"{self.nk}/{p.path.name}: related 指向不存在的页 {r}")

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
        self.nav = []
        for s in self.nc.get("nav", []):
            cp = by_slug[s]
            if cp.draft:
                continue
            if not self.members[s]:
                self.warnings.append(f"{self.nk}: 栏目 {s} 没有已发布文章,不生成、不进导航")
                continue
            self.nav.append(cp)
        self.live_cats = {c.slug for c in self.nav}
        # 主分类内的顺序,用于上一篇/下一篇
        self.seq = {}
        for c in self.nav:
            prim = [s for s in self.members[c.slug] if self.pub[s].get("category") == c.get("category")]
            for k, s in enumerate(prim):
                self.seq[s] = (prim[k - 1] if k else None, prim[k + 1] if k + 1 < len(prim) else None)

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
        pre = "/" + "/".join(x for x in (self.gslug, self.prefix) if x) + "/"
        h = href.split("#")[0]
        if not h.startswith(pre):
            return None
        rest = h[len(pre):].strip("/")
        if rest and "/" in rest:
            return None
        return rest or self.home.slug

    # ------------------------------------------------------------ helpers
    def route(self, p) -> str:
        if isinstance(p, str):
            p = self.pages[p]
        parts = [self.gslug, self.prefix] + ([] if p.type == "home" else [p.slug])
        return "/" + "/".join(x for x in parts if x) + "/"

    def route_slug(self, slug: str) -> str:
        parts = [self.gslug, self.prefix, slug]
        return "/" + "/".join(x for x in parts if x) + "/"

    def url(self, p) -> str:
        return self.base + self.route(p)

    def alt_of(self, im):
        a = im.get("alt")
        return (a.get(self.nk) or a.get("en") or "") if isinstance(a, dict) else (a or "")

    def credit(self):
        c = self.images.get("credit", "")
        return (c.get(self.nk) or c.get("en") or "") if isinstance(c, dict) else c

    def shot(self, key):
        return self.images.get("shots", {}).get(key)

    def image_for(self, p):
        imgs = p.fm.get("images") or []
        key = (imgs[0] if imgs else None) or self.images.get("pages", {}).get(p.slug) or self.images.get("default")
        return self.shot(key) if key else None

    def card_image(self, p):
        """给全站索引用的卡片图:这一页在 _images.json 里映射到的官方截图,推小图变体。
        w/h 用小图的真实尺寸,与 <img> 属性一致,避免布局位移。alt 按语种取。"""
        im = self.image_for(p)
        if not im:
            return None
        src = im.get("src_small") or im.get("src")
        if not src:
            return None
        w = im.get("small_w") if im.get("src_small") else im.get("w")
        base_w, base_h = im.get("w"), im.get("h")
        if not (w and base_w and base_h):
            return None
        return {"src": src, "w": w, "h": round(w * base_h / base_w), "alt": self.alt_of(im)}

    def cat_of(self, p):
        return self.cat_by_name.get(p.get("category"))

    def author_name(self, p):
        return p.get("author") or self.nc.get("author", {}).get("name", "")

    def author_url(self):
        return self.url(self.author_page) if self.author_page else ""

    def entities_of(self, p):
        ids = ([p.get("entity")] if p.get("entity") else []) + list(p.fm.get("entities") or [])
        out = []
        for e in ids:
            if e in self.ents:
                out.append(self.ents[e])
            elif e:
                self.warnings.append(f"{self.nk}/{p.path.name}: entity {e} 不在实体数据里,已跳过")
        return out

    # ------------------------------------------------------------ inline cbs
    def link_cb_factory(self, page, ext_labels):
        def cb(href, inner):
            if href.startswith("#"):
                return f'<a href="{esc(href)}">{inner}</a>'
            tgt = self._internal_slug(href)
            if tgt is not None:
                if tgt not in self.pages:
                    raise NativeError(f"{self.nk}/{page.path.name}: 站内链接指向不存在的页 {href}")
                if not self.is_live(tgt):
                    self.warnings.append(f"{self.nk}/{page.path.name}: 链接 {href} 指向未发布页,已降级为纯文本")
                    return inner
                frag = "#" + href.split("#", 1)[1] if "#" in href else ""
                return f'<a href="{self.route(tgt)}{esc(frag)}">{inner}</a>'
            if href.startswith(("http://", "https://")):
                ext_labels.setdefault(href, re.sub(r"<[^>]+>", "", inner))
                return f'<a href="{esc(href)}"{self.ext_attrs(href)}>{inner}</a>'
            return f'<a href="{esc(href)}">{inner}</a>'
        return cb

    def _resolve_img(self, src, alt):
        """src 既可以是 _images.json 的 key(ssNN),也可以是绝对地址。"""
        im = self.shot(src)
        if im:
            return dict(im, alt=alt or self.alt_of(im))
        if src.startswith(("http://", "https://", "/")):
            return {"src": src, "w": None, "h": None, "alt": alt}
        raise NativeError(f"{self.nk}: 图片 key {src} 不在 _images.json 的 shots 里")

    def img_cb_factory(self, page):
        def cb(src, alt, title):
            im = self._resolve_img(src, alt)
            body_src = im.get("src_small") or im["src"]
            w = im.get("small_w") or im.get("w")
            h = int(round(w * im["h"] / im["w"])) if im.get("w") else None
            wh = f' width="{w}" height="{h}"' if w else ""
            return (f'<img src="{esc(body_src)}"{wh} alt="{esc(im["alt"])}"'
                    f' loading="lazy" decoding="async">')
        return cb

    def figure_cb_factory(self, page):
        def cb(src, alt, title):
            im = self._resolve_img(src, alt)
            body_src = im.get("src_small") or im["src"]
            w = im.get("small_w") or im.get("w")
            h = int(round(w * im["h"] / im["w"])) if im.get("w") else None
            wh = f' width="{w}" height="{h}"' if w else ""
            srcset = ""
            if im.get("src_small"):
                srcset = (f' srcset="{esc(im["src_small"])} {im["small_w"]}w, {esc(im["src"])} {im["w"]}w"'
                          f' sizes="(max-width: 860px) 100vw, 760px"')
            cap = title or im["alt"]
            cr = self.credit()
            capline = esc(cap) + (f'<span class="fig-src">{esc(self.t["sep"])}{esc(cr)}</span>' if cr else "")
            return (f'<figure class="body-fig"><img src="{esc(body_src)}"{srcset}{wh}'
                    f' alt="{esc(im["alt"])}" loading="lazy" decoding="async">'
                    f'<figcaption>{capline}</figcaption></figure>')
        return cb

    def ext_attrs(self, href):
        h = _host(href)
        official = any(h == d or h.endswith("." + d) for d in self.official)
        rel = "noopener" if official else "noopener nofollow"
        return f' target="_blank" rel="{rel}"'

    # ------------------------------------------------------------ cards
    def _thumb(self, p):
        im = self.image_for(p)
        if not im:
            return ""
        src = im.get("src_small") or im["src"]
        w = im.get("small_w") or im["w"]
        h = int(round(w * im["h"] / im["w"])) if im.get("w") else None
        wh = f' width="{w}" height="{h}"' if h else ""
        return (f'<img class="thumb" src="{esc(src)}"{wh} alt="{esc(self.alt_of(im))}"'
                f' loading="lazy" decoding="async">')

    def _badge(self, p):
        v = p.get("gameVersion")
        return f'<span class="badge">{esc(self.t["checked_badge"].format(v=v))}</span>' if v else ""

    def article_cards(self, slugs, heading_level=3, thumbs=True):
        items = []
        for s in slugs:
            p = self.pub[s]
            th = f'<a class="card-img" href="{self.route(p)}" tabindex="-1" aria-hidden="true">{self._thumb(p)}</a>' if thumbs else ""
            items.append(
                f'<li class="card">{th}<div class="card-b">'
                f'<h{heading_level} class="card-t"><a href="{self.route(p)}">{esc(p.get("title"))}</a></h{heading_level}>'
                f'<p>{esc(p.get("description"))}</p>{self._badge(p)}</div></li>')
        return f'<ul class="cards{" with-img" if thumbs else ""}">{"".join(items)}</ul>'

    def category_tiles(self):
        items = []
        for c in self.nav:
            n = len(self.members[c.slug])
            items.append(
                f'<li class="tile"><a class="tile-img" href="{self.route(c)}" tabindex="-1" aria-hidden="true">'
                f'{self._thumb(c)}</a><div class="card-b">'
                f'<h3 class="card-t"><a href="{self.route(c)}">{esc(c.get("category"))}</a></h3>'
                f'<p>{esc(c.get("description"))}</p>'
                f'<p class="count">{esc(self.t["article_count"].format(n=n))}</p></div></li>')
        return f'<ul class="tiles">{"".join(items)}</ul>'

    def prevnext(self, p):
        pn = self.seq.get(p.slug)
        if not pn or not any(pn):
            return ""
        prev, nxt = pn
        bits = []
        if prev and self.is_live(prev):
            bits.append(f'<a class="pn prev" href="{self.route(prev)}">'
                        f'<span>{esc(self.t["prev_guide"])}</span>{esc(self.pub[prev].get("title"))}</a>')
        if nxt and self.is_live(nxt):
            bits.append(f'<a class="pn next" href="{self.route(nxt)}">'
                        f'<span>{esc(self.t["next_guide"])}</span>{esc(self.pub[nxt].get("title"))}</a>')
        return f'<nav class="prevnext" aria-label="{esc(self.t["related"])}">{"".join(bits)}</nav>' if bits else ""

    # ------------------------------------------------------------ entity components
    def _table(self, head, rows, label=None, sortable=False):
        sortattr = ' data-sortable="1"' if sortable else ""
        # 整列都是数字的列右对齐(见 native.css 的 .num)
        num = [
            any(mdlite.plain(str(r[k])).strip() for r in rows if k < len(r))
            and all(mdlite.is_numeric_cell(mdlite.plain(str(r[k]))) for r in rows
                    if k < len(r) and mdlite.plain(str(r[k])).strip())
            for k in range(len(head))
        ]
        cl = [' class="num"' if n else "" for n in num]
        thead = "".join(
            "<th" + cl[k]
            + (f' title="{esc(self.t["sort_by"].format(col=mdlite.plain(h)))}"' if sortable else "")
            + f">{h}</th>" for k, h in enumerate(head))
        tbody = "".join(
            "<tr>" + "".join(f"<td{cl[k] if k < len(cl) else ''}>{c}</td>" for k, c in enumerate(r))
            + "</tr>" for r in rows)
        return (f'<div class="table-scroll" role="region" tabindex="0"'
                f' aria-label="{esc(label or self.t["table_label"])}">'
                f"<table{sortattr}><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table></div>")

    def entity_tables(self, ent, used):
        """返回 [(heading_id, label, html)],表都套在横滑容器里。"""
        t, out = self.t, []

        def block(label, head, rows):
            hid = mdlite.slugify(label, used)
            out.append((hid, label,
                        f'<h2 id="{hid}">{esc(label)}</h2>' + self._table(head, rows, label)))

        typ = ent.get("type")
        if typ == "boss":
            if ent.get("summon"):
                block(t["summon_items"], [esc(t["c_item"]), esc(t["c_quantity"])],
                      [[esc(str(self.loc(r, "item"))), esc(str(r.get("qty", "")))] for r in ent["summon"]])
            if ent.get("drops"):
                block(t["drops"], [esc(t["c_item"]), esc(t["c_quantity"])],
                      [[esc(str(self.loc(r, "item"))), esc(str(r.get("qty", "")))] for r in ent["drops"]])
        elif ent.get("recipe"):
            label = f'{t["recipe"]}{t["sep"]}{self.loc(ent, "name")}'
            block(label, [esc(t["c_material"]), esc(t["c_quantity"])],
                  [[esc(str(self.loc(r, "item"))), esc(str(r.get("qty", "")))] for r in ent["recipe"]])
        return out

    # ------------------------------------------------------------ aggregate tables
    # 列名 → (i18n 表头 key, 取值函数)。列清单与表的适用栏目都在 config/hub.json 里,
    # 本文件不认识任何具体游戏的栏目或实体名。
    COL_HEAD = {
        "order": "c_order", "name": "c_name", "biome": "f_biome", "summon": "f_summon",
        "hp": "f_health", "damage": "f_damage", "weak": "f_weak", "resistant": "f_resistant",
        "very_resistant": "f_very_resistant", "immune": "f_immune", "drops": "f_drops",
        "forsaken": "f_forsaken", "unlocks": "f_unlocks", "ref": "f_boss",
        "key_resources": "f_key_resources", "enemies": "f_enemies", "recipe": "c_material",
        "cargo_slots": "f_cargo", "durability": "f_durability", "station": "f_station",
    }

    def _entity_link(self, eid):
        e = self.ents.get(eid)
        if not e:
            return ""
        nm = esc(str(self.loc(e, "name")))
        s = e.get("page_slug")
        return f'<a href="{self.route_slug(s)}">{nm}</a>' if s and self.is_live(s) else nm

    def _names(self, rows):
        return esc(", ".join(str(x.get(self.nk) or x.get("en") or "") for x in (rows or [])))

    def _qty(self, rows):
        return esc(", ".join(f'{self.loc(r, "item")} \u00d7{r["qty"]}' for r in (rows or [])))

    def _cell(self, e, col):
        if col == "order":
            return esc(str(e.get("order") or ""))
        if col == "name":
            return self._entity_link(next((k for k, v in self.ents.items() if v is e), ""))
        if col == "ref":
            return self._entity_link(e.get("boss") or e.get("ref") or "")
        if col in ("summon", "recipe"):
            return self._qty(e.get(col))
        if col == "drops":
            return esc(self._ent_names(e.get("drops") or []))
        if col in ("key_resources", "enemies", "unlocks"):
            return esc(", ".join(self._list(e.get(col))))
        if col == "hp":
            return esc(str(self._hp(e)))
        if col in ("weak", "resistant", "very_resistant", "immune", "damage"):
            v = e.get("damage_types") if col == "damage" else e.get(col)
            return esc(", ".join(v or []))
        if col == "forsaken":
            fp = e.get("forsaken_power") or {}
            return esc(str(self.loc(fp, "name"))) if fp else ""
        if col in ("biome", "unlocks", "station"):
            key = "crafted_at" if col == "station" else col
            return esc(str(self.loc(e, key)))
        return esc(str(e.get(col) or ""))

    def agg_table(self, spec):
        """按配置出一张聚合排序表。spec = {"type": <实体 type>, "cols": [...], "label": <i18n key>}。"""
        if not spec:
            return "", "", ""
        rows_src = sorted([e for e in self.ents.values() if e.get("type") == spec.get("type")],
                          key=lambda e: (e.get("order") if isinstance(e.get("order"), int) else 99))
        if not rows_src:
            return "", "", ""
        cols = spec.get("cols") or ["name"]
        head = [esc(self.t[self.COL_HEAD.get(c, "c_name")]) for c in cols]
        body = [[self._cell(e, c) for c in cols] for e in rows_src]
        label = self.t.get(spec.get("label") or "", "")
        intro = self.t.get(spec.get("intro") or "", "")
        return self._table(head, body, label, sortable=True), label, intro

    # ------------------------------------------------------------ chrome
    def byline(self, p):
        """H1 下方署名行,与总站页面同一个组件:By <作者> · Last reviewed <日期>。"""
        t = self.t
        line = shell.byline(
            author=self.author_name(p),
            author_href=self.route(self.author_page) if self.author_page else "",
            reviewed=p.get("reviewed") or p.get("updated") or p.get("date"),
            version=p.get("gameVersion"), t=t)
        if p.type == "article" and p.get("scope"):
            line += f'<p class="scope">{esc(t["scope"])}{esc(t.get("colon", ": "))}{esc(p.get("scope"))}</p>'
        return line

    def lang_switch(self, slug):
        alts = [a for a in self.alternates.get(slug, []) if a[0] != self.code]
        if not alts:
            return ""
        links = "".join(f'<a href="{r}" hreflang="{esc(code)}" lang="{esc(code)}">{esc(label)}</a>'
                        for code, r, label in alts)
        return (f'<p class="langsw"><span>{esc(self.t["language"])}{esc(self.t["colon"])}</span>'
                f'<span class="cur">{esc(self.t[self.spec["label_key"]])}</span>{links}</p>')

    def crumbs(self, p, extra_title=None):
        """三级面包屑:<品牌> › <游戏> › <页>(文章页中间还有栏目一级)。"""
        t = self.t
        items = [(self.cfg["brand"], "/"), (self.spec.get("title") or self.g["name"], self.route(self.home))]
        if extra_title is not None:
            items.append((extra_title, None))
        elif p.type == "article":
            # 栏目页没上线就不插这一级:Google 只允许最后一项省略 item,中间级无链接 = 严重问题
            c = self.cat_of(p)
            if c is not None and self.is_live(c.slug):
                items.append((c.get("category"), self.route(c)))
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
        cur_url = self.base + (self.route(p) if extra_title is None else p)
        for k, (name, href) in enumerate(items, start=1):
            e = {"@type": "ListItem", "position": k, "name": name}
            if href:
                e["item"] = self.base + href
            elif k == len(items):
                e["item"] = cur_url
            ld["itemListElement"].append(e)
        return nav, ld

    def cover(self, p):
        """首屏封面(hero):用 600x338 尺寸变体做实际加载图,eager + fetchpriority=high,
        避免 1920x1080 原图在首屏留出一块空黑框。og:image 等仍用原图(im 保留完整字段)。"""
        im = self.image_for(p)
        if not im:
            return "", None
        hero_src = im.get("src_small") or im["src"]
        hero_w = im.get("small_w") or im["w"]
        hero_h = int(round(hero_w * im["h"] / im["w"])) if im.get("w") else im["h"]
        srcset = ""
        if im.get("src_small"):
            srcset = (f' srcset="{esc(im["src_small"])} {im["small_w"]}w, {esc(im["src"])} {im["w"]}w"'
                      f' sizes="(max-width: 860px) 100vw, 760px"')
        credit = self.credit()
        alt = self.alt_of(im)
        fig = (f'<figure class="cover"><img src="{esc(hero_src)}"{srcset} width="{hero_w}" height="{hero_h}"'
               f' alt="{esc(alt)}" loading="eager" fetchpriority="high" decoding="async">'
               + (f"<figcaption>{esc(credit)}</figcaption>" if credit else "") + "</figure>")
        return fig, dict(im, alt=alt)

    def search_form(self):
        """全站搜索(跨全部游戏),当前游戏的结果排前面;无 JS 时退化到本游戏的全量清单页。"""
        if not self.nc.get("search"):
            return ""
        return shell.search_form(action=self.route_slug("all"), index_url="/search-index.json",
                                 lang=self.code, t=self.t, scope=self.short_label(),
                                 placeholder=self.t["search_all_placeholder"])

    def short_label(self):
        return self.spec.get("title") or self.g.get("short") or self.g["name"]

    def header(self):
        # 意图导航文案按本页语种取(self.t),不用 self.site["nav_intents"]——那份是
        # build.py 在总站英文页(/guides /tools ...)里用的全局英文表,只应付总站自己
        # 的页面;游戏内容页有自己的语种,链接不变(配置层),文案必须跟 self.t 走,
        # 与 hub/snapshot.py 的 SnapshotLang.render() 同一条规则(那边一直是对的)。
        intents = [(self.t[k], h) for k, h in self.cfg.get("intent_nav", [])]
        return shell.site_nav(brand=self.cfg["brand"], games=self.site["nav_games"],
                              intents=intents, active_game=self.gslug,
                              search=self.search_form(), t=self.t)

    def nav_sections(self):
        """左侧导航 / 索引用的栏目数据:栏目 = 已发布栏目页,成员 = 该栏目已发布文章。"""
        out = []
        for c in self.nav:
            pages = [{"title": self.pub[s].get("title"), "route": self.route(s), "key": s}
                     for s in self.members[c.slug]]
            out.append({"label": c.get("category"), "route": self.route(c),
                        "pages": pages, "count": len(pages), "key": c.slug})
        return out

    def sidebar(self, cur_slug):
        """左侧常驻游戏内导航 —— 与快照页共用 hub/shell.py:game_nav,本文件不另写一套。"""
        t = self.t
        cur_route = self.route_slug(cur_slug) if cur_slug != self.home.slug else self.route(self.home)
        tools = [(t["all_articles"], self.route_slug("all"), "all")]
        about = []
        if self.author_page:
            about.append((self.author_page.get("title"), self.route(self.author_page), self.author_page.slug))
        about += [(n, h, None) for n, h in t["trust"][:3]]
        im = self.site_game.cover_image()
        return shell.game_nav(
            game_name=self.short_label(), game_href=self.route(self.home),
            subtitle=self.g.get("card", {}).get("genre", ""),
            cover={"src": im.get("src_small") or im.get("src", ""), "alt": self.alt_of(im)} if im else None,
            sections=self.nav_sections(), tools=tools, about=about,
            current=cur_slug if cur_slug in ("all",) else cur_route, t=t)

    # ------------------------------------------------------------ hub 页正文模块的数据源
    def hb_spec(self):
        return self.g.get("hub_body") or {}

    def _hb_pool(self):
        return [im for im in (self.g.get("shots") or []) if im.get("src") and im.get("alt")]

    def _hb_pick_img(self, route, used, page=None):
        im = self.card_image(page) if page is not None else None
        if im and im.get("src") not in used:
            used.add(im["src"])
            return im
        pool = [x for x in self._hb_pool() if x.get("src") not in used]
        if not pool:
            if im:
                used.add(im.get("src"))
            return im
        i = int(hashlib.sha1(route.encode("utf-8")).hexdigest()[:8], 16) % len(pool)
        p = pool[i]
        used.add(p["src"])
        return {"src": p.get("src_small") or p["src"], "w": p.get("small_w") or p.get("w"),
                "h": p.get("h"), "alt": self.alt_of(p)}

    def hb_sections(self):
        used, out = set(), []
        for c in self.nav:
            r = self.route(c)
            out.append((c.get("category"), r, len(self.members[c.slug]),
                        self._hb_pick_img(r, used, c)))
        return out

    def _hb_tool_pages(self):
        keys = [k.lower() for k in self.cfg.get("tools_match", [])]
        return sorted((p for p in self.live_pages()
                       if p.type == "article" and any(k in p.get("title").lower() for k in keys)),
                      key=lambda p: p.get("title"))

    def hb_tools(self):
        used = {im.get("src") for _l, _r, _c, im in self.hb_sections() if im}
        return [(p.get("title"), self.route(p), p.get("description"),
                 self._hb_pick_img(self.route(p), used, p)) for p in self._hb_tool_pages()]

    def hb_featured(self, n=6):
        lands = {self.route(c).rstrip("/") for c in self.nav}
        queues = []
        for c in self.nav:
            ps = [self.pub[s] for s in self.members[c.slug]
                  if self.route(self.pub[s]).rstrip("/") not in lands]
            ps.sort(key=lambda p: (p.get("reviewed") or p.get("updated") or p.get("date"),
                                   p.get("title")), reverse=True)
            if ps:
                queues.append((c.get("category"), ps))
        out, seen, i, guard = [], set(), 0, 0
        used = {im.get("src") for _l, _r, _c, im in self.hb_sections() if im}
        while queues and len(out) < n and guard < 300:
            guard += 1
            label, q = queues[i % len(queues)]
            i += 1
            while q:
                p = q.pop(0)
                r = self.route(p)
                if r in seen:
                    continue
                seen.add(r)
                out.append((label, p.get("title"), r,
                            p.get("reviewed") or p.get("updated") or p.get("date"),
                            self._hb_pick_img(r, used, p)))
                break
            if not any(q for _l, q in queues):
                break
        return out

    def hb_recent(self, n=5):
        return self.recent_rows(n=n)

    def hb_counts(self):
        ds = [p.get("reviewed") or p.get("updated") or p.get("date")
              for p in self.live_pages() if p.type == "article"]
        return {"pages": sum(1 for p in self.live_pages() if p.type != "author"),
                "sections": len(self.nav), "tools": len(self._hb_tool_pages()),
                "langs": len(self.site_game.langs), "entities": len(self.ents),
                "updated": max([d for d in ds if d], default="")}

    def hb_quote(self):
        """范围提示框:逐字取本游戏内容层某一页的第 N 个 H2 与它后面第一段的若干句。
        内容层是 Markdown,所以直接在块上找 —— 一个字都不是框架层写的,语种跟着内容走。"""
        spec = self.hb_spec().get("scope") or {}
        p = self.pages.get(spec.get("slug") or "")
        if p is None or p.draft:
            return None
        blocks = mdlite.parse(p.body)
        idx, want, title, para = 0, int(spec.get("h2") or 0), "", ""
        for k, b in enumerate(blocks):
            if b["t"] == "h" and b["level"] == 2:
                idx += 1
                if idx == want:
                    title = mdlite.plain(b["text"])
                    para = next((mdlite.plain(x["text"]) for x in blocks[k + 1:] if x["t"] == "p"), "")
                    break
        if not (title and para):
            return None
        sents = re.findall(r"[^.\u3002]*[.\u3002]", para) or [para]
        last = int(spec.get("last") or 0)
        if last:
            quote = "".join(sents[-last:]).strip()
        else:
            skip, take = int(spec.get("skip") or 0), int(spec.get("take") or 1)
            quote = "".join(sents[skip:skip + take]).strip()
        if not quote:
            return None
        route = self.route(p)
        cur = self.route(self.home) if getattr(self, "home", None) is not None else ""
        return title, quote, ("" if route == cur else route), p.get("title")

    def hb_self_hosts(self):
        return {_host(self.base)} - {""}

    def hb_gslug(self):
        return self.gslug

    def recent_rows(self, *, exclude="", n=6):
        """本游戏最近更新的文章 → [(标题, 链接, 日期)]。日期真的来自 frontmatter,没有就不进。"""
        rows = []
        for s, p in self.pub.items():
            if s == exclude or p.type != "article":
                continue
            d = p.get("reviewed") or p.get("updated") or p.get("date")
            if d:
                rows.append((d, p.get("title"), self.route(p)))
        rows.sort(reverse=True)
        return [(title, route, d) for d, title, route in rows[:n]]

    def footer(self):
        t = self.t
        links = list(t["trust"])
        if self.author_page:
            links.append((t["author"], self.route(self.author_page)))
        links.append((t["all_articles"], self.route_slug("all")))
        return shell.footer(brand=self.cfg["brand"], year=self.site["year"],
                            links=links, note=t["footer_note"],
                            extra=shell.request_link(game=self.g["name"], t=t, **self.req_ctx()))

    def req_ctx(self):
        """提需求件的站级参数(邮箱 / Web3Forms key / 品牌),来自 build.py 算好的 site["request"]。"""
        r = self.site["request"]
        return {"email": r["email"], "brand": r["brand"]}

    # ------------------------------------------------------------ shell
    def shell(self, *, lang_code, head, crumbs_html, h1, byline, langsw, aside, body,
              cur_slug, scripts="", rail_last=False):
        t = self.t
        toggle = (
            '<input type="checkbox" id="navtoggle" class="navtoggle">'
            f'<label class="navtoggle-l" for="navtoggle"><span aria-hidden="true">&#9776;</span> '
            f'{esc(t["open_menu"])}</label>')
        # 有右栏的页在右栏末尾挂「提需求」卡片;没有右栏内容的页保持 no-rail,
        # 入口只走页脚链接 + 浮动按钮(hub.css: main.no-rail~.req-fab 桌面端也显示),不为一张卡片硬加右栏。
        if aside:
            aside += shell.request_card(game=self.g["name"], t=t, **self.req_ctx())
        aside_html = f'<aside class="rail">{aside}</aside>' if aside else ""
        # rail_last:右栏只是「最近更新」这类小组件时,窄屏把它排到正文之后
        #(速查信息框那种才值得挤在 h1 下面)
        cls = "layout" + ("" if aside else " no-rail") + (" rail-last" if rail_last and aside else "")
        # 面包屑单独占一行网格(grid-area:crumb),右栏信息框顶边才能和 h1 顶边对齐
        main = (
            f'<main class="{cls}" id="main">\n{toggle}\n{self.sidebar(cur_slug)}\n{crumbs_html}\n'
            f'<div class="doc-hd"><h1>{h1}</h1>{byline}{langsw}</div>\n'
            f'{aside_html}\n<div class="doc">{body}</div>\n</main>')
        # 站级 token 已经写进 out/hub.css 的 :root;这里只在该游戏声明了自己的 theme 时
        # 注入差异项(换游戏想换配色只动配置层,框架层一行 hex 都没有)。
        site_theme = self.cfg.get("theme", {})
        over = {k: v for k, v in (self.nc.get("theme") or {}).items() if site_theme.get(k) != v}
        theme_css = "<style>:root{" + ";".join(f"--{k}:{v}" for k, v in over.items()) + "}</style>" if over else ""
        tpl = (self.root / "hub" / "native_page.html").read_text(encoding="utf-8")
        return (tpl.replace("{{LANG}}", esc(lang_code))
                .replace("{{HEAD}}", "\n".join(head))
                .replace("{{FONTS}}", self.site.get("font_links", ""))
                .replace("{{THEME}}", theme_css)
                .replace("{{HEAD_EXTRA}}", self.site["head_extra"])
                .replace("{{HEADER}}", self.header())
                .replace("{{MAIN}}", main)
                .replace("{{SCRIPTS}}", shell.request_block(
                    games=self.site["request"]["games"], current=self.g["slug"], lang=lang_code,
                    key=self.site["request"]["key"], t=t, **self.req_ctx()) + scripts)
                .replace("{{FOOTER}}", self.footer()))

    def head_common(self, *, title, desc, page_url, og_type, im, slug, graphs, extra=()):
        t = self.t
        head = [
            f"<title>{esc(title)}</title>",
            f'<meta name="description" content="{esc(desc)}">',
            f'<link rel="canonical" href="{esc(page_url)}">',
        ]
        for code, route, _label in self.alternates.get(slug, []):
            head.append(f'<link rel="alternate" hreflang="{esc(code)}" href="{esc(self.base + route)}">')
        xd = next((r for c, r, _ in self.alternates.get(slug, []) if c == self.site_game.default_code), None)
        if xd:
            head.append(f'<link rel="alternate" hreflang="x-default" href="{esc(self.base + xd)}">')
        head += [
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
        head += list(extra)
        head.append('<meta name="twitter:card" content="summary_large_image">')
        head += [ld_script(x) for x in graphs]
        return head

    # ------------------------------------------------------------ page build
    def build_page(self, p):
        t = self.t
        blocks = mdlite.parse(p.body)
        h1_text = None
        kept = []
        for b in blocks:
            if b["t"] == "h" and b["level"] == 1:
                if h1_text is None:
                    h1_text = b["text"]
                    continue
                self.warnings.append(f"{self.nk}/{p.path.name}: 多余的 H1 已降为 H2")
                b = dict(b, level=2)
            kept.append(b)
        blocks = kept
        h1_text = h1_text or p.get("title")

        # 正文末尾的「接下来读什么」小节 → 由 frontmatter.related 统一渲染
        for rh in self.spec.get("related_headings", []):
            hit = False
            for k, b in enumerate(blocks):
                if b["t"] == "h" and b["level"] == 2 and mdlite.plain(b["text"]) == rh:
                    tail = blocks[k + 1:]
                    if any(x["t"] == "h" and x["level"] <= 2 for x in tail):
                        break
                    blocks = blocks[:k]
                    hit = True
                    break
            if hit:
                break

        # 卡片块 / 栏目链接列表:hub 与栏目页由数据重渲染,正文里不重复
        out, card_done = [], False
        i = 0
        while i < len(blocks):
            b = blocks[i]
            tgt = self._card_target(b["text"]) if b["t"] == "h" and b["level"] >= 3 else None
            if tgt and tgt in self.pages and self.pages[tgt].type == "article":
                i += 1
                if i < len(blocks) and blocks[i]["t"] == "p":
                    i += 1
                if p.type == "category" and not card_done:
                    card_done = True
                    slugs = self.members.get(p.slug) or []
                    if slugs:
                        out.append({"t": "html", "html": self.article_cards(slugs, b["level"])})
                continue
            if b["t"] in ("ul", "ol") and b["items"]:
                sl = [mdlite.sole_link(x) for x in b["items"]]
                if all(sl) and all(self.pages.get(self._internal_slug(h) or "", None) is not None
                                   and self.pages[self._internal_slug(h)].type == "category" for _, h in sl):
                    i += 1
                    # 这张列表是该小节的全部内容(紧跟标题,后面直接是下一个同级/更高级标题或文末)
                    # 时,标题一起丢——不然折叠段里留下一个空的 <h2>(2026-09-24 /valheim/ 的「All sections」)
                    if out and out[-1]["t"] == "h" and (
                            i >= len(blocks) or (blocks[i]["t"] == "h" and blocks[i]["level"] <= out[-1]["level"])):
                        out.pop()
                    continue  # hub 的栏目 tile 由数据渲染
            out.append(b)
            i += 1
        blocks = out

        used, toc = set(), []
        for b in blocks:
            if b["t"] == "h" and b["level"] in (2, 3):
                b["id"] = mdlite.slugify(b["text"], used)
                if b["level"] == 2:
                    toc.append((b["id"], mdlite.plain(b["text"])))
        h2_count = len(toc)

        lede = ""
        if p.type == "home":
            for k, b in enumerate(blocks):
                if b["t"] == "p":
                    lede = b["text"]
                    blocks = blocks[:k] + blocks[k + 1:]
                    break

        ext_labels = {}
        body_html = mdlite.render(blocks, self.link_cb_factory(p, ext_labels), t.get("table_label", "table"),
                                  self.img_cb_factory(p), self.figure_cb_factory(p))

        ents = self.entities_of(p)
        aside = "".join(self.quick_facts(e, first=(i == 0)) for i, e in enumerate(ents))
        # 右栏「最近更新」小组件:日期取 frontmatter 的 reviewed/updated/date,没有日期的页不列。
        if p.type in ("home", "category"):
            aside += shell.rail_list(t["recent_in_game"], self.recent_rows(exclude=p.slug))

        pre, extra, scripts = [], [], ""
        # 要点框
        tldr = p.fm.get("tldr") or []
        if tldr:
            pre.append(f'<section class="kp"><p class="kp-t">{esc(t["key_points"])}</p><ul>'
                       + "".join(f"<li>{mdlite.inline(x, self.link_cb_factory(p, ext_labels))}</li>"
                                 for x in tldr) + "</ul></section>")

        cat_agg_html = ""
        if p.type == "home":
            # hero:封面下的一句话 = 首页稿第一段;其余稿件收进「关于本攻略」折叠段
            toc = []   # hub 页目录只列生成出来的区块,正文小标题在折叠段里,不进目录
            hid = mdlite.slugify(t["hero_tiles"], used)
            pre.append(f'<h2 id="{hid}">{esc(t["hero_tiles"])}</h2>')
            pre.append(self.category_tiles())
            toc.insert(0, (hid, t["hero_tiles"]))
            # 关于本攻略(折叠)紧跟 tile 网格
            abid = mdlite.slugify(t["about_this_guide"], used)
            pre.append(f'<details class="about" id="{abid}"><summary>{esc(t["about_this_guide"])}</summary>'
                       f'<div class="about-b">{body_html}</div></details>')
            toc.append((abid, t["about_this_guide"]))
            body_html = ""
            bt, blabel, bintro = self.agg_table(self.nc.get("hub_table"))
            if bt:
                bhid = mdlite.slugify(blabel, used)
                pre.append(f'<h2 id="{bhid}">{esc(blabel)}</h2><p>{esc(bintro)}</p>{bt}')
                toc.append((bhid, blabel))
                scripts += SORT_JS
            # 实体数据驱动的速查表(config/hub.json → hub_body.tables;见 hub/hubbody.py)
            th, ttoc = self.hb_tables(used)
            if th:
                pre.append(th)
                toc += ttoc
            sh = [s for s in (self.nc.get("start_here") or []) if self.is_live(s)]
            if sh:
                shid = mdlite.slugify(t["start_here"], used)
                pre.append(f'<h2 id="{shid}">{esc(t["start_here"])}</h2>' + self.article_cards(sh[:3]))
                toc.append((shid, t["start_here"]))
            oh, otoc = self.hb_tool_tiles(used)
            if oh:
                pre.append(oh)
                toc += otoc
            pre.append(self.hb_timeline(used))
            (ahid, lbl), sec = self.all_articles_section(used)
            extra.append(sec)
            toc.append((ahid, lbl))
            # hub 页底部 FAQ:问答全部来自内容层 frontmatter 的 faq(答案里的站内链接
            # 走同一条链接校验路径,指向不存在的页会直接构建报错)。没有 faq 就不出这个区块。
            rows = [(q, mdlite.inline(a, self.link_cb_factory(p, ext_labels)))
                    for q, a in (p.fm.get("faq") or [])]
            if rows:
                fhid = mdlite.slugify(t["faq_heading"], used)
                fq_html, fq_ld = shell.faq(rows, t["faq_heading"], fhid)
                extra.append(fq_html)
                toc.append((fhid, t["faq_heading"]))
                self._faq_ld = fq_ld
        elif p.type == "category":
            tbl, label, intro = self.agg_table((self.nc.get("category_tables") or {}).get(p.slug))
            if tbl:
                hid = mdlite.slugify(label, used)
                cat_agg_html = (f'<section class="agg"><h2 id="{hid}">{esc(label)}</h2>'
                                f'<p>{esc(intro)}</p>{tbl}</section>')
                toc.append((hid, label))
                scripts += SORT_JS
        elif p.type == "author":
            hid = mdlite.slugify(t["author_articles"], used)
            name = self.author_name(p)
            mine = [s for c in self.nav for s in self.members[c.slug]
                    if self.pub[s].get("category") == c.get("category") and self.author_name(self.pub[s]) == name]
            extra.append(f'<h2 id="{hid}">{esc(t["author_articles"].format(name=name))}</h2>'
                         + self.article_cards(mine))
            toc.append((hid, t["author_articles"].format(name=name)))

        # 实体表(召唤材料 / 掉落 / 配方)
        for e in ents:
            for hid, lbl, html in self.entity_tables(e, used):
                extra.append(html)
                toc.append((hid, lbl))

        # 来源
        srcs = p.fm.get("sourceUrls") or []
        ent_srcs = []
        for e in ents:
            for u in e.get("source_urls") or []:
                if u not in srcs and u not in ent_srcs:
                    ent_srcs.append(u)
        all_srcs = list(srcs) + ent_srcs
        if all_srcs:
            hid = mdlite.slugify(t["sources"], used)
            acc = p.get("checkedAt")
            lis = []
            for k, u in enumerate(all_srcs, start=1):
                label = ext_labels.get(u) or _host(u)
                a = acc if u in srcs else (ents[0].get("accessed") if ents else acc)
                lis.append(
                    f'<li id="s{k:03d}"><span class="sid">S{k:03d}</span> '
                    f'<a href="{esc(u)}"{self.ext_attrs(u)}>{esc(label)}</a>'
                    f' <span class="shost">{esc(_host(u))}</span>'
                    + (f' <span class="sdate">{esc(t["accessed"])} <time datetime="{esc(a)}">{esc(a)}</time></span>'
                       if a else "") + "</li>")
            for u in ext_labels:
                if u not in all_srcs:
                    self.warnings.append(f"{self.nk}/{p.path.name}: 正文外链 {u} 不在 sourceUrls 里")
            extra.append(f'<section class="sources"><h2 id="{hid}">{esc(t["sources"])}</h2>'
                         f'<p>{esc(t["sources_intro"])}</p><ol>{"".join(lis)}</ol></section>')
            toc.append((hid, t["sources"]))

        rel = [s for s in (p.fm.get("related") or []) if self.is_live(s) and self.pub[s].type == "article"]
        if rel or p.type == "article":
            pn = self.prevnext(p)
            if rel or pn:
                hid = mdlite.slugify(t["related"], used)
                extra.append(f'<section class="related"><h2 id="{hid}">{esc(t["related"])}</h2>'
                             + (self.article_cards(rel) if rel else "") + pn + "</section>")
                toc.append((hid, t["related"]))

        toc_html = ""
        if h2_count >= 5 or (p.type == "home" and len(toc) >= 5):
            toc_html = (f'<nav class="toc" aria-label="{esc(t["toc"])}"><p class="toc-t">{esc(t["toc"])}</p><ol>'
                        + "".join(f'<li><a href="#{esc(i)}">{esc(l)}</a></li>' for i, l in toc) + "</ol></nav>")

        crumbs_html, crumbs_ld = self.crumbs(p)
        fig, im = self.cover(p)
        if p.type == "category":
            fig = ""  # 栏目页去掉 hero 大图,排序表/卡片网格直接接在要点框之后
        h1_html = mdlite.inline(mdlite.plain(h1_text))

        # 版面顺序:要点框 → (栏目页:排序表) → 封面 → 目录 → (数据区块) → 正文 → 表/来源/关联
        kp_html = pre.pop(0) if tldr else ""
        # hub 页:范围提示框 + 统计胶囊(都在 .prose 之外,与快照套壳页同一位置与同一套 CSS)
        hb_head = (self.hb_note() + self.hb_pills()) if p.type == "home" else ""
        lede_html = (f'<p class="lede">{mdlite.inline(lede, self.link_cb_factory(p, ext_labels))}</p>'
                     if lede else "")
        body = (kp_html + hb_head + cat_agg_html + fig + lede_html + toc_html + '<div class="prose">'
                + "\n".join(pre) + "\n" + body_html + "\n" + "".join(extra) + "</div>")

        # JSON-LD
        graphs = []
        page_url = self.url(p)
        publisher = {"@type": "Organization", "name": self.cfg["brand"], "url": self.base + "/",
                     "logo": {"@type": "ImageObject", "url": self.base + "/favicon.svg"}}
        person = {"@type": "Person", "name": self.author_name(p)}
        if self.author_url():
            person["url"] = self.author_url()
        head_extra = []
        if p.type == "article":
            art = {"@context": "https://schema.org", "@type": "Article",
                   "headline": mdlite.plain(h1_text), "description": p.get("description"),
                   "inLanguage": self.code, "mainEntityOfPage": page_url, "url": page_url,
                   "datePublished": p.get("date"), "dateModified": self.modified(p),
                   "author": person, "publisher": publisher,
                   "about": {"@type": "VideoGame", "name": self.g["name"]}}
            if im:
                art["image"] = {"@type": "ImageObject", "url": im["src"], "width": im["w"], "height": im["h"]}
            c = self.cat_of(p)
            if c is not None:
                art["articleSection"] = c.get("category")
            graphs.append(art)
            head_extra = [f'<meta property="article:published_time" content="{esc(p.get("date"))}">',
                          f'<meta property="article:modified_time" content="{esc(self.modified(p))}">']
        elif p.type == "author":
            graphs.append({"@context": "https://schema.org", "@type": "ProfilePage", "url": page_url,
                           "name": p.get("title"), "inLanguage": self.code,
                           "mainEntity": dict(person, jobTitle=t.get("author_role", ""))})
        else:
            cp = {"@context": "https://schema.org", "@type": "CollectionPage", "url": page_url,
                  "name": p.get("title"), "description": p.get("description"),
                  "inLanguage": self.code,
                  "isPartOf": {"@type": "WebSite", "name": self.cfg["brand"], "url": self.base + "/"},
                  "about": {"@type": "VideoGame", "name": self.g["name"]}}
            if p.type == "home":
                cp["dateModified"] = self.modified(p)
            graphs.append(cp)
        graphs.append(crumbs_ld)
        if getattr(self, "_faq_ld", None):
            graphs.append(self._faq_ld)
            self._faq_ld = None

        head = self.head_common(
            title=p.get("seoTitle") or mdlite.plain(h1_text), desc=p.get("description"),
            page_url=page_url, og_type="article" if p.type == "article" else "website",
            im=im, slug=p.slug, graphs=graphs, extra=head_extra)
        scripts += SEARCH_JS if self.nc.get("search") else NAV_JS
        return self.shell(lang_code=self.code, head=head, crumbs_html=crumbs_html, h1=h1_html,
                          byline=self.byline(p), langsw=self.lang_switch(p.slug), aside=aside,
                          body=body, cur_slug=p.slug, scripts=scripts, rail_last=not ents)

    def all_articles_section(self, used_ids, level=3):
        hid = mdlite.slugify(self.t["all_articles"], used_ids)
        parts = [f'<h2 id="{hid}">{esc(self.t["all_articles"])}</h2>',
                 f'<p>{esc(self.t["all_articles_intro"])}</p>']
        for c in self.nav:
            prim = [s for s in self.members[c.slug] if self.pub[s].get("category") == c.get("category")]
            if not prim:
                continue
            parts.append(f'<h{level} id="{mdlite.slugify(c.get("category"), used_ids)}">'
                         f'<a href="{self.route(c)}">{esc(c.get("category"))}</a></h{level}>')
            parts.append("<ul class=\"linklist\">" + "".join(
                f'<li><a href="{self.route(s)}">{esc(self.pub[s].get("title"))}</a></li>' for s in prim) + "</ul>")
        return (hid, self.t["all_articles"]), "\n".join(parts)

    def build_all_page(self):
        """无 JS 时的搜索退化页:纯链接列表。"""
        t = self.t
        gname = self.spec.get("title") or self.g["name"]
        route = self.route_slug("all")
        page_url = self.base + route
        title = t["all_page_seo"].format(game=gname)
        desc = t["all_page_desc"].format(game=gname)
        used = set()
        (_hid, _lbl), sec = self.all_articles_section(used, level=2)
        body = (f'<div class="prose"><p>{esc(t["all_page_intro"])}</p>'
                + sec.split("\n", 2)[2] + "</div>")
        crumbs_html, crumbs_ld = self.crumbs(route, extra_title=t["all_page_title"])
        graphs = [{"@context": "https://schema.org", "@type": "CollectionPage", "url": page_url,
                   "name": title, "description": desc, "inLanguage": self.code,
                   "isPartOf": {"@type": "WebSite", "name": self.cfg["brand"], "url": self.base + "/"}},
                  crumbs_ld]
        head = self.head_common(title=title, desc=desc, page_url=page_url, og_type="website",
                                im=None, slug="all", graphs=graphs)
        return self.shell(lang_code=self.code, head=head, crumbs_html=crumbs_html,
                          h1=esc(t["all_page_title"]), byline="", langsw=self.lang_switch("all"),
                          aside="", body=body, cur_slug="all",
                          scripts=SEARCH_JS if self.nc.get("search") else NAV_JS)

    def modified(self, p):
        return max(x for x in (p.get("date"), p.get("updated"), p.get("reviewed")) if x) if (
            p.get("date") or p.get("updated") or p.get("reviewed")) else ""

    def lastmod(self, p):
        return p.get("reviewed") or p.get("updated") or p.get("date") or self.site["today"]

    def live_pages(self):
        for p in self.pub.values():
            if p.type == "category" and p.slug not in self.live_cats:
                continue
            yield p

    def search_rows(self):
        rows = []
        for p in self.live_pages():
            c = self.cat_of(p)
            rows.append({"url": self.route(p), "title": p.get("title"), "lang": self.code,
                         "description": p.get("description"),
                         "category": (p.get("category") if p.type in ("category", "home", "author")
                                      else (c.get("category") if c is not None else ""))})
        return rows

    def build(self, dst: Path):
        routes = {}
        for p in self.live_pages():
            html = self.build_page(p)
            sub = "" if p.type == "home" else p.slug
            target = dst / self.prefix / sub / "index.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(html, encoding="utf-8")
            routes[self.route(p)] = self.lastmod(p)
        ap = dst / self.prefix / "all" / "index.html"
        ap.parent.mkdir(parents=True, exist_ok=True)
        ap.write_text(self.build_all_page(), encoding="utf-8")
        routes[self.route_slug("all")] = self.site["today"]
        return routes


# ===========================================================================
#  站点级(一个游戏 = N 个语种)
# ===========================================================================
class NativeGame:
    def __init__(self, root: Path, game: dict, cfg: dict, site: dict):
        self.root, self.g, self.cfg, self.site = root, game, cfg, site
        self.nc = game.get("native", {})
        self.gslug = game["slug"]
        self.base = site["base"]
        self.warnings = []
        self.content_root = root / game["content"]
        img_file = self.content_root / "_images.json"
        self.images = json.loads(img_file.read_text(encoding="utf-8")) if img_file.is_file() else {}
        self.official = [d.lower() for d in self.nc.get("official_domains", [])]
        ef = self.nc.get("entities")
        self.ents = {}
        if ef and (root / ef).is_file():
            self.ents = json.loads((root / ef).read_text(encoding="utf-8")).get("entities", {})
        specs = self.nc.get("langs") or [{
            "code": game.get("lang", "en"), "i18n": game.get("lang", "en"), "dir": "",
            "prefix": "", "title": self.nc.get("title") or game["name"],
            "label_key": "home", "default": True,
            "related_headings": [self.nc["related_heading"]] if self.nc.get("related_heading") else [],
        }]
        # 实体字段上出现的语种后缀(name_en / hazards_zh …),用来还原字段基名
        self.lang_keys = {s.get("dir") for s in specs if s.get("dir")} | {"en"}
        self.langs = [NativeLang(self, s) for s in specs]
        self.default_lang = next((l for l in self.langs if l.default), self.langs[0])
        self.default_code = self.default_lang.code
        self._wire_alternates()

    def _wire_alternates(self):
        slugs = set()
        for l in self.langs:
            slugs |= {p.slug for p in l.live_pages()}
        slugs.add("all")
        for slug in slugs:
            alts = []
            for l in self.langs:
                if slug == "all" or (slug in l.pub and l.is_live(slug)):
                    r = l.route_slug("all") if slug == "all" else l.route(slug)
                    alts.append((l.code, r, l.t[l.spec["label_key"]]))
            if len(alts) < 2:
                alts = alts if len(alts) == 1 else []
            for l in self.langs:
                l.alternates[slug] = alts if len(alts) > 1 else []
            # 单语种页仍需 canonical 自指(已有),不输出 hreflang

    def cover_image(self):
        """游戏封面(左侧导航头 / 首页卡片用):取内容层 _images.json 的默认截图。"""
        key = self.images.get("default")
        return (self.images.get("shots", {}) or {}).get(key) if key else None

    def index(self) -> GameIndex:
        """回填给全站索引:栏目/页/日期取默认语种,搜索索引包含全部语种。"""
        l = self.default_lang
        sections = []
        for c in l.nav:
            pages = [PageRef(l.route(s), l.pub[s].get("title"), l.pub[s].get("description"),
                             c.get("category"), l.pub[s].get("date"), l.lastmod(l.pub[s]),
                             self.gslug, l.code, image=l.card_image(l.pub[s]))
                     for s in l.members[c.slug]]
            sections.append(Section(c.slug, c.get("category"), l.route(c), pages))
        # 一篇文章可以跨栏目列出(见 members 的规则),索引里按 route 去重,页数才是真页数
        pages, seen = [], set()
        for s in sections:
            for p in s.pages:
                if p.route not in seen:
                    seen.add(p.route)
                    pages.append(p)
        for lg in self.langs:
            for p in lg.live_pages():
                if lg.route(p) in seen or p.type == "home":
                    continue
                seen.add(lg.route(p))
                cat = lg.cat_of(p)
                pages.append(PageRef(lg.route(p), p.get("title"), p.get("description"),
                                     p.get("category") if p.type == "category"
                                     else (cat.get("category") if cat is not None else ""),
                                     p.get("date"), lg.lastmod(p), self.gslug, lg.code,
                                     image=lg.card_image(p)))
        c = self.g.get("card", {})
        cover = {"src": c.get("img", ""), "w": c.get("img_w"), "h": c.get("img_h"),
                 "alt": c.get("img_alt", "")}
        return GameIndex(self.g, home_route=l.route(l.home), sections=sections,
                         pages=pages, cover=cover, default_lang=l.code)

    def build(self, out_root: Path):
        dst = out_root / self.gslug
        routes = {}
        for l in self.langs:
            routes.update(l.build(dst))
        for w in dict.fromkeys(self.warnings):
            print(f"  [{self.gslug}] 警告: {w}")
        drafts = sorted(f'{l.nk}/{s}' for l in self.langs for s, p in l.pages.items() if p.draft)
        print(f"  [{self.gslug}] native: {len(self.langs)} 语种,生成 {len(routes)} 页,"
              f"草稿跳过 {len(drafts)}" + (f"({', '.join(drafts)})" if drafts else ""))
        return routes
