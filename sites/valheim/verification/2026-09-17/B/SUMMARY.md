# B 组核验总结（2026-09-17）

负责页面：articles/eikthyr、elder、bonemass、moder、yagluth、queen、swamp、mountains、plains、mistlands；pages/bosses、biomes（共 12 页）。

核验方法：优先通过 `https://valheim.fandom.com/api.php?action=parse&page=<Title>&prop=wikitext&format=json` 拉取官方 wiki 词条原始 wikitext（部分标题为重定向，已改用正式标题重新抓取），并交叉核对 Steam 官方 1.0 发行公告原文（`steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1843481262688942`）与 Steam 新闻 API（appid 892970）。所有来源均于 2026-09-17 访问，HTTP 状态均为 200。

游戏版本：官方 1.0（含 Deep North）已正式发行，最新热更为 1.0.10 / 1.0.12（Steam 公告 gid 1843481262695240 "Hotfix 1.0.10 & 1.0.12"）。**注意**：fandom 的 `Deep North` 词条目前仍标注 `{{Unfinished}}`，infobox 的 `boss` 字段为空，站内也没有独立的 `Kall` / `Kall Fimbulbringer` / `Fimbulbringer` 词条（站内搜索均为空结果）——fandom 尚未跟上 1.0 正式发行的内容更新。

## 结果表

| slug | 页面 | 命题数 | 支持 | 冲突 | 不足 | 状态 | 一句话说明 |
|---|---|---|---|---|---|---|---|
| eikthyr | 赤血灵鹿 | 5 | 5 | 0 | 0 | 通过 | 召唤/掉落/祭坛/攻击全部与 fandom Eikthyr 词条一致，无改动 |
| elder | 古树长老 | 6 | 6 | 0 | 0 | 通过 | 3 颗上古种子、火焰弱点、藤蔓/树根/踩踏三招、沼泽钥匙掉落均核实无误 |
| bonemass | 邪骨恶灵 | 5 | 5 | 0 | 0 | 通过 | 10 根枯骨、钝击弱点/斩击抗性/火穿刺高抗、毒云与召唤小怪均核实无误 |
| moder | 冰霜龙母 | 4 | 4 | 0 | 0 | 通过 | 3 枚龙蛋、飞行远程+落地近战吐息、龙泪→工匠台均核实无误 |
| yagluth | 亚格鲁斯 | 3 | 3 | 0 | 0 | 通过 | 5 个丑地精图腾、近身/陨石/远程三类攻击、Torn spirit 拼写与用途均核实无误 |
| queen | 迷雾女王 | 5 | 5 | 0 | 0 | 通过 | Sealbreaker 由矿洞碎片制作、高击退、多层地形跌落风险均核实无误 |
| swamp | 沼泽开荒 | 4 | 4 | 0 | 0 | 通过 | 沼泽钥匙开墓穴、泥泞废料堆产铁屑、全员敌对+持续下雨均核实无误 |
| mountains | 雪山开荒 | 5 | 5 | 0 | 0 | 通过 | 龙蛋重量200/不可传送、愿望骨定位银矿、银矿传送限制均核实无误 |
| plains | 平原开荒 | 4 | 4 | 0 | 0 | 通过 | 大麦/亚麻仅平原可种、工匠台需龙泪、死亡蚊/丑地精为平原威胁均核实无误 |
| mistlands | 迷雾之地开荒 | 5 | 5 | 0 | 0 | 通过 | 黑核/封印碎片产自被侵染矿洞、矮人提取器、精炼魔力设施伤及周边建筑均核实无误 |
| bosses | Boss栏目导航 | 5 | 4 | 0 | 1 | 通过（已改） | Fader 召唤/攻击、六个正篇 Boss 召唤材料均核实无误；**Kall Fimbulbringer 的“锁链阶段/召唤化身阶段/最终强化阶段”三阶段描述缺乏可靠来源，已改为不作具体阶段断言** |
| biomes | 区域推进导航 | 4 | 4 | 0 | 0 | 通过 | 纯导航页，涉及的前置钥匙/召唤材料/关键资源均与对应独立文章及 fandom 词条一致 |

**合计**：命题 55 条，支持 54 条，冲突 0 条，不足 1 条（已按红线处理为不作断言）。12 页全部状态为「通过」，无需人工决定项。

## 来源打架 / 未获取清单

- 无来源之间互相矛盾（官方与 fandom、fandom 与同行站一致）的情况。
- **唯一的“不足”项**：`pages/bosses.md` 中关于最终 Boss Kall Fimbulbringer 的具体战斗阶段划分（“锁链阶段、召唤化身阶段、最终强化阶段”）。核实过程：
  - fandom 站内搜索 `Kall`、`Fimbulbringer` 均无结果；
  - fandom `Deep North` 词条仍标注 `{{Unfinished}}`，infobox `boss` 字段留空；
  - Steam 1.0 官方发行公告（`steam_community_announcements` gid 1843481262688942）的内容清单中仅有一行 `Boss: Kall Fimbulbringer`，未描述具体战斗机制/阶段。
  - 结论：Boss 名称本身（Kall Fimbulbringer）经 Steam 官方公告确认拼写准确，可以保留；但“三阶段”划分及具体阶段名称目前找不到 S/A 级来源支持，已在 `verified/bosses.md` 中删除该具体断言，改为“具体阶段划分暂无可靠来源支持，本文不做断言”。
  - **提醒其他组**：负责 `kall.md`（最终 Boss 独立文章）与 `deep-north.md` / `save-1-0.md` 的小组在核验时会遇到同样的信源缺口（fandom 尚未收录 1.0 内容），需要格外依赖 Steam 官方公告、patch notes 与官方 Discord/推特，不能仅靠 fandom。

## 输出文件

- `ledger/*.json` × 12：逐条命题、来源、访问日期/状态码、判定与修正说明。
- `verified/*.md` × 12：修正后的完整 Markdown（10 篇文章 + 2 篇栏目页），frontmatter 新增 `checkedAt: "2026-09-17"` 与 `gameVersion` 字段；除 `bosses.md` 软化 Kall 三阶段表述外，其余 11 篇正文原样保留（核验无冲突、无需改动）。
