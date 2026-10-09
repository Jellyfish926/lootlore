# American Plains Mudding 事实底稿（dossier）

取证日：2026-10-09。Roblox 接口第一批 11:12:57–11:13:00 UTC，补充批 11:13:23–11:13:31 UTC，活动历史 11:13:41–11:13:44 UTC，游戏页 HTML 11:13:56 UTC，图片验活 11:14 UTC，RSVP 与 games 接口复读 11:18 UTC（逐条时间见 `raw/fetch_log.txt`）。在线、访问、收藏、赞踩、徽章累计、群成员、RSVP 都是这一刻的快照。
**时点提醒**：官方活动「APM Map Update 🗺️」挂牌 2026-10-10 14:00 UTC 开始，即本次取数之后约 26 小时 47 分。本底稿与全部正文描述的是 **描述里写着「10/3 Update」的版本**；10-10 之后游戏名前缀、描述里的更新说明、活动列表都可能变（见 `todo-ingame.md`）。

范围：Roblox 体验 universeId 2783797267，rootPlaceId 7171174521，创作者群组 American Plains Mudding（groupId 4548068）。站内 slug `american-plains-mudding`；正文写 American Plains Mudding，官方自用缩写 APM（描述、徽章、通行证文本里都出现）。与总站已有的 `/southern-mudding/`（universe 8719555347，群组 33504096）是两款不同的游戏，本底稿没有任何一条事实取自它。

等级：**S** = 官方一手（Roblox 接口 / 官方页面原文 / Roblox 官方文档）；**A** = 开发者本人在官方渠道的原话（本轮 0 条：群组 shout 为 null、群组 wall 接口 404、社交链接接口 401、官方社区频道需登录未进）；**B** = 第三方 wiki / 媒体 / 第三方平台的公开数据；**C** = 视频评论 / 论坛帖（本轮未用）。
原始 JSON 全部在 `raw/`（不进仓）。本文件的数值行由 `scripts/make_dossier.py` 直接从 `raw/*.json` 生成，没有手抄。⏎ 表示原文换行，→ 表示原文制表符。


## 1. 游戏基本信息

| # | 事实 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|
| F1 | 正式名（API `name`）：`[🌲FOREST🌲] American Plains Mudding`；游戏页 `<title>` 为「American Plains Mudding \| Play on Roblox」，canonicalUrlPath `/games/7171174521/American-Plains-Mudding` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F2 | 创作者：群组 American Plains Mudding（id 4548068，type=Group，hasVerifiedBadge=true） | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F3 | created = 2021-07-29T15:11:10.903Z | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F4 | updated = 2026-10-07T00:05:33.298Z（11:12 与 11:18 两次读取同值；按 SKILL 口径不当作补丁日期） | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F5 | 类型：genre_l1 = Simulation，genre_l2 = Vehicle Sim（旧字段 genre = All） | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F6 | maxPlayers = 15 | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F7 | price = None（免费进入） | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F8 | visits = 714,911,302 | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F9 | playing = 6,750（11:18 复读为 6,987） | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F10 | favoritedCount = 8,238,764；favorites/count 接口 = 8,238,764 | https://games.roblox.com/v1/games?universeIds=2783797267 ; https://games.roblox.com/v1/games/2783797267/favorites/count | S | 2026-10-09 11:13 UTC |
| F11 | upVotes = 377,627，downVotes = 45,410（好评率 89.3%，我们计算：377627 ÷ 423037） | https://games.roblox.com/v1/games/votes?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F12 | universeAvatarType = MorphToR15；createVipServersAllowed = false（该字段不能用来判断私服是否开放，见 SKILL） | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F13 | 内容成熟度：Minimal；描述符 Suitable for everyone | https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation (POST, body {"universeId":"2783797267"}) | S | 2026-10-09 11:13 UTC |
| F14 | universe 内 place：1 个（7171174521） | https://develop.roblox.com/v1/universes/2783797267/places?limit=50 | S | 2026-10-09 11:13 UTC |
| F15 | 群组公开游戏列表里同一体验的 created = 2021-07-23T04:11:11.23Z、updated = 2026-10-03T13:43:26.317Z、placeVisits = 714,911,597（与 games v1 的 created 2021-07-29 不一致，见第 12 节） | https://games.roblox.com/v2/groups/4548068/games?accessFilter=Public&limit=50 | S | 2026-10-09 11:13 UTC |
| F16 | 宣传素材：10 张图 + 1 个预览视频（videoId 89700709995341，未下载未观看） | https://games.roblox.com/v2/games/2783797267/media | S | 2026-10-09 11:13 UTC |

## 2. 游戏描述全文（逐行，原样）

description 字段全文共 919 字符；下面每行是原文一行。

| # | 事实 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|
| F17 | `🚜 Pioneering vehicles, trailers, and customization on Roblox. We ain't corporate cash-grab; we’re a project built on faith, grit, and a love for the machine.` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F18 | `🚨 10/3 Update` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F19 | `- New ATV` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F20 | `→ - Animated Suspension` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F21 | `→ - Front and Rear Cargo Box Attachments` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F22 | `→ - Windshield Attachment` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F23 | `- New Forest (Map Update Part 1 of 2)` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F24 | `- Sitting In Vehicles Requires Being Whitelisted` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F25 | `- Bug Fixes (Water Flinging Fixed)` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F26 | `🌽 APM is a one-of-a-kind roleplay world built on your suggestions. We prioritize quality over quantity, pouring our hearts into every update to deliver the most advanced vehicles, trailers, and customization to Roblox. So grab your friends and take to the mud pits, test your skills with towing, or head to the fields for some farming - from boating and off-roading to creating your own unique builds and setups. We are pushing the boundaries of what's possible on Roblox.` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |
| F27 | `Like 👍 and Favorite ⭐ the game to obtain a vehicle!` | https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |

## 3. 通行证（game passes）

接口返回 14 条，nextPageToken 为空；8 条 isForSale=true，6 条 isForSale=false 且 price=null。旧接口 games.roblox.com/v1/games/2783797267/game-passes 返回 404。

