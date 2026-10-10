# Phasmophobia round2 复验（2026-10-10，UTC 13:0x，证据均为今天自取）

## 统计
- 复验对象：fix1.md 的 48 行（含 sourceUrls 新增行、自检配套行）+ 作者自加两处（roadmap 末格、author 字段标签）+ 复述抽查 5 处。
- 复验条数 55，通过 53，不通过 2（均为小问题，无需转 draft）。
- 机械检查：fix1 里每个「改后句」逐字 grep 都在对应文件里（0 缺失）；每个新增 sourceUrl 都写进了对应页的 frontmatter（0 缺失）。
- 新增/全部 71 个不同 sourceUrl：非 Steam 帖链接今天逐个 curl 全部 200；所有 Steam 帖 gid 在今天重取的 ISteamNews 返回里都存在。
- 引文覆盖：12 页所有 ≥25 字符的引号原话，今天都能在该页自己 sourceUrls 所列来源里找到（0 条缺口）；全量原话检索无编造引文（仅图注/图片文字/转录标签类未命中）。
- V-01：今天 appdetails 的 supported_languages 仍是 28 项（页面 28 正确）。
- V-02：今天 appreviews language=all 为 840,984 总数/793,555 好评（Very Positive，94.4%）；english 441,590；商店页 tooltip 为 "94% of the 360,079 user reviews in your language"、"89% of the 2,492 user reviews in the last 30 days"。页面写 840,982 / 360,078 / about 2,490，口径正确、数量级一致，句内已写 "these counts change daily"，通过。
- 作者自加两处：
  - roadmap 末格 "1.0 planned for the second half of 2027"：通过。6/24 Steam 帖原文 "we're making the decision to move the release of 1.0 to the second half of 2027"，该格只说 1.0，收窄后比原来更准；第 3 格引的 "1.0, Switch 2 and more" 是对六月图右下角 `2027 / 1.0 / SWITCH 2 AND MORE` 的转录（我看图核过），可接受。
  - author.md 标签改 "Last reviewed" / "Checked on version"：通过。我只读 lootlore 仓核实：`hub/shell.py` 的 byline() 106–116 行拼 By + t["reviewed"] + t["game_version"]；`config/i18n/en.json` 17 行 "Last reviewed"、18 行 "Checked on version"；`out/valheim/bonemass/index.html` 署名行为 `By Jellyfi · Last reviewed 2026-09-17 · Checked on version 1.0.12`；`hub/native.py` 305–306 行确实替换 {{BRAND}}。author.md 里已无 "Published / Last checked / Game version checked"。
- 复述抽查 5 处（15x 与 Apocalypse 年份、languages、reviews 数、"ran in 2026"/seven campaigns、cosmetics 说法）：description/tldr/FAQ/entities 均已同步（difficulty description、getting-started 卡片、entities 的 custom-difficulty/apocalypse/phasmophobia 实体、updates-events 的 "announced for 2026"、index 的 tldr 与 FAQ 两处 cosmetics 句）。无漏改。

## 不通过清单

| 编号 | 文件 | 现句 | 问题 | 证据 | 改成什么 |
|---|---|---|---|---|---|
| R2-01 | events.md | `\| October 8 to October 15, 11:59 PM BST (announced; still open on October 10) \| Crimson Eye tee \| 2 hours \|` | 括注 "still open on October 10" 把「announced」写成了「已开始」：10/1 公告只说 "live from the moment the event begins until 11:59 PM BST on October 15th"，10/7 之后没有任何官方帖确认活动已开始；与 entities.json crimson-eye-2026 的 `unverified_fields: ["started_in_game"]` 也自相矛盾，也违背 author.md 的「announced → ran 要有后续官方帖」规则 | Steam gid 1845383656381482（10/1）；ISteamNews 今天最新帖仍是 gid 1846018067925452（10/7 v0.19.1.0，称 "launching 8th October 2026"）；官网新闻列表最新为 10/6、10/1 | `October 8 to October 15, 11:59 PM BST (announced; scheduled to run from the start of the event until then)` |
| R2-02 | patch-notes.md（v0.19.1.0 已知问题一句）及 fix1 对 author.md 承诺的收窄 | `lampposts outside 6 Tanglewood Drive may glow`（页面所述已知问题，未带平台限定） | 页面引官网 v0.19.1.0 链接，但官网版写的是 "may glow when viewed by the player (XBOX & Steam only)"，Steam 帖版没有括注；页面既用到这一细节又丢掉平台限定，属于 author.md 自己承诺「用到的差异要写明」的范围，fix1 却把它排除在外 | 官网 `https://www.kineticgames.co.uk/news/phasmophobia-v01910-patch-notes`：「The lampposts outside of 6 Tanglewood Drive may glow when viewed by the player (XBOX & Steam only).」；Steam gid 1846018067925452：「…may glow when viewed by the player.」 | `lampposts outside 6 Tanglewood Drive may glow (the official-site version adds "XBOX & Steam only"; the Steam post omits that)` |

## 是否有页需要转 draft
无。两条不通过均为单句措辞，改完即可；author.md 的占位符与字段声明问题已按仓内证据解决，可放行。
