# 同类站架构对比(Get Your Driver's License!,2026-10-09 抓取)

只学结构,不抄文字。本游戏 2026-09-29 才创建,**目前没有任何专站、Fandom、攻略文或码页**(实测:WebSearch 4 组查询 0 条相关;6 个可能的 Fandom 子域 api.php 全 404;robloxden / tryhardguides / beebom / pockettactics 的猜测 URL 404,progameguides 403)。所以对标对象换成同品类「排队 / 多结局」Roblox 游戏的攻略站,外加已经收录本游戏的两个统计站。每一行都是本人实际打开过的页面;没打开的不列。

结论:同品类攻略站靠「一篇超长的全结局步骤文 + 大量实机截图」吃流量(itemlevel.net 单篇约 90 张截图;allthings.how 单篇一张 25 行结局表)。这两样我们现在都做不了,因为没有进游戏。已收录本游戏的只有统计站,它们把官方数字抄了一遍,**没有一家用上 13 个开发者商品的官方描述**(Rotrends 还停在 12 个)。我们首批就把栏目建在这层一手数据上:排队与跳过、路考与结局、车、通行证、商店,结局全表与车表留到进游戏核实后再补。

## 对比表

| 站 | 实际打开的页 | 抓取状态 | 栏目 / 导航 | 页型 | 表格 / 列表 / 图 | 我们取什么 | 我们不取什么 |
|---|---|---|---|---|---|---|---|
| itemlevel.net(Item Level Gaming) | 「Easiest Game On Roblox: How To Get All Endings」;「Go Pee At 3 AM: Complete Guide & How to Get All Endings」 | WebFetch 可读(2026-10-09) | 顶部:Home / News / Guides / Tier Lists / How-To / Locations;面包屑 Home › Guides › 文章;每个游戏一个 Game Hub 侧栏盒(Easiest Game on Roblox 标 38 篇) | 游戏 hub + 单篇结局总览(H3 一个结局,H4 分步骤)+ 单个结局拆成独立文章 | 0 张表;编号步骤列表;一篇约 90 张 / 约 29 张实机截图;正文约 9,000–10,000 词 / 约 1,500 词;作者 + fact-check 双署名,发布日与更新日 | 「一个游戏一个 hub + 同类实体收进一页」的骨架;页尾「下一篇」与同游戏文章列表;署名与复核日期并列 | 逐结局拆页(我们只有 2 个结局名,拆不出);截图步骤(没进游戏);把更新后的新结局另开一篇 |
| allthings.how | 「Leave Your House at 2 AM: How to Get All Endings (Roblox)」 | WebFetch 可读(2026-10-09;页面标 updated Sep 18, 2026) | 顶部:Gaming / Roblox / Codes / Roblox Events / Fortnite Events / Windows / Apps;文章归 Gaming · How-To | 单篇 how-to:On this page 目录 → 每局必备 → 一张全结局触发表 → 分区域小节 → 「How to confirm an ending registered」 | 1 张约 25 行的结局表 + 2 段编号步骤;4 张实机截图;正文约 1,800 词;署名 AllThingsHow Staff | 「先给一张总表,再分节解释」的写法(我们的 shop / gamepasses / waiting-line 页都先表后文);On this page 目录;结尾放「怎么自己确认」一节(driving-test 页的「How can you track endings yourself?」) | 触发条件表(没有一手来源);匿名署名 |
| rolimons.com | /game/104416416393862(本游戏) | curl 200(2026-10-09) | 站级:Trading / Catalog / Players / Games / Groups;游戏页分 Primary Stats / Peak Player Counts / Description / Charts & More(Charts、Gamepasses、Badges、Places、Servers) | 数据统计页(单页) | 指标卡 + 通行证卡(5 个,名称与价格);「This game has no known badges」 | 交叉核对:通行证 5 个与价格和 Roblox 接口一致;徽章 0 个一致。平均游玩时长 10.06 分钟作为 B 级旁证在 how-to-play 里标明出处引用一次 | 不列开发者商品、不解释任何商品做什么 |
| rotrends.com | /game/10768565603(本游戏) | curl 200(2026-10-09) | 站级:Games / Top / Trending / Analyze / Genres / Players / Groups;游戏页面包屑 Games / Simulation / Idle / 游戏名 | 数据统计页 + 模板化 FAQ(What is… / Who created… / When was… released / How do I play… on my phone) | 指标卡:Global #159、Peak CCU 24.2K、Rating 36%、Avg Session 11.0 mins;「Game Passes 5 passes · Dev Products 12 products」 | 面包屑把品类写成 Simulation / Idle,与 Roblox 接口的 genre_l1 / genre_l2 一致,hub 的 key facts 表照此写;FAQ 的问题清单提示了通用问法(谁做的、什么时候出的) | 模板 FAQ 的答案是字段拼接,没有信息量;商品数过期(12,实际 13) |
| Fandom | 6 个可能的子域(get-your-drivers-license / getyourdriverslicense / get-your-driver-s-license / gydl / time-will-pass / timewillpass) | api.php 全部 404 | — | — | — | — | 没有 Fandom wiki |
| 码站(robloxden / tryhardguides / beebom / pockettactics / progameguides) | 按各站惯用 URL 规则试的 5 个地址 | 404 ×4、403 ×1 | — | — | — | — | 没有码页;官方来源也没有码,我们不建 codes 页 |