| # | 事实 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|
| F28 | 通行证 `Premium Private Servers`（id 190773004）：195 Robux；isForSale=true；created 2023-06-16，updated 2026-08-22；描述原文：`Improve The Private Server Experience! ⏎  ⏎ Some of what is included: ⏎ - 2x Spawn Slots In Private Servers, Up To 16, All Admins In Your Server Have This Ability ⏎ - :weather storm 1, Spawns Tornadoes, Ranges From 1-10 ⏎ - :fly user, Fly Any User ⏎ - :admin user, Give Commands To Any User` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F29 | 通行证 `Premium Trailers`（id 193981735）：195 Robux；isForSale=true；created 2023-06-22，updated 2026-08-06；描述原文：`Get access to exclusive trailers! ⏎  ⏎ (Items within this gamepass are subject to change over time)` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F30 | 通行证 `Premium Vehicles`（id 21147957）：230 Robux；isForSale=true；created 2021-08-14，updated 2026-08-05；描述原文：`Get access to exclusive vehicles! ⏎  ⏎ (Items within this gamepass are subject to change over time)` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F31 | 通行证 `4 Trailer Spawner`（id 45354418）：290 Robux；isForSale=true；created 2022-05-17，updated 2026-08-05；描述原文：`Unlock the ability to spawn 4 trailers!` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F32 | 通行证 `Any Slot Spawner`（id 69232963）：290 Robux；isForSale=true；created 2022-08-04，updated 2026-08-14；描述原文：`Removes trailer and vehicle slot categories. So anything can be spawned in any of the 4-8 slots owned. E.g., all slots could be filled with vehicles, with a cap of 8 if 4 trailer and 4 vehicle spawner gamepasses are owned. (Formerly Premium Rigs)` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F33 | 通行证 `Anywhere Trailer Spawner`（id 45323541）：390 Robux；isForSale=true；created 2022-05-16，updated 2026-08-05；描述原文：`Allows you to spawn trailers from anywhere!` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F34 | 通行证 `Premium Customization`（id 1062063435）：390 Robux；isForSale=true；created 2025-02-10，updated 2026-08-08；描述原文：`Get exclusive access to premium customization features such as: ⏎  ⏎ - Ability To Customize Anywhere ⏎  ⏎ - Ability To Customize Attachments ⏎  ⏎ - Enhanced Window Customization ⏎  ⏎ - Enhanced Exhaust Customization ⏎  ⏎ - Exclusive Attachments ⏎  ⏎ This price will continue to rise as we add more content to the game pass. We have many things in store that will be added to this.` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F35 | 通行证 `4 Vehicle Spawner`（id 683417287）：490 Robux；isForSale=true；created 2024-01-06，updated 2026-08-06；描述原文：`Unlock the ability to spawn 4 vehicles!` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F36 | 通行证 `Donation`（id 20697357）：未在售（price=null）；isForSale=false；created 2021-08-03，updated 2026-08-05；描述原文：`Support APM and get a donor tag by your chats!` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F37 | 通行证 `2023 Halloween Vehicle`（id 630016063）：未在售（price=null）；isForSale=false；created 2023-10-19，updated 2026-08-06；描述原文：`First-ever limited vehicle! 2023 Limited Halloween Vehicle.` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F38 | 通行证 `Limited Christmas Vehicle`（id 672172947）：未在售（price=null）；isForSale=false；created 2023-12-14，updated 2026-08-06；描述原文：`Only available near Christmas. Get it while you can! (You will keep this vehicle forever)` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F39 | 通行证 `Limited Easter Vehicle`（id 757264124）：未在售（price=null）；isForSale=false；created 2024-03-25，updated 2026-08-07；描述原文：`Only available near Easter. Get it while you can! (You will keep this vehicle forever)` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F40 | 通行证 `Limited Halloween Vehicle`（id 1548634305）：未在售（price=null）；isForSale=false；created 2025-10-24，updated 2026-08-09；描述原文：`Only available near Halloween. Get it while you can! (You will keep this vehicle forever)` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F41 | 通行证 `Limited Thanksgiving Vehicle`（id 1603650412）：未在售（price=null）；isForSale=false；created 2025-11-27，updated 2026-08-10；描述原文：`Only available near Thanksgiving. Get it while you can! (You will keep this vehicle forever)` | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |
| F42 | 在售 8 个通行证价格合计 2,470 Robux（我们计算），最低 195，最高 490；priceDiscountDetails 全部为空 | https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |

## 4. 开发者商品（developer products）

接口返回 11 条，nextPageCursor = null；全部 IsForSale=true；名称全部以 `[GIFT] ` 开头。

| # | 事实 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|
| F43 | 商品 `[GIFT] Limited Christmas Vehicle`（DeveloperProductId 72004198）：110 Robux；IsForSale=true；Created 2025-12-12，Updated 2025-12-27；Description：`Only available near Christmas. Get it while you can! (You will keep this vehicle forever)` | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 | S | 2026-10-09 11:13 UTC |
| F44 | 商品 `[GIFT] Limited Thanksgiving Vehicle`（DeveloperProductId 71761264）：125 Robux；IsForSale=true；Created 2025-11-27，Updated 2025-12-27；Description：`Only available near Thanksgiving. Get it while you can! (You will keep this vehicle forever)` | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 | S | 2026-10-09 11:13 UTC |
| F45 | 商品 `[GIFT] Limited Halloween Vehicle`（DeveloperProductId 71182868）：145 Robux；IsForSale=true；Created 2025-10-25，Updated 2025-10-25；Description：`（空）` | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 | S | 2026-10-09 11:13 UTC |
| F46 | 商品 `[GIFT] Premium Trailers`（DeveloperProductId 61251516）：195 Robux；IsForSale=true；Created 2024-08-14，Updated 2025-11-01；Description：`（空）` | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 | S | 2026-10-09 11:13 UTC |
| F47 | 商品 `[GIFT] Premium Private Servers`（DeveloperProductId 69700358）：195 Robux；IsForSale=true；Created 2025-08-15，Updated 2026-08-29；Description：`（空）` | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 | S | 2026-10-09 11:13 UTC |
| F48 | 商品 `[GIFT] Premium Vehicles`（DeveloperProductId 61251553）：230 Robux；IsForSale=true；Created 2024-08-14，Updated 2026-08-29；Description：`（空）` | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 | S | 2026-10-09 11:13 UTC |
| F49 | 商品 `[GIFT] 4 Trailer Spawner`（DeveloperProductId 61251509）：290 Robux；IsForSale=true；Created 2024-08-14，Updated 2026-06-06；Description：`（空）` | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 | S | 2026-10-09 11:13 UTC |
| F50 | 商品 `[GIFT] Any Slot Spawner`（DeveloperProductId 61251525）：290 Robux；IsForSale=true；Created 2024-08-14，Updated 2026-08-29；Description：`（空）` | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 | S | 2026-10-09 11:13 UTC |
| F51 | 商品 `[GIFT] Anywhere Trailer Spawner`（DeveloperProductId 61251249）：390 Robux；IsForSale=true；Created 2024-08-14，Updated 2026-08-29；Description：`（空）` | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 | S | 2026-10-09 11:13 UTC |
| F52 | 商品 `[GIFT] Premium Customization`（DeveloperProductId 69700348）：390 Robux；IsForSale=true；Created 2025-08-15，Updated 2026-06-05；Description：`（空）` | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 | S | 2026-10-09 11:13 UTC |
| F53 | 商品 `[GIFT] 4 Vehicle Spawner`（DeveloperProductId 61251539）：490 Robux；IsForSale=true；Created 2024-08-14，Updated 2026-08-29；Description：`（空）` | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 | S | 2026-10-09 11:13 UTC |
| F54 | 11 个商品价格合计 2,850 Robux（我们计算）；8 个与在售通行证同名的礼物商品价格与对应通行证完全相同（我们逐一比对）；3 个节日限定车礼物商品 145 / 125 / 110 Robux，对应通行证当前未在售、无价格 | https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 ; https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 | S | 2026-10-09 11:13 UTC |

