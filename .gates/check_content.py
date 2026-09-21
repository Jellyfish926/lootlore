#!/usr/bin/env python3
"""check_content —— 对构建产物(HTML 目录)做内容 lint。八道门禁之一,跑在产物上,不看源码。

规则(E = 阻塞,W = 警告):
  E H1_COUNT       每页 H1 必须恰好 1 个
  E IMG_ALT        <img> 必须有非空 alt(装饰图用 alt="" + role="presentation" 可豁免)
  E DEAD_INTERNAL  站内链接必须能解析到产物里的文件(尊重 trailingSlash / cleanUrls)
  E PLACEHOLDER    正文出现占位语(coming soon / being verified / 待补充 / TBD …)
  W HEADING_SKIP   标题层级跳级(H2 → H4)
  W FEW_LINKS      正文站内链接 < N 条(默认 3)
  W LOCALE_LINK    小语种页面里的站内链接指向了主语种页,而对应小语种页存在
  W LANG_ATTR      <html lang> 与所在语种目录不一致

用法:
  python3 check_content.py <html_dir> [--locales de,es,fr,it,ja] [--default en] [--min-links 3]
                           [--trailing-slash auto|yes|no] [--json] [--exclude 404,privacy-policy,terms]
                           [--dir-lang <game>=<lang>,...]

语种判定(2026-09-21 重写——同一个坑踩了三次之后,从「人工传参」改成「自动探测」):
  总站产物是 /<game>/<locale>/<page>,子站自身产物是 /<locale>/<page>,而且不是每个 game 都有
  语种子目录:有的整个 game 目录单语种(如 sephiria/dragonsword-awakening/orc-problem/
  shift-at-midnight,全站一种语言,没有语种子目录);有的混合(如 valheim,根页是默认语种、
  /zh/ 子目录是中文);有的每个语种各自一个子目录(如 beast-of-reincarnation 的
  de/en/es/fr/it/ja)。过去靠 --locales/--dir-lang 人工声明每个 game 的语种结构,声明一旦
  漏传、或者跟目录结构后续变化脱节(valheim 起初整站中文,后来根目录加了英文页,老的
  --dir-lang valheim=zh 就把整个 game 目录误判成 zh),就会整批假警报:2026-09-11
  lootlore 165 条、2026-09-17 valheim 40 条、2026-09-21 第三次(--locales/--dir-lang
  没有完整传上就报了一整批 /beast-of-reincarnation/ 的假 LANG_ATTR)。
  现在按 /<game>/ 切出每个 game 的子树,在子树内自动判定(见 classify_games()):某段名
  形如语种码(it/de/zh…)且该段下多数页面的 <html lang> 真等于段名,才确认为语种子目录;
  确认不了的段(如 valheim/co-op——形如语种码但页面其实是 lang=en)连同 game 根页一起算
  baseline,baseline 语种取多数页面的 lang。全 game 没有任何确认的语种子目录 = 单语种整
  目录站,跑起来会打印「单语种跳过」,不会拿默认语种硬套、也不会拿它跟别的语种子目录比对。
  --locales/--default 不再是判定正确与否的必要输入(保留只为兼容旧调用,以及 LOCALE_LINK
  的排除表);--dir-lang 也保留,但降级成诊断性声明——传了就跟自动探测结果核对,两边对不上
  就打印警告并按自动探测(即与产物页面实际内容一致)的结果判,这样传一个过期的 --dir-lang
  不会再制造假警报,只会在日志里提醒它已经跟不上目录结构了。
退出码:有 E 则 1,否则 0。
"""
import argparse, json, os, re, sys, html
from collections import Counter, defaultdict
from html.parser import HTMLParser

