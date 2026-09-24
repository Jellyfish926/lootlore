"""hubbody —— 游戏 hub 页正文的视觉模块组(框架层)。

为什么有这个文件:hub 页原来是"栏目卡片 + 一段长文 + FAQ",纯文字、零数据表,
站主的原话是"缺少趣味性,全是文字,也没有突出,让人没有看下去的欲望"。
对标(research/D-gamehub-body.md 表 A)里"纯 CSS / 我们素材够"的那几项:
数据表、带缩略图卡片网格、带图标磁贴、徽章胶囊、提示框、单行时间线、大号统计数字。

本文件只提供这些模块的 HTML 骨架,并且:
  * 不含任何游戏专属文字 —— 表头/模块标题一律走 config/i18n 的 f_<字段> / tbl_<type> / hub_*;
    没登记标签的字段直接构建报错(不猜、不humanize、不留空表头)。
  * 不含任何色号 —— 全部走 out/hub.css 的 :root 变量(见 hub/style.css 的 .hb-* 段)。
  * 不认识任何字段的含义 —— 出哪张表、取哪几列、怎么排序、行数上限,全在
    config/hub.json 的 games[].hub_body 里声明;本文件只按声明取值。

数据缺失的口径(硬规矩,与右栏 .qf 速查框同源):
  * 整列没有一个非空值 → 这一列不出(不出空列、不填占位)。
  * 单格没值 → 只写 em dash;若该字段在该条实体的 unverified_fields 里,
    写 config/i18n 的 nc_label(各子站页面里本来就在用的那句"Not confirmed"),不自己发明说法。
  * 有值但字段在 unverified_fields 里 → 值照出,后面挂同一个 nc_label 角标。

列声明支持三种 token(见 games[].hub_body.tables[].cols):
  "@name"        实体自己的本地化名字,有对应页就链过去(表头 key = c_name)
  "@ref:<字段>"  把该字段里的实体 id(单个或数组)解析成实体名 + 链接(表头 key = f_<字段>)
  "@qty:<字段>"  [{item_*, qty}] 形状的配方列表 → "材料 ×数量"(表头 key = f_<字段>)
  "<点路径>"      普通取值;单段字段名走实体的语种回退(hazards_en → hazards_<nk>),
                 多段 a.b 钻进子对象(表头 key = f_<下划线化路径>,退 f_<末段>)

失败关闭的两条:整列全空 → 整列不出;某列出现"指向同一条实体另一个字段名"的内部交叉引用
(数据管线自用的记号,没有任何页面把它印给读者)→ 整列不出并打印构建警告。
"""
import re

from hub import mdlite
from hub.mdlite import esc

NBSP = " "
DASH = "—"
# 形如内部字段名的 token(snake_case、含下划线、≥8 字符)
FIELD_TOKEN_RE = re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+){1,}\b")


def _host(url: str) -> str:
    u = (url or "").split("//", 1)[-1]
    return u.split("/", 1)[0].lower().removeprefix("www.")


def _resolve(obj, path):
    """点路径取值;中途断了就返回 None(不抛)。"""
    cur = obj
    for seg in path.split("."):
        if not isinstance(cur, dict):
            return None
        cur = cur.get(seg)
    return cur


def _empty(v) -> bool:
    return v is None or v == "" or v == [] or v == {}


