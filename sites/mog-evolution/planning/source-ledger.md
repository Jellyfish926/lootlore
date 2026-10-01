# 页面素材来源记录表

规则：每页至少 1 个 S 或 A 级来源才开写；只有 B/C 的页 draft。

来源缩写：
- G = https://games.roblox.com/v1/games?universeIds=10764479526（S）
- V = https://games.roblox.com/v1/games/votes?universeIds=10764479526（S）
- AGE = https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation（POST，S）
- PL = https://develop.roblox.com/v1/universes/10764479526/places?limit=50（S）
- GR = https://groups.roblox.com/v1/groups/426881025（S）
- RO = https://groups.roblox.com/v1/groups/426881025/roles（S）
- GG = https://games.roblox.com/v2/groups/426881025/games?accessFilter=Public&limit=50（S）
- TS = https://games.roblox.com/v1/games?universeIds=10765888078（S，测试版）
- BD = https://badges.roblox.com/v1/universes/10764479526/badges?limit=100（S，空）
- GP = https://apis.roblox.com/game-passes/v1/universes/10764479526/game-passes?passView=Full&pageSize=100（S，空）
- DP = https://apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100（S）
- EV = https://apis.roblox.com/virtual-events/v1/universes/10764479526/virtual-events?limit=50（S）
- TH = https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=10764479526&size=768x432&format=Png&countPerUniverse=10（S）
- IC = https://thumbnails.roblox.com/v1/games/icons?universeIds=10764479526&size=512x512&format=Png（S）
- C1 = mogevolution.wiki / mog-evolution.wiki（B/C，只当线索与对标，不链接、不引用数字）

| 页 | 主来源 | 辅助 | 最高级 | 素材状态 | 图片 |
|---|---|---|---|---|---|
| index | G、GR、DP、EV | V、AGE、BD、GP、PL | S | 充足 | art02（封面）、art06 |
| beginner（栏目） | G | DP、EV | S | 充足 | art04 |
| how-to-play | G（描述原文） | DP（Auto Clicker、VIP、跑步机、锤子描述）、TH | S | 核心循环充足；每次点击收益、Bonesmash 解锁条件未获取，页内明说 | art02、art01 |
| progression | DP（Skip Rebirth / Skip Ascend / Stage / World / X2 Wins / Starter Pack）、G | TH（宣传图标签）、PL | S | 机制关系充足；数值门槛、body 顺序未获取，页内明说 | art06、art05 |
| updates | DP（创建日）、EV、G、PL、TS | GG | S | 充足（时间戳≠补丁说明，页内明说） | art08 |
| community | GR、RO、GG、TS、G | C1（只说「第三方码页也是 0」） | S | 充足；Discord / Trello 未获取 | icon、art07 |
| upgrades（栏目） | DP | G | S | 充足 | art03 |
| appeal | DP、G | — | S | 加成名称、倍率、价格充足；叠加规则未获取 | art02、art04 |
| limiteds | DP | TH | S | 5 个 399 档商品充足（2 个无描述只写名称价格） | art03、icon |
| shop | DP | GP、BD | S | 充足（15 个无描述商品只写名称价格） | art08 |
| author | — | — | — | 编辑方针页 | icon |
| codes | C1 | — | B/C | **素材不足 → 不建** | — |
| bodies / tier list | TH（标签）、DP（LTN、Gigachad） | C1 | S（仅名称） | **素材不足 → 不建**，并入 progression | — |
| ranked | PL（仅 place 名） | C1 | S（仅名称） | **素材不足 → 不建**，并入 updates | — |

## 悬而未决（两处来源说法不同）

| 事项 | 来源 A | 来源 B | 处理 |
|---|---|---|---|
| 最近更新时间 | G `updated` 2026-09-30T17:52Z | GG `updated` 2026-09-26T22:48Z | 两个都照录，说明字段口径不同 |
| 资源名 | DP 商品名 "Appeal" | 同一商品描述 "Power"；Smoothie 描述 "Charisma" | 照录原话；"Power 很可能就是 Appeal" 标我们的读法；Charisma 不下结论 |
| 群组成员 | GR 5,456,141 | RO Member 角色 5,456,192 | 用 GR 数，两接口时点差 |
