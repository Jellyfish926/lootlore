# 同类站架构对比(Roblox Stock Exchange 2,2026-10-08 抓取)

只学结构,不抄文字。页数取各站 sitemap.xml 或页面实测;抓不到的标「未获取」。

结论:对手分两类——**码页**(Roblox Den / Try Hard Guides / Twinfinite / Pro Game Guides 等,更新勤,全是码表,彼此奖励数字对不上、无开发者出处)和**一个 5 页的小 wiki**(robloxstockexchange2.wiki,口径克制但很薄:0 张表、没有通行证/商品/更新史、徽章漏 1 个、码页不做)。**没有任何一家用上 Roblox 官方接口里的通行证描述、开发者商品、活动 listing 与徽章获得数。** 我们的栏目按「codes + 新手 + 徽章 + 更新史 + 社区」与「通行证 + 商店 + algo bots」两栏做,全部建在一手数据上。

## 对比表

| 站 | 抓取状态 | 页数 | 栏目 / 导航 | 主要页型 | 表格 / 信息框 | 数据口径 | 明显短板 |
|---|---|---|---|---|---|---|---|
| robloxstockexchange2.wiki | 200(curl) | 5(sitemap:/、/beginner-guide、/trading-orders、/progression-rebirth、/faq) | Beginner Guide / Trading Orders / Progression / FAQ | 首页(766 词)+ 3 篇指南(324–431 词)+ FAQ(370 词,7 问) | 0 张 `<table>`;卡片式编号步骤;无信息框 | 以官方描述 + 徽章名为锚,自述「不写未核实的码、收益、rebirth 成本」;界面标签来自一段 captured gameplay | 没有通行证、商品、价格、更新史;徽章只列 10 个(漏 Met the game owners!);没有任何数字;FAQ 称「未核实任何码」(官方描述里其实有 TOOLS) |
| Roblox Den /game-codes/roblox-stock-exchange-2 | 200 | 1 | 单页 | codes 数据库页:码表 + How to claim | 1 张表(码/说明/状态/用户投票);7 active、0 expired | 「Last checked 10/07/2026」;靠用户 Works / Doesn't work 投票 | 无开发者出处;奖励与别站打架 |
| Try Hard Guides /stock-exchange-2-codes/ | 200 | 1 | 单页 | codes 单页;H2:All Codes / How to Redeem / How to Get More / Why Not Working / When Released | 0 张表(列表) | 2026-09-29;链了群组与 Discord | 多数码奖励只写「Cash」 |
| Twinfinite /codes/roblox-stock-exchange-2-codes/ | WebFetch 可读;curl 403 | 1 | 单页 | codes 单页;H2 两个 | 列表 | 「Updated: Oct 1, 2026」 | 不含官方描述里的 TOOLS |
| Pro Game Guides /roblox/roblox-stock-exchange-2-codes/ | WebFetch 可读;curl 403 | 1 | 单页 | codes 单页;H2:Active Codes / How to Redeem / What Does Cash Do / More Codes | 列表 | 2026-09-07 | 一个月没更新;不含 TOOLS |
| nerdschalk / allthings.how / gamertweak / mrguider / earnaldo 的码页 | 只在搜索结果里见到标题,未读取 | 各 1 | — | codes 单页 | 未获取 | 未获取 | — |
| rotrends.com/game/10495391267 | 只在搜索结果里见到,未读取 | 1 | — | 数据统计页 | 未获取 | 未获取 | — |
| Fandom | 五个可能的子域(roblox-stock-exchange-2 / robloxstockexchange2 / roblox-stock-exchange / robloxstockexchange / rse2 .fandom.com)api.php 全部 404 | 0 | — | — | — | — | 没有 Fandom wiki |

## 基准栏目的页型(lootlore 仓内,结构照抄的对象)

| 基准 | 文件数 | 页型 | 栏目 | 我们沿用的做法 |
|---|---|---|---|---|
| content/blockspin/en | 12(7 发布 + 5 draft) | home / category / article / author | Getting Started(codes、beginner、game-info、cheats-bans);Money & Gear(全 draft) | codes 页格式(frontmatter `codes[]` + Active / Expired 两表 + 为什么不抄别站 + redeem + 排障);entity 绑定;author 页 |
| content/deep-fishing/en | 12(11 发布 + 1 draft) | home / category ×2 / article / author | Getting Started(how-to-play、rarity、badges、discord);Rods & Upgrades(rods、gamepasses、shop) | 两栏结构;badges 页的 Share 计算;gamepasses / shop 页的官方描述表;hub 首页 at-a-glance 表 + All sections + How this guide uses its sources;`gameVersion` 字段 |
| content/stone-skipping、race-horses、southern-mudding/en | 11–13 | 同上 | 各 1–2 栏 | updates 页(virtual-events 带游标取数、时区换算表、store 创建日时间线、到期动作写进 scope);community 页(官方位置逐一核对表、Discord 口径) |

## 我们采用的栏目结构

| 栏目(category) | slug | 首批文章 | 首发状态 | 说明 |
|---|---|---|---|---|
| Home | index | hub 首页 | 发布 | 通用词落地 + 分流;key facts 表 + markets 表;FAQ 5 条 |
| Getting Started | beginner | how-to-play、codes、badges、updates、community | 全部发布(都有 S 级来源) | 通用词入口:怎么玩、码、徽章、更新、Discord/开发者 |
| Passes & Robux Shop | robux | gamepasses、shop、algo-bots | 全部发布(都有 S 级来源) | 个性词入口:gamepass 值不值、Robux 商品、bot(best bot settings 的诚实回答) |
| Author | author | 作者页 | 发布 | E-E-A-T;写明「不是投资建议」 |

## 我们比它们厚在哪、准在哪

1. **通行证**:13 个通行证的官方描述里有硬数字(0.02% 手续费、50x 杠杆、离线 24h vs 8h、公司 5 vs 2、8 个指标、10×50 自选)。竞品 0 家列出。
2. **商店**:31 个开发者商品的官方名称与价格,含与通行证同名却不同价的 4 个(VIP 229 vs 399 等)——玩家真金白银会踩的坑,竞品没有。
3. **更新史**:12 条官方活动 listing(标题、原话、起止时间)+ 配图里的细节(对冲基金四策略、挑战四档、赛季周一清零、债券三档)。竞品没有;「upd roblox stock exchange 2」是下拉词。
4. **徽章**:11 个徽章的累计与昨日获得数,能说清「90% 下过单、27% 做过空、2% 有 bot / rebirth」。小 wiki 只列了 10 个名字。
5. **码页**:只收官方描述里亲眼看到的 TOOLS,并把「15,000 赞出下一个码、现在差多少」算出来;把码站互相矛盾摆出来而不是照抄。
6. **不做**:script / pastebin(外挂)、best bot settings 的具体参数(无一手来源)、tier list、「method / strategy」类赚钱法(无一手依据且容易写成投资建议)。
