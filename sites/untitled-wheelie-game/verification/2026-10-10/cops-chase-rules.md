# cops-chase-rules 独立核验

47 条命题，0 条被推翻，1 条未验；另有 2 处白话转述列为「边界」（已判 CONFIRMED，供决定是否收紧，见命题 24、29）。取证时间 2026-10-10 02:23–02:27 UTC，原始响应在 `b5/verify/raw/`（自己重取）。AI COPS 是活动接口 `data[4]`，id 2834536995286549130。脚本：`b5/verify/quotes.py`、`b5/verify/search.py`（命中表 `b5/verify/search-hits.txt`）。

## 活动接口取证统计

- 带零起点游标 `?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA`：10 次均 7 条（最多 7 条，出现 10 次），nextPageCursor 恒为空串；顺 previousPageCursor 翻页 6→5→4→3→2→1→0，没有更早记录。
- 不带参数：02:23 的 10 次各回 7 条，02:27 的 10 次各回 1 条（HALLOWEEN UPDATE）。接口行为不稳定。AI COPS 条目在 7 条响应里逐字相同。
- games / game-passes / developer-products 各回 200。

| 编号 | 命题 | 验证路径（URL + 字段）| 结果 | 证据 | 取证时间（UTC）|
|---|---|---|---|---|---|
| 1 | 活动标题逐字 `AI COPS 👮` | EV `data[4].title` | CONFIRMED | `AI COPS 👮` | 02:23 |
| 2 | 建立 2026-09-21 04:17（UTC）；start 09-25 22:00；end 09-26 22:00 | EV `data[4].createdUtc`、`eventTime` | CONFIRMED | created 2026-09-21T04:17:20.772；start 2026-09-25T22:00:06.583；end 2026-09-26T22:00:06.583 | 02:23 |
| 3 | 编辑时间与建立时间在同一秒，「record shows no later edit」 | EV `data[4].updatedUtc` | CONFIRMED | updated 2026-09-21T04:17:20.884，与 created 差 0.112 秒；同接口里 MAP REVAMP 的 updatedUtc 比 created 晚 3 分钟，说明该字段会记录后续编辑 | 02:23 |
| 4 | 建立比开始早「4 days 17 hours」（正文）/「more than four days」（末节）| EV `data[4]` | CONFIRMED | 重算 4 天 17 小时 42 分 45 秒 | 02:23 |
| 5 | 原文开头 `AI Cops are being added!`；`COP BEHAVIOR:` 9 行、`WHAT TO EXPECT:` 3 行，合计 12 行 | EV `data[4].description` | CONFIRMED | 9 + 3 = 12，开头句逐字 | 02:23 |
| 6 | COP BEHAVIOR 1 逐字 `Cops will park beside highways, in parking lots, or in random places` | 同上 | CONFIRMED | 脚本：行文本在页内 True | 02:23 |
| 7 | COP BEHAVIOR 2 逐字 `Cops will have a much higher chance of chasing illegal bikes` | 同上 | CONFIRMED | 同上 | 02:23 |
| 8 | COP BEHAVIOR 3 逐字 `There will be a 3 star system similar to GTA's 5 star system` | 同上 | CONFIRMED | 同上 | 02:23 |
| 9 | COP BEHAVIOR 4 逐字 `At 3 stars, cops will begin to set up roadblocks` | 同上 | CONFIRMED | 同上 | 02:23 |
| 10 | COP BEHAVIOR 5 逐字（含 `costed you!`）| 同上 | CONFIRMED | `You will be fined if you are caught for various crimes, but if you escape, then you will get the money that the fines would have costed you!` | 02:23 |
| 11 | COP BEHAVIOR 6 逐字 `If a cop gets juked out, they will spin out. Slowing them down`（无句号）| 同上 | CONFIRMED | 同上 | 02:23 |
| 12 | COP BEHAVIOR 7 逐字（句末有句号）| 同上 | CONFIRMED | `If cops lose sight of you, they will patrol the area near the last time they saw you.` | 02:23 |
| 13 | COP BEHAVIOR 8 逐字 | 同上 | CONFIRMED | `If they lose sight of you for over 60 seconds, they give up.` | 02:23 |
| 14 | COP BEHAVIOR 9 逐字 | 同上 | CONFIRMED | `Cops don't like wheelies, on any bike too.` | 02:23 |
| 15 | WHAT TO EXPECT 1 逐字，`seperate` 为原文拼写 | 同上 | CONFIRMED | `Single player servers, seperate from the actual game.` | 02:23 |
| 16 | WHAT TO EXPECT 2 逐字 | 同上 | CONFIRMED | `Cops are not easy to get away from. Use tactics to spin them out or hide from them.` | 02:23 |
| 17 | WHAT TO EXPECT 3 逐字 | 同上 | CONFIRMED | `Getting chased will be a gamble, you either lose money or make money.` | 02:23 |
| 18 | 行序与编号：页内表格 1–9、1–3 的顺序与原文一致，未漏未并 | 同上 | CONFIRMED | 原文编号 1–9、1–3，页内一一对应 | 02:23 |
| 19 | tldr / 正文里的子串引文：`a 3 star system similar to GTA's 5 star system`、`At 3 stars, cops will begin to set up roadblocks`、`for over 60 seconds`、`the money that the fines would have costed you`、`Single player servers`、`various crimes`、`don't like wheelies`、`you either lose money or make money.`、`Use tactics to spin them out or hide from them.` | 同上 | CONFIRMED | `quotes.py` 全部在活动文本中命中（EV 档）| 02:23 |
| 20 | 12 行里（行号除外）出现的数字只有 3、5、60 | 同上 | CONFIRMED | 数字：3（两次）、5、60；无其他 | 02:23 |
| 21 | 「Most lines use 'will'」| 同上 | CONFIRMED | 含 will 的 8 行（COP 1–7、WTE 3）/ 12 行 | 02:23 |
| 22 | 白话 COP 1「Cops can be parked at the roadside, in car parks or at other spots on the map」| 对照命题 6 | CONFIRMED | 边界：原文是 beside highways，页内 roadside 范围略宽于 highways，未增加数值或因果；「on the map」为本站补语。判定同范围 | 02:23 |
| 23 | 白话 COP 2「Some bikes draw a chase more often; the line does not say which bikes are illegal」| 对照命题 7 | CONFIRMED | 与原文一致；`illegal` 全语料仅此 1 处 | 02:24 |
| 24 | 白话 COP 3「A wanted level with three steps」| 对照命题 8 | CONFIRMED | 边界：「wanted level」是本站用词，原文只说 3 star system，类比 GTA 星级通缉；未增数值 | 02:23 |
| 25 | 白话 COP 4「Roadblocks start at the top wanted level」| 对照命题 9 | CONFIRMED | 「top」由 3 star system 推出，3 为系统上限，原文无与之矛盾内容；页内已声明白话为本站解读 | 02:23 |
| 26 | 白话 COP 5「Caught means a fine; escaped means you are paid the amount the fines would have been」| 对照命题 10 | CONFIRMED | 与原文一致，未加金额 | 02:23 |
| 27 | 白话 COP 6「A cop that is dodged spins and loses speed」| 对照命题 11 | CONFIRMED | juked out→dodged；`Slowing them down`→loses speed | 02:23 |
| 28 | 白话 COP 7、8（search around the last sighting；超过 60 秒即结束追逐）| 对照命题 12、13 | CONFIRMED | 一致；`over 60 seconds`→「More than 60 seconds」 | 02:23 |
| 29 | 白话 COP 9「Wheelies draw police attention on every bike」| 对照命题 14 | CONFIRMED | 边界：原文是 `Cops don't like wheelies, on any bike too.`；「draw police attention」把「不喜欢」转成「引来注意」，措辞比原文具体，未增数值。正文另有「Whether a wheelie alone adds a star is our question」限定 | 02:23 |
| 30 | 白话 WTE 1–3（solo servers apart from the main game；escaping meant to be hard，两种工具是 spin-outs 与 hiding；a chase ends in a loss or a gain）| 对照命题 15–17 | CONFIRMED | 与原文一致，未增因果 | 02:23 |
| 31 | 「Single player servers」被转述为「solo servers」「one-player servers」，且「How a player opens such a server is not stated」 | 全语料检索 `single player\|server` | CONFIRMED | 命中仅 AI COPS WTE 1（2 处）；游戏记录无相关字段 | 02:24 |
| 32 | 「Read literally, line 5 makes the two amounts equal」 | 命题 10 | CONFIRMED | 原文把逃脱报酬定义为「the money that the fines would have costed you」，字面即罚款额 | 02:23 |
| 33 | 5 属于类比游戏；Untitled Wheelie Game 的计数为 3 | 命题 8 | CONFIRMED | 原文「3 star system similar to GTA's 5 star system」| 02:23 |
| 34 | NEVER PAY FINES 是通行证，149 Robux；描述 `Just never have to pay fines for when you get caught` | GP `name=NEVER PAY FINES`.price / displayDescription | CONFIRMED | price 149；描述逐字一致 | 02:24 |
| 35 | AVOID FINES 是开发者商品，13 Robux | DP `Name=AVOID FINES`.PriceInRobux | CONFIRMED | 13 | 02:24 |
| 36 | 「Two store records carry 'FINES' in their names」 | 检索 `\bfine` | CONFIRMED | 名称含 FINES 的只有这两条 | 02:24 |
| 37 | 游戏记录每服最多 10 人 | GM `data[0].maxPlayers` | CONFIRMED | 10 | 02:24 |
| 38 | 游戏描述 `WHAT YOU CAN DO` 下第一条是 `🚔 RUN FROM COPS` | GM `data[0].description` | CONFIRMED | `🔥 WHAT YOU CAN DO\n\n🚔 RUN FROM COPS\n🏍️ Wheelie around the map…` | 02:24 |
| 39 | 否定：七条公告没有一行把罚款或报酬写成数字 | 检索 `price\|cost\|robux\|\$`、`cash\|money`、`\bfine` | CONFIRMED | 活动内命中：`costed` 1、`money` 3、`fined`/`fines` 2，均无数字；其余六条无金额 | 02:24 |
| 40 | 否定：`illegal` 在游戏描述、7 条活动、12 通行证、23 商品、群描述里只出现 1 次（就是第 2 行）；商店记录没有把任何车标成合法 / 不合法 | 检索 `illegal\|legal` | CONFIRMED | 全语料仅 AI COPS 1 处；GP / DP 0 处 | 02:24 |
| 41 | 否定：通行证描述没提逃脱拿钱；公告没提通行证 | 检索 `escape`、`\bpass` | CONFIRMED | `escape` 仅 COP 5；`\bpass` 在活动文本 0 处；NEVER PAY FINES 描述无 escape | 02:24 |
| 42 | 否定：没写什么行为加星、1 / 2 星表现、星级怎么降；`various crimes` 未点名任何一种；没写什么算「看得见」、建筑 / 隧道是否遮挡、60 秒是否重计；没写入狱 / 没收 | 检索 `star`、`crime`、`sight\|hide\|tunnel\|building`、`jail\|arrest\|prison` | CONFIRMED | star 3 处（COP 3、4，另 Ridstar 子串）；crime 1 处；sight/hide 3 处；`Tunnel System` 在 MAP REVAMP，与追逐无关；jail/arrest/prison 0 | 02:24 |
| 43 | 否定：公告和游戏记录都没说 10 人服里有没有警察；不知道进度 / 钱是否带回主游戏 | 检索 `cop\|server\|player` | CONFIRMED | 游戏描述有 `RUN FROM COPS`、`player` 各 1 处，无关于 10 人服里是否有 AI 警察的陈述 | 02:24 |
| 44 | 「whether the rules were changed after the listing was written」未记录 | 命题 3 | CONFIRMED | updatedUtc≈createdUtc，接口无变更历史字段 | 02:23 |
| 45 | 公告口径检查：页内所有关于公告内容的句子是否带限定 | 页面全文逐段 | CONFIRMED | 首段、「Where do…come from」节、各节首句均带 the announcement says / lists / reads / Taken as written / Read literally；表格白话列受「The plain-words notes are our reading」「Treat every rule below as what the developer's announcement says」统摄；末节与 tldr 第 4 条声明未实测。未发现把公告写成已验证机制的句子。风险点：seoTitle「AI Cops: 3 Stars, Roadblocks, 60s」与 H1「Cop Chase Rules: Stars, Roadblocks」是无限定的标题式陈述，description 字段有「from the developer's AI COPS announcement」补足 | 02:25 |
| 46 | 站内链接：cops-fines、patch-notes、how-to-play、bikes、money | `content/untitled-wheelie-game/en/*.md` | CONFIRMED | cops-fines / how-to-play / bikes / money 均 draft: false；patch-notes 为本批新页；无 draft 页被链 | 02:25 |
| 47 | 封面 art01（与 cops-fines、updates 共用）及其所属说明 | 图片文件 | UNVERIFIED | 本机无 art01 文件；缩略图接口不在 sourceUrls；cops 页 frontmatter 只有 images: ["art01"]，正文无图注文字可核 | 02:25 |

## 机检

1. 外链：正文无 http 外链；sourceUrls 四个地址全回 200，与草稿 sourceUrls 一致。
2. 站内链接：见命题 46。
3. 不带日期的时间词（now / currently / upcoming / soon / latest / recently / new 指时间）：正文 0 处。
4. 兑换码 / 第三方站 / 外挂脚本 / 账号买卖：0 处。
5. 提示：patch-notes 与本页互链，两页须同批上线，否则 /patch-notes/ 或 /cops-chase-rules/ 一端为死链。
