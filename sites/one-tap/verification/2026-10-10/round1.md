# One Tap 英文栏目 对抗验证 round1（2026-10-10，全部证据为今天重新从线上取得）

总结：12 页约 620 条原子命题（A 级全验，B 级基本通读，实际覆盖远超 30%），0 条 REFUTED，23 条 UNVERIFIED/需改写（均为"推断写成确认"、遗漏反向信号、或"全部/唯一"措辞过强），其余 CONFIRMED。没有发现数字/价格/名称/日期/原话类硬错误。

## 1) 统计（命题数为约数）

| 页 | 命题数 | CONFIRMED | REFUTED | UNVERIFIED/需改写 |
|---|---|---|---|---|
| index | 62 | 61 | 0 | 1 (U20) |
| game-info | 72 | 69 | 0 | 3 (U1 U2 U17) |
| gamepasses | 58 | 54 | 0 | 4 (U6 U11 U12 U13) |
| battle-pass | 62 | 57 | 0 | 5 (U3 U4 U5 U6b U7) |
| how-to-play | 52 | 50 | 0 | 2 (U2 U13) |
| cases | 62 | 61 | 0 | 1 (U14) |
| rewards | 50 | 47 | 0 | 3 (U9 U10 U16) |
| shop | 78 | 78 | 0 | 0 |
| updates | 78 | 75 | 0 | 3 (U5 U14 U15) |
| robux | 22 | 22 | 0 | 0 |
| beginner | 16 | 16 | 0 | 0 |
| author | 12 | 11 | 0 | 1 (U19) |

（跨页重复的同一句计入各页。）

