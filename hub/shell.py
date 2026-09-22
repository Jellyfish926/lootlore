"""shell —— 全站统一外壳。框架层,一行游戏专属文字都没有。

谁在用:
  * build.py            总站自有页面(首页 / guides / tools / updates / 信任页 / 404)
  * hub/native.py       原生内容游戏的 hub 页与内容页(目前 /valheim/)
  * 下一轮的快照套壳     game_nav() / crumbs() / byline() / faq() 直接复用,不要另写一套

约定:
  * 界面文字全部由调用方从 config/i18n/<lang>.json 取好后以 t(dict) 传进来;
  * 颜色只用 CSS 变量(定义在 config/hub.json → theme,构建期写进 out/hub.css 的 :root);
  * 任何数字都由调用方从真实文件统计后传进来,本文件不生成任何"看起来像统计"的值;
  * 数据为 0 的模块返回空串,由调用方决定不渲染 —— 不输出"0"也不输出占位语。
"""
from hub.mdlite import esc

CARET = "&#9662;"


# ---------------------------------------------------------------- 一级导航
def site_nav(*, brand, games, intents, active_game="", search="", t):
    """一级导航 = 实体型(游戏,带缩略图的巨菜单)× 意图型(玩家要做的事)两栏并列。

    games:   [{slug, label, href, thumb, thumb_alt, genre}]
    intents: [(label, href)]

    ── 两栏并列是「分组语义」,不是可见文案 ─────────────────────────────────
    by_game / by_need 只作为两个 role="group" 的 aria-label 存在(读屏能读到),
    页面上不印这两个标签。视觉上的分组表达 = 两组之间一条竖线(CSS 侧是
    .nav-ax+.nav-ax 的 ::before,颜色 --line2,≥1024px 下高度收在 26px、
    ≤1023px 抽屉里转成 border-top;--line2 本身对底色 ≥3:1,见 style.css 顶部
    的对比度记录 —— 之前是 --line,1.43:1,这条线在实际背景下等于看不见)。
    2026-09-21 那版把它们当 <p class="nav-ax-t"> 印出来,结果 header 被撑成
    两行(69px)、.hd-in 的 flex-wrap:wrap 让搜索框在 902–940px 掉到第二行,
    再被 .mm-p 面板(absolute / 279px 高 / z-index 95)整块盖住 —— 机检实测
    902px 下真点搜索框会超时(elementFromPoint 命中 a.mm-card)。别再印了。

    intents 的文案必须是调用方按当前页语种从 config/i18n/<lang>.json 取好的
    [(label, href)],不能传站级的全局默认表——hub/native.py 曾经直接复用
    build.py 算好的英文 site["nav_intents"],结果中文页顶栏也是英文,
    hub/snapshot.py 的 SnapshotLang.render() 一直是按页面语种现取,那条路对。

    三档形态(断点见 style.css,与这里的结构一一对应):
      ≥1201px 完整:品牌 · Games▾ · 竖线 · 5 个意图链接 · 搜索框(输入框+文字按钮)
      1024–1200 中间档:同上,搜索按钮收成图标、输入框收窄(不跳抽屉)
      ≤1023px 抽屉:☰ Menu,两个分组都进抽屉;搜索框独占一行
    """
    cards = "".join(
        f'<a class="mm-card{" on" if g["slug"] == active_game else ""}" href="{esc(g["href"])}">'
        + (f'<img src="{esc(g["thumb"])}" alt="{esc(g.get("thumb_alt", ""))}" width="96" height="54"'
           ' loading="lazy" decoding="async">' if g.get("thumb") else "")
        + f'<span class="mm-card-b"><b>{esc(g["label"])}</b>'
        + (f'<i>{esc(g["genre"])}</i>' if g.get("genre") else "")
        + "</span></a>"
        for g in games)
    intent_links = "".join(f'<a href="{esc(h)}">{esc(l)}</a>' for l, h in intents)
    return (
        '<header class="hd">\n<div class="hd-in">\n'
        f'<a class="brand" href="/"><b>&#9670;</b> {esc(brand)}</a>\n'
        '<input type="checkbox" id="topnav" class="topnav">'
        f'<label class="topnav-l" for="topnav"><span aria-hidden="true">&#9776;</span> {esc(t["menu"])}</label>\n'
        f'<nav class="mainnav" aria-label="{esc(t["main_nav"])}">\n'
        f'<div class="nav-ax nav-ax-games" role="group" aria-label="{esc(t["by_game"])}">'
        f'<details class="mm"><summary>{esc(t["games"])}<span class="caret" aria-hidden="true">{CARET}</span>'
        '</summary>'
        f'<div class="mm-p">{cards}'
        f'<a class="mm-all" href="/#games">{esc(t["all_games"])} &rarr;</a></div></details></div>\n'
        f'<div class="nav-ax nav-need" role="group" aria-label="{esc(t["by_need"])}">'
        f'{intent_links}</div>\n'
        "</nav>\n"
        f"{search}\n"
        "</div>\n</header>"
    )


