# American Plains Mudding 待进游戏核实清单（2026-10-09）

## 草稿页

**本批没有 `draft: true` 的页。** 12 个文件里 9 篇文章 + 首页都有 S 级来源；所有无法从官方来源证实的细节都没有写进正文，页内用「not stated / our inference / check in game」标明。下面 A 表是已发布页里标了待核实的条目，B 表是因为没有一手来源而**没有建**的页（连草稿也没生成）。

## A. 已发布页里待进游戏核实的条目

| # | 页 | 页面现在怎么写的 | 进游戏要核实什么 | 核实后改哪里 |
|---|---|---|---|---|
| 1 | how-to-play、vehicles、community、index | 描述原话「Like 👍 and Favorite ⭐ the game to obtain a vehicle!」；写明没说是哪辆、怎么到手 | 点赞 + 收藏后送的是哪辆车（游戏内名称）；要不要重进；在哪个菜单出现 | how-to-play「How do you get the free vehicle?」；entities `free-vehicle-offer` |
| 2 | how-to-play、updates、index | 10/3 说明原话「Sitting In Vehicles Requires Being Whitelisted」；写明没说在哪设置 | 白名单在哪个菜单；是车主加人还是全服设置；对自己的车是否生效 | how-to-play「What changed for passengers…」；未确认表 |
| 3 | spawning、how-to-play、private-servers | 只写官方原话「4-8 slots owned」与「cap of 8 if 4 trailer and 4 vehicle spawner gamepasses are owned」；默认分配与单买一个生成通行证后的槽数写 not stated（round1 删除了首稿的默认分配推导） | 不买任何通行证时车辆 / 拖车各能生成几个；只买 4 Vehicle Spawner 或只买 4 Trailer Spawner 后各是几个 | spawning 第一张表补上两行实测值；tldr；entities `spawn-slots.unverified_fields` |
| 4 | spawning | 写明生成点位置、清车规则未公布 | 车辆 / 拖车在哪里生成（有无固定生成点）；离开或重置后已生成车辆怎么处理；限定车 / 隐藏车占不占槽 | spawning 末节清单 |
| 5 | private-servers | 只列通行证描述里的 3 条命令（`:weather storm 1`、`:fly user`、`:admin user`）；`:admin` 由谁执行写明未测试 | 命令在哪里输入；`:weather storm` 后面的 1–10 控制数量还是强度；`user` 填用户名还是显示名；不买通行证的私服有哪些命令；`:admin` 的有效期 | private-servers 各节；entities `private-server-commands` |
| 6 | private-servers、spawning | 「2x Spawn Slots In Private Servers, Up To 16, All Admins…」照抄；写明 games API 的 createVipServersAllowed 为 false、游戏内私服怎么创建未公布 | 私服是否免费 / 月费多少；翻倍需要房主还是每人自己有通行证 | private-servers「How much…」；spawning「How do slots work in private servers?」 |
| 7 | badges、index | 4 个 Hidden Vehicle + 1 个 Hidden Trailer 只给徽章数据，明说不提供位置 | 每个徽章对应哪辆车 / 哪个拖车（用徽章 ID 607498769738490 / 314947669947351 / 341545978270739 / 1514979861516315 / 3544618350782004 对号）；各自位置；找到后是否进生成列表；10/3 新森林后位置有没有变 | 核实后新建位置页（见 B 表第 2 行），badges 页保留数据口径 |
| 8 | badges、private-servers | Tornado Survivor 只引徽章描述；推断「普通游玩里也有龙卷风」并标明未确认 | 公共服是否自然出现龙卷风、多久一次；命令刷出的龙卷风给不给徽章；「survive」的判定 | badges「How do you get Tornado Survivor?」 |
| 9 | badges、community | Met a Staff Member 昨日 0 次；写明徽章描述没说哪些角色算 staff | 触发条件（同服即可还是要靠近）；哪些群组角色算 staff | badges「Can you still get Met a Staff Member?」 |
| 10 | gamepasses、vehicles | Premium Vehicles / Premium Trailers 只引「exclusive vehicles / trailers」与「subject to change over time」 | 两个通行证当前各含哪些车 / 拖车（游戏内名称，不对应真实车型） | gamepasses 表下说明；vehicles「How do you get more vehicles?」 |
| 11 | gamepasses | Premium Customization 只列描述里的 5 项功能 | 免费改装能改什么、通行证多出什么；10/3 新 ATV 的 Cargo Box / Windshield 附件要不要通行证 | gamepasses「What does Premium Customization include?」 |
| 12 | gamepasses | 礼物商品同价；写明接口没说明怎么选收礼人 | 游戏内赠送流程 | gamepasses「Are the gift versions cheaper?」 |
| 13 | limited-vehicles | 5 个节日通行证 10-09 全部未在售、无价格；3 个礼物商品接口标记在售（145 / 125 / 110）；「2026 是否返场」写明开发者没说 | 10-24、10-31 前后游戏内商店是否上架 Limited Halloween Vehicle、价格多少、是哪辆车；淡季游戏内能不能买那 3 个礼物商品；2023 Halloween Vehicle 是否还卖 | limited-vehicles 全页；entities 5 个 `pass-limited-*` 与 3 个 `product-gift-limited-*` |
| 14 | vehicles、how-to-play | 只列官方文本点过名的类型；写明没有车名、车价、性能、解锁条件，也不确定有没有游戏币 | 游戏内有没有货币；普通车是免费生成还是要解锁；车辆 / 拖车完整清单（游戏内名称） | vehicles；之后可按 Roblox 游戏内名称拆车辆表 |
| 15 | updates、index、guides | 下一条 listing「APM Map Update 🗺️」2026-10-10 14:00 UTC；写明 listing 是日程不是上线记录；「Part 1 of 2」与下一条标题的对应关系写明开发者没确认 | 10-10 之后：描述里的新更新说明、游戏名前缀、是否就是 Map Update Part 2 | updates 三张表 + index 两节 + gameVersion（接口可核，不必进游戏） |
| 16 | community | 写明 Roblox 匿名读不到社交链接（接口 401），无法确认官方 Discord | 用已验证 16+ 的 Roblox 账号打开游戏页，看社交链接里有没有 Discord、指向哪里 | community「Is there an official Discord server?」；届时来源是 Roblox 游戏页本身 |
| 17 | how-to-play | 只提到 2025-11 的 listing 写过「console controls」 | PC / 手机 / 手柄键位；拖车怎么挂（下拉词 how to connect trailer） | 之后可建 controls 页（B 表第 4 行） |

