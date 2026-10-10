# patch-notes 独立核验

44 条命题，1 条被推翻，2 条未验。取证时间 2026-10-10 02:23–02:27 UTC，原始响应在 `b5/verify/raw/`（自己重取，未采信 b5/raw/）。脚本：`b5/verify/quotes.py`（引文逐字比对）、`b5/verify/search.py`（否定句检索，命中表 `b5/verify/search-hits.txt`）。

## 活动接口取证统计

- 带零起点游标 `?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA`：10 次，10 次都是 7 条，nextPageCursor 恒为空串，previousPageCursor 恒为 `id_2zwAAAZ-Vt1O_zyQLI6KCQgKJ`；最多 7 条，出现 10 次。
- 顺 previousPageCursor 翻页：6 → 5 → 4 → 3 → 2 → 1 → 0 条，没有比 FULL GAME RELEASE 更早的记录。
- 不带参数：02:23 的 10 次读取各回 7 条（内容与零游标逐条相同）；02:27 的 10 次读取各回 1 条（HALLOWEEN UPDATE）。`?limit=100`、`?sortOrder=Desc` 回 1 条。同一接口在 4 分钟内行为翻转，回 7 条与回 1 条都出现过。
- 7 条的 eventStatus 都是 `active`，host 都是 Untitled Wheelie Group（hostId 84540135）。
- 四个 sourceUrls 都回 200（games、game-passes、developer-products 各取 1 次，返回 12 个通行证、23 个商品，nextPageToken 空 / nextPageCursor null）。

