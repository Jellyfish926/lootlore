# 页面素材来源记录表

规则：每页至少 1 个 S 或 A 级来源才开写；只有 B/C 的页 draft。本轮 12 页全部有 S 级来源；A 级为 0（开发者 Discord / 群组 wall / X 需登录，未获取）。事实编号（F…）见 `dossier.md`。

来源缩写：
- G = https://games.roblox.com/v1/games?universeIds=8719555347（S）
- V = https://games.roblox.com/v1/games/votes?universeIds=8719555347（S）
- BD = https://badges.roblox.com/v1/universes/8719555347/badges?limit=100（S）
- GP = https://apis.roblox.com/game-passes/v1/universes/8719555347/game-passes?passView=Full&pageSize=100（S）
- DP = https://apis.roblox.com/developer-products/v2/universes/8719555347/developerproducts?limit=100（S）
- EV = https://apis.roblox.com/virtual-events/v1/universes/8719555347/virtual-events（S；不带参数只回 3 条，带 `?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA` 从头翻页得全部 43 条，记 EVH）
- DOC = Roblox 官方文档 7 页（S，dossier 第 13 节）
- RS = https://apis.roblox.com/virtual-events/v1/virtual-events/<eventId>/rsvps/counters（S）
- GR = https://groups.roblox.com/v1/groups/33504096（S）
- RO = https://groups.roblox.com/v1/groups/33504096/roles（S）
- GG = https://games.roblox.com/v2/groups/33504096/games?accessFilter=Public&limit=50（S）
- AG = https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation（S，POST {"universeId":"8719555347"}）
- TH = https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=8719555347&countPerUniverse=10&size=768x432&format=Png（S）
- SG = Google 下拉（B，只作需求证据，`raw/suggest.txt`）
- C1 = southernmudding.wiki；C2 = southernmudding.site（C，只看结构，不作事实、不链接）

| 页 | 主来源 | 辅助 | 最高级 | 素材状态 | 图片 |
|---|---|---|---|---|---|
| index | G、GP、DP、BD | V、GR、AG、EV | S | 充足 | th1（封面）、th2 |
| guides（栏目） | G | BD、GP、DP、EV、GR | S | 充足 | th2 |
| how-to-play | G（描述原文）、BD | GP（F50 / F57 默认上限）、GR（进群送皮卡）、AG | S | 充足；操作按键、UI 位置、免费车名单未获取，正文写 needs in-game check | th3、th2 |
| vehicles | G（车型类别）、GP（各 Pack 描述）、DP（22 个载具商品） | GR | S | 类别与获取途径充足；包内车名、性能、免费车名单未获取 | th6、th7 |
| spawning | GP（Spawn 4 Vehicles / Spawn 4 Trailers / Any Slot Spawning / Portable Trailer Spawner / Deluxe Trailer Pack） | BD（F41 / F42）、DP（礼物价、Gooseneck Camper + Truck） | S | 上限与价格充足；槽位界面、拖车挂接操作未获取 | th5 |
| nitrous | G（9-25 更新说明原文）、GP（Rock Lights / Portable Customization） | EV（Nitrous 活动）、DP（两个礼物） | S | 官方原话 4 行 + 2 个通行证；触发方式、价格、适用车型清单未获取——页面如实列缺口 | th1 |
| gamepasses | GP | DP（13 个礼物商品） | S | 充足；礼物价与通行证价不一致的 8 项并列 | th7 |
| limiteds | DP | G（9-25 说明里 New Pickup Truck / New UTV） | S | 名称、价格、创建日、API 在售标记充足；游戏内是否还在卖、车辆数值未获取 | th4 |
| badges | BD | G（visits）、GP（Luxury Houses）、DP（Luxury House Gift） | S | 充足；房屋数量与位置未获取 | th2 |
| updates | G（描述、updated）、EVH（43 条活动）、RS | GP / DP / BD（创建日）、DOC5 | S | 排期、43 个每周更新标题充足；9-25 之前各周更新说明**全文**未获取 | th6 |
| community | GR、RO、GG | G（描述无码无链接） | S | 群组数据充足；Discord / X / wall 未获取 | th3 |
| author | — | — | — | 编辑方针页 | th5 |
| codes | — | — | — | **无官方来源 → 不建** | — |
| map | C1 / C2（C） | — | C | **只有 C 级 → 不建**（连 draft 也不写，避免把专站内容带进来） | — |

## 悬而未决 / 来源冲突

| 项 | 说法 A | 说法 B | 处理 |
|---|---|---|---|
| 通行证数量 | 前序硬门：14（另有 Placeholder） | 本次 GP：14 条记录 = 13 在售 + 1 Placeholder | 以本次实测为准，写 13；Placeholder 在 gamepasses 页一句带过 |
| 通行证价 vs 礼物价 | GP：如 Spawn 4 Vehicles 490 | DP：Spawn 4 Vehicles Gift 425 | 8 项不一致全部并列，写「cannot tell which is current」 |
| Portable Trailer Spawner | GP 325 | DP「[GIFT] Portable Trailer Spawner」390（礼物反而贵） | 并列 |
| 商品「Deluxe Trailer Pack」 | 名称不带 Gift | 与 Gift 批次同时创建 | 写 likely the gift version，标推断 |
| 「Limited」是否仍在售 | DP：IsForSale = true（61 个全是） | 游戏内商店是否展示：未知 | 只写接口标记，不写回归时间 |
| 9-25 的 New Pickup Truck / New UTV | G 描述：有 | DP：那一周没有新建同名商品 | 写「不在 Robux 商品数据里，怎么获得需进游戏核实」 |
| 更新时刻 | G：「Updates every Friday!」 | EVH：41 条周五活动里 20 条 17:00–17:29、14 条 18:00–18:29；近 10 条 9 条 17:00–17:15；实测落地只有一次（09-25 17:20） | 写「usually 17:00 UTC」+ 分布表 + 实测那一次，不写准点 |
