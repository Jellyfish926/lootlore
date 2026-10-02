# 同类站架构对比（+1 Stone Skipping）

抓取日 2026-10-02（UTC 11:21–11:23；sitemap + 首页 + 每站 3–4 个内页，原始 HTML 见 `raw/comp/`）。**只记架构，不抄文字，不抄它们的码 / 区域名 / 概率。**

## A. 三个第三方专站（C 级，只当线索）

| 站 | sitemap `<loc>` 数 | 栏目 / 目录 | 主要页型 | 表格 / 结构化 | 数据口径（它们自己的说法） | 样本页里看到的短板 |
|---|---|---|---|---|---|---|
| stoneskipping.wiki | 10（含 about / disclosure / privacy / terms 4 个信任页） | 平铺 6 页：`/guide/` `/zones/` `/rebirth-guide/` `/pets/` `/codes/` + 首页 | 「状态页」：每页 400–1,100 词，Quick answer + observed / known / unknown 分段 | codes 页 3 张表、pets / zones 各 1 张；JSON-LD 用 FAQPage、VideoGame | 自称 observed / reported；码标「reported working」「reported expired by one tracker」 | 样本页 0 次出现 Robux；没有通行证 / 商品清单；挂 profitableratecpmnetwork 广告脚本（GA G-2MHYJYTYX7） |
| stone-skipping.wiki | 31 | 5 个栏目 + 2 个独立页：`/progression`（10 篇）`/zones`（6 篇：5 个 zone 各一页 + 1 篇总览）`/pets`（3 篇）`/items`（2 篇）`/rewards`（2 篇）`/codes` `/updates` | 栏目页 + 长尾文章（约 1,000–1,200 词），文章带 Table of Contents、Quick answer、Tips、Checklist、Related Guides | 每篇 1 张表；首页 3 张；JSON-LD 用 Article、BreadcrumbList、ItemList、FAQPage | 标题里直接写「Observed」「Reported」「caption-level glimpses only」；updates 页是活动时间线（3 条） | shop 页只出现 1 次 Robux，没有逐项价格；样本页没有 Auto Wins / Training Zone / King Doggy / 主题蛋等名称；updates 页有这场活动的 UTC 起止（标题写作「ADMIN ABUSE + UPDATE」），但没有 World 5 字样 |
| 1stoneskipping.wiki | 198 = 33 个英文 URL × 6 语种（en / th / pt-BR / es / de / fr） | 8 个栏目：`/guides`（7 篇）`/codes`（1）`/progression`（3）`/zones`（1）`/stones`（2）`/pets`（2）`/rebirth`（2）`/rewards`（3）+ terms / privacy / contact | 栏目页 + 文章（1,400–1,900 词），每篇 H2 是动作句 + FAQ 5 问；站内搜索 | 每篇 1 张表；JSON-LD 用 Article、BreadcrumbList | 行文多为「看提示再决定」式的通用建议，少具体数字 | 同样没有通行证 / 商品价格表；6 语种把同一批内容 ×6（GA G-TLVNXBR5E2） |

三站共同点：都有 codes 页并列出「reported」码；都按「progression / zones / pets / rebirth / rewards(shop)」分栏；都没有通行证与开发者商品的名称 + 价格全表（样本页口径）。

## B. 同类 Roblox 攻略站（通用站，看页型结构）

| 站 | 取到了什么 | 页型结构 | 表格 | 对我们有用的结构点 |
|---|---|---|---|---|
| beebom.com（样本：某款 Roblox 游戏的 codes 页，1,154 词） | 200 | H1「<游戏> Codes (月份 年份)」→ All New Codes → Expired Codes → How to Redeem → How to Get More Codes → Why Are My Codes Not Working | 0（码用列表） | codes 页的五段式是行业惯例；标题带年月。我们没有官方码，不建这一页 |
| deltiasgaming.com（样本：某款 +1 类 Roblox 游戏的 Beginner's Guide） | 200 | H1 → Getting Started → Rebirths and Worlds，两节到底；面包屑 + Article + Person JSON-LD | 0 | 新手页只有两节、零表格 —— 我们的 how-to-play 用「官方原句对照表 + 未知项表」可以更结构化 |
| pockettactics.com / tryhardguides.com（Roblox codes 总表） | 200 | 一页按 A–Z 列出全部游戏的 codes 链接，6,000–13,700 词 | 0 | 总表型聚合页，对单游戏栏目无参考 |
| progameguides.com / destructoid.com / twinfinite.net | **未获取**（Cloudflare 拦截页 403，不过验证，停止该来源） | — | — | — |

## 结论：我们比它们厚在哪、准在哪

1. **商店数据是空白位**：11 个通行证 + 78 个开发者商品的名称、价格、创建日，三个专站的样本页都没有逐项列出。我们的 gamepasses / pets / boosts / shop 四页全部建在这批 S 级数据上。
2. **可算的东西只有我们算了**：蛋 x3 / x8 的每蛋单价与省多少（主题蛋 x8 省 41%）、宠物与孵化通行证的单价（+6 Pets 比 +3 Pets 单价更高）、Skill Multiplier 十档累计 5,980、同名通行证与商品的价差。
3. **活动信息更新一档**：stone-skipping.wiki 也写了这场活动的 UTC 起止，但标题还是「ADMIN ABUSE + UPDATE」；官方条目 10-01 14:47 UTC 更新过，我们取到的标题是「ADMIN ABUSE + WORLD 5」、描述三行（Admin Abuse / World 5 / New features），并换算了 7 个时区。另两站样本页没有活动时间。
4. **机制页我们更薄，而且会明说**：区域名、宠物概率、Rebirth 条件这些只有专站在写（observed / reported），官方一条没有。我们不写，页内用「not shown in public data / needs in-game check」标出，进 todo 等进游戏核实。这是本栏目和专站最大的取舍：**宁可薄，不引用 C 级数字**。
5. **码页不做**：官方来源零码。专站的码一个不收。
6. **不做 zone 单页、stone 清单、tier list、calculator**：全部缺一手来源。

## 我们采用的栏目结构

| 栏目（category） | slug | 首批文章 | 说明 |
|---|---|---|---|
| Getting Started | beginner | how-to-play、updates、community | 通用词入口：怎么玩、活动与更新、群组 / 码 / Discord |
| Robux Shop | robux | gamepasses、pets、boosts、shop | 个性词入口：通行证、蛋与宠物、Skill / Wins 加成、78 个商品全表 |
| （不设栏目） | codes / zones / stones / rebirth | — | 等一手来源或进游戏核实 |

页型沿用 mog-evolution / race-horses 基准：home / category / article / author；每篇文章 tldr 3–4 条、首段 40–60 词直答、问题式 H2、列表信息进表格、≥3 条站内链接、frontmatter `related` 驱动「Read next」。
