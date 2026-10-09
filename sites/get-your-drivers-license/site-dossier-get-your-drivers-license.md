# Get Your Driver's License! 事实底稿(dossier)

取证日:2026-10-09(UTC 11:11–11:29 抓取;快照型数字只代表那一刻)。五个时间点:**T1** = 11:11 UTC(games / votes / favorites / badges / game-passes / developer-products / group / thumbnails / virtual-events / age / media / 游戏页 HTML),**T2** = 11:13 UTC(badges 复查两次、owner、group roles、supported-languages、group games、图标资产、develop universes、public servers),**T3** = 11:15 UTC(第三方页与 Fandom 探测),**T4** = 11:18 UTC(groups v2、games 复读、owner 的群组列表、Roblox 官方文档),**T5** = 11:29 UTC(groups v1、votes、badges 第 4 次复读)。
范围:Roblox 体验「Get Your Driver's License!」,universeId 10768565603,rootPlaceId 104416416393862,创作者群组 Time Will Pass(groupId 356677783)。同群组另外 4 个体验(Hold It In 🚽 / Don't Be Late For Work! ⏰ / Next Prisoner / Next Subject)只在 community 页以「同组其它作品」列名,内容不混入。
原始抓取文件:`raw/`(`fetch-log.txt` 记录每个 URL 的 HTTP 状态;`fetch-time-1.txt` / `fetch-time-2.txt` 是两批的起始时刻;`raw/img/` 是本人看图用的下载件;`raw/comp/` 是第三方页;`raw/docs/` 是 Roblox 官方文档;`raw/suggest.jsonl` 是 Google 下拉原始返回)。raw 不进仓。

