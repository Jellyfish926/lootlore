# Untitled Wheelie Game 事实底稿（dossier）

取证日：2026-09-30（UTC 约 11:11-11:14 抓取；快照型数字只代表这一刻）
范围：Roblox 体验「Untitled Wheelie Game (🚔)」，universeId 10268960646，rootPlaceId 93844268955707。
原始抓取文件（来源笔记，供复核）：`raw/`（games.json / votes.json / badges.json / passes.json / passes_legacy.json / devprod.json / media.json / thumbs.json / thumbs_small.json / icons.json / group.json / group_games.json / roles.json / age.json / places.json / social.json / group_social.json / wall.json / place.json / gamepage.html / suggest.txt / search_testing.json / other_wheelie_district.json / art01.png / art02.png / icon.png）。

来源分级：S = Roblox 官方 API / 官方页面（开发者自己在 Roblox 上登记的数据）；A = 开发者官方群组公告 / 官方 Discord 公告 / 官方 wiki（本次**无**：群组无 shout，wall 接口 NotFound，Discord 链接拿不到）；B = 大型第三方；C = 其他，只当线索。

**同名混淆警告**：Roblox 上另有一款「[AI COPS + MORE👮] Wheelie District 🏍️」（universeId 9765324104，创作者群组 Wheelie District Studios，已认证，2026-02-20 创建，https://games.roblox.com/v1/games?universeIds=9765324104 ，S）。它也主打「AI COPS」，搜索结果里 pcgamesn / pockettactics / gamingdose 的 codes 页全是它，**不是本游戏**，任何 Wheelie District 的码与内容一律不采用。

## 1. 基本信息

| # | 事实 | 值 | 来源 | 级 |
|---|---|---|---|---|
| 1 | 正式名 | Untitled Wheelie Game (🚔) | https://games.roblox.com/v1/games?universeIds=10268960646 `name` | S |
| 2 | 创作者 | 群组 Untitled Wheelie Group（groupId 84540135），类型 Group，无认证标 | 同上 `creator` | S |
| 3 | 创建时间 | 2026-06-04T06:53:02Z | 同上 `created` | S |
| 4 | 最近更新 | 2026-09-30T02:34:41Z | 同上 `updated` | S |
| 5 | 类型 | Simulation › Vehicle Sim | 同上 `genre_l1/genre_l2` | S |
| 6 | 单服人数上限 | 10 | 同上 `maxPlayers` | S |
| 7 | 价格 | 免费（price = null） | 同上 | S |
| 8 | 私服 | 不开放（createVipServersAllowed = false） | 同上 | S |
| 9 | 访问量（快照） | 27,360,884 visits | 同上 | S |
| 10 | 在线（快照） | 1,841 playing（另一次 search API 读到 1,843） | 同上 | S |
| 11 | 收藏（快照） | 708,056 | 同上 `favoritedCount` | S |
| 12 | 点赞/点踩（快照） | 49,128 / 3,068（点赞占比 94.1%，我们计算） | https://games.roblox.com/v1/games/votes?universeIds=10268960646 | S |
| 13 | 头像类型 | MorphToR15 | games API `universeAvatarType` | S |
| 14 | 内容分级 | Maturity: Minimal；descriptor「Suitable for everyone」 | POST https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation body {"universeId":"10268960646"} | S |
| 15 | 徽章 | 0 个（data 空数组） | https://badges.roblox.com/v1/universes/10268960646/badges?limit=100 | S |
| 16 | 群组描述 | "Official Group" | https://groups.roblox.com/v1/groups/84540135 | S |
| 17 | 群组所有者 | username fireblock373（displayName fire，未认证） | 同上 | S |
| 18 | 群组成员（快照） | 703,842 | 同上 `memberCount` | S |
| 19 | 群组公告 shout | 无（null）；公开加入 publicEntryAllowed = true | 同上 | S |
| 20 | 群组角色 | Guest / Member / Members / Content Creator（10 人）/ Tester（rank 253，1 人）/ Admin（0 人）/ Owner（1 人） | https://groups.roblox.com/v1/groups/84540135/roles | S |
| 21 | 群组公开游戏 | 只有本游戏一款（不带过滤时群下共 34 个 universe，另 33 个非公开、访问合计 40，raw/group_games_all.json） | https://games.roblox.com/v2/groups/84540135/games?accessFilter=Public&limit=50 | S |
| 22 | 体验内 place | 主 place 93844268955707 + 一个 "fireblock373's Place: 07092026_1"（138649466891207，用途未知，不写） | https://develop.roblox.com/v1/universes/10268960646/places?limit=50 | S |

