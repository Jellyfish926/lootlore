# 同类站架构对比（Southern Mudding）

抓取日 2026-10-02（11:25–11:31 UTC）。**只学结构，不抄文字**；两个专站都是第三方站（C 级），**正文不引用、不链接、不取任何事实**。页数取各站 sitemap.xml（原始文件 `raw/comp/*-sitemap.xml.out`，抽样页面 `raw/comp/pages/p1–p13.html`）。robots.txt 两站均 `Allow: /`。Fandom 三站走 `api.php`（`raw/comp/fandom_*.json`），只取站点统计与分类名。

## 对比表

| 站 | 页数 | 栏目 | 主要页型 | 表格（抽样页） | 数据口径（它自己声称的） | 结构上的短板 |
|---|---|---|---|---|---|---|
| southernmudding.wiki（专站，C） | 25（sitemap，含 5 个信任/法务页） | Vehicles / Guides / Gamepasses / Updates + FAQ + Recent | 栏目页是薄列表（vehicles 229 词、updates 169 词、0 表）；内页 1,000–1,300 词：gamepasses/current-gamepass-prices（2 表）、vehicles/vehicle-types-guide（2 表）、updates/friday-update-schedule（1 表）、guides/beginner-guide（1 表）；单载具页 3 个；单通行证页 1 个 | 首页 0；内页 1–2 | 每页有 Sources 小节；首页写「Updated for the August 14 Buggies Update」 | 首页停在 8 月 14 日版本；栏目页薄；没有徽章页；没有开发者商品（Limited）全表；没有活动/RSVP 数据 |
| southernmudding.site（专站，C） | 13（sitemap，含 3 个信任页） | 单栏 Guides（8 篇）| beginner、nitrous、vehicles、updates-september-2026、map-and-houses、gamepasses、tornado（龙卷风与追风车）、codes-and-free-rewards；每篇 840–980 词 | 首页 0；内页 1–5 | 首页写「Facts checked Sep 30, 2026 · Roblox build: Nitrous update (Sep 25)」，有在线 / 访问 / 群组人数统计条 | 没有徽章页；没有 Limited 商品全表；更新页按月命名（过月要换 URL）；codes 页的 H2 是「为什么有人搜 codes / 真正的免费奖励」，不是码表 |
| Car Dealership Tycoon Wiki（Fandom，同类载具游戏） | 866 篇条目 | Vehicles / Passes / Updates Log（首页三个入口）+ Discord | 一车一页；分类轴：年份新增（2021–2026 Additions）、获取方式（Shop / Event / Season / Gamepass Car / Limited / Unobtainable / Removed）、驱动形式、产地 | — | 社区编辑 | 分类大量按真实车厂 / 产地建（我们的 IP 红线不允许照搬这一轴） |
| Driving Empire Wiki（Fandom） | 736 篇 | Vehicles 为主 | 一车一页；分类轴：Limited / Event / Gamepass / Off-Sale / Removed、车型类别（Supercars / Race Cars…） | — | 社区编辑 | 同上，Licensed Vehicles 分类 399 页 |
| Ultimate Driving Universe Wiki（Fandom） | 1,032 篇 | Citizen Vehicles / Places / Roads / Game Features | 一车一页 + 地点页 + 道路页 | — | 社区编辑 | 活跃编辑 4 人，维护稀 |
| Southern Mudding 的 Fandom | 未发现（southern-mudding / southernmudding 两个子域 api.php 均 404） | — | — | — | — | — |

三个 Fandom 载具 wiki 的共同结构：**获取方式轴**（商店 / 通行证 / 限时 / 下架）是最稳定的分类，其次是**新增年份/月份轴**；一车一页靠的是车辆数值与图，这两样我们都没有一手来源。

关键词佐证（`raw/suggest.txt`，Google 下拉）：有词的是 discord、map、codes、update（update today / next update / when does … update / what time does … update）、houses、tornado、script；gamepass / limited / nitrous / badges / utv / 6x6 / trailer / money 下拉为空。搜索量**未获取**，不估算。

## 差异化：我们比两个专站厚在哪、准在哪

1. **Limited 商品全表**：22 个可单买载具 + 22 个礼物版，逐字名称、Robux 价、创建日、接口在售标记。两个专站都没有这张表。
2. **通行证价与礼物价并列**：13 个通行证对 13 个礼物商品，7 个礼物更便宜、1 个更贵。专站只给通行证价。
3. **徽章与获得数**：4 个徽章的官方累计数与「每 100 个进游戏徽章对应多少」，把「多少人拖过拖车 / 领过房」变成数字。专站没有徽章页。
4. **更新时间与更新史有官方依据**：Roblox 活动接口里 43 条每周活动（41 条周五开始，近 10 条里 9 条在 17:00–17:15 UTC）+ RSVP 人数，直接回答下拉里的「what time does southern mudding update」；43 个活动标题本身就是逐周更新名。
5. **更新史一页到底**：建服期用商品 / 通行证 / 徽章创建日，2025-12 起用 43 条官方活动标题；不按月开新 URL，一页持续追加。
6. **不写真实车厂名**：全站只用接口里的通用名。
7. **不建 codes 页**：官方描述、群组描述、shout 都没有码；在 community 页一节说清，并指出官方唯一写明的免费奖励是「进群送皮卡」。

## 我们采用的栏目结构

| 栏目（category） | slug | 首批文章 | 说明 |
|---|---|---|---|
| Guides | guides | how-to-play、vehicles、spawning、nitrous、gamepasses、limiteds、badges、updates、community | 单栏目 9 篇，满足「3–5 篇才进导航」；与 race-horses 同构（`native.nav: ["guides"]`） |
| （不设） | codes | — | 无官方来源 |
| （不设） | map / houses / tornado 独立页 | — | 有搜索需求但无一手素材，见 planning/keyword-map.md「砍掉的词」与 todo.md |

页型沿用 race-horses / untitled-wheelie-game 基准：home / category / article / author；tldr 3–4 条、首段 40–60 词直答、问题式 H2、每篇结构不同、≥1 张表、≥3 条站内链接、文末「Read next」。没有学 Fandom 的「一车一页」：车辆数值与图没有一手来源，硬拆只会是空页。
