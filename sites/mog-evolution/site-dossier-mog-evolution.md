# +1 Mog Evolution 事实底稿（dossier）

取证日：2026-10-01（UTC 约 11:10-11:25 抓取；快照型数字只代表这一刻）
范围：Roblox 体验「[W3] +1 Mog Evolution」，universeId 10764479526，rootPlaceId 92648272637932，创作者群组 Navoj Mog（groupId 426881025）。
原始抓取文件（来源笔记，供复核，不进仓）：`raw/`（games.json / votes.json / badges.json / badges_recheck.json / passes.json / passes_legacy.json / devprod.json / age.json / media.json / places.json / group.json / roles.json / wall.json / group_games.json / testing_universe.json / social.json / events.json / events_from.json / icons.json / thumbs.json / thumbs_small.json / gamepage.html / suggest.txt / art01-08.png / icon.png / 竞品 comp_*.html、sitemap_*.xml、c1_*.html、c_*.html）。

来源分级：S = Roblox 官方 API / 官方页面（开发者自己在 Roblox 上登记的数据，含开发者商品描述、官方宣传图、官方活动）；A = 开发者官方群组公告 / 官方 Discord 公告（本次**无**：群组 description 为空、shout 为 null、wall 接口报错、social links 接口需登录）；B = 第三方站 / 视频；C = 论坛 / 推断。

**对任务背景的复核结论**：背景说「机制偏薄、通行证可能为 0、徽章可能为 0」——徽章 0 ✔（两次取数一致）、通行证 0 ✔（新接口空数组，旧接口报错）；但「机制偏薄」**不成立**：开发者商品接口有 **43 个商品，其中 28 个带官方描述**，描述里写明了 Auto Clicker 22 次/秒、VIP 10 倍、跑步机倍率、Rebirth 有等级上限、Ascend 换下一个 body、Stage 1-3 传送、World 2/3 等机制。两个抢注站（mogevolution.wiki / mog-evolution.wiki）一个商品都没写，这是我们的主差异点。另外 places 接口证明体验内有一个「[RANKED]」子 place，virtual-events 接口有一个官方活动「Admin Abuse & Update 4」（10-03 → 10-07）。

## 1. 基本信息

| # | 事实 | 值 | 来源 | 级 |
|---|---|---|---|---|
| 1 | 正式名 | [W3] +1 Mog Evolution | https://games.roblox.com/v1/games?universeIds=10764479526 `name` | S |
| 2 | 创作者 | 群组 Navoj Mog（groupId 426881025），类型 Group，无认证标 | 同上 `creator` | S |
| 3 | 创建时间 | 2026-08-30T13:57:39Z | 同上 `created` | S |
| 4 | 最近更新 | 2026-09-30T17:52:34Z（games API `updated`）；群组游戏列表接口的 `updated` 为 2026-09-26T22:48:57Z（字段口径不同，两者都照录） | 同上；https://games.roblox.com/v2/groups/426881025/games?accessFilter=Public&limit=50 | S |
| 5 | 类型 | Simulation › Incremental Simulator | games API `genre_l1/genre_l2` | S |
| 6 | 单服人数上限 | 12 | games API `maxPlayers` | S |
| 7 | 价格 | 免费（price = null） | games API | S |
| 8 | 私服 | 不开放（createVipServersAllowed = false） | games API | S |
| 9 | 访问量（快照） | 31,783,618 visits | games API | S |
| 10 | 在线（快照） | 7,523 playing | games API | S |
| 11 | 收藏（快照） | 344,986 | games API `favoritedCount` | S |
| 12 | 点赞/点踩（快照） | 265,568 / 5,291（点赞占比 98.0%，我们计算） | https://games.roblox.com/v1/games/votes?universeIds=10764479526 | S |
| 13 | 头像类型 | MorphToR15 | games API `universeAvatarType` | S |
| 14 | 内容分级 | Maturity: Minimal；descriptor「Suitable for everyone」 | POST https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation body {"universeId":"10764479526"} | S |
| 15 | 徽章 | 0 个（data 空数组；按 skill「结论前复查」重取一次，仍为空） | https://badges.roblox.com/v1/universes/10764479526/badges?limit=100 | S |
| 16 | 通行证 | 0 个（gamePasses 空数组）；旧接口 games.roblox.com/v1/games/<id>/game-passes 返回 errors code 0（未获取，以新接口为准） | https://apis.roblox.com/game-passes/v1/universes/10764479526/game-passes?passView=Full&pageSize=100 | S |
| 17 | 体验内 place | 主 place 92648272637932「[W3] +1 Mog Evolution」+ 子 place 88916320688607「+1 Mog Evolution [RANKED]」（description 空） | https://develop.roblox.com/v1/universes/10764479526/places?limit=50 | S |
| 18 | 测试版 | 同群组另有 universe 10765888078「+1 Mog evolution [TESTING]」，2026-09-10 创建，访问 1,287，在线 0，maxPlayers 50，description null | https://games.roblox.com/v1/games?universeIds=10765888078 | S |

