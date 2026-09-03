#!/usr/bin/env python3
"""check_sitemap —— sitemap 与产物 / 线上的一致性。

离线(--out DIR):
  E LOC_NO_FILE   sitemap 里的 URL 在产物里没有对应文件
  E LOC_HOST      <loc> 的域名不是 --host(残留临时域名 vercel.app / 兄弟站域名 = 跨站污染)
  E SITEMAP_MISSING 产物里没有 sitemap.xml
  W PAGE_NOT_IN_SITEMAP  产物里有可索引页但 sitemap 没收(排除 404 / noindex / 信任页可选)
  W ROBOTS        robots.txt 缺 Sitemap 行,或带尾斜杠(会 308,Google 拒收)
线上(--live HOST):
  E LOC_STATUS    任一 <loc> 非 200(串行、10 并发以内)
  E SITEMAP_200   sitemap.xml 或 robots.txt 非 200

用法: python3 check_sitemap.py --out out/ --host example.com [--exclude 404,privacy-policy]
      python3 check_sitemap.py --live example.com
"""
import argparse, os, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (compatible; seo-gates/1.0)"


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20) as r: return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e: return e.code, ""
    except Exception as e: return 0, str(e)


def locs(xml): return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)


def main():
    ap = argparse.ArgumentParser(); g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--out"); g.add_argument("--live"); ap.add_argument("--host", default=""); ap.add_argument("--exclude", default="404,500")
    a = ap.parse_args(); E, W = [], []
    exclude = {x for x in a.exclude.split(",") if x}
    if a.out:
        root = os.path.abspath(a.out); sm = os.path.join(root, "sitemap.xml")
        if not os.path.isfile(sm): E.append(("SITEMAP_MISSING", "sitemap.xml", "产物里没有")); report(E, W); return
        xml = open(sm, encoding="utf-8").read()
        urls = locs(xml)
        # sitemap index → 展开
        for u in list(urls):
            if u.endswith(".xml"):
                sub = os.path.join(root, re.sub(r"^https?://[^/]+/", "", u))
                if os.path.isfile(sub): urls += locs(open(sub, encoding="utf-8").read())
        urls = [u for u in urls if not u.endswith(".xml")]
        listed = set()
        for u in urls:
            host = re.sub(r"^https?://", "", u).split("/")[0]
            if a.host and host != a.host and host != "www." + a.host: E.append(("LOC_HOST", u, f"域名不是 {a.host}"))
            p = re.sub(r"^https?://[^/]+/?", "", u).split("#")[0]; p = p.strip("/")
            cands = [os.path.join(root, p, "index.html"), os.path.join(root, p + ".html"), os.path.join(root, p)] if p else [os.path.join(root, "index.html")]
            if not any(os.path.isfile(c) for c in cands): E.append(("LOC_NO_FILE", u, "产物里无此页"))
            listed.add(p)
        for dp, _, fs in os.walk(root):
            if "/_next" in dp: continue
            for f in fs:
                if not f.endswith(".html"): continue
                rel = os.path.relpath(os.path.join(dp, f), root).replace(os.sep, "/")
                p = (rel[:-len("index.html")] if rel.endswith("index.html") else rel[:-5]).strip("/")
                if p in listed or (p.split("/")[-1] if p else "index") in exclude: continue
                if re.search(r'name="robots"[^>]*noindex', open(os.path.join(dp, f), encoding="utf-8", errors="replace").read()[:4000], re.I): continue
                W.append(("PAGE_NOT_IN_SITEMAP", "/" + p, "可索引页未进 sitemap"))
        rb = os.path.join(root, "robots.txt")
        if os.path.isfile(rb):
            line = [l for l in open(rb, encoding="utf-8").read().splitlines() if l.lower().startswith("sitemap:")]
            if not line: W.append(("ROBOTS", "robots.txt", "缺 Sitemap 行"))
            elif line[0].rstrip().endswith("/"): E.append(("ROBOTS", "robots.txt", "Sitemap 地址带尾斜杠 → 308,Google 拒收"))
        else: W.append(("ROBOTS", "robots.txt", "产物里没有"))
        print(f"check_sitemap(out): {len(urls)} 条 <loc>")
    else:
        host = a.live.replace("https://", "").strip("/")
        st, xml = fetch(f"https://{host}/sitemap.xml")
        if st != 200: E.append(("SITEMAP_200", "/sitemap.xml", f"HTTP {st}")); report(E, W); return
        urls = locs(xml)
        for u in list(urls):
            if u.endswith(".xml"):
                s2, x2 = fetch(u)
                if s2 == 200: urls += locs(x2)
        urls = [u for u in urls if not u.endswith(".xml")]
        st, rob = fetch(f"https://{host}/robots.txt")
        if st != 200: E.append(("SITEMAP_200", "/robots.txt", f"HTTP {st}"))
        elif not re.search(r"^sitemap:\s*\S+", rob, re.I | re.M): W.append(("ROBOTS", "/robots.txt", "缺 Sitemap 行"))
        with ThreadPoolExecutor(8) as ex:
            for u, (s, _) in zip(urls, ex.map(fetch, urls)):
                if s != 200: E.append(("LOC_STATUS", u, f"HTTP {s}"))
        print(f"check_sitemap(live {host}): {len(urls)} 条 <loc>,非 200 {sum(1 for e in E if e[0]=='LOC_STATUS')}")
    report(E, W)


def report(E, W):
    for k, r, m in E: print(f"  ❌ {k:18} {r}  {m}")
    for k, r, m in W[:100]: print(f"  ⚠  {k:18} {r}  {m}")
    print(f"  → {len(E)} 阻塞 · {len(W)} 警告")
    sys.exit(1 if E else 0)


if __name__ == "__main__":
    main()