## 5. 徽章（badges）

接口返回 8 条，nextPageCursor = null；11:13:30 复取一次，id 列表一致，8 条 awardingUniverse.id 全部为 2783797267。4 个徽章同名 `Hidden Vehicle`（描述相同，id 不同）。

| # | 事实 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|
| F55 | 徽章 `Welcome to American Plains Mudding`（id 1123166882832107）：描述 `Thanks for playing American Plains Mudding!`；awardedCount 83,858,118；pastDayAwardedCount 61,198；winRatePercentage 0.295；created 2023-11-11T15:52Z，updated 2023-11-11T15:52Z；enabled=true；每 100 个 Welcome 徽章对应 100.00 个（我们计算） | https://badges.roblox.com/v1/universes/2783797267/badges?limit=100&sortOrder=Asc | S | 2026-10-09 11:13 UTC |
| F56 | 徽章 `Tornado Survivor`（id 3388542076656534）：描述 `Experienced a tornado in APM and lived to tell the tale! 🌪️`；awardedCount 2,684,652；pastDayAwardedCount 4,404；winRatePercentage 0.021；created 2025-07-19T04:33Z，updated 2026-08-04T02:12Z；enabled=true；每 100 个 Welcome 徽章对应 3.20 个（我们计算） | https://badges.roblox.com/v1/universes/2783797267/badges?limit=100&sortOrder=Asc | S | 2026-10-09 11:13 UTC |
| F57 | 徽章 `Hidden Vehicle`（id 607498769738490）：描述 `Congrats, you have found a Hidden Vehicle.`；awardedCount 2,450,309；pastDayAwardedCount 3,169；winRatePercentage 0.015；created 2023-12-30T17:34Z，updated 2025-10-23T00:50Z；enabled=true；每 100 个 Welcome 徽章对应 2.92 个（我们计算） | https://badges.roblox.com/v1/universes/2783797267/badges?limit=100&sortOrder=Asc | S | 2026-10-09 11:13 UTC |
| F58 | 徽章 `Hidden Vehicle`（id 314947669947351）：描述 `Congrats, you have found a Hidden Vehicle.`；awardedCount 1,316,036；pastDayAwardedCount 1,911；winRatePercentage 0.009；created 2024-03-08T04:10Z，updated 2025-10-23T00:49Z；enabled=true；每 100 个 Welcome 徽章对应 1.57 个（我们计算） | https://badges.roblox.com/v1/universes/2783797267/badges?limit=100&sortOrder=Asc | S | 2026-10-09 11:13 UTC |
| F59 | 徽章 `Hidden Vehicle`（id 1514979861516315）：描述 `Congrats, you have found a Hidden Vehicle.`；awardedCount 1,102,935；pastDayAwardedCount 2,352；winRatePercentage 0.011；created 2025-10-23T00:49Z，updated 2025-11-08T14:01Z；enabled=true；每 100 个 Welcome 徽章对应 1.32 个（我们计算） | https://badges.roblox.com/v1/universes/2783797267/badges?limit=100&sortOrder=Asc | S | 2026-10-09 11:13 UTC |
| F60 | 徽章 `Hidden Vehicle`（id 341545978270739）：描述 `Congrats, you have found a Hidden Vehicle.`；awardedCount 896,295；pastDayAwardedCount 1,437；winRatePercentage 0.007；created 2024-06-14T22:02Z，updated 2026-07-11T13:15Z；enabled=true；每 100 个 Welcome 徽章对应 1.07 个（我们计算） | https://badges.roblox.com/v1/universes/2783797267/badges?limit=100&sortOrder=Asc | S | 2026-10-09 11:13 UTC |
| F61 | 徽章 `Hidden Trailer`（id 3544618350782004）：描述 `Congrats, you have found a Hidden Trailer.`；awardedCount 647,691；pastDayAwardedCount 1,303；winRatePercentage 0.006；created 2025-12-10T19:55Z，updated 2026-07-11T13:15Z；enabled=true；每 100 个 Welcome 徽章对应 0.77 个（我们计算） | https://badges.roblox.com/v1/universes/2783797267/badges?limit=100&sortOrder=Asc | S | 2026-10-09 11:13 UTC |
| F62 | 徽章 `Met a Staff Member`（id 3227667483115084）：描述 `Congrats! You have met a staff member of APM!`；awardedCount 374,295；pastDayAwardedCount 0；winRatePercentage 0.0；created 2024-03-04T02:58Z，updated 2024-03-04T03:04Z；enabled=true；每 100 个 Welcome 徽章对应 0.45 个（我们计算） | https://badges.roblox.com/v1/universes/2783797267/badges?limit=100&sortOrder=Asc | S | 2026-10-09 11:13 UTC |
| F63 | 4 个 Hidden Vehicle 徽章累计合计 5,765,575、过去一天合计 8,869（我们计算；同一玩家可拿多个，不能当人数） | https://badges.roblox.com/v1/universes/2783797267/badges?limit=100&sortOrder=Asc | S | 2026-10-09 11:13 UTC |
| F64 | visits ÷ Welcome 徽章累计 = 8.53（我们计算）；Welcome 徽章 2023-11-11 才创建，晚于游戏创建 2 年多，所以徽章占比只覆盖该日期之后 | https://badges.roblox.com/v1/universes/2783797267/badges?limit=100&sortOrder=Asc ; https://games.roblox.com/v1/games?universeIds=2783797267 | S | 2026-10-09 11:13 UTC |

