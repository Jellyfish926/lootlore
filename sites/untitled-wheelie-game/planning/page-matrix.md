# 页面矩阵（Untitled Wheelie Game，英文，首批 11 个文件 = 11 页发布）

一个意图一页；同实体组收进同一页。路由规则沿用 deep-fishing / blockspin：`/<game-slug>/<slug>/`，首页 `/untitled-wheelie-game/`。

| # | URL | 页型 | 承接词 | 这一页要回答的问题 | 优先级 | 状态 |
|---|---|---|---|---|---|---|
| 1 | /untitled-wheelie-game/ | home | untitled wheelie game, roblox | 这是什么游戏、谁做的、我该先看哪一页 | P0 | 发布 |
| 2 | /untitled-wheelie-game/beginner/ | category（Getting Started） | beginner guide | 新手按什么顺序看 | P0 | 发布 |
| 3 | /untitled-wheelie-game/how-to-play/ | article | how to wheelie, controls | 能做哪些事、抬头靠什么、按键哪些未公开 | P0 | 发布 |
| 4 | /untitled-wheelie-game/cops-fines/ | article | cops, fines, never pay fines | 警察追逐与罚款的官方信息、两种免罚方式怎么选 | P0 | 发布 |
| 5 | /untitled-wheelie-game/community/ | article | discord, codes, testing, group | 官方群组、Discord 状态、为什么不列码、别和 Wheelie District 搞混 | P0 | 发布 |
| 6 | /untitled-wheelie-game/updates/ | article | update, new update | 从官方时间戳看每次加了什么 | P1 | 发布 |
| 7 | /untitled-wheelie-game/upgrades/ | category（Money & Upgrades） | upgrades | 钱先花在哪一类 | P0 | 发布 |
| 8 | /untitled-wheelie-game/money/ | article | money, cash, job earning | 钱从哪来、倍率通行证与现金包怎么选 | P0 | 发布 |
| 9 | /untitled-wheelie-game/bikes/ | article | best bike, ebike pack, backfire, sell bikes | 官方点名过哪些车与零件、哪些已下架、哪些没公开 | P0 | 发布 |
| 10 | /untitled-wheelie-game/gamepasses/ | article | gamepasses | 12 个通行证价格与描述、先买哪个 | P0 | 发布 |
| 11 | /untitled-wheelie-game/author/ | author | — | 谁写的、怎么核实 | P0 | 发布 |
| — | /untitled-wheelie-game/codes/ | article | codes | 现在能用的码 | P0（阻塞） | 不建：无官方来源 |
| — | /untitled-wheelie-game/controls/ | article | controls pc | 按键 | P2 | 不建：无来源 |

## 首页模块

| 模块 | 承接 | 写什么 | 链到 |
|---|---|---|---|
| 直答首段 | untitled wheelie game roblox | 一句话说清游戏、开发群组、核心玩法 | how-to-play |
| Start here | beginner | 三篇新手入口 | how-to-play / money / gamepasses |
| 速览表 | — | 开发者、创建日、类型、人数、价格、分级、通行证/商品数 | — |
| 自动表：商品 | cash / backfire | entities item 表（名 + Robux） | money / bikes |
| 更新速览 | update | 最近三次上新 | updates |
| 为什么没有码页 | codes | 直说原因 | community |
| 来源说明 | — | 数据来自 Roblox 官方接口，快照日期 | author |

事件页：无（不需要「到期动作」列）。