## 基准栏目的页型(lootlore 仓内,结构照抄的对象)

| 基准 | 文件数 | 页型 | 栏目 | 我们沿用的做法 |
|---|---|---|---|---|
| content/roblox-stock-exchange-2/en(2026-10-08) | 12(全发布) | home / category ×2 / article ×8 / author | Getting Started;Passes & Robux Shop | frontmatter 字段与顺序、两栏结构、hub 的 key facts 表 + All sections + How this guide uses its sources、gamepasses / shop 的「官方描述逐字表 + 我们的算术表」、community 页的官方位置逐一核对表、author 页结构 |
| content/deep-fishing/en | 12(11 发布 + 1 draft) | 同上 | Getting Started;Rods & Upgrades | hub 页「Why is there no codes page?」一节(官方来源 0 个码时的写法);hub 的「What has changed since launch?」商品创建日时间线 |
| content/stone-skipping/en | 11 | 同上 | 两栏 | `_images.json` 里通行证 / 商品图标(420 方图)作为正文配图、不作首图的做法 |
| content/blockspin/en | 12(7 发布 + 5 draft) | 同上 | Getting Started;Money & Gear(全 draft) | 只有 B/C 来源的页整页 draft 的门控(本批没有这类页,见 planning/page-matrix.md) |

## 我们采用的栏目结构

| 栏目(category) | slug | 首批文章 | 首发状态 | 说明 |
|---|---|---|---|---|
| Home | index | hub 首页 | 发布 | 通用词落地 + 分流;key facts 表 + 一局流程表 + 上架时间线;FAQ 6 条 |
| Getting Started | beginner | how-to-play、waiting-line、driving-test、community | 全部发布(都有 S 级来源) | 一局的四段:怎么玩、排队与跳过、路考 / 结局 / 考官、谁做的 |
| Cars & Robux Shop | robux | cars、gamepasses、shop | 全部发布(都有 S 级来源) | 花 Robux 之前要看的三页:车、通行证、13 个商品 |
| Author | author | 作者页 | 发布 | E-E-A-T;写明哪些内容等进游戏核实 |

## 我们比它们厚在哪、准在哪

1. **商品描述**:13 个开发者商品每个都有一句官方描述,里面有硬数字(往前 5 位、跳过 2:30、5 分钟考官)。统计站不列商品,攻略站还没人写。
2. **跳过排队的算账**:Skip Line / Skip Time / Skip Test 加起来 47 Robux,Skip To End 48;Retake Test 比 Skip To End 便宜 29。全部是官方价格上的算术。
3. **[SALE] 不是折扣**:两个商品名带 [SALE],Roblox 价格记录里折扣列表为空。玩家会被名字误导。
4. **车**:官方只说了 18 辆、Epic 档、Golden Supercar 🏆「The best car in the game」只卖 39 Robux 而 VIP Ticket 🎟️ 卖 149。我们把这六句话摆全,并明说没有车表。
5. **不编**:结局只列官方点名的两个;笔试答案、考场路线一个字不写;没有码页。
6. **不做**:script / 外挂;「best car tier list」(无数值);逐结局拆页(素材不足)。