## 6. 群组

| # | 事实 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|
| F65 | 群组名 American Plains Mudding（id 4548068）；hasVerifiedBadge=true；publicEntryAllowed=true | https://groups.roblox.com/v1/groups/4548068 | S | 2026-10-09 11:13 UTC |
| F66 | memberCount = 3,699,198 | https://groups.roblox.com/v1/groups/4548068 | S | 2026-10-09 11:13 UTC |
| F67 | description 原文：`Welcome to the official American Plains Mudding group!` | https://groups.roblox.com/v1/groups/4548068 | S | 2026-10-09 11:13 UTC |
| F68 | shout = null（无 shout） | https://groups.roblox.com/v1/groups/4548068 | S | 2026-10-09 11:13 UTC |
| F69 | owner：Bebsharky（userId 292262212，hasVerifiedBadge=true）；该账号 created 2017-04-24，个人简介为空 | https://groups.roblox.com/v1/groups/4548068 ; https://users.roblox.com/v1/users/292262212 | S | 2026-10-09 11:13 UTC |
| F70 | 群组 created = 2018-11-23T15:00:56.167Z | https://groups.roblox.com/v2/groups?groupIds=4548068 | S | 2026-10-09 11:13 UTC |
| F71 | 角色与人数：Guest（rank 0）0；Member（rank 1）3,699,202；Member（rank 1）3,700,252；Notable Member（rank 5）10；Tester（rank 10）17；Head Tester（rank 15）1；Moderator（rank 20）4；Head Moderator（rank 25）1；Developer（rank 30）1；Head Developer（rank 35）1；Owner（rank 255）1 | https://groups.roblox.com/v1/groups/4548068/roles | S | 2026-10-09 11:13 UTC |
| F72 | 群组公开体验数：1（只有本作） | https://games.roblox.com/v2/groups/4548068/games?accessFilter=Public&limit=50 | S | 2026-10-09 11:13 UTC |
| F73 | 群组 featured event 接口返回 null | https://groups.roblox.com/v1/featured-content/event?groupId=4548068 | S | 2026-10-09 11:13 UTC |

## 7. 官方活动（virtual-events）

不带游标返回 3 条（当前 1 条 + 未开始 2 条）；带零起点游标分 3 页共 60 条（25 + 25 + 10）。60 条的 startUtc 全部落在周六（UTC）。eventStatus 60 条全是 active，不据此判断是否进行中。

