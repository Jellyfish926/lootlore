# 同类站架构对比（Deep Fishing）

抓取日 2026-09-29。只学结构，不抄文字。页数取各站 sitemap.xml。

## 对比表

| 站 | 页数 | 栏目 | 主要页型 | 表格 / 信息框 | 数据来源口径 | 明显短板 |
|---|---|---|---|---|---|---|
| deepfishing.wiki（2026-09-03 注册） | 38（其中 4 个语种首页 + 3 个法务页） | Codes / Guides / Tier List / Players / Updates / Scripts / Tools / Links | 码页、how-to 指南 8 篇、3 张 tier list（鱼稀有度、通行证、升级）、徽章页、上线说明、在线状态、抛竿计算器、外挂脚本 3 页 | 首页「Quick facts」块；tier list 按 S/A/B/C 分 H2，正文 0 张 `<table>`；每页 FAQ | 以 Roblox 官方页为「身份锚」，但玩法数字多来自视频转述 | 没有鱼竿清单；把 Legendary/Mythical/Secret 直接排成 tier list；做了外挂脚本页（总站不能碰） |
| deep-fishing.wiki（2026-09-21 注册） | 27 | Codes / Progression / Fish / Items / Locations / Tier List / Community | 码页（表格+复制）、新手、升级顺序、金币、等级、任务、成就；鱼图鉴、Secret、Jumbo、变异；鱼饵、宝箱、鱼竿；水域、Pond、Fernshore；两张 tier list；Discord 页 | 每页「Quick answer」+ Comparison / Data table + Roadmap 步骤卡 + Tips 卡；有 TOC | 大量「一段视频里说」，自己也写「价格未确定」「中段两根竿未命名」 | 鱼竿只列 8 根且两根无名；Galaxy Rod 报 5,000 Robux（官方 6,499）；把「Golden Rod」拼错；鱼图鉴页没有一条鱼名 |
| gamerant codes 页 | — | — | 原 URL /roblox-deep-fishing-codes/ 返回 404 | — | — | 未获取 |
| destructoid codes 页 | 1 | Codes | 单页码表 + 兑换步骤 | 列表，无表格 | 标 9-28 新码 update8 | 与两家 wiki 的码数对不上 |
| sportskeeda codes 页 | 1 | Codes | 单页码表 | 1 张表 | 9-23 更新 | 同上 |
| progameguides | — | — | 403 | — | — | 未获取 |

## 结论：我们比它们厚在哪、准在哪

1. **一手数据它们都没用**：Roblox 开发者商品接口直接给出 21 根可解锁鱼竿 + 2 根 Exclusive + 2 个皮肤的官方名称与 Robux 价；两家 wiki 都只凑出 8 根。我们的鱼竿表是全网唯一完整清单。
2. **稀有度用真实数据说话**：13 个徽章的累计获得数（官方 API）能换算出「每 100 个玩过的人里多少人钓到过 Secret」，竞品只有 S/A/B/C 的主观排序。
3. **通行证与 Robux 商店**：9 个通行证 + 80 多个开发者商品的官方名称、价格与上架日期，能画出更新时间线（8-25 宝箱、9-06 附魔石、9-18 单次增益、9-26 Exclusive 竿），竞品没有。
4. **码页不做**：没有官方来源亲眼看到的码，宁可空缺也不跟 C 站互抄。水域页（Fernshore / Pond / Dune Haven）同理先 draft。
5. **不做外挂/脚本页**：deepfishing.wiki 的 Scripts 栏目违反 Roblox 条款，总站不跟。

## 我们采用的栏目结构

| 栏目（category） | slug | 首批文章 | 说明 |
|---|---|---|---|
| Getting Started | beginner | how-to-play、rarity、badges、discord（+ waters 草稿） | 通用词入口：怎么玩、稀有度、徽章、官方社区链接 |
| Rods & Upgrades | gear | rods、gamepasses、shop | 个性词入口：best rod、gamepass 值不值、enchant stone / 宝箱 / 复活 |
| （不设栏目） | codes | — | 等官方来源；拿到后作为 Getting Started 下的一篇文章上线 |

页型沿用 valheim 基准：home / category / article / author；每篇文章 tldr 3-4 条、首段 40-60 词直答、问题式 H2、≥1 张表、≥3 条站内链接、文末「Read next」。
