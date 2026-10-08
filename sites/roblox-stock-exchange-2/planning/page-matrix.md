# 页面矩阵(Roblox Stock Exchange 2,英文,首批 12 个文件 = 12 页全部发布,0 页草稿)

一个意图一页;同实体组收进同一页。路由规则沿用基准栏目:`/<game-slug>/<slug>/`,首页 `/<game-slug>/`。slug 固定 `roblox-stock-exchange-2`,线上 `https://lootwiki.com/roblox-stock-exchange-2/`。

| # | URL | 页型 | 承接词 | 这一页要回答的问题 | 优先级 | 状态 | 到期动作 |
|---|---|---|---|---|---|---|---|
| 1 | /roblox-stock-exchange-2/ | home | roblox stock exchange 2, … game, … wiki | 这是什么游戏、谁做的、有没有码、我该先看哪一页 | P0 | 发布 | 无硬到期:round1 后活动时间一律写绝对日期;每次复核重读 events 接口 |
| 2 | /roblox-stock-exchange-2/beginner/ | category(Getting Started) | … guide | 新手按什么顺序看这五篇 | P0 | 发布 | — |
| 3 | /roblox-stock-exchange-2/how-to-play/ | article | how to play, tutorial, tips, how to sell, is … realistic | 能交易什么、第一局做什么、怎么买卖平仓、杠杆/手续费/离线官方说了什么 | P0 | 发布 | — |
| 4 | /roblox-stock-exchange-2/codes/ | article(codes 规格) | codes, promo codes, game codes | 官方描述里印着哪个码(未进游戏实测)、描述说下一个码何时放、别站的码为什么不收 | P0 | 发布 | 赞数过 15,000 当天重读描述:新码进 Active,TOOLS 视情况移入 Expired;每月初改 title / seoTitle / description 里的年月;超 7 天未核 = P0 |
| 5 | /roblox-stock-exchange-2/badges/ | article | badges, rebirth | 11 个徽章条件、多少人拿到 | P1 | 发布 | — |
| 6 | /roblox-stock-exchange-2/updates/ | article(事件页) | upd …, custom offices, hedge funds, bonds, seasons | 官方列了哪些更新活动、各自的起止时间与原话 | P0 | 发布 | round1 后标题与首段不含 next / starts 这类时效词(title = Official Event History);2026-10-16 23:00 UTC listing 结束后重读 events / passes / products / badges 四个接口并补记。默认不做 308(常青更新史) |
| 7 | /roblox-stock-exchange-2/community/ | article | discord, wiki, developer | 谁做的、官方 Discord 是不是真的、官方消息在哪看 | P1 | 发布 | — |
| 8 | /roblox-stock-exchange-2/robux/ | category(Passes & Robux Shop) | gamepass, robux | Robux 能买哪几类东西、先看哪篇 | P0 | 发布 | — |
| 9 | /roblox-stock-exchange-2/gamepasses/ | article | gamepass, bundle, max leverage, vip, overnight desk … | 13 个通行证各给什么、bundle 划不划算、哪 4 个当商品卖更贵 | P0 | 发布 | — |
| 10 | /roblox-stock-exchange-2/shop/ | article | ai tokens, trader pass, simulate day, trader spotlight | 31 个商品的名称与价格、哪些有官方说明 | P1 | 发布 | — |
| 11 | /roblox-stock-exchange-2/algo-bots/ | article | bot, bot settings, best bot settings, indicator | bot 官方说了什么、花多少 Robux、为什么没有「官方最佳设置」 | P0 | 发布 | — |
| 12 | /roblox-stock-exchange-2/author/ | author | — | 谁写的、怎么核实、为什么不给交易建议 | P0 | 发布 | — |
| — | /roblox-stock-exchange-2/bot-settings/ | article | best bot settings | 具体参数 | P2 | 不建:无一手来源(合并进 #11) | — |
| — | /roblox-stock-exchange-2/rebirth/ | article | rebirth | rebirth 条件与收益 | P2 | 不建:一手只有徽章一句话 | — |
| — | /roblox-stock-exchange-2/markets/ | article | stocks, etf, futures, ipo, crypto, bonds | 各市场机制 | P2 | 不建:官方只有名称与一句话预告;等进游戏核实 | — |
| — | /roblox-stock-exchange-2/scripts/ | — | script, pastebin | — | — | 不做:外挂 | — |

草稿页说明:本批没有只靠 B/C 来源的页,所以没有 `draft: true` 的文件。P2 三页按「宁可空着不预支产能」处理,连草稿也不生成。

## 首页模块

| 模块 | 承接 | 写什么 | 链到 |
|---|---|---|---|
| 直答首段(58 词) | roblox stock exchange 2 | 一句话说清游戏、开发者、创建日 + 核心循环 | — |
| 官方免责引用 | is it real trading | "All markets and currencies are simulated…" | — |
| Where should a new trader start? | guide | 三个入口 | how-to-play / codes / gamepasses |
| What are the key facts? | wiki | 14 行官方数据表(带读取时刻) | — |
| Is there a code? | codes | TOOLS(官方描述里印着,未实测)+ 15,000 赞门槛 + 还差多少 | codes |
| What has the developer announced beyond the four markets? | game | 描述里的四个市场(正文)+ 5 个活动预告表(明写是预告,不代表已上线) | updates |
| What does Robux buy? | gamepass | 13 通行证 / 31 商品的价格区间与三条硬数字 | robux / algo-bots |
| How far do most players get? | badges | 徽章占比 | badges |
| Which update events has the developer listed? | upd | 12 条活动的起止范围 + Custom Offices 的挂牌开始时间(绝对日期)与原话 | updates |
| Who runs the game? | discord / developer | 群组人数、无 shout | community |
| All sections | — | 两个栏目入口 | beginner / robux |
| How this guide uses its sources | — | 来源口径 + 不是投资建议(末句被 hub_body.scope 抽成范围提示框) | — |
| 自动表(hub_body.tables) | gamepass / badges | 13 行通行证表(名/价/描述)、11 行徽章表 | gamepasses / badges |
| FAQ(frontmatter faq,5 条) | 通用问 | 谁做的 / 有没有码 / 是不是真炒股 / 单服人数 / 最便宜通行证 | community / codes / how-to-play / gamepasses |

事件页:updates(round1 后改为绝对时间口径,不再依赖「到期改过去时」;复核动作见上表与 `entities.json` 的 `event-custom-offices.expiry_action`)。
