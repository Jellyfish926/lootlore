# Southern Mudding 事实底稿（dossier）

取证日：2026-10-02。接口第一批 11:19:18–11:19:21 UTC，群组/复查批 11:20:05–11:20:10 UTC，活动 RSVP 11:23:54–11:23:55 UTC（各文件时间见 `raw/` 的 mtime；`raw/fetch_time.txt` 记第一批起点）。在线人数、访问量、徽章累计数、RSVP 等快照型数字只代表这一刻。
**注意时点**：官方活动「This Week's Update!」排在 2026-10-02 17:00:46 UTC 开始，也就是本次取数之后约 5 小时 40 分。本底稿与全部正文描述的是 **9 月 25 日版本（Nitrous 更新）在 10 月 2 日更新落地前的状态**。10-02 更新后游戏名前缀、描述里的更新说明、商品列表都可能变，见 `todo.md` 第 1 条。

范围：Roblox 体验，universeId 8719555347，rootPlaceId 79480724066456。
**正式名以官方 API `name` 为准：`[🚀Nitrous!🚀] Southern Mudding 🚜 OffRoading`**；canonicalUrlPath `/games/79480724066456/Southern-Mudding-OffRoading`；描述自称「Southern Mudding」，并自用缩写「SM」。站内 slug `southern-mudding`，正文写 Southern Mudding。名称前缀随每周更新变，不写进 title。

原始抓取文件：`raw/`（games.json / votes.json / badges.json / badges_recheck.json / passes.json / devprod_p1.json / virtual_events.json / event_*_rsvp.json / media.json / places.json / age.json / group.json / group_games.json / group_roles.json / thumbs_768.json / thumbs_480.json / icons.json / event_thumb.json / wall.json / group_social.json / game_social.json / place_details.json / img/ / suggest.txt / comp/）。`raw/` 不进仓。

来源分级（按本轮任务口径）：**S** = 官方接口 / 官方页面原文（Roblox API 返回的、开发者自己登记的数据）；**A** = 开发者官方渠道原话（Discord 公告、群组 wall、X）——**本轮无**：群组 wall 接口返回错误、群组与游戏 social-links 接口要登录、Discord / X 要登录，全部记「未获取」；**B** = 可信二手；**C** = 第三方专站 / 视频转述（southernmudding.wiki、southernmudding.site 只看了栏目结构，**没有任何一条事实取自它们**）。

来源缩写（全部 S）：
- G = https://games.roblox.com/v1/games?universeIds=8719555347
- V = https://games.roblox.com/v1/games/votes?universeIds=8719555347
- BD = https://badges.roblox.com/v1/universes/8719555347/badges?limit=100
- GP = https://apis.roblox.com/game-passes/v1/universes/8719555347/game-passes?passView=Full&pageSize=100
- DP = https://apis.roblox.com/developer-products/v2/universes/8719555347/developerproducts?limit=100
- EV = https://apis.roblox.com/virtual-events/v1/universes/8719555347/virtual-events （不带参数只返回当前 3 条）
- EVH = https://apis.roblox.com/virtual-events/v1/universes/8719555347/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA （从头翻页，2 页共 43 条；第 2 轮新增）
- DOC1–DOC7 = Roblox 官方文档（见第 13 节；第 2 轮新增）
- RS = https://apis.roblox.com/virtual-events/v1/virtual-events/<eventId>/rsvps/counters
- GR = https://groups.roblox.com/v1/groups/33504096
- RO = https://groups.roblox.com/v1/groups/33504096/roles
- GG = https://games.roblox.com/v2/groups/33504096/games?accessFilter=Public&limit=50
- AG = https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation （POST，body `{"universeId":"8719555347"}`）
- PL = https://develop.roblox.com/v1/universes/8719555347/places?limit=50
- MD = https://games.roblox.com/v2/games/8719555347/media
- TH = https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=8719555347&countPerUniverse=10&size=768x432&format=Png
- IC = https://thumbnails.roblox.com/v1/games/icons?universeIds=8719555347&size=512x512&format=Png

## 1. 基本信息

| # | 事实 | 值 | 来源 | 取数（UTC） | 级 |
|---|---|---|---|---|---|
| F1 | 正式名 | `[🚀Nitrous!🚀] Southern Mudding 🚜 OffRoading` | G `name` | 10-02 11:19 | S |
| F2 | 创作者 | 群组 Southern Mudding（groupId 33504096），type=Group，hasVerifiedBadge=true | G `creator` | 10-02 11:19 | S |
| F3 | 创建时间 | 2025-09-15T04:28:37.477Z | G `created` | 10-02 11:19 | S |
| F4 | 最近更新 | 2026-09-25T17:20:11.671Z | G `updated` | 10-02 11:19 | S |
| F5 | 类型 | genre_l1 = Simulation，genre_l2 = Vehicle Sim（旧字段 genre = All） | G | 10-02 11:19 | S |
| F6 | 单服人数上限 | 10 | G `maxPlayers` | 10-02 11:19 | S |
| F7 | 价格 | 免费（price = null） | G | 10-02 11:19 | S |
| F8 | 私服 | 未开放（createVipServersAllowed = false） | G | 10-02 11:19 | S |
| F9 | 访问量（快照） | 428,075,692 | G `visits` | 10-02 11:19 | S |
| F10 | 在线（快照） | 14,526 | G `playing` | 10-02 11:19 | S |
| F11 | 收藏（快照） | 625,025 | G `favoritedCount` | 10-02 11:19 | S |
| F12 | 点赞 / 点踩（快照） | 221,349 / 17,627（好评率 92.6%，我们计算：221349 ÷ 238976） | V | 10-02 11:19 | S |
| F13 | 内容成熟度 | Minimal；描述符 Suitable for everyone | AG | 10-02 11:19 | S |
| F14 | universe 内 place | 1 个（根 place 79480724066456） | PL | 10-02 11:19 | S |
| F15 | 头像类型 | MorphToR15 | G `universeAvatarType` | 10-02 11:19 | S |
| F16 | 宣传素材 | 7 张图，0 个视频 | MD | 10-02 11:19 | S |
| F17 | 宣传图画面（只写进 alt / 图注，且写明是宣传图） | th1 红色皮卡爬泥坡、后面一辆红色敞篷越野车；th2 两名戴头盔骑手骑四轮沙滩车过睡莲池、岸上停红色皮卡；th3 红色皮卡货斗里装一辆蓝色四轮沙滩车；th4 红色多轴重型罐车过泥坑；th5 红色皮卡用多轴拖车把一艘四台舷外机的快艇倒进水里；th6 骑手骑越野摩托翘头；th7 骑手开六轮沙滩车过泥沟、后面停一辆房车 | TH 图片本身（已逐张看图，存 `raw/img/`） | 10-02 11:19 | S |
| F18 | 支持设备 | **未获取**（描述没写；place-details 接口 401） | — | — | — |

