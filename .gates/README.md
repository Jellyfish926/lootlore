# .gates —— 站点门禁脚本(来自 seo-jianzhan/scripts,2026-09-03)

CI(`.github/workflows/gates.yml`)每次 push / PR 跑:构建 → check_config(Next 站)→ check_content → check_i18n(多语言站)→ check_sitemap → link_check;
红一条不许合。本地复现:同样的命令对 `out` 跑一遍。
每周一 `freshness.yml` 审计线上 sitemap 的 lastmod,过期页开 issue(label: freshness),只提醒不改内容。
改脚本请改 seo-jianzhan/scripts 的真相源再同步到各站,别只改这里。
