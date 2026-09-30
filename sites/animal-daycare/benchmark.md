# 同类站架构对比（Animal Daycare (Anomaly)）

抓取日 2026-09-30。只学结构，不抄文字；两站均为抢注站，**正文不引用、不链接**。页数取各站 sitemap.xml（原始文件 `raw/comp/`）。

## 对比表

| 站 | 页数（sitemap） | 栏目 | 主要页型 | 表格 / 信息框 | 数据来源口径 | 明显短板 |
|---|---|---|---|---|---|---|
| animaldaycare.wiki | 33（含 fr/de/es/pt 4 个语种首页 + terms/privacy/cookies 3 个法务页） | Codes / Guides / Tier List / Players / Updates / Scripts / Tools / Wiki | codes + how-to-redeem；guides 8 篇（controls、daycare-map、getting-started、care-for-children、mini-games、spot-impostors、survive-night、review）；players 3 篇（co-op、mistakes、solo）；tier list 2 篇；patch-notes、latest-changes；impostor-checklist 工具；scripts 页 | 首页「Quick facts」；抽查 3 页正文 `<table>` 共 0 张（patch-notes 页 1 张）；每页 FAQ | 以 Roblox 页面为身份锚，玩法段落为泛泛的策略建议 | 没有徽章、开发者商品、Lamb Coins、职业等级任何官方数据；codes 页整页是「为什么没码」；做了外挂 scripts 页（总站不能碰） |
| animal-daycare.wiki | 9 | Guide / Team Builder / Resource Planner / About | 4 篇 guide（slug 直接用 YouTube 视频标题，如 “…-beginner-guide-tips-tricks-roblox-new-horror-game”“…-shift-1-10-full-game-walkthrough-roblox-4k60fps”）；2 个「工具」页 | beginner guide 4 张表；工具页为通用模板 | 明显转写自 YouTube 新手视频（章节与 Zac Worthy 视频一一对应） | 攻略就是视频转述；工具页与游戏机制无关；无官方数据 |
| Fandom | — | — | animaldaycare.fandom.com 404 | — | — | 不存在 |

## 结论：我们比它们厚在哪、准在哪

1. **官方数据它们都没用**：Roblox 接口直接给出 5 个徽章的逐字条件与累计获得数、25 个开发者商品的官方名称/价格/描述/上架日。两站都没有徽章页和商店页。
2. **「能撑到第几晚」用真实数据说话**：徽章累计数可换算成「每 100 个过了第一晚的人里，多少人过了 2 晚 / 5 班 / 10 班」，竞品只有主观建议。
3. **Lamb Coins 与职业等级**：四档金币包的每 Robux 性价比、1/2/3 星职业等级解锁价是可计算的独家表。
4. **码页不做**：无官方来源；首页一节说明原因与官方码会出现在哪。
5. **不做外挂/脚本页**。
6. **视频来源的具体打法（冒名者特征、夜间威胁）先 draft**：只有 B 级（一段 1.5k 播放的新手视频字幕），等进游戏核实或出现官方来源再翻正。

## 我们采用的栏目结构

| 栏目（category） | slug | 首批文章 | 说明 |
|---|---|---|---|
| Guides | guides | how-to-play、badges、shop、game-info（+ impostors、night-events 两篇 draft） | 只设一个栏目：已发布 4 篇，满足「3-5 篇才进导航」 |
| （不设栏目） | codes | — | 等官方来源 |

页型沿用 deep-fishing / blockspin 基准：home / category / article / author；每篇文章 tldr 3-4 条、首段 40-60 词直答、问题式 H2、≥1 张表、≥3 条站内链接、文末「Read next」。
