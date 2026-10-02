# 页面矩阵（+1 Stone Skipping，英文，首批 11 个文件 = 11 页发布，0 页 draft）

一个意图一页；同实体组收进同一页。路由沿用 mog-evolution / race-horses：`/<game-slug>/<slug>/`，首页 `/stone-skipping/`。

| # | URL | 页型 | 承接词 | 这一页要回答的问题 | 优先级 | 状态 | 到期动作 |
|---|---|---|---|---|---|---|---|
| 1 | /stone-skipping/ | home | +1 stone skipping, stone skipping roblox, +1 skipping stones | 这是什么游戏、谁做的、先看哪页 | P0 | 发布 | **2026-10-04**：改「What's happening this week?」一节、tldr 第 3 条、faq 第 5 条 |
| 2 | /stone-skipping/beginner/ | category（Getting Started） | guide, beginner | 新手按什么顺序看 | P0 | 发布 | 2026-10-04：首段里的活动日期句 |
| 3 | /stone-skipping/how-to-play/ | article | how to play, skill, zones, wins, rebirth, worlds | 官方六句各说了什么、没说什么；官方图显示什么 | P0 | 发布 | 2026-10-04：Worlds 一节 |
| 4 | /stone-skipping/updates/ | article | update, world 5, admin abuse | 活动当地几点开始；从官方时间戳看每次加了什么 | P0 | 发布 | **2026-10-04**：活动一节改过去时、重读 events 与两个商店接口、更新 tldr 与首段 |
| 5 | /stone-skipping/community/ | article | codes, discord, group | 查了哪些官方位置、为什么不列码、群组数据、私服、真假游戏 | P0 | 发布 | 2026-10-04：私服一节与「官方消息在哪」一节的活动句 |
| 6 | /stone-skipping/robux/ | category（Robux Shop） | robux, shop | 买之前看哪篇 | P0 | 发布 | — |
| 7 | /stone-skipping/gamepasses/ | article | gamepass, auto wins, auto rebirth, training zone | 11 个通行证的价格、单价、礼物版、同名异价 | P0 | 发布 | — |
| 8 | /stone-skipping/pets/ | article | eggs, pets, admin egg, dragon egg, king doggy | 六种蛋的价格与捆绑省多少；哪些包的图标是宠物；什么还不知道 | P0 | 发布 | — |
| 9 | /stone-skipping/boosts/ | article | skill multiplier, wins pack, 2x wins | Skill / Wins 加成的十档价格、pack 价格、「永久」是谁的承诺 | P1 | 发布 | — |
| 10 | /stone-skipping/shop/ | article | robux products, starter pack, gift | 78 个商品全表 + 分组 + 合计 | P0 | 发布 | — |
| 11 | /stone-skipping/author/ | author | — | 谁写的、怎么核实 | P0 | 发布 | — |
| — | /stone-skipping/codes/ | article | codes | 现在能用的码 | P0（阻塞） | 不建：无官方来源 | 官方发码当天新建 |
| — | /stone-skipping/zones/ | article | zones | zone 顺序、距离、Wins | P1 | 不建：需进游戏核实 | — |
| — | /stone-skipping/stones/ | article | stones, donut | 投掷物清单与价格 | P2 | 不建：需进游戏核实 | — |
| — | /stone-skipping/rebirth/ | article | rebirth | Rebirth 条件与奖励 | P2 | 不建：需进游戏核实 | — |
| — | /stone-skipping/worlds/ | article | world 2-5 | 各 World 的解锁条件 | P2 | 不建：只有 World 3 / 4 / 5 三场活动的标题与时间窗（S 级，已写进 updates 一节），解锁条件需进游戏核实；10-03 活动后先更新 updates 页 | — |

## 首页模块

| 模块 | 承接 | 写什么 | 链到 |
|---|---|---|---|
| 直答首段 | +1 stone skipping roblox | 一句话说清游戏、开发群组、核心循环 | how-to-play |
| Start here | beginner | 三篇入口 | how-to-play / gamepasses / shop |
| 速览表 | — | 开发者、创建日、类型、人数、价格、分级、徽章 / 通行证 / 商品数、两种官方写法 | — |
| 自动表：通行证 + 商品 | gamepass, robux products | entities gamepass 表（11 行）+ item 表（前 12 行） | gamepasses / shop |
| 本周活动 | admin abuse, world 5 | 活动时间窗 | updates |
| 为什么没有码页 | codes | 直说原因 | community |
| 来源说明 | — | 数据来自 Roblox 官方接口，快照日期 | author |

draft 页：无。11 页都有 S 级来源。拿不到一手来源的主题（码、zone、石头清单、宠物概率、Rebirth 数值、World 解锁）不建页，而不是建 draft —— 如果用 C 级线索先写 draft，正文就得引用专站内容，这一轮不做。