## 2. 玩法（官方描述原文逐句）

来源：https://games.roblox.com/v1/games?universeIds=10268960646 `description`（S）

| # | 原文 | 我们可以写的 |
|---|---|---|
| 23 | "Wheelie around the map, ride with your friends, and experience realistic wheelie physics with interactive traffic." | 核心是抬前轮骑行 + 有交通车流 |
| 24 | "🚔 RUN FROM COPS" | 有警察追逐 |
| 25 | "🏍️ Wheelie around the map" | — |
| 26 | "🚦 Swerve through oncoming traffic" | 有对向车流 |
| 27 | "💰 Deliver pizzas to earn money" | 送披萨赚钱（官方唯一点名的赚钱方式） |
| 28 | "🛠️ Buy bikes, upgrades, and parts" | 可买车、升级、零件 |
| 29 | "🎨 Paint and customize your bike" | 可涂装/改装 |
| 30 | "🏁 Race your friends" | 可和朋友比赛 |
| 31 | "🤝 Host rideouts with other players" | 可组织 rideout（多人结伴骑行） |
| 32 | "🎯 Practice tricks and improve your wheelies" | 可练特技 |
| 33 | "Our wheelie physics are designed to feel as realistic as possible, with a realistic balance point and responsive throttle and brake physics." | 平衡点 + 油门 + 刹车决定抬头 |
| 34 | "Whether you want to cruise around with friends, weave through traffic, build your dream bike, or see how long you can hold a wheelie, there is always something to do." | — |

未获取：具体按键/手柄/手机操作（官方描述未写；Google 下拉有 "controls pc" 需求，但无 S/A 来源）；地图名；车辆完整清单与属性；罚款金额；送披萨报酬。

## 3. 通行证（12 个，全部官方）

来源：https://apis.roblox.com/game-passes/v1/universes/10268960646/game-passes?passView=Full&pageSize=100（S）。
（旧接口 https://games.roblox.com/v1/games/10268960646/game-passes?limit=100 返回 errors code 0，未获取，以新接口为准。）
名称逐字复制 `name` 字段（含 emoji）；价格为 `price`（Robux）；isForSale=false 的 price 为 null。

| # | 名称 | Robux | 在售 | 官方描述 | 创建 | 最后更新 | passId |
|---|---|---|---|---|---|---|---|
| 35 | Bike Customization | — | 否 | Customize the color of your bike. | 2026-06-05 | 2026-08-12 | 1865410310 |
| 36 | Extra Bike Speed | — | 否 | Adds speed to your bike | 2026-06-06 | 2026-08-12 | 1867464419 |
| 37 | X2 Wheelie Earning 💰 | 199 | 是 | （空） | 2026-06-20 | 2026-08-12 | 1884191223 |
| 38 | X3 Wheelie Earning 💰 | 299 | 是 | （空） | 2026-06-20 | 2026-08-12 | 1883687170 |
| 39 | X2 Job Earning 💰 | 299 | 是 | （空） | 2026-06-20 | 2026-08-12 | 1882859227 |
| 40 | X3 Job Earning 💰 | 499 | 是 | （空） | 2026-06-20 | 2026-08-12 | 1882841193 |
| 41 | More Helmets 🪖 | 99 | 是 | （空） | 2026-06-20 | 2026-08-12 | 1882955253 |
| 42 | Free Subway Travel 🚇 | 99 | 是 | （空） | 2026-06-20 | 2026-08-12 | 1882673259 |
| 43 | Eblox Dragster | — | 否 | （空） | 2026-06-27 | 2026-08-12 | 1890749586 |
| 44 | Tuttiro Bike | — | 否 | （空） | 2026-07-01 | 2026-08-12 | 1898310743 |
| 45 | EBike Pack ⚡ | — | 否 | Gives you all Ebikes in the game. (Not Emotos) | 2026-08-15 | 2026-08-15 | 1948772710 |
| 46 | NEVER PAY FINES | 149 | 是 | Just never have to pay fines for when you get caught | 2026-09-26 | 2026-09-26 | 1999880596 |