## 2. 官方描述原文（G `description`，S，10-02 11:19）

逐句拆开。「可以写的」是正文允许的表述上限。

| # | 原文（逐字） | 可以写的 |
|---|---|---|
| F20 | "Welcome to Southern Mudding! Explore a map purpose built for the off-road, using your selection of pickup trucks, semi trucks, trailers, classic cars, American muscle cars, and more!" | 有一张为越野造的地图；车辆类别：pickup trucks、semi trucks、trailers、classic cars、American muscle cars。**地图地点名、区域数官方没写 → 未获取** |
| F21 | "Whether you're here to off-road, play with friends, roleplay, or customize your vehicles, there's something for everyone!" | 四种玩法取向：越野、和朋友玩、角色扮演、改装 |
| F22 | "🚨 September 25th Update" | 当前版本说明标题是 9 月 25 日更新 |
| F23 | "- New Nitrous Customization for Pickup Trucks! Add it in the customization garage." | 氮气是一种改装项，对象是 Pickup Trucks，在 customization garage 里加。**怎么触发、是否收费、持续多久、其他车型能不能装 → 未获取** |
| F24 | "- New Pickup Truck!" | 9-25 新增一辆皮卡。**具体名称、获取方式 → 未获取** |
| F25 | "- New UTV!" | 9-25 新增一辆 UTV。**同上** |
| F26 | "- New LED Whip Lights!" | 9-25 新增 LED Whip Lights。**安装位置与价格 → 未获取** |
| F27 | "🚜 SM is built around depth, realism, and steady improvement. We focus on delivering vehicles that feel right, customization that matters, and updates that add real gameplay — not just surface changes." | 开发者自述的方向；自用缩写 SM |
| F28 | "From heavy towing and deep mud runs to hauling, boating, and dialing in your perfect truck setup, everything is designed to work together." | 官方点名的活动：heavy towing、deep mud runs、hauling、boating、truck setup |
| F29 | "We plan our updates entirely around your suggestions and value the community." | 更新按玩家建议规划（官方自述） |
| F30 | "👍⭐ Thumbs up if you like the game and want new updates!" | — |
| F31 | "❗Updates every Friday!" | 每周五更新（官方原话） |
| F32 | 描述里没有任何兑换码、没有 Discord / 社媒链接 | 无码；无链接 |

## 3. 徽章（4 个，全部官方）

来源 BD（S）。nextPageCursor = null。11:20:09 UTC 重取一次（`raw/badges_recheck.json`，带 sortOrder=Asc），4 个 id、名称、描述一致，awardingUniverse.id 全部 = 8719555347（排除串号坑）。下表数字取第一次（11:19:19）。「每 100 个 Welcome」= 该徽章累计 ÷ Welcome to the game! 累计 × 100，我们计算；比的是徽章总数，不是同一批玩家。`winRatePercentage` 是接口原值，正文按「×100 = 百分比」读并注明是 Roblox 自己给的数。

| # | 徽章 `name`（逐字） | 官方 `description`（逐字） | 累计 awardedCount | 过去一天 | winRatePercentage | 每 100 个 Welcome | created | badge id |
|---|---|---|---|---|---|---|---|---|
| F40 | Welcome to the game! | You played the game! | 76,022,926 | 193,843 | 0.561 | 100.00 | 2025-09-22 | 253480861687000 |
| F41 | Spawned a Vehicle | Spawn a vehicle to obtain this badge. | 62,448,163 | 156,599 | 0.453 | 82.14 | 2025-09-22 | 460060999963993 |
| F42 | Spawned a Trailer | Spawn a trailer to obtain this badge. | 37,089,920 | 80,840 | 0.234 | 48.79 | 2025-09-22 | 3091659662171973 |
| F43 | Claimed a House | Claim a house to obtain this badge. | 7,164,284 | 22,458 | 0.065 | 9.42 | 2025-09-22 | 87107351303065 |

F44：4 个徽章 enabled 全为 true；updated 全在 2025-09-23。

## 4. 通行证（接口 14 条 = 13 个在售 + 1 条 Placeholder）

来源 GP（S，10-02 11:19）。nextPageToken 为空 = 一页取完。`name` 与 `displayName` 一致；`price` 与 `userBasePriceInRobux` 一致；`priceDiscountDetails` 全为空（无折扣）。
**与前序硬门口径的差异**：前序记「通行证 14（另有 Placeholder）」，本次实测是接口返回 14 条、其中 1 条就是 Placeholder，**在售 13 个**。正文一律写 13。

| # | `name`（逐字） | price（Robux） | isForSale | `displayDescription`（逐字） | created | updated | pass id |
|---|---|---|---|---|---|---|---|
| F50 | Spawn 4 Vehicles | 490 | true | Increases vehicle spawn limit from 2 to 4! | 2025-09-19 | 2026-08-09 | 1477209929 |
| F51 | Race Car Pack | 375 | true | Gain access to 3 premium race cars! | 2026-03-20 | 2026-08-10 | 1760202496 |
| F52 | Deluxe Car Pack | 345 | true | A pack of 4 iconic American performance vehicles! | 2025-09-22 | 2026-08-09 | 1481943751 |
| F53 | Any Slot Spawning | 300 | true | Allows you to spawn cars/trailers in any slot | 2026-08-14 | 2026-08-14 | 1948256386 |
| F54 | Luxury Houses | 290 | true | Grants the ability to claim luxury houses! | 2025-09-22 | 2026-08-09 | 1481579856 |
| F55 | Deluxe Mudder Pack | 320 | true | Grants access to 3 lifted mega mudding trucks! | 2025-09-22 | 2026-08-09 | 1481561991 |
| F56 | Classic Car Pack | 290 | true | A pack of 4 iconic American classic vehicles! | 2025-09-22 | 2026-08-09 | 1481901857 |
| F57 | Spawn 4 Trailers | 300 | true | Increases trailer spawn limit from 2 to 4! | 2025-09-19 | 2026-08-09 | 1477477859 |
| F58 | Police Vehicle Pack | 290 | true | A pack of 2 police vehicles! | 2026-01-16 | 2026-08-10 | 1672551026 |
| F59 | Deluxe Trailer Pack | 200 | true | Allows you to spawn the Boat Trailer and Double Jet Ski Trailer! | 2025-09-22 | 2026-08-09 | 1481759872 |
| F60 | Portable Trailer Spawner | 325 | true | Allows you to spawn trailers from anywhere in the map! | 2026-06-05 | 2026-08-12 | 1866262501 |
| F61 | Rock Lights Customization | 80 | true | （空字符串） | 2026-04-10 | 2026-08-11 | 1792403336 |
| F62 | Portable Customization | 80 | true | Customize your vehicles and trailers from anywhere! | 2025-09-22 | 2026-08-09 | 1481767952 |
| F63 | Placeholder | null（userBasePriceInRobux = 0） | **false** | （空字符串） | 2026-01-16 | 2026-08-10 | 1672299266 |

