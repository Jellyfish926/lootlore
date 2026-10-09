# 同类站架构对比（American Plains Mudding）

抓取日 2026-10-09（11:14–11:41 UTC）。**只学结构，不抄文字**；三个站都是第三方站（B 级），**正文不引用、不取任何事实**，它们给出的线索全部回到 Roblox 官方接口核对后才用。页数取各站 sitemap.xml（原始文件 `raw/comp/*-sitemap.xml`，抽样页 `raw/comp/apmwiki_*.html`、`pmwiki_*.html`、`smwiki_*.html`，词数与表格数由 `raw/htmlstat.py` 对 `<main>` 实测）。三站 robots.txt 均 `Allow: /`。

结论：两个 APM 专站一个停在 7 月（最新更新条目是 7 月 18 日，文章日期 7 月 23 日），一个是只有 2 个内容页的空壳。**没有一家用上官方接口里的通行证价格、礼物商品、徽章获得数、60 条活动 listing 与 10/3 更新说明。**

## 对比表

| 站 | 栏目 | 页型 | 页数（sitemap） | 我们取什么 / 它们缺什么 |
|---|---|---|---|---|
| americanplainsmudding.wiki（APM 专站，B） | Getting Started / Vehicles / Customization / Trailers & Towing / Activities / Locations & Map / Codes & Rewards / Updates（8 栏，每栏 1–2 篇）+ About 与 3 个法务页 | 首页 1,698 词、0 表；8 个栏目页 107–147 词、0 表（薄列表）；英文 15 篇文章全部实测：275–449 词，13 篇 0 表、2 篇各 1 表；每页有 Table of Contents 与侧栏「Reward Status」卡 | 84（en / zh / ja 各 28） | **取**：按意图分栏的思路（新手 / 车辆 / 拖车 / 更新 / 码与奖励）；「没有码就明说没有码，并把 Like + Favorite 送车单独讲清」的口径（我们核对过：10-09 的官方描述里确实没有码，确实有送车这句话）。**缺**：通行证一个价格都没有；没有徽章页（4 个 Hidden Vehicle 徽章是下拉头部词）；没有生成上限 / 私服命令；更新停在「July 18」，首页数字是 619M+ 访问（我们 10-09 读到 714.9M）；文章偏通用建议（"Build a Mental Map""Empty-Lot Test"），可核对的数字很少；栏目页不到 150 词 |
| plainsmudding.wiki（APM 专站，B） | 顶部导航 Vehicles / Setups / Activities / Locations / Sources，实际只有首页 + /vehicles 两个内容页 | 首页 268 词、/vehicles 327 词，0 表；/sources 129 词（外链 games API 与游戏页）、/corrections 79 词；页面文字自己写着 "Work in progress""needs update" | 7（首页、/vehicles、/sources、/corrections、3 个法务页） | **取**：独立的 Sources 页与 Corrections 入口（我们用每页 sourceUrls + author 页的报错入口实现）。**缺**：没有任何具体事实——每个板块都是「Confirm names, specs… in game」的占位话术；没有价格、徽章、更新 |
| southernmudding.wiki（同品类 Roblox 泥地越野游戏 Southern Mudding 的专站，B；**另一款游戏，只看结构**） | Vehicles / Guides / Gamepasses / Updates + FAQ + Recent | 栏目页 99–220 词、0 表；内页 663–1,256 词、0–2 表：gamepasses/current-gamepass-prices（1,096 词，2 表）、updates/friday-update-schedule（948 词，1 表）、vehicles/vehicle-types-guide（1,179 词，2 表）、guides/beginner-guide（1,256 词，1 表）；每个更新单独一页（如 october-2-2026-trucks-and-boats，663 词） | 26（含 5 个信任 / 法务页；sitemap lastmod 16 条 2026-08-15、2 条 2026-10-03） | **取**：「通行证价格 + 生成上限」合成一页、「更新时间表」单独成页这两种页型——我们的 gamepasses / spawning / updates 三页对应。**不取**：每周更新各开一页（过周就要换 URL；我们一页持续追加）；一车一页（车辆数值与图没有一手来源）。**缺**：没有徽章页；栏目页薄 |
| Fandom | — | — | 0（american-plains-mudding / americanplainsmudding / apm / american-plains-mudding-roblox 四个子域 api.php 全部 404；只说明这四个子域下没有） | 这四个子域下没有 Fandom wiki 可对标 |

## 需求侧佐证（Google 下拉，`raw/suggest.jsonl`，30 组前缀，全部 200）

有词的：discord（discord server / link / invite / code，共 10 条变体）、hidden vehicle（location / tractor / cars / trailer / semi / truck，共 10 条以上变体）、update（today / next / new / christmas / when does … update / what time does … update）、codes、commands（admin / advanced / private server commands / commands list）、script、tow truck、tornado、map、controls、how to connect trailer、who made / when did … come out、premium customization、game pass、farming、shaboozey。
下拉为空的：wiki、free、limited、atv、badges、whitelist、staff。
搜索量：**未获取（自动任务不查 Semrush）**，不估算。

## 我们比它们厚在哪、准在哪

1. **通行证全表**：8 个在售通行证的官方描述与 Robux 价、8 个礼物商品同价、6 条未在售记录。两个专站一个价格都没有。
2. **生成上限**：官方描述里的「4-8 slots」「cap of 8」「2x … Up To 16」拼成一张表，并标明哪几格是官方原话、哪几格是我们推的。
3. **私服命令**：通行证描述里印着的 3 条命令逐字给出——「commands」是下拉头部词，专站没有这一页。
4. **徽章**：8 个徽章的累计与昨日获得数，4 个同名 Hidden Vehicle 徽章用创建日与徽章 ID 区分；明说不提供位置。
5. **更新时间与更新史**：60 条官方活动 listing 全部周六开始，按季节给出 UTC 时刻分布与换算；24 条写了内容的 listing 逐字列出；专站停在 7 月。
6. **节日限定车**：5 个节日通行证的建档日与节日的间隔、3 个礼物商品的价格，万圣节前三周这页正好有人查。
7. **不写真实车厂名**：全栏目只用官方文本里的通用名；宣传图 alt 同样。
8. **不建 codes 页、不给隐藏车位置、不抄命令表**：官方来源里没有的一律不写，在页面上明说缺什么。

## 我们采用的栏目结构

| 栏目（category） | slug | 首批文章 | 说明 |
|---|---|---|---|
| Home | index | hub 首页 | 通用词落地 + 分流；key facts 表；FAQ 5 条 |
| Guides | guides | how-to-play、vehicles、spawning、private-servers、gamepasses、limited-vehicles、badges、updates、community | 单栏目 9 篇，满足「3–5 篇才进导航」；与 southern-mudding 栏目同构（`native.nav: ["guides"]`） |
| Author | author | 作者页 | E-E-A-T；写明不套真实车厂名 |
| （不设） | codes | — | 无官方来源 |
| （不设） | map / hidden-vehicle-locations / commands 全表 / controls / money | — | 有搜索需求但无一手素材，见 `planning/keyword-map.md`「砍掉的词」与 `todo-ingame.md` |