# ---------------------------------------------------------------- 面包屑
def crumbs(items, base="", *, label="Breadcrumb"):
    """items = [(name, href_or_None)];最后一项当前页。返回 (html, jsonld_dict)。"""
    lis, els = [], []
    for k, (name, href) in enumerate(items, start=1):
        last = k == len(items)
        if href and not last:
            lis.append(f'<li><a href="{esc(href)}">{esc(name)}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{esc(name)}</li>' if last else f"<li>{esc(name)}</li>")
        e = {"@type": "ListItem", "position": k, "name": name}
        if href:
            e["item"] = base + href
        els.append(e)
    html = (f'<nav class="crumbs" aria-label="{esc(label)}"><ol>' + "".join(lis) + "</ol></nav>")
    return html, {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": els}


# ---------------------------------------------------------------- byline
def byline(*, author, author_href="", reviewed="", version="", t):
    """H1 下方的署名行:By <作者> · Last reviewed <日期>。缺的项不显示。"""
    bits = []
    if author:
        a = f'<a href="{esc(author_href)}" rel="author">{esc(author)}</a>' if author_href else esc(author)
        bits.append(f'{esc(t["by"])} {a}')
    if reviewed:
        bits.append(f'{esc(t["reviewed"])} <time datetime="{esc(reviewed)}">{esc(reviewed)}</time>')
    if version:
        bits.append(f'{esc(t["game_version"])} {esc(version)}')
    return f'<p class="byline">{esc(t["sep"]).join(bits)}</p>' if bits else ""


# ---------------------------------------------------------------- 游戏内左侧常驻导航
def game_nav(*, game_name, game_href, subtitle="", cover=None, sections, tools=(), about=(),
             current="", t, quick_max=8):
    """左侧常驻导航(game8 形状),hub 页与内容页共用同一份。

    sections: [{label, route, pages:[{title, route}], count}] —— 只传真实存在的栏目
    tools / about: [(label, href, key)]
    current:  当前页 route 或 key,用来点亮与展开所在栏目
    没有栏目就只出游戏头 + Tools/About,不造空栏目。
    """
    head = ['<div class="sn-head">']
    if cover and cover.get("src"):
        head.append(f'<img class="sn-cover" src="{esc(cover["src"])}" alt="{esc(cover.get("alt", ""))}"'
                    ' width="120" height="68" loading="lazy" decoding="async">')
    head.append(f'<a class="sn-name" href="{esc(game_href)}">{esc(game_name)}</a>')
    if subtitle:
        head.append(f'<p class="sn-sub">{esc(subtitle)}</p>')
    head.append("</div>")

    qa = ""
    tiles = [s for s in sections if s.get("route")][:quick_max]
    if tiles:
        qa = (f'<div class="sn-g"><p class="sn-t">{esc(t["quick_access"])}</p><ul class="sn-qa">'
              + "".join(f'<li><a href="{esc(s["route"])}">{esc(s["label"])}'
                        f'<span>{s["count"]}</span></a></li>' for s in tiles)
              + "</ul></div>")

    idx = ""
    if sections:
        accs = []
        for s in sections:
            here = current and (current == s.get("route") or
                                any(current in (p["route"], p.get("key")) for p in s["pages"]))
            lis = []
            if s.get("route"):
                on = ' aria-current="page" class="on"' if current == s["route"] else ""
                lis.append(f'<li><a href="{esc(s["route"])}"{on}><em>{esc(t["section_overview"])}</em></a></li>')
            for p in s["pages"]:
                on = (' aria-current="page" class="on"'
                      if current and current in (p["route"], p.get("key")) else "")
                lis.append(f'<li><a href="{esc(p["route"])}"{on}>{esc(p["title"])}</a></li>')
            accs.append(f'<details class="sn-acc"{" open" if here else ""}>'
                        f'<summary>{esc(s["label"])}<span>{s["count"]}</span></summary>'
                        f'<ul>{"".join(lis)}</ul></details>')
        idx = (f'<div class="sn-g"><p class="sn-t">{esc(t["guide_index"])}</p>'
               + "".join(accs) + "</div>")

    def group(label, rows):
        if not rows:
            return ""
        lis = "".join(
            f'<li><a href="{esc(h)}"' + (' aria-current="page" class="on"' if k and k == current else "")
            + f">{esc(n)}</a></li>" for n, h, k in rows)
        return f'<div class="sn-g"><p class="sn-t">{esc(label)}</p><ul>{lis}</ul></div>'

    return (f'<nav class="sidenav" id="sidenav" aria-label="{esc(t["site_nav"])}">'
            + "".join(head) + qa + idx + group(t["tools_group"], tools)
            + group(t["about_group"], about) + "</nav>")


# ---------------------------------------------------------------- 右栏小组件
def rail_list(title, rows, *, cls="rw"):
    """右栏小组件。rows = [(label, href, meta_or_empty)];空列表返回空串(不渲染空框)。"""
    if not rows:
        return ""
    lis = "".join(
        f'<li><a href="{esc(h)}">{esc(l)}</a>'
        + (f"<span>{esc(m)}</span>" if m else "") + "</li>"
        for l, h, m in rows)
    return (f'<section class="{cls}"><p class="rw-t">{esc(title)}</p>'
            f"<ul>{lis}</ul></section>")


# ---------------------------------------------------------------- FAQ 手风琴
def faq(items, heading, hid):
    """items = [(question, answer_html)] —— 全部来自内容层,框架不生成问答。
    返回 (html, jsonld_or_None)。"""
    if not items:
        return "", None
    body = "".join(
        f'<details class="fq"><summary>{esc(q)}</summary><div class="fq-b">{a}</div></details>'
        for q, a in items)
    html = f'<section class="faq"><h2 id="{esc(hid)}">{esc(heading)}</h2>{body}</section>'
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return html, ld


# ---------------------------------------------------------------- 页脚
def footer(*, brand, year, links, note):
    nav = "".join(f'<a href="{esc(h)}">{esc(n)}</a>' for n, h in links)
    return ('<footer class="ft">\n<div class="wrap">\n'
            f"<nav>{nav}</nav>\n"
            f"<p>&copy; {esc(str(year))} {esc(brand)}. {esc(note)}</p>\n"
            "</div>\n</footer>")


# ---------------------------------------------------------------- 站内搜索
def search_form(*, action, index_url, lang, t, scope="", placeholder=""):
    """全站搜索表单。无 JS 时提交到 action(全量清单页),是可用的退化路径。"""
    return (f'<form id="gs" class="gs" role="search" action="{esc(action)}" method="get"'
            f' data-lang="{esc(lang)}" data-index="{esc(index_url)}"'
            + (f' data-scope="{esc(scope)}"' if scope else "")
            + f' data-none="{esc(t["search_no_results"])}">'
            f'<label class="sr" for="gs-i">{esc(t["search"])}</label>'
            f'<input id="gs-i" type="search" name="q"'
            f' placeholder="{esc(placeholder or t["search_placeholder"])}"'
            ' autocomplete="off">'
            f'<button type="submit">{esc(t["search"])}</button>'
            '<ul id="gs-r" class="gs-r" hidden></ul></form>')


# 顶栏 Games 巨菜单的「点外面关掉 / Esc 关掉」。没它的时候菜单一旦打开就一直挂着,
# .mm-p 是 absolute + z-index 95,会整块盖住 header 下方的正文链接 —— 这就是站主说的
# 「链接点不动」的第二个来源。无 JS 时退化成「再点一次 summary 关掉」,仍可用。
# 抽屉里(≤1023px)不关,免得点开游戏组就被自己收回去。
NAV_JS = (
    "<script>(function(){var d=document.querySelector('details.mm');if(!d)return;"
    "function sh(){return window.matchMedia('(min-width:1024px)').matches;}"
    "document.addEventListener('click',function(e){"
    "if(d.open&&sh()&&!d.contains(e.target))d.open=false;});"
    "document.addEventListener('keydown',function(e){"
    "if(e.key==='Escape'&&d.open){d.open=false;"
    "var s=d.querySelector('summary');if(s)s.focus();}});"
    "})();</script>"
)

# 全站搜索前端过滤。内联,门禁上限 3KB。结果用 DOM API 拼,不拼 HTML 字符串。
# data-scope 有值时先把结果收窄到该游戏,再补全站结果(当前游戏优先,不丢全站可达性)。
SEARCH_JS = NAV_JS + (
    "<script>(function(){var f=document.getElementById('gs');if(!f)return;"
    "var i=f.querySelector('input'),r=document.getElementById('gs-r'),"
    "L=f.getAttribute('data-lang'),U=f.getAttribute('data-index'),"
    "S=f.getAttribute('data-scope')||'',N=f.getAttribute('data-none'),D=null,P=null;"
    "function load(){if(D)return Promise.resolve(D);if(P)return P;"
    "P=fetch(U).then(function(x){return x.json();}).then(function(j){"
    "D=j.filter(function(e){return e.lang===L;});return D;});return P;}"
    "function row(e){var li=document.createElement('li'),a=document.createElement('a'),"
    "s=document.createElement('span');a.href=e.url;a.textContent=e.title;"
    "s.textContent=e.section?e.game+' \\u00b7 '+e.section:e.game;"
    "li.appendChild(a);li.appendChild(s);return li;}"
    "function run(){var q=i.value.trim().toLowerCase();"
    "if(!q){r.hidden=true;r.textContent='';return;}"
    "load().then(function(d){var m=d.filter(function(e){"
    "return (e.title+' '+e.description+' '+e.section+' '+e.game).toLowerCase().indexOf(q)>=0;});"
    "if(S)m.sort(function(a,b){return (b.game===S)-(a.game===S);});"
    "m=m.slice(0,10);r.textContent='';"
    "if(!m.length){var li=document.createElement('li');li.className='none';"
    "li.textContent=N;r.appendChild(li);}else m.forEach(function(e){r.appendChild(row(e));});"
    "r.hidden=false;});}"
    "i.addEventListener('input',run);i.addEventListener('focus',load);"
    "document.addEventListener('click',function(e){if(!f.contains(e.target))r.hidden=true;});"
    "})();</script>"
)