- F64：13 个在售通行证合计 3,685 Robux（我们计算：490+375+345+300+290+320+290+300+290+200+325+80+80）；最低 80，最高 490。
- F65：14 条记录的 `updated` 全部落在 2026-08-09 至 2026-08-14。接口不记录改了什么（价格 / 图标 / 描述都有可能），**不能据此写「8 月涨价」**；正文只写日期并标推断。
- F66：从通行证描述读出的默认上限：车辆同时生成 2 辆（Spawn 4 Vehicles 描述「from 2 to 4」）、拖车 2 辆（Spawn 4 Trailers 描述「from 2 to 4」）。
- F67：通行证描述里点名的具体载具只有两个：Boat Trailer、Double Jet Ski Trailer（F59）。各 Pack 只给数量与类别（3 premium race cars / 4 iconic American performance vehicles / 3 lifted mega mudding trucks / 4 iconic American classic vehicles / 2 police vehicles），**包内车名未获取**。

## 5. 开发者商品（61 个，全部官方）

来源 DP（S，10-02 11:19）。nextPageCursor = null = 一页取完，共 61 条。61 条全部：`IsForSale` = true、`Description` 空、`PriceDiscountDetails` 空、`IsLimited` = false（这是 Roblox 资产层面的字段，与商品名里的「Limited」无关）、`Name` = `displayName` = `DisplayName`、`PriceInRobux` = `UserBasePriceInRobux`。
3 个商品名尾部带一个空格（下表用 ␠ 标出）；正文与 entities.json 的 `name_en` 去掉首尾空白，原串存 `name_raw`。
分组是我们按名称与创建批次归的类，不是接口字段。

### 5a. 可单买的载具（22 个；20 个名称含 Limited，2 个不含）

| # | `Name`（逐字） | Robux | Created | Updated | ProductId |
|---|---|---|---|---|---|
| F70 | 6x6 Pickup Truck | 250 | 2025-12-17 | 2026-01-15 | 3482067584 |
| F71 | (Limited Special Offer) Gooseneck Camper + Truck␠ | 325 | 2025-12-23 | 2025-12-23 | 3487035699 |
| F72 | 6x6 Pickup Truck 2 | 250 | 2026-01-15 | 2026-04-17 | 3513657635 |
| F73 | (Limited) UTV 2 | 200 | 2026-01-29 | 2026-05-22 | 3525242612 |
| F74 | (Limited) European 6x6 Truck | 200 | 2026-02-05 | 2026-02-05 | 3530662330 |
| F75 | (Limited) Medium Duty Pickup Truck | 200 | 2026-02-19 | 2026-02-19 | 3540563699 |
| F76 | (Limited) 6x6 Pickup Truck 3 | 200 | 2026-04-17 | 2026-05-08 | 3577183349 |
| F77 | (Limited) 6x6 Pickup Truck | 200 | 2026-05-08 | 2026-05-08 | 3588624579 |
| F78 | (Limited) UTV | 249 | 2026-05-22 | 2026-05-22 | 3596647959 |
| F79 | [Limited!] UTV | 249 | 2026-06-05 | 2026-06-05 | 3602859428 |
| F80 | [Limited] Luxury RV | 249 | 2026-06-19 | 2026-06-19 | 3605526607 |
| F81 | [Limited] Pickup Truck 6x6 | 200 | 2026-06-26 | 2026-06-26 | 3606662102 |
| F82 | (Limited) Monster Mudding Truck | 279 | 2026-07-03 | 2026-07-03 | 3607942793 |
| F83 | [Limited] UTV | 229 | 2026-07-09 | 2026-07-09 | 3608986814 |
| F84 | [Limited] Super Tank | 269 | 2026-07-17 | 2026-07-18 | 3610361791 |
| F85 | [Limited] Storm Chaser Vehicle | 229 | 2026-07-31 | 2026-07-31 | 3612477392 |
| F86 | [Limited] Swamp Buggy | 200 | 2026-08-14 | 2026-08-14 | 3707989365 |
| F87 | [Limited] Sport Bike | 239 | 2026-08-21 | 2026-08-21 | 3709173874 |
| F88 | [Limited] Mega Truck | 249 | 2026-08-26 | 2026-08-26 | 3709895177 |
| F89 | [Limited] 4x4 Rock Crawler | 249 | 2026-09-10 | 2026-09-10 | 3712247229 |
| F90 | [Limited] Monster Truck | 249 | 2026-09-18 | 2026-09-18 | 3713425529 |
| F91 | [Limited] Off-Road 6x6 Pickup Truck | 249 | 2026-09-30 | 2026-09-30 | 3715562473 |

- F92：22 个载具商品价格分布：200 ×7、249 ×7、250 ×2、229 ×2、239 / 269 / 279 / 325 各 1；合计 5,213 Robux（我们计算）。
- F93：每个载具商品都有一个同价的礼物版（5b）。
- F94：名称含 UTV 的有 4 个不同商品（F73 / F78 / F79 / F83），名称只差括号样式或编号；含 6x6 的皮卡有 6 个（F70 / F72 / F76 / F77 / F81 / F91）。**接口不给图也不给描述，无法判断它们是不是同一辆车 → 需进游戏核实**。
- F95：`IsForSale` = true 只说明商品记录可售；**游戏内商店当前是否还摆着某个 Limited，公开数据看不到 → 需进游戏核实**。不写任何「何时回归」。

### 5b. 载具礼物版（22 个，与 5a 一一对应、同价、同日创建）

