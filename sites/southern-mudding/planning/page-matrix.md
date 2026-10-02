# 页面矩阵（Southern Mudding，英文，首批 12 个文件 = 12 页发布 + 0 草稿）

路由：`/southern-mudding/<slug>/`，首页 `/southern-mudding/`。全部页面至少有 1 个 S 级来源（Roblox 官方 API），无 draft。A 级来源本轮为 0（群组 wall / Discord / X 需登录）。

| # | URL | 页型 | 承接词 | 这一页要回答的问题 | 优先级 | 状态 |
|---|---|---|---|---|---|---|
| 1 | /southern-mudding/ | home | southern mudding roblox, wiki | 是什么、谁做的、先看哪页、每周几更新、为什么没有码页 | P0 | 发布 |
| 2 | /southern-mudding/guides/ | category | southern mudding guide | 按问题挑哪篇；哪些问题我们答不了 | P0 | 发布 |
| 3 | /southern-mudding/how-to-play/ | article | how to play, beginner | 官方描述里能做什么；按 4 个徽章排的第一次游玩顺序（标明是建议） | P0 | 发布 |
| 4 | /southern-mudding/updates/ | article | update, update today, next update, when/what time | 周五几点更新、9-25 加了什么、43 条官方活动标题排出的更新史 | P0 | 发布 |
| 5 | /southern-mudding/gamepasses/ | article | gamepass + 单通行证名 | 13 个通行证价格与作用、礼物版差价、先买哪个（建议） | P0 | 发布 |
| 6 | /southern-mudding/limiteds/ | article | limited, 6x6, utv, tornado | 22 个 Robux 载具价格与创建日、接口在售标记、龙卷风与 Delivery Event 商品 | P0 | 发布 |
| 7 | /southern-mudding/community/ | article | codes, discord, group, free truck | 官方群组是哪个、进群送皮卡、码与 Discord 的现状 | P0 | 发布 |
| 8 | /southern-mudding/vehicles/ | article | vehicles, trucks, classic cars, race cars | 官方点名的车型类别、四条获取途径（免费 / 进群 / 通行证包 / Robux 单买） | P1 | 发布 |
| 9 | /southern-mudding/spawning/ | article | spawn 4 vehicles, any slot, trailer | 默认上限 2+2、四个生成类通行证、拖车包 | P1 | 发布 |
| 10 | /southern-mudding/nitrous/ | article | nitrous, rock lights, whip lights, customization | 9-25 氮气更新官方原话、两个改装通行证、哪些不知道 | P1 | 发布 |
| 11 | /southern-mudding/badges/ | article | badges, houses, claimed a house | 4 个徽章条件与累计数、领房与 Luxury Houses | P1 | 发布 |
| 12 | /southern-mudding/author/ | author | — | 谁写的、怎么核实 | P0 | 发布 |
| — | /southern-mudding/codes/ | article | codes | — | P0（阻塞） | 不建：无官方来源 |
| — | /southern-mudding/map/ | article | map | — | P2 | 不建：无一手素材，等进游戏核实 |

## 首页模块

| 模块 | 承接 | 写什么 | 链到 |
|---|---|---|---|
| 直答首段 | southern mudding roblox | 游戏、开发者、能做什么 | how-to-play |
| Start here | beginner | 三篇入口 | how-to-play / updates / gamepasses |
| 速查表 | wiki | 开发者、创建日、类型、人数、分级、徽章数、通行证数、商品数、更新日 | — |
| 自动表：通行证 | gamepass | entities gamepass 表 | gamepasses |
| 自动表：商品 | limited | entities item 表（前 12 行） | limiteds |
| 更新时间一节 | update | 周五 17:00 UTC 的官方排期 | updates |
| 为什么没有码页 | codes | 直说原因 + 进群送皮卡 | community |

## 事件页与到期动作

没有独立事件页。updates 页里有一节写 Roblox 活动排期，带到期动作：

| 内容 | 触发日期 | 到期动作 |
|---|---|---|
| 「🚀Nitrous Update!🚀」活动（止于 2026-10-02 17:00:56 UTC） | 2026-10-02 更新落地后 | 重取 games / events / developer-products；updates 页把 Nitrous 一节改过去时并追加 10-02 的更新说明；检查游戏名前缀是否变了；`gameVersion` 改成新日期 |
| 「This Week's Update!」「Next Week's Update!」（滚动占位活动） | 每周五 | 重取 events 接口，更新排期表的日期与 RSVP 数 |
| limiteds 页「API 在售标记」 | 每周五 | 重取 developer-products，追加新商品行；有商品 IsForSale 变 false 就改该行状态 |
