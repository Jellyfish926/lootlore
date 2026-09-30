# 同类站架构对比（Untitled Wheelie Game）

抓取日 2026-09-30。只学结构，不抄文字。第 2 步硬门复验：约 60 个域名（untitledwheeliegame.* / untitled-wheelie-game.* / uwg* / wheelie-game.wiki 等）无抢注站，Fandom 无（本步复查 untitledwheeliegame / untitled-wheelie-game / untitledwheelie 三个 fandom 子域 api.php 均 404）。所以对标对象只有大型第三方的单页码文。

## 对比表

| 站 | 页数（本游戏） | 栏目 | 主要页型 | 表格 / 信息框 | 数据来源口径 | 明显短板 |
|---|---|---|---|---|---|---|
| progameguides.com codes 页 | 1 | Codes | 单页：Active / Inactive 码表 → How to Redeem → Where to Find → What Is 本游戏 | 2 张码表 | 自称来自官方群组公告与 Discord，未给链接 | 只有码；无通行证、无价格、无玩法细节 |
| nerdschalk.com codes 页 | 1 | Codes | 单页：Working → How to redeem → Expired → How to get more → Why didn't my code work | 1 张码表 | 自称官方 Discord 与群组 | 同上；把游戏描述成「chain tricks、garage」，官方描述没有 garage 一词 |
| allthings.how codes 页 | 1 | Codes | 单页：Working → Redeem → Expired → Where posted | 码列表 | 自称群组与 Discord | 同上 |
| rotrends.com 游戏页 | 1 | 统计 | 在线人数/访问趋势 | 图表 | Roblox 公共数据 | 纯统计，无攻略 |
| pcgamesn / pockettactics / gamingdose「Wheelie District codes」 | — | — | — | — | — | **另一款游戏**（Wheelie District，universeId 9765324104），不是对标对象，列出防混淆 |

## 结论：我们比它们厚在哪、准在哪

1. **全网没有一个页面写通行证**：12 个通行证（7 在售 5 下架）的官方名称、价格、描述、上架日期，竞品一个都没列。
2. **赚钱与罚款有官方数据可写**：两组收入倍率通行证（Wheelie / Job）、6 个现金包的官方 Robux 价（可算每 Robux 换多少现金）、罚款相关的 NEVER PAY FINES 通行证与 AVOID FINES 商品——竞品只有一句「送披萨赚钱」。
3. **更新时间线**：从商品与通行证创建日拼出 6 月 4 日到 9 月 30 日的上新节奏（9-04 Backfire、9-21/9-26 罚款相关），竞品没有。
4. **码页不做**：三家码页都说码来自群组/Discord，但群组 shout 为空、wall 不可读、Discord 链接拿不到——没亲眼见官方出处，宁缺。
5. **不做外挂/脚本页**：下拉词第一名是 "script"，违反 Roblox 条款，总站不做。

## 我们采用的栏目结构

| 栏目（category） | slug | 首批文章 | 说明 |
|---|---|---|---|
| Getting Started | beginner | how-to-play、cops-fines、community、updates | 通用词入口：怎么玩、警察与罚款、官方群组/Discord/码状态、更新时间线 |
| Money & Upgrades | upgrades | money、bikes、gamepasses | 个性词入口：怎么赚钱、车与零件、通行证值不值 |
| （不设栏目） | codes | — | 等官方来源；拿到后作为 Getting Started 下的一篇文章上线 |

页型沿用 deep-fishing / blockspin 基准：home / category / article / author；每篇文章 tldr 3-4 条、首段 40-60 词直答、问题式 H2、≥1 张表、≥3 条站内链接、文末「Read next」。
