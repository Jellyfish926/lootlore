# One Tap 事实底稿(dossier)

取证日:2026-10-10(UTC 11:39–11:44 抓取;快照型数字只代表那一刻)。四个时间点:**T1** = 11:39:01–11:39:10 UTC(games / votes / favorites / media / game-passes / developer-products / badges ×2 / virtual-events ×2 / thumbnails / icon / social-links / supported-languages / age),**T2** = 11:39:48–11:40:15 UTC(group v1 / v2 / roles / 群组游戏列表 / wall / 群组 social-links / place→universe / 公开服务器 / playability / 活动游标翻页 ×2 / eventStatus=completed / 通行证与商品图标 / 活动配图 / 游戏页 HTML / 群组页 HTML / develop / owner / 群组活动接口 / place-details),**T3** = 11:41:54–11:42:30 UTC(Roblox 官方文档 create.roblox.com;两个抢注站首页 / sitemap / robots / 各 3 个内页),**T4** = 11:43:35–11:43:39 UTC(Google 下拉 28 组、6 个 Fandom 子域探测、games / votes / group / badges 复读、旧通行证接口、vip-servers 接口)。每个 URL 的 HTTP 状态与时刻在 `raw/fetch-log.txt`。
范围:Roblox 体验「[FPS] One Tap」,universeId 9294074907,rootPlaceId 90568084448279,创作者群组 Stringless Banjo(groupId 1047647644)。群组公开游戏列表只有这一个体验。
原始抓取文件:`raw/`(接口原文 JSON;`raw/img/` 是本人看图用的下载件与 `pool.json`;`raw/comp/` 是两个抢注站与 Fandom 探测;`raw/docs/` 是 Roblox 官方文档 HTML 与 .md;`raw/suggest.jsonl` 是 Google 下拉原始返回;`raw/image-check.txt` 是图片 URL 验 200 记录)。

来源分级(按任务口径):**S** = Roblox 官方接口返回值 / 游戏页 description 原文 / 官方群组 description 与 shout / 官方活动(virtual-events)文本 / 官方图(图内文字本人看图抄录)/ Roblox 官方文档 create.roblox.com;**A** = 开发者本人公开发言(本次 **0 条**独立于 S 的 A 级来源:群组 shout 为 null、wall 接口 404、social links 两个接口 401;开发者的原话全部已经在 S 级的 description 与 6 条活动文本里);**B** = 成熟社区 wiki(本次 **0 条**:6 个可能的 Fandom 子域 api.php 全 404);**C** = 其他(onetap.wiki、onetaproblox.wiki 两个抢注站,只看了栏目结构,**数据一条不采信**;Google 下拉只作需求证据)。

结论:S 级素材 = 一段 18 行的官方描述 + 4 个通行证(description 全空,图标上各有一句官方说明)+ 97 个开发者商品(Description 全空,只有名称 / 价格 / 创建与编辑时间)+ 6 条官方活动文本(其中 Update 2 有 12 行内容清单、Update 有 6 行)+ 群组资料 + 4 张官方 16:9 图 + 3 张可用活动图。**没有任何一手来源的**:武器数值、箱子内容与概率、地图名、任务清单、等级奖励表、战令层数与赛季时长、Gems / Sun Points 每包数量、兑换码、官方 Discord。徽章 0 个。这些全部进第 11 节「未核实」,正文写 not stated by the developer / not confirmed 或不写。

**写作口径(自查五类,2026-10-09 skill 补充)**:① 官方描述是功能清单,不写一局流程、不写必得奖励;② 不由范围反推具体值(`70+` 不写成 70;`Two-Shot … (One to the head)` 不写血量与伤害数字;`2x Case Luck` 图标写的是 `more luck`,不写成概率翻倍);③ 活动 listing 只写「listed from … to …」,不写成实际上线时刻;商品记录的 Created / Updated 只写「record created / edited」;④ 不写任何 Discord 邀请;⑤ 「接口返回 97 条且 nextPageCursor=null」写成「the records we read held 97」,标题用计数不用 Every;`IsForSale=true` 不等于游戏内商店此刻在卖。另:官方描述第 8 行含 `(more coming soon)`,总站门禁 `check_content` 把 coming soon 当占位语**阻塞**,所以页面与 entities.json 只引到 `Unlock 70+ weapon skins` 并用自己的话转述括号内容,本底稿保留原文。

## 1. 基本信息

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F001 | Roblox 上的显示名 | `[FPS] One Tap`(描述正文自称 `One Tap`) | https://games.roblox.com/v1/games?universeIds=9294074907 `name` | S | 2026-10-10 T1 |
| F002 | universeId / rootPlaceId | 9294074907 / 90568084448279(places→universe 接口回 `{"universeId":9294074907}`,互相印证) | https://games.roblox.com/v1/games?universeIds=9294074907 ;https://apis.roblox.com/universes/v1/places/90568084448279/universe | S | 2026-10-10 T1 |
| F003 | 创作者 | 群组 `Stringless Banjo`(id 1047647644,type Group,hasVerifiedBadge=false) | https://games.roblox.com/v1/games?universeIds=9294074907 `creator` | S | 2026-10-10 T1 |
| F004 | 创建时间(games v1) | `2025-12-04T00:44:19.27Z` → 4 December 2025 | https://games.roblox.com/v1/games?universeIds=9294074907 `created` | S | 2026-10-10 T1 |
| F005 | 创建时间(群组游戏列表 / develop 接口) | `2025-12-04T00:44:19.39Z`(与 games v1 差 0.12 秒,同一天;页面引用 games v1) | https://games.roblox.com/v2/groups/1047647644/gamesV2?accessFilter=2&limit=100&sortOrder=Asc ;https://develop.roblox.com/v1/universes/9294074907 | S | 2026-10-10 T2 |
| F006 | `updated` 字段(不可当更新日) | games v1:`2026-10-08T20:11:58.02Z`(T1 与 T4 两次同值);群组游戏列表与 develop 接口:`2026-08-19T08:54:43.003Z`。两个接口两个值 → 按 SKILL 2026-10-08 口径不当「最近更新日」;updates 页只把这两个值并列写出并说明不采用 | https://games.roblox.com/v1/games?universeIds=9294074907 ;https://games.roblox.com/v2/groups/1047647644/gamesV2?accessFilter=2&limit=100&sortOrder=Asc ;https://develop.roblox.com/v1/universes/9294074907 | S | 2026-10-10 T1/T2/T4 |
| F007 | 类型 | genre `All`;genre_l1 `Shooter`;genre_l2 `Deathmatch Shooter` | https://games.roblox.com/v1/games?universeIds=9294074907 | S | 2026-10-10 T1 |
| F008 | 单服人数上限 | 8(T2 公开服务器列表前 10 个服务器 maxPlayers 均为 8、playing 均为 8;验证员同日稍后读到 8 个 8/8、2 个 7/8 → 时点值不可复现,round1 U2 后页面已删去该句,只留 maxPlayers 8) | https://games.roblox.com/v1/games?universeIds=9294074907 `maxPlayers`;https://games.roblox.com/v1/games/90568084448279/servers/Public?limit=10 | S | 2026-10-10 T1/T2 |
| F009 | 价格 | 免费(`price: null`) | https://games.roblox.com/v1/games?universeIds=9294074907 | S | 2026-10-10 T1 |
| F010 | 私服 | games v1 `createVipServersAllowed: false`;游戏页 HTML `data-private-server-price="49"`、`data-can-create-server="False"`、`data-private-server-product-id="3494986672"`。按 SKILL 2026-10-02 口径不能据 createVipServersAllowed 判「未开放」;round1 U1 后 game-info 页把两个字段并列写出(49 Robux 的页面属性 与 createVipServersAllowed=false),结论是不判断能否购买 | https://games.roblox.com/v1/games?universeIds=9294074907 ;https://www.roblox.com/games/90568084448279/One-Tap | S | 2026-10-10 T1/T2 |
| F011 | 访问量 | T1:590,415,564;T4(约 4.5 分钟后):590,428,734。页面一律用 T1 值 | https://games.roblox.com/v1/games?universeIds=9294074907 `visits` | S | 2026-10-10 T1/T4 |
| F012 | 在线 | T1:25,975;T4:26,291 | https://games.roblox.com/v1/games?universeIds=9294074907 `playing` | S | 2026-10-10 T1/T4 |
| F013 | 收藏 | T1:658,502(favorites/count 接口同值 658,502);T4:658,517 | https://games.roblox.com/v1/games?universeIds=9294074907 ;https://games.roblox.com/v1/games/9294074907/favorites/count | S | 2026-10-10 T1/T4 |
| F014 | 点赞 / 点踩 | T1:221,667 / 30,357(合计 252,024;赞占比 87.95%,我们计算:221667÷252024);T4 复读:221,667 / 30,358。页面用 T1 值并写 ≈ 88% | https://games.roblox.com/v1/games/votes?universeIds=9294074907 | S | 2026-10-10 T1/T4 |
| F015 | 日均访问(推导) | 创建日 2025-12-04 到读数日 2026-10-10 共 310 天(27+31+28+31+30+31+30+31+31+30+10);590,415,564 ÷ 310 = 1,904,566 ≈ 1.9 million。只在 game-info 页出现,标明 our division | https://games.roblox.com/v1/games?universeIds=9294074907 | S(推导) | 2026-10-10 T1 |
| F016 | 内容分级 | `Maturity: Mild`;唯一描述项 displayName `Violence (Repeated/Mild)`;minimumAge 0 | https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation (POST `{"universeId":"9294074907"}`;GET 不可用,不放进页面 sourceUrls,页面改放游戏页 URL) | S | 2026-10-10 T1 |
| F017 | 游戏页媒体 | 5 条:1 条 GamePreviewVideo + 4 条 Image(imageId 129416589222458, 79590003078739, 96100438054444, 120330898196027;altText 全空) | https://games.roblox.com/v2/games/9294074907/media | S | 2026-10-10 T1 |
| F018 | 支持语言 | 18 种:English、Arabic、German、Spanish、French、Indonesian、Italian、Japanese、Korean、Polish、Portuguese、Russian、Thai、Turkish、Vietnamese、Chinese (Simplified)、Chinese (Traditional)、Hindi。接口不区分人工翻译与自动翻译 | https://gameinternationalization.roblox.com/v1/supported-languages/games/9294074907 | S | 2026-10-10 T1 |
| F019 | 头像类型 | `universeAvatarType: MorphToR6`(页面未写) | https://games.roblox.com/v1/games?universeIds=9294074907 | S | 2026-10-10 T1 |
| F020 | 游客可玩性 | `playabilityStatus: GuestProhibited`(匿名请求;只说明未登录不能玩,不说明设备支持;页面未写) | https://games.roblox.com/v1/games/multiget-playability-status?universeIds=9294074907 | S | 2026-10-10 T2 |
| F021 | 规范路径 | `/games/90568084448279/One-Tap`(游戏页 200,og:url 同) | https://www.roblox.com/games/90568084448279/One-Tap | S | 2026-10-10 T2 |

