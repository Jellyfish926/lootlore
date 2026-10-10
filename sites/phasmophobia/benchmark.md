# 同类站架构对比（Phasmophobia，2026-10-10 实测）

结论：现有的 Phasmophobia 资料站都按「实体」组织（鬼 / 证据 / 地图 / 装备），数据来自社区实测；没有一个把官方公告当主线做「更新史 + 路线图 + 活动日历 + 平台与价格」并逐条挂一手出处。我们首批不碰实体数据（只有 B 级支撑），先打这块空档；实体库等能进游戏核实后再评估（见 todo.md）。

只记架构，不抄内容；下表没有任何一条事实进入正文或 entities.json。

## 表 1：对标站结构

| 站 | 抓取结果（2026-10-10） | 规模 | 导航 / 栏目 | 页面组件 | 更新时效 | 我们学什么 / 不学什么 |
|---|---|---|---|---|---|---|
| phasmophobia.fandom.com（Phasmopedia） | api.php 200（Main_Page wikitext、MediaWiki:Wiki-navigation、siteinfo statistics、allcategories、Ghost 页 sections） | 实测：articles 323、pages 3,598、images 2,767、activeusers 3（siteinfo） | 导航一级只有 Phasmophobia → Ghosts / Evidence / Maps / Equipment / Guides；首页 5 个图块入口（Ghost / Equipment / Map / Evidence / Sanity）+ 购买按钮（Steam / PlayStation / Xbox） | 分类实测：Ghosts 33、Equipment 25、Maps 16、Evidence 11、Gameplay 30、Development 149、Guides 5；Ghost 总览页分 Characteristics / Behaviour / Types of ghosts / Evidence / Random characteristics | 最近改动 2026-10-09（ID Card、Cosmetics 页，实测 recentchanges） | 学：实体四分法做二期栏目骨架；「Development」类（149 页）说明更新史本身就是一大块内容。不学：把补丁说明逐版抄成 wiki 页 |
| ign.com/wikis/phasmophobia | 200 | 首页可见 88 个 wiki 内链（实测 href 计数，非全站页数） | 首页链接分布：鬼种单页（Banshee、Demon…）、装备单页（Crucifix、EMF Reader…）、地图单页（6 Tanglewood Drive…）、How-To Guides、Tips and Tricks、Difficulty、Optional Objectives、补丁说明页（如 Phasmophobia_September_10_2026_Patch_Notes）、活动攻略（Phasmophobia_Cursed_Hollow_Event_Guide_2026、Alan_Wake_Doll_Locations_and_Puzzle_Solutions） | 未逐页拆解 | 有 2026-09-10 补丁页，说明仍在更新 | 学：补丁说明单独成页、活动每届一页、「How to …」问题式入口。不学：单鬼 / 单装备薄页先行 |
| tybayn.github.io/phasmo-cheat-sheet（Zero-Network cheat sheet） | 200（单页应用，数据由接口加载；抓到的是外壳） | 未获取（数据接口未取） | 单页工具：证据勾选筛鬼、难度 / 证据数 / hunt 时长设置、语音指令控制、地图页签、Weekly 信息、Twitch 信息、多语言 | 工具型，无文章 | 页脚「Copyright © 2023-2026」 | 学：玩家对局中要的是「勾选式」工具，这是二期工具页方向。不学：本轮无法核实其数据来源，不引用 |
| phasmophobia.wiki.gg | 403「Just a second...」挑战页 | 未获取 | 未获取 | 未获取 | 未获取 | — |
| game8.co/games/Phasmophobia | 404 | 未获取 | 未获取 | 未获取 | 未获取 | — |

## 表 2：搜索需求 × 我们的落点（Google 下拉词，2026-10-10 实测，hl=en gl=us；搜索量未获取——本轮按要求不用 Semrush）

| 下拉词（实测原样） | 月量 / KD | 我们的落点 |
|---|---|---|
| phasmophobia update / update today / update 2026 / update roadmap / update log | 未获取 | /phasmophobia/patch-notes/ |
| phasmophobia patch notes / patch notes today / patch notes 2026 | 未获取 | /phasmophobia/patch-notes/ |
| phasmophobia roadmap / roadmap 2026 / roadmap 2027 / roadmap horror 2.0 | 未获取 | /phasmophobia/roadmap/ |
| phasmophobia 1.0 / 1.0 release date / 1.0 update | 未获取 | /phasmophobia/roadmap/ |
| phasmophobia crimson eye 2026 / crimson eye trophy upgrade / crimson eye event guide | 未获取 | /phasmophobia/crimson-eye/ |
| phasmophobia events 2026 / event right now / event calendar / event trophies | 未获取 | /phasmophobia/events/ |
| phasmophobia twitch drops / twitch drops 2026 / twitch drops schedule 2026 / twitch drops cool cat | 未获取 | /phasmophobia/events/ |
| phasmophobia double xp / double xp dates / double xp end date | 未获取 | /phasmophobia/events/ |
| phasmophobia achievements / achievements list / achievements hidden / achievements hunter | 未获取 | /phasmophobia/achievements/ |
| phasmophobia difficulty levels / difficulty differences / difficulty multiplier / custom difficulty settings / custom difficulty unlock | 未获取 | /phasmophobia/difficulty/ |
| phasmophobia price / price steam / crossplay / crossplay ps5 pc / switch 2 release date / system requirements / is phasmophobia on xbox game pass | 未获取 | /phasmophobia/platforms-price/ |
| phasmophobia how to play / how to use sound recorder / how to change character | 未获取 | /phasmophobia/how-to-play/ |
| phasmophobia ghosts / cheat sheet / new ghost deildegast / deildegast evidence / deildegast ability | 未获取 | **本轮不做**：只有社区 wiki（B 级）支撑，官方只公布了 Deildegast 的名字 |
| phasmophobia codes / cheat codes / safe codes / lobby codes | 未获取 | **不做 codes 页**：215 条官方公告里没有兑换码系统；「safe codes」指地图内保险箱、「lobby codes」指联机房间码，都不是兑换码 |

## 我们采用的栏目结构（12 页，只 en）

| 栏目（category） | 栏目页 slug | 文章 |
|---|---|---|
| Home | index | — |
| Getting Started | getting-started | how-to-play、platforms-price、difficulty、achievements |
| Updates & Events | updates-events | patch-notes、roadmap、crimson-eye、events |
| Author | author | — |

与对标站的差异化：
1. 官方公告当主线：更新史时间线、两版路线图逐项对照、活动日历、Twitch Drops 与双倍经验窗口，每个日期 / 数字挂官方帖。
2. 旧规则标年份：难度与等级门槛来自 2021–2024 的补丁说明，页面逐条写出处月份，不当现行值断言。
3. 不做实体库：鬼魂证据表、装备数值、地图房间表首批全部不做（B 级），列 P2。
