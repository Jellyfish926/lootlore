"""mdlite —— 仅标准库的最小 Markdown 渲染器(框架层)。

仓库约定零 pip 依赖(Vercel 不跑构建命令、两条 workflow 都不装包),所以不用 `markdown` 库。
支持:ATX 标题、段落、无序/有序列表(单层)、GFM 表格、引用、围栏代码、分隔线、
行内链接 / **粗体** / *斜体* / `代码`、frontmatter(key: JSON 值 或 裸字符串)。

两步走:parse() 出块列表(dict),调用方可以增删块(剥离 H1、替换卡片块等),
再 render() 出 HTML。行内链接的输出交给回调 link_cb(href, inner_html) -> html,
这样站内/站外/草稿链接的处理全留在调用方,本模块不认识任何站点。
"""
import html as _html
import json
import re

_CJK = r"　-〿㐀-鿿豈-﫿＀-￯"
_CJK_END = re.compile(f"[{_CJK}]$")
_CJK_START = re.compile(f"^[{_CJK}]")

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.S)


def esc(s: str) -> str:
    return _html.escape(s, quote=True)


# ---------------------------------------------------------------- frontmatter
def split_frontmatter(text: str):
    """返回 (dict, body)。值优先按 JSON 解析(内容包的 frontmatter 就是 JSON 值),
    其次 true/false/空,最后按裸字符串(去掉成对引号)。"""
    text = text.lstrip("﻿")
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if not km:
            continue
        k, raw = km.group(1), km.group(2).strip()
        if raw == "":
            v = ""
        elif raw in ("true", "false"):
            v = raw == "true"
        else:
            try:
                v = json.loads(raw)
            except ValueError:
                v = raw[1:-1] if len(raw) > 1 and raw[0] == raw[-1] and raw[0] in "'\"" else raw
        fm[k] = v
    return fm, m.group(2)


# ---------------------------------------------------------------- inline
_LINK = r"\[((?:[^\[\]]|\[[^\[\]]*\])+)\]\(((?:[^()\s]|\([^()\s]*\))+)(?:\s+\"([^\"]*)\")?\)"
_INLINE = re.compile(
    r"`([^`]+)`"                       # 1 code
    + r"|" + _LINK                     # 2 text 3 href 4 title
    + r"|\*\*(.+?)\*\*"                # 5 strong
    + r"|(?<![\w*])\*(?!\s)([^*]+?)(?<!\s)\*(?![\w*])"  # 6 em
)


def inline(s: str, link_cb=None) -> str:
    out, pos = [], 0
    for m in _INLINE.finditer(s):
        out.append(esc(s[pos:m.start()]))
        if m.group(1) is not None:
            out.append(f"<code>{esc(m.group(1))}</code>")
        elif m.group(2) is not None:
            inner = inline(m.group(2), None)
            href = m.group(3)
            out.append(link_cb(href, inner) if link_cb else f'<a href="{esc(href)}">{inner}</a>')
        elif m.group(5) is not None:
            out.append(f"<strong>{inline(m.group(5), link_cb)}</strong>")
        else:
            out.append(f"<em>{inline(m.group(6), link_cb)}</em>")
        pos = m.end()
    out.append(esc(s[pos:]))
    return "".join(out)


def plain(s: str) -> str:
    """行内 Markdown → 纯文本(标题锚点、目录、摘要用)。"""
    s = re.sub(_LINK, lambda m: m.group(1), s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)([^*]+?)(?<!\s)\*(?![\w*])", r"\1", s)
    return s.strip()


def links_in(s: str):
    """[(text, href)] —— 行内文本里的全部链接。"""
    return [(m.group(1), m.group(2)) for m in re.finditer(_LINK, s)]


def sole_link(s: str):
    """整段文本恰好是一个链接时返回 (text, href),否则 None。"""
    m = re.fullmatch(r"\s*" + _LINK + r"\s*", s)
    return (m.group(1), m.group(2)) if m else None


# ---------------------------------------------------------------- blocks
_H = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_UL = re.compile(r"^\s{0,3}[-*+]\s+(.*)$")
_OL = re.compile(r"^\s{0,3}\d+[.)]\s+(.*)$")
_HR = re.compile(r"^\s{0,3}([-*_])(\s*\1){2,}\s*$")
_FENCE = re.compile(r"^\s{0,3}(```|~~~)\s*([\w+-]*)\s*$")
_TSEP = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")


def _cells(line: str):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    parts = re.split(r"(?<!\\)\|", line)
    return [p.strip().replace("\\|", "|") for p in parts]


def _join(a: str, b: str) -> str:
    if not a:
        return b
    if _CJK_END.search(a) and _CJK_START.search(b):
        return a + b
    return a + " " + b


