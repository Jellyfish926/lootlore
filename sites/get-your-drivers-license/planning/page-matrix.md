# 页面矩阵(Get Your Driver's License!,英文,首批 11 个文件 = 11 页全部发布,0 页草稿)

一个意图一页;同实体组收进同一页。路由规则沿用基准栏目:`/<game-slug>/<slug>/`,首页 `/<game-slug>/`。slug 固定 `get-your-drivers-license`,上线后是 `https://lootwiki.com/get-your-drivers-license/`。搜索量一律「未获取(自动任务不查 Semrush)」,优先级按官方描述的功能线顺序与同品类站页型排,不按搜索量排。

| # | URL | 页型 | 承接词 | 这一页要回答的问题 | 优先级 | 状态 | 到期动作 |
|---|---|---|---|---|---|---|---|
| 1 | /get-your-drivers-license/ | home | 游戏名、roblox drivers license game、wiki、codes(一节) | 这是什么游戏、谁做的、一局几步、Robux 买什么、为什么没有码页 | P0 | 发布 | 无硬到期;每次复核重读 games / votes / group 接口并同步页内时刻 |
| 2 | /get-your-drivers-license/beginner/ | category(Getting Started) | guide、beginner | 新手按什么顺序看这四篇 | P0 | 发布 | — |
| 3 | /get-your-drivers-license/how-to-play/ | article | how to play、written test(只到「有笔试」) | 一局有哪几步、商品描述透露了什么、第一局怎么打、别人能不能捣乱、是否免费 | P0 | 发布 | 进游戏核实后补:笔试形式、一局实测时长 |
| 4 | /get-your-drivers-license/waiting-line/ | article | skip line、skip time、skip to end、kill、kill all | 队怎么排、5 个跳过商品各多少钱、哪种情况买哪个、[SALE] 是不是真折扣 | P0 | 发布 | 价格变动时改表与算术;核实 Skip To End 是否连笔试一起跳 |
| 5 | /get-your-drivers-license/driving-test/ | article | driving test、endings、honor roll、towed、retake test、examiner | 考场上有什么、官方点名了哪两个结局、挂了怎么办、当考官多少钱 | P0 | 发布 | 拿到结局全表后把结局拆成 /endings/(本页留摘要 + 链接) |
| 6 | /get-your-drivers-license/community/ | article | discord、developer、time will pass、wiki | 谁做的、还做了什么、有没有官方 Discord、官方消息在哪看 | P1 | 发布 | 群组出现 shout / description 或官方活动时重写「Where would official news appear?」 |
| 7 | /get-your-drivers-license/robux/ | category(Cars & Robux Shop) | robux、gamepass | Robux 能买哪几类东西、先看哪篇 | P0 | 发布 | — |
| 8 | /get-your-drivers-license/cars/ | article | cars、all cars、secret、golden supercar、vip ticket、epic | 官方对车说了什么、档位怎么分、两个车类商品哪个值 | P0 | 发布 | 拿到 18 辆车名与档位后在本页加车表(标核实日期) |
| 9 | /get-your-drivers-license/gamepasses/ | article | gamepass、ban hammer、gravity gun、airhorn、time out | 5 个通行证各做什么、Ban Hammer 值不值、有没有通行证能帮你过考 | P0 | 发布 | 新通行证出现时加行 |
| 10 | /get-your-drivers-license/shop/ | article | robux、shop、scare all、revenge、be the examiner | 13 个商品的名称 / 价格 / 官方描述、四组小计、上架后新增了什么 | P0 | 发布 | 新商品出现时加行并更新「What was added after the first batch?」 |
| 11 | /get-your-drivers-license/author/ | author | — | 谁写的、怎么核实、哪些故意不写 | P0 | 发布 | — |
| — | /get-your-drivers-license/codes/ | article(codes 规格) | codes | 现在能用的码 | — | 不建:官方来源 0 个码 | 开发者在描述或群组里印出码的当天建页 |
| — | /get-your-drivers-license/written-test/ | article | written test answers | 笔试题目与答案 | P2 | 不建:0 来源,等进游戏核实 | — |
| — | /get-your-drivers-license/endings/ | article | all endings | 全部结局与触发条件 | P2 | 不建:一手只有 2 个名字,先并进 #5 | — |
| — | /get-your-drivers-license/badges/ | article | badges | 徽章 | — | 不建:官方徽章 0 个 | 出现徽章时建页 |
| — | /get-your-drivers-license/updates/ | article | update | 更新史 | P2 | 不建:官方活动 0 条 | 出现第一条官方活动时建页 |

草稿页说明:本批没有只靠 B/C 来源的页,所以没有 `draft: true` 的文件(11 页全部至少有 1 个 S 级来源)。P2 的 written-test / endings 按「宁可空着不预支产能」处理,连草稿也不生成;要进游戏核实的条目见 `todo-ingame.md`。

## 首页模块

| 模块 | 承接 | 写什么 | 链到 |
|---|---|---|---|
| 直答首段(58 词) | 游戏名 | 一句话说清游戏、开发者、创建日 + 官方描述列出的五件事(不写成一局的固定顺序) | — |
| 官方口号引用 + 本站边界 | — | "Wait in line and get your Driver's License!";说明没有亲自跑过考场 | — |
| Where should a new driver start? | guide | 三个入口 | how-to-play / waiting-line / cars |
| What are the key facts? | wiki | 14 行官方数据表(带读取时刻) | — |
| What does the official description list? | how to play | 5 行功能表(官方原句 + 对应攻略)+ 考官一句;注明这是功能清单,没说每局都走完、每局都给车 | waiting-line / how-to-play / driving-test / cars |
| What does Robux buy? | gamepass / robux | 5 通行证与 13 商品的价格区间与分工 | robux / gamepasses |
| What was added after launch? | update | 5 行上架时间线(商品 / 通行证创建时刻 + Golden Supercar 🏆 10-05 被编辑) | — |
| Why is there no codes page? | codes | 2026-10-09 读过的三个官方位置(游戏描述 / 群组描述 / 群组 shout)都没有码 | — |
| Who runs the game? | discord / developer | 群组创建日、5 个体验 | community |
| All sections | — | 两个栏目入口 | beginner / robux |
| How this guide uses its sources | — | 来源口径(末句被 hub_body.scope 抽成范围提示框:哪些内容没写、为什么) | — |
| 自动表(hub_body.tables) | shop / gamepass | 13 行商品表(名 / 价 / 描述)、5 行通行证表 | shop / gamepasses |
| FAQ(frontmatter faq,6 条) | 通用问 | 谁做的 / 有没有码 / 几辆车 / 单服人数 / 最便宜的东西 / 能不能跳过排队 | community / cars / shop / waiting-line |

事件页:本批没有(官方活动 0 条)。
