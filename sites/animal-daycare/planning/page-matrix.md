# 页面矩阵（Animal Daycare (Anomaly)，英文，首批 9 个文件 = 7 页发布 + 2 页草稿）

一个意图一页；同实体组收进同一页。路由规则沿用 deep-fishing：`/<game-slug>/<slug>/`，首页 `/animal-daycare/`。
规模说明：机制「勉强过」、素材以官方接口为主，宁少勿凑——没有做 codes、classes、tier list、map、discord 页。

| # | URL | 页型 | 承接词 | 这一页要回答的问题 | 优先级 | 状态 |
|---|---|---|---|---|---|---|
| 1 | /animal-daycare/ | home | animal daycare roblox, animal daycare anomaly, wiki | 这是什么游戏、谁做的、我该先看哪一页、为什么没有码页 | P0 | 发布 |
| 2 | /animal-daycare/guides/ | category（Guides） | animal daycare guide | 按问题挑哪篇看 | P0 | 发布 |
| 3 | /animal-daycare/how-to-play/ | article | how to play, beginner guide, tips | 一个班次里官方要求你做哪些事、哪些细节官方没写 | P0 | 发布 |
| 4 | /animal-daycare/badges/ | article | badges, daycare legend, imposter hunter, shift 1-10 | 5 个徽章条件、多少人拿到、第几晚最难 | P0 | 发布 |
| 5 | /animal-daycare/shop/ | article | lamb coins, classes, toy hammer, water gun, revive | 25 个 Robux 商品各做什么、Lamb Coins 哪档划算、职业等级多少钱 | P0 | 发布 |
| 6 | /animal-daycare/game-info/ | article | developer, who made, max players, rating | 开发者、创建日、人数、分级、访问量、官方社区现状 | P1 | 发布 |
| 7 | /animal-daycare/author/ | author | — | 谁写的、怎么核实 | P0 | 发布 |
| 8 | /animal-daycare/impostors/ | article | how to spot impostors, anomalies | 前台放行时看什么 | P1 | **draft**（具体特征只有 B 级视频） |
| 9 | /animal-daycare/night-events/ | article | black cat, ghost, intruder, nightmare | 夜间各威胁怎么应对 | P1 | **draft**（只有 B 级视频） |
| — | /animal-daycare/codes/ | article | codes | 现在能用的码 | P0（阻塞） | 不建：无官方来源 |

## 首页模块

| 模块 | 承接 | 写什么 | 链到 |
|---|---|---|---|
| 直答首段 | animal daycare roblox | 一句话说清游戏、开发者、核心循环 | how-to-play |
| Start here | beginner | 三篇新手入口 | how-to-play / badges / shop |
| 速查表 | wiki | 开发者、创建日、人数、分级、徽章数、商品数 | game-info |
| 自动表：徽章 | badges | 5 行 entities 表 | badges |
| 自动表：商店 | lamb coins | 25 行 entities 表（名 + Robux） | shop |
| 更新时间线 | patch notes | 按商品/徽章创建日排出的时间线 | shop / badges |
| 为什么没有码页 | codes | 直说原因 | game-info |
| 来源说明 | — | 数据来自 Roblox 官方接口，快照日期 | author |

事件页：无（没有发售倒计时类页面，不需要「到期动作」列）。