## 2. 群组

来源：https://groups.roblox.com/v1/groups/426881025 、/roles（S）

| # | 事实 | 值 | 级 |
|---|---|---|---|
| 19 | 群组名 | Navoj Mog | S |
| 20 | 群组描述 | 空字符串 | S |
| 21 | shout | null（无置顶公告） | S |
| 22 | 所有者 | username CreatorExchangeInc（userId 11551976004，未认证） | S |
| 23 | 成员（快照） | 5,456,141（roles 接口 Member 角色 5,456,192，两接口时点差） | S |
| 24 | 角色 | Guest / Member / Admin（rank 254，1 人）；无 Tester 角色 | S |
| 25 | communityTier | 3（2026-09-11 由 2 升到 3） | S |
| 26 | 公开游戏 | 本游戏 + 「+1 Mog evolution [TESTING]」两款 | S |
| 27 | 群组 wall | v2 wall/posts 返回 errors code 0（未获取） | 未获取 |
| 28 | 群组/体验 social links | 接口要求登录（code 9002）；游戏页 HTML 无 Discord/YouTube/TikTok 链接 | 未获取 |
| 29 | 第三方说法：群组成员 9 月 11 日「16,800+」 | mogevolution.wiki/trello/（只作对比，不进正文数字） | B/C |

## 3. 玩法（官方描述原文逐句）

来源：games API `description`（S）

| # | 原文 | 我们可以写的 |
|---|---|---|
| 30 | "Welcome to +1 Mog Evolution" | — |
| 31 | "👆 Every Click gives you MORE Appeal" | 点击得 Appeal（主资源） |
| 32 | "🔨 Upgrade your hammer to Bonesmash and get even more Appeal" | 锤子可升级，Bonesmash 是官方点名的一档 |
| 33 | "🏆 Earn Wins to ascend and mog more people" | Wins 与 ascend 相关 |
| 34 | "🌍 Climb the leaderboard to become a True Adam" | 排行榜目标是 True Adam |
| 35 | "👍 Like & ⭐ Favorite the game to support future updates!" / "🔥 Thanks for playing and have fun!" | 无码、无社媒链接 |

## 4. 开发者商品（43 个，全部在售，全部官方）

来源：https://apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100（S；nextPageCursor = null，即全量）。名称、描述逐字复制。价格单位 Robux。

