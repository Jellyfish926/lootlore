# 进游戏 / 需要账号才能核实的点（Phasmophobia）

本轮全部内容来自官方文本与 Steam 公开接口，没有进游戏。下面每条都对应页面里一句「以官方某年某帖为准」或「not stated / not confirmed」的话，核实后可以把限定语去掉或改数。

## A. 上线后尽快核（影响当前事件页）

| # | 要核实什么 | 涉及页面 | 现在页面怎么写的 |
|---|---|---|---|
| A1 | Crimson Eye 2026 是否已按 10/8 开始、现在是否在线；活动地图是否每日轮换、每天几张 | crimson-eye、events、index、updates-events | 「announced for October 8 to November 1」「rotation not stated」 |
| A2 | Event Board 上 Crimson Eye 传单写的 Community / Personal 目标各几个、点数门槛、各奖励挂在哪个目标下 | crimson-eye | 「counts not stated」「point totals not published」 |
| A3 | seasonal event tee 与 Twitch Drop 的 Crimson Eye tee 是不是同一件 | crimson-eye | 「does not say whether those are one shirt or two」 |
| A4 | Blood Moon 天气下 2026 届是否仍 +10% 奖励、鬼速 / 理智变化是否同 2025 | crimson-eye | 标为「last year's rules」 |
| A5 | 0 倍率自定义局是否计活动点数 | crimson-eye、difficulty | 「not confirmed; the safe reading is to avoid 0x games」 |
| A6 | Seasonal Event toggle 在菜单的具体位置与文案 | patch-notes、crimson-eye | 只引补丁说明原话 |
| A7 | Ghost Hunts 4 Hearts（10/26–11/1）的奖励与参与方式 | crimson-eye | 「has not been announced」——官方公布后更新 |

## B. 新手与难度（旧补丁说明里的数字是否仍是现值）

| # | 要核实什么 | 涉及页面 | 现在的出处 |
|---|---|---|---|
| B1 | 五个默认难度在难度选择界面的现行描述与数值（准备时间、宽限、hunt 时长、理智药恢复、死亡返还比例、奖励倍率） | difficulty、how-to-play | 2021-10 与 2023-02 补丁说明；数值官方未公布 |
| B2 | Intermediate / Professional / Insanity 的解锁等级；Nightmare 是否仍 30 级；Custom 是否仍 50 级 | difficulty、how-to-play | 2023-12、2024-10 补丁说明 |
| B3 | 自定义难度现行选项清单（三个页签逐项）、最高倍率是否仍 15x、预设是否仍 3 个、指定鬼种选项的确切文案 | difficulty | 2022-09 清单 + 2023-02 上限 + 2026-08 新增 |
| B4 | Evidence Given 软上限（3 证据 4x / 2 证据 5x）与黄色警告图标是否仍在 | difficulty | 2023-02 |
| B5 | Monkey Paw 愿望数（5 / 4 / 3）是否仍按倍率分档 | difficulty | 2023-02 |
| B6 | Apocalypse 挑战现在是否仍限单人；Event Board 传单的现行文案 | difficulty、achievements | 2022 写单人、2024 徽章文本未写 |
| B7 | 每周挑战是否仍为 26 个轮换、完成 3 次给奖励 | difficulty | 2023-02 |
| B8 | 等级门槛：Camp Woodwind 19、Sunny Meadows Restricted 22、Point Hope 15、Sound Recorder 4、Nell’s Diner 5；新 Restricted 变体（Prison / Brownstone / Point Hope）的解锁等级 | how-to-play | 2022–2025 各帖；新变体官方未写等级 |
| B9 | 默认键位：放置键 F、使用键鼠标右键是否仍是默认；1–4 与 H 的实际表现；Igniter 是否固定在 4 | how-to-play | 2022-09 与 2026-07 补丁说明 |
| B10 | 每局照片 5 / 视频 5 / 录音 3 / 可删 3 是否仍是现值；Perfect Investigation 的完整条件 | how-to-play | 2025-06 Chronicle；「usual requirements」官方未列 |
| B11 | 消耗品清单（Crucifix、Salt、Igniter、Sanity Medication 全 Tier；Firelight / Incense I–II）是否仍是现状 | how-to-play | 2023-08 |
| B12 | Training 的现行流程（房间顺序、Ghost Orbs 录制要求、Hold Use 便签） | how-to-play | 2023-08 + 2026-07 + 2026-08 |

## C. 成就

| # | 要核实什么 | 涉及页面 |
|---|---|---|
| C1 | 6 个无描述成就（Work Experience、They're here、The Bait、Flawless Execution、Escape Artist、Doom Slayed）的真实达成条件——拿到 Steam Web API key 后调 ISteamUserStats/GetSchemaForGame，或进游戏解锁验证；确认我们按解锁率做的「内部 ID ↔ 显示名」配对 | achievements |
| C2 | Deildegast、Kormos、Obambo、Gallu、Dayan 是否真的没有对应成就（现结论来自成就页 54 条清单） | achievements |
| C3 | 0 倍率之外的自定义局是否照常计成就 | achievements、difficulty |
| C4 | 「Unique shirts for prestige and event specific achievements」具体对应哪些成就 / 里程碑 | achievements |

## D. 平台与价格

| # | 要核实什么 | 涉及页面 |
|---|---|---|
| D1 | PlayStation Store、Xbox Store 当前售价与是否有 PS VR2 单独条目 | platforms-price |
| D2 | Steam Deck 实机：兼容报告 category 2 对应的客户端标签；单人是否需要联网（与 2025-06「无网络可载入」对照） | platforms-price |
| D3 | 主机语音识别现在支持的语言清单（2025-02 承诺的「full range of languages」是否已上） | platforms-price、how-to-play |
| D4 | appdetails 的 package_groups 里有一个「Subscribe to Phasmophobia — $19.99 for a month, then $13.99 / month」订阅组，含义不明（疑似 Steam 侧数据）；页面未写，需看商店页实际是否展示 | platforms-price |
| D5 | 商店页 EA 问答何时改成 2027（现仍写 second half of 2026） | roadmap、platforms-price、index FAQ |

## E. 待官方公布后更新（不是进游戏，是盯公告）

- Unity 6 更新的具体日期与 Development Preview（官方称 11 月）。
- 第二个 Player Character update / 「cosmetics update」是否仍在 11 月。
- 42 Edgefield Road 重做、Winter’s Jest 2026 的日期。
- 「content update」（Weekly Challenges、语音识别新功能）的内容与日期。
- Kormos 的加入版本（官方帖只在修复条目里提到）。

## F. 二期内容的前置（现在只有 B 级来源）

- 鬼魂证据表、各鬼能力 / 速度 / hunt 阈值；Deildegast 的证据与能力。
- 装备 Tier 数值与解锁等级全表。
- 各地图房间数与大小分类（官方只零散给过 Nell’s Diner 14 间 / 13 个鬼房、Point Hope 10 层 12 间）。
- Cursed Possessions 的现行数值。
