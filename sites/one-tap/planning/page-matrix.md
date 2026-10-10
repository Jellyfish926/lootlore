# 页面矩阵(One Tap,英文,首批 12 个文件 = 12 页全部发布,0 页草稿)

一个意图一页;同实体组收进同一页。路由规则沿用基准栏目:`/<game-slug>/<slug>/`,首页 `/<game-slug>/`。slug 固定 `one-tap`,上线后是 `https://lootwiki.com/one-tap/`。搜索量一律「未获取(本任务不查 Semrush)」,优先级按下拉实测与一手素材厚度排,不按搜索量排。

| # | URL | 页型 | 承接词 | 这一页要回答的问题 | 优先级 | 状态 | 到期动作 |
|---|---|---|---|---|---|---|---|
| 1 | /one-tap/ | home | one tap roblox、game、wiki、codes(一节) | 这是什么游戏、谁做的、官方描述列了什么、Robux 买什么、发过哪些更新、为什么没有码页 | P0 | 发布 | 无硬到期;每次复核重读 games / votes / group / events 接口并同步页内时刻与活动表 |
| 2 | /one-tap/beginner/ | category(Getting Started) | guide、beginner | 新手按什么顺序看这四篇 | P0 | 发布 | — |
| 3 | /one-tap/how-to-play/ | article | how to play、gameplay、sniper / secondary / melee、ban、(how to scope / aim、bots:只列为未说明) | 玩法定位、三类武器的官方规则、能解锁装备什么、Update 2 提到的对局功能、第一局怎么打、什么会被封 | P0 | 发布 | 进游戏核实后补:操作与开镜、对局计分、地图名、是否有 bot |
| 4 | /one-tap/rewards/ | article | quests、daily、levels、leaderboard、xp boost、refresh quest | 三个奖励来源、活动里点名的奖励、Xp Boost 四档价格、2x Level XP 与 boost 的比价、排行榜奖励 | P0 | 发布 | 新活动点名新奖励时加行;价格变动时改表与算术 |
| 5 | /one-tap/updates/ | article | update、update 2、summer update、valentines、revert、lunar update | 6 条官方活动的标题 / 时间 / 原文、每条前后新建了哪些商品记录、最后一次更新怎么判断 | P0 | 发布 | **事件页**:virtual-events 出现第 7 条 listing 当天加行并改 hub 的活动表与 FAQ;每次复核带游标重读(不带游标返回 0 条) |
| 6 | /one-tap/game-info/ | article | discord、developer、stringless banjo、xbox / playstation / mobile、server size、badges | 谁做的、支持哪些平台、单服几人、多少人玩、分级、语言、有没有官方 Discord、有没有徽章 | P1 | 发布 | 群组出现 shout 或 social links 可读时重写 Discord 一节;每次复核重取快照数字 |
| 7 | /one-tap/robux/ | category(Cases & Robux Shop) | robux、shop | Robux 能买哪几类东西、先看哪篇 | P0 | 发布 | — |
| 8 | /one-tap/gamepasses/ | article | gamepass、2x money、2x case luck、2x xp、double voting value | 4 个通行证的价格与图标原文、各自能确认什么、合计多少、先买哪个 | P0 | 发布 | 新通行证出现或 description 被填上时改表 |
| 9 | /one-tap/cases/ | article | cases、case prices、karambit / energy sword / proto / cosmic / glitched / moon case 等 | 49 个 Case 商品的价格、16 个系列的单价、多买是否便宜、哪些像箱子但未确认 | P0 | 发布 | 新箱子系列出现时加行(看 developer-products 的 Created);价格变动时改两张表与 Karambit / Energy Sword 的算术 |
| 10 | /one-tap/battle-pass/ | article | battle pass、premium battlepass、skip tiers | 接口里名为 Premium Battlepass 与 Skip* 的 7 条记录的名称 / 价格 / 日期;按名称里的层数做的除法(标明是名称读法);两条赛季公告原文。round1 后不再回答「值不值」 | P0 | 发布 | 进游戏拿到层数与赛季结束日后补一节;新 listing 提到新赛季时加行 |
| 11 | /one-tap/shop/ | article | robux shop、gems、sun points、bundle、starterpack、limited、donation | 97 个商品分 13 组的计数 / 价格范围 / 小计,Gems、Sun Points、Bundle、Limited、Donation 各表,读取方法与未确认项 | P0 | 发布 | 每次复核重读 developer-products:条数、合计 43,177、13 组小计、最常见价格、已编辑条数都要重算 |
| 12 | /one-tap/author/ | author | — | 谁写的、怎么核实、哪些故意不写 | P0 | 发布 | — |
| — | /one-tap/codes/ | article(codes 规格) | codes | 现在能用的码 | — | 不建:官方来源 0 个码 | 开发者在描述、群组 description / shout 或活动文本里印出码的当天建页(title / description / 正文带当月年月) |
| — | /one-tap/skins/ | article | skins、all skins | 皮肤清单与获取方式 | P2 | 不建:官方无名单,等进游戏核实 | — |
| — | /one-tap/weapons/ | article | weapons、best gun | 武器表与数值 | P2 | 不建:0 个官方数值 | — |
| — | /one-tap/maps/ | article | maps | 地图清单 | P2 | 不建:无图名 | — |
| — | /one-tap/aim-settings/ | article | how to scope、how to aim | 开镜 / 瞄准 / 设置 | P1(下拉有需求) | 不建:0 来源,需进游戏实测并自截图 | 实测后建页,首批最值得补的一页 |
| — | /one-tap/badges/ | article | badges | 徽章 | — | 不建:官方徽章 0 个 | badges 接口出现第一条时建页 |