| # | 名称 | Robux | 官方描述（逐字；空=无描述） | 创建 | 最后更新 |
|---|---|---|---|---|---|
| P1 | +100K Appeal | 49 | Instantly gain 100,000 Power. | 08-30 | 09-10 |
| P2 | +1M Appeal | 149 | Instantly gain 1,000,000 Power. | 08-30 | 09-10 |
| P3 | +10M Appeal | 299 | Instantly gain 10,000,000 Power. | 08-30 | 09-10 |
| P4 | Skip Ascend | 29 | Ascend to the next body instantly, no requirements. | 08-30 | 09-10 |
| P5 | Skip Rebirth | 39 | Rebirth instantly without reaching the level cap. | 08-30 | 09-10 |
| P6 | Teleport Stage 1 | 2 | Unlock the Stage 1 teleport. | 08-30 | 09-08 |
| P7 | Teleport Stage 2 | 5 | Unlock the Stage 2 teleport. | 08-30 | 09-08 |
| P8 | Teleport Stage 3 | 9 | Unlock the Stage 3 teleport. | 08-30 | 09-08 |
| P9 | x1.5 Power | 1 | Permanently earn 1.5x Power. | 08-30 | 09-10 |
| P10 | x2 Power | 2 | Permanently earn 2x Power. | 08-30 | 09-08 |
| P11 | x4 Power | 5 | Permanently earn 4x Power. | 08-30 | 09-08 |
| P12 | x8 Power | 12 | Permanently earn 8x Power. | 08-30 | 09-08 |
| P13 | x16 Power | 19 | Permanently earn 16x Power. | 08-30 | 09-08 |
| P14 | x32 Power | 29 | Permanently earn 32x Power. | 08-30 | 09-08 |
| P15 | x64 Power | 49 | Permanently earn 64x Power. | 08-30 | 09-08 |
| P16 | x128 Power | 79 | Permanently earn 128x Power. | 08-30 | 09-08 |
| P17 | x256 Power | 199 | Permanently earn 256x Power. | 08-30 | 09-08 |
| P18 | X2 Wins | 49 | Permanently earn double Wins. | 08-30 | 09-08 |
| P19 | Starter Pack | 9 | One-time offer: the LTN body, +2,000 Appeal and +50 Wins. Can only be bought once. | 08-31 | 09-10 |
| P20 | VIP | 99 | Permanent VIP: earn 10x Appeal, plus a VIP name tag. Can only be bought once. | 08-31 | 09-08 |
| P21 | +100M Appeal | 499 | Instantly gain 100,000,000 Appeal. | 08-31 | 09-10 |
| P22 | x9 Treadmill | 69 | Unlock the x9 treadmill belt. Earn 9x Appeal while standing on it, no rebirths needed. | 08-31 | 09-10 |
| P23 | x99 Treadmill | 249 | Unlock the x99 treadmill belt. Earn 99x Appeal while standing on it, no rebirths needed. | 08-31 | 09-10 |
| P24 | x999 Treadmill | 999 | Unlock the x999 treadmill belt. Earn 999x Appeal while standing on it, no rebirths needed. | 08-31 | 09-10 |
| P25 | Auto Clicker | 39 | Permanent Auto Clicker unlock. Automatically earns Appeal at 22 clicks per second. Can only be bought once. | 08-31 | 09-10 |
| P26 | 2x Win Pad | 49 | （空） | 09-09 | 09-09 |
| P27 | Gigachad [LIMITED] | 399 | Permanently unlock the Gigachad body in +1 Mog Evolution. Gives a x4 body Appeal multiplier while equipped. One unlock per player. The 1,500-copy counter is informational; purchases remain available after it reaches zero. | 09-10 | 09-10 |
| P28 | Claviculars Hammer | 399 | Permanently unlock Claviculars Hammer in +1 Mog Evolution. Gives x1024 Appeal while equipped. Unlimited availability; one permanent unlock per player. | 09-10 | 09-10 |
| P29 | Skip to World 2 | 99 | （空） | 09-10 | 09-10 |
| P30 | Buy Hammer Upgrade [1] | 29 | （空） | 09-18 | 09-18 |
| P31 | Buy Hammer Upgrade [2] | 79 | （空） | 09-18 | 09-18 |
| P32 | Mogger Pack | 99 | （空） | 09-18 | 09-19 |
| P33 | x2 Treadmill | 9 | （空） | 09-18 | 09-18 |
| P34 | x3 Treadmill | 19 | （空） | 09-18 | 09-18 |
| P35 | x5 Treadmill | 39 | （空） | 09-18 | 09-18 |
| P36 | x8 Treadmill | 79 | （空） | 09-18 | 09-18 |
| P37 | x12 Treadmill | 99 | （空） | 09-18 | 09-18 |
| P38 | x18 Treadmill | 129 | （空） | 09-18 | 09-18 |
| P39 | Smoothie | 399 | Permanently unlock Smoothie in +1 Mog Evolution. Gives x2048 Charisma while equipped. Unlimited availability; one permanent unlock per player. | 09-24 | 09-24 |
| P40 | Skip to World 3 | 99 | （空） | 09-24 | 09-24 |
| P41 | Revenge | 99 | （空） | 09-24 | 09-24 |
| P42 | LOOKSMEOWXER [W2 LIMITED] | 399 | （空） | 09-26 | 09-26 |
| P43 | MANGO MOGGER [W3 LIMITED] | 399 | （空） | 09-26 | 09-26 |

