# Phasmophobia round2 修改记录（fix2）

- 对应清单：round2.md 的 R2-01、R2-02；「R2-01 同类」是按要求全栏目 grep 后一并统一成 announced / scheduled 口径的句子。
- 改前 / 改后由 raw/_tools/apply_fix2.py 逐字取出、逐字写回（替换前断言原句在文件里恰好出现 1 次）。表里的 `\|` 是 Markdown 表格转义，原文是 `|`。

| 编号 | 文件 | 改前句（逐字） | 改后句（逐字） | 处理方式 |
|---|---|---|---|---|
| R2-01 | events.md | \| October 8 to October 15, 11:59 PM BST (announced; still open on October 10) \| Crimson Eye tee \| 2 hours \| | \| October 8 to October 15, 11:59 PM BST (announced; scheduled to run from the start of the event until then) \| Crimson Eye tee \| 2 hours \| | 照改 |
| R2-02 | patch-notes.md | Two known issues are listed: lampposts outside 6 Tanglewood Drive may glow, and | Two known issues are listed: lampposts outside 6 Tanglewood Drive may glow (the official-site version adds "XBOX & Steam only"; the Steam post omits that), and | 照改 |
| R2-01 同类 | events.md | three are past and the fourth runs October 15 to 22. | three are past and the fourth is scheduled for October 15 to 22. | tldr 第 4 条：runs → is scheduled for |
| R2-01 同类 | events.md | \| Crimson Eye 2026 \| October 8 to November 1, 2026 \| Seasonal tee, | \| Crimson Eye 2026 \| October 8 to November 1, 2026 (announced) \| Seasonal tee, | 活动表：未获后续官方帖确认的一行标 announced |
| R2-01 同类 | events.md | For this month's event, see the dedicated | For the event announced for this month, see the dedicated | this month's event → the event announced for this month |
| R2-01 同类 | events.md | October 15 to 22, 2026, inside Crimson Eye. The developer calls these Double XP & Rewards. | The next announced window is October 15 to 22, 2026, inside the announced Crimson Eye dates. The developer calls these Double XP & Rewards. | Double XP 小节首句改成 announced 口径 |
| R2-01 同类 | events.md | \| October 15 to 22, 2026 \| Middle of Crimson Eye \| "all rewards from completed investigations" \| | \| October 15 to 22, 2026 (announced) \| Middle of the announced Crimson Eye dates \| "all rewards from completed investigations" \| | Double XP 表末行标 announced |
| R2-01 同类 | crimson-eye.md | description: "Phasmophobia Crimson Eye 2026 runs October 8 to November 1. Event locations, Blood Moon rewards, the Twitch Drop deadline, Double XP week and open questions." | description: "Phasmophobia Crimson Eye 2026 is announced for October 8 to November 1: locations, Blood Moon rewards, Twitch Drop deadline, Double XP dates, open questions." | description：runs → is announced for（其余压缩以守住 140–160 字符） |
| R2-01 同类 | crimson-eye.md | A Twitch Drop for the Crimson Eye tee runs until 11:59 PM BST on October 15; Double XP & Rewards runs October 15 to 22; Ghost Hunts 4 Hearts returns October 26 to November 1. | A Twitch Drop for the Crimson Eye tee is scheduled until 11:59 PM BST on October 15; Double XP & Rewards is scheduled for October 15 to 22; Ghost Hunts 4 Hearts is due back October 26 to November 1. | tldr 第 3 条：runs / returns → is scheduled / is due back |
| R2-01 同类 | crimson-eye.md | A Twitch Drop and a Double XP week run inside the event. | A Twitch Drop and a Double XP week are scheduled inside it. | 首段末句：run → are scheduled |
| R2-01 同类 | crimson-eye.md | \| Date (2026) \| What happens \| Source wording \| | \| Date (2026) \| What is scheduled \| Source wording \| | 日程表表头：What happens → What is scheduled |
| R2-01 同类 | crimson-eye.md | ## What else runs in Phasmophobia during the event? | ## What else is scheduled in Phasmophobia during the event? | H2：runs → is scheduled |
| R2-01 同类 | crimson-eye.md | it runs October 15 to 22, | it is scheduled for October 15 to 22, | runs → is scheduled for |
| R2-01 同类 | crimson-eye.md | If you only have one free week, that is the one where a contract pays twice. | If you only have one free week, that is the one where a contract is due to pay twice. | pays → is due to pay |
| R2-01 同类 | crimson-eye.md | In the final week the fundraiser with the American Heart Association returns. | In the final week the fundraiser with the American Heart Association is due to return. | returns → is due to return |
| R2-01 同类 | updates-events.md | \| Next Double XP \| October 15 to 22 \| | \| Next Double XP \| Announced for October 15 to 22 \| | 状态表：补 Announced for |

## 同步改动（不在 12 页正文里）

| 文件 | 改了什么 |
|---|---|
| entities.json（raw/_tools/gen_entities.py 重新生成） | `crimson-eye-2026.twitch_drop_en` 改为「Announced: Crimson Eye tee for two hours of Phasmophobia streams, scheduled from the start of the event until 11:59 PM BST on October 15, 2026」；`double_xp_en` 改为「Announced for October 15 to 22, 2026」；`drop-crimson-eye-tee` 新增 `status_en`（Announced on October 1, 2026; scheduled to run from the start of the event until 11:59 PM BST on October 15. No later official post confirms it has started.）并把 `unverified_fields` 设为 `["started"]`，与 crimson-eye-2026 的 `["started_in_game"]` 口径一致 |
| dossier.md（raw/_tools/facts.py 重新生成） | X6 改为「patch-notes 已括注两版差异」；新增 B57k（官网版带「(XBOX & Steam only)」的原句）。现 367 条事实、564 组比对全部命中 |
| README.md | 新增 4c 节 |

## 全栏目同类说法排查

`grep -n -i 'still open\|is live\|has started\|now live\|underway\|currently\|already started\|has begun\|kicked off\|ongoing\|right now\|in progress\|live now'` 扫 12 页与 entities.json：改后只剩 1 处命中，是 platforms-price 里的官方原话引文 "Currently we have no plans to be on Xbox Game Pass."，与活动状态无关。另外人工过了一遍所有带 October / Crimson Eye 的句子：index（tldr、正文、FAQ）、roadmap、patch-notes、updates-events 的 tldr 原本就是 "announced for" / "scheduled for" 口径，没有动。

## 改后自检（2026-10-10）

| 检查 | 结果 |
|---|---|
| check_content.py | 0 个问题。title 44–52、seoTitle 51–58、description 144–159 字符（crimson-eye 的新 description 157）；8 篇文章 1,204–1,488 词；文章与首页首段 53–60 词；「Phasmophobia」密度 1.06%–1.32%；每篇文章站内链接 ≥4 个不同目标、无死链；12 页封面互不相同 |
| check_facts.py | 564 组（事实, 来源）全部命中 |
| check_quotes.py | 226 条引文，212 条命中；未命中 14 条与上一轮相同（图片文字、站内标签与自述、V-05 带省略号的截引、引号配对假阳性）。本轮新增的引文 "XBOX & Steam only" 在官网 v0.19.1.0 页原文里命中 |
| check_source_coverage.py | 177 条有出处的引文，0 条缺口 |