## 2. 官方描述(逐行原文;正文引用时去掉行首 emoji 与行首连字符,其余逐字)

来源:https://games.roblox.com/v1/games?universeIds=9294074907 `description`(S,T1 取;T4 复读、develop 接口、群组游戏列表、游戏页 HTML `<meta name="description">` 四处一致)。非空行共 18 行。

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F022 | 描述第 1 行(口号) | "Boom Headshot!" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F023 | 描述第 2 行(一句话定位:FFA、无队伍) | "One Tap is a fast-paced FPS sniper FFA arena, no teams, just pure chaos!" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F024 | 描述第 3 行(狙击:一枪) | "🎯 One-shot snipers" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F025 | 描述第 4 行(副武器:两枪,爆头一枪) | "🔫 Two-Shot Secondaries (One to the head)" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F026 | 描述第 5 行(近战武器) | "🔪 Melee Weapons" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F027 | 描述第 6 行(连杀 / 花式 / 干净击杀(只有名词,无规则)) | "🏆 Streaks, trick shots, clean kills and more!" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F028 | 描述第 7 行(小标题) | "🔓 Progress & Customization" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F029 | 描述第 8 行(皮肤数量下限 70+(页面不引括号里的 coming soon,见抬头说明)) | "-Unlock 70+ weapon skins (more coming soon)" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F030 | 描述第 9 行(箱子 → rare & limited cosmetics) | "-Roll cases to earn rare & limited cosmetics" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F031 | 描述第 10 行(三类可装备外观) | "-Equip kill effects, name tags, and skins" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F032 | 描述第 11 行(三个奖励来源) | "-Earn rewards from levels, daily, and quests" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F033 | 描述第 12 行(小标题) | "🎮 Platform Support" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F034 | 描述第 13 行(四类设备) | "PC 💻 \| Mobile 📱 \| Tablet \| Console 🎮" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F035 | 描述第 14 行(主机点名 Xbox 与 PlayStation) | "(Xbox & PlayStation supported)" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F036 | 描述第 15 行(求赞) | "👍 Enjoying the game?" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F037 | 描述第 16 行(求赞) | "Leave a thumbs-up, it helps a lot!" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F038 | 描述第 17 行(警示小标题) | "⚠️ NOTICE:" | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F039 | 描述第 18 行(封禁规则:三种行为、永久、不受理申诉) | "Cheating, exploiting, or farming with alts will result in a permanent ban. No appeals." | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F040 | 描述里有没有兑换码 | **没有**。全文 18 行(见上),无 code / CODE / redeem 字样 | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |
| F041 | 描述里有没有提战令 / 通行证 / Gems / Discord | **都没有**(全文无 battle pass / pass / gems / discord 字样) | https://games.roblox.com/v1/games?universeIds=9294074907 `description` | S | 2026-10-10 T1 |

## 3. 开发者群组

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F042 | 群组名 / id | `Stringless Banjo` / 1047647644;hasVerifiedBadge=false | https://groups.roblox.com/v1/groups/1047647644 | S | 2026-10-10 T2 |
| F043 | 群组 description | "Just me and my friend making fun roblox games lol" | https://groups.roblox.com/v1/groups/1047647644 | S | 2026-10-10 T2 |
| F044 | 群组 shout | `null`(无公告) | https://groups.roblox.com/v1/groups/1047647644 | S | 2026-10-10 T2 |
| F045 | 群组创建时间 | `2025-11-27T22:35:25.74Z` → 27 November 2025(比游戏记录早 7 天:11-27 → 12-04) | https://groups.roblox.com/v2/groups?groupIds=1047647644 | S | 2026-10-10 T2 |
| F046 | 群主 | username `BanjoMeni`,displayName `FpsHolder`,userId 9098936033,hasVerifiedBadge=true;账号创建 `2025-08-03T23:52:43.125Z` → 3 August 2025;个人简介 "Holder" | https://groups.roblox.com/v1/groups/1047647644 ;https://users.roblox.com/v1/users/9098936033 | S | 2026-10-10 T2 |
| F047 | 成员数 | T2:207,489;T4:207,494。页面用 T2 值 207,489 并写 as of 10 October 2026 | https://groups.roblox.com/v1/groups/1047647644 | S | 2026-10-10 T2/T4 |
| F048 | 角色 | Guest(rank 0,0 人);Member(rank 1,207,490 人);Cool People(rank 1,207,562 人);Developer(rank 250,1 人);Owner(rank 254,1 人);Holder(rank 255,1 人)。页面只写 Developer / Owner / Holder 三个角色各 1 个账号 | https://groups.roblox.com/v1/groups/1047647644/roles | S | 2026-10-10 T2 |
| F049 | 群组公开游戏 | 1 个:`[FPS] One Tap`(nextPageCursor=null) | https://games.roblox.com/v2/groups/1047647644/gamesV2?accessFilter=2&limit=100&sortOrder=Asc | S | 2026-10-10 T2 |
| F050 | 群组 wall | v2 wall/posts 返回 404(原因不明,不归因为需登录) | https://groups.roblox.com/v2/groups/1047647644/wall/posts?limit=10&sortOrder=Desc | S | 2026-10-10 T2 |
| F051 | 社交链接(游戏 / 群组) | 两个接口匿名请求均 401 `Authentication token is missing` → **未获取**;不写任何 Discord / X / YouTube | https://games.roblox.com/v1/games/9294074907/social-links/list ;https://groups.roblox.com/v1/groups/1047647644/social-links | S | 2026-10-10 T1/T2 |

## 4. 通行证(4 个,nextPageToken 空串 = 已取全)

来源:https://apis.roblox.com/game-passes/v1/universes/9294074907/game-passes?passView=Full&pageSize=100 (S,T1;不带 pageSize 参数的同一接口返回字节完全相同)。名称逐字复制 `name` 字段;4 个 `isForSale` 均为 true,`priceDiscountDetails` 均为空数组,`displayDescription` **均为空串**,creator 均为群组 1047647644。旧接口 `games.roblox.com/v1/games/9294074907/game-passes` 返回 404。
图标文字来源:https://thumbnails.roblox.com/v1/assets?assetIds=126028198454624,128625042989986,126925465702985,130506004802111&size=700x700&format=Png (S,T2;本人看 700x700 图逐字抄录,下载件在 `raw/img/pass-*.png`)。