计数（我们计算）：43 个，全部 IsForSale=true；带描述 28 个、无描述 15 个；价格 1-999 Robux；全买一遍合计 5,910 Robux（我们计算，raw/devprod.json 求和）；9 档 Power 合计 395、9 档跑步机合计 1,691。

### 从商品描述能写的机制（S 原文 → 我们的写法）

| # | 原文依据 | 可以写成 | 不可以写成 |
|---|---|---|---|
| M1 | P25 "Automatically earns Appeal at 22 clicks per second" | Auto Clicker 每秒 22 次点击 | 手动点击的上限是多少 |
| M2 | P20 "earn 10x Appeal, plus a VIP name tag" | VIP = 10 倍 Appeal + 名牌 | VIP 与其他倍率叠加方式 |
| M3 | P22-24 "Earn 9x/99x/999x Appeal while standing on it, no rebirths needed" | 有跑步机（treadmill belt），站上去才生效；描述说购买版"不需要 rebirth" | 「免费跑步机靠 rebirth 解锁」只能写成「描述暗示」 |
| M4 | P33-38 x2/x3/x5/x8/x12/x18 Treadmill（无描述） | 名称与价格 | 效果（按名称推断与 x9 同类，标推断） |
| M5 | P5 "Rebirth instantly without reaching the level cap" | Rebirth 正常需要达到等级上限 | 等级上限是多少、rebirth 给什么 |
| M6 | P4 "Ascend to the next body instantly, no requirements" | Ascend = 换到下一个 body；正常有要求 | 要求是什么（官方描述只说 "Earn Wins to ascend"） |
| M7 | P6-8 "Unlock the Stage 1/2/3 teleport" | 有 Stage 1-3 与对应传送点 | Stage 是什么、在哪 |
| M8 | P9-17 "Permanently earn N x Power" | 9 档永久 Power 倍率 | 是否叠加、是否必须按顺序买 |
| M9 | P1-3 商品名 "Appeal"、描述 "Power"；P21 描述 "Appeal"；P39 "Charisma" | 官方文案里 Appeal / Power / Charisma 三个词都出现；我们按商品名判断 Power 很可能就是 Appeal（标为我们的读法） | 「Charisma 就是 Appeal」写成确认 |
| M10 | P19 "the LTN body, +2,000 Appeal and +50 Wins. Can only be bought once." | Starter Pack 内容 | LTN 在 body 序列中的位置 |
| M11 | P27 "Gigachad body … x4 body Appeal multiplier while equipped … 1,500-copy counter is informational; purchases remain available after it reaches zero" | Gigachad 是 body，x4，计数器只是展示 | — |
| M12 | P28 "Claviculars Hammer … x1024 Appeal while equipped" | 付费锤子 x1024 | 与 Bonesmash 的关系 |
| M13 | P39 "Smoothie … x2048 Charisma while equipped" | 装备型物品 x2048 Charisma | Smoothie 属于哪个装备栏 |
| M14 | P29 / P40 "Skip to World 2 / World 3" | 至少有 World 1-3 | 正常解锁条件 |
| M15 | P18 "Permanently earn double Wins."；P26 "2x Win Pad"（无描述） | Wins 有付费倍率 | Win Pad 是什么（按名推断是赢取 Wins 的平台，标推断） |
| M16 | P30-31 Buy Hammer Upgrade [1]/[2]（无描述） | 锤子升级有可付费购买的档位 | 这两档是不是 Bonesmash |