def _starts_block(line: str, nxt: str) -> bool:
    return bool(
        _H.match(line) or _UL.match(line) or _OL.match(line) or _HR.match(line)
        or _FENCE.match(line) or line.lstrip().startswith(">")
        or (line.lstrip().startswith("|") and _TSEP.match(nxt or ""))
    )


def parse(md: str):
    lines = md.replace("\r\n", "\n").split("\n")
    blocks, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        nxt = lines[i + 1] if i + 1 < n else ""
        if not line.strip():
            i += 1
            continue
        fm = _FENCE.match(line)
        if fm:
            fence, lang, buf = fm.group(1), fm.group(2), []
            i += 1
            while i < n and not lines[i].strip().startswith(fence):
                buf.append(lines[i])
                i += 1
            blocks.append({"t": "code", "lang": lang, "text": "\n".join(buf)})
            i += 1
            continue
        hm = _H.match(line)
        if hm:
            blocks.append({"t": "h", "level": len(hm.group(1)), "text": hm.group(2)})
            i += 1
            continue
        if _HR.match(line):
            blocks.append({"t": "hr"})
            i += 1
            continue
        if line.lstrip().startswith("|") and _TSEP.match(nxt):
            head = _cells(line)
            aligns = []
            for c in _cells(nxt):
                c = c.strip()
                aligns.append("center" if c.startswith(":") and c.endswith(":") else
                              "right" if c.endswith(":") else "left" if c.startswith(":") else "")
            rows = []
            i += 2
            while i < n and lines[i].strip().startswith("|"):
                r = _cells(lines[i])
                r = (r + [""] * len(head))[: len(head)]
                rows.append(r)
                i += 1
            blocks.append({"t": "table", "head": head, "align": aligns, "rows": rows})
            continue
        if line.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            blocks.append({"t": "quote", "blocks": parse("\n".join(buf))})
            continue
        lm = _UL.match(line) or _OL.match(line)
        if lm:
            kind = "ul" if _UL.match(line) else "ol"
            rx = _UL if kind == "ul" else _OL
            items = []
            while i < n:
                cur = lines[i]
                m2 = rx.match(cur)
                if m2:
                    items.append(m2.group(1).strip())
                    i += 1
                    continue
                if cur.strip() and cur.startswith((" ", "\t")) and items:  # 续行
                    items[-1] = _join(items[-1], cur.strip())
                    i += 1
                    continue
                break
            blocks.append({"t": kind, "items": items})
            continue
        buf = line.strip()
        i += 1
        while i < n and lines[i].strip() and not _starts_block(lines[i], lines[i + 1] if i + 1 < n else ""):
            buf = _join(buf, lines[i].strip())
            i += 1
        blocks.append({"t": "p", "text": buf})
    return blocks


def slugify(text: str, used: set) -> str:
    base = re.sub(r"[^\w㐀-鿿-]+", "-", plain(text).lower()).strip("-") or "section"
    s, k = base, 2
    while s in used:
        s, k = f"{base}-{k}", k + 1
    used.add(s)
    return s


def render(blocks, link_cb=None, table_label="table") -> str:
    out = []
    for b in blocks:
        t = b["t"]
        if t == "h":
            idattr = f' id="{esc(b["id"])}"' if b.get("id") else ""
            out.append(f'<h{b["level"]}{idattr}>{inline(b["text"], link_cb)}</h{b["level"]}>')
        elif t == "p":
            out.append(f"<p>{inline(b['text'], link_cb)}</p>")
        elif t in ("ul", "ol"):
            li = "".join(f"<li>{inline(x, link_cb)}</li>" for x in b["items"])
            out.append(f"<{t}>{li}</{t}>")
        elif t == "table":
            def cell(tag, txt, al):
                st = f' style="text-align:{al}"' if al else ""
                return f"<{tag}{st}>{inline(txt, link_cb)}</{tag}>"
            al = b["align"] + [""] * len(b["head"])
            thead = "".join(cell("th", h, al[k]) for k, h in enumerate(b["head"]))
            tbody = "".join(
                "<tr>" + "".join(cell("td", c, al[k]) for k, c in enumerate(r)) + "</tr>" for r in b["rows"]
            )
            out.append(
                f'<div class="table-scroll" role="region" tabindex="0" aria-label="{esc(table_label)}">'
                f"<table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table></div>"
            )
        elif t == "quote":
            out.append(f"<blockquote>{render(b['blocks'], link_cb, table_label)}</blockquote>")
        elif t == "code":
            cls = f' class="language-{esc(b["lang"])}"' if b["lang"] else ""
            out.append(f"<pre><code{cls}>{esc(b['text'])}</code></pre>")
        elif t == "hr":
            out.append("<hr>")
        elif t == "html":
            out.append(b["html"])
    return "\n".join(out)
