# One Tap 第二轮复验 round2（2026-10-10，证据均为今天重新取得）

## 统计
- 复验条数：fix1.md 第二节 80 行（逐行 grep 改后句：80/80 逐字出现在对应文件里，0 缺失），另加 battle-pass.md 整页重读、U15/U19/entities/复述漏改四项专项。
- 通过 77 行；不通过 3 项（均为小问题，见下）。无 REFUTED，无新数字/新引文错误。
- 是否有页需转 draft：否。

## 专项结论
1. 改后句事实核对：U1（HTML data-private-server-price="49" 与 game API createVipServersAllowed:false 并列，今天复现）、U13、U12（今天放大看图：左侧 o 被裁、右侧 cases 末个 s 被裁一半，句号不可见，与改后句一致）、U14（Karambit 记录 28 Jan，距 13 Mar 约 6 周；12 Mar 18:18 与 24 Apr 03:00 UTC 创建、listing 起始 13 Mar 12:10 / 24 Apr 16:00，成立）、U16、U17（roles 接口有 Guest 与 Cool People）、U20（POST get-age-recommendation 返回 Mild/Violence (Repeated/Mild)，游戏页 HTML 无该值）均成立；文档引句仍逐字存在。
2. battle-pass.md 整页：title/seoTitle/description/tldr/H2/表格/Read next 现在核心是「接口里有什么名字、价格、日期」。每层单价表表头、引导句、表后句、tldr 均挂了「按名称里的层数相除、记录不确认功能」的前提，表不再误导，无需删表。表内数值重算无误（20/20/59.7/85；60 vs 179；200 vs 850；600÷20=30；850−600=250；449+600=1,049）。仅剩预设性措辞见 N1。
3. U15 事实：virtual-events 今天取到 Revert createdUtc 2026-08-09T13:18:17Z、eventTime.start 13:20:15Z（约 1 分 58 秒）；Game Revert createdUtc 2026-08-15T05:18:17Z、start 05:20:28Z（约 2 分 11 秒）；"about two minutes" 成立。6 条里最晚 start 为 2026-08-15，之后无 listing，成立。"4 of 6 创建早于开始 2 周以上"、Summer 创建 5 Apr 成立。
4. U2 删句：两页确已无 8/8 时点句，只留 maxPlayers 8（成立）。U19：lootlore 仓核实——hub/native.py 第 306 行 .replace("{{BRAND}}", self.cfg["brand"])，config/hub.json brand=LootWiki；第 1217–1224 行 author 分支用 author_articles（en.json "Guides by {name}"）追加文章卡片；out/blockspin/author/index.html 里 {{BRAND}} 0 次、有 "Guides by Jellyfi"。U19 不改成立。
5. entities.json：今天重取 97 商品 + 4 通行证，101 条 name/price/product_id/developer_product_id/pass_id/创建与更新日期全部逐字一致，0 处不符；Skip/Premium Battlepass/Xp Boost 的 shop_group 标签与 key_notes 已改为名称口径，unverified_fields 含 function。
6. 复述漏改抽查（index、shop、robux、updates、beginner、author、cases、gamepasses、rewards）：tier skips / battle pass products / skips tiers / Xp Boost timers 在这些页已全部改为 named / products 口径，只剩 N2 一处。

## 不通过清单
编号 | 文件 | 现句 | 问题 | 证据 | 改成什么

N1 | battle-pass.md（低，可选）| "3. Check how long the season has left. No listing gives an end date for a season." / "- Whether Premium Battlepass covers one season or carries over." / "- What earns battle pass progress: kills, quests, XP or something else." / "1. Open the battle pass screen and count the tiers." | 这几句仍预设「有一个正在运行的赛季、有进度、有游戏内 battle pass 界面」；官方只有两条 listing 行与商品名，没有任何一手文本说明当前有赛季或进度机制。 | listing 原文只有 "New Battlepass season" / "New BP Season"；7 条商品 Description 全空（今天重取）。 | 3 → "3. If the game shows a season, check how long it has left. No listing gives an end date for a season."；carries over → "- Whether Premium Battlepass, if it is a season purchase, covers one season or carries over."；progress → "- Whether there is battle pass progress, and if so what earns it: kills, quests, XP or something else."；1 → "1. If the game has a battle pass screen, count the tiers on it. No official source we read gives that number."

N2 | rewards.md 第 78 行 | "| 2x Level XP pass | 149 | Not a timer; a one-time pass |" | 反向把 Xp Boost 默认成「计时器」，与 U10 已收紧的口径（时长只来自名称）不一致。 | 4 条 Xp Boost 记录 Description 为空。 | "| 2x Level XP pass | 149 | A pass, paid once; no time in the name |"

N3 | updates.md 第 127 行 | "So some listings have been visible well ahead of their start date." | 用 createdUtc 推「可见」；创建时间不等于公开可见时间。 | virtual-events 只给 createdUtc/updatedUtc，没有公开时间字段（eventVisibility 现为 public，只是当前值）。 | "So some listing records existed well ahead of their start date; the records do not show when each one became visible."

## 是否转 draft
无。battle-pass.md 经改写后核心是名称与价格，价格/日期全部与接口一致，N1 处理后更稳；其余页不需转 draft。