## 5. 官方活动

来源：https://apis.roblox.com/virtual-events/v1/universes/10764479526/virtual-events?limit=50（S；加 fromUtc=2026-08-01 也只返回这一条，过往活动未获取）

| # | 字段 | 值 |
|---|---|---|
| E1 | title / description | Admin Abuse & Update 4（描述与标题相同，无更多文字） |
| E2 | 时间 | 开始 2026-10-03T23:00:21Z，结束 2026-10-07T23:00:21Z（4 天） |
| E3 | host | Navoj Mog（group 426881025） |
| E4 | 分类 | newContent |
| E5 | 创建 | 2026-09-28T02:24:20Z |
| E6 | 推断 | 标题 "Update 4" → 此前有 3 次大更新（我们的读法，未确认编号口径）；"Admin Abuse" 在 Roblox 惯指开发者在线发放加成的活动，本游戏活动内容官方未写（C） |

**到期动作**：活动页内容（updates 页中的活动一节）在 2026-10-08 改写为过去时，并核对是否有新活动；不单独建活动页。

## 6. 更新时间线（由官方创建/更新时间戳拼出，不等于补丁说明）

| 日期（2026） | 出现了什么 | 来源 |
|---|---|---|
| 08-30 | 体验创建（13:57 UTC）；18 个商品：+100K/+1M/+10M Appeal、Skip Ascend、Skip Rebirth、Teleport Stage 1-3、x1.5-x256 Power 九档、X2 Wins | games API / devprod |
| 08-31 | Starter Pack、VIP、+100M Appeal、x9/x99/x999 Treadmill、Auto Clicker（7 个） | devprod |
| 09-08 / 09-10 | 多数早期商品的 Updated 戳落在这两天（批量编辑） | devprod |
| 09-09 | 2x Win Pad | devprod |
| 09-10 | Gigachad [LIMITED]、Claviculars Hammer、Skip to World 2；同日 [TESTING] universe 创建 | devprod / testing_universe |
| 09-11 | 群组 communityTier 2 → 3 | group |
| 09-18 | Buy Hammer Upgrade [1]/[2]、Mogger Pack、x2/x3/x5/x8/x12/x18 Treadmill（9 个） | devprod |
| 09-24 | Smoothie、Skip to World 3、Revenge | devprod |
| 09-26 | LOOKSMEOWXER [W2 LIMITED]、MANGO MOGGER [W3 LIMITED]；群组游戏列表 updated 22:48 UTC | devprod / group_games |
| 09-28 | 官方活动「Admin Abuse & Update 4」登记 | events |
| 09-30 | games API updated 17:52 UTC | games |
| 10-03 → 10-07 | Admin Abuse & Update 4 活动窗口 | events |

第三方说法（B，只作旁证，不当事实）：mogevolution.wiki/updates/world-3/ 称标题 9 月 16 日-24 日为 [W2]、9 月 26 日后为 [W3]；我们只亲眼见到 10-01 的 [W3] 标题。

## 7. 图片（S）

