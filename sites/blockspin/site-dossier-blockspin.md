# BlockSpin 事实底稿（dossier）

取证日期：2026-09-29（北京时间）。原始抓取文件在 `raw/`。
来源等级：S = 官方（Roblox 官方 API 返回的开发者自填信息、开发商官网）；A = 平台一手（开发者本人在 Roblox DevForum 的帖子、官方群组成员身份可在 Roblox API 验证）；B = 社区维护（Fandom、YouTube 视频标题）；C = 二手 SEO 站（只作线索/交叉）。

结论：S/A 级能撑住的只有「游戏基本信息 + 官方兑换码 1 个 + 死亡掉落与房屋保险箱 + 平台/分级 + 官方封禁申诉游戏」。职业/工作清单、地图地点、武器、载具、数值一律只有 B/C，全部进「未核实」。

## 一、游戏基本信息

| # | 事实 | 值 | 来源 | 级 |
|---|---|---|---|---|
| F01 | 游戏名（Roblox 当前标题） | `BlockSpin 🔪 [WEATHER]`（方括号是更新标签，会随更新变；正文统一写 BlockSpin） | https://games.roblox.com/v1/games?universeIds=6765805766 | S |
| F02 | universeId / rootPlaceId | 6765805766 / 104715542330896 | 同上 | S |
| F03 | 创作者 | 群组 Cinnamon Go!（groupId 33720745，已认证蓝标） | 同上 `creator` | S |
| F04 | 群组归属 | 群组描述：「Action and Adventure games. Owned and Managed by Cinnamon Software.」；群主 CinnamonSoftware（userId 4883001638）；成员 398,854 | https://groups.roblox.com/v1/groups/33720745 | S |
| F05 | 开发商 | Cinnamon Software，自述为独立 Roblox 工作室，作品 LifeTogether、BlockSpin、BayView；两位总监 Rhyles、ArraySegment | https://devforum.roblox.com/t/4777100 （2026-08-05，开发商招聘帖） | A |
| F06 | 开发商官网对 BlockSpin 的一句话 | 「Enter the city, grind jobs, fight for dominance.」 | https://www.cinnamon.co.uk/ | S |
| F07 | 开发商官网品牌页数据 | BlockSpin「Fast-paced competitive gameplay」，Total Plays 1.0B+，Peak CCU 50K+，MAU 3.4M+（页面未标日期） | https://www.cinnamon.co.uk/brands | S |
| F08 | 创建日期 | 2024-11-06T14:19:35Z | games API `created` | S |
| F09 | 最近更新 | 2026-09-19T00:32:58Z | games API `updated` | S |
| F10 | 类型 | genre_l1 Action / genre_l2 Open World Action | games API | S |
| F11 | 每服最大人数 | 28 | games API `maxPlayers` | S |
| F12 | 访问量（2026-09-29 取） | 1,259,345,162 | games API `visits` | S |
| F13 | 收藏数（2026-09-29 取） | 985,284 | games API `favoritedCount` | S |
| F14 | 点赞/点踩（2026-09-29 取） | 275,155 / 75,148（好评率约 78.5%，推导） | https://games.roblox.com/v1/games/votes?universeIds=6765805766 | S |
| F15 | 在线（抓取瞬间） | 14,588（瞬时值，不写进正文） | games API `playing` | S |
| F16 | 私服 | `createVipServersAllowed: false`（API 返回不允许创建 VIP 私服） | games API | S |
| F17 | 内容分级 | Maturity: Moderate；描述项 Blood (Light/Realistic)、Violence (Repeated/Moderate) | https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation（POST universeId） | S |
| F18 | 设定地点 | 描述原话「Based in a Florida county.」 | games API `description` | S |
| F19 | 玩法循环（官方原话） | 「Spin the block. Grind your way through jobs to unbox random reward cases, and level up your character to become the top dog in the city.」「…becoming the most powerful gangster around. With intense battles, unforgettable finishers, and a world that reacts to your every move…」 | games API `description` | S |
| F20 | 死亡规则（官方原话） | 「You drop everything in your inventory on death, place items into the safe in your house to keep them secure.」 | games API `description` | S |
| F21 | 游戏主机平台 | 开发者 AVeryCanadianHolder（在 Cinnamon Go! 群组角色 = Developer，经 Roblox API 验证）2025-09-15 发帖称 BlockSpin 在 PlayStation 上崩溃增多、Xbox 无增加 → 游戏可在 PlayStation 与 Xbox 上玩（至少在 2025-09） | https://devforum.roblox.com/t/3936850 + https://groups.roblox.com/v1/users/648805907/groups/roles | A |
| F22 | 官方封禁申诉游戏 | 同群组发布「Ban Appeal Game」（universe 9710075439，2026-02-11 创建），描述原话「Banned on BlockSpin? … Join. Pay. Get instantly unbanned.」 | https://games.roblox.com/v2/groups/33720745/games?accessFilter=Public&limit=50 | S |
| F23 | 官方社媒 | 开发商官网链接：Discord https://discord.gg/ATp5Kn2zhu 、X https://x.com/CinnamonRoblox 、Roblox 社区 16007265 Cinnamon Software（成员 1,393,970） | https://www.cinnamon.co.uk/ + https://groups.roblox.com/v1/groups/16007265 | S |
| F24 | BlockSpin 专属 Discord | 服务器「BlockSpin 🧨」id 1337420081382297682 存在（widget 可读，频道/消息不可读） | https://discord.com/api/guilds/1337420081382297682/widget.json | B（能证明存在，不能证明是官方链接） |
| F25 | 游戏通行证 | 公开 API 返回 0 个 game pass | https://apis.roblox.com/game-passes/v1/universes/6765805766/game-passes?passView=Full&pageSize=100 | S（但「0 个」按规格不写进正文） |
| F26 | 徽章 | 公开 API 返回 0 个 badge | https://badges.roblox.com/v1/universes/6765805766/badges?limit=100 | S（同上不写） |
| F27 | 官方虚拟活动 | 0 条 | https://apis.roblox.com/virtual-events/v1/universes/6765805766/virtual-events | S（不写） |

