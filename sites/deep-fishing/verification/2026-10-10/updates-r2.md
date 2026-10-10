# updates 页终稿第二轮核验（r2）

62 条命题（表中 62 行），1 条被推翻，1 条未验（第 57 条）。取证时间 2026-10-10 00:27–00:31 UTC，自己重取全部接口（游戏、98 商品、9 通行证、13 徽章、活动 20 次轮询、群、votes），旧值只对仓内 HEAD 版 shop.md、gamepasses.md、badges.md 与 entities.json。
活动轮询：8 条 14 次、1 条 6 次（那 1 条是 EGGS & PETS are COMING!）。
对全部记录的 created / updated 重做 2026-09-28 之后的清单（商品 Created、Updated；通行证、徽章、游戏、活动的 created / updated / 起止）：时间线表无漏行、无错行。

## 命题表

| 编号 | 命题 | 验证路径 | 结果 | 证据 |
|---|---|---|---|---|
| 1 | 9 条商品记录创建于 29 Sep–9 Oct 2026 | developerproducts | CONFIRMED | Season Pass、Skip 1、Skip 10、Reset Season、3 个 Leviathan、Shop Daily Claimable Ad、Oni Soulbinder Skin = 9 |
| 2 | 10 月 10 日商品列表 98 条 | 同上 | CONFIRMED | len = 98，nextPageCursor null |
| 3 | 89 + 9 = 98 | 自己重算 | CONFIRMED | 98 |
| 4 | 本站 9 月 29 日读数为 89（shop.md "89 of them when we checked"，checkedAt 2026-09-29） | HEAD:shop.md 第 27 行 | CONFIRMED | 逐字有 |
| 5 | Season Pass 399、Skip 1 79、Skip 10 449、Reset Season 19 | developerproducts | CONFIRMED | PriceInRobux 一致 |
| 6 | Oni Soulbinder Skin 1,649；Season Pass 399 | 同上 | CONFIRMED | 1649；399 |
| 7 | 九个通行证、13 个徽章 | game-passes、badges | CONFIRMED | 9 / 13 |
| 8 | 本站 9 月 29 日也记九个通行证、13 个徽章 | HEAD:gamepasses.md 第 25 行；badges.md 第 4 行 | CONFIRMED | "nine game passes"；"All 13 Deep Fishing Badges" |
| 9 | 无通行证或徽章记录的创建日期晚于 1 Aug 2026 | game-passes、badges | CONFIRMED | 通行证最晚 2026-07-19；徽章最晚 2026-08-01T20:55（仍是 1 Aug） |
| 10 | 九个通行证的编辑日期均 ≥ 29 Sep | game-passes | CONFIRMED | 八个 2026-09-29T20:23:xx，Double Coins 2026-10-07T12:44 |
| 11 | 游戏记录 updated = 9 Oct 2026 18:38 UTC，created = 18 July 2026 | games | CONFIRMED | updated 2026-10-09T18:38:20.186Z；created 2026-07-18T22:34:37.651Z |
| 12 | 游戏记录携带两个时间戳（created、updated） | games | CONFIRMED | 另有 visits 等计数字段，但时间戳字段就这两个 |
| 13 | EGGS & PETS are COMING! 窗口 11 Oct 16:00–15 Oct 16:00 | virtual-events | CONFIRMED | 2026-10-11T16:00:27Z – 2026-10-15T16:00:27Z |
| 14 | 首段：没有通行证 / 徽章记录创建于这段时间（与第 9 条同） | 同上 | CONFIRMED | 同第 9 条 |
| 15 | 时间线 27 Sep 16:00–28 Sep 16:00 Fish Update + Rework 窗口 | virtual-events | CONFIRMED | 2026-09-27T16:00:55Z – 09-28T16:00:55Z |
| 16 | 29 Sep 20:06–20:26：19 个旧商品与 8 个通行证被编辑 | developerproducts、game-passes | CONFIRMED | 商品 Updated 20:06:06 至 20:26:08（共 19），通行证 20:23:11–20:23:42（8） |
| 17 | 19 个商品 = Starter Pack + 4 个 Server Luck + 5 个 Coin Pack + 9 个 [Gift] | 同上 | CONFIRMED | 1+4+5+9 = 19，名称逐个对上 |
| 18 | 29 Sep 21:26–21:31 创建四个季节商品 | 同上 | CONFIRMED | 21:26:15、21:27:22、21:27:45、21:31:13 |
| 19 | 30 Sep 05:37–05:38 创建三个 Leviathan；05:39 三个均被编辑 | 同上 | CONFIRMED | 创建 05:37:59、05:38:13、05:38:34；编辑 05:39:36、05:39:41、05:39:45 |
| 20 | 30 Sep 15:27 创建 Shop Daily Claimable Ad | 同上 | CONFIRMED | 15:27:24 |
| 21 | 4 Oct 14:00 EGGS 列表创建 | virtual-events | CONFIRMED | createdUtc 2026-10-04T14:00:46Z |
| 22 | 4 Oct 16:00–8 Oct 16:00 NEW WORLD 窗口 | 同上 | CONFIRMED | 见上 |
| 23 | 4 Oct 16:14–16:15 Skip 1、Skip 10 被编辑 | developerproducts | CONFIRMED | 16:14:51、16:15:02 |
| 24 | 7 Oct 12:44 Double Coins 被编辑 | game-passes | CONFIRMED | 2026-10-07T12:44:26Z |
| 25 | 9 Oct 18:38 游戏 updated | games | CONFIRMED | 同第 11 条 |
| 26 | 9 Oct 23:53 Oni 创建、Shop Daily Claimable Ad 被编辑 | developerproducts | CONFIRMED | 23:53:12；23:53:38 |
| 27 | 表中没有漏行（2026-09-28 之后的 created / updated / 活动起止全覆盖） | 全部接口重扫 | CONFIRMED | 另查：NEW WORLD 的 updated 在 27 Sep（窗外）；EGGS updated 与 created 同在 4 Oct 14:00；其它活动 updated 均早于 28 Sep；徽章最晚编辑 5 Aug |
| 28 | 五个商品表（Leviathan ×3、Shop Daily Ad、Oni）价格 149 / 399 / 1,199 / 29 / 1,649 | developerproducts | CONFIRMED | 一致 |
| 29 | 五个商品创建 / 编辑时间（表格） | 同上 | CONFIRMED | x1：05:37→05:39；x3：05:38→05:39；x10：05:38→05:39；Shop Daily：15:27→9 Oct 23:53；Oni：23:53 且未编辑（Updated = Created） |
| 30 | 五个商品描述为空、IsForSale 均为 true | 同上 | CONFIRMED | |
| 31 | 399 ÷ 3 = 133.0；1,199 ÷ 10 = 119.9；单个 149 | 自己重算 | CONFIRMED | 133.0；119.9 |
| 32 | "[Skin] Divine King Rod" 与 "[Skin] Divine Queen Rod" 是此前仅有的两个带 [Skin] 的商品，Oni 名字不含 Rod | developerproducts | CONFIRMED | 仅这两个 [Skin] |
| 33 | 季节组四个商品"created within five minutes" | 同上 | CONFIRMED | 21:26:15 到 21:31:13 = 4 分 58 秒 |
| 34 | 季节组表格 Edited：Skip 1 4 Oct 16:14、Skip 10 4 Oct 16:15，Season Pass、Reset Season 未编辑 | 同上 | CONFIRMED | |
| 35 | 四个商品描述为空 | 同上 | CONFIRMED | |
| 36 | "season" 只出现在两个商品名（Season Pass、Reset Season），不在通行证 / 徽章 / 活动 / 游戏描述 | 六个响应全字符串搜 | CONFIRMED | 命中仅 dp.json 的这两条 |
| 37 | 449 ÷ 79 ≈ 5.68，约 5.7 倍 | 自己重算 | CONFIRMED | 5.683 |
| 38 | Season Pass 是商品、不在九个通行证内 | game-passes | CONFIRMED | 九个通行证名单中无 |
| 39 | 商品记录"有空描述"（Season Pass） | developerproducts | CONFIRMED | |
| 40 | 通行证编辑：八个 29 Sep 20:23、Double Coins 7 Oct 12:44 | game-passes | CONFIRMED | |
| 41 | Double Coins 现描述 "Earn 2x more coins when selling fish! 🪙" | game-passes | CONFIRMED | 逐字 |
| 42 | 本站 9 月 29 日数据 "Earn 2x more coins! 🪙"；旧价 399 | HEAD:gamepasses.md 第 40 行；entities.json 第 1022 行 | CONFIRMED | gamepasses.md 表格 399 / "Earn 2x more coins!"；entities.json "Earn 2x more coins! 🪙" |
| 43 | Double Coins 现价 399 | game-passes | CONFIRMED | |
| 44 | 与本站 9 月 29 日读数相比，九个通行证价格相同 | HEAD:gamepasses.md | CONFIRMED | 旧表 99/149/249/249/249/349/399/599/99 与现价逐个相同 |
| 45 | 同期九个 [Gift] 商品价格与旧页相同 | HEAD:gamepasses.md 第 68–75 行 | CONFIRMED | 99 ×2、149、249 ×3、349、399、599 对上 |
| 46 | Starter Pack 与 4 个 Server Luck 价格相同 | HEAD:shop.md 第 85、89 行 | CONFIRMED | 旧页 "x2 99, x4 249, x8 599, x16 999"、"Starter Pack 99" |
| 47 | "Those older pages print no prices for the five Coin Packs, so we have no earlier figure for them." | HEAD:shop.md 第 86 行 | REFUTED | 反例：旧页 shop.md（HEAD）第 86 行 "Coins \| Small 39, Medium 99, Big 249, Huge 599, Giant 1,649"，与 10 月 10 日现价（39 / 99 / 249 / 599 / 1649）逐个相同。连带："the same for … 14 of the 19 products" 与实际不符，旧页有记录的是 19 / 19 |
| 48 | Welcome! 徽章 29 Sep 为 2,104,103 | HEAD:badges.md 第 32、36 行 | CONFIRMED | |
| 49 | Welcome! 徽章 10 Oct 为 3,034,384 | badges | CONFIRMED | 我取到 3,035,608，差 0.04%，在 2% 内 |
| 50 | 无徽章的创建或编辑日期晚于 5 Aug 2026 | badges | CONFIRMED | 最晚 updated 2026-08-05T13:51:57 |
| 51 | NEW WORLD IS COMING 副标题 "🌋The Emberdeep"，标语逐字 "Deep Fishing expands with a brand new Volcano World, 30 fish, boats, daily rewards, and much more." | virtual-events | CONFIRMED | |
| 52 | Fish Update + Rework 副标题 "48 Fish, Many Rods & more" | 同上 | CONFIRMED | |
| 53 | 三条活动的列表创建日：19 Sep、26 Sep、4 Oct；NEW WORLD 上次编辑 27 Sep（开窗前一周） | 同上 | CONFIRMED | 09-19T16:47、09-26T21:41、10-04T14:00；updated 09-27T13:16 |
| 54 | 商品名不含 "Emberdeep"、"Volcano"、"boat" | developerproducts | CONFIRMED | 三词仅出现在活动文字 |
| 55 | 另五条活动列表（Update 3 起至 Toxic + Kraken）；Mutation Roll + Rarity💫 是八条里唯一描述为完整更新清单的 | virtual-events | CONFIRMED | 其余七条描述为空或一句话 |
| 56 | Oni 23:53 比 18:38 晚 5 小时 15 分；Skip 编辑在 NEW WORLD 开窗 16:00 之后 15 分钟内 | 自己重算 | CONFIRMED | 5:15；16:15:02 − 16:00:03 = 14 分 59 秒 |
| 57 | "The endpoints do not show deleted products / deleted records"（出现两处） | 接口响应 | UNVERIFIED | 响应里没有任何关于已删除记录是否显示的字段或说明，无法用这些接口证实或证伪 |
| 58 | 商品、通行证、徽章列表各一次响应返回完整、无后续页 | 各接口 | CONFIRMED | nextPageCursor null / nextPageToken "" |
| 59 | 活动接口读法不一致（8 条或未结束那 1 条） | 20 次轮询 | CONFIRMED | 见上 |
| 60 | 5 条名称含大小写 / 表情符号：EGGS & PETS are COMING!、Update 3 👀、Toxic + Kraken 🐙☢️、Mutation Roll + Rarity💫、Double Coins 等 | 各接口 | CONFIRMED | 逐字一致 |
| 61 | 更新页没有把创建 / 编辑时间写成功能上线时间，没有把活动列表写成已上线更新 | 通读 | CONFIRMED | 正文反复限定 "a record date … does not say when a feature reached players"；events 一节写 "describes a plan" |
| 62 | description / tldr 里 "nine added store products" | developerproducts | CONFIRMED | 9 条创建记录；其「已上线」含义在正文限定为记录 |


## 机检
① 正文外链 0 个；sourceUrls 五个地址我逐个 curl，全部 200，均为 Roblox 官方接口。
② 站内链接目标：badges、codes、enchants、gamepasses、rods、shop（related 为 shop、gamepasses、badges），全部在白名单内，无 waters。
③ 无日期的 now / currently / upcoming / soon / latest / recently：0 处（"new" 仅在 NEW WORLD 等标题中，"Still not confirmed" 为小标，非时间副词）。
其它观察：正文图 art01 而 _images.json pages 映射与 frontmatter 为 art04。