| # | 事实 | 来源 |
|---|---|---|
| I1 | 游戏页 8 张宣传图 + 1 个宣传视频（videoId 119605172922403，与图 1 同 imageId），altText 全空 | https://games.roblox.com/v2/games/10764479526/media |
| I2 | 768x432 与 480x270 两档 URL，16 个全部 curl 200（2026-10-01） | thumbnails multiget 接口 |
| I3 | 图标 512x512 curl 200 | https://thumbnails.roblox.com/v1/games/icons?universeIds=10764479526&size=512x512&format=Png |
| I4 | art01：两个橙发雕塑头像侧脸，左红底（下垂憔悴脸）、右绿底（棱角分明英俊脸） | 亲眼看 raw/art01.png |
| I5 | art02：三个蓝底分格，头像从憔悴到英俊，周围数字 +1 → +67 → +999，箭头连接 | raw/art02.png |
| I6 | art03：左 "CHOPPED" 红底胖角色、右 "MOGGER" 蓝天肌肉角色 | raw/art03.png |
| I7 | art04：草地上小个子 "YOU" 箭头指向高大肌肉 "BOSS" | raw/art04.png |
| I8 | art05：三格 "Sub 3"（瘦小）/"MTN"（肌肉，红底）/"Chad"（肌肉，蓝底） | raw/art05.png |
| I9 | art06："SUB 3" 胖角色周围 +1 → 箭头 → "True Adam" 肌肉角色周围 +999 | raw/art06.png |
| I10 | art07：中间普通头像，左箭头 "TRUE ADAM"（英俊），右箭头 "SUBHUMAN"（憔悴） | raw/art07.png |
| I11 | art08：草地上五个角色从小到大排成一列，左上 "CHOPPED"、右上彩虹字 "MOGGER" | raw/art08.png |
| I12 | 图标：橙发、蓝眼、黑蓝上衣的肌肉 Roblox 角色正面，背景云层 | raw/icon.png |

宣传图上的标签（Sub 3、MTN、Chad、True Adam、Subhuman、Chopped、Mogger、Boss）是官方美术文字，可写成「官方宣传图上出现的标签」；**不能**写成游戏内 body 的完整顺序或解锁条件。商品里能确认是 body 的只有 LTN（P19）和 Gigachad（P27）。

## 8. 兑换码 / 社媒（结论：不建 codes 页）

| # | 事实 | 来源 | 级 |
|---|---|---|---|
| C1 | 游戏描述无任何码 | games API description | S |
| C2 | 群组 description 空、shout = null | groups API | S |
| C3 | 群组 wall 接口报错 | groups v2 wall | 未获取 |
| C4 | social links 需登录；游戏页 HTML 无外链 | games / groups social-links | 未获取 |
| C5 | 两个抢注站码页均为「0 个 active」 | mogevolution.wiki/codes/（9-27 检查） | B |
| C6 | 官方活动描述无码 | events API | S |
| C7 | 攻略博客 UrGameTips 码页写 "No working codes are listed right now"（Updated September 26, 2026；验证员第 1 轮提供，2026-10-01 我方复取 200 一致） | https://urgametips.com/plus-1-mog-evolution-codes/ | B（仅交叉核对） |
| C8 | Roblox Help「Cheating and Exploiting」：作弊/外挂违反 Roblox Terms of Use，会导致删号，并警告 keylogger/phishing（验证员核得；我方直连 403 未复取） | https://en.help.roblox.com/hc/en-us/articles/203312450-Cheating-and-Exploiting | S（Roblox 官方帮助） |

## 9. 需求证据（Google 下拉，2026-10-01 实测，raw/suggest.txt）

"mog evolution" → mog evolution script / mog evolution / mog evolution script keyless / mog evolution codes。"+1 mog evolution"、"mog evolution roblox / wiki / world 2 / bodies / true adam / hammer" 均无下拉。搜索量：未获取（未用 Semrush，未估算）。

## 10. 未获取项汇总（需进游戏核实）

- 手动点击收益、Bonesmash 之外的锤子档位名称与价格（游戏币）、Bonesmash 的解锁条件
- Wins 怎么赚（Win Pad 的位置与机制）、Ascend 需要多少 Wins、body 的完整顺序
- Rebirth 等级上限、rebirth 奖励、免费跑步机的解锁条件
- Stage 1-3 是什么；World 2 / World 3 的正常解锁条件
- Power 倍率是否叠加、是否需按顺序购买；VIP、跑步机、body、锤子倍率之间的乘法关系
- 15 个无描述商品（2x Win Pad、Skip to World 2/3、Hammer Upgrade [1]/[2]、Mogger Pack、x2-x18 Treadmill、Revenge、LOOKSMEOWXER、MANGO MOGGER）的具体内容
- [RANKED] place 的规则与入口；排行榜按什么排序
- Admin Abuse & Update 4 的具体内容
- 官方 Discord / Trello / YouTube（接口需登录）；兑换码
- 支持设备（需登录接口）