## 二、兑换码

| # | 码 | 奖励 | 状态 | 来源 | 级 |
|---|---|---|---|---|---|
| K01 | `W7C28D` | $500 游戏内现金，限新玩家 | 2026-09-29 仍在官方描述中 → active | 游戏描述原话「Use code W7C28D for $500 free cash if you're a new player!」 https://games.roblox.com/v1/games?universeIds=6765805766 | S |

交叉（C，只作线索，不上页）：
- Pocket Gamer（2026-09-26 更新）列 active：HURRICANE_RELEASE、2UFU96、7AVJ0M、W7C28D、M16_RELEASE、UNDER_THE_BARREL、BLOCKSPIN_GRIPS_UPDATE + 14 个「referral codes」；expired：BLOCKSPIN_FISHING、EVERYTHING_10、UPDATEOMEGA、EVERYTHING_CRATE、30K_CCU。https://www.pocketgamer.com/roblox/blockspin-codes/
- Roblox Den（2026-09-26 检查）：5 active（W7C28D active；7AVJ0M/1X21TB/PN8984/VX49HE 为 Check）、159 expired，HURRICANE_RELEASE、M16_RELEASE、UNDER_THE_BARREL、BLOCKSPIN_GRIPS_UPDATE 标 expired。https://robloxden.com/game-codes/blockspin
- Pocket Tactics（2026-06-19 更新）：码都是 referral 码、每号只能兑换一个、兑换入口在屏幕右侧图标 → codes 按钮。https://www.pockettactics.com/blockspin-codes
- 兑换步骤（右侧菜单 → Codes 标签 → 输入 → Redeem）三家 C 站一致，但无 S/A 来源 → 页面上只写「在游戏内的兑换码输入框」，并标注未一手核实。

## 三、官方素材（图片）

| key | 画面（本人看图写） | URL（768×432） | 级 |
|---|---|---|---|
| th1 | BlockSpin 标志 + 一辆蓝色超跑在夜间街道漂移，火花四溅 | https://tr.rbxcdn.com/180DAY-faec41dafa29c7f849b7cc61a6dc6759/768/432/Image/Png/noFilter | S |
| th2 | 戴绿色头巾的角色坐在草坪椅上钓鱼，钓起一条黄色大鱼，背景是平房和棕榈树，画面文字「FISHING」 | …fb5203b9ee151dc1186e15488ac8f48f… | S |
| th3 | 两名蒙面角色在「Quick-11」便利店抢劫，一人持枪，一人往黑色旅行袋里装现金，店员举手 | …a29dc9289b3e87a61d957d8d4211c98c… | S |
| th4 | 快餐店内，持枪蒙面角色与拿拖把拖地、身穿黄色围裙的店员，旁有「CAUTION WET FLOOR」牌和薯条汉堡海报 | …74cbb089082a05ef336177e5b24dbb90… | S |
| icon | 戴金链的角色举枪指向镜头，背景棕榈树，BlockSpin 标志 | https://tr.rbxcdn.com/180DAY-3fa1cc9c917b841b5630adea21e87134/512/512/Image/Png/noFilter | S |

图片说明：四张都是官方宣传缩略图（插画风合成），不是实机截图，alt 里如实写「promotional thumbnail」。能从官方图里直接读出的事实：存在名为 Quick-11 的便利店、存在钓鱼玩法、存在快餐店场景、有抢劫/持枪题材。

## 四、B 级素材（社区）

