#!/usr/bin/env python3
"""freshness_audit —— 保鲜审计:哪些页过期了。只报告,绝不改内容。

数据来源(按优先级):sitemap.xml 的 <lastmod> → 页面里的「Last reviewed / Last updated / updated」日期。
分级(seo-yunying 五·三 阈值):
  P0  codes 页(URL 或 title 含 code)超 7 天未核验;超 30 天几乎必有失效码
  P1  时效性页(URL 含 boss|tier|build|weapon|patch|meta|best)超 90 天
  P2  其他页超 180 天(信息页,提示而已)
输出 markdown(给 GitHub issue 用),退出码始终 0(审计不阻塞)。
用法: python3 freshness_audit.py --out DIR | --live HOST  [--codes-days 7] [--stale-days 90]
"""
import argparse, datetime as dt, os, re, sys, urllib.request

TIME_SENSITIVE = re.compile(r"boss|tier|build|weapon|patch|meta|best|ranking|update", re.I)
CODES = re.compile(r"code", re.I)
DATE = re.compile(r"(20\d{2}-\d{2}-\d{2})")


def fetch(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "seo-gates/1.0"}), timeout=20) as r: return r.read().decode("utf-8", "replace")
    except Exception: return ""


def main():
    ap = argparse.ArgumentParser(); g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--out"); g.add_argument("--live"); ap.add_argument("--codes-days", type=int, default=7); ap.add_argument("--stale-days", type=int, default=90)
    a = ap.parse_args(); today = dt.date.today()
    if a.out:
        sm = os.path.join(a.out, "sitemap.xml"); xml = open(sm, encoding="utf-8").read() if os.path.isfile(sm) else ""
    else:
        xml = fetch(f"https://{a.live}/sitemap.xml")
    entries = re.findall(r"<url>\s*<loc>\s*([^<\s]+)\s*</loc>(?:.*?<lastmod>\s*([^<\s]+)\s*</lastmod>)?.*?</url>", xml, re.S)
    if not entries:
        print("# 保鲜审计\n\n未获取:sitemap.xml 读不到或没有 <url> 条目。"); return
    rows = []
    for loc, lastmod in entries:
        d = None
        m = DATE.search(lastmod or "")
        if m: d = dt.date.fromisoformat(m.group(1))
        if d is None:
            html = ""
            if a.out:
                p = re.sub(r"^https?://[^/]+/?", "", loc).strip("/")
                for c in (os.path.join(a.out, p, "index.html"), os.path.join(a.out, p + ".html")):
                    if os.path.isfile(c): html = open(c, encoding="utf-8", errors="replace").read(); break
            else: html = fetch(loc)
            m = re.search(r"(?:last reviewed|last updated|updated|reviewed)[^0-9]{0,30}(20\d{2}-\d{2}-\d{2})", html, re.I)
            if m: d = dt.date.fromisoformat(m.group(1))
        age = (today - d).days if d else None
        path = re.sub(r"^https?://[^/]+", "", loc)
        if CODES.search(path):
            lvl = "P0" if (age is None or age > a.codes_days) else None
            note = "codes 页超 30 天,几乎必有失效码" if age and age > 30 else "codes 页超 7 天未核验"
        elif TIME_SENSITIVE.search(path):
            lvl = "P1" if (age is None or age > a.stale_days) else None; note = "时效性页超 90 天,版本可能已变"
        else:
            lvl = "P2" if (age is not None and age > 180) else None; note = "超 180 天,顺手核一眼"
        if lvl: rows.append((lvl, path, age, note if age is not None else "日期未获取(sitemap 无 lastmod 且页面无日期戳)"))
    rows.sort(key=lambda r: ({"P0": 0, "P1": 1, "P2": 2}[r[0]], -(r[2] or 9999)))
    print(f"# 保鲜审计 {today.isoformat()}\n")
    print(f"sitemap {len(entries)} 页 · P0 {sum(r[0]=='P0' for r in rows)} · P1 {sum(r[0]=='P1' for r in rows)} · P2 {sum(r[0]=='P2' for r in rows)}\n")
    if not rows: print("全部在期内,无需动作。"); return
    print("| 级别 | 页面 | 距上次更新 | 说明 |\n|---|---|---|---|")
    for lvl, path, age, note in rows[:60]: print(f"| {lvl} | `{path}` | {age if age is not None else '未获取'} 天 | {note} |")
    if len(rows) > 60: print(f"\n… 另 {len(rows)-60} 条")
    print("\n动作:P0 当轮更(官方渠道核新码 → 改 status → 动日期戳);P1 对照最新补丁核数值;P2 顺手。**本审计只提醒,不改内容。**")


if __name__ == "__main__":
    main()
