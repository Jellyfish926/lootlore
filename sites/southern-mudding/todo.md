# 待办：需进游戏核实的事项 + 未获取项

取数时点：2026-10-02 11:19–11:24 UTC。全部正文描述的是 **9 月 25 日版本**。

## 0. 最急：10-02 更新落地后重取（当天）

官方活动「This Week's Update!」排在 2026-10-02 17:00:46 UTC 开始，晚于本次取数约 5 小时 40 分。上线前（或上线当天）必须：

1. 重取 `games`（name 前缀、description 的更新说明、updated）、`virtual-events`、`developer-products`、`game-passes`、`badges`。
2. 若描述换成了新的更新说明：updates.md 追加一节并把 Nitrous 一节改成过去时；index.md「What did the 25 September update add?」一节同步；nitrous.md 首段的「currently starts with [🚀Nitrous!🚀]」核对；全部页 `gameVersion` 改成新日期。
3. 9-30 创建的「[Limited] Off-Road 6x6 Pickup Truck」是否写进了新说明——写了就把 updates.md / limiteds.md 里「nothing official says so yet」改成事实。
4. entities.json 的 3 条活动实体带 `expiry_action`；`event-nitrous-update` 在 10-02 17:00 UTC 到期。
5. 徽章累计数、访问量、群组人数、RSVP 都是快照，重取后同步 index / badges / community / how-to-play / spawning / nitrous / updates 里的数字（dossier 第 11 节有逐页对应表）。

## 1. 需进游戏核实（公开接口没有，正文已写成 not shown in public data / needs an in-game check）

| # | 事项 | 影响的页 | 现在正文怎么写的 |
|---|---|---|---|
| 1 | 操作按键（PC / 手柄 / 触屏），生成、车库、领房菜单在哪 | how-to-play | 列为未知 |
| 2 | 免费可生成的车辆与拖车名单 | how-to-play、vehicles、spawning | 「Not listed in public data」 |
| 3 | 游戏币叫什么、怎么赚、车辆的游戏币价 | index、how-to-play、vehicles | 列为未知；没有 money 页 |
| 4 | 群组赠送的是哪辆皮卡、进游戏后在哪、是否要重进 | community、how-to-play、vehicles | 只引官方一句；「leave and rejoin」写明是一般经验 |
| 5 | 氮气：触发键、是否收游戏币、是否耗尽/补充、除皮卡外能不能装、名称带 Pickup Truck 的 Robux 车能不能装 | nitrous | 逐条列在「What should you check in game?」 |
| 6 | LED Whip Lights、rock lights 在改装菜单的位置与价格；Rock Lights Customization 通行证到底解锁什么（接口描述为空） | nitrous、gamepasses | 写「no description in the API」「likely cosmetic」 |
| 7 | Portable Customization 能否在车库外加氮气 | nitrous | 写 likely，标推断 |
| 8 | 槽位界面：默认显示几格；Any Slot Spawning 是否等于「4 格随便放」；与两个 Spawn 4 通行证是否叠到 8 | spawning、gamepasses | 写「our interpretation of a single sentence」 |
| 9 | 拖车怎么挂 / 摘；哪些车能拖哪些拖车；超上限再生成会不会顶掉旧车 | spawning | 列为未知 |
| 10 | 载具是否只能在固定点生成（Portable Trailer Spawner 的存在只是暗示拖车如此） | spawning | 写 suggests |
| 11 | 房屋：数量、位置、能做什么、领取是否跨会话保留；普通房是否免费（Luxury Houses 措辞只是暗示） | badges | 写 inference |
| 12 | 22 个 Robux 载具当前在游戏内商店是否还摆着（接口 IsForSale 61 个全 true，不能说明游戏内是否展示） | limiteds | 写「cannot confirm it from public data」；不写回归时间 |
| 13 | 4 个名称含 UTV、6 个 6x6 皮卡商品是不是各自不同的车 | limiteds、vehicles | 写「suggests separate vehicles… cannot prove it」 |
| 14 | 5 个车辆包里各有哪些车（接口只给数量与类别） | gamepasses、vehicles | 写「not named in the pass data」 |
| 15 | 9-25 的 New Pickup Truck / New UTV 叫什么、怎么获得（那一周没有新建 Robux 商品） | vehicles、nitrous、updates | 写 needs an in-game check |
| 16 | 龙卷风：效果、范围、是否自然生成、Storm Chaser Vehicle 有无特殊作用 | limiteds | 写 not shown in public data |
| 17 | Delivery Event Unlock Now：与 2026-02-13 的 Trucking Event!（「Deliver cargo to unlock a new truck.」）的关系是按日期推断的；解锁的是哪辆车、商品现在是否还有效 | limiteds | 写 likely… our inference from the dates… need an in-game check |
| 18 | 礼物商品怎么选收礼人；礼物价与通行证价不一致时游戏内实际显示哪个价 | gamepasses、limiteds | 写「Check the price shown in game」 |
| 19 | 游戏里有没有兑换码输入框 | community、index | 写 needs an in-game check |
| 20 | 商品「Deluxe Trailer Pack」（无 Gift 字样）是否就是礼物版 | gamepasses | 写 likely，标推断 |
| 21 | 支持设备（PC / 手机 / 主机） | how-to-play | 没写（接口 401、描述没提） |
| 22 | 地图地点、设施（下拉有「southern mudding map」需求） | 未建页 | P2，核实后建 map 页 |