### 已独立复现、无需改动的重点项（CONFIRMED，实测 2026-10-10）
- 4 个通行证名称/价格/创建时间/更新时间/描述为空全部与 game-passes API 一致（79/149/299/499；创建 29 Dec 2025 02:48-02:50 UTC；更新 10 Aug 2026 06:16-06:20 UTC；总和 1,026；displayDescription 全空）。
- 开发者商品：developerproducts API 一次返回 97 条、nextPageCursor 空；全部 IsForSale=true、无折扣、Description 全空、共用图标 88963008124478（我看图确认是灰色立方体）；价格 5–10,000；含 Case 的名字 49 条；16 家族（Case1-5 + 11 命名）；14 个家族每案单价各档相同，仅 Energy Sword（199→150）与 Karambit（149→150）例外；最常见价 199 共 12 条；50 条创建=更新时间；shop 页 13 组的条数与金额小计、43,177 总和、updates 页逐日期批次表（32/14/4/4/15/3/6/5/10/1/3 = 97）全部重算一致。
- entities.json：97 个商品 + 4 个通行证的 name/price/product_id/developer_product_id/pass_id/icon id/创建与更新日期逐字一致，0 处不符；页面 frontmatter 引用的 20 个 entity 键全部存在。
- 6 条活动（需带零起点游标才返回；无游标返回 0 条，limit=100 仍 6 条，nextPageCursor 空）：标题、副标题、起止时间、正文原话（Update 2 的 12 行、Update 的 6 行、Game Revert 全段）逐字一致；listing 创建日（26 Jan、31 Jan、5 Apr、5 Apr、9 Aug、15 Aug）、Update 2 更新于 16 Mar、"6 条中 4 条创建早于开始 2 周以上"均成立；两次 Update 起始相隔 42 天成立。
- description 全文：18 行非空文本；所有引号内原话（含 "(Xbox & PlayStation supported)"、ban 告示、"Unlock 70+ weapon skins (more coming soon)"）逐字存在；无兑换码、无 Discord 邀请。
- 群组：created 2025-11-27，owner BanjoMeni / FpsHolder，owner 账号 2025-08-03 创建，shout=null，gamesV2 仅 1 个游戏，角色 Developer/Owner/Holder 各 1 人，群描述原句一致；游戏 created 2025-12-04，genre Shooter/Deathmatch Shooter，maxPlayers 8，18 种语言逐个一致，badges 空，creator 群组 id 一致。
- 分级 Mild / "Violence (Repeated/Mild)" / minimumAge 0：用 POST apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation {"universeId":"9294074907"} 复现。
- Roblox 文档定句逐字存在：passes（"let you charge users a one-time Robux fee to access special privileges inside your game"）、developer-products（"an item or ability that a user can purchase more than once"）、private-servers（"a subscription-based feature that allows a player to decide who can play a game with them"、"a monthly Robux fee"）、social-media-links（"Social media links are only visible to users who have verified their age as at least 16 years old."）。社交链接两个接口今天均 401 "Authentication token is missing"。
- _images.json：23 个 rbxcdn URL 全部 200 且 content-type 为 image/*；通行证图标哈希与今天 thumbnails/v1/game-passes 返回一致；4 张图标亲眼看图，转录除 U12 外全部正确（2x Money / "Grants double money from kills."；2x XP / "Grants double XP."；2x Votes / "Your votes will count twice."；2x Case Luck / "Grants more luck when opening cases"）；事件图 alt 抽看 ev-update / th4 / ev-summer 与画面相符。
- 算术：全部重算无误（6×80=480 余 19；499/1026≈49%；221,667÷252,024≈88%；590,415,564÷310≈1.9M，4 Dec 2025 至 10 Oct 2026 = 310 天；Skip 每档单价；250/1,049 等）。
- 禁词扫描：无 onetap.wiki / onetaproblox.wiki / onetap.com 引用；无 Counter-Strike / Halo 等第三方挂钩；无兑换码、Discord 邀请、广告/变现话术。

### 易变值：今天取到的量级（均与页面 "as of 10 October 2026" 同量级，CONFIRMED）
| 项 | 页面（11:39 UTC） | 今天我取到 |
|---|---|---|
| visits | 590,415,564 | 590,558,100 |
| playing | 25,975 | 27,571 |
| favourites | 658,502 | 658,677 |
| likes / dislikes | 221,667 / 30,357 | 221,694 / 30,365 |
| group members | 207,489 | 207,538 |
| 公开服务器前 10 个 | 全部 8/8 | 8 个 8/8，2 个 7/8（见 U2） |
| game.updated | 8 Oct 2026 | 2026-10-08T20:11:58Z；v2 groups 为 2026-08-19T08:54Z（页面说法一致） |

## 2) 修改清单（无 REFUTED；以下为 UNVERIFIED / 需改写）

编号 | 文件 | 原句（逐字） | 判定 | 证据 | 改成什么

**U1 | game-info.md** | "The game's public Roblox page carries a private server price of 49 Robux in its page data. We could not open the purchase window without an account, so we have not confirmed that one can be bought at that price." | UNVERIFIED（遗漏反向信号，高优先级）| https://www.roblox.com/games/90568084448279/One-Tap 的 HTML 确有 data-private-server-price="49"（并有 data-private-server-product-id="3494986672"）；但 https://games.roblox.com/v1/games?universeIds=9294074907 同一游戏记录里 "createVipServersAllowed":false。两个一手字段互相矛盾，页面只写了支持 49 的一边。 | 改成："The game's public Roblox page carries a private-server price attribute of 49 Robux, but Roblox's own game record for One Tap reports createVipServersAllowed as false. The two disagree, and we could not open a purchase window without an account, so we do not say whether private servers can be bought." 同时把 tldr/其他页若引用 49 Robux 私服价的地方一并删除（我只在 game-info 见到）。

**U2 | game-info.md、how-to-play.md** | "the first ten servers returned were all full, at 8 of 8" / "the first ten servers it returned were all full at 8 of 8" | UNVERIFIED（时点值，今天不能复现）| https://games.roblox.com/v1/games/90568084448279/servers/Public?limit=10 今天返回 [8,8,8,8,8,8,8,8,7,7]/8；maxPlayers=8 成立。 | 保留 "maxPlayers 8"；改成 "When we read the public server list at 11:39 UTC on 10 October 2026, the first ten servers returned were full or one player short of full." 或直接删掉 8/8 的时点句，只留 max 8。

**U3 | battle-pass.md** | tldr/正文/title："Six more products skip tiers"、"six tier skip products"、"Second, six products have names that begin with Skip and refer to tiers."；title "Premium Price and Tier Skips" | UNVERIFIED（由商品名推功能）| developerproducts API：6 条 Skip* 记录 Description 均为空；"Skip All" 的名字里根本没有 tier。功能只能由名字推断。 | tldr 改："Six more products have names that begin with Skip (Skip One Tier, Skip Three Tiers, Skip Five Tiers, Skip Ten Tiers, Skip All, Skip All Tiers); none has a description, so what they skip is our reading of the names."；正文 Second 改为 "six products have names that begin with Skip, four of them naming a number of tiers"；title/seoTitle/description 里的 "Tier Skips" 可保留，但页首第一段加一句同样的限定。

**U4 | battle-pass.md** | "From those we can say that the pass runs in seasons, that it has tiers, and that a premium version is sold for Robux." | UNVERIFIED（推断写成确认）| 只有 3 个字面事实：商品名 "Premium Battlepass"；Update 2 listing 原文 "New Battlepass season"；商品名含 "Tier(s)"。没有任何一手文字说"这些商品属于同一个 pass"。 | "From those we can say that an official listing mentions a Battlepass season, and that the store has a product named Premium Battlepass and products named for tiers. We read these as parts of one battle pass, but no record says so."

**U5 | battle-pass.md、updates.md** | battle-pass tldr："Two event listings announce a new season: \"New Battlepass season\" (13 March 2026) and \"New BP Season\" (24 April 2026)."；updates："BP reads as battle pass, which the March listing spells out" | UNVERIFIED（"BP"=battle pass 是推断；battle-pass 页当事实用）| virtual-events 原文 April 为 "New BP Season"，March 为 "New Battlepass season"；官方没有写 BP 的全称。 | battle-pass 改："Two event listings mention a new season: \"New Battlepass season\" (13 March 2026) and \"New BP Season\" (24 April 2026; we read BP as Battlepass, the listing does not spell it out)."；"What is official" 表后同步；updates 句可保留但把 "BP reads as battle pass, which the March listing spells out" 改为 "We read BP as battle pass because the March listing says Battlepass; the April listing does not spell it out."

**U6 | battle-pass.md** | "so a second tap buys a second skip" ；gamepasses.md："So an Xp Boost is bought again each time, while 2x Level XP is paid for once." | UNVERIFIED（平台机制被写成游戏行为）| create.roblox.com 文档只说 developer product "can purchase more than once"（能力），没有说该游戏每个商品都可重复消耗/叠加。 | battle-pass："Roblox allows a developer product to be bought more than once; whether the game lets you stack skips is not stated." gamepasses："Roblox lets a developer product be bought more than once, so an Xp Boost can be bought again; a pass is paid for once. Whether boosts stack is not stated."

**U7 | battle-pass.md** | "By our reading of the record prices, there is no reason to buy the three-tier or ten-tier product." 与 "It is cheaper than Skip Ten Tiers at any point, which makes the ten-tier product hard to explain." | UNVERIFIED（建立在 U3 的名字推断上）| 价格算术成立（179/3≈59.7，850/10=85，850−600=250），但前提（Skip X Tiers 真跳 X 档、Skip All 真跳全部）无一手来源。 | "If the names describe what the products do, the three-tier and ten-tier products cost more per tier than the two cheaper ones; the records do not confirm what any Skip product does." 删去 "no reason to buy" 和 "hard to explain" 两句，或前面加 "If the names are accurate,"。

**U9 | rewards.md** | "A fourth track, the battle pass, is not in the description at all." | UNVERIFIED（把 battle pass 当作奖励轨道）| battle-pass 页自己写明 free/premium 轨道内容与"什么赚取进度"均未公布；"track" 是推断。 | "The battle pass is not in the description at all. A product named Premium Battlepass and two listing lines about a season appear elsewhere; what it rewards is not stated. It has its own battle pass page."

**U10 | rewards.md（连带 index/robux/shop 的 "Xp Boost timers"）** | rewards tldr："Four Xp Boost products cost 30, 60, 120 and 360 Robux for 30 minutes, 1 hour, 2 hours and 6 hours." | UNVERIFIED（时长/计时器来自商品名）| 4 条记录 Description 为空，仅名称 "Xp Boost 30 Minutes / 1 Hour / 2 Hours / 6 Hours"。正文表头已写 "Minutes in the name"，但 tldr 与 "timers" 是当事实说。 | tldr："Four products are named Xp Boost with 30 Minutes, 1 Hour, 2 Hours and 6 Hours in the name, at 30, 60, 120 and 360 Robux. By our division that is 1 Robux per minute named at every size." 其余页的 "Xp Boost timers" 可改 "Xp Boost products"。

**U11 | gamepasses.md** | tldr："The only official explanation is on the icons"；正文："So the short lines drawn on the icons are the whole of the developer's explanation" | UNVERIFIED（"我读了 X" ≠ "X 是全部"）| 只核对了 API 的 description 字段（空）和图标；游戏内商店文案、Discord、群页其他处未读（社交链接 401）。 | tldr："The only official explanation we could read is on the icons…"；正文 "…are the only explanation from the developer that we could read."

**U12 | gamepasses.md** | table 与引文 "Grants more luck when opening cases"（页面称 "this page quotes all four icons word for word"） | UNVERIFIED（局部）| 我下载 700×700 图并放大：该行左侧 "o" 被圆框裁掉（页面已说明），右侧 "cases" 的末个 "s" 被裁一半，其后是否还有句号（其余三张图的末行都以句号结尾）看不到。 | 表格该格改 "Grants more luck when opening cases" 后加说明 "(the frame cuts both ends of this line; a final full stop, if any, is not visible)"，并把 "word for word" 改为 "as far as the frame shows"。

**U13 | gamepasses.md、how-to-play.md** | how-to-play："One more match feature shows up in the store. … So players vote on something."；gamepasses："So One Tap has some kind of vote" | UNVERIFIED（由图标文字推功能）| 一手只有图标文字 "2x Votes" / "Your votes will count twice."；没有任何官方文本说明是哪种投票、是否在比赛中。 | how-to-play："The Double Voting Value pass icon reads … 'Your votes will count twice.' That implies some voting feature, but no official source we read says what is voted on or whether it happens in a match."（把 "match feature" 去掉）。

**U14 | cases.md、updates.md** | cases："The dates line up with the developer's listings. … Two families were created on 24 April, the day the April listing with \"2 New Weapon cases\" started."；updates："The case lines match the store: the cases page prices the Cosmic, Glitched, Energy Sword, Proto and Karambit products." | UNVERIFIED（活动 listing ≠ 商品上架；创建日因果）| 反例：Karambit 的 3 条记录创建于 28 Jan 2026，比 "New Karambit Case Additions"（Update 2，13 Mar）早 6 周；商品 Created 只是记录登记日。页面其他处已有免责声明，但这两句仍在把对应写成确认。 | cases："Several records were created within a day of a listing starts (12 March for Update 2, 24 April for the April listing). That is a match of dates and names; it does not show those products went on sale with that update, and the Karambit records date from 28 January." updates："The case names in the Update 2 listing also appear in product names (Cosmic, Glitched, Energy Sword, Proto, Karambit); the records do not show when each product reached the in-game shop."

**U15 | updates.md** | "Going by the six so far, as an event listing on the game's Roblox page, posted by Stringless Banjo." | UNVERIFIED（预测写成回答）| 6 条里 2 条（Revert/Game Revert）是事后才发的；game 记录 updated=2026-10-08 但 8 月 15 日后无任何 listing，说明不是每次改动都会有 listing。 | "The six listings are the only official announcements we could read. The records do not show that every update gets one: the game record's updated field reads 8 October 2026 while the newest listing is dated 15 August."（该 updated 字段页面前文已说不可靠，可只保留前半句并去掉预测。）

**U16 | rewards.md** | "So, according to the listing, the prize goes to the top 100 players and is handed out after the board resets." | UNVERIFIED（"reset" 的对象是推断）| 原文只有 "(Given after reset)"，未说 reset 的是排行榜。 | "According to the listing, the prize is for the top 100 and is \"Given after reset\"; the listing does not say what is reset."

**U17 | game-info.md（可选，非错误）** | "Its role list has three ranks above ordinary members, named Developer, Owner and Holder, and each is held by one account." | CONFIRMED，但不完整 | https://groups.roblox.com/v1/groups/1047647644/roles 另有 Guest(rank 0) 与同为 rank 1 的 "Cool People"（memberCount 207,610，高于 Member 的 207,538）。 | 可补半句 "The list also has a Guest role and a second rank-1 role named Cool People."（不补也不算错）。

**U19 | author.md** | "Every guide article published under the byline is listed at the end of this page."；description/正文含未替换占位符 "{{BRAND}}"（出现 2 处）| UNVERIFIED（页面自身一句断言取决于模板是否自动追加；占位符若未被构建替换会直接上线）| 本文件末尾没有文章列表，只有 "Where should you start?" 三个链接。 | 确认构建会替换 {{BRAND}} 且自动追加文章列表；否则删除该句。

**U20 | index.md / game-info.md（出处）** | "The maturity label comes from Roblox's experience-guidelines data, which is not available as a plain link." | UNVERIFIED（出处标注）| 值本身 CONFIRMED（POST get-age-recommendation，见上）。但 sourceUrls 里放的是游戏页 URL，该 HTML 不含 "Mild"/"Violence"（已 grep）。 | 在正文或 sourceUrls 旁注 "Roblox experience-guidelines API (POST request, universeId 9294074907)"；不要让读者以为游戏页 URL 里有这个值。

## 3) 建议转 draft 的页

- 无需整页转 draft。价格、名称、日期、原话、计数全部对得上，最弱的 battle-pass.md 价格表与算术站得住，问题只集中在"Skip 商品跳档、BP=battle pass、Premium Battlepass 属同一通行证"三处名字推断（U3-U7）。
- 若 U3–U7 不能在发布前改完：把 battle-pass.md 置 draft（其核心卖点"每档价格/值不值"全部依赖名字推断）；其余页可先发。
- 发布前必须处理（会被当成事实复述的）：U1（私服 49 Robux 与 createVipServersAllowed:false 冲突）、U3–U5、U19（占位符）。其余为措辞限定。

## 4) 方法说明/限制
- 取证全部为今天自取的线上接口与文档（无任何 dossier/raw 作证据）；dossier 仅用于定位出处，其中 F016 分级的 POST 路径我另行实测。
- 未验证项：badges"三次读取均为空"（我只读了一次，为空）；页面 11:39 UTC 的瞬时数值无法复现，只比较量级。
- 抽样（B 级）：因 A 级覆盖已近全页且未出现 REFUTED，我对 B 级（图片 alt、归纳性句子、建议句）做了通读而非随机 30%。
