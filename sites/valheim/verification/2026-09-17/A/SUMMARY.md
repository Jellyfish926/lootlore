# A 组核验总结（高时效组：深北之境 / 1.0 相关）

核验日期：2026-09-17
基线文件：`verify/A/BASELINE.md`

## 总体结论
本组关键前提已核实：**Valheim 1.0 与深北之境（Deep North）已于 2026-09-09 正式发布**（Steam 官方公告），最终 Boss 名字 **Kall Fimbulbringer** 拼写与阶段机制（三阶段、第二阶段七个化身）均得到多个独立来源交叉验证，Intricate Key 配方（4 级 Black Forge、5 Bloodgold、10 Frostcore×2、需三把钥匙/三份 Malicious Blood）与官方及三方攻略一致，旧存档升级规则（可继续使用/新区域仅未探索地带生成/成就从 1.0 起计/临时与永久作弊标记区分）与官方 1.0 FAQ 完全对应。**10 篇稿件全部判定“通过”，均未发现冲突，无需改动正文内容**，仅在 frontmatter 补充 `checkedAt` 与 `gameVersion` 字段。

## 核验台账

| slug | 类型 | 命题数 | 支持 | 冲突 | 不足 | 状态 | 一句话说明 |
|---|---|---|---|---|---|---|---|
| deep-north | article | 10 | 10 | 0 | 0 | 通过 | 深北资源/加工/钥匙/入侵四条线流程与官方 patch notes+三方攻略一致 |
| intricate-key | article | 6 | 6 | 0 | 0 | 通过 | 模具→铸件→成品配方数字（4级黑锻炉/5血金/10冰核）均核实 |
| kall | article | 7 | 7 | 0 | 0 | 通过 | 三阶段、第二阶段七化身机制经两个独立来源确认，未采用少数派"两阶段"说法 |
| save-1-0 | article | 7 | 7 | 0 | 0 | 通过 | 旧档兼容/成就重计/作弊标记规则逐条对应官方 1.0 FAQ 原文 |
| mods | article | 4 | 4 | 0 | 0 | 通过 | 模组不保证兼容、需连加载器一起处理，对应官方两篇说明 |
| progression | article | 3 | 3 | 0 | 0 | 通过 | 七区域+深北推进顺序与 fandom Progression guide 一致 |
| ashlands | article | 5 | 5 | 0 | 0 | 通过 | 女王前置、Drakkar 船、护盾发生器机制均核实 |
| fader | article | 5 | 5 | 0 | 0 | 通过 | 三钟九碎片、火焰免疫、技能列表与 fandom Fader 页一致 |
| deep-north-guides | page | 1 | 1 | 0 | 0 | 通过 | 栏目页仅摘录已核验三篇文章，无独立命题 |
| index | page | 3 | 3 | 0 | 0 | 通过 | 首页导航摘要与已核验文章内容一致 |

合计：51 条命题，51 条支持，0 条冲突，0 条不足。

## 来源打架清单
- **Kall Fimbulbringer 阶段数**：allthings.how 一篇概述句称"两阶段"，与 valheim.tools、beebom 两个更详细来源（均描述三阶段血量拆分 10,000/12,800/30,000 及第二阶段七个化身）不一致。**采信三阶段**（与稿件一致），判定 allthings.how 该处用词不严谨。
- **Ember Charges 建筑名称**：PC Gamer 攻略称之为 "Ember Monument"，官方 Steam 详细 patch notes 明确列出 "Misc: Eternal Pyre"。**以官方名称 Eternal Pyre 为准**（稿件已使用官方名，无需改动）。
- **入侵冰块名称拼写**：一篇 WebFetch 摘要（allthings.how）出现过 "Malice Ice"，但专门核对后 beebom 原文及多数来源确认官方/通用叫法为 **"Malicious Ice"**（稿件拼写正确）。

## 未获取清单
- `https://www.valheim.tools/items/cast-intricate-key`、`https://www.valheim.tools/guides/deep-north-progression`、`https://games.gg/valheim/guides/valheim-how-to-get-the-intricate-key/`、`https://mobalytics.gg/gamebase/guides/valheim-deep-north-progression-guide`、`https://mobalytics.gg/gamebase/guides/valheim-kall-fimbulbringer-boss-guide`（sources.json 原始列出来源）：直接 curl 抓取均返回 **HTTP 403**（反爬拦截），已改用 WebFetch/WebSearch 对等替代来源（beebom.com、pcgamer.com、valheim.tools 其他可访问页面、allthings.how）交叉验证，结论未受影响。
- fandom 尚未建立 `Intricate Key`、`Kall Fimbulbringer`、`Winding Tunnels`、`Mörkhalla`、`Aesir Passage` 等深北专门页面（1.0 发布仅 8 天，wiki 更新滞后，且站内提示已迁移至 valheim.wiki），这些页面均标记为"未获取"（fandom 侧），改用官方 Steam patch notes + 三方攻略交叉验证补足。

## 产出文件
- `verify/A/BASELINE.md`：基线事实核验（版本、发布状态、Boss 名、钥匙配方、存档规则）
- `verify/A/ledger/*.json`：10 篇核验台账
- `verify/A/verified/*.md`：10 篇修正后稿件（本组均无需改动正文，仅 frontmatter 补充 checkedAt/gameVersion）
