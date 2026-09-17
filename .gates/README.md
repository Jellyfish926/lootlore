# .gates —— 站点门禁脚本(来自 seo-jianzhan/scripts,2026-09-03)

CI(`.github/workflows/gates.yml`)每次 push / PR 跑:构建 → check_config(Next 站)→ check_content → check_i18n(多语言站)→ check_sitemap → link_check;
红一条不许合。本地复现:同样的命令对 `out` 跑一遍。
每周一 `freshness.yml` 审计线上 sitemap 的 lastmod,过期页开 issue(label: freshness),只提醒不改内容。
改脚本请改 seo-jianzhan/scripts 的真相源再同步到各站,别只改这里。

lootlore 本地增补(2026-09-17,待同步回 seo-jianzhan/scripts):
- `check_content.py --dir-lang valheim=zh`:整个游戏目录是单一非主语种(无语种子目录)时,LANG_ATTR 按声明语种判,不再误报。
- `tech_audit.py`(由 seo-jianzhan/scripts/tech-audit.py 复制):加 `--out/--base/--prefix/--summary` 命令行;title/description 按显示宽度(CJK 记 2);正文词数按「拉丁词 + CJK/2」;外部热链 og:image 不按本地文件查。只报告不阻塞。
