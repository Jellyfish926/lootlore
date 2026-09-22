"""snapshot —— 快照游戏(config/hub.json 里 kind=snapshot)的套壳渲染器。框架层。

输入:sources/<game>/**.html —— 各子站的构建产物(每日自动同步的镜像,内容真相源)
输出:out/<slug>/**(路径与子站一致),正文沿用子站产出,外壳换成 hub 统一外壳
     —— 与 /valheim/(hub/native.py)共用 hub/shell.py 的同一套组件与同一份 hub.css。

三条硬规矩:
  1. 正文零改动。只做三件"搬位置"的事:H1 → 外壳标题区、子站自带的面包屑 → 外壳面包屑、
     子站自带的署名行 → 外壳 byline 位;其余 <main> 内 HTML 原样搬进 <div class="doc">。
     不改写、不补词、不删句(唯一的结构性补充是给没有 id 的 h2/h3 补锚点 id,纯属性,
     与 hub/native.py 给原生内容加锚点是同一件事)。
  2. head 元数据沿用子站产出的原值:title / description / canonical / hreflang(含 x-default)/
     og / twitter / JSON-LD 全部原样保留,一个字都不重写。只补子站确实没有的(og:site_name)。
  3. 界面文字跟每页 <html lang> 走 config/i18n/<lang>.json,缺 key 回退英文。

本文件不含任何游戏专属文字,也不含任何色号:栏目名来自子站页面自己的面包屑/卡片网格,
界面文字来自 config/i18n,颜色一律走 out/hub.css 的 :root 变量。
"""
import hashlib
import html as _html
import json
import re
from pathlib import Path

from hub import mdlite, shell
from hub.hubbody import HubBodyMixin
from hub.mdlite import esc
from hub.native import EntityBox
from hub.pageindex import snapshot_index

