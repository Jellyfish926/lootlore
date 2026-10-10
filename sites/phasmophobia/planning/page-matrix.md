# 页面矩阵（Phasmophobia，en，首批 12 页）

一个搜索意图 = 一个页面。全部 12 页 draft: false（每页都有 S 级来源支撑，见 source-ledger.md）。

| # | URL | 页型 | 承接关键词 | 这页要回答的用户问题 | 优先级 | 到期动作 |
|---|---|---|---|---|---|---|
| 1 | /phasmophobia/ | home | phasmophobia | 这是什么游戏、现在什么状态、我该先看哪页 | P0 | 每次新版本后更新「What changed」表与 tldr 第 2 条 |
| 2 | /phasmophobia/getting-started/ | category | （栏目页） | 新手四类问题分流：怎么玩 / 在哪买 / 选什么难度 / 成就 | P0 | — |
| 3 | /phasmophobia/how-to-play/ | article | how to play、how to use sound recorder | 第一局做什么、默认按键、照片 / 视频 / 录音上限、死了会怎样、等级门槛 | P0 | Unity 6 更新（官方称 11 月）后复核按键与 Training 段 |
| 4 | /phasmophobia/platforms-price/ | article | price、crossplay、ps5 / xbox、switch 2、system requirements、game pass | 多少钱、哪些平台、配置、跨平台、Deck、是否还在 EA | P0 | 价格 / 折扣变动时更新；1.0 或 Switch 2 定档时重写首段 |
| 5 | /phasmophobia/difficulty/ | article | difficulty levels、custom difficulty settings / unlock、difficulty multiplier、achievements hunter | 五个默认难度差在哪、自定义难度怎么算倍率、0 倍率的后果、Apocalypse 门槛 | P0 | 官方「content update」（Weekly Challenges 改动，TBC）上线后更新 |
| 6 | /phasmophobia/achievements/ | article | achievements、achievements list、achievements hidden、achievements not working | 54 个成就全表 + 解锁率、哪些没描述、自定义局算不算 | P0 | 解锁率每月刷一次（raw/achievements_parsed.json 重抓）；成就数变化时改标题 |
| 7 | /phasmophobia/updates-events/ | category | （栏目页） | 更新 / 路线图 / 活动四页分流 + 当前状态速查表 | P0 | 每次活动或版本后改「Where things stand」表 |
| 8 | /phasmophobia/patch-notes/ | article | update、update today、patch notes、patch notes 2026、new ghost | 最新版本是哪个、今年每个版本改了什么 | P0 | **每个新版本帖 7 天内加一行**；2027-01 起新开 2027 页，本页标题保留 2026 |
| 9 | /phasmophobia/roadmap/ | article | roadmap 2026 / 2027、1.0 release date、unity 6 update、horror 2.0 | 1.0 什么时候、今年还剩什么、两版路线图差在哪 | P0 | 下一篇 Development Preview 或路线图更新后改；Unity 6 上线后改状态列 |
| 10 | /phasmophobia/crimson-eye/ | article（事件页） | crimson eye 2026、crimson eye trophy upgrade、crimson eye event guide | 今年活动日期、地图、奖励、掉宝与双倍、和往年差在哪 | P0 | **失效日 2026-11-01**：活动结束后一周内把时态改成过去式、补官方结算信息，保留为「2026 回顾」常青页并在 events 页保持入口（不 308，因为每年同名活动会回来；2027 届新开 /crimson-eye-2027/ 时本页 title 保留年份）|
| 11 | /phasmophobia/events/ | article | events 2026、event calendar、event trophies、twitch drops、twitch drops schedule 2026、double xp dates | 活动规则、历届日期与奖励、Twitch 绑定步骤、掉宝与双倍窗口 | P0 | Winter’s Jest 2026 公告后 7 天内加行；每个新 Twitch Drop / Double XP 公告后加行 |
| 12 | /phasmophobia/author/ | author | — | 谁写的、怎么核实、怎么报错 | P0 | — |

P1（上线后第一周，素材已在 raw/ 里）：`winters-jest`（等 2026 届公告）、`player-character-update`（Customisation shop 与两次 Player Character 更新的官方口径）、`map-reworks`（Bleasdale / Grafton / Tanglewood / Willow 重做与 Restricted 变体，全 S 级）。

P2（等 GSC 真实搜索数据 + 进游戏核实后再定，不预支）：鬼魂证据表与单鬼页、装备 Tier 数值表、地图房间表、Cursed Possessions、cheat-sheet 型工具页——目前只有 B 级支撑，做了也只能 draft。

## 首页模块

| 模块 | 承接词 | 写什么 | 链到 |
|---|---|---|---|
| 首段直答 | phasmophobia | 一句话定义 + 开发商 / EA 起始日 / 美区价 | — |
| New to the game? | how to play、price、difficulty、achievements | 四个入口 | how-to-play、platforms-price、difficulty、achievements |
| What changed in 2026 表 | update、patch notes | 五个关键版本 | patch-notes |
| What is coming next | roadmap、1.0、crimson eye | 短期活动 + 年内计划 + 1.0 窗口 | crimson-eye、roadmap、events |
| 栏目列表 | — | 两个栏目 | getting-started、updates-events |
| 来源说明（hub_body.scope 取这一节） | — | 来源范围与不做什么 | — |
| FAQ（frontmatter faq） | price、1.0、latest update、crimson eye、crossplay、achievements、codes | 7 问 | 各页 |