PLACEHOLDER_CS = re.compile(r"\bTBD\b|\bTODO\b")
PLACEHOLDER = re.compile(r"coming soon|being verified|will be verified|to be confirmed|待补充|稍后补|稍后更新|即将上线|lorem ipsum", re.I)
TRUST = {"about", "contact", "privacy-policy", "privacy", "terms", "terms-of-service", "disclaimer", "editorial-policy", "404", "500", "search"}


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h = []; self.imgs = []; self.links = []; self.lang = None; self.in_main = 0; self.main_seen = False
        self.text = []; self._skip = 0; self.in_head = False; self.noindex = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = (a.get("lang") or "").split("-")[0].lower()
        if tag == "head": self.in_head = True
        if tag == "meta" and (a.get("name") or "").lower() == "robots" and "noindex" in (a.get("content") or "").lower(): self.noindex = True
        if tag in ("main", "article") and not self.main_seen: self.in_main += 1; self.main_seen = True
        if tag in ("script", "style", "nav", "header", "footer", "aside"): self._skip += 1
        if self._skip: return
        if re.fullmatch(r"h[1-6]", tag): self.h.append((int(tag[1]), self.getpos()[0]))
        if tag == "img": self.imgs.append((a.get("alt"), a.get("role"), a.get("src", "")))
        if tag == "a" and a.get("href"): self.links.append((a["href"], self.in_main > 0, bool(a.get("hreflang"))))

    def handle_endtag(self, tag):
        if tag == "head": self.in_head = False
        if tag in ("script", "style", "nav", "header", "footer", "aside") and self._skip: self._skip -= 1
        if tag in ("main", "article") and self.in_main: self.in_main -= 1

    def handle_data(self, d):
        if not self._skip and not self.in_head: self.text.append(d)


def dir_prefix_lang(parts, dir_lang):
    """--dir-lang 支持多段前缀(如 valheim/zh=zh);取最长匹配的那条。"""
    best = None
    for pref, lang in dir_lang.items():
        seg = [x for x in pref.strip("/").split("/") if x]
        if parts[:len(seg)] == seg and (best is None or len(seg) > best[0]):
            best = (len(seg), lang)
    return best[1] if best else None


LOCALE_SEG_RE = re.compile(r"^[a-z]{2}(-[a-z]{2})?$")
HTML_LANG_RE = re.compile(r'<html\b[^>]*\blang="([^"]*)"', re.I)


def classify_games(root, exclude):
    """扫描 root 下每个 /<game>/ 子树,自动判定它的语种结构。见文件头「语种判定」说明。

    路径第 1 段(game 之后那一段,如 /beast-of-reincarnation/it/ 里的 "it")被「确认」为
    语种子目录,当且仅当:①它形如语种码(LOCALE_SEG_RE);②该段下多数页面的 <html lang>
    真的等于这个段名。两个条件都是从产物内容里量出来的,不依赖外部声明,所以 valheim/co-op
    这种形如语种码、但页面其实是 lang=en 的目录不会被误判(内容跟目录名对不上,就不确认)。
    不满足条件的段连同 game 根页一起计入该 game 的 baseline 桶,baseline 语种取桶内多数 lang。

    返回 {game: {"confirmed": {seg: lang}, "confirmed_pages": {seg: n}, "baseline_lang": lang|None, "baseline_pages": n}}
    """
    buckets = defaultdict(Counter)  # (game, seg_or_None) -> Counter(lang)
    for dp, _, fs in os.walk(root):
        if "/_next" in dp or "/node_modules" in dp: continue
        for f in fs:
            if not f.endswith(".html"): continue
            path = os.path.join(dp, f)
            route = route_of(path, root)
            parts = route.strip("/").split("/") if route.strip("/") else []
            if not parts: continue
            slug = parts[-1]; first = parts[0]
            if slug in exclude or first in exclude: continue
            try: head = open(path, encoding="utf-8", errors="replace").read(4096)
            except Exception: continue
            mo = HTML_LANG_RE.search(head)
            lang = mo.group(1).split("-")[0].lower() if mo else ""
            if not lang: continue
            buckets[(parts[0], parts[1] if len(parts) >= 2 else None)][lang] += 1
    by_game = defaultdict(dict)
    for (game, seg), counter in buckets.items():
        by_game[game][seg] = counter
    profiles = {}
    for game, segs in by_game.items():
        confirmed, baseline = {}, Counter()
        for seg, counter in segs.items():
            top_lang, _ = counter.most_common(1)[0]
            if seg and LOCALE_SEG_RE.match(seg) and top_lang == seg:
                confirmed[seg] = top_lang
            else:
                baseline.update(counter)
        profiles[game] = {
            "confirmed": confirmed,
            "confirmed_pages": {s: sum(segs[s].values()) for s in confirmed},
            "baseline_lang": baseline.most_common(1)[0][0] if baseline else None,
            "baseline_pages": sum(baseline.values()),
        }
    return profiles