| # | 名称(逐字) | 价格(Robux) | 图标上的字(逐字) | passId | 图标 assetId | created(UTC) | updated(UTC) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|---|---|
| F052 | `Double Voting Value` | 79 | "2x Votes" / "Your votes will count twice." | 1647434878 | 130506004802111 | 2025-12-29T02:48:21.667Z | 2026-08-10T06:16:53.031Z | game-passes 接口 + 图标接口 | S | 2026-10-10 T1 |
| F053 | `2x Level XP` | 149 | "2x XP" / "Grants double XP." | 1647856647 | 126925465702985 | 2025-12-29T02:50:42.932Z | 2026-08-10T06:20:40.206Z | game-passes 接口 + 图标接口 | S | 2026-10-10 T1 |
| F054 | `2x Money` | 299 | "2x Money" / "Grants double money from kills." | 1647410905 | 126028198454624 | 2025-12-29T02:49:48.648Z | 2026-08-10T06:16:40.024Z | game-passes 接口 + 图标接口 | S | 2026-10-10 T1 |
| F055 | `2x Case Luck` | 499 | "2x Case Luck" / "Grants more luck when" / 末行两端被圆形边框裁切:左侧 o 被裁掉,右侧 cases 的末个 s 被裁一半,其后是否有句号看不到(其余三张末行都以句号结尾);页面写作 opening cases 并注明裁切(round1 U12) | 1647434885 | 128625042989986 | 2025-12-29T02:50:22.866Z | 2026-08-10T06:16:53.031Z | game-passes 接口 + 图标接口 | S | 2026-10-10 T1 |

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F056 | 四个通行证合计 | 1,026 Robux(79+149+299+499,我们计算);2x Case Luck 占 48.6%(499÷1026);其余三个合计 527;最便宜两个合计 228 | https://apis.roblox.com/game-passes/v1/universes/9294074907/game-passes?passView=Full&pageSize=100 | S(推导) | 2026-10-10 T1 |
| F057 | 四个通行证的创建时刻 | 全部在 2025-12-29 02:48:21–02:50:42 UTC(2 分 21 秒内);全部在 2026-08-10 06:16:40–06:20:40 UTC 被编辑(接口不说明改了什么) | https://apis.roblox.com/game-passes/v1/universes/9294074907/game-passes?passView=Full&pageSize=100 | S | 2026-10-10 T1 |
| F058 | 2x Case Luck 与 80 Robux 箱子的比价(推导) | 6 × 80 = 480;499 − 480 = 19 | https://apis.roblox.com/game-passes/v1/universes/9294074907/game-passes?passView=Full&pageSize=100 ;https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S(推导) | 2026-10-10 T1 |

## 5. 开发者商品(97 个,nextPageCursor = null = 已取全)