TAG_RE = re.compile(r"<[^>]+>")
CLS_RE = re.compile(r'\bclass="([^"]*)"', re.I)
LD_RE = re.compile(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', re.S | re.I)
SCRIPT_RE = re.compile(r'<script\b((?:"[^"]*"|\'[^\']*\'|[^>"\'])*)>(.*?)</script>', re.S | re.I)
MAIN_RE = re.compile(r'<main\b[^>]*>(.*)</main>', re.S | re.I)
H1_RE = re.compile(r'<h1\b[^>]*>(.*?)</h1>', re.S | re.I)
H2_START_RE = re.compile(r'<h2\b', re.I)
HEAD_RE = re.compile(r'<head\b[^>]*>(.*?)</head>', re.S | re.I)
HTML_LANG_RE = re.compile(r'<html\b[^>]*\blang="([^"]*)"', re.I)
HEADING_RE = re.compile(r'<(h[23])\b((?:"[^"]*"|\'[^\']*\'|[^>"\'])*)>(.*?)</\1>', re.S | re.I)
ID_ATTR_RE = re.compile(r'\bid="([^"]*)"', re.I)
ALL_IDS_RE = re.compile(r'\bid="([^"]+)"', re.I)

# head 里逐字保留的元数据,按这个顺序输出(值全部是子站产出的原值)
HEAD_KEEP = (
    re.compile(r'<title\b[^>]*>.*?</title>', re.S | re.I),
    re.compile(r'<meta\s+name="description"[^>]*>', re.I),
    re.compile(r'<meta\s+name="robots"[^>]*>', re.I),
    re.compile(r'<link\s+rel="canonical"[^>]*>', re.I),
    re.compile(r'<link\s+rel="alternate"[^>]*>', re.I),
    re.compile(r'<link\s+rel="(?:prev|next)"[^>]*>', re.I),
    # 子站给首屏大图打的 preload 照搬(只要图片那一种;子站的 CSS/字体 preload 不搬,那些文件不在了)
    re.compile(r'<link\s+rel="preload"[^>]*\bas="image"[^>]*>', re.I),
    re.compile(r'<meta\s+property="og:[^"]*"[^>]*>', re.I),
    re.compile(r'<meta\s+name="twitter:[^"]*"[^>]*>', re.I),
    re.compile(r'<meta\s+property="article:[^"]*"[^>]*>', re.I),
)

# 子站自带的面包屑 / 署名行 / 空广告位的 class 记号(各子站都用这几个名字,见 sources/*/)
CRUMB_CLASSES = ("crumbs", "crumb", "breadcrumb", "breadcrumbs")
BYLINE_CLASSES = ("meta", "updated", "byline")
AD_CLASSES = ("ad-native", "ad-banner", "ad-slot", "ad")


def _text(s: str) -> str:
    return _html.unescape(TAG_RE.sub("", s or "")).strip()


def _url_host(url: str) -> str:
    u = (url or "").split("//", 1)[-1]
    return u.split("/", 1)[0].lower().removeprefix("www.")


def _norm(s: str) -> str:
    return " ".join(_text(s).split())


def _slug(text: str, used: set) -> str:
    """锚点 id:与 hub/mdlite.slugify 同一套规则(小写、非词字符折成连字符、重名加序号)。"""
    base = re.sub(r"[^\w-]+", "-", _norm(text).lower()).strip("-") or "section"
    s, k = base, 2
    while s in used:
        s, k = f"{base}-{k}", k + 1
    used.add(s)
    return s


def _tag_pat(tag: str):
    return re.compile(r'<(/?)' + tag + r'\b((?:"[^"]*"|\'[^\']*\'|[^>"\'])*)(/?)>', re.I)


def _find_element(html: str, tag: str, *, classes=None, start=0, limit=None):
    """找 [start, limit) 内第一个 <tag> 且 class 命中 classes 的元素,同名标签按深度配平。
    返回 (open_start, open_end, close_start, close_end);找不到返回 None。"""
    limit = len(html) if limit is None else limit
    pat = _tag_pat(tag)
    i = start
    while True:
        m = pat.search(html, i, limit)
        if not m:
            return None
        if m.group(1):                      # 闭合标签
            i = m.end()
            continue
        if classes is not None:
            cl = CLS_RE.search(m.group(2))
            if not (set((cl.group(1) if cl else "").split()) & set(classes)):
                i = m.end()
                continue
        if m.group(3):                      # 自闭合
            return m.start(), m.end(), m.end(), m.end()
        depth, j = 1, m.end()
        while depth:
            n = pat.search(html, j)
            if not n:
                return None
            if n.group(1):
                depth -= 1
                if depth == 0:
                    return m.start(), m.end(), n.start(), n.end()
            elif not n.group(3):
                depth += 1
            j = n.end()
        i = m.end()


def _cut(html: str, span):
    """删掉一个元素,返回 (新 html, 内层 html)。"""
    a, b, c, d = span
    return html[:a] + html[d:], html[b:c]


# ---------------------------------------------------------------- 正文分段(零改动)
TAG_ANY_RE = re.compile(r'<(/?)([a-zA-Z][\w-]*)\b((?:"[^"]*"|\'[^\']*\'|[^>"\'])*)(/?)>')
VOID_TAGS = {"img", "br", "hr", "meta", "link", "input", "source", "area", "base",
             "col", "embed", "param", "track", "wbr"}


def split_at_h2(body: str, indices):
    """把正文按 <h2> 序号(1 起)切成若干段 —— 只为了在段之间插入外壳层的新模块。

    🔴 正文一个字节都不改:切点只落在标签与标签之间,返回的 parts 逐字节拼起来 == 传入的 body
    (.gates/check_snapshot.py 每次构建后都实测这一条)。frames[i] 是第 i 个切点处仍然打开的
    元素栈 [(tag, attrs)],调用方在前一段末尾补 </tag>、在后一段开头补 <tag attrs> 把 DOM 配平
    —— 补出来的标签是外壳层的,不算正文字节。

    切点还会向外"贴边":如果 <h2> 正好是某个容器(如 <section class="wrap">)的第一个子元素,
    切点挪到那个容器的开标签之前,这样新模块不会被塞进子站自己的小节里。
    """
    if not indices:
        return [body], [], []
    want = sorted({i for i in indices if i and i > 0})
    stack = []            # [(tag, attrs, open_start, content_start)]
    cuts, seen_h2 = [], 0
    for m in TAG_ANY_RE.finditer(body):
        close, tag, attrs, self_c = m.group(1), m.group(2).lower(), m.group(3), m.group(4)
        if not close and tag == "h2":
            seen_h2 += 1
            if seen_h2 in want:
                cut, st = m.start(), list(stack)
                while st and not body[st[-1][3]:cut].strip():
                    cut = st[-1][2]
                    st.pop()
                cuts.append((cut, [(t, a) for t, a, _o, _c in st], seen_h2))
        if tag in VOID_TAGS or self_c:
            continue
        if close:
            if stack:
                stack.pop()
        else:
            stack.append((tag, attrs, m.start(), m.end()))
    parts, frames, applied, last = [], [], [], 0
    for cut, st, n in cuts:
        if cut <= last:
            continue
        parts.append(body[last:cut])
        frames.append(st)
        applied.append(n)
        last = cut
    parts.append(body[last:])
    return parts, frames, applied


# ---------------------------------------------------------------- 单页解析
class SnapPage:
    """一个快照页解析出来的全部素材。每一项都来自文件本身,没有就是空,不填默认值。"""

    __slots__ = ("route", "path", "lang", "head", "jsonld", "ld_objs", "body", "h1",
                 "byline", "heads", "scripts", "has_crumb_ld")

    def __init__(self, route, path):
        self.route, self.path = route, path
        self.lang = ""
        self.head = []          # 子站 head 里逐字保留的标签
        self.jsonld = []        # 子站 JSON-LD(原样字符串)
        self.ld_objs = []       # 解析后的 JSON-LD 对象(只读,用来取面包屑/FAQ)
        self.body = ""          # <main> 内的正文(摘掉面包屑 / H1 / 署名行之后)
        self.h1 = ""            # H1 内层 HTML(逐字)
        self.byline = ""        # 子站署名行内层 HTML(逐字)
        self.heads = []         # [(级别, 纯文本, id)] —— 正文小标题与锚点
        self.scripts = []       # 页面自带的内联脚本(交互件用),逐字搬过来
        self.has_crumb_ld = False


def parse_page(raw: str, route: str, path: Path) -> SnapPage:
    p = SnapPage(route, path)
    m = HTML_LANG_RE.search(raw)
    p.lang = (m.group(1) if m else "").strip()

    hm = HEAD_RE.search(raw)
    head_src = hm.group(1) if hm else raw
    for pat in HEAD_KEEP:
        p.head += pat.findall(head_src) if pat.groups else [x.group(0) for x in pat.finditer(head_src)]

    mm = MAIN_RE.search(raw)
    if not mm:
        raise ValueError(f"{path}: 没有 <main>,套不了壳")
    body = mm.group(1)

    # JSON-LD:head 里的 + <main> 里的(Next 站把它放在 main 内),一律原样搬进新 head
    for src in (head_src, body):
        for x in LD_RE.finditer(src):
            p.jsonld.append(x.group(0))
            try:
                d = json.loads(x.group(1))
            except Exception:
                continue
            p.ld_objs += d if isinstance(d, list) else [d]
    body = LD_RE.sub("", body)
    p.has_crumb_ld = any(o.get("@type") == "BreadcrumbList" for o in p.ld_objs if isinstance(o, dict))

    # 页面自带的交互件脚本(ld+json 已摘走;三方脚本在 URL 改写阶段就被剥掉了)
    for x in SCRIPT_RE.finditer(raw):
        if "application/ld+json" in (x.group(1) or "").lower():
            continue
        if not x.group(2).strip():
            continue
        p.scripts.append(x.group(0))

    # 1) 子站自带的面包屑 → 交给外壳的面包屑组件
    for tag in ("nav", "p", "ol", "div"):
        span = _find_element(body, tag, classes=CRUMB_CLASSES)
        if span:
            body, _ = _cut(body, span)
            break

    # 2) H1 → 交给外壳标题区(内层 HTML 逐字,连 <br> 都不动)
    h1 = H1_RE.search(body)
    if h1:
        p.h1 = h1.group(1)
        h1_at = h1.start()
        body = body[:h1.start()] + body[h1.end():]
    else:
        h1_at = -1

    # 3) 子站自带的署名行 = H1 之后、第一个 <h2> 之前的第一个 meta/updated/byline 段落
    if h1_at >= 0:
        nxt = H2_START_RE.search(body, h1_at)
        span = _find_element(body, "p", classes=BYLINE_CLASSES, start=h1_at,
                             limit=nxt.start() if nxt else None)
        if span:
            body, inner = _cut(body, span)
            p.byline = inner

    # 4) 空广告位(子站留的 hidden 占位,内层是空的)不搬过来
    while True:
        span = _find_element(body, "aside", classes=AD_CLASSES)
        if not span or body[span[1]:span[2]].strip():
            break
        body, _ = _cut(body, span)

    # 5) 给没有 id 的 h2/h3 补锚点 id(纯属性,正文文字一个不动)
    used = set(ALL_IDS_RE.findall(body))
    out, last = [], 0
    for m in HEADING_RE.finditer(body):
        lvl, attrs, inner = m.group(1).lower(), m.group(2), m.group(3)
        cur = ID_ATTR_RE.search(attrs)
        if cur:
            hid = cur.group(1)
        else:
            hid = _slug(inner, used)
            attrs = f' id="{hid}"' + attrs
        p.heads.append((int(lvl[1]), _norm(inner), hid))
        out.append(body[last:m.start()] + f"<{lvl}{attrs}>{inner}</{lvl}>")
        last = m.end()
    p.body = ("".join(out) + body[last:]).strip()
    return p


# ---------------------------------------------------------------- 单语种渲染
class SnapshotLang(EntityBox, HubBodyMixin):
    """一个快照游戏的一个语种。栏目分组由 hub/pageindex.py 从真实文件发现,本类只管套壳。"""

    def __init__(self, game_site, root_path: str, lang: str):
        self.gs = game_site
        self.root_path = root_path          # 该语种在子站里的根路径("/" 或 "/ja")
        self.lang = lang
        self.t = game_site.i18n(lang)
        self.nk = (lang or "en").split("-")[0]
        self.lang_keys = game_site.lang_keys
        self.ents = game_site.ents
        g = dict(game_site.g, default_path=root_path)
        self.index = snapshot_index(game_site.root, g, self.t["more_guides"])
        self.home_route = self.index.home_route
        self.by_route = {p.route: p for p in self.index.pages}
        # slug → 路由。既认末段("weapons"),也认该语种根之下的完整相对路径
        # ("towers/cannon" —— entities.json 的 page_slug 就是这么写的)。末段优先,
        # 完整路径只在末段没占位时补进来,不覆盖既有映射。
        self.by_slug = {p.route.rstrip("/").rsplit("/", 1)[-1]: p.route for p in self.index.pages}
        pre = self.home_route
        for p in self.index.pages:
            rel = p.route[len(pre):].strip("/") if p.route.startswith(pre) else p.route.strip("/")
            if rel:
                self.by_slug.setdefault(rel, p.route)
        self.sec_of = {}                    # route -> Section
        for s in self.index.sections:
            for p in s.pages:
                self.sec_of.setdefault(p.route, s)
        self.pages = {}                     # route -> SnapPage

    # -------------------------------------------------- EntityBox 需要的两个钩子
    def rel_slug(self, route: str) -> str:
        """页面路由 → 该语种根之下的相对路径(实体数据的 page_slug 就是按这个写的)。"""
        pre = self.home_route
        return route[len(pre):].strip("/") if route.startswith(pre) else route.strip("/")

    def route_slug(self, slug):
        return self.by_slug.get(slug, "")

    def is_live(self, slug):
        return slug in self.by_slug

    # -------------------------------------------------- 解析
    def add(self, route: str, raw: str, path: Path):
        self.pages[route] = parse_page(raw, route, path)

    def section_routes(self):
        """没有 index 页的栏目(扁平站的卡片分组):把磁贴指向 hub 页上该分组标题的锚点。
        锚点 id 就是 hub 页真实渲染出来的那个 id,不是猜的。"""
        hub = self.pages.get(self.home_route) or self.pages.get(self.home_route.rstrip("/"))
        by_label = {}
        if hub:
            for lvl, text, hid in hub.heads:
                by_label.setdefault(text.lower(), hid)
        for s in self.index.sections:
            if s.route:
                continue
            hid = by_label.get(s.label.lower())
            if hid:
                s.route = f"{self.home_route}#{hid}"

    # -------------------------------------------------- hub 页正文模块的数据源
    def hb_spec(self):
        return self.gs.g.get("hub_body") or {}

    def _hb_pool(self):
        return [im for im in self.index.shot_pool if im and im.get("src") and im.get("alt")]

    def _hb_pick_img(self, route, used):
        """一个栏目/工具用哪张缩略图:先要那一页自己的配图,撞车了按 route 的 sha1 从该游戏的
        官方截图池里换一张没用过的 —— 固定映射,构建间稳定(与首页 #by-game 同一机制)。"""
        ref = self.by_route.get(route)
        im = self.index.image_for(ref) if ref is not None else None
        if im and im.get("src") not in used:
            used.add(im["src"])
            return im
        pool = [x for x in self._hb_pool() if x.get("src") not in used]
        if not pool:
            if im:
                used.add(im.get("src"))
            return im
        i = int(hashlib.sha1(route.encode("utf-8")).hexdigest()[:8], 16) % len(pool)
        used.add(pool[i]["src"])
        return pool[i]

    def hb_sections(self):
        used, out = set(), []
        for s in self.index.sections:
            if not s.route:
                continue
            out.append((s.label, s.route, s.count, self._hb_pick_img(s.route, used)))
        return out

    def _hb_tool_pages(self):
        keys = [k.lower() for k in self.gs.cfg.get("tools_match", [])]
        return sorted((p for p in self.index.pages
                       if any(k in p.title.lower() for k in keys)), key=lambda p: p.title)

    def hb_tools(self):
        used = {im.get("src") for _l, _r, _c, im in self.hb_sections() if im}
        return [(p.title, p.route, p.description, self._hb_pick_img(p.route, used))
                for p in self._hb_tool_pages()]

    def hb_featured(self, n=6):
        """各栏目轮转取,栏目内按页面自记复核日倒序 —— 与首页 #by-game 精选同一条规则。
        兜底桶(_more)与栏目自己的落地页不进来;没有日期的页排在最后但仍可入选。"""
        lands = {s.route.rstrip("/") for s in self.index.sections if s.route}
        queues = []
        for sec in self.index.sections:
            if sec.key == "_more":
                continue
            ps = [p for p in sec.pages if p.route.rstrip("/") not in lands]
            ps.sort(key=lambda p: (p.date, p.title), reverse=True)
            if ps:
                queues.append((sec.label, ps))
        if not queues:
            queues = [("", sorted(self.index.pages, key=lambda p: (p.date, p.title), reverse=True))]
        out, seen, i, guard = [], set(), 0, 0
        used = {im.get("src") for _l, _r, _c, im in self.hb_sections() if im}
        while queues and len(out) < n and guard < 300:
            guard += 1
            label, q = queues[i % len(queues)]
            i += 1
            while q:
                p = q.pop(0)
                if p.route in seen:
                    continue
                seen.add(p.route)
                out.append((label, p.title, p.route, p.date, self._hb_pick_img(p.route, used)))
                break
            if not any(q for _l, q in queues):
                break
        return out

    def hb_recent(self, n=5):
        return [(p.title, p.route, p.date) for p in self.index.recent(n + 2) if p.date][:n]

    def hb_counts(self):
        return {"pages": len(self.index.pages), "sections": len(self.index.sections),
                "tools": len(self._hb_tool_pages()), "langs": len(self.gs.langs),
                "entities": len(self.ents), "updated": self.index.updated}

    def hb_quote(self):
        """范围提示框:逐字取该游戏自己某一页的第 N 个 <h2> 与它后面第一段的若干句。
        配置只声明"取哪一页、第几个 h2、跳几句、取几句",一个字都不是我们写的;
        各语种取的是各语种那一页自己的原文,所以自动跟着页面语言走。"""
        spec = (self.hb_spec().get("scope") or {})
        slug = spec.get("slug")
        route = self.route_slug(slug) if slug else ""
        page = self.pages.get(route) or self.pages.get(route.rstrip("/"))
        if not page:
            return None
        hs = list(re.finditer(r'<h2\b[^>]*>(.*?)</h2>', page.body, re.S))
        i = int(spec.get("h2") or 0) - 1
        if not (0 <= i < len(hs)):
            return None
        title = _norm(hs[i].group(1))
        pm = re.search(r'<p\b[^>]*>(.*?)</p>', page.body[hs[i].end():], re.S)
        if not pm:
            return None
        text = _norm(pm.group(1))
        sents = re.findall(r'[^.\u3002]*[.\u3002]', text) or [text]
        last = int(spec.get("last") or 0)
        if last:
            quote = "".join(sents[-last:]).strip()
        else:
            skip, take = int(spec.get("skip") or 0), int(spec.get("take") or 1)
            quote = "".join(sents[skip:skip + take]).strip()
        if not quote:
            return None
        ref = self.by_route.get(route)
        return title, quote, route, (ref.title if ref else _norm(page.h1))

    def hb_self_hosts(self):
        return {_url_host(self.gs.base), _url_host(self.gs.g.get("origin", ""))} - {""}

    def hb_gslug(self):
        return self.gs.gslug

    # -------------------------------------------------- 外壳零件
    def nav_sections(self):
        """栏目 index 页本身也在 pageindex 的成员清单里(它就是该目录下的一个页),
        但外壳已经用「Section overview」那一行代表它了 —— 列表里不再重复一遍。
        count 仍是该栏目的真实页数(overview 那一行就是其中一页)。"""
        out = []
        for s in self.index.sections:
            pages = [{"title": p.title, "route": p.route} for p in s.pages
                     if not (s.route and p.route == s.route)]
            out.append({"label": s.label, "route": s.route, "count": s.count, "pages": pages})
        return out

    def sidebar(self, route: str, t: dict):
        g = self.gs.g
        c = g.get("card", {})
        author = self.by_slug.get("author", "")
        about = []
        if author:
            ap = self.by_route.get(author)
            about.append(((ap.title if ap else t["author"]), author, author))
        about += [(n, h, None) for n, h in t["trust"][:3]]
        return shell.game_nav(
            game_name=g.get("short") or g["name"], game_href=self.home_route,
            subtitle=c.get("genre", ""),
            cover={"src": c.get("img", ""), "alt": c.get("img_alt", "")} if c.get("img") else None,
            sections=self.nav_sections(), tools=(), about=about, current=route, t=t)

    def crumbs(self, page: SnapPage, t: dict):
        """三/四级面包屑。中间几级优先取页面自带的 BreadcrumbList(子站自己维护的、已本地化),
        没有就退到索引发现的栏目。返回 (html, 需要补的 JSON-LD 或 None)。"""
        g = self.gs.g
        items = [(self.gs.cfg["brand"], "/"), (g.get("short") or g["name"], self.home_route)]
        mid = []
        for o in page.ld_objs:
            if not isinstance(o, dict) or o.get("@type") != "BreadcrumbList":
                continue
            els = o.get("itemListElement") or []
            for e in els[1:-1]:
                name = _norm(str(e.get("name") or ""))
                item = str(e.get("item") or "")
                if name:
                    mid.append((name, item[len(self.gs.base):] if item.startswith(self.gs.base) else None))
            break
        if not mid:
            s = self.sec_of.get(page.route)
            if s is not None and s.label:
                mid = [(s.label, s.route or None)]
        if page.route in (self.home_route, self.home_route.rstrip("/")):
            items = items[:1] + [(items[1][0], None)]
            mid = []
        else:
            ref = self.by_route.get(page.route)
            items += mid + [(_norm(page.h1) or (ref.title if ref else ""), None)]
        html, ld = shell.crumbs(items, self.gs.base, label=t["breadcrumb"])
        return html, (None if page.has_crumb_ld else ld)

    def rail(self, page: SnapPage, t: dict):
        """右栏:实体信息框(匹配到才有)+ 最近更新(hub 页与栏目页)。都为空就不出右栏。"""
        out = "".join(self.gs.quick_facts_for(self, page))
        ents_rendered = bool(out)
        is_hub = page.route in (self.home_route, self.home_route.rstrip("/"))
        is_sec = any(s.route == page.route for s in self.index.sections)
        if is_hub or is_sec:
            rows = [(p.title, p.route, p.date) for p in self.index.recent(6)
                    if p.route != page.route][:5]
            out += shell.rail_list(t["recent_in_game"], rows)
        return out, ents_rendered

    def lang_switch(self, page: SnapPage, t: dict):
        """语言切换器:候选语种完全取自页面自己的 hreflang(子站维护的),标签取 i18n 的 lang_<code>。
        子站只声明了自己一种语言的页面不出切换器 —— 不替子站补语种。"""
        alts = []
        for tag in page.head:
            m = re.search(r'rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)"', tag)
            if not m:
                continue
            code, href = m.group(1).lower(), m.group(2)
            if code == "x-default" or any(code == c for c, _ in alts):
                continue
            alts.append((code, href[len(self.gs.base):] if href.startswith(self.gs.base) else href))
        if len(alts) < 2:
            return ""
        cur = (page.lang or self.lang).split("-")[0].lower()
        links = "".join(f'<a href="{esc(r)}" hreflang="{esc(c)}" lang="{esc(c)}">'
                        f'{esc(t.get(f"lang_{c}", c.upper()))}</a>'
                        for c, r in alts if c != cur)
        if not links:
            return ""
        return (f'<p class="langsw"><span>{esc(t["language"])}{esc(t["colon"])}</span>'
                f'<span class="cur">{esc(t.get(f"lang_{cur}", cur.upper()))}</span>{links}</p>')

    # -------------------------------------------------- 正文容器
    def doc_html(self, page: SnapPage) -> str:
        """hub 页:在子站正文的小节之间插入外壳层的新模块(hub/hubbody.py),
        正文本身逐字节不动 —— 只是被分装进多个 .sn-body 容器,拼起来与原文完全一致。
        其余页(内容页)一律原样一段,外壳层不往里插任何东西。"""
        body = f'<div class="prose sn-body">{page.body}</div>'
        if page.route not in (self.home_route, self.home_route.rstrip("/")):
            return body
        slots = self.hb_spec().get("slots") or []
        if not slots:
            return body
        used = set(ALL_IDS_RE.findall(page.body))
        head = [x for x in slots if int(x.get("h2") or 0) == 0]
        tail = [x for x in slots if int(x.get("h2") or 0) < 0]
        mids = sorted((x for x in slots if int(x.get("h2") or 0) > 0), key=lambda x: int(x["h2"]))
        parts, frames, applied = split_at_h2(page.body, [int(x["h2"]) for x in mids])
        if "".join(parts) != page.body:                     # 分段必须是零改动
            raise AssertionError(f"{page.path}: hub 页正文分段后与原文不一致")
        by_h2 = {int(x["h2"]): (x.get("mods") or []) for x in mids}
        out = [self.hb_render(x.get("mods") or [], used)[0] for x in head]
        for k, part in enumerate(parts):
            # 切点落在子站自己的容器里时,前一段末尾补 </tag>、后一段开头补 <tag attrs> 配平 DOM。
            # 这几个补出来的标签夹在 <!--hbf--> … <!--/hbf--> 之间,.gates/check_snapshot.py
            # 把这段整体去掉之后,各段拼起来必须与原文逐字节相同。
            fo = frames[k - 1] if k else []
            fc = frames[k] if k < len(frames) else []
            opens = ("".join(f"<{tg}{at}>" for tg, at in fo) + "<!--/hbf-->") if fo else ""
            closes = ("<!--hbf-->" + "".join(f"</{tg}>" for tg, _a in reversed(fc))) if fc else ""
            out.append(f'<div class="prose sn-body">{opens}{part}{closes}</div>')
            if k < len(applied):
                out.append(self.hb_render(by_h2.get(applied[k], []), used)[0])
        out += [self.hb_render(x.get("mods") or [], used)[0] for x in tail]
        return "".join(x for x in out if x)

    # -------------------------------------------------- 整页
    def render(self, page: SnapPage) -> str:
        t = self.gs.i18n(page.lang or self.lang)
        crumbs_html, crumb_ld = self.crumbs(page, t)
        aside, has_ent = self.rail(page, t)
        head = list(page.head)
        if not any('property="og:site_name"' in x for x in head):
            head.append(f'<meta property="og:site_name" content="{esc(self.gs.cfg["brand"])}">')
        head += page.jsonld
        if crumb_ld is not None:
            head.append('<script type="application/ld+json">'
                        + json.dumps(crumb_ld, ensure_ascii=False, separators=(",", ":"))
                        .replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
                        + "</script>")
        byline = f'<p class="byline">{page.byline}</p>' if page.byline.strip() else ""
        cls = "layout" + ("" if aside else " no-rail") + ("" if has_ent else " rail-last" if aside else "")
        toggle = ('<input type="checkbox" id="navtoggle" class="navtoggle">'
                  f'<label class="navtoggle-l" for="navtoggle"><span aria-hidden="true">&#9776;</span> '
                  f'{esc(t["open_menu"])}</label>')
        main = (f'<main class="{cls}" id="main">\n{toggle}\n{self.sidebar(page.route, t)}\n'
                f'{crumbs_html}\n<div class="doc-hd"><h1>{page.h1}</h1>{byline}'
                f'{self.lang_switch(page, t)}</div>\n'
                + (f'<aside class="rail">{aside}</aside>\n' if aside else "")
                + f'<div class="doc">{self.doc_html(page)}</div>\n</main>')
        intents = [(t[k], h) for k, h in self.gs.cfg.get("intent_nav", [])]
        header = shell.site_nav(
            brand=self.gs.cfg["brand"], games=self.gs.site["nav_games"], intents=intents,
            active_game=self.gs.gslug,
            search=shell.search_form(action="/guides", index_url="/search-index.json",
                                     lang=(page.lang or self.lang).split("-")[0], t=t,
                                     scope=self.gs.g.get("short") or self.gs.g["name"],
                                     placeholder=t["search_all_placeholder"]), t=t)
        ft_links = list(t["trust"])
        footer = shell.footer(brand=self.gs.cfg["brand"], year=self.gs.site["year"],
                             links=ft_links, note=t["footer_note"])
        tpl = (self.gs.root / "hub" / "snapshot_page.html").read_text(encoding="utf-8")
        return (tpl.replace("{{LANG}}", esc(page.lang or self.lang))
                .replace("{{HEAD}}", "\n".join(head))
                .replace("{{FONTS}}", self.gs.site.get("font_links", ""))
                .replace("{{HEAD_EXTRA}}", self.gs.site["head_extra"])
                .replace("{{HEADER}}", header)
                .replace("{{MAIN}}", main)
                .replace("{{SCRIPTS}}", "".join(page.scripts) + shell.SEARCH_JS)
                .replace("{{FOOTER}}", footer))


# ---------------------------------------------------------------- 游戏级
class SnapshotGame:
    """一个快照游戏 = N 个语种。语种清单从子站 hub 页自己的 hreflang 里发现,不手工维护。"""

    def __init__(self, root: Path, game: dict, cfg: dict, site: dict):
        self.root, self.g, self.cfg, self.site = root, game, cfg, site
        self.gslug = game["slug"]
        self.base = site["base"]
        self.src = root / game["source"]
        self._i18n = {}
        self.stats = {"pages": 0, "entity_boxes": 0, "langs": 0, "sections": 0}
        ef = game.get("entities")
        self.ents = {}
        if ef and (root / ef).is_file():
            try:
                self.ents = json.loads((root / ef).read_text(encoding="utf-8")).get("entities", {}) or {}
            except Exception:
                self.ents = {}
        self.match_by = game.get("entity_match") or ["page_slug"]
        self.entity_max = int(game.get("entity_max") or 3)
        self.lang_keys = {l for l in self._roots_and_langs()[1]} | {"en"}
        self.langs = [SnapshotLang(self, rp, lg) for rp, lg in zip(*self._roots_and_langs())]
        self.default = self.langs[0]

    # -------------------------------------------------- i18n
    def i18n(self, lang: str) -> dict:
        key = (lang or "en").split("-")[0].lower() or "en"
        if key not in self._i18n:
            base = json.loads((self.root / "config" / "i18n" / "en.json").read_text(encoding="utf-8"))
            f = self.root / "config" / "i18n" / f"{key}.json"
            if f.is_file():
                base.update(json.loads(f.read_text(encoding="utf-8")))
            self._i18n[key] = base
        return self._i18n[key]

    # -------------------------------------------------- 语种发现
    def _home_file(self, root_path: str):
        p = root_path.strip("/")
        for cand in ((self.src / p / "index.html") if p else (self.src / "index.html"),
                     self.src / f"{p}.html"):
            if cand.is_file():
                return cand
        return None

    def _roots_and_langs(self):
        if getattr(self, "_rl", None):
            return self._rl
        dp = self.g.get("default_path", "/")
        roots = [dp if dp.startswith("/") else "/" + dp]
        hf = self._home_file(roots[0])
        raw = hf.read_text(encoding="utf-8", errors="replace") if hf else ""
        for code, href in re.findall(r'<link\s+rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)"', raw):
            if code.lower() == "x-default":
                continue
            tail = href[len(self.g["origin"].rstrip("/")):] if href.startswith(self.g["origin"].rstrip("/")) else ""
            seg = "/" + tail.strip("/").split("/")[0] if tail.strip("/") else "/"
            if seg not in roots and self._home_file(seg):
                roots.append(seg)
        langs = []
        for r in roots:
            f = self._home_file(r)
            m = HTML_LANG_RE.search(f.read_text(encoding="utf-8", errors="replace")) if f else None
            langs.append(((m.group(1) if m else "en").split("-")[0].lower()))
        self._rl = (roots, langs)
        return self._rl

    # -------------------------------------------------- 实体绑定(只做渲染侧接线)
    def quick_facts_for(self, lang: SnapshotLang, page: SnapPage):
        """按配置的绑定方式把页面对上实体,渲染成右栏信息框(配置层 entity_match 决定用哪几种)。

          page_slug —— 实体的 page_slug 对页面在该语种根之下的相对路径(数据里写的是
                       "towers/cannon" / "endings/grave-decision" 这种多段路径,也允许单段)
          h1        —— 实体名与页面 H1 原文完全相同

        实体文件不存在 / 对不上 / 一行事实都凑不出来 → 静默不渲染,不出空框、不出占位值。"""
        if not self.ents:
            return []
        rel = lang.rel_slug(page.route)
        h1 = _norm(page.h1).lower()
        hit = []
        for e in self.ents.values():
            if not isinstance(e, dict):
                continue
            for how in self.match_by:
                if how == "page_slug" and rel and str(e.get("page_slug") or "").strip("/") == rel:
                    hit.append(e)
                    break
                if how == "h1" and h1 and str(lang.loc(e, "name")).strip().lower() == h1:
                    hit.append(e)
                    break
        # 一页对上太多实体说明它是清单页(比如成就总表),那就不是"本页讲这一个实体"了 ——
        # 右栏不该堆几十个折叠框。上限写在配置层(entity_max),超了就整页不渲染。
        if len(hit) > self.entity_max:
            return []
        # 同名实体(数据里同一个东西分了两条,比如"结局"和"同名成就")只出一个框,
        # 留信息更全的那条 —— 右栏不出两个标题一样的框。
        best = {}
        for e in hit:
            html = lang.quick_facts(e, generic=True)
            if not html:
                continue
            key = str(lang.loc(e, "name")).strip().lower()
            if html.count("<dt>") > best.get(key, ("", -1))[1]:
                best[key] = (html, html.count("<dt>"))
        out = [v[0] for v in best.values()]
        self.stats["entity_boxes"] += 1 if out else 0
        return out

    # -------------------------------------------------- 构建
    def build(self, out_root: Path, transform):
        """transform(html, game) = build.py 的 URL 改写(剥三方脚本 + 原站域名/根相对链接 → 总站)。
        解析在改写之后做,所以 head 与正文里的链接已经是总站 URL,外壳不必再二次改写。"""
        from hub.pageindex import _excluded, _route_of, TRUST_SLUGS
        dst = out_root / self.gslug
        by_root = {l.root_path.strip("/"): l for l in self.langs}
        routes = {}
        for p in sorted(self.src.rglob("*.html")):
            rel = p.relative_to(self.src)
            if _excluded(rel, self.g):
                continue
            seg = rel.parts[0] if len(rel.parts) > 1 else ""
            lang = by_root.get(seg, by_root.get(""))
            if lang is None:
                continue
            route = _route_of(self.gslug, rel)
            if route.rstrip("/").rsplit("/", 1)[-1] in TRUST_SLUGS:
                continue
            raw = p.read_text(encoding="utf-8")
            for patch in self.g.get("patches", []):
                if patch["file"] == str(rel):
                    assert patch["find"] in raw, f"patch find miss: {rel}"
                    raw = raw.replace(patch["find"], patch["find"] + patch["insert_after"], 1)
            lang.add(route, transform(raw, self.g), p)
        for l in self.langs:
            l.section_routes()
        for l in self.langs:
            for route, page in l.pages.items():
                rel = page.path.relative_to(self.src)
                target = dst / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(l.render(page), encoding="utf-8")
                routes[route] = page_lastmod(page) or self.site["today"]
                self.stats["pages"] += 1
        self.stats["langs"] = len(self.langs)
        self.stats["sections"] = len(self.default.index.sections)
        return routes

    def copy_assets(self, out_root: Path):
        """非 HTML 资源(图片 / 子站数据 json)照搬,路径与子站一致。"""
        dst = out_root / self.gslug
        n = 0
        for p in self.src.rglob("*"):
            if p.is_dir() or p.suffix == ".html":
                continue
            rel = p.relative_to(self.src)
            if _asset_excluded(rel, self.g) or p.name == ".DS_Store":
                continue
            if self.g.get("exclude_all_txt") and p.suffix == ".txt":
                continue
            target = dst / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(p.read_bytes())
            n += 1
        return n

    def index(self):
        """回填全站索引:栏目/页数/更新日取默认语种,其余语种的页只进搜索索引(带自己的 lang)。"""
        gi = self.default.index
        seen = {p.route for p in gi.pages}
        for l in self.langs[1:]:
            for p in l.index.pages:
                if p.route not in seen:
                    seen.add(p.route)
                    p.lang = l.lang
                    gi.pages.append(p)
        for p in gi.pages:
            if not p.lang:
                p.lang = self.default.lang
        gi.default_lang = self.default.lang
        return gi


def page_lastmod(page: SnapPage) -> str:
    """sitemap 的 lastmod:取页面自己 JSON-LD 里的 dateModified / datePublished。"""
    best = ""
    for o in page.ld_objs:
        if not isinstance(o, dict):
            continue
        for k in ("dateModified", "datePublished"):
            v = o.get(k)
            if isinstance(v, str) and re.match(r"^\d{4}-\d{2}-\d{2}", v):
                best = max(best, v[:10])
    return best


def _asset_excluded(rel: Path, game: dict) -> bool:
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
    return False
