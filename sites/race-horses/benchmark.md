# 同类站架构对比（[INDEX📖] Race Horses）

抓取日 2026-10-01。只学结构，不抄文字；三站均为抢注站，**正文不引用、不链接**。页数取各站 sitemap.xml（原始文件 `raw/comp/`，抽样页面 `raw/comp/pages/`）。robots.txt 三站均 `Allow: /`。

## 对比表

| 站 | 页数（sitemap） | 栏目 | 主要页型 | 表格（抽样） | 数据口径 | 明显短板 |
|---|---|---|---|---|---|---|
| race-horses.wiki | 140（英文 35 + es / ja / pt-BR 各约 35） | Guides / Horses / Races / Care / Economy / Badges | 每栏 2-6 篇长文（rarities、traits、shiny、leveling、hurdle-races、race-rewards、feeding-apples、cleaning、cash、offline-earnings、stable-upgrades、max-stable、100k-race）；徽章拆成单徽章页（hatch-50-eggs、win-50-races、first-and-last…） | 首页 0；badges 1；rarities 3；traits 2；cash 1 | 自称以官方描述与徽章为依据，正文大量泛泛建议（「judge a horse over several entries」） | 稀有度写「All Six Tiers」漏 Exotic；0 处 Index；0 个 Robux 价格；没有徽章累计数；没有通行证页 |
| racehorses.online | 40（en / pt / es 各 13 + privacy） | Wiki / Guides / Updates | beginner、shiny、horse-care、stable-upgrades、money、leveling、get-better-horses、offline-earnings；wiki/rarities；updates | rarities 1；updates 1；shiny 1 | 「Last verified」日期 + 来源框；updates 停在 09-21 的「Sep 24 NEW EGG + STABLE UPGRADE」预告 | 预告后没跟进（Exotic 蛋 09-22 已上架）；无徽章页、无通行证页、无价格；首页 0 表 |
| racehorses.wiki | 12 | 扁平 | badges（「All 23」）、rarities、traits-shiny、horses、codes、hatch-calculator、stable-roi、sources、beginner-guide | badges 1；codes 1；rarities 1 | 有 sources 页；codes 页列 4 个第三方报告码并注明「未亲测」 | 徽章 23 个（官方 24，缺 Fruity Foal）；无 Exotic；计算器靠用户自填概率；无通行证价格 |
| Fandom | — | — | 未发现 | — | — | — |

关键词佐证（`raw/suggest.txt`）：Google 下拉「race horses roblox …」长尾（index / exotic / shiny / badges / gamepass / eggs）全部为空；有词的部分都落到另一款游戏「Horse Race」。需求量**未获取**，不估算。

## 差异化：我们比它们厚在哪、准在哪

1. **24 枚徽章完整表 + 官方累计数**：三站最多列 23 个且没有任何获得数。我们给逐字条件、累计与 24 小时获得数、「每 100 个 Horsin' Around 对应多少」——把「多难」变成数字。
2. **7 档稀有度（含 Exotic）**：竞品写 6 档。我们用 7 枚孵化徽章 + 7 个买蛋商品证明阶梯，并给每档的 Robux 蛋价与跳过计时价。
3. **通行证价格表 + 礼物版价格**：竞品 0 个 Robux 价格。5 个通行证、11 个礼物商品、32 个开发者商品全量官方价；指出 X2 RACE CASH 通行证 329 与礼物版 249 的不一致。
4. **Index 说清「官方说了什么、没说什么」**：竞品 0 处提到 Index。官方只有一句「Collect horses for rewards」，我们照实写并列出能确认的收集维度（7 档稀有度、性状、闪光、毛色、眼睛大小），不编奖励。
5. **更新时间线**：按徽章 / 商品 / 通行证创建日排出 6 月至 9 月的时间线（竞品 updates 页停在预告）。
6. **不建 codes 页**：官方描述、群组描述、shout 都没有码；竞品码全部来自第三方转述。
7. **消歧**：页面点明本作不是「Horse Race」。

## 我们采用的栏目结构

| 栏目（category） | slug | 首批文章 | 说明 |
|---|---|---|---|
| Guides | guides | how-to-play、badges、eggs、horses、races、care-stable、gamepasses、updates | 单栏目 8 篇，满足「3-5 篇才进导航」 |
| （不设） | codes | — | 无官方来源 |

页型沿用 animal-daycare / untitled-wheelie-game 基准：home / category / article / author；tldr 3-4 条、首段 40-60 词直答、问题式 H2、每篇结构不同、≥1 张表、≥3 条站内链接、文末「Read next」。