class HubBodyMixin:
    """hub 页正文模块。宿主(hub/native.py 的 NativeLang、hub/snapshot.py 的 SnapshotLang)
    需要提供这些钩子:t / nk / ents / lang_keys / route_slug / is_live,以及下面 hb_* 数据源。"""

    # -------------------------------------------------- 宿主要实现的数据源(默认全空)
    def hb_spec(self) -> dict:
        return {}

    def hb_sections(self):
        """[(label, route, count, image|None)] —— 栏目 + 真实页数 + 缩略图。"""
        return []

    def hb_tools(self):
        """[(title, route, desc, image|None)] —— 该游戏自己的互动工具页。"""
        return []

    def hb_featured(self, n=6):
        """[(section_label, title, route, date, image|None)] —— 各栏目轮转取,
        栏目内按页面自记复核日倒序(与首页 #by-game 的精选同一条规则,没有任何"热门"排序)。"""
        return []

    def hb_recent(self, n=5):
        """[(title, route, date)] —— 按页面自记复核日倒序。"""
        return []

    def hb_counts(self) -> dict:
        """{pages, sections, tools, langs, entities} —— 数字全部来自实际统计。"""
        return {}

    def hb_quote(self):
        """(标题, 正文, 路由, 页标题) —— 全部逐字取自该游戏自己的某一页,见 hub_body.scope。"""
        return None

    def hb_self_hosts(self):
        """"自己家"的域名:总站域名 + 该游戏子站域名。用来判断某条 source_url 是站内自述
        还是真外部来源 —— 站内自述不能印成"Source: 某某站",那会把自己当成第三方引用。"""
        return set()

    def hb_gslug(self):
        return ""

    def hb_warn(self, msg):
        """构建期警告。宿主有 warnings 列表就记进去,否则直接打印 —— 不许静默。"""
        w = getattr(self, "warnings", None)
        if isinstance(w, list):
            w.append(msg)
        else:
            print(f"  警告: {msg}")

    def hb_img(self, im, cls="thumb"):
        if not im or not im.get("src"):
            return ""
        w, h = im.get("w"), im.get("h")
        wh = f' width="{w}" height="{h}"' if w and h else ""
        return (f'<img class="{cls}" src="{esc(im["src"])}"{wh} alt="{esc(im.get("alt", ""))}"'
                f' loading="lazy" decoding="async">')

    # -------------------------------------------------- 小工具
    def _hb_head_key(self, col):
        t = self.t
        if col == "@name":
            return t["c_name"]
        if col.startswith("@ref:") or col.startswith("@qty:"):
            col = col[5:]
        base = self._base_key(col.split(".")[-1]) if hasattr(self, "_base_key") else col.split(".")[-1]
        for key in (f'f_{col.replace(".", "_")}', f"f_{base}", f"f_{col.split('.')[-1]}"):
            if key in t:
                return t[key]
        if col in ("order", "level_number"):
            return t["c_order"]
        raise KeyError(f"hub_body: 列 {col!r} 在 config/i18n 里没有表头标签(f_… 或 c_…),"
                       f"补上标签或把这一列从 hub_body.tables[].cols 里去掉")

    def _hb_unverified(self, ent, col) -> bool:
        """字段是否被该条实体自己标为"未核实"。unverified_fields 的条目形如 "hp" 或
        "moveset (page states explicitly: …)",所以按字段名 + 分隔符前缀比。
        语种后缀两种写法都比(hazards_en 与 hazards)。"""
        field = col[5:] if col[:5] in ("@ref:", "@qty:") else col
        field = field.split(".")[0]
        names = {field, self._base_key(field)}
        for x in ent.get("unverified_fields") or []:
            v = str(x)
            for f in names:
                if v == f or v.startswith(f + " ") or v.startswith(f + "("):
                    return True
        return False

    def _hb_raw(self, ent, col):
        """列声明 → 原始取值(与 _hb_cell 同一套解析,给"整列是否全空"的判断用)。"""
        if col == "@name":
            return self.loc(ent, "name", None)
        if col[:5] in ("@ref:", "@qty:"):
            return _resolve(ent, col[5:])
        return self.loc(ent, self._base_key(col), None) if "." not in col else _resolve(ent, col)

    def _hb_scalar(self, v):
        """取值 → (纯文本, 是否数字)。列表/子对象走本地化取值,不 JSON 化。"""
        t = self.t
        if isinstance(v, bool):
            return (t["yes"] if v else t["no"]), False
        if isinstance(v, (int, float)):
            return str(v), True
        if isinstance(v, list):
            parts = []
            for x in v:
                if isinstance(x, dict):
                    nm = (self.loc(x, "name") or self.loc(x, "item") or self.loc(x, "label")
                          or x.get(self.nk) or x.get("en"))
                    if nm:
                        parts.append(str(nm))
                elif not _empty(x):
                    parts.append(str(x))
            return ", ".join(parts), False
        if isinstance(v, dict):
            nm = self.loc(v, "name") or self.loc(v, "item") or self.loc(v, "label")
            return (str(nm) if nm else ""), False
        return ("" if _empty(v) else str(v)), False

    def _hb_entity_link(self, eid_or_ent, ent_id=""):
        ent = self.ents.get(eid_or_ent) if isinstance(eid_or_ent, str) else eid_or_ent
        if not ent:
            return ""
        nm = esc(str(self.loc(ent, "name")))
        slug = ent.get("page_slug")
        r = self.route_slug(slug) if slug else ""
        return f'<a href="{esc(r)}">{nm}</a>' if r else nm

    def _hb_cell(self, ent, col):
        """→ (html, 纯文本, 是否数字)。"""
        t = self.t
        if col == "@name":
            nm = str(self.loc(ent, "name") or "")
            return self._hb_entity_link(ent), nm, False
        if col.startswith("@qty:"):
            rows = _resolve(ent, col[5:]) or []
            parts = []
            for r in rows:
                if not isinstance(r, dict):
                    continue
                item = self.loc(r, "item")
                qty = r.get("qty")
                # qty \u7f3a\u5931(None/\u7a7a)\u65f6\u53ea\u7ed9\u6750\u6599\u540d,\u4e0d\u62fc"\u00d7\u2026"\u540e\u7f00,\u4e0d\u8be5\u6e32\u67d3\u6210\u5b57\u9762\u4e0a\u7684 "\u00d7None"\u3002
                parts.append(f'{item}{NBSP}\u00d7{self.loc(r, "qty", qty)}'
                             if qty not in (None, "") else str(item))
            txt = ", ".join(parts)
            return esc(txt), txt, False
        if col.startswith("@ref:"):
            raw = _resolve(ent, col[5:])
            ids = raw if isinstance(raw, list) else ([raw] if raw else [])
            links, names = [], []
            for x in ids:
                e = self.ents.get(x) if isinstance(x, str) else (x if isinstance(x, dict) else None)
                if not e:
                    continue
                links.append(self._hb_entity_link(e))
                names.append(str(self.loc(e, "name") or ""))
            return ", ".join(links), ", ".join(names), False
        # 单段字段名走实体的语种回退(hazards_en → hazards_<nk> → hazards_en),
        # 多段点路径按原样钻进子对象。
        raw = (self.loc(ent, self._base_key(col), None) if "." not in col
               else _resolve(ent, col))
        txt, isnum = self._hb_scalar(raw)
        if not txt:
            return "", "", isnum
        return esc(txt), txt, isnum

    # -------------------------------------------------- 模块:数据表
    def hb_tables(self, used):
        """按 config 声明出 1-3 张真数据表。返回 (html, [(锚点, 标题)])。"""
        spec = self.hb_spec()
        t = self.t
        out, toc = [], []
        for tb in spec.get("tables") or []:
            typ = tb.get("type")
            rows_src = [e for e in self.ents.values() if e.get("type") == typ]
            if len(rows_src) < 3:
                continue                      # 撑不住三行的表不出
            sort = tb.get("sort")
            if sort:
                def key(e, s=sort):
                    v = _resolve(e, s)
                    if isinstance(v, bool):
                        return (1, 0, "" if v else "z")
                    if isinstance(v, (int, float)):
                        return (0, v, "")
                    return (2, 0, str(v or ""))
                rows_src.sort(key=key)
            total = len(rows_src)
            cap = int(tb.get("max") or total)
            rows_use = rows_src[:cap]
            cols = [c for c in (tb.get("cols") or [])
                    if c == "@name" or any(not _empty(self._hb_raw(e, c)) for e in rows_use)]
            # 失败关闭:某一列里出现「指向同一条实体另一个字段名」的内部交叉引用
            # (例:"…disputed figure, see wish_fountain_capacity_dispute"),
            # 那是数据管线自用的记号、没有任何页面把它印给读者看 —— 整列不出,
            # 该字段的完整说法仍在该条目自己的页面上(名字那一列就链着)。
            dropped = []
            keep = []
            for c in cols:
                leak = ""
                for e in rows_use:
                    txt = self._hb_cell(e, c)[1]
                    for tok in FIELD_TOKEN_RE.findall(txt):
                        if tok in e:
                            leak = tok
                            break
                    if leak:
                        break
                (dropped if leak else keep).append((c, leak))
            if dropped:
                self.hb_warn(f"hub_body[{typ}]: 列 {[c for c, _ in dropped]} 含内部字段交叉引用"
                             f"({dropped[0][1]}),整列不渲染")
            cols = [c for c, _ in keep]
            if len(cols) < 2:
                continue                      # 只剩一列就不是表
            head = [self._hb_head_key(c) for c in cols]
            cells, numeric = [], [True] * len(cols)
            for e in rows_use:
                row = []
                for k, c in enumerate(cols):
                    html, txt, isnum = self._hb_cell(e, c)
                    nc = self._hb_unverified(e, c)
                    if not txt:
                        # 空格只写 em dash;该字段被这条实体自己标为未核实时写 nc_label。
                        # 空格/未核实不参与"这一列是不是数字列"的判断(与 native._table 同口径),
                        # 否则一条缺值就把整列的右对齐 + tabular-nums 弄丢。
                        html = (f'<span class="hb-nc">{esc(t["nc_label"])}</span>' if nc else DASH)
                    else:
                        if nc:
                            html += f' <span class="hb-nc">{esc(t["nc_label"])}</span>'
                            numeric[k] = False
                        elif not mdlite.is_numeric_cell(txt):
                            numeric[k] = False
                    row.append(html)
                cells.append(row)
            label = t[f"tbl_{typ}"]
            hid = mdlite.slugify(label, used)
            cl = [' class="num"' if n else "" for n in numeric]
            thead = "".join(f"<th{cl[k]}>{esc(h)}</th>" for k, h in enumerate(head))
            tbody = "".join("<tr>" + "".join(f"<td{cl[k]}>{c}</td>" for k, c in enumerate(r))
                            + "</tr>" for r in cells)
            # 来源:取本表用到的这些行自己记的 source_url / source_urls。
            # 站内自述(总站域名 / 该游戏子站域名 / 路径落在 /<game>/ 下)不算外部来源。
            selfhosts, gslug = self.hb_self_hosts(), self.hb_gslug()
            hosts = []
            for e in rows_use:
                for u in (e.get("source_urls") or ([e["source_url"]] if e.get("source_url") else [])):
                    h = _host(u)
                    if not h or h in selfhosts:
                        continue
                    path = "/" + (u.split("//", 1)[-1].split("/", 1) + [""])[1]
                    if gslug and path.startswith(f"/{gslug}/"):
                        continue
                    if h not in hosts:
                        hosts.append(h)
            src = (t["tbl_src_one"].format(host=hosts[0]) if len(hosts) == 1
                   else t["tbl_src_many"])
            foot = [f'<span class="hb-shown">{esc(t["tbl_shown"].format(n=len(rows_use), total=total))}</span>']
            if src:
                foot.append(f"<span>{esc(src)}</span>")
            more = self.route_slug(tb.get("all") or "") if tb.get("all") else ""
            more_html = (f'<div class="hb-more"><a href="{esc(more)}">'
                         f'{esc(t["tbl_more"].format(n=total, label=label.lower()))}{NBSP}&rarr;</a></div>'
                         if more else "")
            # --c = 列数(数据),CSS 拿它算表格最小宽度:列多就横滑,不靠挤窄单元格换行拉高
            out.append(f'<h3 id="{hid}">{esc(label)}</h3>'
                       f'<figure class="hb-fig">'
                       f'<div class="table-scroll" role="region" tabindex="0"'
                       f' aria-label="{esc(label)}{esc(t["sep"])}{esc(t["table_label"])}">'
                       f'<table style="--c:{len(cols)}"><thead><tr>{thead}</tr></thead>'
                       f"<tbody>{tbody}</tbody></table></div>"
                       f'<figcaption class="hb-src">{esc(t["sep"]).join(foot)}</figcaption>'
                       f"</figure>{more_html}")
            toc.append((hid, label))
        if not out:
            return "", []
        hid = mdlite.slugify(t["hub_data_heading"], used)
        return (f'<section class="hb hb-band" data-hb="tables">'
                f'<h2 id="{hid}">{esc(t["hub_data_heading"])}</h2>'
                f'<p class="hb-sub">{esc(t["hub_data_sub"])}</p>' + "".join(out) + "</section>",
                [(hid, t["hub_data_heading"])] + toc)

    # -------------------------------------------------- 模块:栏目磁贴(缩略图 + 页数徽章)
    def hb_tiles(self, used):
        rows = [r for r in self.hb_sections() if r[1]]
        if len(rows) < 2:
            return "", []
        t = self.t
        items = []
        for label, route, count, im in rows:
            badge = (f'<span class="hb-badge" aria-hidden="true">{count}</span>' if count else "")
            thumb = (f'<a class="tile-img" href="{esc(route)}" tabindex="-1" aria-hidden="true">'
                     f"{self.hb_img(im)}</a>" if im else "")
            items.append(
                f'<li class="tile">{thumb}{badge}<div class="card-b">'
                f'<h3 class="card-t"><a href="{esc(route)}">{esc(label)}</a></h3>'
                f'<p class="count">{esc(t["article_count"].format(n=count))}</p></div></li>')
        hid = mdlite.slugify(t["hub_sections_heading"], used)
        return (f'<section class="hb" data-hb="tiles">'
                f'<h2 id="{hid}">{esc(t["hub_sections_heading"])}</h2>'
                f'<ul class="tiles hb-tiles">{"".join(items)}</ul></section>',
                [(hid, t["hub_sections_heading"])])

    # -------------------------------------------------- 模块:精选卡片(缩略图 + 栏目 + 复核日)
    def hb_cards(self, used):
        rows = self.hb_featured(int(self.hb_spec().get("picks") or 6))
        if len(rows) < 3:
            return "", []
        t = self.t
        items = []
        for sec, title, route, date, im in rows:
            thumb = (f'<a class="rc-shot" href="{esc(route)}" tabindex="-1" aria-hidden="true">'
                     f"{self.hb_img(im, 'thumb')}</a>" if im else "")
            meta = []
            if sec:
                meta.append(f'<span class="rc-g">{esc(sec)}</span>')
            items.append(
                f'<li class="rcard">{thumb}<div class="rc-b">{"".join(meta)}'
                f'<h3><a href="{esc(route)}">{esc(title)}</a></h3>'
                + (f'<div class="rc-d"><time datetime="{esc(date)}">'
                   f'{esc(t["reviewed_on"].format(d=date))}</time></div>' if date else "")
                + "</div></li>")
        hid = mdlite.slugify(t["hub_picks_heading"], used)
        return (f'<section class="hb hb-band" data-hb="cards">'
                f'<h2 id="{hid}">{esc(t["hub_picks_heading"])}</h2>'
                f'<ul class="rcards hb-cards">{"".join(items)}</ul></section>',
                [(hid, t["hub_picks_heading"])])

    # -------------------------------------------------- 模块:统计胶囊
    def hb_pills(self):
        t, c = self.t, self.hb_counts()
        bits = []
        for key, single, plural in (("pages", "stat_guides", "stat_guides"),
                                    ("sections", "stat_sections", "stat_sections"),
                                    ("entities", "stat_entries", "stat_entries"),
                                    ("tools", "stat_tool", "stat_tools"),
                                    ("langs", "stat_languages", "stat_languages")):
            n = c.get(key) or 0
            if key == "langs" and n < 2:
                continue
            if not n:
                continue
            bits.append(f'<li><b>{n}</b>{NBSP}{esc(t[plural if n > 1 else single])}</li>')
        return f'<ul class="hb hb-pills" data-hb="pills">{"".join(bits)}</ul>' if bits else ""

    # -------------------------------------------------- 模块:范围提示框(逐字引用本站页面)
    def hb_note(self):
        q = self.hb_quote()
        if not q:
            return ""
        title, text, route, page_title = q
        link = (f'<div class="hb-note-s"><a href="{esc(route)}">{esc(page_title)}{NBSP}&rarr;</a></div>'
                if route and page_title else "")
        return (f'<aside class="hb hb-note" data-hb="note">'
                f'<p class="hb-note-t">{esc(title)}</p><p>{esc(text)}</p>{link}</aside>')

    # -------------------------------------------------- 模块:要点框(数字全部来自实际统计)
    def hb_keypoints(self):
        t, c = self.t, self.hb_counts()
        li = []
        if c.get("pages") and c.get("sections"):
            li.append(t["kp_pages"].format(n=c["pages"], m=c["sections"]))
        if c.get("entities"):
            li.append(t["kp_entities"].format(n=c["entities"]))
        if c.get("tools"):
            n = c["tools"]
            li.append(t["kp_tools"].format(n=n, label=t["stat_tool" if n == 1 else "stat_tools"]))
        if c.get("updated"):
            li.append(t["kp_updated"].format(d=c["updated"]))
        if c.get("langs", 0) > 1:
            li.append(t["kp_langs"].format(n=c["langs"]))
        li = li[:4]
        if len(li) < 3:
            return ""
        return (f'<section class="hb kp" data-hb="keypoints">'
                f'<p class="kp-t">{esc(t["key_points"])}</p><ul>'
                + "".join(f"<li>{esc(x)}</li>" for x in li) + "</ul></section>")

    # -------------------------------------------------- 模块:工具磁贴
    def hb_tool_tiles(self, used):
        rows = self.hb_tools()
        if not rows:
            return "", []
        t = self.t
        items = []
        for title, route, desc, im in rows:
            thumb = (f'<a class="tc-shot" href="{esc(route)}" tabindex="-1" aria-hidden="true">'
                     f"{self.hb_img(im, 'thumb')}</a>" if im else "")
            items.append(f'<li class="tcard">{thumb}<div class="tc-b">'
                         f'<h3><a href="{esc(route)}">{esc(title)}</a></h3>'
                         + (f'<div class="tc-d">{esc(desc)}</div>' if desc else "") + "</div></li>")
        hid = mdlite.slugify(t["hub_tools_heading_game"], used)
        return (f'<section class="hb hb-band" data-hb="tools">'
                f'<h2 id="{hid}">{esc(t["hub_tools_heading_game"])}</h2>'
                f'<ul class="tcards hb-tools">{"".join(items)}</ul></section>',
                [(hid, t["hub_tools_heading"])])

    # -------------------------------------------------- 模块:单行时间线(自记复核日)
    _hb_used = None

    def hb_timeline(self, used=None):
        self._hb_used = used if used is not None else set()
        rows = self.hb_recent(5)
        rows = [r for r in rows if r[2]]
        if len(rows) < 3:
            return ""
        t = self.t
        items = "".join(
            f'<li><time datetime="{esc(d)}">{esc(d)}</time>'
            f'<a href="{esc(r)}">{esc(ti)}</a></li>' for ti, r, d in rows)
        hid = mdlite.slugify(t["hub_tl_heading"], self._hb_used)
        return (f'<section class="hb" data-hb="timeline">'
                f'<h3 class="hb-tl-t" id="{hid}">{esc(t["hub_tl_heading"])}</h3>'
                f'<ol class="hb-tl">{items}</ol></section>')

    # -------------------------------------------------- 组装
    def hb_render(self, names, used):
        """按名字渲染一组模块,返回 (html, toc 项)。未知名字直接报错(配置写错要立刻炸)。"""
        html, toc = [], []
        for n in names:
            if n == "note":
                html.append(self.hb_note())
            elif n == "pills":
                html.append(self.hb_pills())
            elif n == "keypoints":
                html.append(self.hb_keypoints())
            elif n == "timeline":
                html.append(self.hb_timeline(used))
            elif n == "tiles":
                h, tc = self.hb_tiles(used)
                html.append(h)
                toc += tc
            elif n == "cards":
                h, tc = self.hb_cards(used)
                html.append(h)
                toc += tc
            elif n == "tables":
                h, tc = self.hb_tables(used)
                html.append(h)
                toc += tc
            elif n == "tools":
                h, tc = self.hb_tool_tiles(used)
                html.append(h)
                toc += tc
            else:
                raise KeyError(f"hub_body.slots: 未知模块名 {n!r}")
        return "".join(x for x in html if x), toc
