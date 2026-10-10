# 页面素材来源记录（Phasmophobia）

规则：每页至少 1 个 S 或 A 级来源才开写。12 页全部满足，全部 draft: false。没有任何页面以 B / C 级来源为唯一依据。事实编号见 dossier.md。

| 页 | 主来源（级） | 辅来源（级） | 素材状态 | 悬而未决 |
|---|---|---|---|---|
| index | appdetails、商店页（S）；v0.19.1.0 补丁说明（S） | 2026-06-24 路线图帖、Crimson Eye 公告（S） | 充足 | — |
| getting-started | 同子页（S） | — | 充足 | — |
| how-to-play | 商店描述（S）；Chronicle v0.13、Ascension v0.9、v0.17.0.0、v0.18.0.0、v0.18.0.1 hotfix、v0.19.0.0 补丁说明（S） | Nightmare v0.4（2021）、Apocalypse v0.7（2022）、Tempest v0.8、Eventide v0.10、v0.15.1.0、主机语音识别 v0.11.1.2、Bans & Reporting 指南（S） | 充足 | 2022 年的默认键（F / 鼠标右键）与各等级门槛是否仍为现值——页面标了出处年份；Perfect Investigation 的「usual requirements」官方未列 |
| platforms-price | appdetails、商店页、Deck 兼容报告接口（S） | 2023-06 / 2024-07 / 2024-10 主机公告、官网 v0.11、v0.11.1.2、Chronicle、Nell’s Diner v0.15.0.0、v0.14.2.0、2025-12 Switch 2、2026-06 路线图帖、官网游戏页（S） | 充足 | 主机商店现价与 Steam 区域价未取（页面写 not checked）；Deck 报告 category 2 的文字标签接口不返回（页面不译）；Deck 离线与 Chronicle「无网可载入」的出入（并列不裁决） |
| difficulty | 商店描述（S）；Nightmare v0.4、Apocalypse v0.7、Tempest v0.8.0.0 / v0.8.1.0、v0.19.0.0、v0.19.0.1（S） | Holiday 2023 v0.9.3.0、官网 v0.11、Eventide、Chronicle、Ascension、v0.18.0.0（S）；Steam 成就页（A） | 充足（规则逐条标年份） | 各难度具体数值（准备时间秒数等）官方补丁说明未给 → 不写；Intermediate / Professional / Insanity 解锁等级官方未给；Apocalypse 是否仍限单人未明；Monkey Paw 愿望数表为 2023 年口径 |
| achievements | Steam 成就页 HTML（A，平台一手）；成就百分比 API（S） | v0.19.0.0、v0.19.0.1、v0.18.0.0、官网 v0.15.1.0、Nell’s Diner v0.15.0.0、v0.17.0.0、Ascension（S） | 充足 | 6 个无描述成就的达成条件（需 schema API key 或进游戏）→ 只列内部 ID 作推断线索并标注；解锁率为当日快照 |
| updates-events | 同子页（S） | — | 充足 | — |
| patch-notes | 2026 年 16 个版本的官方帖（Steam feed 全量 + 官网同文页）（S） | 2026-06-24 帖、QoL 预告三篇（S） | 充足 | 官网列表日期与 Steam 时间戳不一致（页面说明并统一用 Steam UTC）；Kormos 何时加入官方帖未写 |
| roadmap | 2026-01-31 与 2026-06-24 路线图帖及其内嵌图片（S） | Development Preview #21、v0.17.1.0 说明、v0.19.0.1、v0.19.1.0、商店页 EA 问答、Switch 2 公告（S） | 充足 | 第二个 Player Character update 是否仍在 11 月、Unity 6 具体日期、netcode 更新去向——官方未再说明；路线图图片文字为目视转录 |
| crimson-eye | 2026-10-01 公告（官网版含 Edit）、v0.19.1.0 补丁说明（S） | 2024 公告与 v0.11、2025 公告与 v0.14.2.0、2026-06 路线图帖、v0.19.0.0、v0.15.1.0（S） | 充足（日程为「已公告」口径） | 活动是否已按期开始未进游戏确认；2026 届的点数 / 目标数 / 轮换规则 / 奖励加成官方未写；seasonal event tee 与 Crimson Eye tee 是否同一件未明；0 倍率是否计活动点数未明 |
| events | Cursed Hollow 2025 官网帖、2026 公告与 v0.16.1.0、Crimson Eye 2025 / 2026、Winter’s Jest 2025 公告与 v0.15.1.0、Alan Wake v0.17.1.0（S） | 官网 Twitch Drops 页、首个 Twitch Drops 公告、2026 年 7 个掉宝公告（6 个在 Steam、1 个只在官网）、4 个双倍公告、v0.14.1.0、v0.18.0.1（S） | 充足 | 各目标点数官方未公布；Alan Wake 活动结束日未写；Cursed Hollow 2025 结束日未取；Winter’s Jest 2026 未公告 |
| author | 站内规范 | — | 充足 | — |

## 取证顺序实录

1. appdetails → 确认类型（Action / Indie / Early Access，4 人联机恐怖）、价格、平台、截图池。
2. ISteamNews 全量（377 条，官方 215 条）→ 2024-10 至今逐条通读，更早的按主题检索（difficulty / custom / unlock / prestige / console）。
3. 官网新闻页 53 篇（含 2026 年列表上的全部 33 篇）+ 5 个固定页 → 与 Steam 文本逐条比对（check_facts.py），记下 6 处两边不一致（dossier 第 9 节）。
4. 成就页 HTML + 百分比 API → 54 条逐字入库。
5. 两张路线图图片下载目视。
6. 对标站只看结构（benchmark.md）。