| # | `Name`（逐字） | Robux | Created | ProductId |
|---|---|---|---|---|
| F100 | Gift 6x6 Pickup Truck␠ | 250 | 2025-12-17 | 3482074930 |
| F101 | (GIFT Special Offer) Gooseneck Camper + Truck␠ | 325 | 2025-12-23 | 3487036012 |
| F102 | Gift 6x6 Pickup Truck 2 | 250 | 2026-01-15 | 3513658057 |
| F103 | (Limited) Gift UTV 2 | 200 | 2026-01-29 | 3525242877 |
| F104 | (Limited) Gift European 6x6 Truck | 200 | 2026-02-05 | 3530662725 |
| F105 | (Limited) Gift Medium Duty Pickup Truck | 200 | 2026-02-19 | 3540564006 |
| F106 | (Limited) Gift 6x6 Pickup Truck 3 | 200 | 2026-04-17 | 3577183447 |
| F107 | (Limited) Gift 6x6 Pickup Truck | 200 | 2026-05-08 | 3588624727 |
| F108 | (Limited) Gift UTV | 249 | 2026-05-22 | 3596648050 |
| F109 | [Limited!] Gift UTV | 249 | 2026-06-05 | 3602859485 |
| F110 | [Limited] Gift Luxury RV | 249 | 2026-06-19 | 3605526660 |
| F111 | [Limited] Gift Pickup Truck 6x6 | 200 | 2026-06-26 | 3606662174 |
| F112 | (Limited) Gift Monster Mudding Truck | 279 | 2026-07-03 | 3607942833 |
| F113 | [Limited] Gift UTV | 229 | 2026-07-09 | 3608986917 |
| F114 | [Limited] Gift Super Tank | 269 | 2026-07-17 | 3610361875 |
| F115 | [Limited] Gift Storm Chaser Vehicle | 229 | 2026-07-31 | 3612477448 |
| F116 | [Limited] Gift Swamp Buggy | 200 | 2026-08-14 | 3707989400 |
| F117 | [Limited] Gift Sport Bike | 239 | 2026-08-21 | 3709173927 |
| F118 | [Limited] Gift Mega Truck | 249 | 2026-08-26 | 3709895197 |
| F119 | [Limited] Gift 4x4 Rock Crawler | 249 | 2026-09-10 | 3712247367 |
| F120 | [Limited] Gift Monster Truck | 249 | 2026-09-18 | 3713425589 |
| F121 | [Limited] Gift Off-Road 6x6 Pickup Truck | 249 | 2026-09-30 | 3715562507 |

### 5c. 通行证礼物版（13 个）

| # | `Name`（逐字） | Robux | Created | Updated | 对应通行证（现价） | 差额（礼物 − 通行证） |
|---|---|---|---|---|---|---|
| F130 | Portable Customization Gift | 80 | 2025-09-23 | 2025-09-23 | Portable Customization（80） | 0 |
| F131 | Rock Lights Customization Gift | 80 | 2026-04-10 | 2026-04-10 | Rock Lights Customization（80） | 0 |
| F132 | Deluxe Trailer Pack | 200 | 2025-09-23 | 2026-03-02 | Deluxe Trailer Pack（200） | 0 |
| F133 | Classic Car Pack Gift | 250 | 2025-09-23 | 2025-09-23 | Classic Car Pack（290） | −40 |
| F134 | Luxury House Gift | 250 | 2025-09-23 | 2026-05-26 | Luxury Houses（290） | −40 |
| F135 | Police Vehicle Pack Gift | 250 | 2026-01-16 | 2026-01-16 | Police Vehicle Pack（290） | −40 |
| F136 | Deluxe Mudder Pack Gift | 275 | 2025-09-23 | 2026-05-26 | Deluxe Mudder Pack（320） | −45 |
| F137 | Deluxe Car Pack Gift | 300 | 2025-09-23 | 2025-09-23 | Deluxe Car Pack（345） | −45 |
| F138 | Spawn 4 Trailers Gift | 300 | 2025-09-23 | 2026-06-03 | Spawn 4 Trailers（300） | 0 |
| F139 | Any Slot Spawning Gift | 300 | 2026-08-14 | 2026-08-14 | Any Slot Spawning（300） | 0 |
| F140 | Race Car Pack Gift | 325 | 2026-03-20 | 2026-05-26 | Race Car Pack（375） | −50 |
| F141 | [GIFT] Portable Trailer Spawner | 390 | 2026-06-05 | 2026-07-19 | Portable Trailer Spawner（325） | **+65** |
| F142 | Spawn 4 Vehicles Gift | 425 | 2025-09-23 | 2026-05-26 | Spawn 4 Vehicles（490） | −65 |

- F143：F132 的商品名就叫「Deluxe Trailer Pack」，不带 Gift。把它归为礼物版**是推断**（与另外 7 个 Gift 商品同在 2025-09-23 15:57–15:58 UTC 这一批创建，且同名通行证已存在）；正文必须写 likely。
- F144：13 个礼物里 7 个比通行证便宜（40–65）、5 个同价、1 个更贵（Portable Trailer Spawner，礼物 390 对通行证 325）。通行证记录 `updated` 都在 8 月（F65）；礼物商品 `Updated` 除 Any Slot Spawning Gift（与通行证同为 2026-08-14）外都早于对应通行证的 `updated`——**可能是通行证改过价而礼物没跟**，也可能相反；接口看不出，正文只并列两个价并写 likely / cannot tell。

### 5d. 其他（4 个）

| # | `Name`（逐字） | Robux | Created | Updated | ProductId |
|---|---|---|---|---|---|
| F150 | Spawn Tornado 3 Minutes | 120 | 2026-04-01 | 2026-04-03 | 3567989884 |
| F151 | Spawn Tornado 5 Minutes | 200 | 2026-04-01 | 2026-04-03 | 3567990023 |
| F152 | Spawn Tornado 8 Minutes | 300 | 2026-04-01 | 2026-04-03 | 3567990139 |
| F153 | Delivery Event Unlock Now | 200 | 2026-02-12 | 2026-02-12 | 3535529014 |

- F154：龙卷风每分钟单价（我们计算）：3 分钟 40.0、5 分钟 40.0、8 分钟 37.5 Robux / 分钟。龙卷风做什么、影响范围、是否也会自然生成 → **未获取**。
- F155：「Delivery Event Unlock Now」只有名称与价格。Delivery Event 是什么、解锁什么、是否仍在进行 → **未获取**。

## 6. 官方活动（Roblox Events）——第 2 轮重写（2026-10-02 12:13 UTC 重取）

**第 1 轮的错误**：当时只读了不带参数的接口（返回 3 条），据此写了「接口只返回当前与未来的活动」「three event listings」。验证员指出加参数后能取到 43 条，属实，已全部改正。

