#!/usr/bin/env python3
"""check_ga —— GA4 埋点「只有自己那一个、每页各一处、都在 <head> 里」的门禁(跑在产物上)。

真相源是 config/hub.json 的 ga4_id;门禁自己不写任何测量 ID,配置改了这里跟着改。

ga4_id 非空时(全部是 E,红一条就阻塞):
  E FOREIGN_ID   out/ 里出现了 ga4_id 之外的 G-XXXXXXXXXX —— 子站快照自带的标签没剥净,
                 这些页的数据会打进别人的媒体资源
  E GTAG_JS      某页 googletagmanager.com/gtag/js?id=<ga4_id> 外链行不是恰好 1 次
                 (0 次 = 这页没埋点;≥2 次 = 双重计数,会话/浏览量直接翻倍)
  E GTAG_CONFIG  某页 gtag('config','<ga4_id>') 内联行不是恰好 1 次(同上)
  E NOT_IN_HEAD  上面两处里有任一处不在 <head>…</head> 区间内,或跑到了 <body> 之后 ——
                 快照正文里子站自己的脚本会抢在它前面跑,首屏浏览量漏报
  E NO_HEAD      页面里找不到成对的 <head>…</head>

与 ga4_id 是否为空无关(Consent Mode v2 默认值每页必有,AdSense 也吃这个信号):
  E CONSENT_REGION   gtag('consent','default',{…region:[…]}) 那条(EEA/UK/CH 用的 denied)不是恰好 1 次
  E CONSENT_FALLBACK gtag('consent','default',{…}) 不带 region 的兜底那条不是恰好 1 次
                     (0 次 = 非弹窗地区没有默认值,Google CMP 只更新弹窗用户,其余全按「未知」处理)
  E CONSENT_ORDER    consent 段没有排在 adsbygoogle.js / gtag/js?id= / gtag('config') 之前(按字节偏移比)
                     —— 顺序反了 default 就不生效(Google:「If your consent code is called out of order,
                     consent defaults won't work」)
  E CONSENT_NOT_IN_HEAD  consent 段不在 <head>…</head> 里
  E DATALAYER_INIT   window.dataLayer=window.dataLayer||[] 不是恰好 1 次(≥2 = dataLayer/gtag 定义重复,
                     多半是 GA 片段又把定义抄了一遍;0 = 没有 consent 段)
  E ADS_ON_404       404.html 里出现 adsbygoogle —— AdSense 政策不许错误页带广告代码(提审前检查会阻塞);
                     404 只留 consent 段 + GA 片段。CONSENT_ORDER 只比对页里实际出现的脚本,404 没有
                     adsbygoogle 时不会误报

ga4_id 为空时(等于「本站不接 GA4」):
  E LEFTOVER_ID    out/ 里还能扫到 G-XXXXXXXXXX
  E LEFTOVER_GTAG  out/ 里还留着 gtag.js 外链或 gtag('config') 内联片段
  —— 「没配就该一处都没有」,免得清空配置之后还有半截标签在线上跑。

ID 扫描覆盖 out/ 下**所有**文件(不止 html;按字节读,不受图片/二进制影响)。

用法: python3 .gates/check_ga.py [--out out]
退出码:有 E 则 1。
"""
import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ID_RE = re.compile(rb"G-[A-Z0-9]{10}")          # 二进制安全:直接对字节找测量 ID
HEAD_OPEN_RE = re.compile(r"<head\b[^>]*>", re.I)
HEAD_CLOSE_RE = re.compile(r"</head\s*>", re.I)
BODY_OPEN_RE = re.compile(r"<body\b[^>]*>", re.I)
# 没配 ga4_id 时用的"任意 ID"版本:只要还有 gtag 片段就算残留
GTAG_JS_ANY_RE = re.compile(r"googletagmanager\.com/gtag/js", re.I)
GTAG_CFG_ANY_RE = re.compile(r"gtag\(\s*['\"]config['\"]", re.I)
# Consent Mode v2:default 命令(整条,到分号为止;对象字面量里没有分号)
CONSENT_DEFAULT_RE = re.compile(r"gtag\(\s*['\"]consent['\"]\s*,\s*['\"]default['\"]\s*,\s*\{[^;]*?\}\s*\)", re.I | re.S)
CONSENT_REGION_RE = re.compile(r"\bregion\s*:\s*\[", re.I)
ADSENSE_JS_RE = re.compile(r"pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js", re.I)
DATALAYER_INIT_RE = re.compile(r"window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|\s*\[\s*\]")


