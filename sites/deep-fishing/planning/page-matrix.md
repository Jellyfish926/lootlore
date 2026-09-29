# 页面矩阵（Deep Fishing，英文，首批 12 个文件 = 11 页发布 + 1 页草稿）

一个意图一页；同实体组收进同一页。路由规则沿用 valheim：`/<game-slug>/<slug>/`，首页 `/<game-slug>/`。

| # | URL | 页型 | 承接词 | 这一页要回答的问题 | 优先级 | 状态 |
|---|---|---|---|---|---|---|
| 1 | /deep-fishing/ | home | deep fishing roblox, deep fishing roblox wiki | 这是什么游戏、谁做的、我该先看哪一页 | P0 | 发布 |
| 2 | /deep-fishing/beginner/ | category（Getting Started） | deep fishing guide, beginner | 新手按什么顺序看这几篇 | P0 | 发布 |
| 3 | /deep-fishing/how-to-play/ | article | how to play, beginner guide | 按住松开怎么抛、钓到之后做什么、钱和 XP 从哪来 | P0 | 发布 |
| 4 | /deep-fishing/rarity/ | article | mutations, secret fish, rarest fish | 有哪几档稀有度、变异是什么、Secret 有多难 | P0 | 发布 |
| 5 | /deep-fishing/badges/ | article | deep fishing badges | 13 个徽章条件、多少人拿到 | P1 | 发布 |
| 6 | /deep-fishing/discord/ | article | deep fishing roblox discord, group, lazygames | 官方群组、Discord、有没有官方 wiki | P0 | 发布 |
| 7 | /deep-fishing/gear/ | category（Rods & Upgrades） | deep fishing tier list, upgrades | 钱先花在哪一类 | P0 | 发布 |
| 8 | /deep-fishing/rods/ | article | best rod, all rods, galaxy rod | 一共几根竿、顺序、Robux 价、Exclusive 和皮肤 | P0 | 发布 |
| 9 | /deep-fishing/gamepasses/ | article | gamepasses, best gamepass, auto sell, fish magnet | 9 个通行证各做什么、按玩法先买哪个 | P0 | 发布 |
| 10 | /deep-fishing/shop/ | article | enchant, revive, lucky chest, server luck | Robux 商店里还有哪些系统，各自说明了什么、没说明什么 | P1 | 发布 |
| 11 | /deep-fishing/author/ | author | — | 谁写的、怎么核实 | P0 | 发布 |
| 12 | /deep-fishing/waters/ | article | pond, fernshore, dune haven | 水域顺序与解锁条件 | P1 | **draft**（只有 C/B 来源） |
| — | /deep-fishing/codes/ | article | deep fishing codes | 现在能用的码 | P0（阻塞） | 不建：无官方来源 |
| — | /deep-fishing/fish/ | article | wiki creatures / animals | 鱼种清单 | P2 | 不建：无来源 |

## 首页模块

| 模块 | 承接 | 写什么 | 链到 |
|---|---|---|---|
| 直答首段 | deep fishing roblox | 一句话说清游戏与开发者 + 核心循环 | how-to-play |
| Start here | beginner | 三篇新手入口 | how-to-play / rarity / rods |
| 自动表：鱼竿 | best rod | 23 行 entities 表（名 + Robux 解锁价） | rods |
| 自动表：徽章 | badges | 13 行 entities 表 | badges |
| 为什么没有码页 | codes | 直说原因 + 在哪等官方码 | discord |
| 来源说明 | — | 数据来自 Roblox 官方接口，快照日期 | author |

事件页：无（没有发售倒计时类页面，不需要「到期动作」列）。
