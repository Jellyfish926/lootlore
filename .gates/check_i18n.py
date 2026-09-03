#!/usr/bin/env python3
"""check_i18n —— 多语言站的翻译覆盖率与残页检查(跑在 HTML 产物上)。

规矩(seo-jianzhan 多语言纪律):没翻的页可以不生成(详情页回退主语种),但**生成了就不能是残页或占位页**。
  E STUB_PAGE     小语种页正文字数 < 主语种同页的 40%(残缺翻译 / 模板占位)
  E PLACEHOLDER   小语种页含占位语
  E LANG_ATTR     <html lang> 与目录语种不一致
  W MISSING       主语种有、该语种没有的页(允许,但列出来;切换器不应显示它)
  W EXTRA         该语种有、主语种没有的页(通常是遗留)
  W NO_HREFLANG   小语种页缺 hreflang alternate

用法: python3 check_i18n.py <html_dir> --default en --locales de,es,fr,it,ja [--min-ratio 0.4] [--json]
      --strict  把 MISSING 也当阻塞(想让「语种必须完整」当门禁时用)
"""
import argparse, json, os, re, sys
from html.parser import HTMLParser

PLACEHOLDER_CS = re.compile(r"\bTBD\b|\bTODO\b")
PLACEHOLDER = re.compile(r"coming soon|being verified|will be verified|待补充|稍后补|即将上线|lorem ipsum|English fallback", re.I)
CJK = re.compile(r"[぀-ヿ㐀-鿿]")


class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.lang = None; self.text = []; self._skip = 0; self.hreflang = 0; self.in_head = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = (a.get("lang") or "").split("-")[0].lower()
        if tag == "head": self.in_head = True
        if tag == "link" and a.get("hreflang"): self.hreflang += 1
        if tag in ("script", "style", "nav", "header", "footer", "aside"): self._skip += 1
    def handle_endtag(self, tag):
        if tag == "head": self.in_head = False
        if tag in ("script", "style", "nav", "header", "footer", "aside") and self._skip: self._skip -= 1
    def handle_data(self, d):
        if not self._skip and not self.in_head: self.text.append(d)


def words(text, lang):
    if lang in ("ja", "zh", "ko") or CJK.search(text): return len(CJK.findall(text)) + len(re.findall(r"[A-Za-z0-9]+", text))
    return len(re.findall(r"[A-Za-z0-9'’-]+", text))


def pages(root, loc):
    base = os.path.join(root, loc)
    out = {}
    if not os.path.isdir(base): return out
    for dp, _, fs in os.walk(base):
        for f in fs:
            if f.endswith(".html"):
                rel = os.path.relpath(os.path.join(dp, f), base).replace(os.sep, "/")
                rel = rel[:-len("index.html")] if rel.endswith("index.html") else rel[:-5]
                out[rel.strip("/") or "index"] = os.path.join(dp, f)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root"); ap.add_argument("--default", default="en"); ap.add_argument("--locales", required=True)
    ap.add_argument("--min-ratio", type=float, default=0.4); ap.add_argument("--strict", action="store_true"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    base = pages(root, a.default)
    if not base:
        print(f"主语种目录 {a.default}/ 下没有 html —— 单语种站不需要这道门禁,跳过"); sys.exit(0)
    base_words = {}
    for k, path in base.items():
        p = P(); p.feed(open(path, encoding="utf-8", errors="replace").read()); base_words[k] = words(" ".join(p.text), a.default)
    E, W, stats = [], [], {}
    for loc in [x for x in a.locales.split(",") if x and x != a.default]:
        pg = pages(root, loc)
        missing = sorted(set(base) - set(pg)); extra = sorted(set(pg) - set(base))
        stubs = 0
        for k in missing: W.append(("MISSING", f"/{loc}/{k}", "主语种有此页,该语种未生成"))
        for k in extra: W.append(("EXTRA", f"/{loc}/{k}", "主语种没有此页"))
        for k, path in pg.items():
            p = P(); p.feed(open(path, encoding="utf-8", errors="replace").read())
            txt = " ".join(p.text); n = words(txt, loc)
            if k in base_words and base_words[k] > 150 and n < base_words[k] * a.min_ratio:
                E.append(("STUB_PAGE", f"/{loc}/{k}", f"{n} 词 vs 主语种 {base_words[k]}(<{int(a.min_ratio*100)}%)")); stubs += 1
            m = PLACEHOLDER.search(txt) or PLACEHOLDER_CS.search(txt)
            if m: E.append(("PLACEHOLDER", f"/{loc}/{k}", f"「{m.group(0)}」"))
            if p.lang and p.lang != loc: E.append(("LANG_ATTR", f"/{loc}/{k}", f"lang={p.lang}"))
            if p.hreflang == 0: W.append(("NO_HREFLANG", f"/{loc}/{k}", "无 hreflang alternate"))
        stats[loc] = {"pages": len(pg), "missing": len(missing), "extra": len(extra), "stubs": stubs, "coverage": round(len(pg) / max(len(base), 1), 2)}
    if a.strict:
        E += [w for w in W if w[0] == "MISSING"]; W = [w for w in W if w[0] != "MISSING"]
    if a.json:
        print(json.dumps({"default_pages": len(base), "locales": stats, "errors": E, "warnings": W}, ensure_ascii=False, indent=1))
    else:
        print(f"check_i18n: 主语种 {len(base)} 页 · " + " · ".join(f"{l}: {s['pages']}页/覆盖 {s['coverage']}/残页 {s['stubs']}" for l, s in stats.items()))
        for k, r, m in E: print(f"  ❌ {k:12} {r}  {m}")
        for k, r, m in W[:100]: print(f"  ⚠  {k:12} {r}  {m}")
        if len(W) > 100: print(f"  … 另 {len(W)-100} 条警告")
    sys.exit(1 if E else 0)


if __name__ == "__main__":
    main()