def gtag_js_re(gid: str):
    """外链行:<script async src="…/gtag/js?id=<ID>"></script>"""
    return re.compile(r"googletagmanager\.com/gtag/js\?id=" + re.escape(gid), re.I)


def gtag_cfg_re(gid: str):
    """内联行:gtag('config','<ID>') —— 引号样式与空白都放过,只认语义"""
    return re.compile(r"gtag\(\s*['\"]config['\"]\s*,\s*['\"]" + re.escape(gid) + r"['\"]", re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="out")
    a = ap.parse_args()
    out = (ROOT / a.out) if not Path(a.out).is_absolute() else Path(a.out)
    cfg = json.loads((ROOT / "config" / "hub.json").read_text(encoding="utf-8"))
    gid = (cfg.get("ga4_id") or "").strip()
    errs = []
    if not out.is_dir():
        print(f"E NO_OUT        {out}: 产物目录不存在")
        print(f"check_ga: 0 个 html(扫了 0 个文件)· 错误 1")
        sys.exit(1)

    files = sorted(p for p in out.rglob("*") if p.is_file())
    # 一、全量扫所有文件里的测量 ID(去重),顺带记下每个 ID 的出现次数与文件
    hits = {}                                   # id -> [次数, [文件 rel, …]]
    for p in files:
        found = ID_RE.findall(p.read_bytes())
        if not found:
            continue
        rel = str(p.relative_to(out))
        for b in found:
            k = b.decode("ascii")
            e = hits.setdefault(k, [0, []])
            e[0] += 1
            if rel not in e[1]:
                e[1].append(rel)

    htmls = [p for p in files if p.suffix.lower() == ".html"]
    # 二、Consent Mode v2 默认值:每页两条 default 各 1 次、都在 <head>、排在所有 Google 脚本之前、
    #     dataLayer 只初始化一次。不看 ga4_id —— AdSense 单独也要吃这个信号。
    for p in htmls:
        rel = str(p.relative_to(out))
        t = p.read_text(encoding="utf-8", errors="replace")
        ho = HEAD_OPEN_RE.search(t)
        hc = HEAD_CLOSE_RE.search(t, ho.end()) if ho else None
        defaults = list(CONSENT_DEFAULT_RE.finditer(t))
        with_region = [m for m in defaults if CONSENT_REGION_RE.search(m.group(0))]
        fallback = [m for m in defaults if not CONSENT_REGION_RE.search(m.group(0))]
        if len(with_region) != 1:
            errs.append(("CONSENT_REGION", rel,
                         f"带 region 的 gtag('consent','default') {len(with_region)} 次(应恰好 1 次)"))
        if len(fallback) != 1:
            errs.append(("CONSENT_FALLBACK", rel,
                         f"不带 region 的兜底 gtag('consent','default') {len(fallback)} 次(应恰好 1 次)"))
        if rel == "404.html":
            n_ads = len(re.findall(r"adsbygoogle", t, re.I))
            if n_ads:
                errs.append(("ADS_ON_404", rel, f"出现 adsbygoogle {n_ads} 处(错误页不许带广告代码,应 0 处)"))
        n_dl = len(DATALAYER_INIT_RE.findall(t))
        if n_dl != 1:
            errs.append(("DATALAYER_INIT", rel,
                         f"window.dataLayer=window.dataLayer||[] {n_dl} 次(应恰好 1 次)"
                         + ("  ← dataLayer/gtag 重复定义" if n_dl > 1 else "")))
        if not defaults:
            continue
        first, last = defaults[0].start(), defaults[-1].end()
        if ho and hc and not (ho.end() <= first and last <= hc.start()):
            errs.append(("CONSENT_NOT_IN_HEAD", rel, f"consent 段不在 <head>…</head> 内(偏移 {first})"))
        for what, rx in (("adsbygoogle.js", ADSENSE_JS_RE), ("gtag/js?id=", GTAG_JS_ANY_RE),
                         ("gtag('config')", GTAG_CFG_ANY_RE)):
            for m in rx.finditer(t):
                if m.start() < last:
                    errs.append(("CONSENT_ORDER", rel,
                                 f"{what}(偏移 {m.start()})排在 consent default 段(结束于 {last})之前"))
                    break
    if gid:
        for k in sorted(hits):
            if k == gid:
                continue
            n, fs = hits[k]
            errs.append(("FOREIGN_ID", k,
                         f"出现 {n} 次,见 " + ", ".join(fs[:3])
                         + (f" 等 {len(fs)} 个文件" if len(fs) > 3 else "")))
        js_re, cfg_re = gtag_js_re(gid), gtag_cfg_re(gid)
        for p in htmls:
            rel = str(p.relative_to(out))
            t = p.read_text(encoding="utf-8", errors="replace")
            ho = HEAD_OPEN_RE.search(t)
            hc = HEAD_CLOSE_RE.search(t, ho.end()) if ho else None
            bo = BODY_OPEN_RE.search(t)
            if not (ho and hc):
                errs.append(("NO_HEAD", rel, "没有成对的 <head>…</head>"))
            for kind, rx, what in (("GTAG_JS", js_re, "gtag.js 外链行"),
                                   ("GTAG_CONFIG", cfg_re, "gtag('config') 内联行")):
                ms = list(rx.finditer(t))
                if len(ms) != 1:
                    errs.append((kind, rel, f"{what} {len(ms)} 次(应恰好 1 次)"
                                 + ("  ← 双重计数" if len(ms) > 1 else "")))
                if not (ho and hc):
                    continue
                for m in ms:
                    if ho.end() <= m.start() < hc.start():
                        continue
                    pos = ("落在 <body> 里" if bo and m.start() >= bo.start()
                           else "落在 <head>…</head> 之外")
                    errs.append(("NOT_IN_HEAD", rel, f"{what}{pos}(偏移 {m.start()})"))
    else:
        for k in sorted(hits):
            n, fs = hits[k]
            errs.append(("LEFTOVER_ID", k,
                         f"ga4_id 为空但仍出现 {n} 次,见 " + ", ".join(fs[:3])
                         + (f" 等 {len(fs)} 个文件" if len(fs) > 3 else "")))
        for p in htmls:
            rel = str(p.relative_to(out))
            t = p.read_text(encoding="utf-8", errors="replace")
            nj, nc = len(GTAG_JS_ANY_RE.findall(t)), len(GTAG_CFG_ANY_RE.findall(t))
            if nj or nc:
                errs.append(("LEFTOVER_GTAG", rel,
                             f"ga4_id 为空但仍有 gtag.js 外链 {nj} 处 / gtag('config') 内联 {nc} 处"))

    for kind, f, msg in errs[:200]:
        print(f"E {kind:14s} {f}: {msg}")
    if len(errs) > 200:
        print(f"…(还有 {len(errs) - 200} 条同类错误没打印)")
    seen = " / ".join(f"{k}×{hits[k][0]}" for k in sorted(hits)) or "无"
    print(f"check_ga: {len(htmls)} 个 html(扫了 {len(files)} 个文件)· "
          f"配置 ga4_id={gid or '(空)'} · 产物里的测量 ID {seen} · 错误 {len(errs)}")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
