# 同类站架构对比(One Tap,2026-10-10 抓取)

只学结构,不抄文字,**不采信其任何数据**(两个站都是以游戏名抢注的新站,按任务口径记 C 级,只能当线索)。每一行都是本人实际打开过的页面(curl 浏览器 UA,原文在 `raw/comp/`);没打开的页只按 sitemap 记 URL,不评价内容。全程未遇到验证码 / 挑战页。

结论:两个抢注站都把「三类武器 + 进阶技巧 + 没有码」当主线,页面短(389–788 词)、几乎没有数据表(8 个已打开页面里只有 2 张表)。**没有一家列出 97 个开发者商品的价格**,也没有一家把 6 条官方活动的原文与 listed start / end 分开写——onetaproblox.wiki 的更新页把活动 **结束** 时间当成更新日(March 21 / May 8 / June 30),与官方 listed start(March 13 / April 24 / June 15)对不上。我们首批把栏目建在这层一手数据上:箱子单价、战令跳层单价、通行证图标原文、6 条活动原文;武器强度榜、瞄准教学、地图这类需要进游戏的内容首批不做。

## 对比表

| 站 | 实际打开的页 | 抓取状态 | 栏目 / 导航 | 页型 | 表格 / 列表 / 图 | 我们取什么 | 我们不取什么 |
|---|---|---|---|---|---|---|---|
| onetap.wiki | 首页;/codes/;/wiki/weapons/;/updates/;sitemap.xml;robots.txt | curl 200(2026-10-10 T3) | 顶部下拉:Codes(Code status / Update watch)、Weapons(Role selector / Weapon guide)、Guides(How to get better 等);面包屑 Home / 栏目;页脚 Core pages / Sources / Site info。sitemap 24 条:codes、tier-list、trello、squad-planner、resource-calculator、guides(beginner / progression / farming / how-to-get-better)、wiki(weapons / progression / items-and-rewards / maps-and-systems / builds-and-entities)、updates、sources + about / contact / privacy / terms / disclosure;lastmod 全部 2026-07-24 | 首页(约 1,190 词,1 个视频 iframe)+ 短内页(codes 约 440 词、weapons 约 600 词、updates 约 390 词)+ 3 个工具页(未打开)+ 单独的 /sources/ 页(未打开) | 已打开的 4 页 0 张表;首页 3 张图;首页 FAQ 4 问;JSON-LD 2–4 段 | 「没有码就明说没有,并写清一个码要出现在哪才算数」的写法(我们放进 hub 的「Why is there no codes page?」一节,不单独建页);把官方链接与来源清单放在显眼位置;首页按三类武器分流 | 套模板留下的空栏目(squad-planner、resource-calculator、trello、farming、builds-and-entities 与这款游戏对不上);tier list(没有任何官方数值可排);码页空着也建一页(总站规格:数据为 0 的项不建页) |
| onetaproblox.wiki | 首页;/codes/;/guides/game-passes/;/guides/updates/;sitemap.xml;robots.txt | curl 200(2026-10-10 T3) | 顶部:Guides(Beginner guide / Aim & settings / Weapons & loadouts / Tips & tricks / Progression & rewards / Cases & cosmetics / Game passes / Updates)、Community & Discord、Codes、FAQ、About、Contact、「Play on Roblox」按钮;面包屑 Home / Guides / 标题;页内 On this page 目录;每页底部「More guides」6 卡。sitemap 16 条;lastmod 2026-09-30 ×11、2026-10-07 ×5 | 首页(约 740 词,三组各 3 卡:New player start here / Get better, faster / Meta & updates)+ 8 篇 guides + codes + community + faq;每页一行「Last verified 日期 · Game version」 | game-passes 页 1 张表(4 个通行证);updates 页 1 张表 + 按日期的 H3 时间线;每页 8–10 张图 | 「栏目少而平」的结构(一组 guides + 少量独立页);每页顶部的复核日期行;页内目录;game passes 用一张总表开头;updates 用时间线(我们按 listed start 排,并把 listing 与实际上线分开写) | 用活动结束时间当更新日;「Lunar event — August 8」这类官方 listing 里不存在的条目;Community & Discord 页(官方一手页面上看不到邀请,我们不写);把通行证效果写成确定句(官方 description 为空,只有图标上的一句话) |
| Fandom | 6 个可能的子域(one-tap / onetap / one-tap-roblox / onetaproblox / fps-one-tap / stringless-banjo)的 api.php | 全部 404(2026-10-10 T4) | — | — | — | — | 没有可用的社区 wiki,B 级来源为 0 |

