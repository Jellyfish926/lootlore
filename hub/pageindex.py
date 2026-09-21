"""pageindex —— 站点索引:自动发现每个游戏有哪些页、分成哪些栏目、各页最后更新日。框架层。

真相源只有两个,都在仓里:
  * 快照游戏  sources/<game>/**.html —— 子站构建产物。栏目分组取页面自带的 BreadcrumbList
    JSON-LD(子站自己维护的),扁平结构的站退回用该游戏 hub 页的 <h2> 分组;
    日期取 JSON-LD 的 dateModified / datePublished。
  * 原生游戏  hub/native.py 渲染时把栏目/成员/日期回填进来(见 NativeGame.index_sections)。

本文件不含任何游戏专属文字:栏目名来自页面自己的面包屑或标题,兜底标签走 config/i18n。
手工维护链接清单必然漂移,所以这里一条都不写。
"""
import html as _html
import json
import re
from pathlib import Path

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
DESC_RE = re.compile(r'<meta\s+name="description"\s+content="([^"]*)"', re.I)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)
LD_RE = re.compile(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', re.S | re.I)
NOINDEX_RE = re.compile(r'<meta\s+name="robots"[^>]+noindex', re.I)
TAG_RE = re.compile(r"<[^>]+>")
H2_RE = re.compile(r"<h2[^>]*>(.*?)</h2>", re.S | re.I)
A_RE = re.compile(r'<a\s[^>]*href="([^"#?]+)[^"]*"[^>]*>(.*?)</a>', re.S | re.I)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")
# 法务/信任页:总站自己有一套,子站快照里的同名页不进攻略索引(与 .gates/check_content 的 TRUST 同口径)
TRUST_SLUGS = {"about", "contact", "privacy", "privacy-policy", "terms", "terms-of-service",
               "disclaimer", "editorial-policy", "404", "500", "search"}


def _text(s: str) -> str:
    return _html.unescape(TAG_RE.sub("", s or "")).strip()


def _day(v) -> str:
    """把 ISO 时间戳截成日期;不是日期就返回空串(绝不猜)。"""
    if not isinstance(v, str):
        return ""
    m = DATE_RE.match(v.strip())
    return m.group(0) if m else ""


class PageRef:
    """一个可索引页。title/description/日期全部来自文件本身,没有就是空,不填默认值。"""

    __slots__ = ("route", "title", "description", "section", "published", "modified", "game", "lang")

    def __init__(self, route, title, description="", section="", published="", modified="",
                 game="", lang="en"):
        self.route = route
        self.title = title
        self.description = description
        self.section = section
        self.published = published
        self.modified = modified
        self.game = game
        self.lang = lang

    @property
    def date(self):
        return self.modified or self.published


class Section:
    __slots__ = ("key", "label", "route", "pages")

    def __init__(self, key, label, route="", pages=None):
        self.key = key
        self.label = label
        self.route = route
        self.pages = pages or []

    @property
    def count(self):
        return len(self.pages)


class GameIndex:
    """一个游戏的索引。sections 只包含真实存在且非空的栏目(空栏目不进导航)。"""

    def __init__(self, game: dict, *, home_route: str, sections=None, pages=None, cover=None,
                 default_lang="en"):
        self.slug = game["slug"]
        self.default_lang = default_lang
        self.name = game["name"]
        self.short = game.get("short") or game["name"]
        self.card = game.get("card", {})
        self.kind = game.get("kind", "snapshot")
        self.home_route = home_route
        self.sections = sections or []
        self.pages = pages or []
        self.cover = cover or {}

    @property
    def page_count(self):
        """卡片与索引上显示的页数 = 默认语种的页数(镜像语种另算,不重复计入)。"""
        return sum(1 for p in self.pages if p.lang == self.default_lang)

    @property
    def updated(self):
        ds = [p.date for p in self.pages if p.date and p.lang == self.default_lang]
        return max(ds) if ds else ""

    def recent(self, n=5):
        dated = [p for p in self.pages if p.date]
        return sorted(dated, key=lambda p: (p.date, p.title), reverse=True)[:n]


# ---------------------------------------------------------------- 快照发现
def _excluded(rel: Path, game: dict) -> bool:
    ex_files = set(game.get("exclude_files", []))
    ex_dirs = set(game.get("exclude_dirs", []))
    ex_prefixes = tuple(game.get("exclude_prefixes", []))
    parts = rel.parts
    if parts and parts[0] in ex_dirs:
        return True
    if len(parts) == 1 and rel.name in ex_files:
        return True
    if ex_prefixes and str(rel).startswith(ex_prefixes):
        return True
    return rel.name == "404.html" or "404" in parts


def _route_of(slug: str, rel: Path) -> str:
    """产物路由(cleanUrls):x/index.html → /slug/x/ ;x.html → /slug/x 。"""
    s = str(rel).replace("\\", "/")
    if s.endswith("/index.html"):
        return f"/{slug}/{s[:-len('index.html')]}"
    if s == "index.html":
        return f"/{slug}/"
    return f"/{slug}/{s[:-5]}"


def _crumb_section(ld_items, origin: str, slug: str):
    """从 BreadcrumbList 取上一级栏目 → (label, route);层级不足 3 返回 None。"""
    for obj in ld_items:
        if obj.get("@type") != "BreadcrumbList":
            continue
        els = obj.get("itemListElement") or []
        if len(els) < 3:
            return None
        parent = els[-2]
        label = _text(str(parent.get("name") or ""))
        item = str(parent.get("item") or "")
        if not label:
            return None
        route = ""
        if item.startswith(origin):
            tail = item[len(origin):]
            route = f"/{slug}{tail}" if tail.startswith("/") else f"/{slug}/{tail}"
        return label, route
    return None


SUFFIX_RE = re.compile(r"\s*[|·]\s*[^|·]{0,40}$")


def _index_title(h1: str, title: str) -> str:
    """索引里显示的标题:正常取 <h1>;<h1> 短到没信息量而 <title> 是它的扩写时改取 <title>
    (并去掉「| 站名」后缀)。真实踩到的两种:某快照页 <h1> 是「The No」(子站自己的截断),
    作者页 <h1> 是裸「Jellyfi」。不猜、不拼接,只在两者确实同源时换一个更完整的那个。"""
    t = (SUFFIX_RE.sub("", title).strip() or title).strip()
    if not h1:
        return t
    low_h1, low_t = h1.lower(), t.lower()
    if low_t.startswith(low_h1) and len(t) > len(h1) and (len(h1) < 14 or len(t) > len(h1) + 6):
        return t
    return h1


def _scan_html(path: Path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    if NOINDEX_RE.search(raw):
        return None
    ld_items = []
    for m in LD_RE.finditer(raw):
        try:
            d = json.loads(m.group(1))
        except Exception:
            continue
        ld_items += d if isinstance(d, list) else [d]
    pub = mod = ""
    for obj in ld_items:
        if obj.get("@type") in ("Article", "BlogPosting", "WebPage", "CollectionPage"):
            pub = pub or _day(obj.get("datePublished"))
            mod = mod or _day(obj.get("dateModified"))
    t = _text(TITLE_RE.search(raw).group(1)) if TITLE_RE.search(raw) else ""
    h1 = _text(H1_RE.search(raw).group(1)) if H1_RE.search(raw) else ""
    desc = DESC_RE.search(raw)
    return {
        "title": _index_title(h1, t),
        "seo_title": t,
        "description": _html.unescape(desc.group(1)) if desc else "",
        "published": pub,
        "modified": mod,
        "ld": ld_items,
        "raw": raw,
    }


def _card_groups(raw: str, keep: set, slug: str):
    """扁平结构的站(所有页都在语种根下,没有目录层):用该游戏 hub 页自己的卡片网格分组。

    只认「卡片链接」—— <a href=…> 内部含 <h3> 的那种,这是策展卡片网格的结构特征;
    页内目录、页脚导航那种裸 <a> 列表一律不算,否则会把「Sources」这类正文小标题
    误当成栏目。返回 [(h2 标签, [route,…])],只保留 ≥3 张卡的组。"""
    marks = [(m.start(), "h2", _text(m.group(1))) for m in H2_RE.finditer(raw)]
    for m in A_RE.finditer(raw):
        if "<h3" in m.group(2).lower():
            marks.append((m.start(), "a", m.group(1)))
    marks.sort(key=lambda x: x[0])
    groups, cur, seen = [], None, set()
    for _pos, kind, val in marks:
        if kind == "h2":
            cur = (val, [])
            groups.append(cur)
            continue
        if cur is None or not val.startswith("/"):
            continue
        tail = val.rstrip("/")
        route = next((c for c in (f"/{slug}{val}", f"/{slug}{tail}", f"/{slug}{tail}/") if c in keep), "")
        if route and route not in seen:
            seen.add(route)
            cur[1].append(route)
    return [(lbl, rs) for lbl, rs in groups if len(rs) >= 3 and lbl]


def snapshot_index(root: Path, game: dict, fallback_label: str) -> GameIndex:
    src = root / game["source"]
    slug = game["slug"]
    origin = game.get("origin", "").rstrip("/")
    default_path = game.get("default_path", "/")
    lang_root = default_path.strip("/")
    home_route = f"/{slug}{default_path.rstrip('/') or '/'}"
    if not home_route.endswith("/"):
        home_route += "/"

    found, dirs = {}, {}
    for p in sorted(src.rglob("*.html")):
        rel = p.relative_to(src)
        if _excluded(rel, game):
            continue
        if lang_root and rel.parts[0] != lang_root:
            continue
        info = _scan_html(p)
        if info is None or not info["title"]:
            continue
        route = _route_of(slug, rel)
        if route.rstrip("/").rsplit("/", 1)[-1] in TRUST_SLUGS:
            continue
        found[route] = info
        # 语种根之后的第一段目录名 = 栏目 key(深度 1 的页没有目录,key 为空)
        parts = rel.parts[1:] if lang_root else rel.parts
        info["dirkey"] = parts[0] if len(parts) > 1 else ""
        if info["dirkey"]:
            dirs.setdefault(info["dirkey"], []).append(route)

    home_info = found.get(home_route) or found.get(home_route.rstrip("/"))
    cover = {}
    if game.get("card", {}).get("img"):
        c = game["card"]
        cover = {"src": c["img"], "w": c.get("img_w"), "h": c.get("img_h"), "alt": c.get("img_alt", "")}

    home_routes = {home_route, home_route.rstrip("/")}
    refs, by_route = [], {}
    crumb_label = {}   # dirkey -> 该目录下页面面包屑里出现最多的上级栏目名
    for route, info in found.items():
        if route in home_routes:
            continue
        ref = PageRef(route, info["title"], info["description"], "",
                      info["published"], info["modified"], slug)
        refs.append(ref)
        by_route[route] = ref
        cs = _crumb_section(info["ld"], origin, slug)
        if cs and info["dirkey"]:
            crumb_label.setdefault(info["dirkey"], {}).setdefault(cs[0], 0)
            crumb_label[info["dirkey"]][cs[0]] += 1

    # 1) 目录即栏目。标签优先取子站面包屑里的栏目名(它自己维护的),
    #    否则取该目录 index 页的标题,最后退到目录名。
    sec_by_label, assigned = {}, set()

    def sec_for(label, route=""):
        s = sec_by_label.get(label)
        if s is None:
            s = sec_by_label[label] = Section(re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-"),
                                             label, route)
        elif route and not s.route:
            s.route = route
        return s

    for dirkey, routes in sorted(dirs.items()):
        members = [by_route[r] for r in routes if r in by_route]
        # 只有自己 index 页的目录不是栏目,是一个顶层页(尾斜杠路由的站每页都占一个目录)
        if len(members) < 2:
            continue
        idx_route = f"/{slug}/{lang_root + '/' if lang_root else ''}{dirkey}/"
        labels = crumb_label.get(dirkey) or {}
        if labels:
            label = max(labels.items(), key=lambda kv: (kv[1], -len(kv[0])))[0]
        elif idx_route in found:
            label = found[idx_route]["title"]
        else:
            label = dirkey.replace("-", " ").replace("_", " ").title()
        sec = sec_for(label, idx_route if idx_route in found else "")
        for r in members:
            r.section = label
            assigned.add(r.route)
        sec.pages += members

    # 2) 深度 1 的页(扁平站):用 hub 页自己的卡片网格分组接管
    rest = [r for r in refs if r.route not in assigned]
    if rest and home_info:
        keep = {r.route for r in rest}
        for label, routes in _card_groups(home_info["raw"], keep, slug):
            members = [by_route[r] for r in routes if r in by_route and r not in assigned]
            if len(members) < 3:
                continue
            sec = sec_for(label)
            for r in members:
                r.section = label
                assigned.add(r.route)
            sec.pages += members
        rest = [r for r in refs if r.route not in assigned]

    # 3) 还剩下的页:兜底栏目(界面文字来自 config/i18n,不是游戏专属文字)
    if rest:
        sec = sec_for(fallback_label)
        sec.key = "_more"
        for r in rest:
            r.section = fallback_label
        sec.pages += rest

    sections = [s for s in sec_by_label.values() if s.pages]
    for s in sections:
        s.pages.sort(key=lambda p: p.title)
    sections.sort(key=lambda s: (s.key == "_more", -s.count, s.label))
    return GameIndex(game, home_route=home_route, sections=sections, pages=refs, cover=cover)


# ---------------------------------------------------------------- 站点级
class SiteIndex:
    """全站索引。games 按 config/hub.json 的顺序;原生游戏由 native 渲染器回填。"""

    def __init__(self):
        self.games = []

    def add(self, gi: GameIndex):
        self.games.append(gi)

    def by_slug(self, slug):
        return next((g for g in self.games if g.slug == slug), None)

    @property
    def page_count(self):
        return sum(g.page_count for g in self.games)

    def recent(self, n=40, lang=""):
        rows = [p for g in self.games for p in g.pages
                if p.date and (not lang or p.lang == lang)]
        return sorted(rows, key=lambda p: (p.date, p.game, p.title), reverse=True)[:n]

    def search_rows(self):
        """全站搜索索引的行。每条都带 game 与 lang,前端按 lang 过滤、按 game 显示归属。"""
        rows = []
        for g in self.games:
            for p in g.pages:
                rows.append({"url": p.route, "title": p.title,
                             "description": p.description[:180],
                             "game": g.short, "section": p.section, "lang": p.lang})
        return rows