## 2. 未获取项与原因

| 项 | 原因 | 后续 |
|---|---|---|
| 群组 wall | 公开接口返回 404 + 空错误体（不能证明是「匿名不可读」） | 是否登录后可读未验证；按边界本轮不取 |
| 游戏 / 群组 social-links（官方 Discord、X、YouTube） | 匿名 401；官方文档写明只对已验证年龄 ≥16 岁的账号可见 | 站主用**已做年龄验证（16+）**的账号看游戏页社交链接，确认后 community 页可写成官方 |
| Discord 公告、X 帖子（A 级来源） | 需登录 | 同上；拿到后历史更新说明、码的有无都能补 |
| 单个活动详情（`/virtual-events/<id>`）、place 详情 | 401 | 列表接口已够用 |
| 9-25 之前各周的更新说明**全文** | 描述只留当期；活动列表有 43 条每周标题（第 2 轮已取，带 cursor 参数翻页），但没有全文 | 之后每周五取一次描述存档，自己攒历史 |
| 搜索量 / KD | Semrush 按任务边界未用 | 只有 Google 下拉（`raw/suggest.txt`） |
| Roblox 游戏页 HTML | 未抓（接口已覆盖同样字段） | — |
| 第三方专站事实 | 按规则只当线索，本轮**一条都没用**，只记了栏目结构（benchmark.md） | — |

## 3. 接入时要处理的小项

1. 3 个商品名在接口里带尾部空格（`Gift 6x6 Pickup Truck `、`(Limited Special Offer) Gooseneck Camper + Truck `、`(GIFT Special Offer) Gooseneck Camper + Truck `）。正文与 `name_en` 去了尾空格，原串在 entities.json 的 `name_raw`。验证员逐字比对时请按 strip 后比。
2. 前序硬门记「通行证 14（另有 Placeholder）」，实测是 14 条 = 13 在售 + 1 条 Placeholder。全站写 13。
3. 宣传图 CDN 地址带 `180DAY-` 前缀，建议 60 天内重跑 thumbnails 接口刷新 `_images.json`。
4. 首批 12 页同一天日期；按规范应错开发布。建议首日发 index / guides / author / how-to-play / updates / gamepasses / limiteds / community（P0），其余 4 篇（vehicles / spawning / nitrous / badges，P1）隔天或隔周翻正——如要分批，把这 4 篇暂设 `draft: true` 并改发布日。
5. `config-snippet.json` 的 `game` 对象追加进 `config/hub.json` 的 `games[]`；i18n 不需要新增键。
6. 独立对抗验证尚未做（本轮只有产出方自检）。按规范 entities.json 与正文翻正前要过一轮 `adversarial-verify`。

## 4. 自检记录（2026-10-02）