**取数方法（可复现）**：
- 不带参数：`https://apis.roblox.com/virtual-events/v1/universes/8719555347/virtual-events` → 3 条（当前在开的三条），nextPageCursor 为空。记为 EV。
- 验证员给的 `?eventStatus=completed`：我在 12:11–12:13 UTC 连试 5 次（含 Completed / all / ended / active 等变体与 limit、fromUtc 等参数，`raw/` 未逐个存档），**每次仍只返回同样 3 条**，没能复现「第一页 24 条」。验证员 11:52 的存档 `verify/.../live/ev_completed.json` 确有 24 条并带 nextPageCursor，所以差异在接口行为（原因未知），不在数据。
- 我实际走通的路径：游标形如 `id_2` + base64url(两个 msgpack uint64：开始时间毫秒、活动 id)。自己构造一个「时间 0、id 0」的起始游标 `id_2zwAAAAAAAAAAzwAAAAAAAAAA`，请求 `…/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA` → 第 1 页 24 条，nextPageCursor = `id_2zwAAAZ6YusqKzyVxK9IiggIy`；再请求该游标 → 第 2 页 19 条，nextPageCursor 为空。合计 **43 条，id 无重复**，与验证员存档的 43 个 id 完全一致。记为 EVH。原始响应 `raw/events_hist_p1.json`、`raw/events_hist_p2.json`，合并排序后 `raw/events_hist_all.json`，请求日志 `raw/events_hist_fetchlog.json`。
- RSVP：RS（S，10-02 11:23，只取了当前三条）。单个活动详情接口 `…/virtual-events/<id>` 返回 401，未获取。

43 条共同点：host 全是群组 Southern Mudding（hostId 33504096，认证）；category 全是 newContent；eventStatus 字段全是 active（已结束的也是，接口如此）；title = displayTitle、description = displayDescription。

| # | `title`（逐字） | startUtc | endUtc | createdUtc | `subtitle`（逐字） | `description`（逐字；⏎ = 换行） |
|---|---|---|---|---|---|---|
| E01 | Towing Update | 2025-12-12 Fri 17:00:19 | 2025-12-19 17:00 | 2025-12-08 | The towing update | Check out our new towing update |
| E02 | Winter Update Pt. 2 | 2025-12-23 Tue 18:50:00 | 2026-01-01 17:00 | 2025-12-19 | 2nd part of Winter Upd | （标准句） |
| E03 | 🎆 New Years Update | 2025-12-31 Wed 18:00:43 | 2026-01-09 18:00 | 2025-12-23 | New Years Update | New truck and trailers! |
| E04 | Chassis Cab Trucks! | 2026-01-09 Fri 18:00:00 | 2026-01-16 18:00 | 2026-01-02 | New Chassis Cab Trucks! | Added new Chassis Cab Trucks! |
| E05 | 🚨Police Update | 2026-01-16 Fri 18:00:20 | 2026-01-23 18:00 | 2026-01-09 | This Week's Update | Follow to be notified when the police update releases! |
| E06 | New Trucks! | 2026-01-23 Fri 18:00:00 | 2026-01-30 18:00 | 2026-01-23 | This week's Update | （标准句） |
| E07 | Dirtbike Update | 2026-01-30 Fri 18:00:45 | 2026-02-06 18:00 | 2026-01-23 | This Week's Update | （标准句） |
| E08 | Tire Customization! 🔧 | 2026-02-06 Fri 18:00:13 | 2026-02-13 18:00 | 2026-01-24 | This Week's Update | （标准句） |
| E09 | Trucking Event! | 2026-02-13 Fri 18:00:52 | 2026-02-20 18:00 | 2026-01-30 | SM's First Event! | Deliver cargo to unlock a new truck. ⏎  ⏎ Follow to be notified when the update drops! |
| E10 | Lawn Mower Update | 2026-02-20 Fri 18:00:00 | 2026-02-27 18:00 | 2026-02-06 | Lawn Mower Update | （标准句） |
| E11 | Boat Update | 2026-02-27 Fri 19:40:00 | 2026-03-06 18:00 | 2026-02-14 | This Week's Update | （标准句） |
| E12 | Lift Kits! | 2026-03-06 Fri 18:15:02 | 2026-03-13 17:00 | 2026-02-20 | New Lift Kits + Offset! | New lift kits, wheel offset customization, and more! |
| E13 | ATVs Update! | 2026-03-13 Fri 19:30:24 | 2026-03-20 17:00 | 2026-02-27 | ATVs Update! | Follow to be notified when the update drops! ⏎  ⏎ Introducing many new ATVs and UTVs, as well as a new part of the map! |
| E14 | New Truck + More | 2026-03-20 Fri 17:10:51 | 2026-03-27 17:00 | 2026-02-27 | New Truck + More | （标准句） |
| E15 | RV Update | 2026-03-27 Fri 18:00:01 | 2026-04-03 17:00 | 2026-03-04 | RV Update | （标准句） |
| E16 | Storm Chasing Update! | 2026-04-03 Fri 18:30:11 | 2026-04-10 17:00 | 2026-03-20 | Storm Chasing Update! | Follow to be notified when the update drops |
| E17 | 🔧Tires + Rock Lights!🔧 | 2026-04-10 Fri 17:00:03 | 2026-04-17 17:00 | 2026-03-27 | 🔧Tires + Rock Lights!🔧 | （标准句） |
| E18 | New Trucks + Dunes! | 2026-04-17 Fri 18:00:39 | 2026-04-24 17:00 | 2026-04-03 | New Trucks + Dunes! | （标准句） |
| E19 | Toy Haulers! | 2026-04-24 Fri 17:45:59 | 2026-05-01 17:00 | 2026-04-10 | Toy Haulers! | （标准句） |
| E20 | Opening Doors + Tailgates | 2026-05-01 Fri 17:00:31 | 2026-05-08 17:00 | 2026-04-17 | This Week's Update | （标准句） |
| E21 | Truck Campers! | 2026-05-08 Fri 17:20:38 | 2026-05-15 17:00 | 2026-04-24 | Truck Campers! | （标准句） |
| E22 | 🗺️ Map Expansion! | 2026-05-15 Fri 17:00:28 | 2026-05-22 17:00 | 2026-05-01 | Map Expansion! | （标准句） |
| E23 | Dirtbikes, UTVs, & ramps! | 2026-05-22 Fri 17:00:32 | 2026-05-29 17:00 | 2026-05-08 | Dirtbikes, UTVs, & ramps! | （标准句） |
| E24 | Bed Cargo + Houses! | 2026-05-29 Fri 18:15:38 | 2026-06-05 17:00 | 2026-05-15 | Bed Cargo + Houses! | （标准句） |
| E25 | Tiny Home Trailers! | 2026-06-05 Fri 17:00:16 | 2026-06-12 17:00 | 2026-05-22 | Tiny Home Trailers! | （标准句） |
| E26 | New Side-by-side + more! | 2026-06-12 Fri 17:00:33 | 2026-06-19 18:00 | 2026-05-29 | New Side-by-side + more! | （标准句） |
| E27 | New RVs & Toy Hauler! | 2026-06-19 Fri 18:00:18 | 2026-06-26 18:25 | 2026-06-05 | New RVs & Toy Hauler! | （标准句） |
| E28 | Engine Swaps!🛠️ | 2026-06-26 Fri 19:45:27 | 2026-07-03 17:00 | 2026-06-12 | Engine Swaps!🛠️ | （标准句） |
| E29 | 🇺🇸July 4th+MAP! | 2026-07-03 Fri 18:00:04 | 2026-07-10 17:00 | 2026-06-19 | 🇺🇸July 4th+MAP! | （标准句） |
| E30 | License Plates+New ATVs | 2026-07-10 Fri 17:30:54 | 2026-07-17 17:00 | 2026-06-26 | License Plates+New ATVs | Follow to be notified when the update is dropped! |
| E31 | 💥Military Vehicles!🎖️ | 2026-07-17 Fri 17:30:00 | 2026-07-24 17:00 | 2026-07-03 | 💥Military Vehicles!🎖️ | （标准句） |
| E32 | 🎣 Boats & Fishing Upd 🐠 | 2026-07-24 Fri 17:00:38 | 2026-07-31 17:00 | 2026-07-10 | 🎣 Boats & Fishing Upd 🐠 | （标准句） |
| E33 | 📡Tornado Chaser Upd!🌪️ | 2026-07-31 Fri 17:00:31 | 2026-08-07 17:00 | 2026-07-17 | 📡Tornado Chaser Upd!🌪️ | （标准句） |
| E34 | 🚐Stacker Trailer!🚐 | 2026-08-07 Fri 17:00:36 | 2026-08-14 17:00 | 2026-07-24 | 🚐Stacker Trailer!🚐 | （标准句） |
| E35 | 🐊Swamp Buggies🐊 | 2026-08-14 Fri 17:00:15 | 2026-08-21 17:00 | 2026-07-31 | 🐊Swamp Buggies🐊 | （标准句） |
| E36 | 🏍️Motorcycle Update!🏍️ | 2026-08-21 Fri 17:00:10 | 2026-08-28 17:00 | 2026-08-07 | 🏍️Motorcycle Update!🏍️ | （标准句） |
| E37 | ✨Show Trucks!✨ | 2026-08-28 Fri 17:00:01 | 2026-09-04 17:00 | 2026-08-14 | ✨Show Trucks!✨ | （标准句） |
| E38 | 🚚New Wrecker!🚚 | 2026-09-04 Fri 18:00:57 | 2026-09-11 17:00 | 2026-08-21 | 🚚New Wrecker!🚚 | （标准句） |
| E39 | ⛰️4x4 Crawlers!⛰️ | 2026-09-11 Fri 17:00:02 | 2026-09-18 17:00 | 2026-08-28 | ⛰️4x4 Crawlers!⛰️ | （标准句） |
| E40 | 🚐RVs Update!🚐 | 2026-09-18 Fri 17:00:52 | 2026-09-25 17:00 | 2026-09-04 | 🚐RVs Update!🚐 | （标准句） |
| E41 | 🚀Nitrous Update!🚀 | 2026-09-25 Fri 17:15:56 | 2026-10-02 17:00 | 2026-09-11 | 🚀Nitrous Update!🚀 | （标准句） |
| E42 | This Week's Update! | 2026-10-02 Fri 17:00:46 | 2026-10-09 17:00 | 2026-09-18 | This Week's Update! | （标准句） |
| E43 | Next Week's Update! | 2026-10-09 Fri 17:00:16 | 2026-10-16 17:00 | 2026-09-25 | Next Week's Update! | （标准句） |