| 编号 | 命题 | 验证路径（URL + 字段）| 结果 | 证据 | 取证时间（UTC）|
|---|---|---|---|---|---|
| 1 | 活动共 7 条，之后无下一页 | EV `data` 长度、`nextPageCursor` | CONFIRMED | 10/10 次 7 条，nextPageCursor 为空串；prev 链 6→0 | 02:23 |
| 2 | 7 个标题逐字（含表情符号）：FULL GAME RELEASE、BIG UPDATE、EBIKE UPDATE、MAP REVAMP、AI COPS 👮、Mopeds + Rain 🛵🌧️、HALLOWEEN UPDATE 🎃 | EV `data[i].title` | CONFIRMED | 脚本逐条 `title in 页面文本` 全 True（含变体选择符）| 02:23 |
| 3 | 开始时间 UTC：07-23 20:00、08-08 00:00、08-15 20:00、09-05 21:00、09-25 22:00、10-02 22:00、10-21 22:30 | EV `eventTime.startUtc` | CONFIRMED | 2026-07-23T20:00:47、08-08T00:00:30、08-15T20:00:56、09-05T21:00:44、09-25T22:00:06、10-02T22:00:28、10-21T22:30:29 | 02:23 |
| 4 | 建立日 UTC：07-17、08-04、08-14、09-04、09-21、09-30、10-06 | EV `createdUtc` | CONFIRMED | 07-17T17:55:54、08-04T23:23:15、08-14T05:50:13、09-04T22:04:48、09-21T04:17:20、09-30T01:57:19、10-06T20:52:53 | 02:23 |
| 5 | 「created between 17 July and 6 October 2026」 | EV `createdUtc` 最小 / 最大 | CONFIRMED | 最小 2026-07-17T17:55:54，最大 2026-10-06T20:52:53 | 02:23 |
| 6 | MAP REVAMP 建立 09-04 22:04、开始 09-05 21:00，间隔「22 hours 56 minutes」 | EV `data[3]` createdUtc / startUtc | CONFIRMED | 重算 22:55:56.113（按页内 HH:MM 相减为 22:56；精确秒数是 22 小时 55 分 56 秒）| 02:23 |
| 7 | HALLOWEEN 建立 10-06 20:52、开始 10-21 22:30，「about 15 days」 | EV `data[6]` | CONFIRMED | 重算 15 天 1 小时 37 分 36 秒 | 02:23 |
| 8 | 每条建立时间早于自己的开始时间；MAP REVAMP 间隔最短、HALLOWEEN 最长 | EV 七条 createdUtc / startUtc | CONFIRMED | 间隔：6d2h05m、3d0h37m、1d14h11m、22h56m、4d17h43m、2d20h03m、15d1h38m；最短 MAP REVAMP，最长 HALLOWEEN | 02:23 |
| 9 | 「each text was written ahead of the update it describes」 | EV 七条 updatedUtc 与 startUtc | CONFIRMED | 七条 updatedUtc 都早于 startUtc（最近一次编辑：HALLOWEEN 10-09T22:06:45，仍在 10-21 之前）| 02:23 |
| 10 | 5 条副标题是 `Be Ready!⌛📢`（FULL GAME、BIG、AI COPS、Mopeds、HALLOWEEN）；另两条是 `Ridstar, Super73, Macfox`、`+ New Trick System` | EV `subtitle` | CONFIRMED | 5 条一致；EBIKE、MAP REVAMP 为另两条 | 02:23 |
| 11 | Mopeds + Rain 原文：`New Bikes 🏍️:`、`Normal Moped, 40MPH stock, 80MPH modded 🛵`、`Junkyard Moped, 35MPH stock, 160MPH modded 🛠️`；tldr 与首段引文 `40MPH stock, 80MPH modded`、`35MPH stock, 160MPH modded` | EV `data[5].description` | CONFIRMED | 脚本逐字命中 | 02:23 |
| 12 | 推导：80−40=40；160−35=125；40−35=5；160÷80=2 | 由 11 的四个数 | CONFIRMED | 重算全部一致 | 02:23 |
| 13 | 这四个 MPH 数是读到的记录里以数字给出的车速 | 全语料检索 `speed\|mph` | CONFIRMED | mph 只在 Mopeds + Rain description（4 处）；通行证 Extra Bike Speed 只有文字「Adds speed to your bike」，无数字 | 02:24 |
| 14 | 灯和雨三行逐字：`Lights on all bikes 💡:`、`Bar Light on basically all bikes, some come stock with one 🔦`、`Baja Light for all bikes 🔆`、`Rain 🌧️:`、`A rain setting with a lightning option ⚡🌩️`；引文 `on basically all bikes`、`for all bikes`、`A rain setting` | EV `data[5].description` | CONFIRMED | 脚本逐字命中；三行位于两个标题之下 | 02:23 |
| 15 | 否定：公告没说 modded 指什么、怎么获得、多少钱、是否平路极速 | 检索 `modded\|mod\b\|upgrade`；通读 `data[5]` | CONFIRMED | modded 只出现 2 次且无解释；`Backfire Mod for Gas Bikes` 是另一条；description 全文只有速度、灯、雨 | 02:24 |
| 16 | 否定：「moped」只在这一个活动里；12 个通行证名与 23 个商品名里没有 | 检索 `moped`；GP 12 条、DP 23 条 | CONFIRMED | 命中 3 处，全在 Mopeds + Rain（title 1、description 2）；GP/DP 0 | 02:24 |
| 17 | Bar Light / Baja Light 措辞差异（basically all vs all）；「which bikes are excluded」未说明 | EV `data[5]` | CONFIRMED | 原文如此，无排除名单 | 02:23 |
| 18 | FULL GAME RELEASE 逐字：`The full game will be set to release on july 23, 1:00PM MST (4:00 PM EST)!`、`Make sure your notifications are on!⌛`；start 07-23 20:00 UTC、end 07-24 20:00 UTC | EV `data[0]` | CONFIRMED | description 逐字一致；start 2026-07-23T20:00:47.551、end 2026-07-24T20:00:47.551。备注：原文 MST 1PM 折 UTC 20:00，与 start 一致；EST 4PM 折 UTC 21:00，原文自身不一致，页内只照抄、未据此下结论 | 02:23 |
| 19 | 游戏记录建立 2026-06-04，到 07-23 为 49 天 | GM `data[0].created` | CONFIRMED | created 2026-06-04T06:53:02.486Z；6 月剩 26 天 + 23 = 49（精确 49 天 13 小时）| 02:24 |
| 20 | BIG UPDATE 引文逐字；两台车和工作未命名；最后编辑 08-07 23:53，距开始 00:00 为 7 分钟 | EV `data[1]` | CONFIRMED | description 一致、无名称；updatedUtc 2026-08-07T23:53:28，start 2026-08-08T00:00:30，相差 7 分 02 秒 | 02:23 |
| 21 | 「The job that the game description does name, pizza delivery」 | GM `data[0].description` | CONFIRMED | 含 `💰 Deliver pizzas to earn money` | 02:24 |
| 22 | EBIKE UPDATE：副标题 `Ridstar, Super73, Macfox` 逐字；description 转述「a single four-word line saying that all bikes are on the way」忠实；「does not say what the three names are」 | EV `data[2]` | CONFIRMED | 原文 `All bikes coming soon!`，4 个词，意思即「所有车快来了」，转述未增减数值或范围；三个名字只出现在 subtitle（检索 `ridstar\|super73\|macfox` 仅 1 处）。表格「a one-line description about bikes」同样成立 | 02:23 |
| 23 | EBike Pack ⚡ 通行证建立 2026-08-15 06:29 UTC，与 EBIKE 开始同一 UTC 日 | GP `name=EBike Pack ⚡`.createdTimestamp | CONFIRMED | 2026-08-15T06:29:15.331Z；EBIKE start 2026-08-15T20:00:56 | 02:24 |
| 24 | MAP REVAMP：副标题 `+ New Trick System`、标题行 `THINGS COMING WITH THE UPDATE:`、7 项逐字 | EV `data[3]` | CONFIRMED | 7 项：New Map / Infinite Highway System / Tunnel System / New Trick System / Backfire Mod for Gas Bikes / Jetson Ebike / Bug Fixes / Other Small things，与页内一致，条数 7 | 02:23 |
| 25 | 「None of the seven items comes with a place name, a control or a figure such as a speed」 | 通读 `data[3]` 7 项；检索 `key\|button\|control` | CONFIRMED | 7 项只有名词短语，无地名、按键、数值；活动语料 `key\|button\|control` 0 命中（唯一命中在群描述 JSON 的 key 字段名）| 02:24 |
| 26 | 七条公告里提到 Backfire 的只有 MAP REVAMP 第 4 项；该项写明 `Gas Bikes` | 检索 `backfire` | CONFIRMED | 活动内 1 处（MAP REVAMP）；另 3 处是商品名 | 02:24 |
| 27 | 三个 Backfire 商品建立于 2026-09-04 03:02 UTC，为 MAP REVAMP 开始（09-05）的前一天 | DP `INSTALL BACKFIRE`、`LEVEL 2 BACKFIRE`、`LEVEL 3 BACKFIRE`.Created | CONFIRMED | 03:02:01、03:02:14、03:02:25（2026-09-04）| 02:24 |
| 28 | AI COPS：开头 `AI Cops are being added!`；COP BEHAVIOR 9 行、WHAT TO EXPECT 3 行；三处引文 `a 3 star system similar to GTA's 5 star system`、`At 3 stars`、`for over 60 seconds` | EV `data[4].description` | CONFIRMED | 9 + 3 行；三处引文子串命中 | 02:23 |
| 29 | HALLOWEEN 时间：start 10-21 22:30 UTC、end 11-01 08:00 UTC、建立 10-06、最后编辑 10-09 22:06 | EV `data[6]` | CONFIRMED | start 2026-10-21T22:30:29、end 2026-11-01T08:00:29、created 2026-10-06T20:52:53、updated 2026-10-09T22:06:45 | 02:23 |
| 30 | HALLOWEEN 原文逐字：`Orange Grass and Trees! 🍂`、三条要点、`Be ready 10 days before halloween! 🛵🎃`；31−10=21 与 start 日一致；读取日窗口未开 | EV `data[6]` | CONFIRMED | 逐字命中；start 在 10-21，晚于 10-10 | 02:23 |
| 31 | 否定：HALLOWEEN 的任务步骤、车名与速度、结束后能否再拿都没写 | 检索 `halloween\|quest` | CONFIRMED | 只在 HALLOWEEN 的 title / description（5 处），无步骤 | 02:24 |
| 32 | 罚款相关记录时间：AVOID FINES 09-21，NEVER PAY FINES 09-26，AI COPS 开始 09-25 22:00（「around the AI COPS start」）| DP `AVOID FINES`.Created；GP `NEVER PAY FINES`.createdTimestamp；EV `data[4]` | CONFIRMED | 2026-09-21T22:55:07；2026-09-26T06:44:16；2026-09-25T22:00:06 | 02:24 |
| 33 | 否定：七条公告没有一条写出价格或现金数额 | 检索 `price\|cost\|robux\|$`、`cash\|money`；通读 | CONFIRMED | 活动语料只命中 AI COPS 的 `costed` 与 `money`（无数字）；其余命中在商品名和游戏描述 | 02:24 |
| 34 | 否定：记录没说 06-04 到 07-23 之间游戏处于什么状态 | 检索 `test\|beta\|alpha` | CONFIRMED | 全语料 0 命中 | 02:24 |
| 35 | 方法说明：零起点游标 3/3 回 7 条且无下一页；不带参数 6/6 只回 1 条 | EV 带 / 不带游标 | CONFIRMED | 零游标 10/10 回 7 条、next 空串；不带参数 02:27 的 10/10 回 1 条（HALLOWEEN）。注意 02:23 的不带参数 10/10 回 7 条，接口不稳定，页内「plain request returned one」只对特定时段成立 | 02:27 |
| 36 | 12 个通行证、23 个商品 | GP `gamePasses` 长度、DP `developerProducts` 长度 | CONFIRMED | 12；23 | 02:24 |
| 37 | 每条活动归 Untitled Wheelie Group 所有 | EV `host.hostName` | CONFIRMED | 7/7 | 02:23 |
| 38 | 页内站内链接目标均为本栏目已发布页或本批新页 | `content/untitled-wheelie-game/en/*.md` | CONFIRMED | bikes、community、cops-fines、gamepasses、money、updates 均 draft: false；cops-chase-rules 为本批新页，无 draft 页被链 | 02:25 |
| 39 | 页内提到的各站内页确实涵盖所述内容（community 谈 testing、gamepasses 有 EBike Pack 描述、money 有 pizza、cops-fines 谈两件罚款商品、bikes 谈 Backfire）| 仓内 md 检索 | CONFIRMED | community.md:62 有 testing server 小节；gamepasses.md:52 有 EBike Pack ⚡；money.md 有 pizza；cops-fines.md 有 NEVER PAY FINES / AVOID FINES；bikes.md 有 Backfire | 02:26 |
| 40 | updates 页「built from the creation dates on game pass and developer product records」 | updates.md 正文表格 | CONFIRMED | updates.md 表格全由通行证 / 商品创建日构成（该页仍写「developer does not publish patch notes on Roblox」，与新页矛盾，已在 old-page-fixes.md #1、#2 列出，不属本页命题）| 02:26 |
| 41 | 页内「Every time on this page is UTC」 | 页面全文 | REFUTED | 反例：同页第 52 行引文 `1:00PM MST (4:00 PM EST)` 是 MST / EST 时间，不是 UTC。草稿原句（第 5 行）：「Every time on this page is UTC.」（其余自写时间均按 UTC 核过）| 02:25 |
| 42 | 首段与 tldr 把这 7 条公告称作「patch notes」/「The developer's patch notes are seven Roblox event announcements」，即这 7 条就是开发者的全部更新说明 | 仅 virtual-events 接口 | UNVERIFIED | 允许的来源里只能看到 7 条活动；无法证明开发者没有在游戏内、Discord 等别处另发更新说明（后者禁止作证）。草稿原句：「Untitled Wheelie Game patch notes exist as seven event announcements the developer created」| 02:25 |
| 43 | 封面 / 正文图 art01 的图注「Official thumbnail · Untitled Wheelie Group (Roblox)」及图片描述（黑头盔骑手、两辆警车、AI COPS 字样、红箭头）| 图片文件（仓内未找到 art01 / art02 文件；AI COPS 活动 `thumbnails[0].mediaId`=98813158422274）| UNVERIFIED | 本机无图片文件，缩略图接口不在 sourceUrls，无法确认 art01 就是该活动缩略图或画面内容 | 02:25 |
| 44 | 公告口径检查：页内所有关于公告内容的句子是否带「announcement says / lists / reads / as written」等限定 | 页面全文逐段 | CONFIRMED | 除命题 41 外未发现把公告内容写成已验证机制的句子；首段、tldr 第 4 条、末节「What is still not confirmed」均声明未实测。表格「What the line leaves open」一列、「reads like something a player switches on」均带「reads like / not confirmed」限定 | 02:25 |

## 机检

1. 外链：正文无 http 外链；frontmatter sourceUrls 四个地址都回 200（见上），且与草稿 sourceUrls 一致。
2. 站内链接：/bikes/、/community/、/cops-fines/、/gamepasses/、/money/、/updates/ 均存在且 draft: false；/cops-chase-rules/ 为本批新页。无 draft 页被链。
3. 不带日期的时间词（now / currently / upcoming / soon / latest / recently / new 指时间）：正文 0 处（命中的 new 全是引文里的 New Map / 2 new bikes / New Trick System 等）。EBIKE 的 `soon` 已转述，正文无 `coming soon` 字样。
4. 兑换码 / 第三方站 / 外挂脚本 / 账号买卖：0 处。
5. 二级发现：updates.md 与 index.md 现行文字仍说「developer does not publish patch notes on Roblox」，与本页矛盾（old-page-fixes.md 已覆盖）。
