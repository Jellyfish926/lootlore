# Bongo Cat 事实底稿（dossier）

- 游戏：Bongo Cat，Steam appid 3419430，开发/发行 Irox Games
- 取证日期：2026-09-29（全部 URL 当天实测 200，除「未获取」节所列）
- 等级：S = 一手官方（商店页/官方公告/开发者本人帖/Steam 官方 API）；A = 平台一手（Steam 讨论区玩家帖、社区指南、Steam 市场、SteamDB）；B = 社区 wiki/视频；C = 二手 SEO 站（只交叉验证）
- 公告链接统一格式：`N(gid)` = `https://store.steampowered.com/news/app/3419430/view/<gid>`（全部 66 条公告已逐字读完，原文存 raw/news.txt）
- 原始抓取物：`raw/`（appdetails.json、news.json/news.txt、thr/*.html 讨论帖、dlc/*.json、img/*.jpg）

## 1. 基本信息

| # | 事实 | 来源 | 级 |
|---|---|---|---|
| F01 | 名称 Bongo Cat；type=game；免费（is_free=true） | https://store.steampowered.com/api/appdetails?appids=3419430&l=english&cc=us | S |
| F02 | 开发商、发行商均为 Irox Games | 同上 | S |
| F03 | 发售日 Mar 5, 2025 | 同上；公告 N(1792751526108641) 写「March 5, 9:00AM CET」 | S |
| F04 | genres：Casual, Indie, Massively Multiplayer, Simulation, Free To Play | appdetails | S |
| F05 | categories：Single-player, Multi-player, Co-op, Online Co-op, Steam Achievements, Partial Controller Support, Stats, Family Sharing 等 | appdetails | S |
| F06 | 平台：windows=true, mac=true, linux=false | appdetails | S |
| F07 | 商店简介原文：「Bongo cat needs your help. Bongo cat needz more hatz!!! Every time you press a key, Bongo cat will punch your taskbar. Type, click, play, work to collect more points. Which hats will you find?」 | appdetails short_description | S |
| F08 | 掉落池概率（商店页原文）：Common 90% / Uncommon 9.5% / Rare 0.49% / Epic 0.01% / Legendary 1 in 500000，注「*Subject to change」 | appdetails detailed_description；https://store.steampowered.com/app/3419430/Bongo_Cat/ | S |
| F09 | 「Based on the artwork and meme of @StrayRogue」 | appdetails detailed_description | S |
| F10 | 最低配置：64 位、Windows 10/11、1 GB RAM、Graphics: Any、需宽带、100 MB 存储 | appdetails pc_requirements | S |
| F11 | 支持 24 种界面语言（appdetails 列表计数）；首发公告写「25 languages」 | appdetails supported_languages；N(1793384379332669) | S（见矛盾 C1） |
| F12 | Steam 成就总数 28 | appdetails achievements.total；https://steamcommunity.com/stats/3419430/achievements/ | S |
| F13 | 官方 Steam 截图 5 张（screenshots[]），无网站字段（website=null） | appdetails | S |
| F14 | bongo.cat 不是游戏官网：页面署名「Art courtesy of @StrayRogue / Meme by @DitzyFlama / Website by Eric Huber」，是原网页版打鼓 meme 站 | https://bongo.cat/ | S（页面自述） |
| F15 | 一周年公告：「5.8 million players downloaded Bongo Cat」 | N(1826362059921578)（2026-03-05） | S |
| F16 | 开发者 Steam 名「Spiced Pigeon」（讨论区 [developer] 徽章），公告署名 Marcel；团队成员提及 Lars（UI、联合创始人）、Flores（美术）、Iris（2025-10 加入）、Flo | 讨论区帖；N(1818752592137196)、N(1821922921810120)、N(1840310314350721) | S |
| F17 | 联系邮箱 contact@irox-games.com；Discord 用户名 spicedpigeon | N(1799088287868198)；N(1815034432865853) | S |

## 2. 核心玩法：敲击、宝箱、兑换

| # | 事实 | 来源 | 级 |
|---|---|---|---|
| G01 | 每按一次键 / 点一次鼠标，猫拍一下任务栏，计数累积 | F07 | S |
| G02 | 掉落计时器在 Demo 更新里改为 30 分钟（「Increase the drop timer to 30min」） | N(1792116353300258)（2025-02-23） | S |
| G03 | 只有攒够 1000 次点击才弹出宝箱（「only shows chest popup if you have 1000 clicks」） | N(1794102528240823)（2025-03-18） | S |
| G04 | 开箱会扣点击数：「When buying a chest a popup now displays the number of taps subtracted」；可关闭「-1000」数字显示 | N(1797185861746045)、N(1799088287826807) | S |
| G05 | 开发者回帖：「typing 1000 letters in 30min should be possible :P no need for clickers」 | https://steamcommunity.com/app/3419430/discussions/0/597395881634853843/ | S（开发者本人） |
| G06 | 兑换（exchange）：同稀有度 10 件升 1 件更高一档（「10 items of the same rarity can be upgraded to one of a higher tier」） | N(1792116353300258) | S；C 级 gamerant 一致 |
| G07 | 自动放入全部重复物品、提示重复够兑换；收藏（favorite）物品在自动兑换中被忽略；Shift+Click 一次兑换 1000+ | N(1795283637857596)、N(1797185861746045)、N(1800357164536345) | S |
| G08 | 2025-05-09 修复「快速兑换时会把非重复物品也换掉」的 bug | N(1799088287868198) | S |
| G09 | 游戏模式（gaming mode）：宝箱就绪前猫不可交互，F4 退出 | N(1793384379535358)；FAQ 帖 | S |
| G10 | 表情（emoji）有独立的第二个宝箱，只含表情；表情兑换在表情之间升级 | N(1811772772604122)、N(1813041031167641) | S |
| G11 | 可以给好友开宝箱：花你 1000 clicks，对好友免费；表情宝箱同理（双方都需更新） | N(1836506165556399)、N(1837955055360738) | S |
| G12 | 新增「unique」稀有度：不可掉落，只能通过特殊活动（如降临节日历）领取 | N(1842212951313382)（2026-09-01） | S |
| G13 | 重置当前敲击不会重置成就；设置里可看终身总敲击 | N(1795283637857596) | S |
| G14 | Steam 显示你「离开（away）」时会干扰掉落（红叉问题），2025-03-18 称已修复 | N(1793384379535358)、N(1794102528240823) | S |

## 3. 物品获取渠道

| # | 渠道 | 事实 | 来源 | 级 |
|---|---|---|---|---|
| I01 | 宝箱掉落 | 按 F08 概率从掉落池出皮肤/帽子 | F08 | S |
| I02 | 兑换 | G06 | — | S |
| I03 | 限时活动 | 活动期间可掉 20 件活动限定物品，结束后不再掉落（见第 5 节活动表） | 各活动公告 | S |
| I04 | 支持者物品（Item Store / DLC） | Item Store 在售：Paw Pass Token $4.99；Bumble Kitten、Meowxolotl、Sea Purrtle、Migrating Currents、Pollinating Breeze、Regenerating Bloom、Wrestler Cutie Punch、Yin、Yang、Appreciation、Spooky Skeleton、Hades 等均 $2.50（2026-09-29 美区页面） | https://store.steampowered.com/itemstore/3419430/ | S |
| I05 | Item Store 物品不可上市场 | 「Made the item store items non marketable (never intended to do so) -> JUST THESE ONES」 | N(1799088287826807) | S |
| I06 | DLC 包（2026-04-13 起把原支持者包做成独立 DLC） | God Pack（Zeus/Poseidon/Hades）、Mecha Pack（S.L.A.S.H./P.U.R.R/B.O.N.K.）、Squirrel Pack、Wrestler Pack（Six Seven Lives/Cutie Punch/Ribbit Rampage）发售日 Apr 13, 2026；Wild Wonders（Bumble Kitten/Meowxolotl/Sea Purrtle）Jun 27, 2026 | dlc appdetails：https://store.steampowered.com/app/3929900/ 、/4600310/、/4600320/、/4600330/、/4856340/；N(1829528821315214) | S |
| I07 | Paw Pass（2026-09-01 起） | 每月主题（首月 Circus）；免费+付费两条线，各 100 Bongo Coins；500 coins 可换付费线或支持者物品；奖励永久可领、无截止；每月至少打开一次游戏自动领免费票；领奖不消耗 taps；离线不能领奖但进度照算；可通过 Steam 交易赠送票 | N(1842212951313382) | S |
| I08 | 成就奖励物品 | 一周年：新的敲击数成就会给新皮肤和帽子（「Not all achievements will give you new cosmetics, but the new tap amount ones will」） | N(1826362059921578) | S |
| I09 | 100 万点击特别皮肤+帽子 | 「a special skin and hat for everyone who reaches 1 million clicks (this was edited back down from 5M)」 | N(1823825466497567)（2026-02-05） | S |
| I10 | 联动/合作赠品 | OKU、Let Them Trade、Paddle³、4 个 Indie Demo、Tap Tap Loot（买游戏送 Goo Cat/Jester Hat/Bunny Ears/Bunny Skin）、Typing Farmer（Angry Tomato Stray Hat、Pig Skin）、Nightwater（2026-09-18：Nightwater Skin/Backpack、Wooden Nightwater Cat、Wooden Nightwater Stick） | 对应公告 | S |
| I11 | 「试玩换物品」类激励已下线 | 2026-06-27：因违反 Steam 准则，停用激励奖励（如 wishlist 奖励），改为拥有完整游戏或移除 | N(1836506165556399) | S |
| I12 | 多人专属水果套装 | 多人会话（至少 1 名其他玩家）中弹窗选 Strawberry / Pineapple / Watermelon 队，只能拿一套 | N(1807332909696878) | S |
| I13 | Demo 专属 | 玩 Demo ≥30 分钟可得两件 Demo 专属 legendary 帽子；Demo 物品不带入正式版 | N(1792751526108641)、N(1793384379332669) | S |
| I14 | 删除物品 | 设置里可删除物品，不可恢复 | N(1807332909696878) | S |
| I15 | 点数商店 | ILoyaltyRewardsService/QueryRewardItems appids=3419430 返回 total_count 0（无点数商店物品）；一周年公告称 Steam Point Shop 在计划中 | https://api.steampowered.com/ILoyaltyRewardsService/QueryRewardItems/v1/?appids%5B0%5D=3419430；N(1826362059921578) | S |

## 4. 交易与市场

| # | 事实 | 来源 | 级 |
|---|---|---|---|
| T01 | 正式版起掉落的物品可在 Steam 市场交易、也可好友间交易 | N(1793384379332669)（2025-03-05） | S |
| T02 | 2025-03-11 移除玩家间交易（市场仍可用），原因：机器人账号刷物品集中抛售 | N(1793384379535358) | S |
| T03 | 2025-11-10 重新开放全部物品的好友交易 | N(1815580768395840) | S |
| T04 | Item Store 物品不可上市场（I05） | — | S |
| T05 | 2026-09-29 市场搜索 total_count=540 个挂单物品种类 | https://steamcommunity.com/market/search/render/?appid=3419430&norender=1 | A |
| T06 | 市场价格波动大（当日样本最高挂价 Silly Post It $255.65）——只作说明，不进正文价格表 | 同上 | A |
| T07 | 玩家帖观点：开发者从市场交易抽成——**未核实**（非开发者说法） | https://steamcommunity.com/app/3419430/discussions/0/500576094581177001/ | A（未核实，不写） |

## 5. 限时活动时间线（全部 S，来自公告）

| 活动 | 开始公告日 | 结束/截止 | 要点 | gid |
|---|---|---|---|---|
| April Event（500k 玩家庆祝） | 2025-03-31 | 2025-04-22 | 20 件 April Fools' 物品，每稀有度 4 件 | 1795283637960385 |
| Summer Sale & Event | 2025-06-27 | 2025-07-18 | 20 件夏季物品，每稀有度 4 件；商店 8 折 | 1803527891535449 |
| Autumn Event | 2025-10-08 | 2025-10-31 | 20 件；活动物品掉率显著提高（总体稀有度概率不变） | 1813041031167641 |
| Free Halloween Treat | 2025-10-30 | 2025-11-05 | 三选一：Zombie / Nosfergato / Frankittystein | 1815034432865853 |
| Animal Shelter 慈善 | 2025-11-10 | 2025-11-17 | Luna 免费，另 5 只付费，净收入捐慕尼黑动物收容所；最终捐 15.000€ | 1815580768395840、1818752592137196 |
| Winter Event & Advent Calendar | 2025-12-01 | 2025-12-31 | 20 件冬季物品；免费降临日历 12-01 至 12-25 每天 8am GMT 开门；Deluxe Calendar 25 件付费 | 1817483467044521 |
| Steam Typing Fest | 2026-02-05 | 未写明 | 免费 Ranged Mecha L.A.S.E.R.；100 万点击特别皮肤+帽子 | 1823825466497567 |
| Year of the Horse / Lunar New Year | 2026-02-16 | 2026-03-16 | 20 件；红包日历 02-16 至 03-01 每天 8pm CET；Deluxe 14 件付费 | 1824644522846187 |
| Bongo Royale（愚人节） | 2026-04-01 | 3 天 | 多人大厅变打字大逃杀，随机大厅最多 250 人；参与者得特别皮肤；结束后补发 Blood Splatter Skin 2 天 | 1828894815553998 |
| Summer Event 2026 | 2026-06-16 | 2026-07-14 | 20 件夏季物品 | 1835236783574334 |
| Paw Pass: Circus | 2026-09-01 | 奖励无截止 | 首个月度通行证 | 1842212951313382 |

## 6. 多人（Meowtiplayer）

| # | 事实 | 来源 | 级 |
|---|---|---|---|
| M01 | 2025-08-11 上线，最多 100 位好友同屏；全部走 Steam，无需自建服务器 | N(1807332909696878) | S |
| M02 | 大厅代码去掉 l / I / O，旧代码作废（2025-08-27） | N(1809235871549290) | S |
| M03 | 私人大厅（仅 Steam 邀请）2026-01-14；三种状态 Friends/Lobby Code、Invite only、Public；「join random lobby」 | N(1821922921810120)、N(1829528821315214) | S |
| M04 | 聊天（不做审核，可关闭）2026-04-13；语言过滤 2026-04-20，2026-06-27 起可本地关闭 | N(1829528821315214)、N(1830163047265223)、N(1836506165556399) | S |
| M05 | Discord SDK：可经 Discord 加入大厅，设置可关 | N(1830163047257430)、N(1830163047265223) | S |
| M06 | AFK 提示：2 分钟无操作显示 | N(1830163047257430) | S |
| M07 | 大厅名称与大厅浏览器 2026-06-05；持久大厅代码 2026-06-16 | N(1834602721190507)、N(1835236783574334) | S |
| M08 | 摸头（Pat）2026-07-12；多人布局 8 种 pattern、F6 预览槽位 2026-08-10 | N(1837955055360738)、N(1840310314350721) | S |
| M09 | 表情：多人大厅中悬停猫使用；静音其他玩家 | N(1811772772443374) | S |

## 7. 安全 / 键盘记录疑问（只收开发者或官方说法）

| # | 事实（原话要点） | 来源 | 级 |
|---|---|---|---|
| S01 | 「i just count how many keys are pressed i don't process them any further」「the game doesn't require any internet connection to work i just send stuff to the steam client (for the items to drop)」（2025-03） | https://steamcommunity.com/app/3419430/discussions/0/595142635298013586/ | S（开发者本人） |
| S02 | 「i ship the .pdb files so you can take a look what the code does」；代码未混淆，可用 dnSpy 等查看；不请求网络访问权限 | https://steamcommunity.com/app/3419430/discussions/0/597398346071595150/ ；/597399326497452033/ | S（开发者本人） |
| S03 | 「no there is no malicious code but yes let others verify it for you..」 | https://steamcommunity.com/app/3419430/discussions/0/500576094581177001/ | S（开发者本人） |
| S04 | CS2：「nope, but cs2 will kick you out of the ranked lobby if you have it over the same window ... but no bans tho」（2025-04-24 问 VAC） | https://steamcommunity.com/app/3419430/discussions/0/597398871354738307/ | S（开发者本人，仅代表开发者说法，非 Valve） |
| S05 | 2025-10-30 起加入 Steam Stats 分析，「fully anonymized」 | N(1815034432865853) | S |
| S06 | 注意：2025 年「不需要联网」的说法之后，游戏已加入多人、聊天、Discord SDK、Paw Pass（离线不能领奖）等联网功能 | M01/M04/M05/I07 | S（我方据公告并列陈述，不下结论） |
| S07 | Admin Mode 为可选（opt-in），用于部分游戏里点击不被记录；关闭方法：Steam 库→管理→浏览本地文件→BongoCat.exe 属性→兼容性→取消「以管理员身份运行」 | N(1793384379535358)、N(1794102528240823) | S |
| S08 | 自动连点器：**未找到开发者或官方的允许/禁止/封号说法**；开发者只说过「no need for clickers」（G05）。官方与 The Farmer Was Replaced 联动的「The Typer Was Replaced」可用 `tap()` 自动化（需拥有该游戏） | 搜索讨论区 auto clicker/ban/macro 共 25 帖无开发者回帖；N(1830163047257430) | S / 未获取官方政策 |
| S09 | 5M 敲击 Steam 成就因玩家反对被移除，计划改为游戏内成就 | https://steamcommunity.com/app/3419430/discussions/0/785451333487492012/ | S（开发者本人） |

## 8. Steam Error 与常见故障（官方给出的处理）

| # | 问题 | 官方说法/处理 | 来源 | 级 |
|---|---|---|---|---|
| E01 | Steam Error（2025-05） | 「Fixes the steam error issue because items can now stack. You might need to keep Bongo Cat running for 30min」 | N(1799088287821846) | S |
| E02 | Steam Error 弹窗（2026-02-28 开发者置顶） | Steam API 大量返回 failed，但物品照常掉落/兑换照常完成；关掉弹窗，到 Steam 库存 → Inventory History 查是否真的掉了；03-09 Valve 已介入 | https://steamcommunity.com/app/3419430/discussions/0/766312101614459106/ | S |
| E03 | 计时器与 Steam 不同步 | 「restart steam, start bongo cat, wait 30min without opening a chest」 | https://steamcommunity.com/app/3419430/discussions/0/597402042488586436/ | S（开发者回帖） |
| E04 | 2025-10-02 大量 Steam Error | Valve 修复后端 | N(1811772772484130) | S |
| E05 | 黑色背景不透明 | F3 或设置里开「Transparency Fix」 | N(1807966710813696)；FAQ 帖 | S |
| E06 | 看不到猫 | 打开游戏后立刻按 F8（不点击别处）；F8 切换显示器 | N(1807966710813696)、N(1807332909696878) | S |
| E07 | 菜单/猫跑出屏幕、缩放过大 | 点一下猫后按 F1 复位 | FAQ 帖 https://steamcommunity.com/app/3419430/discussions/0/599643530220034451/ | S |
| E08 | 隐藏计数 | F2 | FAQ 帖 | S |
| E09 | 卡在 gaming mode | Alt+Tab 聚焦后按 F4，或重启（计时器会重置） | FAQ 帖 | S |
| E10 | 手柄不生效 | 设置开启手柄支持；仍不行则禁用 Steam Input（库中手柄图标或 属性→Controller） | https://steamcommunity.com/app/3419430/discussions/0/603024565119004311/ | S |
| E11 | Mac 点击不计数 | 系统设置→隐私与安全→输入监控，给 Steam 和 Bongo Cat 授权 | https://steamcommunity.com/app/3419430/discussions/0/806846367620396268/ | S |
| E12 | Linux | 测试分支 beta code `linuxtesting`，只支持 X11；Wayland 可能不支持 | https://steamcommunity.com/app/3419430/discussions/0/573792389464878955/；N(1834602721190507) | S |
| E13 | 其他快捷键 | F12 picture mode（2025-03-28，2025-04-20 起存到 Steam 截图）；F 翻转；R 旋转（2026-03-23）；Esc / M / 中键开背包（2026-08-10） | 对应公告 | S |
| E14 | 旧物品白图 | 「Update and Restart」按钮在设置里 | N(1805431065363156) | S |
| E15 | Steam Cloud 只存装备的帽子（2025-05-26 准备移除） | N(1800357164536345) | S |

## 9. 成就（28 个，2026-09-29 抓取，全球解锁率）

数据文件：`achievements.json`（fetch_achievements.py 格式，源 https://steamcommunity.com/stats/3419430/achievements/）。要点：
- 最容易：Bongo Beat 1（90.8%）；最难：Bongo Beat Diamond「25.000.000 bongo beats. You did it.」（0.4%）
- 同名分级：Item Collector ×4（5/20/100/1.000 items）、Emoter ×3 + Sparkly Emoter、Meowtiplayer Friend/Group/Pack/Party（2/5/10/50 人大厅）、Trader/Vendor/Merchant（交换 1/10/100 次）
- 描述里的数字用欧式千分位「1.000.000」——正文照抄原文写法并在表外注释

## 10. 互相矛盾

| # | 点 | 说法 A | 说法 B | 处理 |
|---|---|---|---|---|
| C1 | 语言数 | appdetails 列 24 种 | 首发公告「25 languages」 | 正文写「24 languages listed on the store page」 |
| C2 | 平台 | appdetails mac=true / linux=false | 2026-03-23 公告称 Mac 为「experimental」；Linux 走 beta 分支 | 正文写商店标注 + 实验/测试状态 |
| C3 | 峰值在线 | SteamDB 新闻源条目（发布于 2025-03-29）写「peaked at 194,508 ... on 4 May 2025」 | 发布日期早于所述峰值日期（条目内容被动态更新） | 不写具体峰值 |
| C4 | 是否需联网 | 开发者 2025 年：「doesn't require any internet connection」 | 2025-08 后多人/聊天/Discord/Paw Pass 需要联网 | is-it-safe 页两者并列，注明时间 |
| C5 | Paw Pass 解锁节奏 | fandom（B）：「every 5k taps/clicks unlocks an item」 | 官方公告只写「reaching its milestones」 | 不写 5k |
| C6 | 5M 成就 | 2026-02-05 公告：100 万点击奖励「edited back down from 5M」 | 2026-02-17 开发者帖：5M 成就移除 | 两者不冲突，都写，注日期 |

## 11. 未核实（不进正文或只以「未核实」出现）

- 当前版本的宝箱计时器是否仍是 30 分钟（最新一手出处为 2025-02 Demo 公告与 2025 开发者回帖；2026 年 UI 重做后未再公告）——正文写「per the developer's 2025 notes」
- 开箱是否仍固定扣 1000 taps（2026 公告里「open friends' chests costs 1000 clicks」间接支持）
- Paw Pass 每个里程碑的具体 taps 数（C5）
- 各帽子/皮肤的单件稀有度：Steam 物品定义 API（IInventoryService/GetItemDefMeta）需 key，返回 403，未获取；bongocat.org（C）有 223 件列表，但 C 级不可作唯一来源 → 首批不做单件稀有度表
- 自动连点器是否会被封号：无官方说法（S08）
- 用户给的「在线约 16 万」：本轮未获取一手当前在线数（SteamDB 未抓，steamcharts 未抓），正文不写
- 市场抽成比例：未获取一手说法

## 12. 未获取（原因）

| 目标 | 结果 |
|---|---|
| bongocatdb.vercel.app | HTTP 429「Vercel Security Checkpoint」，未绕行 |
| steamhunters.com/apps/3419430 | HTTP 403 |
| SteamDB | 未抓取（按规则被挡记未获取；仅用 Steam 新闻源里的 SteamDB 条目，且判为矛盾不用） |
| Steam 点数商店页 store.steampowered.com/points/shop/app/3419430 | 页面为 JS 渲染，HTML 中无游戏内容；改用官方 API 得 0 件 |
| Steam 物品定义（稀有度/物品全表） | GetItemDefMeta 需 API key → 403 |
| 市场单品页的物品标签 | listings 页 HTML 无 g_rgAssets，未取到稀有度标签 |
| Steam 社区指南正文 | 仅取标题清单（10 篇），均为玩家工具/个人向，未用作事实来源 |
| YouTube 视频 | 本轮未检索（无可验证的一手视频可嵌） |
| gamerant 原猜测 URL /bongo-cat-guide/ | 404；改取站内搜索得到的 /bongo-cat-how-get-epic-legendary-items-hats-fast/（C 级，仅交叉验证兑换 10→1 与 30 分钟） |