来源分级(按任务口径):**S** = 官方一手(Roblox games / badges / game-passes / developer-products / groups / thumbnails 接口、游戏页官方 description、Roblox 官方文档 create.roblox.com);**A** = 开发者本人在官方渠道的原话(本次 **0 条**:群组 description 为空串、shout 为 null、wall 接口 404、social links 接口 401、官方活动 0 条);**B** = 第三方 wiki / 媒体 / 统计站(本次只有 Rolimon's 与 Rotrends 两个统计页);**C** = 视频评论 / 论坛帖(本次 **0 条**,未检索到)。

结论:S 级素材是「一段 6 行功能描述 + 5 个通行证 + 13 个开发者商品(每个都有一句官方描述)+ 群组资料 + 2 张官方图」。**13 个商品描述是最厚的一层**,里面有硬数字(往前 5 位、跳过 2:30、5 分钟考官、+1 分钟)和若干专名(Epic、The Loop、Ticket #001、waiting room)。**没有任何一手来源的**:18 辆车的名字与稀有度分档、全部结局名单(只有 Honor Roll 与 Towed 两个名字)、笔试题目与答案、考场路线、不花 Robux 能否当考官、兑换码、官方 Discord。徽章 0 个、官方活动 0 条。这些全部进「未核实」,正文写 not published 或不写。

**round1 修订(2026-10-09,独立对抗验证之后;逐条对照见 `fix-round1.md`)**:① 官方描述是功能清单,**不写一局的先后顺序、不写每局必得车**,页面改成「the description lists …」口径;② 单服 25 人只写这个事实本身,不再反推「队伍最多 24 人」(队伍怎么填充无来源);③ `goes poof` 一律照引原文并写明效果未说明,不写成 remove / clear the line;④ 通行证描述里点名别人的是 3 个(Time Out / Gravity Gun 🔥 / Ban Hammer),Airhorn 描述只有 "A very loud airhorn.",不算;⑤「不花钱也能通关」没有实测,改成「免费游玩、没有任何描述说必须购买、本站未实测不付费通关」;⑥ 商店变更按 F059 改(Golden Supercar 🏆 10-05 被编辑);⑦ 平均时长分别归属:Rolimon's 10.06 分钟、Rotrends Avg Session 11.0 mins;⑧「别站也没有码表」这类否定句删掉,只写 2026-10-09 读过的三个官方位置。

## 1. 基本信息

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F001 | 正式名 | `Get Your Driver's License!`(直撇号 U+0027,结尾有感叹号,无 emoji) | https://games.roblox.com/v1/games?universeIds=10768565603 | S | 2026-10-09 T1 |
| F002 | universeId / rootPlaceId | 10768565603 / 104416416393862(places→universe 接口回 `{"universeId":10768565603}`,互相印证) | https://games.roblox.com/v1/games?universeIds=10768565603 ;https://apis.roblox.com/universes/v1/places/104416416393862/universe | S | 2026-10-09 T1 |
| F003 | 创作者 | 群组 `Time Will Pass`(id 356677783,type Group,hasVerifiedBadge=false) | https://games.roblox.com/v1/games?universeIds=10768565603 `creator` | S | 2026-10-09 T1 |
| F004 | 创建时间 | `2026-09-29T08:24:37.079Z` → 29 September 2026 | https://games.roblox.com/v1/games?universeIds=10768565603 `created` | S | 2026-10-09 T1 |
| F005 | `updated` 字段(不可当更新日) | games v1 读到 `2026-10-08T18:36:30.185Z`(T1 与 T4 两次同值);群组游戏列表与 develop 接口同一字段是 `2026-10-08T15:24:03.049Z`。两个接口口径不同 → 按 SKILL 2026-10-08 口径不当「最近更新日」,正文不写 | https://games.roblox.com/v1/games?universeIds=10768565603 ;https://games.roblox.com/v2/groups/356677783/gamesV2?accessFilter=2&limit=100&sortOrder=Asc ;https://develop.roblox.com/v1/universes/10768565603 | S | 2026-10-09 T1/T2/T4 |
| F006 | 类型 | genre `All`;genre_l1 `Simulation`;genre_l2 `Idle` | https://games.roblox.com/v1/games?universeIds=10768565603 | S | 2026-10-09 T1 |
| F007 | 单服人数上限 | 25(公开服务器列表前 10 个服务器 maxPlayers 均为 25、在线 19–20 人) | https://games.roblox.com/v1/games?universeIds=10768565603 `maxPlayers`;https://games.roblox.com/v1/games/104416416393862/servers/Public?limit=10 | S | 2026-10-09 T1/T2 |
| F008 | 价格 | 免费(`price: null`) | https://games.roblox.com/v1/games?universeIds=10768565603 | S | 2026-10-09 T1 |
| F009 | 私服 | `createVipServersAllowed: false`;游戏页 `data-private-server-price="0"`、`data-can-create-server="False"` —— 按 SKILL 2026-10-02 口径不能据此判「不开放私服」,正文写无法确认 | https://games.roblox.com/v1/games?universeIds=10768565603 ;https://www.roblox.com/games/104416416393862 | S | 2026-10-09 T1 |
| F010 | 访问量 | T1:4,755,810;T4(约 8 分钟后):4,769,917 | https://games.roblox.com/v1/games?universeIds=10768565603 `visits` | S | 2026-10-09 T1/T4 |
| F011 | 在线 | T1:18,571;T4:19,526 | https://games.roblox.com/v1/games?universeIds=10768565603 `playing` | S | 2026-10-09 T1/T4 |
| F012 | 收藏 | T1:18,041(favorites/count 接口同值 18,041);T4:18,077 | https://games.roblox.com/v1/games?universeIds=10768565603 ;https://games.roblox.com/v1/games/10768565603/favorites/count | S | 2026-10-09 T1/T4 |
| F013 | 点赞 / 点踩 | T1:4,663 / 8,278(合计 12,941;好评率 36.0%,我们计算:4663÷12941=36.03%;踩÷赞=1.78)。**点踩多于点赞**。T5(11:29)复读:4,666 / 8,342。页面一律用 T1 值并标 11:11 UTC | https://games.roblox.com/v1/games/votes?universeIds=10768565603 | S | 2026-10-09 T1 |
| F014 | 内容分级 | `Maturity: Minimal`;描述项 displayName `Suitable for everyone`;minimumAge 0 | https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation (POST `{"universeId":"10768565603"}`;GET 不可用,不放进页面 sourceUrls) | S | 2026-10-09 T1 |
| F015 | 游戏页媒体 | 1 张图片(imageId 71974832019062,altText 空),0 个视频 | https://games.roblox.com/v2/games/10768565603/media | S | 2026-10-09 T1 |
| F016 | 支持语言 | 18 种:English、Arabic、German、Spanish、French、Hindi、Indonesian、Italian、Japanese、Korean、Polish、Portuguese、Russian、Thai、Turkish、Vietnamese、Chinese (Simplified)、Chinese (Traditional)。接口不区分人工翻译与自动翻译 | https://gameinternationalization.roblox.com/v1/supported-languages/games/10768565603 | S | 2026-10-09 T2 |
| F017 | 头像类型 | `universeAvatarType: MorphToR15` | https://games.roblox.com/v1/games?universeIds=10768565603 | S | 2026-10-09 T1 |
| F018 | 游客可玩性 | `playabilityStatus: GuestProhibited`(匿名请求;只说明未登录不能玩,不说明设备支持) | https://games.roblox.com/v1/games/multiget-playability-status?universeIds=10768565603 | S | 2026-10-09 T2 |
| F019 | 规范路径 | `/games/104416416393862/Get-Your-Drivers-License`(游戏页 200,og:url 同) | https://www.roblox.com/games/104416416393862 | S | 2026-10-09 T1 |

## 2. 官方描述(逐行原文;emoji 在正文引用时去掉,其余逐字)

来源:https://games.roblox.com/v1/games?universeIds=10768565603 `description`(S,T1 取;develop 接口、群组游戏列表、游戏页 HTML `<meta name="description">` 三处复读一致)

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F020 | 描述第 1 行(口号) | "Wait in line and get your Driver's License!" | https://games.roblox.com/v1/games?universeIds=10768565603 `description` | S | 2026-10-09 T1 |
| F021 | 描述第 2 行(取号排队) | "🎟️ Take a number and wait your turn" | 同上 | S | 2026-10-09 T1 |
| F022 | 描述第 3 行(笔试) | "📝 Pass the written test" | 同上 | S | 2026-10-09 T1 |
| F023 | 描述第 4 行(路考;三种障碍名) | "🚦 Drive the test course: cows, ducks, ramps and more" | 同上 | S | 2026-10-09 T1 |
| F024 | 描述第 5 行(18 辆车;两端措辞) | "🎁 Win 1 of 18 cars, from rusty hatchbacks to secret supercars" | 同上 | S | 2026-10-09 T1 |
| F025 | 描述第 6 行(结局;两个结局名) | "🏅 Unlock every ending, from Honor Roll to Towed" | 同上 | S | 2026-10-09 T1 |
| F026 | 描述第 7 行(考官) | "📋 Be the Examiner and judge other players' driving" | 同上 | S | 2026-10-09 T1 |
| F027 | 描述第 8 行 | "Can you get your license?" | 同上 | S | 2026-10-09 T1 |
| F028 | 描述里有没有兑换码 | **没有**。全文 8 行(见 F020–F027),无 code / CODE / redeem 字样 | 同上 | S | 2026-10-09 T1 |

## 3. 通行证(5 个,nextPageToken 空串 = 已取全)

来源:https://apis.roblox.com/game-passes/v1/universes/10768565603/game-passes?passView=Full&pageSize=100 (S,T1)。名称逐字复制 `name` 字段(含 emoji、方括号、大小写);5 个 `isForSale` 均为 true,`priceDiscountDetails` 均为空数组,creator 均为群组 356677783。旧接口 `games.roblox.com/v1/games/10768565603/game-passes` 返回 404。

| # | 名称(逐字) | 价格(Robux) | 官方描述(逐字) | passId | created(UTC) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F030 | `PRO EMOJI PACK 😈` | 9 | "Unlocks the pro emoji pack." | 2003648331 | 2026-09-30T06:18:59.574Z | 上述 game-passes 接口 | S | 2026-10-09 T1 |
| F031 | `Airhorn [ANNOYING] ☠️` | 16 | "A very loud airhorn." | 2002994378 | 2026-09-30T06:19:01.549Z | 同上 | S | 2026-10-09 T1 |
| F032 | `Time Out` | 24 | "Put someone in time out." | 2001596592 | 2026-09-30T06:19:03.76Z | 同上 | S | 2026-10-09 T1 |
| F033 | `Gravity Gun 🔥` | 160 | "Pick people up and throw them." | 2002502542 | 2026-09-30T06:19:05.89Z | 同上 | S | 2026-10-09 T1 |
| F034 | `Ban Hammer` | 1,200 | "Bonk people with the ban hammer." | 2001554576 | 2026-09-30T06:19:07.928Z | 同上 | S | 2026-10-09 T1 |
| F035 | 五个通行证合计 | 1,409 Robux(9+16+24+160+1,200,我们计算);Ban Hammer 一项占 85.2%(1200÷1409) | 同上 | S(推导) | 2026-10-09 T1 |
| F036 | 五个通行证的创建时刻 | 全部在 2026-09-30 06:18:59–06:19:08 UTC 之间(9 秒内),updated 与 created 相同 | 同上 | S | 2026-10-09 T1 |

## 4. 开发者商品(13 个,nextPageCursor = null = 已取全)

来源:https://apis.roblox.com/developer-products/v2/universes/10768565603/developerproducts?limit=100 (S,T1)。名称逐字复制 `Name` 字段;13 个 `IsForSale` 均为 true,`PriceDiscountDetails` 均为空数组,`UserBasePriceInRobux` 与 `PriceInRobux` 相同。

| # | 名称(逐字) | 价格(Robux) | 官方描述(逐字) | ProductId | Created(UTC) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F040 | `Skip Line [SALE]` | 9 | "Jump 5 places ahead in the line." | 3715579206 | 2026-09-30T06:18:19.591Z | 上述 developer-products 接口 | S | 2026-10-09 T1 |
| F041 | `Skip Time [SALE]` | 9 | "Skip 2:30 of the wait in the waiting room." | 3715579219 | 2026-09-30T06:18:27.236Z | 同上 | S | 2026-10-09 T1 |
| F042 | `Skip Test` | 29 | "Pass the written test straight away." | 3715579223 | 2026-09-30T06:18:30.579Z | 同上 | S | 2026-10-09 T1 |
| F043 | `Skip To End` | 48 | "Go straight to your driving test." | 3715579231 | 2026-09-30T06:18:33.875Z | 同上 | S | 2026-10-09 T1 |
| F044 | `Kill` | 9 | "The person ahead of you in line goes poof." | 3715579244 | 2026-09-30T06:18:37.273Z | 同上 | S | 2026-10-09 T1 |
| F045 | `Kill All` | 160 | "Everyone waiting in line goes poof." | 3715579246 | 2026-09-30T06:18:40.699Z | 同上 | S | 2026-10-09 T1 |
| F046 | `Scare All` | 24 | "A jumpscare on everyone's screen." | 3715579250 | 2026-09-30T06:18:44.003Z | 同上 | S | 2026-10-09 T1 |
| F047 | `Revenge ⚡` | 9 | "Get back at whoever knocked you out." | 3715579253 | 2026-09-30T06:18:47.579Z | 同上 | S | 2026-10-09 T1 |
| F048 | `Be The Examiner 📋` | 29 | "5 minutes as the driving examiner." | 3715579261 | 2026-09-30T06:18:50.901Z | 同上 | S | 2026-10-09 T1 |
| F049 | `+1 Minute` | 9 | "One more minute as the examiner." | 3715579266 | 2026-09-30T06:18:54.224Z | 同上 | S | 2026-10-09 T1 |
| F050 | `VIP Ticket 🎟️` | 149 | "Ticket #001: your next car is Epic or better." | 3715579273 | 2026-09-30T06:18:57.558Z | 同上 | S | 2026-10-09 T1 |
| F051 | `Golden Supercar 🏆` | 39 | "The best car in the game, yours to keep. Drive it on The Loop." | 3715639484 | 2026-09-30T14:45:53.708Z | 同上 | S | 2026-10-09 T1 |
| F052 | `Retake Test` | 19 | "Failed your driving test? Take it again right away, no line." | 3717235859 | 2026-10-08T12:07:01.007Z | 同上 | S | 2026-10-09 T1 |
| F053 | 13 个商品合计 | 542 Robux(各买一次,我们计算);最低 9(5 个:Skip Line [SALE]、Skip Time [SALE]、Kill、Revenge ⚡、+1 Minute),最高 160(Kill All) | 同上 | S(推导) | 2026-10-09 T1 |
| F054 | 名称带 `[SALE]` 但接口无折扣记录 | Skip Line [SALE]、Skip Time [SALE] 两个商品 `PriceDiscountDetails: []`,`UserBasePriceInRobux` = `PriceInRobux` = 9 | 同上 | S | 2026-10-09 T1 |
| F055 | 上架时间线(商品 / 通行证创建与编辑时刻) | 2026-09-29 08:24 UTC 体验创建 → 2026-09-30 06:18–06:19 UTC 前 11 个商品与 5 个通行证 → 2026-09-30 14:45 UTC Golden Supercar 🏆 创建 → **2026-10-05 20:24 UTC Golden Supercar 🏆 被编辑**(见 F059)→ 2026-10-08 12:07 UTC Retake Test 创建 | 上述两个接口 + games v1 | S | 2026-10-09 T1 |
| F056 | 考官时长单价(我们计算) | Be The Examiner 📋:29 Robux ÷ 5 分钟 = 5.8 Robux / 分钟;+1 Minute:9 Robux / 分钟;连买 10 分钟 = 29 + 5×9 = 74 Robux | 同上 | S(推导) | 2026-10-09 T1 |
| F057 | 排队类单价(我们计算) | Skip Line [SALE]:9 Robux ÷ 5 位 = 1.8 Robux / 位;Kill:9 Robux 处理前面 1 人;Skip Time [SALE]:9 Robux ÷ 150 秒 | 同上 | S(推导) | 2026-10-09 T1 |
| F059 | `Updated` 字段(round1 补记:首版漏读) | 13 个商品里 12 个 `Updated` = `Created`;唯一例外 `Golden Supercar 🏆`:Created `2026-09-30T14:45:53.708Z`,Updated `2026-10-05T20:24:33.119Z`(改了什么接口不记录)。5 个通行证 `updated` = `created`。所以商店至少有 3 个变更事件(2 次新增 + 1 次编辑),页面不再写「changed twice」 | 同上(raw/devproducts.json、raw/gamepasses.json) | S | 2026-10-09 T1 |
| F058 | 商品描述里出现的专名 | `the line`、`the waiting room`、`written test`、`driving test`、`driving examiner` / `the examiner`、`Epic`(车的档位,"Epic or better" 说明其上还有档)、`Ticket #001`、`The Loop`(可开 Golden Supercar 的地点名) | 同上 | S | 2026-10-09 T1 |

## 5. 徽章、官方活动、兑换码(全部为 0)

| # | 事实 | 值 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F060 | 徽章数 | **0**。`data: []`、`nextPageCursor: null`;按 SKILL「badges 结论前复查」口径共取 4 次(T1 Asc、T2 Asc、T2 Desc、T5 Asc),四次均为空 | https://badges.roblox.com/v1/universes/10768565603/badges?limit=100&sortOrder=Asc | S | 2026-10-09 T1/T2 |
| F061 | 官方活动(virtual-events) | **0 条**。不带游标与带零起点游标两种取法均 `data: []` | https://apis.roblox.com/virtual-events/v1/universes/10768565603/virtual-events ;同 URL 加 `?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA` | S | 2026-10-09 T1 |
| F062 | 兑换码 | **0 个**。官方描述(F020–F027)无码;群组 description 空串、shout null(F071、F072);没有任何官方来源出现码 → 不建 codes 页,任何页不写码 | 见 F028、F071、F072 | S | 2026-10-09 T1 |
| F063 | 群组置顶活动 | `null` | https://groups.roblox.com/v1/featured-content/event?groupId=356677783 | S | 2026-10-09 T4 |

## 6. 开发者群组

| # | 事实 | 值 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F070 | 群组名 / id | `Time Will Pass` / 356677783;name-history 接口 `data: []`(无改名记录) | https://groups.roblox.com/v1/groups/356677783 ;https://groups.roblox.com/v1/groups/356677783/name-history?limit=10 | S | 2026-10-09 T1/T4 |
| F071 | 群组 description | 空串 `""` | https://groups.roblox.com/v1/groups/356677783 | S | 2026-10-09 T1 |
| F072 | 群组 shout | `null` | 同上 | S | 2026-10-09 T1 |
| F073 | 成员数 | T1(11:11:22)groups v1:795,647;T2(11:13)roles 接口 Member 角色 796,013;T4(11:18)用户群组列表接口 798,008;**T5(11:28:57)同一个 groups v1 接口复读:801,043**。同一接口约 18 分钟涨 5,396(801,043−795,647,我们计算)→ community 页写两次读数与差值,其它页写 about 800,000 并注明是快照。增长原因无一手来源,不写 | https://groups.roblox.com/v1/groups/356677783 ;https://groups.roblox.com/v1/groups/356677783/roles ;https://groups.roblox.com/v2/users/10383353739/groups/roles | S | 2026-10-09 T1/T2/T4 |
| F074 | 群组创建时间 | `2026-09-27T11:55:07.373Z` → 27 September 2026(比本游戏创建早 2 天) | https://groups.roblox.com/v2/groups?groupIds=356677783 | S | 2026-10-09 T4 |
| F075 | 群主 | userId 10383353739,username `DiveAndThrive`,displayName `Waiting`,hasVerifiedBadge=false;账号创建 `2026-01-21T17:00:04.701Z`,个人 description 空串 | https://groups.roblox.com/v1/groups/356677783 `owner`;https://users.roblox.com/v1/users/10383353739 | S | 2026-10-09 T1/T2 |
| F076 | 加入方式 | `publicEntryAllowed: true`(任何人可加入);hasVerifiedBadge=false | https://groups.roblox.com/v1/groups/356677783 | S | 2026-10-09 T1 |
| F077 | 角色 | Guest(0 人)、Member(796,013,基础角色)、stats(2)、stats(0)、Dev(1)、Admin(2) | https://groups.roblox.com/v1/groups/356677783/roles | S | 2026-10-09 T2 |
| F078 | 群组 wall | v1 与 v2 的 wall/posts 都返回 404(原因不明,不归因为需登录) | https://groups.roblox.com/v2/groups/356677783/wall/posts?limit=10&sortOrder=Desc | S | 2026-10-09 T2/T4 |
| F079 | 群组 / 游戏 social links | 两个接口匿名请求都返回 401 "Authentication token is missing" → 官方 Discord、X、YouTube 是否存在**未获取** | https://groups.roblox.com/v1/groups/356677783/social-links ;https://games.roblox.com/v1/games/10768565603/social-links/list | S | 2026-10-09 T1/T2 |
| F080 | 同组公开体验(共 5 个,nextPageCursor null) | 见下表 | https://games.roblox.com/v2/groups/356677783/gamesV2?accessFilter=2&limit=100&sortOrder=Asc | S | 2026-10-09 T1 |

同组体验(F080 明细;名称逐字,placeVisits 为 T1 值):

| 名称(逐字) | universeId | created(UTC) | placeVisits | 描述首句(逐字) |
|---|---|---|---|---|
| `Hold It In 🚽` | 10768310363 | 2026-09-27T13:20:42.897Z | 40,822 | "🚽 You REALLY need to go... and the only restroom is on the TOP floor of the mall!" |
| `Don't Be Late For Work! ⏰` | 10768351352 | 2026-09-27T17:45:48.573Z | 864,877 | "⏰ You overslept... it's 8:47 and work starts at 9:00!" |
| `Next Prisoner` | 10768409691 | 2026-09-28T03:30:14.923Z | 22,037 | "You stole ONE mango. Now you're going to prison. 🥭🚔" |
| `Next Subject` | 10768448776 | 2026-09-28T13:12:34.427Z | 331,342 | (description 为 null) |
| `Get Your Driver's License!` | 10768565603 | 2026-09-29T08:24:37.26Z | 4,755,987 | "Wait in line and get your Driver's License!" |

## 7. 官方图片(本人看图抄录;都是宣传美术,不是实机截图)

| # | 事实 | 值 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F090 | 游戏页宣传图(唯一 1 张,16:9) | 车内视角:左边一个黑发、八字胡、红色 polo 衫的角色怒指右边,手里的写字板上是红圈里的大写 **F**;右边蓝色连帽衫、橙棕色头发的角色抱头流泪,双手离开方向盘;窗外一块牌子写 **DRIVING SCHOOL** 并画着一辆小车,远处有橙色锥桶 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=10768565603&countPerUniverse=10&size=768x432&format=Png → https://tr.rbxcdn.com/180DAY-292b9310361cd23209c4272964fcff4a/768/432/Image/Png/noFilter | S | 2026-10-09 T1 |
| F091 | 游戏图标(512x512) | 蓝色连帽衫、橙棕色头发的角色笑着举起一张卡片,卡片抬头 **DRIVER LICENSE**,带头像与绿色对勾;背景是 **DRIVING SCHOOL** 牌子、一辆车顶有红色 **L** 牌的红色小车、两个橙色锥桶 | https://thumbnails.roblox.com/v1/games/icons?universeIds=10768565603&size=512x512&format=Png → https://tr.rbxcdn.com/180DAY-d4c5777def995052ac489614139a44c9/512/512/Image/Png/noFilter | S | 2026-10-09 T1 |
| F092 | 通行证图标 5 张(420x420) | PRO EMOJI PACK 😈:紫色带角坏笑表情,后面两个黄色表情;Ban Hammer:深色大锤;Time Out:一副手铐;Gravity Gun 🔥:紫色漩涡带白色星芒;Airhorn [ANNOYING] ☠️:白罐红喇叭的气笛 | https://thumbnails.roblox.com/v1/assets?assetIds=73260523707418,71583720567452,133611055833620,92809346914354,104491280702785&size=420x420&format=Png | S | 2026-10-09 T2 |
| F093 | 商品图标 13 张(420x420;Skip Line [SALE] 与 Skip Time [SALE] 是同一张图,同一 CDN 哈希) | Skip Line / Skip Time:绿色双箭头快进;Skip Test:写着红色 A+ 的试卷加绿色快进角标;Skip To End:黑白格旗加绿色快进角标;Kill:深色底上的红色拳套;Kill All:黄底红色警铃;Scare All:白色幽灵与 BOO! 字样;Revenge ⚡:红底黄色闪电;Be The Examiner 📋:写字板上两个绿勾一个红叉加一支铅笔;+1 Minute:秒表加绿色 +1;VIP Ticket 🎟️:金色票券写 **#001** 带星;Golden Supercar 🏆:深蓝地面上一辆金色楔形低多边形跑车;Retake Test:方向盘加橙色重试箭头 | https://thumbnails.roblox.com/v1/assets?assetIds=83594712941098,118857276237629,105328531977019,90157103137595,71569432380463,102398161320664,84707369106912,99444745706344,136984438178136,76945416388444,104038954481377,95039828332574,109600651257969&size=420x420&format=Png | S | 2026-10-09 T2 |
| F094 | 图片里有没有真实汽车品牌 | 没有。宣传图与图标里的车没有任何厂标或车型字样;正文与 alt 只用通用词(hatchback、supercar、car) | F090–F093 的图 | S | 2026-10-09 T1/T2 |

## 8. Roblox 平台机制(只引官方文档原文)

| # | 事实 | 原文(逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F100 | 通行证定义 | "Passes let you charge users a one-time Robux fee to access special privileges inside your game, such as entry to a restricted area, an in-game avatar item, or a permanent power-up." | https://create.roblox.com/docs/production/monetization/passes | S | 2026-10-09 T4 |
| F101 | 开发者商品定义 | "A developer product is an item or ability that a user can purchase more than once, such as in-game currency, ammo, or potions." | https://create.roblox.com/docs/production/monetization/developer-products | S | 2026-10-09 T4 |
| F102 | 社交链接可见性 | "Social media links are only visible to users who have verified their age as at least 16 years old." | https://create.roblox.com/docs/production/promotion/social-media-links | S | 2026-10-09 T4 |
| F103 | Minimal 分级说明 | 表格行:Minimal → "May contain occasional mild violence and/or light unrealistic blood." | https://create.roblox.com/docs/production/promotion/content-maturity | S | 2026-10-09 T4 |

## 9. 第三方(B 级;只作旁证,页面上出现时标明出处)

| # | 事实 | 值 | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F110 | Rolimon's 统计页 | Players 18,488;Visits 4,753,474;Upvotes 4,663;Downvotes 8,288;Rating 36.005%;Favorites 18,021;Average Playtime 10.06 Minutes;All-Time Peak CCU 24,263(「9 hours ago」);「This game has no known badges」;列 5 个通行证,价格与 F030–F034 一致 | https://www.rolimons.com/game/104416416393862 | B | 2026-10-09 T3 |
| F111 | Rotrends 统计页 | Global #159;Peak CCU 24.2K;Rating 36%;Avg Session 11.0 mins;Genre Simulation / Subgenre Idle;Maturity All Ages;Up-and-Coming 榜 #37(Oct 6, 2026);Game Passes 5 passes;Dev Products **12 products**(比我们 T1 取到的 13 少 1,Retake Test 是 10-08 新增) | https://rotrends.com/game/10768565603 | B | 2026-10-09 T3 |
| F112 | 攻略 / 码站覆盖 | 未检索到任何一篇。WebSearch 4 组查询(游戏名 + codes / cars / endings / written test answers / wiki)结果全是别的驾驶游戏或真实驾考资料;robloxden / tryhardguides / beebom / pockettactics 的猜测 URL 返回 404,progameguides 返回 403 | 见 `raw/fetch-log.txt` | — | 2026-10-09 T3 |
| F113 | Fandom | 6 个可能的子域(get-your-drivers-license / getyourdriverslicense / get-your-driver-s-license / gydl / time-will-pass / timewillpass .fandom.com)api.php 全部 404 | 见 `raw/fetch-log.txt` | — | 2026-10-09 T3 |
| F114 | Google 下拉 | 27 组前缀里 25 组返回空数组(24 组带游戏名的 + `time will pass roblox`);只有泛词 `roblox drivers license game` 返回 2 条(roblox drivers license game、roblox drivers test game);`get your driver's license! ` 返回的 10 条全是真实驾照词,与游戏无关 | https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=… (`raw/suggest.jsonl`) | B(需求证据) | 2026-10-09 T3 |

## 10. 互相矛盾

| 项 | 值 A | 值 B | 处理 |
|---|---|---|---|
| `updated` 字段 | games v1:2026-10-08T18:36:30Z | gamesV2 / develop:2026-10-08T15:24:03Z | 两个都不当更新日;「上线后新增了什么」只用商品创建时刻(F055) |
| 开发者商品数 | Roblox 接口 13(T1) | Rotrends 12 | 以 Roblox 接口为准;差的那个是 10-08 才创建的 Retake Test |
| 点踩数 | Roblox 接口 8,278(T1) | Rolimon's 8,288 | 以 Roblox 接口为准(两边取数时刻不同) |
| 群组成员数 | 795,647(T1) | 796,013(T2)/ 798,008(T4)/ 801,043(T5) | 增长中;community 页写 T1 与 T5 两个读数,其它页写 about 800,000 并标日期 |

## 11. 未核实(没有任何一手来源;正文不写具体值)

| 项 | 现状 | 页面处理 |
|---|---|---|
| 18 辆车的名字、稀有度分档名单、各档概率 | 官方只给数量 18、两端措辞、档位名 Epic(且其上还有档) | cars 页只写这些,其余列入待进游戏核实 |
| Golden Supercar 是否算在 18 辆之内;「yours to keep」是否意味着别的车不保留 | 商品描述只有一句 | cars 页明写「描述没说」 |
| The Loop 是什么、怎么去 | 只有地点名 | cars 页明写 not published |
| 全部结局名单与触发条件 | 只有 Honor Roll 与 Towed 两个名字;「from … to …」暗示一头一尾但官方没排序 | driving-test 页只列这两个名字,不解释触发条件 |
| 笔试题目、题数、及格线、答案 | 0 来源 | 不写;how-to-play / waiting-line 只写「有笔试、Skip Test 可直接通过」 |
| 考场路线、障碍位置、扣分规则 | 只有 cows / ducks / ramps 三个名词 | driving-test 页不写路线 |
| 不花 Robux 能否当考官;考官的打分界面;考官打分是否决定结局 | 描述说可以当考官;商品卖 5 分钟 | driving-test 页写「描述没说是否有免费途径」 |
| 排队人数、等候室总时长、取号规则、队伍是否只由同服真人玩家组成 | 只有「往前 5 位」「跳过 2:30」与单服 25 人这个事实 | waiting-line 页只做价格算术,不写队伍长度、不写总时长 |
| 一局的先后顺序;是否每局(或只有通过的一局)都给车 / 结局;不付费能否通关 | 官方描述只是功能清单;我们没有玩过 | 各页写「the description lists …」「no description says a purchase is required, but we have not played a full run without paying」 |
| 「goes poof」之后那个人去哪(回队尾 / 重生) | 0 来源 | 明写 not stated |
| 「knocked you out」是谁、用什么打的 | Revenge ⚡ 描述只有一句;Ban Hammer 描述是 "Bonk people" 但没说会击倒 | 不把两者连起来写成确认 |
| PRO EMOJI PACK 里有哪些表情、免费表情有没有 | 0 来源 | 写 not listed |
| 兑换码系统是否存在 | 官方来源 0 个码 | 不建 codes 页;index 一节说明原因 |
| 官方 Discord / X / YouTube | social links 接口 401 | community 页写无法匿名读取,引 F102 原文 |
| 支持设备、私服 | 匿名接口读不到 / 字段不可用 | 不写结论 |
| 平均一局时长 | 只有 B 级(Rolimon's 10.06 分钟、Rotrends 11.0 分钟) | 仅在 how-to-play 一句话标明第三方统计 |
| 游戏内实测 | **没有进游戏** | 所有「界面长什么样」的描述都来自官方图并注明 |