来源:https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 (S,T1)。名称逐字复制 `Name` 字段(97 个名称互不相同;`displayName` / `DisplayName` 与 `Name` 全部一致);97 个 `IsForSale` 均为 true;`PriceDiscountDetails` 均为空数组;`UserBasePriceInRobux` 与 `PriceInRobux` 全部相同;**`Description` / `displayDescription` 全部为空串**;97 个共用同一个 `IconImageAssetId` 88963008124478(灰色立方体占位图,见 https://thumbnails.roblox.com/v1/assets?assetIds=88963008124478&size=700x700&format=Png )。
分组是本站编辑口径(按名称里的词归类,规则在 `tools/groups.py`),不是官方分类。「单价」= 价格 ÷ 名称里的数量,我们计算。

### 5.1 Numbered cases (Case 1 to Case 5)(15 个;价格 10–800;一样买一个合计 2,450;全表所在页:/one-tap/cases/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F059 | `Case 1 Buy 1` | 15 | 15÷1=15 | 72287250 | 2025-12-29T02:24:20.792Z | 2025-12-29T02:24:20.792Z | S | 2026-10-10 T1 |
| F060 | `Case 1 Buy 3` | 45 | 45÷3=15 | 72287255 | 2025-12-29T02:24:36.665Z | 2025-12-29T02:24:36.665Z | S | 2026-10-10 T1 |
| F061 | `Case 1 Buy 10` | 150 | 150÷10=15 | 72287254 | 2025-12-29T02:24:28.434Z | 2025-12-29T02:24:28.434Z | S | 2026-10-10 T1 |
| F062 | `Case 2 Buy 1` | 40 | 40÷1=40 | 72287259 | 2025-12-29T02:24:45.384Z | 2025-12-29T02:41:06.185Z | S | 2026-10-10 T1 |
| F063 | `Case 2 Buy 3` | 120 | 120÷3=40 | 72287266 | 2025-12-29T02:24:58.392Z | 2025-12-29T02:41:13.682Z | S | 2026-10-10 T1 |
| F064 | `Case 2 Buy 10` | 400 | 400÷10=40 | 72287264 | 2025-12-29T02:24:52.501Z | 2025-12-29T02:41:09.42Z | S | 2026-10-10 T1 |
| F065 | `Case 3 Buy 1` | 10 | 10÷1=10 | 72287267 | 2025-12-29T02:25:05.375Z | 2025-12-29T02:40:22.94Z | S | 2026-10-10 T1 |
| F066 | `Case 3 Buy 3` | 30 | 30÷3=10 | 72287269 | 2025-12-29T02:25:19.284Z | 2025-12-29T02:40:39.725Z | S | 2026-10-10 T1 |
| F067 | `Case 3 Buy 10` | 100 | 100÷10=10 | 72287268 | 2025-12-29T02:25:11.393Z | 2025-12-29T02:40:43.5Z | S | 2026-10-10 T1 |
| F068 | `Case 4 Buy 1` | 30 | 30÷1=30 | 72287290 | 2025-12-29T02:25:25.631Z | 2025-12-29T02:39:42.21Z | S | 2026-10-10 T1 |
| F069 | `Case 4 Buy 3` | 90 | 90÷3=30 | 72287293 | 2025-12-29T02:25:35.942Z | 2025-12-29T02:39:55.388Z | S | 2026-10-10 T1 |
| F070 | `Case 4 Buy 10` | 300 | 300÷10=30 | 72287292 | 2025-12-29T02:25:31.494Z | 2025-12-29T02:40:03.356Z | S | 2026-10-10 T1 |
| F071 | `Case 5 Buy 1` | 80 | 80÷1=80 | 72888811 | 2026-01-28T21:08:19.809Z | 2026-01-28T21:08:19.809Z | S | 2026-10-10 T1 |
| F072 | `Case 5 Buy 3` | 240 | 240÷3=80 | 72888820 | 2026-01-28T21:08:32.078Z | 2026-01-28T21:08:32.078Z | S | 2026-10-10 T1 |
| F073 | `Case 5 Buy 10` | 800 | 800÷10=80 | 72888827 | 2026-01-28T21:08:40.516Z | 2026-01-28T21:08:40.516Z | S | 2026-10-10 T1 |

### 5.2 Named cases(33 个;价格 15–1,050;一样买一个合计 12,898;全表所在页:/one-tap/cases/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F074 | `Battle Case 1` | 80 | 80÷1=80 | 76114798 | 2026-06-15T01:21:21.96Z | 2026-06-15T01:21:21.96Z | S | 2026-10-10 T1 |
| F075 | `Battle Case 3` | 240 | 240÷3=80 | 76114800 | 2026-06-15T01:21:29.726Z | 2026-06-15T01:21:29.726Z | S | 2026-10-10 T1 |
| F076 | `Battle Case 10` | 800 | 800÷10=80 | 76114805 | 2026-06-15T01:21:42.712Z | 2026-06-15T01:21:42.712Z | S | 2026-10-10 T1 |
| F077 | `1 Cosmic Case` | 80 | 80÷1=80 | 73783309 | 2026-03-12T18:18:24.244Z | 2026-03-13T02:17:05.959Z | S | 2026-10-10 T1 |
| F078 | `3 Cosmic Cases` | 240 | 240÷3=80 | 73783306 | 2026-03-12T18:18:24.233Z | 2026-03-13T02:17:17.256Z | S | 2026-10-10 T1 |
| F079 | `10 Cosmic Cases` | 800 | 800÷10=80 | 73783307 | 2026-03-12T18:18:24.248Z | 2026-03-13T02:17:21.794Z | S | 2026-10-10 T1 |
| F080 | `Cyber Case #2 1` | 80 | 80÷1=80 | 74616791 | 2026-04-24T03:00:35.151Z | 2026-04-24T03:00:35.151Z | S | 2026-10-10 T1 |
| F081 | `Cyber Case #2 3` | 240 | 240÷3=80 | 74616795 | 2026-04-24T03:00:45.453Z | 2026-04-24T03:00:45.453Z | S | 2026-10-10 T1 |
| F082 | `Cyber Case #2 10` | 800 | 800÷10=80 | 74616796 | 2026-04-24T03:00:54.541Z | 2026-04-24T03:00:54.541Z | S | 2026-10-10 T1 |
| F083 | `Dragon Case 1` | 80 | 80÷1=80 | 74616815 | 2026-04-24T03:03:46.283Z | 2026-04-24T03:03:46.283Z | S | 2026-10-10 T1 |
| F084 | `Dragon Case 3` | 240 | 240÷3=80 | 74616820 | 2026-04-24T03:04:01.874Z | 2026-04-24T03:04:01.874Z | S | 2026-10-10 T1 |
| F085 | `Dragon Case 10` | 800 | 800÷10=80 | 74616816 | 2026-04-24T03:03:52.303Z | 2026-04-24T03:03:52.303Z | S | 2026-10-10 T1 |
| F086 | `1 Energy Sword Case` | 199 | 199÷1=199 | 73783315 | 2026-03-12T18:18:24.663Z | 2026-09-30T22:21:34.109Z | S | 2026-10-10 T1 |
| F087 | `3 Energy Sword Cases` | 450 | 450÷3=150 | 73783313 | 2026-03-12T18:18:24.656Z | 2026-03-26T02:56:43.638Z | S | 2026-10-10 T1 |
| F088 | `6 Energy Sword Cases` | 900 | 900÷6=150 | 73783314 | 2026-03-12T18:18:24.661Z | 2026-03-26T02:56:56.843Z | S | 2026-10-10 T1 |
| F089 | `1 Glitched Case` | 15 | 15÷1=15 | 73783317 | 2026-03-12T18:18:24.7Z | 2026-03-12T18:18:24.7Z | S | 2026-10-10 T1 |
| F090 | `3 Glitched Cases` | 45 | 45÷3=15 | 73783312 | 2026-03-12T18:18:24.653Z | 2026-03-12T18:18:24.653Z | S | 2026-10-10 T1 |
| F091 | `10 Glitched Cases` | 150 | 150÷10=15 | 73783316 | 2026-03-12T18:18:24.671Z | 2026-03-12T18:18:24.671Z | S | 2026-10-10 T1 |
| F092 | `Guardian Case 1` | 80 | 80÷1=80 | 76114807 | 2026-06-15T01:21:52.195Z | 2026-06-15T01:21:52.195Z | S | 2026-10-10 T1 |
| F093 | `Guardian Case 3` | 240 | 240÷3=80 | 76114810 | 2026-06-15T01:22:02.381Z | 2026-06-15T01:22:02.381Z | S | 2026-10-10 T1 |
| F094 | `Guardian Case 10` | 800 | 800÷10=80 | 76114812 | 2026-06-15T01:22:11.367Z | 2026-06-15T01:22:11.367Z | S | 2026-10-10 T1 |
| F095 | `1 Karambit Case` | 149 | 149÷1=149 | 72888706 | 2026-01-28T21:03:14.828Z | 2026-09-30T23:27:32.512Z | S | 2026-10-10 T1 |
| F096 | `3 Karambit Case` | 450 | 450÷3=150 | 72888744 | 2026-01-28T21:05:31.339Z | 2026-03-26T02:56:47.078Z | S | 2026-10-10 T1 |
| F097 | `7 Karambit Cases` | 1,050 | 1050÷7=150 | 72888958 | 2026-01-28T21:16:46.808Z | 2026-03-26T02:57:03.197Z | S | 2026-10-10 T1 |
| F098 | `Moon Case 1` | 80 | 80÷1=80 | 77146922 | 2026-08-03T22:20:17.12Z | 2026-08-03T22:20:17.12Z | S | 2026-10-10 T1 |
| F099 | `Moon Case 3` | 240 | 240÷3=80 | 77146925 | 2026-08-03T22:20:27.029Z | 2026-08-03T22:20:27.029Z | S | 2026-10-10 T1 |
| F100 | `Moon Case 10` | 800 | 800÷10=80 | 77146928 | 2026-08-03T22:20:42.554Z | 2026-08-03T22:20:42.554Z | S | 2026-10-10 T1 |
| F101 | `1 Proto Case` | 150 | 150÷1=150 | 73783311 | 2026-03-12T18:18:24.575Z | 2026-03-26T02:57:29.038Z | S | 2026-10-10 T1 |
| F102 | `3 Proto Cases` | 450 | 450÷3=150 | 73783310 | 2026-03-12T18:18:24.246Z | 2026-03-26T02:56:52.427Z | S | 2026-10-10 T1 |
| F103 | `7 Proto Cases` | 1,050 | 1050÷7=150 | 73783304 | 2026-03-12T18:18:24.232Z | 2026-03-26T02:57:07.828Z | S | 2026-10-10 T1 |
| F104 | `Vintage Case 1` | 80 | 80÷1=80 | 76114789 | 2026-06-15T01:19:52.351Z | 2026-06-15T01:20:40.395Z | S | 2026-10-10 T1 |
| F105 | `Vintage Case 3` | 240 | 240÷3=80 | 76114793 | 2026-06-15T01:20:52.699Z | 2026-06-15T01:20:52.699Z | S | 2026-10-10 T1 |
| F106 | `Vintage Case 10` | 800 | 800÷10=80 | 76114796 | 2026-06-15T01:21:12.619Z | 2026-06-15T01:21:12.619Z | S | 2026-10-10 T1 |

### 5.3 Nightmare 1 / 3 / 5(3 个;价格 149–750;一样买一个合计 1,349;全表所在页:/one-tap/cases/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F107 | `Nightmare 1` | 149 | 149÷1=149 | 74492705 | 2026-04-17T02:59:55.425Z | 2026-09-30T23:27:52.56Z | S | 2026-10-10 T1 |
| F108 | `Nightmare 3` | 450 | 450÷3=150 | 74492709 | 2026-04-17T03:00:05.567Z | 2026-04-17T03:00:05.567Z | S | 2026-10-10 T1 |
| F109 | `Nightmare 5` | 750 | 750÷5=150 | 74492714 | 2026-04-17T03:00:25.984Z | 2026-04-17T03:00:25.984Z | S | 2026-10-10 T1 |

### 5.4 Product named Case(1 个;价格 5–5;一样买一个合计 5;全表所在页:/one-tap/cases/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F110 | `Case` | 5 |  | 72888976 | 2026-01-28T21:17:27.964Z | 2026-01-29T02:42:09.86Z | S | 2026-10-10 T1 |

### 5.5 Gems packs(5 个;价格 49–2,299;一样买一个合计 3,845;全表所在页:/one-tap/shop/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F111 | `Gems Small` | 49 |  | 72287305 | 2025-12-29T02:26:14.696Z | 2025-12-29T02:26:14.696Z | S | 2026-10-10 T1 |
| F112 | `Gems Medium` | 199 |  | 72287304 | 2025-12-29T02:26:09.136Z | 2025-12-29T02:26:09.136Z | S | 2026-10-10 T1 |
| F113 | `Gems Large` | 499 |  | 72287296 | 2025-12-29T02:25:52.536Z | 2025-12-29T02:25:52.536Z | S | 2026-10-10 T1 |
| F114 | `Gems Massive` | 799 |  | 72287300 | 2025-12-29T02:26:01.07Z | 2025-12-29T02:26:01.07Z | S | 2026-10-10 T1 |
| F115 | `Gems Best Value` | 2,299 |  | 72287295 | 2025-12-29T02:25:44.215Z | 2025-12-29T02:25:44.215Z | S | 2026-10-10 T1 |

### 5.6 Sun Points packs(5 个;价格 80–2,000;一样买一个合计 4,400;全表所在页:/one-tap/shop/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F116 | `Sun Points Small` | 80 |  | 76022285 | 2026-06-10T00:38:00.965Z | 2026-06-14T23:10:10.765Z | S | 2026-10-10 T1 |
| F117 | `Sun Points Medium` | 320 |  | 76022281 | 2026-06-10T00:37:38.708Z | 2026-06-14T23:10:02.345Z | S | 2026-10-10 T1 |
| F118 | `Sun Points Large` | 800 |  | 76022275 | 2026-06-10T00:37:05.021Z | 2026-06-14T23:10:17.359Z | S | 2026-10-10 T1 |
| F119 | `Sun Points Massive` | 1,200 |  | 76022272 | 2026-06-10T00:36:40.597Z | 2026-06-14T23:10:25.416Z | S | 2026-10-10 T1 |
| F120 | `Sun Points Best Value` | 2,000 |  | 76022269 | 2026-06-10T00:36:06.786Z | 2026-06-14T23:10:31.722Z | S | 2026-10-10 T1 |

### 5.7 Product named 500(1 个;价格 5–5;一样买一个合计 5;全表所在页:/one-tap/shop/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F121 | `500` | 5 |  | 72888933 | 2026-01-28T21:15:18.93Z | 2026-01-29T02:42:03.514Z | S | 2026-10-10 T1 |

### 5.8 Premium Battlepass and Skip products(7 个;价格 20–850;一样买一个合计 2,798;全表所在页:/one-tap/battle-pass/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F122 | `Skip One Tier` | 20 |  | 72287317 | 2025-12-29T02:26:54.159Z | 2025-12-29T02:26:54.159Z | S | 2026-10-10 T1 |
| F123 | `Skip Five Tiers` | 100 |  | 72287316 | 2025-12-29T02:26:48.437Z | 2025-12-29T02:26:48.437Z | S | 2026-10-10 T1 |
| F124 | `Skip Three Tiers` | 179 |  | 72287323 | 2025-12-29T02:27:09.901Z | 2025-12-29T02:27:09.901Z | S | 2026-10-10 T1 |
| F125 | `Premium Battlepass` | 449 |  | 72287310 | 2025-12-29T02:26:31.473Z | 2026-02-04T20:14:18.13Z | S | 2026-10-10 T1 |
| F126 | `Skip All` | 600 |  | 72888757 | 2026-01-28T21:06:07.515Z | 2026-01-28T21:06:07.515Z | S | 2026-10-10 T1 |
| F127 | `Skip All Tiers` | 600 |  | 72890143 | 2026-01-28T22:43:05.98Z | 2026-01-28T22:43:05.98Z | S | 2026-10-10 T1 |
| F128 | `Skip Ten Tiers` | 850 |  | 72287320 | 2025-12-29T02:27:02.945Z | 2025-12-29T02:27:02.945Z | S | 2026-10-10 T1 |

### 5.9 Xp Boost products(4 个;价格 30–360;一样买一个合计 570;全表所在页:/one-tap/rewards/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F129 | `Xp Boost 30 Minutes` | 30 |  | 72287332 | 2025-12-29T02:27:56.903Z | 2025-12-29T02:27:56.903Z | S | 2026-10-10 T1 |
| F130 | `Xp Boost 1 Hour` | 60 |  | 72287329 | 2025-12-29T02:27:39.182Z | 2025-12-29T02:27:39.182Z | S | 2026-10-10 T1 |
| F131 | `Xp Boost 2 Hours` | 120 |  | 72287330 | 2025-12-29T02:27:47.472Z | 2025-12-29T02:27:47.472Z | S | 2026-10-10 T1 |
| F132 | `Xp Boost 6 Hours` | 360 |  | 72287334 | 2025-12-29T02:28:04.357Z | 2025-12-29T02:28:04.357Z | S | 2026-10-10 T1 |

### 5.10 Refresh Quest(1 个;价格 39–39;一样买一个合计 39;全表所在页:/one-tap/rewards/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F133 | `Refresh Quest` | 39 |  | 72888860 | 2026-01-28T21:11:10.498Z | 2026-01-28T21:11:10.498Z | S | 2026-10-10 T1 |

### 5.11 Bundles and Starterpack(4 个;价格 79–449;一样买一个合计 1,176;全表所在页:/one-tap/shop/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F134 | `Starterpack` | 79 |  | 72287325 | 2025-12-29T02:27:24.872Z | 2026-01-29T15:03:24.052Z | S | 2026-10-10 T1 |
| F135 | `Starfire Bundle` | 299 |  | 72287324 | 2025-12-29T02:27:16.807Z | 2026-01-13T21:24:05.797Z | S | 2026-10-10 T1 |
| F136 | `Astral Bundle` | 349 |  | 72287247 | 2025-12-29T02:24:03.065Z | 2026-01-28T23:39:04.717Z | S | 2026-10-10 T1 |
| F137 | `Dragon Bundle` | 449 |  | 76108341 | 2026-06-14T16:43:56.369Z | 2026-09-30T22:20:50.938Z | S | 2026-10-10 T1 |

### 5.12 Limited-named products(14 个;价格 95–199;一样买一个合计 2,532;全表所在页:/one-tap/shop/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F138 | `[LIMITED] Solar Cannon 115` | 95 |  | 72904350 | 2026-01-29T17:55:49.09Z | 2026-01-29T17:55:49.09Z | S | 2026-10-10 T1 |
| F139 | `[LIMITED OFFER] Cosmic Vortex` | 149 |  | 72904371 | 2026-01-29T17:57:44.501Z | 2026-01-29T18:19:20.9Z | S | 2026-10-10 T1 |
| F140 | `[LIMITED OFFER] Solar Cannon` | 149 |  | 72904372 | 2026-01-29T17:57:44.505Z | 2026-01-29T18:19:20.848Z | S | 2026-10-10 T1 |
| F141 | `[LIMITED OFFER] Stardust` | 149 |  | 72904370 | 2026-01-29T17:57:44.517Z | 2026-01-29T18:19:20.869Z | S | 2026-10-10 T1 |
| F142 | `Limited 1` | 199 |  | 72889020 | 2026-01-28T21:19:59.14Z | 2026-01-29T20:33:05.408Z | S | 2026-10-10 T1 |
| F143 | `Limited 2` | 199 |  | 72889026 | 2026-01-28T21:20:17.212Z | 2026-01-29T18:44:40.506Z | S | 2026-10-10 T1 |
| F144 | `Limited 3` | 199 |  | 72889007 | 2026-01-28T21:19:44.139Z | 2026-01-29T20:33:10.353Z | S | 2026-10-10 T1 |
| F145 | `Limited 4` | 199 |  | 76341321 | 2026-06-27T20:35:53.95Z | 2026-06-27T20:35:53.95Z | S | 2026-10-10 T1 |
| F146 | `Limited Skin 1` | 199 |  | 73783308 | 2026-03-12T18:18:24.241Z | 2026-03-26T02:56:26.771Z | S | 2026-10-10 T1 |
| F147 | `Limited Skin 2` | 199 |  | 73783305 | 2026-03-12T18:18:24.233Z | 2026-03-26T02:56:30.034Z | S | 2026-10-10 T1 |
| F148 | `Limited Skin 3` | 199 |  | 73783303 | 2026-03-12T18:18:24.156Z | 2026-03-26T02:56:33.123Z | S | 2026-10-10 T1 |
| F149 | `Nightmare Fuel [LIMITED]` | 199 |  | 72287307 | 2025-12-29T02:26:21.761Z | 2026-01-27T01:53:16.053Z | S | 2026-10-10 T1 |
| F150 | `Prototype-1 [LIMITED]` | 199 |  | 72287313 | 2025-12-29T02:26:41.652Z | 2026-01-27T02:15:47.042Z | S | 2026-10-10 T1 |
| F151 | `The Covenant [LIMITED]` | 199 |  | 72287326 | 2025-12-29T02:27:31.705Z | 2026-01-27T02:15:57.697Z | S | 2026-10-10 T1 |

### 5.13 Donations(4 个;价格 10–10,000;一样买一个合计 11,110;全表所在页:/one-tap/shop/)

| # | 名称(逐字) | 价格(Robux) | 单价(推导) | DeveloperProductId | Created(UTC) | Updated(UTC) | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|
| F152 | `10 Robux Donation` | 10 |  | 73649325 | 2026-03-06T01:16:41.802Z | 2026-03-06T01:16:41.802Z | S | 2026-10-10 T1 |
| F153 | `100 Robux Donation` | 100 |  | 73649324 | 2026-03-06T01:16:41.801Z | 2026-03-06T01:16:41.801Z | S | 2026-10-10 T1 |
| F154 | `1000 Robux Donation` | 1,000 |  | 73649326 | 2026-03-06T01:16:41.811Z | 2026-03-06T01:16:41.811Z | S | 2026-10-10 T1 |
| F155 | `10000 Robux Donation` | 10,000 |  | 73649323 | 2026-03-06T01:16:41.761Z | 2026-03-06T01:16:41.761Z | S | 2026-10-10 T1 |

### 5.14 商品层面的推导与计数(全部是我们的算术,来源同上)

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F156 | 商品总数 / 价格范围 / 一样买一个合计 | 97 / 5–10,000 Robux / 43,177 Robux(13 组小计相加:2,450 + 12,898 + 1,349 + 5 + 3,845 + 4,400 + 5 + 2,798 + 570 + 39 + 1,176 + 2,532 + 11,110) | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S(推导) | 2026-10-10 T1 |
| F157 | 名称含 Case 的商品 | 49 个 = 编号箱 15 + 具名箱 33 + 单独一个 `Case`;48 个分属 16 个系列(Case 1–5 共 5 个 + 具名 11 个:Karambit、Proto、Energy Sword、Cosmic、Glitched、Cyber Case #2、Dragon Case、Vintage Case、Battle Case、Guardian Case、Moon Case) | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S(推导) | 2026-10-10 T1 |
| F158 | 单个箱子的价格范围(16 个系列) | 10(Case 3 Buy 1)到 199(1 Energy Sword Case);单价 80 的系列 8 个:Case 5、Cosmic、Cyber Case #2、Dragon Case、Vintage Case、Battle Case、Guardian Case、Moon Case | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S(推导) | 2026-10-10 T1 |
| F159 | 多买是否更便宜 | 16 个系列里 14 个各档单价完全相同;Energy Sword:1 个 199,3 个 450(150/个;比 3×199=597 便宜 147),6 个 900(150/个;比 6×199=1,194 便宜 294);Karambit:1 个 149,3 个 450(150/个;比 3×149=447 贵 3),7 个 1,050(150/个;比 7×149=1,043 贵 7);Proto 各档都是 150 | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S(推导) | 2026-10-10 T1 |
| F160 | Nightmare 1 / 3 / 5 | 149 / 450 / 750(149、150、150 每单位);名称不含 Case,另有商品 `Nightmare Fuel [LIMITED]`;页面不说它是什么 | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S(推导) | 2026-10-10 T1 |
| F161 | `500` 与 `Case` 两条记录 | 各 5 Robux;`500` 创建于 2026-01-28T21:15:18Z,`Case` 创建于 2026-01-28T21:17:27Z(相差 2 分 9 秒);两条都在 2026-01-29T02:42:03Z / 02:42:09Z 被编辑;用途未确认 | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S | 2026-10-10 T1 |
| F162 | 名称为 Premium Battlepass / Skip* 的 7 条(7 条 Description 全空;「跳几层」「属于同一个战令」都只是由名称读出,round1 U3–U7 后页面一律加限定) | Premium Battlepass 449;Skip One Tier 20(20/层);Skip Three Tiers 179(59.67/层);Skip Five Tiers 100(20/层);Skip Ten Tiers 850(85/层);Skip All 600;Skip All Tiers 600。3 层单买 60 对 179;10 层按两份 Skip Five Tiers 200 对 850;600÷20=30;850−600=250;449+600=1,049。页面的每层单价按一位小数写:20.0 / 59.7 / 20.0 / 85.0。四条编号 Skip 的 Created 与 Updated 完全相同(从未编辑);Premium Battlepass 于 2026-02-04 被编辑;Skip All 创建 2026-01-28T21:06:07Z、Skip All Tiers 创建 2026-01-28T22:43:05Z(相差 97 分钟) | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S(推导) | 2026-10-10 T1 |
| F163 | Xp Boost 4 条 | 30 分钟 30、1 小时 60、2 小时 120、6 小时 360 → 每分钟 1 Robux,各档相同(页面写 1.0);2 小时 + 30 分钟 = 150 Robux,对比 2x Level XP 通行证 149;12 × 30 = 360 | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 ;https://apis.roblox.com/game-passes/v1/universes/9294074907/game-passes?passView=Full&pageSize=100 | S(推导) | 2026-10-10 T1 |
| F164 | Gems 5 条 | Small 49、Medium 199(÷49≈4.06)、Large 499(≈10.18)、Massive 799(≈16.31)、Best Value 2,299(≈46.92);页面按一位小数写 1.0 / 4.1 / 10.2 / 16.3 / 46.9;5 条 Created 与 Updated 完全相同;每包数量接口里没有 | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S(推导) | 2026-10-10 T1 |
| F165 | Sun Points 5 条 | Small 80、Medium 320(4 倍)、Large 800(10 倍)、Massive 1,200(15 倍)、Best Value 2,000(25 倍);2026-06-10 00:36–00:38 UTC 创建,2026-06-14 23:10 UTC 全部被编辑;☀️Summer Update! 活动 listed start 2026-06-15 14:00 UTC,活动文本没有 Sun Points 字样 | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 ;https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S(推导) | 2026-10-10 T1 |
| F166 | 名称含 LIMITED / Limited 的 14 条 | 199 Robux 的 10 条、149 的 3 条、95 的 1 条;占位式名称 7 条(Limited 1–4、Limited Skin 1–3);`[LIMITED] Solar Cannon 115`(95,2026-01-29T17:55:49Z)与 `[LIMITED OFFER] Solar Cannon`(149,2026-01-29T17:57:44Z)相差 1 分 55 秒 | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S(推导) | 2026-10-10 T1 |
| F167 | Donation 4 条 | 10 / 100 / 1000 / 10000 Robux Donation,价格等于名称里的数;4 条 Created 都是 2026-03-06T01:16:41Z(同一秒) | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S | 2026-10-10 T1 |
| F168 | 最常见价格 / 编辑情况 | 199 Robux 出现 12 次(Gems Medium、1 Energy Sword Case、10 条 Limited 名称);Created 与 Updated 完全相同的 50 条,其余 47 条至少编辑过一次;2026-09-30 被编辑的 4 条:`1 Karambit Case`、`1 Energy Sword Case`、`Nightmare 1`、`Dragon Bundle` | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S(推导) | 2026-10-10 T1 |

### 5.15 商品记录按创建日计数(我们计数)

| # | Created(UTC 日期) | 条数 | 时刻范围 | 名称 | 来源 | 等级 |
|---|---|---|---|---|---|---|
| F169 | 2025-12-29 | 32 | 02:24:03–02:28:04 | `Astral Bundle`、`Case 1 Buy 1`、`Case 1 Buy 10`、`Case 1 Buy 3`、`Case 2 Buy 1`、`Case 2 Buy 10`、`Case 2 Buy 3`、`Case 3 Buy 1`、`Case 3 Buy 10`、`Case 3 Buy 3`、`Case 4 Buy 1`、`Case 4 Buy 10`、`Case 4 Buy 3`、`Gems Best Value`、`Gems Large`、`Gems Massive`、`Gems Medium`、`Gems Small`、`Nightmare Fuel [LIMITED]`、`Premium Battlepass`、`Prototype-1 [LIMITED]`、`Skip Five Tiers`、`Skip One Tier`、`Skip Ten Tiers`、`Skip Three Tiers`、`Starfire Bundle`、`Starterpack`、`The Covenant [LIMITED]`、`Xp Boost 1 Hour`、`Xp Boost 2 Hours`、`Xp Boost 30 Minutes`、`Xp Boost 6 Hours` | developer-products 接口 | S(计数) |
| F170 | 2026-01-28 | 14 | 21:03:14–22:43:05 | `1 Karambit Case`、`3 Karambit Case`、`Skip All`、`Case 5 Buy 1`、`Case 5 Buy 3`、`Case 5 Buy 10`、`Refresh Quest`、`500`、`7 Karambit Cases`、`Case`、`Limited 3`、`Limited 1`、`Limited 2`、`Skip All Tiers` | developer-products 接口 | S(计数) |
| F171 | 2026-01-29 | 4 | 17:55:49–17:57:44 | `[LIMITED] Solar Cannon 115`、`[LIMITED OFFER] Cosmic Vortex`、`[LIMITED OFFER] Solar Cannon`、`[LIMITED OFFER] Stardust` | developer-products 接口 | S(计数) |
| F172 | 2026-03-06 | 4 | 01:16:41–01:16:41 | `10000 Robux Donation`、`100 Robux Donation`、`10 Robux Donation`、`1000 Robux Donation` | developer-products 接口 | S(计数) |
| F173 | 2026-03-12 | 15 | 18:18:24–18:18:24 | `Limited Skin 3`、`7 Proto Cases`、`Limited Skin 2`、`3 Cosmic Cases`、`Limited Skin 1`、`1 Cosmic Case`、`3 Proto Cases`、`10 Cosmic Cases`、`1 Proto Case`、`3 Glitched Cases`、`3 Energy Sword Cases`、`6 Energy Sword Cases`、`1 Energy Sword Case`、`10 Glitched Cases`、`1 Glitched Case` | developer-products 接口 | S(计数) |
| F174 | 2026-04-17 | 3 | 02:59:55–03:00:25 | `Nightmare 1`、`Nightmare 3`、`Nightmare 5` | developer-products 接口 | S(计数) |
| F175 | 2026-04-24 | 6 | 03:00:35–03:04:01 | `Cyber Case #2 1`、`Cyber Case #2 3`、`Cyber Case #2 10`、`Dragon Case 1`、`Dragon Case 10`、`Dragon Case 3` | developer-products 接口 | S(计数) |
| F176 | 2026-06-10 | 5 | 00:36:06–00:38:00 | `Sun Points Best Value`、`Sun Points Massive`、`Sun Points Large`、`Sun Points Medium`、`Sun Points Small` | developer-products 接口 | S(计数) |
| F177 | 2026-06-14 | 1 | 16:43:56–16:43:56 | `Dragon Bundle` | developer-products 接口 | S(计数) |
| F178 | 2026-06-15 | 9 | 01:19:52–01:22:11 | `Vintage Case 1`、`Vintage Case 3`、`Vintage Case 10`、`Battle Case 1`、`Battle Case 3`、`Battle Case 10`、`Guardian Case 1`、`Guardian Case 3`、`Guardian Case 10` | developer-products 接口 | S(计数) |
| F179 | 2026-06-27 | 1 | 20:35:53–20:35:53 | `Limited 4` | developer-products 接口 | S(计数) |
| F180 | 2026-08-03 | 3 | 22:20:17–22:20:42 | `Moon Case 1`、`Moon Case 3`、`Moon Case 10` | developer-products 接口 | S(计数) |

## 6. 官方活动(virtual-events,6 条)

来源:https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA (S,T1;带零起点游标,返回 6 条,nextPageCursor 空串)。**不带游标的 https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events 返回 0 条**(T1),`?eventStatus=completed` 也返回 0 条(T2);沿 previousPageCursor 翻两次分别返回后 5 条 / 后 4 条,没有出现第 7 条。交叉路径:https://apis.roblox.com/virtual-events/v1/virtual-events/groups/1047647644 (S,T2)同样返回这 6 条(倒序)。6 条的 `eventStatus` 全部是 `active`(含已结束的,按 SKILL 口径不据此判进行中);host 全部是群组 Stringless Banjo;`eventCategories` 全部是 newContent。

| # | title(逐字) | subtitle | listed start(UTC) | listed end(UTC) | listing created | listing updated | 配图 mediaId | 等级 | 取数时间 |
|---|---|---|---|---|---|---|---|---|---|
| F181 | `Valentines` | `Valentines` | 2026-02-14T21:14:44+00:00 | 2026-02-15T17:00:44+00:00 | 2026-01-26T19:50:09.294+00:00 | 2026-02-14T21:11:57.002+00:00 | 88388513445715 | S | 2026-10-10 T1 |
| F182 | `Update 2` | `One Tap Second Update` | 2026-03-13T12:10:49+00:00 | 2026-03-21T16:00:49+00:00 | 2026-01-31T01:36:13.505+00:00 | 2026-03-16T02:30:47.287+00:00 | 127182754594072 | S | 2026-10-10 T1 |
| F183 | `Update` | `More Stuff lol!` | 2026-04-24T16:00:55.6+00:00 | 2026-05-08T17:00:55.6+00:00 | 2026-04-05T04:04:14.511+00:00 | 2026-04-24T10:05:27.944+00:00 | 134947861539288 | S | 2026-10-10 T1 |
| F184 | `☀️Summer Update!` | `Summer Update` | 2026-06-15T14:00:55.6+00:00 | 2026-06-30T05:00:55.6+00:00 | 2026-04-05T04:16:17.805+00:00 | 2026-06-15T19:19:56.191+00:00 | 111201366562498 | S | 2026-10-10 T1 |
| F185 | `Revert` | `Revert` | 2026-08-09T13:20:15.423+00:00 | 2026-08-09T15:15:15.423+00:00 | 2026-08-09T13:18:17.679+00:00 | 2026-08-09T13:18:17.802+00:00 | 106005103409162 | S | 2026-10-10 T1 |
| F186 | `Game Revert` | `Revert` | 2026-08-15T05:20:28.851+00:00 | 2026-08-15T07:15:28.851+00:00 | 2026-08-15T05:18:17.334+00:00 | 2026-08-15T05:18:17.449+00:00 | 82429300588092 | S | 2026-10-10 T1 |

活动 description 原文(逐字,换行以 ` / ` 表示,空行省略):

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F187 | `Valentines` 的 description | "Valentines / We put out some of the valentines content for today! Obtain a free kill effect by joining." | https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-10 T1 |
| F188 | `Update 2` 的 description | "Update 2 / Content: / 3 New Maps (Removed temporarily in new servers to fix some issues) / New Battlepass season / New Cosmic and Glitched weapon cases / New Robux Energy Sword and Proto Cases / New Karambit Case Additions / New Level Reward Sniper and Knife / New Limited Weapons / Leaderboard Tag and Kill Effect reward for top 100 (Given after reset) / Reporting players / Improved anti-cheat / Crosshair size customization / New Leaderboards (Delayed, fixing it don't worry!)" | https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-10 T1 |
| F189 | `Update` 的 description | "Final List: / 28 total new weapons! These weapon models are also much higher quality than previous updates. / 2 New Weapon cases / New BP Season / 4 New Level Reward Skins / Leaderboard prize additions / New Limited Weapons / Small update, saving the big stuff for the summer update!!" | https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-10 T1 |
| F190 | `☀️Summer Update!` 的 description | "Join One Tap now to take part in the Summer Event alongside other new content!" | https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-10 T1 |
| F191 | `Revert` 的 description | "Game has been reverted to a previous version for testing." | https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-10 T1 |
| F192 | `Game Revert` 的 description | "One Tap has been experiencing some backend issues after publishing the lunar update for the game. We have not been able to pin point the exact issue yet but we have decided to revert to a previous version. The new Kill effects and tags are no longer in the game for now but weapons have been re added." | https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-10 T1 |
| F193 | Update 2 的内容行数 | `Content:` 之后 12 行(3 New Maps … / New Battlepass season / New Cosmic and Glitched weapon cases / New Robux Energy Sword and Proto Cases / New Karambit Case Additions / New Level Reward Sniper and Knife / New Limited Weapons / Leaderboard Tag and Kill Effect reward for top 100 (Given after reset) / Reporting players / Improved anti-cheat / Crosshair size customization / New Leaderboards (Delayed, fixing it don't worry!)) | https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S(计数) | 2026-10-10 T1 |
| F194 | Update(4 月)的内容行数 | `Final List:` 之后 6 行 + 结尾一句 `Small update, saving the big stuff for the summer update!!` | https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S(计数) | 2026-10-10 T1 |
| F195 | listing 记录比 listed start 早多少(推导) | Valentines:2026-01-26 → 02-14 = 19 天;Update 2:01-31 → 03-13 = 41 天;Update:04-05 → 04-24 = 19 天;☀️Summer Update!:04-05 → 06-15 = 71 天(≈10 周);Revert / Game Revert:各早 2 分钟。四条早于两周 | https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S(推导) | 2026-10-10 T1 |
| F196 | 两次赛季公告的间隔(推导) | `New Battlepass season`(Update 2,listed start 2026-03-13)到 `New BP Season`(Update,listed start 2026-04-24)= 42 天(3 月剩 18 天 + 4 月 24 天)。只是两条公告的间隔,开发者没有公布赛季时长;BP = Battlepass 是本站读法,4 月 listing 没有写全称(round1 U5) | https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S(推导) | 2026-10-10 T1 |
| F197 | 商品创建日与 listing 的相对位置(推导) | 2026-03-06(4 条 Donation)比 Update 2 早 7 天;03-12(15 条)比 Update 2 早 1 天;04-17(3 条 Nightmare)比 Update 早 7 天;04-24(6 条)与 Update 同日(03:00–03:04 UTC,早于 16:00 的 listed start);06-10(5 条 Sun Points)比 Summer 早 5 天;反例:Karambit 3 条创建于 01-28,比 Update 2(03-13)里的 New Karambit Case Additions 早 44 天 → 创建日与 listing 相近只是日期与名称吻合,不说明随该更新上架(round1 U14);06-14 / 06-15(1 + 9 条)在 Summer listed start 当天或前一天;06-27(Limited 4)在 Summer 窗口内(06-15–06-30);08-03(3 条 Moon Case)比 Revert 早 6 天;Valentines(02-14)前后两周内没有新建商品记录(最近的是 01-29 与 03-06) | https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 ;https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S(推导) | 2026-10-10 T1 |
| F198 | `lunar update` 的出处 | 只出现在 Game Revert 的 description 里("after publishing the lunar update for the game");没有任何 listing 以 lunar 命名;`Moon Case` 三条记录创建于 2026-08-03;两者之间没有官方文字相连,页面只并列写出 | https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA ;https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 | S | 2026-10-10 T1 |

## 7. 徽章 / 兑换码 / 官方 Discord

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F199 | 徽章 | 0 个。`{"previousPageCursor":null,"nextPageCursor":null,"data":[]}`,T1 读 2 次(带与不带 sortOrder)、T4 再读 1 次,三次均为空 | https://badges.roblox.com/v1/universes/9294074907/badges?limit=100 | S | 2026-10-10 T1/T4 |
| F200 | 兑换码 | **官方来源 0 个码**:游戏 description 18 行无码;群组 description 一句话无码;群组 shout 为 null;6 条活动 description 无码;社交链接未获取(401)。→ **不建 codes 页**。两个抢注站列的内容一律不采信(它们自己也写当前无码,但不作为出处) | https://games.roblox.com/v1/games?universeIds=9294074907 ;https://groups.roblox.com/v1/groups/1047647644 ;https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-10 T1/T2 |
| F201 | 官方 Discord | **未获取 / 不写**:Roblox 站内可读位置(description、群组 description、shout、6 条活动文本)都没有邀请链接;social-links 两个接口 401。任何 vanity 邀请码都没有官方一手页面可证,页面不出现任何 discord 链接 | https://games.roblox.com/v1/games?universeIds=9294074907 ;https://groups.roblox.com/v1/groups/1047647644 ;https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA | S | 2026-10-10 T1/T2 |

## 8. 官方图片(图内文字与画面为本人看图所见)

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F202 | 宣传图 th1(imageId 129416589222458) | 768x432;主视觉:黄色方头角色(蓝衣)咧嘴笑,端着绿黑方块狙击枪;远处屋顶一个红发角色举绿色步枪,橙色弹道弧线;图内无文字 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=9294074907&countPerUniverse=10&size=768x432&format=Png → https://tr.rbxcdn.com/180DAY-a3b7486513c2f5f78c14a24efd5d6c35/768/432/Image/Png/noFilter | S | 2026-10-10 T1 |
| F203 | 宣传图 th2(imageId 79590003078739) | 768x432;第一人称:两条浅黄色方块手臂握一把亮绿色像素狙击枪(黑色瞄准镜),灰色格子房间;图内无文字 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=9294074907&countPerUniverse=10&size=768x432&format=Png → https://tr.rbxcdn.com/180DAY-dada95a4e96832b2b0b416fc35b65933/768/432/Image/Png/noFilter | S | 2026-10-10 T1 |
| F204 | 宣传图 th3(imageId 96100438054444) | 768x432;第一人称:黑色带红色发光纹路的狙击枪,有黑烟,灰色格子房间;图内无文字 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=9294074907&countPerUniverse=10&size=768x432&format=Png → https://tr.rbxcdn.com/180DAY-fa67bff3555d0cd5ebc0d6e9264c4458/768/432/Image/Png/noFilter | S | 2026-10-10 T1 |
| F205 | 宣传图 th4(imageId 120330898196027) | 768x432;第一人称:深灰色步枪,枪管橙色发光并带火花,灰色格子房间;图内无文字 | https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=9294074907&countPerUniverse=10&size=768x432&format=Png → https://tr.rbxcdn.com/180DAY-7f35906266a1cbf531a95b97f5300ad8/768/432/Image/Png/noFilter | S | 2026-10-10 T1 |
| F206 | 游戏图标 icon | 512x512;与 th1 同一主视觉的方形构图(黄色方头角色在左、红发角色在右上);图内无文字 | https://thumbnails.roblox.com/v1/games/icons?universeIds=9294074907&size=512x512&format=Png → https://tr.rbxcdn.com/180DAY-00155b28dc7219013f3365f5def385ef/512/512/Image/Png/noFilter | S | 2026-10-10 T1 |
| F207 | 活动配图 Valentines(mediaId 88388513445715) | 768x432;主视觉的情人节版:角色戴粉色心形眼镜,画面飘粉色爱心 | https://thumbnails.roblox.com/v1/assets?assetIds=88388513445715,127182754594072,134947861539288,111201366562498,106005103409162,82429300588092&size=768x432&format=Png → https://tr.rbxcdn.com/180DAY-2b2834d02df92a311cf08f08c17b4e55/768/432/Image/Png/noFilter | S | 2026-10-10 T2 |
| F208 | 活动配图 Update(mediaId 134947861539288) | 768x432;第一人称:狙击枪被画成纯黑剪影,中间一个白色问号 | https://thumbnails.roblox.com/v1/assets?assetIds=88388513445715,127182754594072,134947861539288,111201366562498,106005103409162,82429300588092&size=768x432&format=Png → https://tr.rbxcdn.com/180DAY-1349f509741f169fc26d468e42d6ebb2/768/432/Image/Png/noFilter | S | 2026-10-10 T2 |
| F209 | 活动配图 ☀️Summer Update!(mediaId 111201366562498) | 实际解码 767x432;主视觉的夏日版:背景换成海滩、棕榈树与太阳 | https://thumbnails.roblox.com/v1/assets?assetIds=88388513445715,127182754594072,134947861539288,111201366562498,106005103409162,82429300588092&size=768x432&format=Png → https://tr.rbxcdn.com/180DAY-8949cd9ea458dbfb8a81638997764584/768/432/Image/Png/noFilter | S | 2026-10-10 T2 |
| F210 | 未入池的活动配图 | Update 2(mediaId 127182754594072)与 Revert / Game Revert(mediaId 106005103409162 / 82429300588092,两者同一个 CDN 哈希)画面与 th1 是同一张主视觉,只差裁切 → 不入池,避免不同 key 同一画面 | https://thumbnails.roblox.com/v1/assets?assetIds=88388513445715,127182754594072,134947861539288,111201366562498,106005103409162,82429300588092&size=768x432&format=Png | S | 2026-10-10 T2 |
| F211 | 通行证图标 4 张 | 700x700;深灰色圆盘 + 像素字;文字见第 4 节 | https://thumbnails.roblox.com/v1/assets?assetIds=126028198454624,128625042989986,126925465702985,130506004802111&size=700x700&format=Png | S | 2026-10-10 T2 |
| F212 | 开发者商品图标 | 97 个商品共用 assetId 88963008124478:白底上一块灰色立方体(Roblox 默认占位图样式)→ **不入池、不作封面** | https://thumbnails.roblox.com/v1/assets?assetIds=88963008124478&size=700x700&format=Png | S | 2026-10-10 T2 |

## 9. Roblox 官方文档原文(平台通用机制只引原文,T3 取,raw/docs/*.md)

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F213 | 通行证定义 | "Passes let you charge users a one-time Robux fee to access special privileges inside your game, such as entry to a restricted area, an in-game avatar item, or a permanent power-up."(文档 last_updated 2026-10-08) | https://create.roblox.com/docs/production/monetization/passes | S | 2026-10-10 T3 |
| F214 | 开发者商品定义 | "A developer product is an item or ability that a user can purchase more than once, such as in-game currency, ammo, or potions." | https://create.roblox.com/docs/production/monetization/developer-products | S | 2026-10-10 T3 |
| F215 | 社交链接可见性 | "Social media links are only visible to users who have verified their age as at least 16 years old. Users who are under 16 years old or who have not verified their age cannot view social media links.";另:"you can add up to three links to social media sites on your game details pages" | https://create.roblox.com/docs/production/promotion/social-media-links | S | 2026-10-10 T3 |
| F216 | 私服定义 | "A private server is a subscription-based feature that allows a player to decide who can play a game with them. While private servers can be free, you can also use private servers as a method of monetization by charging players who want to access private servers a monthly Robux fee." | https://create.roblox.com/docs/production/monetization/private-servers | S | 2026-10-10 T3 |

## 10. B / C 级线索(只记存在,不采信数据)

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 等级 | 取数时间 |
|---|---|---|---|---|---|
| F217 | onetap.wiki(抢注站) | 首页 200;sitemap 24 条,lastmod 全部 2026-07-24;栏目:codes / tier-list / trello / squad-planner / resource-calculator / guides(4)/ wiki(5)/ updates / sources + 信任页。只用于 benchmark.md 的架构对比 | https://onetap.wiki/ ;https://onetap.wiki/sitemap.xml | C | 2026-10-10 T3 |
| F218 | onetaproblox.wiki(抢注站) | 首页 200;sitemap 16 条,lastmod 2026-09-30 ×11、2026-10-07 ×5;栏目:guides(8)/ codes / community / faq + 信任页。其 updates 页用活动的 **end** 时间当更新日(March 21 / May 8 / June 30),与官方 listed start 不符 → 反例,我们按 listed start 写 | https://onetaproblox.wiki/ ;https://onetaproblox.wiki/sitemap.xml ;https://onetaproblox.wiki/guides/updates/ | C | 2026-10-10 T3 |
| F219 | Fandom | one-tap / onetap / one-tap-roblox / onetaproblox / fps-one-tap / stringless-banjo 六个子域 api.php 全部 404 → 没有可用的社区 wiki | https://one-tap.fandom.com/api.php?action=query&meta=siteinfo&siprop=general|statistics&format=json(其余同构) | B(不存在) | 2026-10-10 T4 |
| F220 | Google 下拉(需求证据) | `one tap roblox` 返回:one tap roblox game / codes / bots / wiki / discord;`one tap roblox how to` 返回:how to scope in one tap roblox、how to aim in one tap roblox;`one tap roblox g` 含 best gun in one tap roblox;含 script 的词一律不做。case / skins / battle pass / gems / karambit / update 六组返回空 | https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=…(raw/suggest.jsonl) | C(需求证据) | 2026-10-10 T4 |

## 11. 互相矛盾 / 未核实(页面一律写 not stated by the developer / not confirmed,或不写)

| # | 项 | 现状 | 页面处理 |
|---|---|---|---|
| U01 | games API `updated` 两个值(2026-10-08 与 2026-08-19) | 两个官方接口不一致 | updates 页并列写出、不采用为更新日 |
| U02 | 私服是否开放与价格 | 页面数据 49 Robux vs createVipServersAllowed=false;未登录无法验证 | game-info 页写「页面数据带 49 Robux,未确认能买」 |
| U03 | 武器数值(伤害、血量、射速、换弹)、哪些武器算 secondary | 0 来源 | how-to-play「What does the developer not state?」 |
| U04 | 操作方式(开镜 / 瞄准)、各平台键位 | 0 来源(下拉有 how to scope / how to aim 需求) | how-to-play、game-info 明写没有官方说明 |
| U05 | 大厅是否有 bot | 0 来源(下拉有 bots 需求) | how-to-play 列为未说明 |
| U06 | 地图名与数量;Update 2 撤下的 3 张新图是否恢复 | 只有 Update 2 一行 | how-to-play 引原文并写后续 listing 未提 |
| U07 | 投票投的是什么(Double Voting Value) | 图标只说 votes count twice | gamepasses 写 not stated;不写成地图投票 |
| U08 | Money 能买什么;Money 与 Gems 的关系;哪种货币开箱 | 0 来源 | gamepasses / shop 写 not stated |
| U09 | 箱子内容、概率、是否可不花 Robux 获得 | 0 来源 | cases「What is not stated」 |
| U10 | Case 1–5 各对应游戏内哪个箱子 | 0 来源 | cases 写按游戏内按钮价格对表 |
| U11 | 2x Case Luck 的 luck 具体改变什么 | 名称 2x、图标 more luck,无数值 | gamepasses / cases 写不可计算 |
| U12 | 战令层数、赛季时长、免费 / 付费奖励、Premium 是否跨赛季、Skip All 与 Skip All Tiers 的区别 | 0 来源 | battle-pass「What is not stated」 |
| U13 | Xp Boost 倍率、是否与 2x Level XP 叠加、下线是否计时 | 0 来源 | rewards 写 not stated |
| U14 | Refresh Quest 刷新一个还是全部任务 | 只有名称与价格 | rewards 写 not stated |
| U15 | 等级奖励表、每日奖励内容、任务清单、排行榜统计口径与重置周期 | 只有活动里的零散行 | rewards 末节列表 |
| U16 | Gems / Sun Points 每包数量与用途;Sun Points 与夏日活动的关系 | 名称与日期吻合,活动文本未提 | shop 写 our reading of the name and the dates |
| U17 | Bundle / Starterpack / Limited 各条内容;Limited 1–4、Limited Skin 1–3 当前对应哪件物品;`115` 的含义;`500` 的含义 | 只有名称与价格 | shop 写 not confirmed |
| U18 | 97 条 IsForSale=true 的商品是否都在游戏内商店出售 | 接口标记不等于游戏内在售 | cases / battle-pass / shop / robux 都有一句声明 |
| U19 | lunar update 的内容;被撤下的 Kill effects 与 tags 是否已恢复 | Game Revert 之后没有新 listing | updates 写 none since says |
| U20 | Valentines 的 free kill effect 是否仍可获得;top 100 奖励是否会再发 | 活动窗口已结束,无后续说明 | rewards 写 No listing says |
| U21 | 官方 Discord / X / YouTube | social links 401 | game-info「Is there an official One Tap Discord?」写 could not confirm |
| U22 | 各设备实测可玩性 | 只有描述里的 Platform Support 四行 | game-info 写 not tested |