## B. 因为没有一手来源而没有建的页

| # | 没建的页 | 有无搜索需求（Google 下拉） | 进游戏要拿到什么才能建 |
|---|---|---|---|
| 1 | codes | 有（codes / roblox codes） | 不靠进游戏：要等官方描述 / 群组 shout 出现码。游戏内若有兑换入口，截图记下入口位置，页面仍只收官方来源的码 |
| 2 | hidden-vehicle-locations | 有（头部词，10 条以上变体） | 4 辆隐藏车 + 1 个隐藏拖车的位置截图、对应徽章 ID、取得方式 |
| 3 | commands（完整命令表） | 有（commands list / admin commands / advanced commands） | 私服里实测可用命令清单与语法；公共服有无命令 |
| 4 | controls | 有（controls / controls pc / convertible top / how to connect trailer） | 各平台键位表、挂拖车与开合车顶的操作 |
| 5 | map | 有（map / map roblox） | 地图地点名称与用途、10/3 新森林的位置；10-10 Map Update 之后再截 |
| 6 | money / 车价表 | 下拉未见 money 词 | 先确认游戏内有没有货币 |

## C. 不用进游戏、按日期重读接口的动作

| 日期 | 动作 | 涉及文件 |
|---|---|---|
| 2026-10-10 14:00 UTC 之后 | 重读 games（描述、name 前缀）与 virtual-events；更新说明换新后改 index / updates / how-to-play 相关节与全部页的 gameVersion | index、updates、how-to-play、guides、entities（`update-2026-10-03`、`update-schedule`） |
| 每周六 listing 开始后 | events 新增一条 → updates 两张表追加；若标题 / 描述点了新车型 → vehicles 表追加 | updates、vehicles、entities |
| 2026-10-24、10-31、11-27、12-25 前后 | 重读 game-passes：节日通行证 isForSale / price 有变化就写进 limited-vehicles | limited-vehicles、gamepasses、entities |
| 2026-10-25（英国）/ 11-01（美国）换冬令时后 | 核对 listing 开始时刻是否移到约 14:35 UTC；改 updates 的换算表 | updates |
| 每次复核 | 重取快照数字（在线、访问、收藏、赞踩、群成员、徽章累计、RSVP）并同步页内时刻；重读 8 个在售通行证价格（Premium Customization 描述写明会涨价） | index、community、badges、gamepasses、spawning、private-servers |
| 每 60 天 | 重跑 thumbnails 接口刷新 `180DAY-` URL 并逐个验 200（`scripts/make_images.py`） | _images.json、config card.img |