推导（页面上注明是推导/我们的解读）：
- 47 在售 7 个，合计 1,643 Robux（我们计算：199+299+299+499+99+99+149）；下架 5 个。
- 48 "Wheelie Earning" 与 "Job Earning" 两组倍率通行证 → 游戏里至少有「抬头赚钱」和「工作赚钱」两类收入（按通行证名推断，官方未写细则）。倍率是否叠加、X3 是否包含 X2，未说明。
- 49 "EBike Pack" 描述 "(Not Emotos)" → 游戏把电动车分为 Ebikes 与 Emotos 两类（官方描述原文可证两类名称存在）。
- 50 "NEVER PAY FINES" 描述 → 被抓会被罚款（S，原文 "fines for when you get caught"）。罚款金额未获取。
- 51 "Free Subway Travel" → 地图里有地铁；按名字推断地铁通常要付费，票价未获取。
- 52 下架通行证现在能否以其他方式获得：未获取。

## 4. 开发者商品（23 个，全部官方）

来源：https://apis.roblox.com/developer-products/v2/universes/10268960646/developerproducts?limit=100（S）。描述字段全部为空。

| # | 名称 | Robux | 在售 | 创建 |
|---|---|---|---|---|
| 53 | 10 Robux / 25 Robux / 100 Robux / 250 Robux / 500 Robux / 1,000 Robux / 5,000 Robux / 10,000 Robux / 25,000 Robux / 50,000 Robux / 100,000 Robux / 1,000,000 Robux | 与名称相同 | 是 | 2026-06-04 |
| 54 | 50 Robux | —（null） | 否 | 2026-06-04 |
| 55 | $750 | 49 | 是 | 2026-06-25 |
| 56 | $2,250 | 99 | 是 | 2026-06-25 |
| 57 | $5,000 | 199 | 是 | 2026-06-25 |
| 58 | $13,500 | 399 | 是 | 2026-06-25 |
| 59 | $30,000 | 799 | 是 | 2026-06-25 |
| 60 | $67,500 | 1499 | 是 | 2026-06-25 |
| 61 | INSTALL BACKFIRE | 25 | 是 | 2026-09-04 |
| 62 | LEVEL 2 BACKFIRE | 30 | 是 | 2026-09-04 |
| 63 | LEVEL 3 BACKFIRE | 40 | 是 | 2026-09-04 |
| 64 | AVOID FINES | 13 | 是 | 2026-09-21 |

推导：
- 65 "$" 命名的 6 个商品按名字是游戏内现金包（官方无描述；游戏描述说送披萨 "earn money"）。每 Robux 换到的现金（我们计算）：15.3 / 22.7 / 25.1 / 33.8 / 37.5 / 45.0，越大包越划算。
- 66 以 Robux 数额命名的 13 个商品用途未说明（名字像打赏档位，但官方没写），正文只说「用途未说明」。
- 67 BACKFIRE 三档：安装 + 2 级 + 3 级，作用官方未描述。
- 68 AVOID FINES 13 Robux vs NEVER PAY FINES 149 Robux：149 ÷ 13 ≈ 11.5 —— **假如** AVOID FINES 只免一次罚款，第 12 次起通行证更划算（条件推导，AVOID FINES 覆盖范围未说明）。

## 5. 更新时间线（由官方创建/更新时间戳拼出，不等于补丁说明）

| 日期（2026） | 出现了什么 | 来源 |
|---|---|---|
| 06-04 | 体验创建；13 个 Robux 数额商品 | games API / devprod |
| 06-05 | Bike Customization 通行证 | passes |
| 06-06 | Extra Bike Speed 通行证 | passes |
| 06-20 | X2/X3 Wheelie Earning、X2/X3 Job Earning、More Helmets、Free Subway Travel | passes |
| 06-25 | 6 个现金包 | devprod |
| 06-27 | Eblox Dragster 通行证 | passes |
| 07-01 | Tuttiro Bike 通行证 | passes |
| 08-12 | 当时的 10 个通行证记录同日被编辑（updated 戳） | passes |
| 08-15 | EBike Pack ⚡ | passes |
| 09-04 | INSTALL / LEVEL 2 / LEVEL 3 BACKFIRE | devprod |
| 09-21 | AVOID FINES | devprod |
| 09-26 | NEVER PAY FINES | passes |
| 09-30 | 体验页 updated 02:34 UTC | games API |

