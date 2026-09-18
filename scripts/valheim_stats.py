#!/usr/bin/env python3
"""valheim_stats —— /valheim/ 内容密度统计(只统计,不改内容)。

对每一页输出:语言 / 词数(拉丁词数;中文页按汉字数)/ 表格数 / 图片数 / 有无信息框 / 有无 tldr。
数据取自构建产物 out/valheim/**(表格、图片、信息框以实际渲染结果为准)与
content/valheim/<lang>/*.md 的 frontmatter(tldr / entity / entities)。

用法:
  python3 scripts/valheim_stats.py                 # 表格
  python3 scripts/valheim_stats.py --json          # JSON
  python3 scripts/valheim_stats.py --out out --content content/valheim
"""
import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from hub import mdlite  # noqa: E402

CJK = re.compile(r"[㐀-鿿豈-﫿]")


class P(HTMLParser):
    """只数正文区(.doc 里的 .prose 与要点框);导航、页头页脚、右栏信息框不计入词数。"""

    def __init__(self):
        super().__init__()
        self.text, self._skip, self.tables, self.imgs, self.rail = [], 0, 0, 0, 0
        self.lang = None
        self._in_doc = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "aside" and "rail" in cls:
            self.rail += 1
        if tag in ("script", "style", "nav", "header", "footer", "aside"):
            self._skip += 1
            return
        if self._skip:
            return
        if tag == "div" and "doc" in cls.split():
            self._in_doc += 1
        if self._in_doc:
            if tag == "table":
                self.tables += 1
            # 正文配图只数 figure(封面 / 正文 figure);卡片缩略图(.thumb)不算
            if tag == "img" and "thumb" not in cls.split():
                self.imgs += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "header", "footer", "aside") and self._skip:
            self._skip -= 1

    def handle_data(self, d):
        if not self._skip and self._in_doc:
            self.text.append(d)


def words(text, lang):
    """中文/日文/韩文页按汉字数,其余按拉丁词数 —— 口径由页面语种决定,不看正文里混排的字符。"""
    if (lang or "").split("-")[0] in ("zh", "ja", "ko"):
        return len(CJK.findall(text))
    return len(re.findall(r"[A-Za-z0-9'’-]+", text))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="out")
    ap.add_argument("--content", default="content/valheim")
    ap.add_argument("--slug", default="valheim")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    out = ROOT / a.out / a.slug
    content = ROOT / a.content
    cfg = json.loads((ROOT / "config" / "hub.json").read_text(encoding="utf-8"))
    game = next(g for g in cfg["games"] if g["slug"] == a.slug)
    specs = game["native"]["langs"]

    rows = []
    for spec in specs:
        d = content / spec["dir"]
        for md in sorted(d.glob("*.md")):
            if md.name.startswith("_"):
                continue
            fm, _body = mdlite.split_frontmatter(md.read_text(encoding="utf-8"))
            slug = fm.get("slug") or md.stem
            sub = "" if fm.get("type") == "home" else slug
            html_path = out / spec["prefix"] / sub / "index.html"
            if not html_path.is_file():
                continue
            p = P()
            p.feed(html_path.read_text(encoding="utf-8"))
            body = " ".join(p.text)
            rows.append({
                "lang": spec["code"],
                "slug": slug,
                "type": fm.get("type") or "article",
                "url": "/" + str(html_path.relative_to(ROOT / a.out).parent).replace("\\", "/") + "/",
                "words": words(body, spec["code"]),
                "tables": p.tables,
                "images": p.imgs,
                "infobox": bool(p.rail),
                "tldr": bool(fm.get("tldr")),
                "entity": bool(fm.get("entity") or fm.get("entities")),
            })

    if a.json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return

    hdr = f'{"lang":<6}{"slug":<20}{"type":<9}{"words":>7}{"tbl":>5}{"img":>5}{"info":>6}{"tldr":>6}'
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(f'{r["lang"]:<6}{r["slug"]:<20}{r["type"]:<9}{r["words"]:>7}{r["tables"]:>5}'
              f'{r["images"]:>5}{"Y" if r["infobox"] else "-":>6}{"Y" if r["tldr"] else "-":>6}')
    print("-" * len(hdr))
    for spec in specs:
        g = [r for r in rows if r["lang"] == spec["code"]]
        if not g:
            continue
        print(f'{spec["code"]}: {len(g)} 页 · 有信息框 {sum(1 for r in g if r["infobox"])} 页 · '
              f'有 tldr {sum(1 for r in g if r["tldr"])} 页 · 表格合计 {sum(r["tables"] for r in g)} · '
              f'图片合计 {sum(r["images"] for r in g)} · '
              f'词数 min {min(r["words"] for r in g)} / 中位 '
              f'{sorted(r["words"] for r in g)[len(g)//2]} / max {max(r["words"] for r in g)}')


if __name__ == "__main__":
    main()