- F160 = E41（🚀Nitrous Update!🚀；going / notGoing = 67,491 / 10,758，11:23 UTC）；F161 = E42（This Week's Update!；43,785 / 5,324）；F162 = E43（Next Week's Update!；8,044 / 603）。
- F163（重写）：43 条里 **41 条在周五开始**；另两条是 E02（周二 2025-12-23 18:50）与 E03（周三 2025-12-31 18:00）。2026-01-09 至 2026-10-09 每个周五恰好一条，连续 40 条。41 条周五列表的开始时刻分布（UTC）：17:00–17:29 **20 条**、17:30–17:59 **3 条**、18:00–18:29 **14 条**、18:30–18:59 **1 条**（E16）、19:30 以后 **3 条**（E11 19:40、E13 19:30、E28 19:45）。**与验证员数到的一致**（20 / 3 / 14 / 1 / 3）。最近 10 条（含未开始的 E42、E43）里 9 条在 17:00–17:15，例外是 E38（09-04 18:00）；只算已开始的最近 10 条（E32–E41）也是 9 条。
- F163b：活动开始时间是开发者排的日程，不等于实际更新时刻。能从 listing 实测的只有一次：F4 `updated` = 2026-09-25T17:20:11Z，比 E41 开始（17:15:56）晚 4 分 15 秒。正文写「usually 17:00 UTC」+ 这一次实测 17:20。
- F163c（推断，正文已标 inference）：E04–E10（2026-01-09 至 02-20，7 个周五）全部 18:00 UTC；18:00 UTC（冬令）与 17:00 UTC（夏令）都是美东 13:00 → 11 月 1 日美国改冬令时后 UTC 时刻**可能**回到 18:00。开发者没说过。
- F164：17:00 UTC 换算（美国夏令时到 2026-11-01、英国到 2026-10-25；我们换算）：13:00 EDT / 12:00 CDT / 10:00 PDT / 18:00 BST。
- F165（更正）：描述只留当期更新说明；**活动列表保留了每周更新的标题**，最早到 2025-12-12；完整更新说明仍然没有。
- F166：Nitrous 活动缩略图 mediaId 81746768314421 的 CDN 地址与游戏宣传图 th1 相同（`raw/event_thumb.json`）。
- F167：43 条的 description：34 条恰好是标准句「Follow to be notified when the update drops!」；3 条是变体（E05、E16、E30）；6 条有实质内容（E01、E03、E04、E09、E12、E13，其中 E09、E13 同时含标准句）。
- F168：41 条已有具体标题的列表里没有一条叫「This Week's Update!」之类的占位名；32 条在开始前 14 天创建。
- F169（活动标题与商店数据的同日/邻日对应，正文用到的）：E16 Storm Chasing Update!（04-03）↔ 三个 Spawn Tornado 商品 04-01 创建；E33 📡Tornado Chaser Upd!🌪️（07-31）↔ [Limited] Storm Chaser Vehicle 07-31 创建；E17 🔧Tires + Rock Lights!🔧（04-10）↔ Rock Lights Customization 通行证 04-10 创建；E09 Trucking Event!（02-13 至 02-20，subtitle「SM's First Event!」，description「Deliver cargo to unlock a new truck.」）↔ 商品 Delivery Event Unlock Now 02-12 创建（**二者有关是按日期的推断**，正文标 likely / our inference）；E24 Bed Cargo + Houses!（05-29）；E25 Tiny Home Trailers!（06-05）；E34 🚐Stacker Trailer!🚐（08-07）；E07 Dirtbike Update（01-30）、E10 Lawn Mower Update（02-20）、E11 Boat Update（02-27）、E13 ATVs Update!（03-13）；E08 Tire Customization! 🔧（02-06）、E12 Lift Kits!（03-06）、E28 Engine Swaps!🛠️（06-26）、E30 License Plates+New ATVs（07-10）；E22 🗺️ Map Expansion!（05-15）。