| # | 事实 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|
| F74 | 活动 `Camper Update`（副标题 `This Weeks Update`，id 4982049383135314386）：start 2025-08-16T13:35Z，end 2025-08-23T12:30Z；描述原文：`Two new campers, gifting gamepass, and more!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F75 | 活动 `Tilt Deck Trailer Update`（副标题 `This Weeks Update`，id 2802779979928830411）：start 2025-08-23T13:35Z，end 2025-08-30T12:30Z；描述原文：`Enjoy the new tilt deck trailer!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F76 | 活动 `This Weeks Update`（副标题 `🔴Police Update🔵`，id 5465135976638317000）：start 2025-08-30T13:35Z，end 2025-09-06T12:35Z；描述原文：`Enjoy the new livery for all pickups, cars, and some premium vehicles/rigs. ⏎  ⏎ Also enjoy the new modern, vintage, dash, and visor light bars. ⏎  ⏎ Thank you all for the support!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F77 | 活动 `APM SUV Update`（副标题 `This Weeks Update`，id 616930290706416108）：start 2025-09-06T13:35Z，end 2025-09-13T10:15Z；描述原文：`Join the event to get notified right when the next update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F78 | 活动 `🔥SUV, Trailer Lights🔥`（副标题 `This Weeks Update`，id 6253569631953093143）：start 2025-09-13T13:35Z，end 2025-09-20T12:30Z；描述原文：`Enjoy the most recent update with a very highly requested SUV and advanced trailer lighting!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F79 | 活动 `APM ATV Update`（副标题 `This Weeks Update`，id 8195209086849778214）：start 2025-09-27T13:35Z，end 2025-10-04T12:30Z；描述原文：`New fully animated ATV and more!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F80 | 活动 `APM Update`（副标题 `This Week's Update`，id 9120605682834080342）：start 2025-10-04T13:35Z，end 2025-10-11T11:00Z；描述原文：`Get notified right when the next update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F81 | 活动 `APM Harvesting Update 🌾`（副标题 `This Week's Update`，id 2379724708137140847）：start 2025-10-11T13:35Z，end 2025-10-18T11:00Z；描述原文：`Massive harvesting update with a combine, draper head, header trailer, and more!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F82 | 活动 `[👻] APM Update`（副标题 `This Week's Update`，id 799713806790689368）：start 2025-10-25T13:35Z，end 2025-11-01T11:00Z；描述原文：`New Halloween vehicles. Fall Map. And more!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F83 | 活动 `APM Update`（副标题 `This Week's Update`，id 1174332378965607025）：start 2025-11-01T13:35Z，end 2025-11-08T12:00Z；描述原文：`New advanced gooseneck enclosed trailers!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F84 | 活动 `APM Update`（副标题 `This Week's Update`，id 1609276890784989796）：start 2025-11-08T14:35Z，end 2025-11-15T12:00Z；描述原文：`Complete Hitch Overhaul! New fifth wheel adapter for pickups. New gooseneck hitches for semi. Fifth wheels slide on semi now. All new models and so much more!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F85 | 活动 `APM Update`（副标题 `This Week's Update`，id 4297991654976783017）：start 2025-11-15T14:35Z，end 2025-11-22T12:00Z；描述原文：`New amphibious vehicles and 4WD!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F86 | 活动 `APM Update`（副标题 `This Week's Update`，id 2547051384780096069）：start 2025-11-22T14:35Z，end 2025-11-29T12:00Z；描述原文：`New dovetail trailer, console controls, and more!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F87 | 活动 `APM Update`（副标题 `This Week's Update`，id 2135757738229891704）：start 2025-11-29T14:35Z，end 2025-12-06T12:00Z；描述原文：`New pickup and topper, console controls, and more!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F88 | 活动 `APM Update`（副标题 `This Week's Update`，id 8660480128934740559）：start 2025-12-06T14:45Z，end 2025-12-13T12:00Z；描述原文：`Mudflaps, New Customization Store, And New Customization UI Out Now!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F89 | 活动 `APM Update`（副标题 `This Week's Update`，id 3825287191638835881）：start 2025-12-13T14:40Z，end 2025-12-20T12:00Z；描述原文：`Enjoy all the new content, features, and Christmas map!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F90 | 活动 `APM Update`（副标题 `This Week's Update`，id 2854481074430149325）：start 2025-12-20T14:40Z，end 2025-12-27T12:00Z；描述原文：`Pickup Tailgates, New Pickup, And More!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F91 | 活动 `APM Update`（副标题 `This Week's Update`，id 2131400558567490162）：start 2025-12-27T14:40Z，end 2026-01-03T12:00Z；描述原文：`Get notified right when the next update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F92 | 活动 `🔥APM Update🔥`（副标题 `This Week's Update`，id 4289001379344417436）：start 2026-01-03T14:40Z，end 2026-01-10T12:00Z；描述原文：`Get notified right when the next update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F93 | 活动 `☀️APM Update☀️`（副标题 `This Week's Update`，id 1440547991394714219）：start 2026-01-10T14:35Z，end 2026-01-17T12:00Z；描述原文：`New Lighting Revamp, New Pickup, New Lighting System, and more!☀️` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F94 | 活动 `🧂 APM Update🧂`（副标题 `This Week's Update`，id 2644140240897049227）：start 2026-01-17T14:45Z，end 2026-01-24T12:00Z；描述原文：`New salt spreader, snow plow, salt plant, and more!🧂🛣️` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F95 | 活动 `APM Update`（副标题 `This Week's Update`，id 7237429556716241468）：start 2026-01-24T14:35Z，end 2026-01-31T12:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F96 | 活动 `APM Update`（副标题 `This Week's Update`，id 553804564163986060）：start 2026-01-31T15:30Z，end 2026-02-07T12:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F97 | 活动 `APM Update`（副标题 `This Week's Update`，id 7828919099852587580）：start 2026-02-07T15:10Z，end 2026-02-14T12:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F98 | 活动 `APM Update`（副标题 `This Week's Update`，id 1237961045419229831）：start 2026-02-14T14:45Z，end 2026-02-21T12:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F99 | 活动 `APM Update`（副标题 `This Week's Update`，id 4990900334277427885）：start 2026-02-21T14:45Z，end 2026-02-28T12:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F100 | 活动 `APM Update`（副标题 `This Week's Update`，id 7797217016279728686）：start 2026-02-28T14:45Z，end 2026-03-07T12:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F101 | 活动 `APM Update`（副标题 `This Week's Update`，id 2482623608371544661）：start 2026-03-07T14:45Z，end 2026-03-14T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F102 | 活动 `APM Update`（副标题 `This Week's Update`，id 932498674246877818）：start 2026-03-14T14:15Z，end 2026-03-21T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F103 | 活动 `APM Update`（副标题 `Next Week's Update`，id 1906868545032159895）：start 2026-03-21T14:30Z，end 2026-03-28T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F104 | 活动 `APM Update`（副标题 `This Week's Update`，id 8812805008694313625）：start 2026-03-28T13:45Z，end 2026-04-04T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F105 | 活动 `APM Update`（副标题 `This Week's Update`，id 486171115073438330）：start 2026-04-04T13:45Z，end 2026-04-11T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F106 | 活动 `APM Update`（副标题 `This Week's Update`，id 1788752841842754101）：start 2026-04-11T13:45Z，end 2026-04-18T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F107 | 活动 `APM Update`（副标题 `This Week's Update`，id 7862834838846440089）：start 2026-04-18T14:50Z，end 2026-04-25T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F108 | 活动 `APM Update`（副标题 `This Week's Update`，id 4533123388742435416）：start 2026-04-25T14:15Z，end 2026-05-02T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F109 | 活动 `APM Update`（副标题 `This Week's Update`，id 6998533925115134584）：start 2026-05-02T13:45Z，end 2026-05-09T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F110 | 活动 `APM Update`（副标题 `This Week's Update`，id 6049901693364208217）：start 2026-05-09T13:55Z，end 2026-05-16T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F111 | 活动 `APM Update`（副标题 `This Week's Update`，id 8419391668880540313）：start 2026-05-16T13:50Z，end 2026-05-23T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F112 | 活动 `APM Update`（副标题 `This Week's Update`，id 4298705512398193239）：start 2026-05-23T13:50Z，end 2026-05-30T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F113 | 活动 `APM Update`（副标题 `This Week's Update`，id 4087018211827122843）：start 2026-05-30T14:00Z，end 2026-06-06T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F114 | 活动 `APM Update`（副标题 `This Week's Update`，id 7539938030602289804）：start 2026-06-06T13:50Z，end 2026-06-13T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F115 | 活动 `APM Update`（副标题 `This Week's Update`，id 3137342093509395024）：start 2026-06-13T14:00Z，end 2026-06-20T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F116 | 活动 `APM Update`（副标题 `This Week's Update`，id 1873374101469528655）：start 2026-06-20T13:50Z，end 2026-06-27T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F117 | 活动 `APM Update`（副标题 `This Week's Update`，id 6033548401885446755）：start 2026-06-27T15:05Z，end 2026-07-04T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F118 | 活动 `APM Update`（副标题 `This Week's Update`，id 6550750562122596953）：start 2026-07-04T13:45Z，end 2026-07-11T11:00Z；描述原文：`Get notified right when the update drops.` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F119 | 活动 `APM Update`（副标题 `This Week's Update`，id 1572054357720040204）：start 2026-07-11T13:45Z，end 2026-07-18T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F120 | 活动 `APM Update`（副标题 `This Week's Update`，id 1503875858836881971）：start 2026-07-18T14:15Z，end 2026-07-25T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F121 | 活动 `APM Update`（副标题 `This Week's Update`，id 1443130941898883690）：start 2026-07-25T14:10Z，end 2026-07-31T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F122 | 活动 `APM Update`（副标题 `This Week's Update`，id 163935200001262128）：start 2026-08-01T13:55Z，end 2026-08-08T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F123 | 活动 `🤠SHABOOZEY EVENT🤠`（副标题 `This Week's Update`，id 3866399056830005844）：start 2026-08-08T13:50Z，end 2026-08-15T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F124 | 活动 `APM Update`（副标题 `This Week's Update`，id 174719189041414794）：start 2026-08-15T13:45Z，end 2026-08-22T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F125 | 活动 `APM Update`（副标题 `This Week's Update`，id 7666976816644620960）：start 2026-08-22T13:50Z，end 2026-08-29T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F126 | 活动 `APM Update`（副标题 `This Week's Update`，id 4969597173802074699）：start 2026-08-29T17:00Z，end 2026-09-05T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F127 | 活动 `APM Update`（副标题 `This Week's Update`，id 133754157336232583）：start 2026-09-05T13:55Z，end 2026-09-12T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F128 | 活动 `APM Update`（副标题 `This Weeks Update`，id 2877123510046687887）：start 2026-09-12T13:45Z，end 2026-09-19T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F129 | 活动 `APM Dirtbikes 🏍️`（副标题 `This Weeks Update`，id 7624890202187760247）：start 2026-09-19T13:55Z，end 2026-09-26T11:00Z；描述原文：`Get notified right when the update drops!`；配图 mediaId 110368663107405 | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F130 | 活动 `APM Cowl Hoods Update`（副标题 `This Week's Update`，id 5972309176410571339）：start 2026-09-26T13:50Z，end 2026-10-03T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F131 | 活动 `APM Forest Update 🌲`（副标题 `This Weeks Update`，id 8210160679504708371）：start 2026-10-03T13:50Z，end 2026-10-10T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F132 | 活动 `APM Map Update 🗺️`（副标题 `Next Week's Update`，id 1153890537187705599）：start 2026-10-10T14:00Z，end 2026-10-17T11:00Z；描述原文：`Get notified right when the update drops!`；配图 mediaId 119697635046294 | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F133 | 活动 `APM Update`（副标题 `Next Next Week's Update`，id 4671235016800469657）：start 2026-10-17T13:45Z，end 2026-10-24T11:00Z；描述原文：`Get notified right when the update drops!` | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F134 | 活动 `APM Forest Update 🌲` RSVP：going 35,427，notGoing 2,514 | https://apis.roblox.com/virtual-events/v1/virtual-events/8210160679504708371/rsvps/counters | S | 2026-10-09 11:18 UTC |
| F135 | 活动 `APM Map Update 🗺️` RSVP：going 176,125，notGoing 18,836 | https://apis.roblox.com/virtual-events/v1/virtual-events/1153890537187705599/rsvps/counters | S | 2026-10-09 11:18 UTC |
| F136 | 活动 `APM Update（10-17）` RSVP：going 15,050，notGoing 662 | https://apis.roblox.com/virtual-events/v1/virtual-events/4671235016800469657/rsvps/counters | S | 2026-10-09 11:18 UTC |
| F137 | 60 条活动开始时刻分布（UTC，半小时桶，我们统计）：13:30 起 31 条；14:00 起 7 条；14:30 起 18 条；15:00 起 2 条；15:30 起 1 条；17:00 起 1 条 | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F138 | 60 条里两处隔了 14 天：2025-09-13 → 2025-09-27，2025-10-11 → 2025-10-25（2025-09-20 与 2025-10-18 两个周六没有挂牌）；其余相邻两条都隔 7 天（我们统计） | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F139 | 分时段的开始时刻（我们统计）：2025-08-16 至 2025-11-01 共 10 条全部 13:35 UTC；2025-11-08 至 2026-03-07 共 18 条在 14:35–15:30 UTC；2026-03-14 至 2026-10-17 共 32 条，其中 2026-03-28 起的 30 条有 27 条在 13:45–14:15 UTC（例外：04-18 14:50、06-27 15:05、08-29 17:00） | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |
| F140 | 标题统计（我们统计）：60 条里 44 条标题是 `APM Update`；描述 38 条是 `Get notified right when the update drops!`，3 条是 `Get notified right when the next update drops!`，1 条以句号结尾，1 条是 `Join the event to get notified right when the next update drops!`，其余 17 条写了具体内容 | https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-09 11:13 UTC |

## 8. 图片（官方缩略图）

逐个 curl 验 200 的记录在 `raw/image-check.txt`（23 个 URL 全部 200 image/Png）。画面描述是本人逐张看图写的，只用通用车型词。

| # | 事实 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|
| F141 | th1（imageId 127965895404466）：https://tr.rbxcdn.com/180DAY-31cf1860de3a53f27b0ca69ed541d818/768/432/Image/Png/noFilter ；画面：一个穿橙色反光背心的 Roblox 角色骑一辆红色四轮 ATV，前货架上绑着一把铲子；后面停一辆白色皮卡，尾门写 AMERICAN PLAINS FIRE，背景是松林 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=2783797267&countPerUniverse=10&size=768x432&format=Png | S | 2026-10-09 11:14 UTC |
| F142 | th2（imageId 101704244644678）：https://tr.rbxcdn.com/180DAY-9e2d8f7f776984546b289068c8b6c0ac/768/432/Image/Png/noFilter ；画面：两名 Roblox 骑手在空中做越野摩托特技，一红一蓝，下方是松树；同一张图也是活动「APM Dirtbikes 🏍️」的配图（mediaId 110368663107405，CDN 哈希相同） | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=2783797267&countPerUniverse=10&size=768x432&format=Png | S | 2026-10-09 11:14 UTC |
| F143 | th3（imageId 113361585184489）：https://tr.rbxcdn.com/180DAY-b41d1419ddb68faa72fdff97dfbdfaf6/768/432/Image/Png/noFilter ；画面：一辆蓝色并排座越野车（车门写 APM，车尾插美国国旗）腾空，后面一名骑手骑 ATV 跃起扬起泥土 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=2783797267&countPerUniverse=10&size=768x432&format=Png | S | 2026-10-09 11:14 UTC |
| F144 | th4（imageId 95246580298618）：https://tr.rbxcdn.com/180DAY-20fdfcf2e300e9fe4632022437d630d8/768/432/Image/Png/noFilter ；画面：一辆白色第五轮式房车拖挂（车头写 APM）停在木屋旁，侧面有伸缩舱与踏步 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=2783797267&countPerUniverse=10&size=768x432&format=Png | S | 2026-10-09 11:14 UTC |
| F145 | th5（imageId 93581475163489）：https://tr.rbxcdn.com/180DAY-1e10a55b419e1ce8e507583b36db8ef6/768/432/Image/Png/noFilter ；画面：一个戴焊接面罩的 Roblox 角色蹲在一辆深蓝色平板皮卡旁，货台上有一台蓝色焊机，写着 APM 2021；背景有风车与谷仓 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=2783797267&countPerUniverse=10&size=768x432&format=Png | S | 2026-10-09 11:14 UTC |
| F146 | th6（imageId 106819451759874）：https://tr.rbxcdn.com/180DAY-1ca411de4a972fa1339dd6c58bf2e4e5/768/432/Image/Png/noFilter ；画面：一辆红色高底盘皮卡背着大型露营车厢（车身写 AmericanPlains），停在草地小路上，背景是山 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=2783797267&countPerUniverse=10&size=768x432&format=Png | S | 2026-10-09 11:14 UTC |
| F147 | th7（imageId 103187397875783）：https://tr.rbxcdn.com/180DAY-27a8730ceb54fb5864e4b55e521cee6b/768/432/Image/Png/noFilter ；画面：一辆红色重型救援拖车伸出吊臂，把一台白色滑移装载机吊离地面，停车场摆着交通锥 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=2783797267&countPerUniverse=10&size=768x432&format=Png | S | 2026-10-09 11:14 UTC |
| F148 | th8（imageId 88898841472232）：https://tr.rbxcdn.com/180DAY-60554bfe6934c2a3fa5de9988b9d9f25/768/432/Image/Png/noFilter ；画面：一辆红色皮卡把拖车上的白色钓鱼艇倒进水里（船身写 APM），背景有美国国旗与风车 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=2783797267&countPerUniverse=10&size=768x432&format=Png | S | 2026-10-09 11:14 UTC |
| F149 | th9（imageId 111737831706271）：https://tr.rbxcdn.com/180DAY-16e834c2ee47200f10bae14f0d7ab67d/768/432/Image/Png/noFilter ；画面：暴雨中一辆黑色装甲车（车身写 APM 2021 与 American Plains）行驶在公路上，后方农用风车旁有一道龙卷风 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=2783797267&countPerUniverse=10&size=768x432&format=Png | S | 2026-10-09 11:14 UTC |
| F150 | th10（imageId 124873558179614）：https://tr.rbxcdn.com/180DAY-b1344a68e6bb78ed993f8ed504aeda38/768/432/Image/Png/noFilter ；画面：一台红色联合收割机装着宽幅割台（写 APM、2021），停在牛栏旁 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=2783797267&countPerUniverse=10&size=768x432&format=Png | S | 2026-10-09 11:14 UTC |
| F151 | ev_map（活动「APM Map Update 🗺️」配图，mediaId 119697635046294）：https://tr.rbxcdn.com/180DAY-d8db7d543bf08e1377bfe24226e6ddd5/768/432/Image/Png/noFilter ；画面：小镇主街，两侧是砖房店面与行道树，路上有老式轿车和皮卡，背景是松林山坡 | https://thumbnails.roblox.com/v1/assets?assetIds=119697635046294,110368663107405&size=768x432&format=Png | S | 2026-10-09 11:14 UTC |
| F152 | icon（512x512）：https://tr.rbxcdn.com/180DAY-349b9f539333d0e440cf334a58ec345a/512/512/Image/Png/noFilter ；画面：星条旗花纹的 APM 三个字母，下方一个穿反光背心的 Roblox 角色骑带挡风玻璃的红色 ATV | https://thumbnails.roblox.com/v1/games/icons?universeIds=2783797267&size=512x512&format=Png | S | 2026-10-09 11:14 UTC |

## 9. Roblox 官方文档原文（平台机制只引原文）

| # | 事实 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|
| F153 | 原文：`Passes let you charge users a one-time Robux fee to access special privileges inside your game, such as entry to a restricted area, an in-game avatar item, or a permanent power-up.` | https://create.roblox.com/docs/production/monetization/passes | S | 2026-10-09 11:17–11:21 UTC |
| F154 | 原文：`A developer product is an item or ability that a user can purchase more than once, such as in-game currency, ammo, or potions.` | https://create.roblox.com/docs/production/monetization/developer-products | S | 2026-10-09 11:17–11:21 UTC |
| F155 | 原文：`A badge is a special award you can gift players when they meet a goal within your game, such as completing a difficult objective or playing for a certain amount of time.` | https://create.roblox.com/docs/production/publishing/badges | S | 2026-10-09 11:17–11:21 UTC |
| F156 | 原文：`A private server is a subscription-based feature that allows a player to decide who can play a game with them. While private servers can be free, you can also use private servers as a method of monetization by charging players who want to access private servers a monthly Robux fee.` | https://create.roblox.com/docs/production/monetization/private-servers | S | 2026-10-09 11:17–11:21 UTC |
| F157 | 原文：`Players can discover your events on the experience's detail page and through an event details page, and they can opt into notifications that they'll receive when your event begins.` | https://create.roblox.com/docs/production/promotion/experience-events | S | 2026-10-09 11:17–11:21 UTC |
| F158 | 原文：`Social media links are only visible to users who have verified their age as at least 16 years old.` | https://create.roblox.com/docs/production/promotion/social-media-links | S | 2026-10-09 11:17–11:21 UTC |
| F159 | 原文：`When you publish an updated version of a game to Roblox, players aren't immediately removed from old versions of the game. … If you don't restart servers, players transition to the new version of the game as the servers running old versions eventually empty and shut down.` | https://create.roblox.com/docs/projects/update-games | S | 2026-10-09 11:17–11:21 UTC |

## 10. 第三方来源（只作线索 / 需求证据，不进正文事实）

| # | 事实 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|
| F160 | 试过一个未经官方证实的邀请线索，未采用、不记录 | （不记录） | B | 2026-10-09 11:17 UTC |
| F161 | americanplainsmudding.wiki：sitemap 84 条 URL（en / zh / ja 各 28 条）；首页写「619M+ Visits、6.9M+ Favorites」，文章日期 2026-07-23，最新更新条目是「July 18」；codes 页称截至 2026-07-23 未见官方兑换码系统（与我们 10-09 读到的描述一致：描述里没有码） | https://americanplainsmudding.wiki/sitemap.xml | B | 2026-10-09 11:14–11:15 UTC |
| F162 | plainsmudding.wiki：sitemap 7 条 URL（首页、/vehicles、/sources、3 个法务页、/corrections）；sources 页外链 games API 与一个 /games/7171174521/welding-rigs-american-plains-mudding 形式的游戏页地址 | https://plainsmudding.wiki/sitemap.xml | B | 2026-10-09 11:14–11:15 UTC |
| F163 | Google 下拉（suggestqueries，hl=en gl=us，30 组前缀，全部 200，无验证码）：头部词 discord / roblox / script / hidden vehicle / update / codes / commands / next update；原始返回在 raw/suggest.jsonl | https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=american+plains+mudding | B | 2026-10-09 11:16 UTC |
| F164 | Fandom：american-plains-mudding / americanplainsmudding / apm / american-plains-mudding-roblox 四个子域 api.php 全部 404（这四个子域下没有 wiki；不能证明别的子域也没有，页面只写「We found no official wiki」） | https://american-plains-mudding.fandom.com/api.php | B | 2026-10-09 11:14 UTC |

## 11. 未获取项

| 项 | 结果 | 原因 / 处理 |
|---|---|---|
| 游戏社交链接（Discord / X / YouTube） | 未获取 | `games.roblox.com/v1/games/2783797267/social-links/list` 返回 401 "Authentication token is missing"；游戏页 HTML（匿名）里没有任何 discord / x.com / youtube 外链。Roblox 文档原文：社交链接只对验证年龄 ≥16 的用户可见 |
| 群组社交链接 | 未获取 | `groups.roblox.com/v1/groups/4548068/social-links` 返回 401 |
| 群组 wall | 未获取 | v1 与 v2 的 `wall/posts` 都返回 404（原因不明，不归因为需登录） |
| 群组 shout | 接口返回 null | 没有 shout，不是取数失败 |
| 更新日志（除描述里的 10/3 一段） | 未获取 | 游戏页匿名 HTML 没有更新日志区块；描述只保留最近一次更新说明；旧描述在公开接口里没有存档。活动 listing 保留了 60 条标题，其中 17 条写了具体内容 |
| 官方兑换码 | 0 个 | 游戏描述、群组描述里都没有码；shout 为 null。不建 codes 页 |
| 旧通行证接口 | 404 | 改用新接口取到 14 条 |
| place 详情（支持设备等） | 未获取 | `multiget-place-details` 返回 401 |
| 私服是否开放、价格 | 未获取 | `createVipServersAllowed=false` 不能作判据；游戏页匿名 HTML 的 `data-can-create-server="False"` 是匿名访客状态，也不能作判据。通行证「Premium Private Servers」的存在说明游戏里有私服这回事，价格与创建方法未获取 |
| 4 个 Hidden Vehicle / 1 个 Hidden Trailer 的位置与是什么车 | 未获取 | 徽章只有名称、一句描述与计数；位置只有社区视频（未读取、未核实） |
| 免费车（Like + Favorite）是哪辆、怎么领 | 未获取 | 描述只有一句话 |
| 「Sitting In Vehicles Requires Being Whitelisted」怎么操作 | 未获取 | 描述只有这一行 |
| 游戏内货币、车辆价格与解锁条件、地图地点名、操作键位 | 未获取 | 公开接口里没有 |
| Premium Vehicles / Premium Trailers 包含哪些车 | 未获取 | 通行证描述只写「exclusive vehicles / trailers」且「subject to change over time」 |
| Premium Private Servers 的完整命令表、命令在哪里输入 | 未获取 | 通行证描述写「Some of what is included」，只列了 3 条命令 |
| 5 个节日限定车通行证的在售价与今年是否返场 | 未获取 | 当前 isForSale=false、price=null；描述只写「Only available near …」 |
| 预览视频内容 | 未观看 | media 接口列出 1 个 GamePreviewVideo，未下载 |
| 搜索量 / KD | 未获取（自动任务不查 Semrush） | 需求证据只有 Google 下拉 |
| 游戏内实测 | 未做 | 没有进游戏；所有「画面长什么样」的描述都来自官方宣传图并注明 |

## 12. 互相矛盾 / 需要谨慎的地方

| 项 | 值 A | 值 B | 处理 |
|---|---|---|---|
| 体验创建时间 | games v1 `created` = 2021-07-29T15:11:10.903Z | 群组游戏列表 v2 `created` = 2021-07-23T04:11:11.23Z | 正文以 games v1 的 2021-07-29 为主（任务书给定的也是这个日期），community 页并列写出两个值，不解释成因；不写「发售日」 |
| 最近更新时间 | games v1 `updated` = 2026-10-07T00:05:33.298Z | 群组游戏列表 v2 `updated` = 2026-10-03T13:43:26.317Z | 两个都不当补丁日期写；正文用描述里的「10/3 Update」+ 活动 listing 的 2026-10-03 13:50 UTC。v2 的 10-03 13:43 只在底稿里记一笔 |
| 群组人数 | group.json memberCount 3,699,198 | roles 接口两个 Member 角色 3,699,202 / 3,700,252 | 取数相隔约 24 秒且口径不同；正文只用 group 接口的 3,699,198 |
| 节日限定车礼物商品 IsForSale=true | 对应通行证 isForSale=false | — | 接口标记不等于游戏内商店此刻在卖；正文写「接口标记在售，是否能在游戏里买到未核实」 |
| 默认生成上限 | 官方原文只有「4-8 slots owned」「cap of 8 if 4 trailer and 4 vehicle spawner gamepasses are owned」 | 默认分配、单买一个生成通行证后的槽数：原文没有写，也推不出来（round1 对抗验证：首稿的默认分配推导不成立，已删） | 正文只写「4 到 8」与「两个生成通行证都有时封顶 8」；其余一律写 not stated，不算每槽单价 |
| 活动开始时刻 = 更新上线时刻？ | listing 的 startUtc | 实际上线时刻未知 | 正文一律写 listed start，不写成上线时刻 |
| 徽章占比 | 以 Welcome 徽章累计为分母 | Welcome 徽章 2023-11-11 才创建；各徽章创建日不同 | 正文注明是「每 100 个 Welcome 徽章对应多少个」，不是概率，也不是人数占比 |
| 「SHABOOZEY EVENT」是什么 | 活动标题原文 `🤠SHABOOZEY EVENT🤠`（2026-08-08） | 描述只有通用一句 | 只照抄标题，不解释、不写联动对象 |

