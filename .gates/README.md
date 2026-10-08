# .gates —— 站点门禁脚本(来自 seo-jianzhan/scripts,2026-09-03)

CI(`.github/workflows/gates.yml`)每次 push / PR 跑:构建 → check_config(Next 站)→ check_content → check_i18n(多语言站)→ check_sitemap → link_check;
红一条不许合。本地复现:同样的命令对 `out` 跑一遍。
每周一 `freshness.yml` 审计线上 sitemap 的 lastmod,过期页开 issue(label: freshness),只提醒不改内容。
改脚本请改 seo-jianzhan/scripts 的真相源再同步到各站,别只改这里。

lootlore 本地增补(2026-09-17,待同步回 seo-jianzhan/scripts):
- `check_content.py --dir-lang valheim=zh`:整个游戏目录是单一非主语种(无语种子目录)时,LANG_ATTR 按声明语种判,不再误报。
- `tech_audit.py`(由 seo-jianzhan/scripts/tech-audit.py 复制):加 `--out/--base/--prefix/--summary` 命令行;title/description 按显示宽度(CJK 记 2);正文词数按「拉丁词 + CJK/2」;外部热链 og:image 不按本地文件查。只报告不阻塞。

lootlore 本地增补(2026-09-18,valheim v2,待同步回 seo-jianzhan/scripts):
- `check_content.py --dir-lang valheim/zh=zh`:`--dir-lang` 支持多段路径前缀,取最长匹配(原来只认顶层目录)。
- `check_i18n.py --root-default`:主语种页直接落在栏目根(`/<game>/…`)、其余语种在 `/<game>/<locale>/` 下的布局;
  LANG_ATTR 比较时按主语种码截断(`zh-CN` ↔ `zh`)。gates.yml 因此把 check_i18n 拆成两步跑。

lootlore 本站专有门禁(2026-10-08,脚本在 `scripts/` 而不在 `.gates/` —— 它还有 `--live` 线上模式,不只是门禁):
- `scripts/url_consistency_audit.py --out out` —— 全站页面 URL 只许「带尾斜杠」一种写法。逐页实测并计数:
  sitemap `<loc>` 不带斜杠 / 重复;canonical 缺失、不带斜杠、不自指;og:url 不自指;hreflang 不带斜杠、
  指向不存在、互指不对称、无自指;JSON-LD 里本站 URL 不带斜杠或指向不存在;站内 `<a href>` / form action /
  内联脚本 / search-index.json / llms.txt 不带斜杠;`vercel.json` 没开 `trailingSlash:true`、redirects
  源地址缺带斜杠写法、目的地不带斜杠或不存在;游戏根目录 `/<slug>/` 既无页面也无重定向。任一项 ≠ 0 退出码 1。
  `--live https://lootwiki.com` 审线上(另测每页「不带斜杠变体」是否 308 单跳到带斜杠版)。
  gates.yml 与 sync-sources.yml 都跑 `--out` 这一条。

lootlore 本站专有门禁(2026-09-22,不同步回 seo-jianzhan/scripts —— 只有套壳站群才有这条约束):
- `check_snapshot.py` —— 快照页正文「逐字节零改动」的门禁。对 `sources/<game>/**.html`
  跑与 build.py 同一条链路(`transform_urls` → `hub.snapshot.parse_page`),再把产物里
  `.sn-body` 的内容拼起来逐字节比;hub 页允许被分装进多个 `.sn-body`(在小节之间插外壳层
  新模块),外壳补出来的配平标签夹在 `<!--hbf-->…<!--/hbf-->` 之间、比对前整段剔掉。
  三条 E:BODY_DIFF(字节不一致)· SPLIT_ON_PAGE(内容页出现多个 `.sn-body`)·
  TEXT_DIFF(可见文字缺词)。用法:`python3 .gates/check_snapshot.py --out out`。