草稿页说明:本批没有只靠 B/C 来源的页,所以没有 `draft: true` 的文件(12 页里 9 页直接引用 S 级来源,3 页是栏目索引 / 作者页,事实全部来自子页)。P1/P2 的 aim-settings / skins / weapons / maps 按「宁可空着不预支产能」处理,连草稿也不生成;要进游戏核实的条目见 `todo.md`。

## 首页模块

| 模块 | 承接 | 写什么 | 链到 |
|---|---|---|---|
| 直答首段(58 词) | 游戏名 | 一句话说清游戏、开发者、创建日 + 三条武器规则 + 单服 8 人 | — |
| 官方口号引用 + 本站边界 | — | "Boom Headshot!" 与官方一句话定位;说明没有进对局核实 | — |
| Where should a new One Tap player start? | guide | 四个入口 | how-to-play / rewards / cases / updates |
| What are the key facts about One Tap? | wiki | 17 行官方数据表(带读取时刻 11:39 UTC) | — |
| What does the official description list? | how to play | 10 行功能表(官方原句 + 对应攻略);注明是功能清单,没说怎么计分、奖励值多少 | how-to-play / shop / cases / rewards / game-info |
| What does Robux buy in One Tap? | gamepass / robux | 4 通行证与 97 商品的价格区间与分工;商品全部没有描述 | robux / gamepasses / battle-pass |
| What has the developer posted about updates? | update | 6 行活动表(标题 + listed start) | updates |
| Why is there no codes page? | codes | 2026-10-10 读过的官方位置(游戏描述 / 群组描述 / 群组 shout / 6 条活动)都没有码 | — |
| Who makes One Tap? | discord / developer | 群组创建日与一句话简介 | game-info |
| All sections | — | 两个栏目入口 | beginner / robux |
| How this guide uses its sources | — | 来源口径(末句被 hub_body.scope 抽成范围提示框:哪些内容没写、为什么) | — |
| 自动表(hub_body.tables) | gamepass / shop | 4 行通行证表(名 / 价 / 图标原文)、商品表前 15 行(名 / 价 / 备注) | gamepasses / shop |
| FAQ(frontmatter faq,6 条) | 通用问 | 谁做的 / 有没有码 / 主机能不能玩 / 单服人数 / 通行证价格 / 最近一条官方更新 | game-info / gamepasses / updates |

事件页:updates(到期动作见上表 #5)。
