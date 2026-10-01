# verify-round2（取证 2026-10-01，只复验改动句）
| # | 项 | 新句位置 | 取证 | 结果 |
|---|---|---|---|---|
| R1 | updates.md 导语「in most weeks since」+ 第89行「From 7 to 29 September … every week; … quiet spells, such as 27 August to 7 September」 | updates.md:25,89 | 自己用 badges+passes+products 的 created 按周一起算周：9/7、9/14、9/21、9/28 周均有新建（9/7-9/10、9/17、9/21-9/24、9/29）；空周为 6/22、7/13、7/20、8/3、8/31，共 15 周中 10 周有新建=「most」成立；27 Aug→7 Sep 空档成立 | PASS |
| R2 | horses.md tldr/表格 | horses.md:12,45 | 改为「三个随机属性；稀有度跟随七档蛋」，与正文一致，且不再断言稀有度随机 | PASS |
| R3 | author.md「listed below」 | author.md:22 | lootlore/hub/native.py:1193-1200：type==author 时自动追加 `author_articles` 小节，列出同 category 且 author 名相同的文章卡片；文案句成立（前提：Guides 在 nav 里，Jellyfi 的 8 页满足过滤）。{{BRAND}} 由 native.py:305 / build.py:696 构建期替换 | PASS |
| U1 | eggs.md「At least one … fan site … still lists only six rarities」 | eggs.md:28 | race-horses.wiki 实测原文：「The official badges verify six tiers: Common, Uncommon, Rare, Epic, Legendary, and Mythic」，全站无 Exotic | PASS（建议补站名/链接，非必须） |
| U2 | horses.md「The fan sites we checked on 1 October 2026 did not cover it either」 | horses.md:37 | 已限定为「我们查过的」；racehorses.online、Destructoid 无 Index 内容 | PASS |
| U3 | eggs/horses/races/care-stable 的 scope 及 eggs tldr 「do not appear in … Roblox's public data / listing or store data」 | 各 scope、eggs.md:12 | 已限定在 Roblox 公开数据范围，API 内确无此类信息 | PASS |
| U4/U5 | races.md:79、gamepasses.md:40,70 | 同左 | 改成「开发者决定每次购买授予什么；时长未说明」，不再断言「one-off / per use」 | PASS |
| U6 | updates.md:93 | 同左 | 改成「Not as far as Roblox's data shows … 已删除条目不会出现在数据里」 | PASS |
| U7 | eggs.md:28 / index.md:80 | 同左 | 均改为「created」口径 | PASS |
| M5 | gamepasses.md:96「every 7 to 15 days」 | 同左 | 间隔 14/15/7/7 天 | PASS |
| M7 | updates.md:75「rowatcher.com listed the game under an earlier "[NEW🎉]" prefix」 | updates.md:75 | 我取 rowatcher.com/games/10387635049（原 /games/{placeId} 404，301 跳转）：title/og 均为「[INDEX📖] Race Horses Player Count…」，页内无任何「NEW」；站内搜索也未见。我能核到 [NEW🎉] 的是 https://www.rblxscripts.net/game/race-horses（标题「[NEW🎉] Race Horses Scripts」） | **仍需改** |
| G | guides.md:37「Covers the Exotic tier that other fan sites still miss.」 | guides.md:37 | 只证明 race-horses.wiki 一个站漏；racehorses.online 只列 3 档、Destructoid 无稀有度，但其余站未验 | **仍需改（轻）** |

## 仍需改
1. updates.md | 「A third-party tracker, rowatcher.com, listed the game under an earlier "[NEW🎉]" prefix when we searched on 1 October 2026.」→「A third-party scripts site, rblxscripts.net, listed the game as "[NEW🎉] Race Horses Scripts" when we checked on 1 October 2026.」 | https://www.rblxscripts.net/game/race-horses | rowatcher 当前页显示 [INDEX📖]，找不到 [NEW🎉]，无法核实；rblxscripts 才是实证来源（它是脚本站，不叫 tracker）。若作者另有 rowatcher 的快照/URL 证据，需给出具体 URL。
2. guides.md | 「Covers the Exotic tier that other fan sites still miss.」→「Covers the Exotic tier, which at least one fan site still leaves out.」 | https://race-horses.wiki | 与 eggs.md 的限定口径对齐，避免全称。