## 基准栏目的页型(lootlore 仓内,结构照抄的对象)

| 基准 | 文件数 | 页型 | 栏目 | 我们沿用的做法 |
|---|---|---|---|---|
| content/get-your-drivers-license/en(2026-10-09) | 11(全发布) | home / category ×2 / article ×7 / author | Getting Started;Cars & Robux Shop | frontmatter 字段与顺序(逐项一致)、两栏结构、hub 的 key facts 表 + 官方描述逐行表 + 「Why is there no codes page?」+ All sections + How this guide uses its sources、gamepasses / shop 的「官方原文表 + 我们的算术表」、author 页结构、`_images.json` 里「16:9 图不够时用官方方形图标分封面」的做法 |
| content/american-plains-mudding/en(2026-10-09) | 12(全发布) | home / category ×1 / article ×9 / author | Guides | updates 页的「listing 表 + 逐条原文 + 更新日期怎么判断」写法;活动实体(`event-<日期>-<slug>`,type mechanic)的 entities 结构 |
| content/blockspin/en(2026-09-29,2026-10-10 增补) | 15(11 发布 + 4 draft) | 同上 | Getting Started;Money & Gear | robux-shop 页「商品记录没有描述时只印名称 / 价格 / 记录日期,功能标 not confirmed,分组注明 ours」的口径——One Tap 97 个商品全部没有描述,整栏沿用这个口径;scope 字段的写法 |
| content/deep-fishing/en(2026-09-29) | 15(14 发布 + 1 draft) | 同上 | Getting Started;Rods & Upgrades | hub 页官方来源 0 个码时不建 codes 页的写法;商品创建日时间线 |
| content/valheim/en | 多语种 wiki 型 | boss / biome / item 等实体页 | 多栏 | 只对照了 entities.json 的字段级 `*_source` 约定与 `page_slug` 绑定方式;One Tap 没有可逐件建页的实体数据(武器 / 皮肤无名单),不做实体页 |

## 我们采用的栏目结构

| 栏目(category) | slug | 首批文章 | 首发状态 | 说明 |
|---|---|---|---|---|
| Home | index | hub 首页 | 发布 | 通用词落地 + 分流;key facts 表 + 官方描述十行表 + 活动一览表;FAQ 6 条 |
| Getting Started | beginner | how-to-play、rewards、updates、game-info | 全部发布(都有 S 级来源) | 怎么玩 / 奖励来源 / 更新史 / 谁做的与平台 |
| Cases & Robux Shop | robux | gamepasses、cases、battle-pass、shop | 全部发布(都有 S 级来源) | 花 Robux 之前要看的四页:通行证、箱子、战令、全店 |
| Author | author | 作者页 | 发布 | E-E-A-T;写明哪些内容等进游戏核实 |

## 我们比它们厚在哪、准在哪

1. **全店价格**:97 个开发者商品逐条来自 Roblox 接口,分 13 组,每组给计数、价格范围、小计。两个抢注站都没有。
2. **箱子单价与「多买不便宜」**:16 个系列里 14 个各档单价相同;Energy Sword 多买便宜(199 → 150),Karambit 多买反而贵 1 Robux / 个(450 对 3×149=447)。全部是官方价格上的算术。
3. **名为 Premium Battlepass / Skip 的 7 条记录的价格**:按名称里的层数相除,Skip One Tier 与 Skip Five Tiers 都是 20,Skip Three Tiers 约 59.7,Skip Ten Tiers 85;Skip All 600。7 条都没有描述,「跳几层」是名称读法(round1 U3–U7 后页面全部加了限定,不再写值不值)。
4. **通行证只引图标原文**:4 个通行证 description 为空,我们逐字抄图标上的句子(如 2x Case Luck 图标写的是 "more luck",不是翻倍),并明说其余没有官方说明。
5. **更新史按 listed start,并把 listing 与实际上线分开**;商品记录创建日与活动并排;`updated` 字段两个接口两个值,不当更新日。
6. **不编**:没有武器数值、没有 tier list、没有箱子概率、没有码页、没有 Discord 邀请。
7. **不做**:script / 外挂 / 刷号(官方描述明写永久封禁);把商品名与任何第三方作品挂钩。
