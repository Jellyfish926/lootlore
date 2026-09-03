#!/usr/bin/env python3
"""check_config —— Next.js + MDX 站的「三处一致」检查(跑在源码上)。

三处 = config/site.json 的 nav[].slug ↔ content/<locale>/<slug>/ 目录 ↔ 每个 locale 目录的栏目集合。
  E NAV_NO_DIR      nav 登记了栏目,content/<default>/ 下没有目录
  E EMPTY_CATEGORY  栏目目录下 0 篇 .mdx(空栏目不上导航 —— 空列表页是 thin content 且会被收录)
  E BAD_FRONTMATTER mdx 缺 title / description
  E IMG_KEY         正文引用 ![](key) 但 config/images.json 没有这个 key
  W DIR_NO_NAV      content 里有栏目目录但 nav 没登记(孤儿栏目,不会进导航)
  W LOCALE_DIFF     非默认 locale 的栏目集合与默认不同
  W TITLE_LEN       title 不在 40-60 字符 / description 不在 140-160(seo-jianzhan 硬规格)
  W ENV_GITIGNORE   存在 .env* 但 .gitignore 没排除

用法: python3 check_config.py <site_root> [--default en] [--json]
"""
import argparse, glob, json, os, re, sys


def frontmatter(path):
    s = open(path, encoding="utf-8", errors="replace").read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", s, re.S)
    if not m: return {}, s
    fm = {}
    for line in m.group(1).splitlines():
        k = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if k: fm[k.group(1)] = k.group(2).strip().strip('"').strip("'")
    return fm, m.group(2)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("root"); ap.add_argument("--default", default="en"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args(); root = os.path.abspath(a.root)
    cfg = os.path.join(root, "config", "site.json"); content = os.path.join(root, "content")
    if not os.path.isfile(cfg) or not os.path.isdir(content):
        print("不是 Next+MDX 布局(无 config/site.json 或 content/),跳过 check_config"); sys.exit(0)
    site = json.load(open(cfg, encoding="utf-8"))
    nav = [n["slug"] for n in site.get("nav", []) if isinstance(n, dict) and n.get("slug")]
    images = {}
    ip = os.path.join(root, "config", "images.json")
    if os.path.isfile(ip):
        try: images = json.load(open(ip, encoding="utf-8"))
        except Exception: pass
    if isinstance(images, dict) and isinstance(images.get("images"), dict): images = images["images"]
    img_keys = {k for k in images.keys() if not k.startswith("_")} if isinstance(images, dict) else set()
    E, W = [], []
    locales = sorted(d for d in os.listdir(content) if os.path.isdir(os.path.join(content, d)))
    if a.default not in locales: E.append(("NO_DEFAULT_LOCALE", content, f"缺 content/{a.default}/"));
    cats = {}
    for loc in locales:
        base = os.path.join(content, loc)
        cats[loc] = {d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)) and d not in ("site",)}
    dcats = cats.get(a.default, set())
    for s in nav:
        if s not in dcats: E.append(("NAV_NO_DIR", s, f"nav 有 {s},content/{a.default}/{s}/ 不存在"))
        elif not glob.glob(os.path.join(content, a.default, s, "*.mdx")): E.append(("EMPTY_CATEGORY", s, "0 篇 mdx —— 空栏目不上导航"))
    for d in sorted(dcats - set(nav)): W.append(("DIR_NO_NAV", d, "content 里有目录但 nav 没登记"))
    for loc in locales:
        if loc != a.default and cats[loc] != dcats: W.append(("LOCALE_DIFF", loc, f"栏目集合 {sorted(cats[loc])} ≠ 默认 {sorted(dcats)}"))
    for path in glob.glob(os.path.join(content, "**", "*.mdx"), recursive=True):
        rel = os.path.relpath(path, root)
        fm, body = frontmatter(path)
        if not fm.get("title") or not fm.get("description"): E.append(("BAD_FRONTMATTER", rel, "缺 title / description")); continue
        if not 40 <= len(fm["title"]) <= 60: W.append(("TITLE_LEN", rel, f"title {len(fm['title'])} 字符(规格 40-60)"))
        if not 140 <= len(fm["description"]) <= 160: W.append(("TITLE_LEN", rel, f"description {len(fm['description'])} 字符(规格 140-160)"))
        for key in re.findall(r"!\[[^\]]*\]\(([A-Za-z0-9_-]+)\)", body):
            if img_keys and key not in img_keys: E.append(("IMG_KEY", rel, f"images.json 无 key「{key}」"))
    gi = open(os.path.join(root, ".gitignore"), encoding="utf-8").read() if os.path.isfile(os.path.join(root, ".gitignore")) else ""
    if glob.glob(os.path.join(root, ".env*")) and ".env" not in gi: W.append(("ENV_GITIGNORE", ".gitignore", "存在 .env* 但未排除"))
    if a.json: print(json.dumps({"nav": nav, "locales": locales, "errors": E, "warnings": W}, ensure_ascii=False, indent=1))
    else:
        print(f"check_config: nav {nav} · locales {locales} · {len(E)} 阻塞 · {len(W)} 警告")
        for k, r, m in E: print(f"  ❌ {k:16} {r}  {m}")
        for k, r, m in W: print(f"  ⚠  {k:16} {r}  {m}")
    sys.exit(1 if E else 0)


if __name__ == "__main__":
    main()