| # | 内容 | 来源 | 状态 |
|---|---|---|---|
| B01 | Fandom robloxblockspin：主页仍是模板文字；仅 Cars、Weapons、Elite_Vehicle_Crate、F-150 等少量页；Cars 页列 Basic/Rare/Elite Case 三档载具掉率（2025-08-17 编辑）；Elite Case 在 Car Dealership 售 $16,500（2025-10-24 编辑） | https://robloxblockspin.fandom.com/rest.php/v1/page/Cars 、…/Elite_Vehicle_Crate | 过旧（>11 个月），且 api.php 返回 410，只能用 rest.php 读 |
| B02 | Fandom blockspin.fandom.com：只有 2 页模板主页，无内容 | https://blockspin.fandom.com/api.php?action=query&list=allpages | 无用 |
| B03 | YouTube 标题可见的玩法词：Hurricane（载具/物品，见多支视频）、M16（「0.42%」「legendary」）、Fishing update、Quantum hack tool / ATM routes、Drum Mag、car crates & wraps、legendary guns、stack servers | yt-dlp ytsearch（见 raw/ 与本节下方） | 只有标题，字幕被「Sign in to confirm you're not a bot」拦截，未获取 |

YouTube 可引视频（标题/频道/播放量，2026-09-29 取）：
- j1XWaZs3Bfk「The ULTIMATE Beginner's Guide To Roblox BlockSpin」2kane 37,113
- gBKaBC4rgF4「Can I Go From Noob to Pro in 60 Minutes? | Roblox Blockspin」ChrisOffScript 437,101
- 91UoIxMhSYE「Ultimate Blockspin Money Making Guide」Koko 213,607
- yNKl-TXbFCY「BEST WAYS TO MAKE MONEY IN BLOCKSPIN (RANKING EVERY JOB)」Novaa 18,080
- g4nvhoC1XGk「The Quantum Swiper's Guide To Blockspin: ATM Routes…」Koko 32,373
- MRO7ukcpsYM「This Fishing Update Is OP In Roblox BlockSpin」2kane 71,422
- 81xCncxi1W0「BLOCK SPIN - Melee Weapon Tier List」OppBunG 28,240

## 五、C 级线索（不上页，等一手确认）

| # | 线索 | 来源 |
|---|---|---|
| C01 | 三个「已确认」工作：Janitor @ Burger Place、Shelf Stocker @ Quick-11、Cook @ The Butcher's Cut；另有工作「在复核中」；钓鱼单列 | https://blockspintools.com/guides/jobs |
| C02 | 任务系统：侧栏 Quests，全部完成共得 $1,000、100 XP、6 Bottles、15 Bricks、5 Molotovs；「Work 3 Different Jobs」推荐 Burger Place、Quick 11、The Butcher's C… | https://blockspinvalues.com/quest-guide-i18n.js |
| C03 | 交易价值表分 Common/Uncommon、Rare、Epic、Legendary、Omega、Misc、Vehicles；「BlockSpin Plus」、现金税、重置时身上别超 60,000 现金 | https://blockspinvalues.com/ |
| C04 | 武器来源：Dumpsters、Weapon Crates、Airdrops | Fandom Weapons 页（B，2025-10-24）+ blockspintools 首页 Airdrops 条目（C） |
| C05 | 新号兑换码报错「Could not validate your account (Alt Account)」，玩 10-15 分钟后消失 | https://www.pocketgamer.com/roblox/blockspin-codes/ |
| C06 | Pocket Gamer：可抢其他玩家的现金和物品，兑换前靠近 ATM | 同上 |
| C07 | 物品/载具/装备清单（2025-03-26 版，已旧） | https://deltiasgaming.com/block-spin-roblox-item-guide-list-of-vehicles-weapons-and-equipment/ |

## 互相矛盾

| 事项 | 说法 A | 说法 B | 处理 |
|---|---|---|---|
| HURRICANE_RELEASE 等更新码状态 | Pocket Gamer 2026-09-26：active | Roblox Den 2026-09-26：expired | 两边都是 C，且无官方来源 → 整批不上页 |
| HURRICANE_RELEASE 奖励 | Pocket Tactics：500 cash referral | Roblox Den：「Free Rewards」 | 同上 |
| 总游玩量 | 开发商品牌页：1.0B+ | games API：1,259,345,162 | 不矛盾（品牌页是取整/未更新），正文用 API 值并注明取数日期 |
| 兑换数量 | Pocket Tactics：每号只能兑换一个（referral） | Pocket Gamer：普通码 + 一个 referral 码分两栏 | 无一手来源，正文只写官方原话「if you're a new player」 |

## 未核实（查不到就不写）

- 兑换码入口的具体 UI 位置（C×3 一致，无 S/A）
- 工作/职业清单、工资、等级机制（C 为主）
- 地图地点：Jack's Hardware Store 位置（Google 相关搜索里有需求，但所有来源都未见可核实描述）
- ATM「hack」机制、Quantum 工具（只有 YouTube 标题）
- 武器清单、稀有度、掉率；载具箱子掉率与价格（Fandom 2025 年数据，版本已过多次更新）
- 交易价值（blockspinvalues 为社区自定价，本质是意见）
- 手机端可玩性：Roblox 可玩设备字段需登录 API，未获取；Pocket Gamer 的 iOS/Android 标签是其站内分类，不作证据
- BlockSpin Plus 是什么（只见 C 站提到）
- 官方 X / Discord 公告内容（X robots 禁止、Discord 需登录，未获取）
