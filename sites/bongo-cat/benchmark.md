# 同类站架构对比（2026-09-29 实测）

结论：可对标的只有 bongocat.org 一个活站，它是程序化 wiki（223 件物品卡片、无表格、成就只收 7 个、最近更新停在 Feb 25），强项是「物品单页」长尾；我们首批不跟物品单页，打它没有的四块：成就全表（28 个 + 解锁率）、开箱/兑换机制、安全与报错（有开发者原话出处）、交易规则与活动时间线。

## 表 1：对标站结构

| 站 | 抓取结果 | 规模 | 导航/栏目 | 页面组件 | 成就覆盖 | 更新时效 | 我们学什么 / 不学什么 |
|---|---|---|---|---|---|---|---|
| bongocat.org | 200 | 首页自述「264 game entities across 7 categories」；Items 223、Rarity Tiers 6、Events 10、Supporter Packs 5、Cross-Promotions 6、Achievements 7、Updates 7；sitemap 拆 wiki-sitemap / pages-sitemap | 三组：Cosmetics（Items、Rarity Tiers）/ Events & Promotions（Events、Supporter Packs、Cross-Promotions）/ Progression（Achievements、Updates）+ 站内搜索 | 物品页：Details 键值（Item Type、Rarity、Obtained From、Tradeable、Obtainability、Drop Rate）+ Quick Facts（Confidence、Verified 日期）+「Incomplete」提示；列表页为 A–Z / Recent 排序卡片；全站 0 张 `<table>` | 只列 7 个 Bongo Beat 成就（Steam 实际 28 个），无解锁率 | 最近更新卡片全是 Feb 25（2026） | 学：按「来源渠道」分栏（活动/支持者包/联动）、物品键值信息框、Verified 日期。不学：程序化单物品薄页、无表格 |
| bongocatdb.vercel.app | 429 Vercel Security Checkpoint | 未获取 | 未获取 | 未获取 | 未获取 | 未获取 | — |
| steamhunters.com/apps/3419430 | 403 | 未获取 | 未获取 | 未获取 | 未获取 | 未获取 | — |
| bongo-cat.fandom.com | api.php 200 | 9 个页面（Hats、Skins、Emojis 各一句话；Paw pass、Circus ticket、Angry (Skin) 有内容） | Skins / Hats / Emojis / Paw pass | Item template 信息框（rarity、obtained_from、is_it_limited?、item_type） | 无 | 2026-09 有 Circus Paw Pass 截图 | 学：物品信息框字段；数据不足，只作 B 级线索 |
| gamerant（单篇） | 200 | 1 篇 How to Get Epic & Legendary Items（May 18, 2025） | 文章 Jump Links 2 节 | 纯文字步骤 | 无 | 2025-05 | 只交叉验证兑换 10→1 与约 30 分钟宝箱 |

## 表 2：搜索需求 × 对标站覆盖（Semrush 美国库 2026-09-29，站主提供）

| 词 | 月量 / KD | 第一页现状（站主提供） | 我们的落点 |
|---|---|---|---|
| bongo cat | 22.2K / 57 | — | /bongo-cat/（hub） |
| bongo cat game | 1.9K | — | hub + how-to-play |
| bongo cat steam | 1.3K / 51 | — | hub + how-to-play |
| bongo cat steam error | 590 | — | steam-error |
| is bongo cat on steam safe | 70 | — | is-it-safe |
| bongo cat wiki | 20 | 已有 bongocat.org | hub |
| bongo cat codes | 0 | — | **不做**：游戏没有兑换码系统（Paw Pass Token 是 Steam 商店物品，不是兑换码） |
| bongo cat hats / skins / items | 未给量 | hats 已有 bongocat.org | hats-skins（机制向，不逐件） |
| bongo cat achievements (guide) | 未给量 | 第一页全是聚合器 | achievements（全表 + 追踪器数据） |
| bongo cat auto clicker / unlock all cheat | 未给量 | — | 并入 is-it-safe（只写有出处的部分） |

## 我们采用的栏目结构（12 页，只 en）

| 栏目（category） | 栏目页 slug | 文章 |
|---|---|---|
| Home | index | — |
| Getting Started | getting-started | how-to-play、steam-error、is-it-safe、multiplayer |
| Hats, Skins & Achievements | collection | hats-skins、exchange-trading、events、achievements |
| Author | author | — |

与 bongocat.org 的差异化：
1. 表格优先：每篇 ≥1 张数据表（掉率、活动时间线、快捷键、28 成就）。
2. 每条事实挂一手出处（公告/开发者帖），页脚 S001… 来源列表。
3. 不做单物品页（缺一手稀有度数据）；等拿到 Steam 物品定义（需 API key）再评估 P2 物品库。