## 7. 官方群组

| # | 事实 | 值 | 来源 | 取数（UTC） | 级 |
|---|---|---|---|---|---|
| F170 | 群组名 / 认证 | Southern Mudding；hasVerifiedBadge = true | GR | 10-02 11:20 | S |
| F171 | 群组描述（逐字） | "Join the group for a free pickup truck!" | GR `description` | 10-02 11:20 | S |
| F172 | 所有者 | SouthernMudHold（userId 9886193400，账号有认证标） | GR `owner` | 10-02 11:20 | S |
| F173 | 成员数（快照） | 649,071 | GR `memberCount` | 10-02 11:20 | S |
| F174 | shout | null（无） | GR `shout` | 10-02 11:20 | S |
| F175 | 公开加入 | publicEntryAllowed = true | GR | 10-02 11:20 | S |
| F176 | 角色与人数 | Guest 0 / Member 649,071（另一条同名 Member 记录 649,170）/ Tester 2 / Artist 2 / Admin 9 / Lead 3 / PM 1 / Owner 1 | RO | 10-02 11:20 | S |
| F177 | 群组公开游戏 | 只有本作一款 | GG | 10-02 11:20 | S |
| F178 | 群组赠车 | 官方只有 F171 这一句。**送哪辆皮卡、进游戏后去哪领、是否要重进 → 未获取** | — | — | — |

## 8. 兑换码

- F180：G 描述（F32）、GR 描述（F171）、GR shout（F174）三处官方来源都没有任何兑换码。群组 wall、social-links、Discord 未获取。**结论：不建 codes 页，任何页都不列码。**游戏里有没有兑换码输入框 → 未获取（需进游戏核实）。

## 9. 未获取清单（原因）

| 项 | 原因 |
|---|---|
| 群组 wall | `groups.roblox.com/v2/groups/33504096/wall/posts` 返回 404 + 空错误体。只能说「公开接口返回 404」，不能证明是「匿名不可读」 |
| 群组 social-links | 401 Authentication token is missing |
| 游戏 social-links（Discord / X / YouTube 官方链接） | 匿名请求 401 Authentication token is missing；且官方文档写明社交链接只对已验证年龄 ≥16 岁的用户可见（DOC1），不是「登录即可见」 |
| place 详情（设备支持等） | 401 |
| 单个活动详情 | 401 |
| Discord 公告、X | 需登录，按任务边界不取 |
| 历史更新说明全文（9-25 之前） | 描述只留当期；活动列表只留了每周标题（43 条，见第 6 节），没有全文 |
| 车辆性能数值、免费车名单、游戏币名称与收入、地图地点、房屋数量与位置、氮气用法、群组赠车领取步骤、Delivery Event 内容、龙卷风机制、各 Pack 内车名、操作按键 | 公开接口没有；需进游戏核实（见 todo.md） |
| 搜索量 | Semrush 未用（按任务边界）；只有 Google 下拉（`raw/suggest.txt`），不估算 |

## 10. 关键词佐证（Google 下拉，2026-10-02 11:22 UTC，`raw/suggest.txt`，B 级，只作需求证据）

- 「southern mudding」→ roblox / discord / roblox discord / roblox map / script / roblox codes / map / roblox script / new update / roblox new update
- 「southern mudding update」→ update today / new update / next update / when does southern mudding update / what time does southern mudding update
- 「southern mudding roblox」→ … houses / update today / discord servers
- 「southern mudding tornado」→ southern mudding tornado / southern mudding roblox tornado
- 下拉为空的：codes（单独查）、nitrous、gamepass、free truck、limited、best truck、trailer、money、6x6、utv、badges

## 11. 正文 ↔ 底稿对应表（给验证员；第 2 轮更新）

| 页（content/en） | 用到的事实编号 |
|---|---|
| index.md | F1–F13、F16、F20–F31、F40–F43、F50–F64、F92、E41–E43、F163、F170–F174、F180、DOC1（间接） |
| guides.md | F31、F40–F43、F64、F66、F92、F163、F171 |
| how-to-play.md | F2–F8、F13、F20、F21、F28、F40–F43、F50、F57、F66、F171、F178、F180 |
| vehicles.md | F20、F24、F25、F51、F52、F55、F56、F58、F59、F67、F70–F94、F171、E07、E10、E11、E13 |
| spawning.md | F41、F42、F50、F53、F57、F59、F60、F66、F71、F138、F139、F141、F142、F143、E25、E34 |
| nitrous.md | F1、F22–F26、F61、F62、F130、F131、E41（F160）、E08、E12、E17、E28、E30、F169、F173 |
| gamepasses.md | F50–F65、F130–F144、DOC4 |
| limiteds.md | F70–F95、F100–F121、F150–F155、E09、E16、E33、F169 |
| badges.md | F9、F40–F44、F54、F134、E24、DOC3 |
| updates.md | F3、F4、F22–F26、F31、F50、F54、F55、F57（创建日）、F40–F43（创建日）、F70–F91（创建日的星期统计）、E01–E43、F163、F163b、F163c、F164、F165、F167、F168、DOC1、DOC5 |
| community.md | F2、F32、F170–F178、F180、E42 的 RSVP、F167、DOC1、DOC2、DOC6 |
| author.md | 编辑方针页，无独立事实；数量引用 F44、F64、F92 |

## 12. 正文里的推断句清单（全部已在句内标 likely / suggests / our reading / inference；验证员请重点核这些有没有被写成确认）

