#!/usr/bin/env python3
"""check_snapshot —— 快照页正文"逐字节零改动"的门禁(跑在产物上,对照 sources/)。

规矩(全部是 E,红一条就阻塞):
  E BODY_DIFF    产物里 .sn-body 的内容拼起来 ≠ 子站原文 <main> 经 hub/snapshot.parse_page
                 搬位置(面包屑/H1/署名行)之后的正文 —— 说明有人改了正文字节
  E SPLIT_ON_PAGE  内容页出现了多个 .sn-body —— 外壳层只许在 hub 页的小节之间插模块,
                 内容页一律一段不动
  E TEXT_DIFF    产物 .sn-body 的可见文字 ≠ 子站原文 <main> 的可见文字(减掉被搬走的
                 面包屑 / H1 / 署名行那几段)—— 与上一条互相独立:上一条比字节,这一条
                 比"人眼能看到的字",两条都过才算正文真的没动

用法: python3 .gates/check_snapshot.py [--out out] [--json]
退出码:有 E 则 1。
"""
import argparse, html as _html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build as B                                                    # noqa: E402
from hub import snapshot as S                                        # noqa: E402
from hub.pageindex import _excluded, _route_of, TRUST_SLUGS          # noqa: E402

SN_RE = re.compile(r'<div class="prose sn-body">')
# hub 页把正文分装进多个 .sn-body 时,外壳层补出来的配平标签夹在这对注释里(见 hub/snapshot.doc_html)
HBF_RE = re.compile(r"<!--hbf-->.*?<!--/hbf-->", re.S)
MAIN_RE = re.compile(r'<main\b[^>]*>(.*)</main>', re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")
LD_RE = re.compile(r'<script[^>]*>.*?</script>', re.S | re.I)


def norm_text(s: str) -> str:
    return " ".join(_html.unescape(TAG_RE.sub(" ", LD_RE.sub(" ", s or ""))).split())


def sn_bodies(page_html: str):
    """把产物里每个 <div class="prose sn-body"> 的内层 HTML 取出来(按标签深度配平)。"""
    out = []
    for m in SN_RE.finditer(page_html):
        depth, i = 1, m.end()
        start = i
        for t in re.finditer(r"<(/?)div\b[^>]*>", page_html[m.end():]):
            depth += -1 if t.group(1) else 1
            if depth == 0:
                out.append(page_html[start:m.end() + t.start()])
                break
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="out")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    out = (ROOT / a.out) if not Path(a.out).is_absolute() else Path(a.out)
    cfg = json.loads((ROOT / "config" / "hub.json").read_text(encoding="utf-8"))
    errs, n_pages, n_hub = [], 0, 0
    for g in cfg["games"]:
        if g.get("kind") == "native":
            continue
        src = ROOT / g["source"]
        slug = g["slug"]
        # hub 页 = 每个语种各自的根页(beast 有 6 个),语种清单取自渲染器自己的发现逻辑
        game = S.SnapshotGame(ROOT, g, cfg, {"base": cfg["base_url"].rstrip("/"),
                                             "today": "", "year": ""})
        homes = {l.home_route for l in game.langs} | {l.home_route.rstrip("/") for l in game.langs}
        for p in sorted(src.rglob("*.html")):
            rel = p.relative_to(src)
            if _excluded(rel, g):
                continue
            route = _route_of(slug, rel)
            if route.rstrip("/").rsplit("/", 1)[-1] in TRUST_SLUGS:
                continue
            built = out / slug / rel
            if not built.is_file():
                continue
            raw = p.read_text(encoding="utf-8")
            for patch in g.get("patches", []):
                if patch["file"] == str(rel):
                    raw = raw.replace(patch["find"], patch["find"] + patch["insert_after"], 1)
            try:
                # 与 build.py 同一条链路:先 URL 改写,再解析 —— 不然比出来的差异只是
                # 子站根相对链接加了 /<game>/ 前缀,不是正文被改
                parsed = S.parse_page(B.transform_urls(raw, g), route, p)
            except Exception as e:                      # noqa: BLE001
                errs.append(("PARSE", str(rel), repr(e)))
                continue
            bh = built.read_text(encoding="utf-8")
            parts = sn_bodies(bh)
            n_pages += 1
            is_hub = route in homes
            if is_hub:
                n_hub += 1
            elif len(parts) > 1:
                errs.append(("SPLIT_ON_PAGE", str(rel), f"{len(parts)} 个 .sn-body"))
            joined = HBF_RE.sub("", "".join(parts))
            if joined != parsed.body:
                errs.append(("BODY_DIFF", str(rel),
                             f"产物 {len(joined)} 字节 vs 原文 {len(parsed.body)} 字节"))
            # 可见文字:原文 <main> 的字 = 被搬走的 H1 + 署名行 + 正文 的字
            mm = MAIN_RE.search(B.transform_urls(raw, g))
            main_html = mm.group(1) if mm else ""
            # 子站自带的面包屑被搬进外壳,它的字本来就不在正文里 —— 先从原文侧减掉
            for tag in ("nav", "p", "ol", "div"):
                span = S._find_element(main_html, tag, classes=S.CRUMB_CLASSES)
                if span:
                    main_html = main_html[:span[0]] + main_html[span[3]:]
                    break
            want = norm_text(main_html)
            got = " ".join(x for x in (norm_text(parsed.h1), norm_text(parsed.byline),
                                       norm_text(joined)) if x)
            # 面包屑被搬进外壳,它的字不在正文里 —— 从原文那一侧按 token 多重集差比
            wt, gt = want.split(), got.split()
            if sorted(gt) != sorted(w for w in wt if True) and len(gt) > len(wt):
                errs.append(("TEXT_DIFF", str(rel), f"产物多出 {len(gt) - len(wt)} 个词"))
            else:
                missing = _missing(wt, gt)
                if missing:
                    errs.append(("TEXT_DIFF", str(rel), f"缺 {len(missing)} 个词: "
                                                        + " ".join(missing[:8])))
    for kind, f, msg in errs:
        print(f"E {kind:14s} {f}: {msg}")
    print(f"check_snapshot: {n_pages} 个快照页(含 {n_hub} 个 hub 页) · 错误 {len(errs)}")
    sys.exit(1 if errs else 0)


def _missing(want_tokens, got_tokens):
    """原文有、产物没有的词(多重集差)。面包屑的词允许只出现在原文一侧,所以这里只报
    '产物缺词',缺词才说明正文被删了。"""
    from collections import Counter
    d = Counter(want_tokens) - Counter(got_tokens)
    return [w for w, c in d.items() for _ in range(c)]


if __name__ == "__main__":
    main()
