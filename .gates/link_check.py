#!/usr/bin/env python3
"""
link_check.py —— 站内死链全量检查

为什么需要它:
  adsense_check.py 和 sitemap 检查都只回答「sitemap 里列出的页面是否活着」。
  它们答不了「站上渲染出来的链接是否指向真实页面」。
  这两个问题不一样 —— 一个不存在的页面不会出现在 sitemap 里,所以指向它的链接
  永远不会被 sitemap 检查发现。

  2026-08-10 实际踩过:sephiriawiki.site 首页最显眼的 CTA 按钮指向
  /guides/beginner-guide/(那是 dragonsword.site 的路径,配置复制时没改),
  sitemap 26 条全部 200、审计全绿,但首页第一个按钮是 404。

  这是「两个真相源」的又一次:hero.cta 和 startHere 各写了一遍同一个链接,
  改了一个没改另一个。

用法:
  # 线上模式:从 sitemap 出发爬全站,检查每一个站内链接
  python3 scripts/link_check.py --live sephiriawiki.site

  # 构建产物模式:不需要联网,检查 out/ 目录
  python3 scripts/link_check.py --out sites/sephiriawiki.site/out

  # 配置模式:只检查 config/site.json 里的 href 是否有对应内容文件(最快)
  python3 scripts/link_check.py --config sites/sephiriawiki.site

有死链时退出码为 1,可以挂进 CI / watchdog。
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict

UA = {"User-Agent": "Mozilla/5.0 (compatible; seo-factory-linkcheck/1.0)"}
TRUST_SLUGS = {"about", "contact", "privacy-policy"}


def fetch(url, timeout=25, tries=3):
    """返回 (状态码, 正文)。状态码 0 = 网络层失败,不是 404。

    这个区分很重要:沙箱/容器里偶发的 TLS 超时会让一个活得好好的页面
    看起来像死链。踩过一次 —— 报了两条「死链」,直接 curl 三次全是 200。
    「我没看到」不等于「它不存在」,所以这里重试,并且把两种失败分开报。
    """
    last = 0
    for attempt in range(tries):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout)
            return r.status, r.read().decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            return e.code, ""          # 真的 HTTP 错误,不用重试
        except Exception:
            last = 0
            if attempt < tries - 1:
                time.sleep(1.5 * (attempt + 1))
    return last, ""


def internal_hrefs(html):
    """抽出所有站内绝对路径链接,去掉 #锚点 和 ?参数。"""
    out = set()
    for h in re.findall(r'href="([^"]+)"', html):
        if h.startswith("/") and not h.startswith("//"):
            out.add(h.split("#")[0].split("?")[0])
    return out


def check_live(host):
    base = f"https://{host}"
    status, sm = fetch(base + "/sitemap.xml")
    if status != 200:
        print(f"✗ 拿不到 sitemap ({status}): {base}/sitemap.xml")
        return 1
    pages = re.findall(r"<loc>([^<]+)</loc>", sm)
    print(f"{host}: sitemap {len(pages)} 页")

    links = defaultdict(set)
    for p in pages:
        _, html = fetch(p)
        src = p.replace(base, "") or "/"
        for href in internal_hrefs(html):
            links[href].add(src)
    print(f"  发现 {len(links)} 个不同站内链接,逐个验证…")

    bad = []
    for href in sorted(links):
        code, _ = fetch(base + href)
        if code != 200:
            bad.append((code, href, sorted(links[href])))
    return report(bad)


def check_out(outdir):
    """检查构建产物。href /a/b/ 对应 out/a/b/index.html。"""
    if not os.path.isdir(outdir):
        print(f"✗ 目录不存在: {outdir} —— 先跑 npm run build")
        return 1
    htmls = []
    for root, _, files in os.walk(outdir):
        for f in files:
            if f.endswith(".html"):
                htmls.append(os.path.join(root, f))
    print(f"{outdir}: {len(htmls)} 个 HTML")

    def resolves(href):
        p = href.strip("/")
        for cand in (
            os.path.join(outdir, p, "index.html"),
            os.path.join(outdir, p) if p else None,
            os.path.join(outdir, p + ".html") if p else None,
        ):
            if cand and os.path.isfile(cand):
                return True
        return href == "/" and os.path.isfile(os.path.join(outdir, "index.html"))

    links = defaultdict(set)
    for h in htmls:
        src = "/" + os.path.relpath(h, outdir).replace("index.html", "")
        with open(h, encoding="utf-8", errors="ignore") as fh:
            for href in internal_hrefs(fh.read()):
                links[href].add(src)
    print(f"  发现 {len(links)} 个不同站内链接,逐个验证…")

    bad = [(404, href, sorted(srcs)) for href, srcs in sorted(links.items()) if not resolves(href)]
    return report(bad)


def check_config(sitedir):
    """只查 config/site.json 里的 href —— 最快,建站时先跑这个。"""
    cfg = os.path.join(sitedir, "config", "site.json")
    if not os.path.isfile(cfg):
        print(f"✗ 找不到 {cfg}")
        return 1
    d = json.load(open(cfg, encoding="utf-8"))
    content = os.path.join(sitedir, "content", "en")
    live = {n["slug"] for n in d.get("nav", [])}

    hrefs = []

    def walk(o, path=""):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "href" and isinstance(v, str):
                    hrefs.append((path, v))
                else:
                    walk(v, f"{path}.{k}" if path else k)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, f"{path}[{i}]")

    walk(d)

    def exists(h):
        p = h.strip("/")
        if p == "":
            return True
        if p in TRUST_SLUGS:
            return os.path.isfile(os.path.join(content, "site", p + ".mdx"))
        if "/" not in p:
            return p in live and os.path.isdir(os.path.join(content, p))
        return os.path.isfile(os.path.join(content, p + ".mdx"))

    print(f"{sitedir}: config 里 {len(hrefs)} 个 href")
    bad = [(404, h, [path]) for path, h in hrefs if not exists(h)]
    return report(bad)


def report(bad):
    """bad: [(code, href, sources)]。code 0 = 重试后仍连不上,单独归类。"""
    dead = [b for b in bad if b[0] != 0]
    unreachable = [b for b in bad if b[0] == 0]

    if unreachable:
        print(f"  ⚠️ {len(unreachable)} 个地址重试后仍连不上 —— 这是网络问题,不是死链:")
        for _, href, srcs in unreachable:
            print(f"      {href}  (出现在 {len(srcs)} 处)")
        print("      换个有稳定出网的环境复跑,或手动 curl 确认。")

    if not dead:
        print("  ✓ 无死链" + ("(但有上面那些没测到的)" if unreachable else ""))
        return 1 if unreachable else 0

    print(f"  ✗ {len(dead)} 个死链:")
    for code, href, srcs in dead:
        print(f"    [{code}] {href}")
        for s_ in srcs[:8]:
            print(f"          ← {s_}")
        if len(srcs) > 8:
            print(f"          ← …共 {len(srcs)} 处")
    return 1


def main():
    ap = argparse.ArgumentParser(description="站内死链检查")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--live", metavar="HOST", help="线上域名,如 sephiriawiki.site")
    g.add_argument("--out", metavar="DIR", help="构建产物目录,如 sites/xxx/out")
    g.add_argument("--config", metavar="SITEDIR", help="站点根目录,只查 config 里的 href")
    a = ap.parse_args()
    if a.live:
        sys.exit(check_live(a.live))
    if a.out:
        sys.exit(check_out(a.out))
    sys.exit(check_config(a.config))


if __name__ == "__main__":
    main()