| 页 | 推断内容 | 依据（事实编号） | 句内标记 |
|---|---|---|---|
| how-to-play / spawning | 默认可同时生成 2 辆车 + 2 辆拖车 | F50、F57 两条通行证描述「from 2 to 4」（F66） | going by the pass descriptions / If those descriptions are current |
| spawning | 槽位平时按类型分，Any Slot Spawning 解除限制 | F53 一句描述 | The wording implies… That is our interpretation of a single sentence |
| spawning | 拖车平时只能在固定点生成 | F60 通行证的存在 | suggests |
| gamepasses | 商品「Deluxe Trailer Pack」是礼物版 | F132、F143（同批创建） | likely… the data does not say so |
| gamepasses | 礼物价低于通行证价是因为通行证 8 月改过价 | F65、F144 | may have been… That is an inference |
| badges | 普通房人人可领、豪宅要通行证 | F43、F54 措辞 | The pass wording suggests… It is still an inference |
| badges | Claimed a House 少的三个原因 | 无直接数据 | Three explanations are plausible, and they are ours |
| badges | 约 5.6 次访问 / 每个 Welcome 徽章 → 与玩家回访相符 | F9 ÷ F40；徽章「已有则不能再发」见 DOC3；访问量定义没有出处 | is consistent with… but the visit definition is not published in the sources we read |
| limiteds | 同名不同括号的商品是不同的车 | F94（各有独立 ID、价、创建日） | suggests separate vehicles. The data cannot prove it |
| limiteds | （第 2 轮已删）原句「开发者可以不改标记就撤按钮」无出处，改成「游戏内是否展示由游戏自己控制，公开数据看不到」 | DP `IsForSale` 字段本身 | The flag belongs to the Roblox product record… |
| limiteds / updates | 9-30 新建的 Off-Road 6x6 属于 10-02 更新 | F91 创建日 | It may belong to… nothing official says so yet |
| limiteds | Delivery Event Unlock Now 是 Trucking Event!（E09）那次解锁的付费捷径 | F153 创建日 02-12 与 E09 开始日 02-13 相邻、E09 描述「Deliver cargo to unlock a new truck.」（F169） | it is likely… That link is our inference from the dates |
| nitrous | Portable Customization 能在车库外加氮气 | F23、F62 | would likely… not a confirmed one |
| nitrous | Rock Lights Customization 是外观项 | F61 名称 | likely cosmetic, going by its name |
| nitrous | 氮气是性能项 | 名称 | by its name |
| updates | 更新「通常 17:00 UTC」 | 41 条周五列表的开始时刻分布（F163）+ 唯一一次实测 17:20（F163b） | Usually… An event's start time is the developer's schedule, not a record… not a guarantee |
| updates | 11 月改冬令时后可能回到 18:00 UTC | E04–E10 七个周五都是 18:00（F163c） | may shift… That is our inference… the developer has not said so |
| updates | 周五发布规律 | F31 官方原话 + 43 条活动 41 条周五开始（F163）+ 22 个载具商品 12 个周五创建 | Yes, with two early exceptions |
| updates / community | （第 2 轮改为有出处）旧服务器不立即换版本 → 引 DOC5 原话；活动通知 → 引 DOC2 原话；「进群奖励要重进」的理由句已删，只留「try rejoining… we have not confirmed that this is needed」 | DOC5、DOC2 | 引号内为文档原话 |
| vehicles | 宣传图里的房车 / 船对应 Luxury RV / Boat Trailer | F17、F59、F80 | Some may correspond… we have not matched any image |
| nitrous | Engine Swaps、License Plates 两个活动标题属于改装类 | E28、E30 标题 | sound like tuning features too, but no official text calls them customization |
| badges | 2026-05-29 那次更新动了房屋 | E24 标题「Bed Cargo + Houses!」 | The event title shows… the listing does not say what changed |
| vehicles | 9-25 的新皮卡 / 新 UTV 用游戏币买或别的方式解锁 | F24、F25 + 那周无新商品 | They may be… needs an in-game check |
| community | 官方 Discord 是否存在 | social-links 401 | We could not confirm one |

## 13. Roblox 官方文档来源（第 2 轮新增，S 级；2026-10-02 12:16–12:17 UTC 自取，副本在 `raw/docs/`）

| # | URL | 用到的原话（逐字） | 用在哪 |
|---|---|---|---|
| DOC1 | https://create.roblox.com/docs/en-us/production/promotion/social-media-links | "Social media links are only visible to users who have verified their age as at least 16 years old." 另：同页写明 Community Standards 只允许把社交链接放在 game's main details page | community.md（Discord 一节、未读清单表、scope、tldr）、index.md、updates.md |
| DOC2 | https://create.roblox.com/docs/en-us/production/promotion/experience-events | "Players who click **Notify Me** for an upcoming event will receive stream notifications in their Roblox inbox when the event starts." | community.md |
| DOC3 | https://create.roblox.com/docs/en-us/reference/engine/classes/BadgeService | "The player must not already have the badge (note that a player may delete an awarded badge from their profile and be awarded the badge again)" | badges.md（转述，未加引号） |
| DOC4 | https://create.roblox.com/docs/en-us/production/monetization/passes | "**Passes** let you charge users a one-time Robux fee to access special privileges inside your game, such as entry to a restricted area, an in-game avatar item, or a permanent power-up." | gamepasses.md（引 "a one-time Robux fee"） |
| DOC5 | https://create.roblox.com/docs/en-us/projects/update-experiences | "When you publish an updated version of an experience to Roblox, players aren't immediately removed from old versions of the experience." / "If you don't restart servers, players transition to the new version of the experience as the servers running old versions eventually empty and shut down." | updates.md（比验证员给的 publish 页更直接，所以用了这一页） |
| DOC6 | https://about.roblox.com/community-standards | "Using or sharing exploits to help yourself or others gain an unfair advantage anywhere on the platform"（列在「Roblox doesn’t allow cheating, exploits…」之下） | community.md |
| DOC7 | https://create.roblox.com/docs/en-us/production/publishing/badges | 全页没有 win rate / winRatePercentage 的定义（grep 无结果） | badges.md「Roblox's Creator Docs do not define how it is calculated」 |

## 14. 第 2 轮改动记录

逐条「改前句 → 改后句」见 `raw/round2_edits.json`（74 条精确替换，脚本 `raw/round2_edits.py`）；updates.md 是整页重写，改前版本在 `raw/en_round1_backup/updates.md`。`_images.json` 的 th1、th5 alt 与 `config-snippet.json` 的 card.img_alt 同步改了；`entities.json` 活动实体从 3 条补到 43 条（总实体 82 → 122）。