- 在 `raw/_buildcheck/` 里放了一份总站仓副本（不含 .git，不动 `$SP/repos/`），把内容包与 config 项放进去实跑：`build.py` 生成 southern-mudding 13 页（12 页 + all）、草稿 0、无构建警告；`check_content` 0 阻塞 0 警告；`check_sitemap` 0 阻塞；`link_check` 无死链；`check_ga` 0 错误；`tech_audit --prefix /southern-mudding`：title 全在 30–60、canonical / JSON-LD / OG / alt 无缺。副本验完已删，脚本留在 `raw/`。
- `raw/selfcheck.py`：12 页 frontmatter 字段齐、title / seoTitle 40–60、description 140–160、首段 40–60 词、每页站内链接目标 ≥3 且文件存在、tldr 3–4 条、禁用套话 0、真实车厂名 0、表内名称对应价格与接口一致。
- `raw/verify_verbatim.py`：111 行表格行的名称 / 价格 / 描述 / 创建日与 `raw/` 逐项比对通过；正文与 frontmatter 里的引号内文字逐条在接口原文里查到（剩余未命中的都是我们自己的术语，如 "Per 100 Welcome"）。
- 图片：`_images.json` 15 个 URL 写入前逐个 curl 验 200（image/Png）。
- 兑换码：全包 0 个。第三方站内容：0 条。

## 5. 第 2 轮（对抗验证 F01–F19）处理记录（2026-10-02 12:11–12:40 UTC）

- F01–F19 全部已改，逐条改前 / 改后见 `raw/round2_edits.json`；updates.md 整页重写（旧版在 `raw/en_round1_backup/`）。
- 43 条活动自己重取成功，但**走的不是验证员给的 URL**：`?eventStatus=completed` 我这边连试多次只回 3 条；改用 `?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA`（自己构造的起始游标）翻 2 页取到 24 + 19 = 43 条，id 与验证员存档一致。接口为什么对两边行为不同，没查明。**以后每周重取活动列表要用 cursor 这条路**。
- 周五开始时间分布我数到 20 / 3 / 14 / 1 / 3（17:00–17:29 / 17:30–17:59 / 18:00–18:29 / 18:30–18:59 / 19:30+），与验证员一致；近 10 条 9 条在 17:00–17:15，一致。
- 新增了 7 个 Roblox 官方文档来源（dossier 第 13 节），把原来几句「平台通用机制」换成了文档原话或删掉。
- 仍未解决（需要人或登录态）：见第 1、2 节——social links 要 16+ 年龄验证账号；群组 wall；全部「需进游戏核实」项；`winRatePercentage` 字段没有官方定义；「访问量」的统计口径没有官方出处。
- updates.md 现在约 1,550 词（43 行活动表撑的），略超「内页 800–1500 词」上限；没有为了卡线砍表。
- 实体数 82 → 122（43 条活动全部建了实体，3 条在开的保留原 id）。
- 自检：selfcheck 全过（title / seoTitle 40–60、description 140–160、首段 40–60 词、内链目标 ≥3、无码、无车厂名）；verify_verbatim：89 行商品 / 通行证 / 徽章表格行 + 50 行活动表格行对账通过，135 处引号文字都能在接口或官方文档原文查到（剩 13 条未命中全是我们自己的术语或步骤序号，同第 1 轮）；仓副本重建 13 页、check_content / check_sitemap / link_check 0 阻塞，副本已删。
- 一次操作失误已清理：重建副本时 `rsync` 不存在导致 `cd` 失败，后续 `mkdir/cp` 落到了 `/home/claude/content/` 与 `/home/claude/data/`（都是本内容包的副本）。发现后立刻删掉了这两个目录，`$SP/repos/` 未受影响（git status 干净）。

## 6. 第 3 轮（复验 G1–G3）处理记录（2026-10-02）

- G1 vehicles.md、G2 community.md（表格 + scope）、G3 updates.md 按验证员替换句改完；另把 index.md 里同一句「a Discord server needs an account」同步成 G2 口径。逐条见 `raw/round3_edits.json`。
- 复验确认活动接口行为随时间变过：现在不带参数、`?eventStatus=completed`、`?cursor=…` 都能取到 43 条。
- selfcheck 重跑全过；description 与首段词数未变（updates / community description 仍 160，badges 首段仍 60 词）。
