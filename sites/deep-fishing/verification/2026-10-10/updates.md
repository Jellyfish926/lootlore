# updates 页核验（lootwiki.com/deep-fishing/updates/ 草稿）

41 条命题，2 条被推翻，7 条未验（U35–U41）。

取证：全部由核验方 2026-10-10 00:14–00:18 UTC 重新取得，存于 b2/v/（未采信 b2/raw）。URL 简写同 codes 页（G / DP / GP / BD / EV）。EV 轮询 44 次，最多 8 条（出现 40 次），1 条出现 4 次，明细见 verify/events-poll.log 与 codes.md。

## 命题表
| 编号 | 命题 | 验证路径 | 结果 | 证据 | 取证时间(UTC) |
|---|---|---|---|---|---|
| U1 | 商品共 98 个，一页取完 | DP | CONFIRMED | developerProducts 长 98，无 nextPageCursor | 00:14:13 |
| U2 | 创建日 ≥ 2026-09-28 的商品恰好 9 个：Season Pass、Skip 1、Skip 10、Reset Season、x1/x3/x10 Leviathan Bottle(s)、Shop Daily Claimable Ad、Oni Soulbinder Skin | DP | CONFIRMED | 下标 89–97 共 9 条，其余 89 条 Created 均早于 2026-09-29 | 00:14:13 |
| U3 | Season Pass 399，29 Sep 21:26 创建，未编辑 | DP | CONFIRMED | Created = Updated = 2026-09-29T21:26:15.844Z | 00:14:13 |
| U4 | Skip 1 79，创建 29 Sep 21:27，编辑 4 Oct 16:14 | DP | CONFIRMED | Created 2026-09-29T21:27:22.524Z；Updated 2026-10-04T16:14:51.498Z | 00:14:13 |
| U5 | Skip 10 449，创建 29 Sep 21:27，编辑 4 Oct 16:15 | DP | CONFIRMED | Created 2026-09-29T21:27:45.724Z；Updated 2026-10-04T16:15:02.298Z | 00:14:13 |
| U6 | Reset Season 19，创建 29 Sep 21:31，未编辑 | DP | CONFIRMED | Created = Updated = 2026-09-29T21:31:13.312Z | 00:14:13 |
| U7 | 四个赛季商品「在五分钟内」创建（21:26 到 21:31） | DP | CONFIRMED | 21:26:15.844 到 21:31:13.312 = 4 分 57.5 秒 | 00:14:13 |
| U8 | x1 / x3 / x10 Leviathan 价格 149 / 399 / 1,199；创建 05:37、05:38、05:38；编辑均 05:39 | DP | CONFIRMED | Created 05:37:59 / 05:38:13 / 05:38:34；Updated 05:39:36 / 05:39:41 / 05:39:45（2026-09-30） | 00:14:13 |
| U9 | Shop Daily Claimable Ad 29，创建 30 Sep 15:27，编辑 9 Oct 23:53 | DP | CONFIRMED | Created 2026-09-30T15:27:24.246Z；Updated 2026-10-09T23:53:38.941Z | 00:14:13 |
| U10 | Oni Soulbinder Skin 1,649，创建 9 Oct 23:53，未编辑，名称无 Rod，上架 | DP | CONFIRMED | Created = Updated = 2026-10-09T23:53:12.663Z；IsForSale true | 00:14:13 |
| U11 | 这 9 个商品描述字段全空、全部在售 | DP | CONFIRMED | Description 均 ""；IsForSale 均 true | 00:14:13 |
| U12 | 「两个更早的皮肤商品」名为 [Skin] Divine King Rod、[Skin] Divine Queen Rod | DP | CONFIRMED | 名称逐字一致 | 00:14:13 |
| U13 | 29 Sep 被编辑的 19 个旧商品 = Starter Pack + Server Luck ×4 + Coin Pack ×5 + [Gift] ×9，编辑时间 20:06–20:26 | DP | CONFIRMED | 筛 Updated ≥ 09-28 且 Created < 09-28 恰 19 条，Updated 2026-09-29T20:06:06 至 20:26:08 | 00:14:13 |
| U14 | 9 个通行证；8 个编辑时间为 29 Sep 20:23；Double Coins 为 7 Oct 12:44 | GP | CONFIRMED | 9 条；8 条 updated 2026-09-29T20:23:11–20:23:42；Double Coins 2026-10-07T12:44:26.091Z；9 条 updated 均 ≥ 29 Sep | 00:14:13 |
| U15 | Double Coins 现描述「Earn 2x more coins when selling fish! 🪙」，价格 399 | GP | CONFIRMED | displayDescription 逐字一致，price 399 | 00:14:13 |
| U16 | 徽章 13 个，一页取完；最晚创建/编辑 2026-08-05 | BD | CONFIRMED | data 长 13，nextPageCursor 空；最晚 updated 2026-08-05T13:51:57.238Z；最晚 created 2026-08-01T20:55:36Z | 00:14:15 |
| U17 | Welcome! 徽章获得数超过 303 万 | BD | CONFIRMED | awardedCount 3,034,946 | 00:14:15 |
| U18 | 游戏记录 updated 为 9 Oct 18:38 | G | CONFIRMED | updated 2026-10-09T18:38:20.186Z | 00:14:10 |
| U19 | Fish Update + Rework：窗口 27 Sep 16:00 到 28 Sep 16:00，列表创建于 19 Sep，副标题「48 Fish, Many Rods & more」 | EV | CONFIRMED | 2026-09-27T16:00:55.323 → 2026-09-28T16:00:55.323；createdUtc 2026-09-19T16:47:00；subtitle 逐字一致 | 00:14:28 |
| U20 | NEW WORLD IS COMING：窗口 4 Oct 16:00 到 8 Oct 16:00，创建 26 Sep，最后编辑 27 Sep，副标题「🌋The Emberdeep」，tagline 逐字 | EV | CONFIRMED | 2026-10-04T16:00:03 → 10-08T16:00:03；createdUtc 2026-09-26T21:41:59；updatedUtc 2026-09-27T13:16:58；subtitle / tagline 一致 | 00:14:28 |
| U21 | EGGS & PETS are COMING!：窗口 11 Oct 16:00 到 15 Oct 16:00，列表创建 4 Oct（14:00） | EV | CONFIRMED | 2026-10-11T16:00:27 → 10-15T16:00:27；createdUtc 2026-10-04T14:00:46 | 00:14:28 |
| U22 | 活动共 8 条；更早 5 条为 Update 3 👀（8 月）…Toxic + Kraken 🐙☢️（9 月）；仅 Mutation Roll + Rarity💫 的 description 是完整变更清单 | EV | CONFIRMED | 8 条；Update 3 窗口 2026-08-23；Toxic 2026-09-20；仅 Mutation 条 974 字符 26 个 "- " 行 | 00:14:28 |
| U23 | 前两个活动窗口在读取日已关闭，第三个未开始 | EV | CONFIRMED | 10-08 与 09-28 均早于 10-10；10-11 晚于 10-10 | 00:14:28 |
| U24 | 「season」一词在读取的记录中只出现在 Season Pass 与 Reset Season 两个商品名里（无通行证、徽章、活动、游戏描述） | G GR EV GP DP BD | CONFIRMED | 全响应检索：DP 2 条商品名（各 3 个重复字段），其余 0 | 00:14:40 |
| U25 | 商品名里没有 Emberdeep / Volcano / boat | DP | CONFIRMED | 三词在 DP 命中 0；仅 EV 副标题与 tagline 含 | 00:14:40 |
| U26 | Season Pass 在开发者商品里，不在 9 个通行证里 | DP GP | CONFIRMED | DP[89]；GP 9 个名字无 Season Pass | 00:14:13 |
| U27 | 推导：89 + 9 = 98 | DP | CONFIRMED | 9 条 Created ≥ 09-29；其余 89；合计 98 | 00:14:13 |
| U28 | 推导：399/3 = 133.0；1,199/10 = 119.9；449/79 ≈ 5.68 | DP | CONFIRMED | 133.0；119.9；5.6835 | 00:14:13 |
| U29 | 推导：Oni 创建 23:53 比游戏 updated 18:38 晚 5 小时 15 分 | DP G | CONFIRMED | 23:53:12 − 18:38:20 = 5:14:52 | 00:14:13 |
| U30 | Skip 1 / Skip 10 编辑发生在 NEW WORLD 开始（16:00）之后 15 分钟内 | DP EV | CONFIRMED | 16:15:02.298 − 16:00:03.218 = 14 分 59 秒 | 00:14:13 |
| U31 | NEW WORLD 最后编辑「比窗口早一周」；EGGS 创建「比窗口早一周」 | EV | CONFIRMED | 27 Sep 13:16 → 4 Oct 16:00 = 7 天 2 小时 43 分；4 Oct 14:00 → 11 Oct 16:00 = 7 天 2 小时（"a week" 为近似说法，非精确七天） | 00:14:28 |
| U32 | 没有新增通行证或徽章 | GP BD | CONFIRMED | 通行证 created 最晚 2026-07-19；徽章 created 最晚 2026-08-01；无 created ≥ 09-28 | 00:14:15 |
| U33 | 页面正文「The table puts every dated record from that window in order」（第一张时间线表） | DP EV GP | REFUTED | 反例：Leviathan 三个商品的编辑时间 2026-09-30T05:39:36 / 05:39:41 / 05:39:45 在窗口内，是带日期的记录，该表 30 Sep 行只写「created」，没有 05:39 编辑行（后文第二张表才出现） | 00:14:13 |
| U34 | 页面称「The game's 'updated' timestamp … is the one timestamp on the game record itself」 | G | REFUTED | 反例：同一游戏记录还有 created: 2026-07-18T22:34:37.651Z；按字面「唯一时间戳」不成立 | 00:14:10 |
| U35 | 「We counted 89 developer products on 29 September」 | — | UNVERIFIED | 29 日的计数来自仓内旧页，不在允许来源。现状仅能说：今天接口里 Created 早于 29 Sep 21:26 的商品为 89 个，未排除期间有已删除商品 | — |
| U36 | 19 个商品与 9 个通行证价格与 29 Sep 所读的商店页、通行证页相同 | — | UNVERIFIED | 旧价格在仓内页面，不在允许来源，未取证；今天价格见 U13、U14 | — |
| U37 | Double Coins 29 日描述为「Earn 2x more coins! 🪙」，价格当天 399 | — | UNVERIFIED | 接口只回当前文本，无历史；旧文本在仓内数据 | — |
| U38 | 「No game pass or badge was … removed」「same counts we recorded on 29 September」 | — | UNVERIFIED | 删除无法从当前接口观测，29 日计数不在允许来源 | — |
| U39 | 「The award counts keep climbing」 | BD | UNVERIFIED | 只有一个时间点的计数（Welcome! 3,034,946），无对比数据 | — |
| U40 | 「Season Pass is not among the passes, which is why the game pass guide does not include it」（因果，指向本站另一页） | — | UNVERIFIED | 后半句涉及本站 gamepasses 页的内容与原因，非 Roblox 官方来源 | — |
| U41 | 「Everything here was read … shortly after 00:00 UTC」（写手读取时刻）及图片 art01 的描述 | — | UNVERIFIED | 写手读取时刻无法由接口复核（核验方读取为 00:14–00:18 UTC，接口数据与页面一致）；图片不在允许取证范围 | — |

## 机检
1. 正文外链：0 个（只有站内链接与图片 key art01）。sourceUrls 5 个地址 curl 均 200（games、developer-products、game-passes、badges、virtual-events，00:14–00:18 UTC），均出现在 sourceUrls 内。
2. 站内链接目标：shop、gamepasses、rods、enchants、badges、codes，全部在允许 slug 内，没有 waters 或其他。
3. 无日期限定的 now / currently / upcoming / soon / latest / recently：0 处（grep 仅命中 NEW / new，位于活动标题「NEW WORLD IS COMING」等引文内）。
4. 活动提醒：接口不稳定，见 codes.md 的轮询结果；页面写的「some reads eight, others only the one」已复现（44 次中 4 次只回 1 条）。
