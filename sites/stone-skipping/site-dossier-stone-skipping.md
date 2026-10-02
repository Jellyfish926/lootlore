# +1 Stone Skipping 事实底稿（dossier）

取证日：2026-10-02（UTC 11:19–11:38 首轮抓取；12:03–12:05 第 1 轮对抗验证后补取，逐条时间见 `raw/fetchlog.txt`；快照型数字只代表 11:19 这一刻）
范围：Roblox 体验「+1 Stone Skipping」，universeId 10765298801，rootPlaceId 111543903102439，创作者群组 Meow Labs（groupId 207366578）。
原始响应（供复核，**不进仓**）：`raw/`（games.json / votes.json / badges.json / badges_recheck.json / passes.json / passes_recheck.json / passes_legacy.json / devprod_p1.json / devprod_recheck.json / events.json / events_from.json / events_completed.json / events_now2.json / events_cursor.json / events_1204.json / vip_check.json / private_servers.json / docs_social.md / docs_social.html / docs_maturity.html / docs_passes_new.html / places.json / media.json / age.json / group.json / roles.json / group_games.json / wall.json / social.json / group_social.json / owner.json / thumbs.json / thumbs_small.json / icons.json / pass_icons.json / asset_icons.json / event_thumb_768.json / event_thumb_480.json / gamepage.html / docs_devproducts.html / docs_passes.html / suggest.txt / img/*.png / comp/*）。

来源分级：**S** = Roblox 官方接口 / 官方页面原文（含开发者自己登记在 Roblox 上的名称、价格、活动、宣传图与图标）；**A** = 开发者官方渠道原话（官方 Discord / X / 群组公告）；**B** = 可信二手；**C** = 第三方专站 / 视频转述（只当线索，不当事实来源）。
本轮 **A 级为 0 条**：群组 description 只有 "meow?"、shout 为 null；Discord / X 需登录（按规定不取），群组 wall 接口返回 404，均记「未获取」。所以全部可写事实都是 S 级。

**对任务背景的复核结论**：徽章 0 ✔（两次取数都是空数组）、通行证 11 ✔、开发者商品 78 ✔（nextPageCursor = null，一页取完；11:38 重取一致）、description 无兑换码 ✔、三个第三方专站存在 ✔。背景里没提到的三件事：① **11 个通行证 + 78 个商品的官方描述全部是空字符串** —— 与 mog-evolution（28/43 有描述）不同，本游戏的机制细节**没有任何官方文字**，只有名称和价格；② virtual-events 接口有一个官方活动「ADMIN ABUSE + WORLD 5」（10-03 16:00–18:00 UTC）；③ 官方图标上有「WORLD 4」横幅。在线人数本次读数 20,948（任务背景约 19,800，时点不同）。

## 1. 基本信息

| # | 事实 | 值 | 来源 URL / 字段 | 取数时间（UTC） | 级 |
|---|---|---|---|---|---|
| F1 | 标题（listing name） | +1 Stone Skipping | https://games.roblox.com/v1/games?universeIds=10765298801 `name` | 10-02 11:19 | S |
| F2 | description 首句用的名字 | "+1 Skipping Stones"（与标题写法不同，两个都是官方原文，照录不统一） | 同上 `description` | 10-02 11:19 | S |
| F3 | 创作者 | 群组 Meow Labs（id 207366578），type Group，hasVerifiedBadge false | 同上 `creator` | 10-02 11:19 | S |
| F4 | 创建时间 | 2026-09-05T19:40:44.021Z | 同上 `created` | 10-02 11:19 | S |
| F5 | 最近更新 | 2026-09-30T18:09:39.135Z（games API `updated`）；群组游戏列表接口的 `updated` 为 2026-09-23T02:50:03.75Z（字段口径不同，两者照录，正文只用前者） | 同上；https://games.roblox.com/v2/groups/207366578/games?accessFilter=Public&limit=50 | 10-02 11:19 | S |
| F6 | 类型 | genre_l1 Simulation，genre_l2 Incremental Simulator | games API | 10-02 11:19 | S |
| F7 | 单服人数上限 | 10 | games API `maxPlayers` | 10-02 11:19 | S |
| F8 | 价格 | 免费（price = null） | games API | 10-02 11:19 | S |
| F9 | 私服 | **无法确认**。games API `createVipServersAllowed` = false，但该字段不可靠：Blox Fruits（994732206）、Pet Simulator 99（3317771874）、DOORS（2440500124）三款已知有私服的游戏同样为 false（raw/vip_check.json，10-02 12:04）；私服接口 /v1/games/111543903102439/private-servers 返回 401。正文不再写「不开放」 | games API；https://games.roblox.com/v1/games?universeIds=994732206,3317771874,2440500124 | 10-02 11:19 / 12:04 | 未获取 |
| F10 | 访问量（快照） | 5,252,489 visits | games API `visits` | 10-02 11:19 | S |
| F11 | 在线（快照） | 20,948 playing | games API `playing` | 10-02 11:19 | S |
| F12 | 收藏（快照） | 202,909 | games API `favoritedCount` | 10-02 11:19 | S |
| F13 | 点赞 / 点踩（快照） | 10,362 / 435（点赞占比 95.97%，我们计算） | https://games.roblox.com/v1/games/votes?universeIds=10765298801 | 10-02 11:19 | S |
| F14 | 头像类型 | MorphToR15 | games API `universeAvatarType` | 10-02 11:19 | S |
| F15 | 内容分级 | Maturity: Minimal；descriptor「Suitable for everyone」 | POST https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation ，header content-type: application/json，body {"universeId":"10765298801"} | 10-02 11:19 | S |
| F16 | 徽章 | 0 个（data 空数组；11:38 重取仍为空） | https://badges.roblox.com/v1/universes/10765298801/badges?limit=100 | 10-02 11:19 / 11:38 | S |
| F17 | 通行证 | 11 个，全部 isForSale=true，displayDescription 全空，priceDiscountDetails 全空；旧接口 games.roblox.com/v1/games/<id>/game-passes 返回 404 errors code 0（未获取，以新接口为准） | https://apis.roblox.com/game-passes/v1/universes/10765298801/game-passes?passView=Full&pageSize=100 | 10-02 11:19 / 11:38 | S |
| F18 | 开发者商品 | 78 个，76 个 IsForSale=true，2 个 false 且 PriceInRobux=null；Description 全空；IsLimited / IsLimitedUnique 全 false | https://apis.roblox.com/developer-products/v2/universes/10765298801/developerproducts?limit=100 | 10-02 11:19 / 11:38 | S |
| F19 | 体验内 place | 只有 1 个：111543903102439「+1 Stone Skipping」（无 RANKED / 子 place） | https://develop.roblox.com/v1/universes/10765298801/places?limit=50 | 10-02 11:19 | S |
| F20 | 游戏页规范路径 | /games/111543903102439/1-Stone-Skipping；页面 HTML 的 title 为「+1 Stone Skipping \| Play on Roblox」 | games API `canonicalUrlPath`；https://www.roblox.com/games/111543903102439/1-Stone-Skipping | 10-02 11:21 | S |
| F21 | 距创建天数 | 取数时距创建 26 天 15.6 小时（正文写「less than four weeks」）；9-05 → 10-02 | 我们计算（F4、取数时间） | — | 计算 |

## 2. 群组

来源：https://groups.roblox.com/v1/groups/207366578 、/roles 、https://users.roblox.com/v1/users/2994850996 （S，10-02 11:19）

| # | 事实 | 值 | 级 |
|---|---|---|---|
| G1 | 群组名 | Meow Labs | S |
| G2 | 群组 description | "meow?"（全部内容就这一个词） | S |
| G3 | shout | null（无置顶公告） | S |
| G4 | 所有者 | username iPlayfade（userId 2994850996，displayName iPlayfade，hasVerifiedBadge false，账号创建 2021-10-20T19:24:59Z，个人简介为空） | S |
| G5 | 成员（快照） | 481,097（groups API `memberCount`；roles 接口 Member 角色同为 481,097） | S |
| G6 | 角色 | Guest（rank 0，0 人）/ Member（rank 1）/ Investor（rank 1，1 人）/ Admin（rank 254，0 人）/ Owner（rank 255，1 人） | S |
| G7 | 入群 | publicEntryAllowed true；hasVerifiedBadge false | S |
| G8 | communityTier | currentTier 3，previousTier 2，tierUpdatedTime 2026-09-24T00:08:09Z | S |
| G9 | 公开游戏 | 只有本游戏 1 款（https://games.roblox.com/v2/groups/207366578/games?accessFilter=Public&limit=50 ，nextPageCursor null） | S |
| G10 | 成员数 ÷ 收藏数 | 481,097 ÷ 202,909 = 2.37（正文写「more than twice」） | 计算 |
| G11 | 群组 wall | https://groups.roblox.com/v2/groups/207366578/wall/posts 返回 404，body {"errors":[{"code":0,"message":""}]}；原因不明（不写成「需登录」） | 未获取 |
| G12 | 群组 / 体验 social links | https://games.roblox.com/v1/games/10765298801/social-links/list 与 groups/.../social-links 返回 401「Authentication token is missing」。正文只写实测到的 401，可见性规则引用 R3 原文，不写「只对登录用户显示」 | 未获取 |

## 3. 玩法（官方 description 逐句原文）

来源：games API `description`（S，10-02 11:19；places 接口与游戏页 meta description 文字一致）

| # | 原文（含 emoji） | 我们可以写的 | 不可以写的 |
|---|---|---|---|
| L0 | "🌊 Skip stones across the water, level up, and throw farther in +1 Skipping Stones!" | 核心动作：在水面打水漂、升级、扔更远；description 自称 +1 Skipping Stones | — |
| L1 | "⚡ Every bounce gives you +1 Skill!" | 每次弹跳 +1 Skill（基础资源） | +1 之后怎么涨 |
| L2 | "💪 Train and level up to throw farther!" | 训练和升级让你扔得更远 | 等级门槛、训练怎么做 |
| L3 | "🏆 Reach farther zones to earn more Wins!" | 越远的 zone 给越多 Wins | zone 名称、距离、每个 zone 给多少 Wins |
| L4 | "🍩 Unlock better stones and unusual objects to throw... even a DONUT!" | 可解锁更好的石头和奇怪的投掷物，官方点名 DONUT | 完整清单、价格、各自效果 |
| L5 | "🐾 Collect pets for powerful boosts!" | 宠物给加成 | 加成对象与数值 |
| L6 | "🔄 Rebirth to grow stronger and beat your longest throw!" | Rebirth 让你更强；目标是刷新最远纪录 | Rebirth 条件、奖励、是否重置 |
| L7 | "👍 Like & Favorite if you enjoy the game!" | description 到此结束：无码、无社媒链接、无 World 字样 | — |

## 4. 通行证（11 个，全部在售，全部无官方描述）

来源：https://apis.roblox.com/game-passes/v1/universes/10765298801/game-passes?passView=Full&pageSize=100 （S；nextPageToken 空 = 全量；10-02 11:19，11:38 重取一致）。名称逐字复制 `name`（与 `displayName` 一致）。价格单位 Robux，`price` 与 `userBasePriceInRobux` 一致。

| # | 名称 | Robux | 在售 | 官方描述 | 创建（UTC） | 最后更新（UTC） | passId |
|---|---|---|---|---|---|---|---|
| P1 | Hatch +3 Eggs [STACKS] | 25 | 是 | （空） | 2026-09-14T13:20Z | 2026-09-14T14:27Z | 1975575792 |
| P2 | Auto Wins | 25 | 是 | （空） | 2026-09-14T19:01Z | 2026-09-14T21:32Z | 1975737922 |
| P3 | +1 Pet | 69 | 是 | （空） | 2026-09-29T13:40Z | 2026-09-30T13:33Z | 2002580384 |
| P4 | Koi Training Zone | 99 | 是 | （空） | 2026-09-29T09:15Z | 2026-09-29T13:41Z | 1997937475 |
| P5 | Hatch +8 Eggs [STACKS] | 145 | 是 | （空） | 2026-09-14T13:20Z | 2026-09-14T14:27Z | 1975287804 |
| P6 | Auto Rebirth | 149 | 是 | （空） | 2026-09-19T23:47Z | 2026-09-19T23:47Z | 1985061337 |
| P7 | +3 Pets | 195 | 是 | （空） | 2026-09-15T11:05Z | 2026-09-29T13:41Z | 1982684356 |
| P8 | Golden Training Zone | 249 | 是 | （空） | 2026-09-14T10:10Z | 2026-09-29T09:16Z | 1979541573 |
| P9 | Hatch +16 Eggs [STACKS] | 299 | 是 | （空） | 2026-09-14T13:20Z | 2026-09-14T14:27Z | 1979565519 |
| P10 | +6 Pets | 499 | 是 | （空） | 2026-09-29T13:41Z | 2026-09-30T13:33Z | 1998423525 |
| P11 | Admin Training Zone | 599 | 是 | （空） | 2026-09-14T10:10Z | 2026-09-29T09:16Z | 1975305800 |

计数（我们计算）：11 个合计 2,353 Robux；价格 25–599。分组合计：Auto Wins + Auto Rebirth = 174；三个 Training Zone = 947；+1/+3/+6 Pets = 763；三个 Hatch = 469。单价：+1 Pet 69.0、+3 Pets 65.0/只、+6 Pets 83.2/只；Hatch +3 8.3/个、+8 18.1/个、+16 18.7/个（把名称里的数字当数量，是我们的读法）。29 或 30 日有更新戳的通行证 6 个：三个 Training Zone + 三个 Pet 通行证。

## 5. 开发者商品（78 个）

来源：https://apis.roblox.com/developer-products/v2/universes/10765298801/developerproducts?limit=100 （S；nextPageCursor = null，即全量；10-02 11:19，11:38 重取一致）。名称逐字复制 `Name`（与 `displayName` 一致）。按创建时间排序。`Description` / `displayDescription` 78 个全空，所以下表没有描述列。

| # | 名称 | Robux | 在售 | 创建（2026，UTC） | 最后更新 | 图标 | ProductId |
|---|---|---|---|---|---|---|---|
| D1 | Starter Pack | 39 | 是 | 09-10 | 09-30 | 自定义 | 3712280631 |
| D2 | Skill Multiplier [TIER 1] | 3 | 是 | 09-10 | 09-14 | 自定义 | 3712280699 |
| D3 | Skill Multiplier [TIER 2] | 19 | 是 | 09-10 | 09-18 | 自定义 | 3712281019 |
| D4 | Skill Multiplier [TIER 3] | 45 | 是 | 09-10 | 09-18 | 自定义 | 3712281041 |
| D5 | Skill Multiplier [TIER 4] | 129 | 是 | 09-10 | 09-18 | 自定义 | 3712281129 |
| D6 | 2x Wins [PERMANENT] | 59 | 是 | 09-10 | 09-14 | 自定义 | 3712281171 |
| D7 | Skip Rebirth | 35 | 是 | 09-10 | 09-18 | 自定义 | 3712281203 |
| D8 | Wins Pack 1 | 25 | 是 | 09-10 | 09-14 | 自定义 | 3712281296 |
| D9 | Wins Pack 2 | 59 | 是 | 09-10 | 09-14 | 自定义 | 3712281324 |
| D10 | Wins Pack 3 | 115 | 是 | 09-10 | 09-14 | 自定义 | 3712281350 |
| D11 | Wins Pack 4 | 229 | 是 | 09-10 | 09-14 | 自定义 | 3712281382 |
| D12 | Wins Pack 5 [20% OFF] | 459 | 是 | 09-10 | 09-14 | 自定义 | 3712281439 |
| D13 | Skill Boost | 29 | 是 | 09-10 | 09-18 | 自定义 | 3712281537 |
| D14 | Wins Boost | 29 | 是 | 09-10 | 09-18 | 自定义 | 3712281559 |
| D15 | Boost Pack | 95 | 是 | 09-10 | 09-18 | 自定义 | 3712281589 |
| D16 | Rainbow Egg | 45 | 是 | 09-10 | 09-19 | 自定义 | 3712281643 |
| D17 | Rainbow Egg x3 | 99 | 是 | 09-10 | 09-19 | 自定义 | 3712281660 |
| D18 | Rainbow Egg x8 | 249 | 是 | 09-10 | 09-19 | 自定义 | 3712281678 |
| D19 | Skill Pack 1 [TIER 2] | 25 | 是 | 09-10 | 09-14 | 自定义 | 3712282224 |
| D20 | Skill Pack 2 [TIER 2] | 95 | 是 | 09-10 | 09-18 | 自定义 | 3712282242 |
| D21 | Skill Pack 3 [TIER 2] | 185 | 是 | 09-10 | 09-18 | 自定义 | 3712282260 |
| D22 | Skill Pack 1 [TIER 1] | 11 | 是 | 09-10 | 09-14 | 自定义 | 3712292163 |
| D23 | Skill Pack 2 [TIER 1] | 45 | 是 | 09-10 | 09-18 | 自定义 | 3712292223 |
| D24 | Skill Pack 3 [TIER 1] | 95 | 是 | 09-10 | 09-18 | 自定义 | 3712292244 |
| D25 | Claim All Gifts | 49 | 是 | 09-10 | 09-14 | 自定义 | 3712296556 |
| D26 | Admin Egg | 175 | 是 | 09-12 | 09-14 | 自定义 | 3712529899 |
| D27 | Admin Egg x3 | 459 | 是 | 09-12 | 09-14 | 自定义 | 3712529931 |
| D28 | Admin Egg x8 | 1149 | 是 | 09-12 | 09-14 | 自定义 | 3712529975 |
| D29 | Skill Pack 1 [TIER 3] | 45 | 是 | 09-12 | 09-14 | 自定义 | 3712542128 |
| D30 | Skill Pack 2 [TIER 3] | 185 | 是 | 09-12 | 09-18 | 自定义 | 3712542168 |
| D31 | Skill Pack 3 [TIER 3] | 369 | 是 | 09-12 | 09-18 | 自定义 | 3712542204 |
| D32 | 5x Wins [PERMANENT] | 229 | 是 | 09-12 | 09-14 | 自定义 | 3712543053 |
| D33 | 10x Wins [PERMANENT] | 575 | 是 | 09-12 | 09-14 | 自定义 | 3712543100 |
| D34 | Pirate Egg | 59 | 是 | 09-12 | 09-14 | 自定义 | 3712632204 |
| D35 | Pirate Egg x3 | 115 | 是 | 09-12 | 09-14 | 自定义 | 3712632219 |
| D36 | Pirate Egg x8 | 279 | 是 | 09-12 | 09-19 | 自定义 | 3712632245 |
| D37 | Admin Training Zone | 195 | 是 | 09-13 | 09-13 | 默认灰方块 | 3712634639 |
| D38 | Golden Training Zone | 315 | 是 | 09-13 | 09-13 | 默认灰方块 | 3712634656 |
| D39 | Boost Bundle | 无（null） | 否 | 09-13 | 09-13 | 默认灰方块 | 3712634943 |
| D40 | Power Boost | 无（null） | 否 | 09-13 | 09-13 | 默认灰方块 | 3712634969 |
| D41 | Wins Pack 5 | 575 | 是 | 09-13 | 09-14 | 自定义 | 3712636333 |
| D42 | Golden Zone | 115 | 是 | 09-13 | 09-13 | 默认灰方块 | 3712637237 |
| D43 | Admin Zone | 289 | 是 | 09-13 | 09-13 | 默认灰方块 | 3712637272 |
| D44 | Phoenix Relic [LIMITED STOCK] | 499 | 是 | 09-13 | 09-14 | 自定义 | 3712726391 |
| D45 | Skill Multiplier [TIER 5] | 255 | 是 | 09-14 | 09-18 | 自定义 | 3712868376 |
| D46 | Skill Multiplier [TIER 6] | 425 | 是 | 09-14 | 09-16 | 自定义 | 3712868411 |
| D47 | Skill Multiplier [TIER 7] | 615 | 是 | 09-14 | 09-16 | 自定义 | 3712868445 |
| D48 | Astronaut Egg | 59 | 是 | 09-19 | 09-23 | 自定义 | 3713687212 |
| D49 | Astronaut Egg x3 | 115 | 是 | 09-19 | 09-23 | 自定义 | 3713687457 |
| D50 | Astronaut Egg x8 | 279 | 是 | 09-19 | 09-23 | 自定义 | 3713687483 |
| D51 | King Doggy | 999 | 是 | 09-22 | 09-23 | 自定义 | 3714242159 |
| D52 | Offline Reward x3 | 9 | 是 | 09-26 | 09-28 | 默认灰方块 | 3714836657 |
| D53 | Chocolatier Egg | 59 | 是 | 09-26 | 09-26 | 自定义 | 3714883758 |
| D54 | Chocolatier Egg x3 | 115 | 是 | 09-26 | 09-26 | 自定义 | 3714883795 |
| D55 | Chocolatier Egg x8 | 279 | 是 | 09-26 | 09-26 | 自定义 | 3714883816 |
| D56 | Skill Multiplier [TIER 8] | 995 | 是 | 09-27 | 09-28 | 默认灰方块 | 3715117052 |
| D57 | Skill Multiplier [TIER 9] | 1499 | 是 | 09-27 | 09-28 | 默认灰方块 | 3715117082 |
| D58 | Skill Multiplier [TIER 10] | 1995 | 是 | 09-27 | 09-28 | 默认灰方块 | 3715117107 |
| D59 | Golden Skip | 12 | 是 | 09-29 | 09-29 | 默认灰方块 | 3715390318 |
| D60 | Diamond Skip | 19 | 是 | 09-29 | 09-29 | 默认灰方块 | 3715390383 |
| D61 | Devil Pack | 299 | 是 | 09-29 | 09-30 | 自定义 | 3715439442 |
| D62 | [GIFT] Boost Pack | 95 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715622988 |
| D63 | [GIFT] Skill Boost | 29 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715623007 |
| D64 | [GIFT] Wins Boost | 29 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715623023 |
| D65 | [GIFT] Admin Egg | 175 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715623069 |
| D66 | [GIFT] Admin Egg x3 | 459 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715623141 |
| D67 | [GIFT] Admin Egg x8 | 1149 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715630657 |
| D68 | [GIFT] Koi Training Zone | 99 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715630688 |
| D69 | [GIFT] Golden Training Zone | 249 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715630708 |
| D70 | [GIFT] Admin Training Zone | 599 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715630731 |
| D71 | [GIFT] +1 Pet | 69 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715630882 |
| D72 | [GIFT] +3 Pets | 195 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715630932 |
| D73 | [GIFT] +6 Pets | 499 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715630960 |
| D74 | [GIFT] Auto Wins | 25 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715630983 |
| D75 | [GIFT] Auto Rebirth | 149 | 是 | 09-30 | 09-30 | 默认灰方块 | 3715631006 |
| D76 | `Dragon Egg `（接口原值带尾随空格） | 59 | 是 | 10-01 | 10-01 | 自定义 | 3715841017 |
| D77 | Dragon Egg x3 | 115 | 是 | 10-01 | 10-01 | 自定义 | 3715841047 |
| D78 | Dragon Egg x8 | 279 | 是 | 10-01 | 10-01 | 自定义 | 3715841081 |

计数（我们计算，脚本对 raw/devprod_p1.json 求和）：
- C1 在售 76 个合计 20,195 Robux；非 [GIFT] 在售 62 个合计 16,375；14 个 [GIFT] 合计 3,820；价格 3–1,995。
- C2 Skill Multiplier [TIER 1–10]：3 / 19 / 45 / 129 / 255 / 425 / 615 / 995 / 1,499 / 1,995，合计 5,980；累计 3、22、67、196、451、876、1,491、2,486、3,985、5,980；后三档合计 4,489。5,980 ÷ 16,375 = 36.5%。
- C3 蛋：Rainbow 45 / 99 / 249；Admin 175 / 459 / 1,149；Pirate、Astronaut、Chocolatier、Dragon 均 59 / 115 / 279。每蛋单价：Rainbow 45.0 → 33.0 → 31.1；Admin 175.0 → 153.0 → 143.6；主题蛋 59.0 → 38.3 → 34.9。x8 相对 8 个单买：Rainbow 省 111（30.8%）、Admin 省 251（17.9%）、主题蛋省 193（40.9%）；主题蛋 x3 省 62（35.0%）。Admin ÷ 主题蛋：单个 2.97 倍、x3 3.99 倍、x8 4.12 倍。
- C4 Wins：Wins Pack 1–5 = 25 / 59 / 115 / 229 / 575；Wins Pack 5 [20% OFF] = 459（比 575 低 20.2%）；2x / 5x / 10x Wins [PERMANENT] = 59 / 229 / 575（分别等于 Wins Pack 2 / 4 / 5 的价格）。
- C5 [GIFT] 14 个：8 个对应通行证（价格与通行证相同：Auto Wins 25、+1 Pet 69、Koi 99、Auto Rebirth 149、+3 Pets 195、Golden 249、+6 Pets 499、Admin 599），3 个对应 Boost Pack / Skill Boost / Wins Boost（95 / 29 / 29，同价），3 个对应 Admin Egg / x3 / x8（175 / 459 / 1,149，同价）。三个 Hatch 通行证没有 [GIFT] 版。
- C6 同名异价：商品「Admin Training Zone」195（通行证 599）、商品「Golden Training Zone」315（通行证 249）；另有商品「Golden Zone」115、「Admin Zone」289。这四个商品都是 09-13 创建、默认灰方块图标。是否仍在游戏内出售：未获取（需进游戏核实）。
- C7 未上架：Boost Bundle、Power Boost（IsForSale false，PriceInRobux null，09-13 创建）。
- C8 26 个商品用默认灰方块图标（assetId 88963008124478）：D37–D40、D42–D43、D52、D56–D60、D62–D75。

### 从名称与图标能写的（S 原文 → 我们的写法）

所有「可以写成」都必须带 likely / suggests / from the name 之类的限定词，因为没有任何官方描述。

| # | 依据 | 可以写成 | 不可以写成 |
|---|---|---|---|
| M1 | 通行证名 Auto Wins、Auto Rebirth；图标：奖杯、两个环形箭头 | 「likely 自动领取 Wins / 自动 Rebirth」 | 具体速率、离线是否生效 |
| M2 | 通行证名 Koi / Golden / Admin Training Zone；图标是带平台的主题水道；L2 "Train" | 「likely 特殊训练区」 | 倍率、三者差别 |
| M3 | 通行证名 +1 Pet / +3 Pets / +6 Pets；图标是宠物 +1/+3/+6 | 「most likely 宠物栏位」 | 基础栏位数 |
| M4 | 通行证名 Hatch +3 / +8 / +16 Eggs [STACKS] | 「most likely 一次多孵；[STACKS] suggests 三者可叠加（合计 +27，469 Robux）」 | 基础孵化数 |
| M5 | 商品名 Skill Multiplier [TIER n] | 十档价格与累计 | 每档倍率、是否必须按顺序买 |
| M6 | 商品名 Skill Pack n [TIER n]、Wins Pack n | 「most likely 一次性给 Skill / Wins」 | 数量；[TIER] 的含义（只能标为猜测） |
| M7 | 商品名 2x / 5x / 10x Wins [PERMANENT] | 名称自带「永久」；是否叠加未说明 | 「永久」是平台保证 |
| M8 | Skill Boost / Wins Boost / Boost Pack：药水图标（蓝星瓶 / 黄星瓶 / 蓝焰瓶），名称无 [PERMANENT] | 「likely 限时加成」 | 时长、倍率 |
| M9 | 商品名 Skip Rebirth（35）、通行证 Auto Rebirth（149） | 「suggests Rebirth 有一个可付费跳过 / 自动化的条件」 | 条件是什么 |
| M10 | 商品名 Offline Reward x3、Claim All Gifts、Golden Skip、Diamond Skip | 名称与价格；Offline Reward「suggests 有离线收益」 | Golden / Diamond Skip 跳过什么 |
| M11 | Starter Pack 图标：白色独角猫宠物 + 黄、蓝两瓶星形药水 + 闪电；Devil Pack 图标：黑色带角红眼宠物 + 蓝黄绿三瓶药水 + 标 +1 的棕色小宠物；King Doggy 图标：戴皇冠披红披风持权杖的黄色小狗 | 「图标显示…；图标不是内容清单」 | 包里具体有什么 |
| M12 | Phoenix Relic [LIMITED STOCK]（499）；图标：金色凤凰徽章嵌红宝石；接口 IsLimited=false | 名称带限量标签，Roblox 的 limited 标志未设 | 库存数、效果 |
| M13 | 六种蛋的图标（彩虹蛋、绿黑带冠 Admin 蛋、海盗帽蛋、宇航员头盔蛋、紫礼帽巧克力蛋、带角红宝石龙蛋） | 蛋的名称、价格、上架日 | 蛋里的宠物、概率、属于哪个 World |

## 6. 官方活动

来源：https://apis.roblox.com/virtual-events/v1/universes/10765298801/virtual-events?limit=50 （S）。**接口返回不稳定**：10-02 11:19 两次请求（含 fromUtc=2026-09-01）各只返回 E1 这一条；12:03:24–12:03:27 连续 10 次请求（`?eventStatus=completed`、`?limit=50`、不带参数、其他 eventStatus 值）全部返回 3 条（raw/events_completed.json、events_now2.json 等）；12:04:48 起又只返回 1 条（12:04–12:05 共 18 次）。eventStatus 参数看起来不起筛选作用（各取值返回相同列表，三条的 eventStatus 都是 active）。3 条里的 universeId / placeId / host 都是本游戏与 Meow Labs，不是串返别的 universe。验证方（第 1 轮）也用 `?eventStatus=completed` 取到过。**第 2 轮复验后的结论**：稳定能取到 3 条的是带游标的请求 `https://apis.roblox.com/virtual-events/v1/universes/10765298801/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA`（验证方多次稳定；我方实测 4/4 次返回 3 条，previousPageCursor 非空，raw/events_cursor.json）；默认请求通常只返回即将开始的 1 条（我方同批 4 次里 3 次 1 条、1 次 3 条；验证方 6 次都是 1 条），`eventStatus` 参数不能取到过往活动。E11–E14、W5 的出处统一用游标 URL；updates / index / how-to-play / community 的 sourceUrls 与 entities 活动实体已换 / 补成游标 URL。

| # | 字段 | 值 |
|---|---|---|
| E1 | title | ADMIN ABUSE + WORLD 5 |
| E2 | subtitle | FIRST ADMIN ABUSE!! |
| E3 | description | "- Admin Abuse\n- World 5\n- New features"（三行） |
| E4 | 时间 | startUtc 2026-10-03T16:00:15.025Z，endUtc 2026-10-03T18:00:15.025Z（2 小时；2026-10-03 是周六） |
| E5 | host | Meow Labs（group 207366578），hasVerifiedBadge false |
| E6 | 分类 / 状态 | eventCategories newContent；eventStatus active；eventVisibility public |
| E7 | 创建 / 更新 | createdUtc 2026-09-26T09:04:02Z；updatedUtc 2026-10-01T14:47:19Z |
| E8 | 缩略图 | mediaId 118484159559809（「ADMIN ABUSE」黄字 + 打水漂场景） |
| E9 | 时区换算（我们计算，zoneinfo） | PDT 周六 09:00–11:00；EDT 12:00–14:00；BRT 13:00–15:00；BST 17:00–19:00；CEST 18:00–20:00；UTC+8 周日 10-04 00:00–02:00 |
| E10 | 推断 | "Admin Abuse" 的含义官方未写。第 1 轮验证后正文删掉了「品类惯例」那句（无出处），只写「副标题称这是第一次 admin abuse，listing 没解释内容」 |
| E11 | 过往活动 1 | title「World 3 + New Content」，subtitle 同 title，description 空；startUtc 2026-09-20T18:00:01Z，endUtc 2026-09-23T18:00:01Z；createdUtc 2026-09-15T14:32:14Z；updatedUtc 2026-09-20T16:42:03Z；newContent；host Meow Labs；id 4568563551630918292 |
| E12 | 过往活动 2 | title「WORLD 4 + UPDATE」，subtitle「CLICK TO NOTIFY!」，description 空；startUtc 2026-09-27T16:00:56Z，endUtc 2026-10-01T16:00:56Z；createdUtc 2026-09-22T11:53:59Z；updatedUtc 2026-09-27T11:12:59Z；newContent；host Meow Labs；id 109092769317913177 |
| E13 | 过往活动缩略图 | 两场的 mediaId（137066914653459、106193094296108）取到同一张图：「FREE BOOSTS!」「BIG UPDATE」字样 + 打水漂场景（raw/img/pastevent_*.png）；未收入 _images.json |
| E14 | 计算 | 主题蛋商品创建时间与活动开始：Astronaut 09-19 20:41 → World 3 活动 09-20 18:00（早 21 小时）；Chocolatier 09-26 14:46 → World 4 活动 09-27 16:00（早 25 小时）；Dragon 10-01 17:16 → World 5 活动 10-03 16:00（早 47 小时）。listing 没说蛋属于哪个 World，正文只写时间关系 |

**到期动作**：2026-10-04 把 updates 页活动一节改成过去时，重读 events 接口与两个商店接口；同步首页「What's happening this week?」一节、tldr、faq 第 5 条、community 页私服一节的活动句。

## 7. World 的一手证据

| # | 事实 | 来源 | 级 |
|---|---|---|---|
| W1 | 官方图标底部横幅文字「WORLD 4」 | https://thumbnails.roblox.com/v1/games/icons?universeIds=10765298801&size=512x512&format=Png （亲眼看 raw/img/icon.png） | S |
| W2 | 官方活动标题与描述含「WORLD 5」/「World 5」 | E1、E3 | S |
| W3 | description 没有 World 字样；商品 / 通行证里没有任何名称含 World 的条目。但 Golden Skip、Diamond Skip、Golden Zone、Admin Zone 无描述、作用未知，所以正文只写「没找到名称写明跳到某个 world 的商品」，不写「没有 skip to world 商品」 | L0–L7；§4、§5 | S |
| W5 | World 3、World 4 各有一场官方活动（E11、E12），活动窗口 09-20 18:00 起、09-27 16:00 起；活动无描述，只能说「活动标题与窗口」，不能说 world 开放的确切时刻 | events API（12:03） | S |
| W4 | World 2 的上线日期（没有任何活动标题含 World 2）；World 2–5 的解锁条件 | 无一手来源 | 未获取 |

## 8. 更新时间线（由官方创建时间戳拼出，不等于补丁说明）

| 日期（2026，UTC） | 出现了什么 | 来源 |
|---|---|---|
| 09-05 | 体验创建（19:40） | F4 |
| 09-10 | 25 个商品（D1–D25） | §5 |
| 09-12 | 11 个商品（D26–D36：Admin Egg ×3、Skill Pack [TIER 3] ×3、5x / 10x Wins、Pirate Egg ×3） | §5 |
| 09-13 | 8 个商品（D37–D44：两个同名 Training Zone 商品、Boost Bundle、Power Boost、Wins Pack 5、Golden Zone、Admin Zone、Phoenix Relic [LIMITED STOCK]） | §5 |
| 09-14 | 6 个通行证（Admin / Golden Training Zone、Hatch +3 / +8 / +16、Auto Wins）；商品 Skill Multiplier [TIER 5–7] | §4、§5 |
| 09-15 | 通行证 +3 Pets；活动「World 3 + New Content」登记（14:32） | §4、E11 |
| 09-19 | 通行证 Auto Rebirth；商品 Astronaut Egg ×3 | §4、§5 |
| 09-20 | 活动「World 3 + New Content」开始（18:00），09-23 18:00 结束 | E11 |
| 09-22 | 商品 King Doggy；活动「WORLD 4 + UPDATE」登记（11:53） | §5、E12 |
| 09-24 | 群组 communityTier 2 → 3 | G8 |
| 09-26 | 商品 Offline Reward x3、Chocolatier Egg ×3；活动登记（09:04） | §5、E7 |
| 09-27 | 商品 Skill Multiplier [TIER 8–10]；活动「WORLD 4 + UPDATE」开始（16:00），10-01 16:00 结束 | §5、E12 |
| 09-29 | 通行证 Koi Training Zone、+1 Pet、+6 Pets；商品 Golden Skip、Diamond Skip、Devil Pack | §4、§5 |
| 09-30 | 14 个 [GIFT] 商品；games API updated 18:09 | §5、F5 |
| 10-01 | 商品 Dragon Egg ×3（17:16）；活动条目更新（14:47） | §5、E7 |
| 10-03 | ADMIN ABUSE + WORLD 5 活动 16:00–18:00 | E4 |

计数（我们计算）：09-10 → 10-01 按日历含首尾共 22 天（正文写 within 22 calendar days），有新通行证或新商品创建的日期 12 个（09-10、12、13、14、15、19、22、26、27、29、30、10-01）。主题蛋间隔：Pirate 09-12 → Astronaut 09-19（7 天）→ Chocolatier 09-26（7 天）→ Dragon 10-01（5 天）。首批商品创建于体验创建后第 5 天。

## 9. 图片（S）

| # | 事实 | 来源 |
|---|---|---|
| I1 | 游戏页宣传图 4 张（media 接口 4 条 Image，无视频，altText 全空） | https://games.roblox.com/v2/games/10765298801/media |
| I2 | 768x432 与 480x270 两档 URL，8 个全部 curl 200；实际解码尺寸 767x432 | thumbnails multiget 接口；raw/img |
| I3 | art01（imageId 115530770000806）：橙发 Roblox 角色在草岸上扔出灰色扁石，石头在蓝色水面弹三次，每处水花标 +1 | 亲眼看 raw/img/art01.png |
| I4 | art02（110645317028002）：三格 —— 蓝底灰石「+1」/ 橙底裂纹熔岩石「+150M」/ 紫底银色飞碟「+4B」 | raw/img/art02.png |
| I5 | art03（135445766275325）：左「LEVEL 1」皱眉角色扔小石头一次水花 +1；右「LEVEL 999」同角色扔金色圆盘弹出很远「+1M」 | raw/img/art03.png |
| I6 | art04（75863455722029）：角色沿笔直长河投掷，物体一路弹向远处，每处 +1，上方黄色大字「999,999m」 | raw/img/art04.png |
| I7 | event（mediaId 118484159559809）：黄色大字「ADMIN ABUSE」+ 左岸角色 + 灰石打水漂 +1；768x432 / 480x270 两档 curl 200 | https://thumbnails.roblox.com/v1/assets?assetIds=118484159559809&size=768x432&format=Png |
| I8 | icon 512x512：黑外套橙发角色扔灰石，三处 +1，底部紫色横幅「WORLD 4」；curl 200 | icons 接口 |
| I9 | 通行证 / 商品图标 5 张 420x420（Koi Training Zone、Dragon Egg、King Doggy、Starter Pack、Devil Pack），curl 200 | https://thumbnails.roblox.com/v1/assets?assetIds=…&size=420x420&format=Png |

宣传图上的数字（+150M、+4B、+1M、LEVEL 999、999,999m）是官方美术文字，可以写成「官方宣传图显示…」，**不能**写成游戏内数值表。宣传图里出现的投掷物（灰石、熔岩石、飞碟、金色圆盘）不是物品清单。

## 10. 兑换码 / 社媒（结论：不建 codes 页，任何页都不列码）

| # | 事实 | 来源 | 级 |
|---|---|---|---|
| S1 | 游戏 description 无任何码 | games API description（L0–L7） | S |
| S2 | 群组 description = "meow?"，shout = null | groups API | S |
| S3 | 三场官方活动（World 3 + New Content、WORLD 4 + UPDATE、ADMIN ABUSE + WORLD 5）的 title / subtitle / description 均无码 | events API（E1–E3、E11–E12） | S |
| S4 | 游戏页 HTML（未登录）没有开发者的 Discord / YouTube / X 链接（grep discord 0 命中；页面里的 youtube.com/user/roblox 与 twitter meta 是 Roblox 自己的） | https://www.roblox.com/games/111543903102439/1-Stone-Skipping | S |
| S5 | 群组 wall | 404，无错误消息 | 未获取 |
| S6 | social links（体验 / 群组） | 接口无令牌返回 401「Authentication token is missing」 | 未获取 |
| S7 | 官方 Discord / X | 需登录，按规定不取 | 未获取 |
| S8 | 三个第三方专站都有 codes 页并列出「reported」码 | stoneskipping.wiki/codes/、stone-skipping.wiki/codes、1stoneskipping.wiki/codes/1-stone-skipping-codes（10-02 11:22） | C（只记「它们有码页」这一事实；码本身不抄、不进任何交付物） |
| S9 | 游戏内是否有输码框 | 只有第三方说法 | 未获取（待进游戏核实） |

## 11. Roblox 平台文档（S）

| # | 原文 | 来源 |
|---|---|---|
| R1 | "Passes let you charge users a one-time Robux fee to access special privileges inside your game, such as entry to a restricted area, an in-game avatar item, or a permanent power-up." 正文只引 "let you charge users a one-time Robux fee"，不再推成「每账号一次」 | https://create.roblox.com/docs/production/monetization/passes （旧地址 …/monetization/game-passes 301 到此；10-02 11:31 / 12:03） |
| R2 | "A developer product is an item or ability that a user can purchase more than once, such as in-game currency, ammo, or potions." | https://create.roblox.com/docs/production/monetization/developer-products （10-02 11:31） |
| R3 | "Social media links are only visible to users who have verified their age as at least 16 years old. Users who are under 16 years old or who have not verified their age **cannot** view social media links." | https://create.roblox.com/docs/production/promotion/social-media-links （10-02 12:04；.md 版 https://create.roblox.com/docs/en-us/production/promotion/social-media-links.md 同文） |
| R4 | 内容成熟度文档含 "Paid random items"、"Paid item trading" 描述符 —— 所以不能写「分级只管内容不管消费」；正文改为「该标签描述体验内容，不说明玩家可能花多少」 | https://create.roblox.com/docs/production/promotion/content-maturity （10-02 12:04） |

## 12. 需求证据（Google 下拉，2026-10-02 实测，raw/suggest.txt）

"stone skipping roblox" → stone skipping roblox codes；"stone skipping codes" → stone skipping codes / stone skipping codes roblox。"+1 stone skipping"、"+1 stone skipping codes"、"+1 stone skipping wiki"、"stone skipping roblox pets / world / rebirth / script / eggs / gamepass"、"stone skipping admin abuse"、"+1 skipping stones"、"skipping stones roblox" 均无下拉。搜索量：未获取（未用 Semrush，未估算）。

## 13. 第三方线索（C 级，**没有一条进入正文**；只用来列进游戏核实清单）

| 线索 | 出处 | 处理 |
|---|---|---|
| 区域链（5 个 zone 名称与顺序） | stoneskipping.wiki/zones/、stone-skipping.wiki/zones/… | 不采用；进 todo |
| 「Hacked Admin」蛋的价格与概率 | stoneskipping.wiki/pets/、stone-skipping.wiki/pets/… | 不采用；进 todo |
| Shop 里有输码框、码清单 | 三站 codes / shop 页 | 不采用；码一个不抄；进 todo |
| Auto Throw、Friend boost、Rebirth pads、Gifts（定时奖励）等系统 | stone-skipping.wiki、1stoneskipping.wiki 的 URL 与标题 | 不采用；进 todo |
| 过往活动「World 4 + UPDATE」 | stone-skipping.wiki/updates | 第 1 轮验证后已由 events 接口直接取到（E12，S 级）；正文用的是接口数据，不是专站说法 |

## 14. 未获取项汇总

| 项 | 原因 |
|---|---|
| 官方 Discord / X 内容 | 需登录，按规定不取 |
| 群组 wall | 接口 404（errors code 0，无消息，原因不明） |
| 体验 / 群组 social links | 接口无令牌返回 401；Roblox 文档称社交链接只对已验证年龄 ≥16 的用户可见（R3） |
| 旧通行证接口 | 404（已知对新游戏失效，以新接口为准） |
| 私服是否开放 | createVipServersAllowed 字段不可靠（F9）；私服接口 401 |
| World 2 的日期 | 没有任何官方活动标题含 World 2；接口对过往活动的返回不稳定（§6） |
| World 2–5 的解锁条件 | 无一手来源 |
| 所有数值（Skill 倍率、等级门槛、zone 距离与 Wins、石头清单与价格、宠物名与加成、蛋概率、Rebirth 条件与奖励、药水时长、pack 数量、基础宠物栏位与孵化数） | 公开接口不含；需进游戏核实 |
| 支持设备 | 本轮没有找到可匿名读取的接口，未取 |
| progameguides.com / destructoid.com / twinfinite.net（benchmark 用） | Cloudflare 拦截页（403），不过验证，停止该来源 |
| 搜索量 | 未用 Semrush，未估算 |

## 15. 正文 ↔ 底稿对应表（给验证员）

| 页 | 正文里的事实句用到的底稿条目 |
|---|---|
| index | F1–F4、F6–F13、F15–F18、F21；L1–L6；G1–G3、G5；E1–E4、E11、E12；W1；S1–S3、S8；§4 / §5 计数（11 个、25–599；78 个、76 在售；十档 Skill Multiplier、六种蛋、14 个 [GIFT]） |
| beginner | L1–L6；E1、E4；F4；G1 |
| how-to-play | F1–F2；L1–L6（表格逐句）；I4–I6；W1–W3、W5；E1、E4、E11、E12；M2、M3、M4、M9；§4 / §5（Skip Rebirth 35、Auto Rebirth 149、六种蛋、六个宠物 / 孵化通行证名） |
| updates | E1–E9、E11–E14；F4、F5；§8 时间线全表；W1–W5；I7、I8；计数（22 个日历日 12 个日期、蛋间隔 7 / 7 / 5 天） |
| community | S1–S8；G1–G12；F3、F7、F9（改为无法确认）、F10–F13、F15、F17–F18；E1、E7、E11、E12；W1；R3、R4 |
| robux | §4 / §5 计数；各类最低价（D2 3、D52 9、P1 / P2 25、D8 25、D13 / D14 29、D1 39、D16 45）；L2、L5、L6 |
| gamepasses | P1–P11 全表；§4 计数与单价；C5、C6；R1；M1–M4；§8（通行证四批日期） |
| pets | L5；C3；D16–D18、D26–D28、D34–D36、D48–D50、D53–D55、D76–D78；D1、D61、D51；M11、M13；P3、P7、P10、P1、P5、P9；C5；E4 |
| boosts | C2、C4；D19–D24、D29–D31（Skill Pack）；D13–D15；C5、C7；R1、R2；M5–M8；L1–L6；I4、I6 |
| shop | D1–D78 全表；C1、C2、C6、C7；F16、F17；M10、M12；R2 |
| author | 无新事实（编辑方针页）；S1–S3 的结论 |