## 6. 图片（S）

| # | 事实 | 来源 |
|---|---|---|
| 69 | 游戏页 2 张宣传图：imageId 97897289381980、119853287473264，altText 为空 | https://games.roblox.com/v2/games/10268960646/media |
| 70 | 768x432 与 480x270 两档 URL，均 curl 200（2026-09-30） | thumbnails multiget 接口 |
| 71 | 图 1 画面：戴黑头盔的 Roblox 角色骑小型越野/迷你摩托抬前轮，身后两辆警车亮灯追来，大字 "AI COPS" + 红色箭头 | 亲眼看 raw/art01.png |
| 72 | 图 2 画面：同一角色骑黑红迷你摩托在高速路抬前轮，后方黄色跑车，右上红色感叹号 | raw/art02.png |
| 73 | 图标 512x512：与图 2 同一构图的方图 | https://thumbnails.roblox.com/v1/games/icons?universeIds=10268960646&size=512x512&format=Png |

「AI COPS」是官方宣传图上的文字，可写成「官方宣传图标注 AI COPS」，不写成「警察是 AI 控制的已确认机制」之外的细节。

## 7. 兑换码 / 社媒（结论：不建 codes 页）

| # | 事实 | 来源 | 级 |
|---|---|---|---|
| 74 | 游戏描述无任何码 | games API description | S |
| 75 | 群组 shout = null；群组描述只有 "Official Group" | groups API | S |
| 76 | 群组 wall 接口返回 NotFound（v1 与 v2） | https://groups.roblox.com/v2/groups/84540135/wall/posts | S（结果为空） |
| 77 | 体验 social links / 群组 social links 接口要求登录（code 9002），游戏页 HTML 里未见 Discord/YouTube 链接 | https://games.roblox.com/v1/games/10268960646/social-links/list | 未获取 |
| 77b | 第三方码页（progameguides、destructoid）链接 Discord 邀请 discord.com/invite/QHuDU7GHSB；邀请 API 显示服务器名 "Untitled Wheelie Game Official"、邀请人 username fireblock373（global_name Fire），与 Roblox 群主同名，成员约 4,046 | https://discord.com/api/v9/invites/QHuDU7GHSB?with_counts=true（raw/discord_invite.json，第4步复核后补） | B（强佐证，非 Roblox 站内自证；不写成已确认官方，不加超链接） |
| 78 | 第三方码页（progameguides / nerdschalk / allthings.how）一致列 1 个 active 现金码 + 2 个过期码，自称来自官方群组与 Discord | 这三家页面（2026-09-30 WebFetch） | B/C，未见一手出处 → 不收 |

## 8. 需求证据（Google 下拉，2026-09-30 实测，raw/suggest.txt）

untitled wheelie game script / codes / discord / testing / roblox / controls / controls pc / codes roblox / testing discord；how to wheelie in untitled wheelie game；best bike in untitled wheelie game；how to sell bikes in untitled wheelie game roblox。
搜索量：未获取（禁用 Semrush；未估算）。

## 9. 未获取项汇总

- 操作按键（PC/手机/手柄）、"how to wheelie" 的具体输入 —— 无 S/A 来源
- 车辆完整清单、价格（游戏币）、属性、"best bike"、如何卖车 —— 无来源
- 罚款金额、警察追逐规则、地图名、地铁票价、送披萨报酬 —— 无来源
- 官方 Discord 链接与 Discord 公告 —— social links 接口需登录
- 兑换码 —— 无官方来源亲眼所见
- "testing" 版本 —— Roblox 搜索只返回本体（raw/search_testing.json），群组仅有 1 名 Tester 角色成员
- 支持设备（需登录接口）