def route_of(path, root):
    rel = os.path.relpath(path, root).replace(os.sep, "/")
    if rel.endswith("/index.html"): rel = rel[:-len("index.html")]
    elif rel.endswith(".html"): rel = rel[:-5]
    return "/" + rel.strip("/") + ("/" if rel.endswith("/") or rel == "" else "")


def resolve(href, root, trailing):
    """站内 href → 产物文件是否存在。返回 (exists, normalized_route)"""
    h = href.split("#")[0].split("?")[0]
    if not h or h.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "//", "data:")): return True, None
    h = html.unescape(h)
    if not h.startswith("/"): return True, None  # 相对路径不判(少见)
    p = h.strip("/")
    cands = [os.path.join(root, p), os.path.join(root, p, "index.html"), os.path.join(root, p + ".html")] if p else [os.path.join(root, "index.html")]
    ok = any(os.path.isfile(c) for c in cands)
    return ok, "/" + p + ("/" if trailing else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root"); ap.add_argument("--locales", default=""); ap.add_argument("--default", default="en")
    ap.add_argument("--min-links", type=int, default=3); ap.add_argument("--trailing-slash", default="auto")
    ap.add_argument("--json", action="store_true"); ap.add_argument("--exclude", default="")
    ap.add_argument("--dir-lang", default="", help="逗号分隔的 <顶层目录>=<语种>,如 <game>=zh")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    locales = [x for x in a.locales.split(",") if x]
    exclude = set(TRUST) | {x for x in a.exclude.split(",") if x}
    dir_lang = dict(x.split("=", 1) for x in a.dir_lang.split(",") if "=" in x)
    trailing = a.trailing_slash
    if trailing == "auto":
        # 有 x/index.html 结构 → trailing;全是 x.html → clean
        idx = sum(1 for dp, _, fs in os.walk(root) for f in fs if f == "index.html")
        flat = sum(1 for dp, _, fs in os.walk(root) for f in fs if f.endswith(".html") and f != "index.html")
        trailing = "yes" if idx >= flat else "no"
    trailing = trailing == "yes"

    game_profiles = classify_games(root, exclude)
    known_locale_segs = {seg for prof in game_profiles.values() for seg in prof["confirmed"]}
    if not a.json:
        for game in sorted(game_profiles):
            prof = game_profiles[game]
            if not prof["confirmed"]:
                print(f"  [LANG] 单语种跳过: /{game}/ 全目录判定为 {prof['baseline_lang'] or '?'}"
                      f"({prof['baseline_pages']} 页) —— 没有已确认的语种子目录,不做跨目录语种比对,仍查页内一致性")
            else:
                segs_desc = ", ".join(f"{s}={l}({prof['confirmed_pages'][s]}页)" for s, l in sorted(prof["confirmed"].items()))
                base_desc = f"根页 baseline={prof['baseline_lang']}({prof['baseline_pages']}页)" if prof["baseline_lang"] else "根页无"
                print(f"  [LANG] /{game}/ 语种目录:{segs_desc};{base_desc}")
        for pref, lang in dir_lang.items():
            pseg = [x for x in pref.strip("/").split("/") if x]
            prof = game_profiles.get(pseg[0]) if pseg else None
            if not prof: continue
            actual = prof["confirmed"].get(pseg[1]) if len(pseg) >= 2 else prof["baseline_lang"]
            if actual and actual != lang:
                print(f"  [LANG] ⚠ --dir-lang {pref}={lang} 与实测内容不符(该前缀下多数页实际是 {actual}),"
                      f"按实测结果处理,已忽略这条过期声明")

    E, W = [], []
    pages = 0
    for dp, _, fs in os.walk(root):
        if "/_next" in dp or "/node_modules" in dp: continue
        for f in fs:
            if not f.endswith(".html"): continue
            path = os.path.join(dp, f)
            route = route_of(path, root)
            parts = route.strip("/").split("/") if route.strip("/") else []
            slug = parts[-1] if parts else "home"
            first = parts[0] if parts else ""
            if slug in exclude or first in exclude: continue
            p = P()
            try: p.feed(open(path, encoding="utf-8", errors="replace").read())
            except Exception as e: E.append(("PARSE", route, str(e)[:80])); continue
            if p.noindex: continue
            pages += 1
            h1 = [x for x in p.h if x[0] == 1]
            if len(h1) != 1: E.append(("H1_COUNT", route, f"H1 数量 {len(h1)}"))
            prev = 1
            for lvl, line in p.h:
                if lvl > prev + 1: W.append(("HEADING_SKIP", route, f"H{prev}→H{lvl} @line {line}")); break
                prev = lvl
            for alt, role, src in p.imgs:
                if (alt is None or not alt.strip()) and role != "presentation": E.append(("IMG_ALT", route, src[:80]))
            body = " ".join(p.text)
            m = PLACEHOLDER.search(body) or PLACEHOLDER_CS.search(body)
            if m: E.append(("PLACEHOLDER", route, f"「{m.group(0)}」"))
            internal_main = 0
            # 语种判定:先按 /<game>/ 切子树,子树内的语种结构已在主循环前由 classify_games()
            # 自动探测好(game_profiles)——目录名与页面实际 <html lang> 互相印证,不靠
            # --locales/--dir-lang 兜底,漏传/传错参数不会再把整站误判成默认语种(这个坑
            # 2026-09-11、09-17、09-21 踩了三次,细节见文件头「语种判定」说明)。
            game = parts[0] if parts else ""
            prof = game_profiles.get(game)
            seg = parts[1] if len(parts) >= 2 else None
            if prof and seg is not None and seg in prof["confirmed"]:
                page_locale = prof["confirmed"][seg]
                locale_prefix = parts[:1]
            elif prof and prof["confirmed"] and prof["baseline_lang"]:
                # 混合目录(如 valheim:根页默认语种 + /zh/ 子目录):根页按 baseline 语种判
                page_locale = prof["baseline_lang"]
                locale_prefix = parts[:-1] if parts else []
            elif prof and prof["baseline_lang"]:
                # 全目录单语种,没有已确认的语种子目录,没有「同语种旁页」可比,跳过 LOCALE_LINK
                page_locale = prof["baseline_lang"]
                locale_prefix = None
            else:
                page_locale = a.default
                locale_prefix = parts[:-1] if parts else []
            for href, in_main, has_hreflang in p.links:
                ok, norm = resolve(href, root, trailing)
                if norm is None: continue
                if not ok: E.append(("DEAD_INTERNAL", route, href[:100])); continue
                if in_main or not p.main_seen: internal_main += 1
                # 带显式 hreflang 属性的链接是语言切换器自报的「故意跨语种」(如页头
                # 「语言:中文 [English]」控件),不是正文误链,不计入 LOCALE_LINK。
                if page_locale != a.default and locale_prefix is not None and not has_hreflang:
                    norm_parts = norm.strip("/").split("/")
                    link_seg = norm_parts[len(locale_prefix)] if len(norm_parts) > len(locale_prefix) else ""
                    if (norm_parts[:len(locale_prefix)] == locale_prefix and link_seg
                            and link_seg not in locales and link_seg not in known_locale_segs and link_seg not in exclude):
                        loc_parts = locale_prefix + [page_locale] + norm_parts[len(locale_prefix):]
                        loc_path = os.path.join(root, *loc_parts)
                        if os.path.isfile(os.path.join(loc_path, "index.html")) or os.path.isfile(loc_path + ".html"):
                            loc_route = "/" + "/".join(loc_parts) + "/"
                            W.append(("LOCALE_LINK", route, f"{href} 指向主语种页,但 {loc_route} 存在"))
            if internal_main < a.min_links: W.append(("FEW_LINKS", route, f"正文站内链接 {internal_main} < {a.min_links}"))
            if p.lang and page_locale and p.lang != page_locale.lower(): W.append(("LANG_ATTR", route, f"<html lang={p.lang}> 但目录语种 {page_locale}"))
    if a.json:
        print(json.dumps({"pages": pages, "errors": E, "warnings": W, "game_locale_profile": game_profiles}, ensure_ascii=False, indent=1))
    else:
        print(f"check_content: {pages} 页 · {len(E)} 阻塞 · {len(W)} 警告 (trailingSlash={'yes' if trailing else 'no'})")
        for k, r, m in E: print(f"  ❌ {k:14} {r}  {m}")
        for k, r, m in W[:200]: print(f"  ⚠  {k:14} {r}  {m}")
        if len(W) > 200: print(f"  … 另 {len(W)-200} 条警告")
    sys.exit(1 if E else 0)


if __name__ == "__main__":
    main()
