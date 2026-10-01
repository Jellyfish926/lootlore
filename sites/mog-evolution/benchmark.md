# 同类站架构对比（+1 Mog Evolution）

抓取日 2026-10-01（sitemap + 首页 + 9 个内页，原始 HTML 见 `raw/comp_*.html`、`raw/sitemap_*.xml`、`raw/c1_*.html`、`raw/c_*.html`）。只学结构，不抄文字。

两个抢注站同一套模板（sitemap 结构几乎一致、页面文案句式相同），GA ID 不同（G-PMKC28K2CX / G-ZC6ZRQRSNX），mogevolution.wiki 挂了 profitableratecpmnetwork 广告脚本。Fandom 未查到同名 wiki（未逐个子域验证，记为未获取）。

## 对比表

| 站 | sitemap 页数 | 栏目 / 目录 | 主要页型 | 表格 / 信息框 | 数据口径 | 明显短板 |
|---|---|---|---|---|---|---|
| mogevolution.wiki | 30（含 6 个信任/法务页） | `/codes/` `/tier-list/` `/trello/` `/calculator/` `/squad-planner/` `/resource-calculator/` `/guides/`（beginner、progression、farming、ascension、wins、rebirth） `/wiki/`（items-and-rewards、maps-and-systems、builds-and-entities、ranked、bonesmash） `/updates/`（world-2、world-3、admin-abuse） | 「状态页」为主：每页 Quick answer + Confirmed / Unknown / Reported 三段；计算器让玩家自己填点击数 | 少量卡片；无数据表 | 只引用游戏描述 4 句 + 游戏 API 标题/时间戳；活动名来自「public event trackers」，自称无法一手验证 | **0 个开发者商品**：Auto Clicker 22 次/秒、VIP 10x、跑步机、Rebirth 等级上限、Ascend 换 body、Stage 传送全没写；ranked 页说「未确认」，但 places 接口直接有 [RANKED] place；活动页没拿到 virtual-events 接口的官方活动 |
| mog-evolution.wiki | 29 | 同上，另有 `/wiki/appeal/` `/wiki/evolution-labels/` `/guides/hammers/` `/guides/wins-and-ascension/`，无 world-3 页 | 同上；tier-list 页明说「不能排」，只列宣传图 6 个标签 | 标签卡片 | 同上 + 宣传图文字（Chopped、Mogger、Sub 3、MTN、Chad、True Adam） | 同上；hammers 页只有 Bonesmash 一个名字，没写商品里的 Claviculars Hammer x1024、Hammer Upgrade [1]/[2] |

## 结论：我们比它们厚在哪、准在哪

1. **商品数据是全网空白**：43 个开发者商品（28 个带官方描述）的名称、价格、描述、上架日——两个竞品一个都没列。这批描述是官方原话，能把「机制偏薄」的空洞填上：Auto Clicker 22 次/秒、VIP 10 倍、跑步机 x2-x999、Rebirth 有等级上限、Ascend 换到下一个 body、Stage 1-3 传送、World 2/3、Gigachad x4、Claviculars Hammer x1024、Smoothie x2048。
2. **每 Robux 性价比可算**：四个 Appeal 包每 Robux 换到 2,041 → 200,401 Appeal；九档 Power 合计 395 Robux；x8 跑步机（79）比 x9（69）还贵——竞品的计算器只能让玩家自己填数。
3. **Ranked 与活动有一手证据**：places 接口有 `+1 Mog Evolution [RANKED]` 子 place；virtual-events 接口有「Admin Abuse & Update 4」（10-03 23:00 → 10-07 23:00 UTC）。竞品两项都标「reported / 无法验证」。
4. **更新时间线**：从商品创建日拼出 8-30 → 9-26 的上新节奏（9-10 World 2 + Gigachad、9-18 跑步机扩档 + 锤子升级、9-24 World 3 + Smoothie、9-26 W2/W3 限定）。
5. **码页不做**：游戏描述、群组、活动描述都没有码；竞品码页也是 0。
6. **不做外挂/脚本页**：下拉词第一是 "mog evolution script"，违反 Roblox 条款，总站不做。
7. **不做计算器 / squad planner / tier list**：计算器所需的每次点击收益无一手来源；游戏无组队系统的一手证据；body 顺序无一手来源。

## 我们采用的栏目结构

| 栏目（category） | slug | 首批文章 | 说明 |
|---|---|---|---|
| Getting Started | beginner | how-to-play、progression、updates、community | 通用词入口：怎么玩、Wins/Rebirth/Ascend/World 进度、更新与活动、群组/码/测试服 |
| Boosts & Robux | upgrades | appeal、limiteds、shop | 个性词入口：怎么更快拿 Appeal、399 Robux 限定解锁、43 个商品全表 |
| （不设栏目） | codes | — | 等官方来源 |

页型沿用 untitled-wheelie-game / animal-daycare 基准：home / category / article / author；每篇文章 tldr 3-4 条、首段 40-60 词直答、问题式 H2、≥1 张表、≥3 条站内链接、frontmatter `related` 驱动「Read next」。
