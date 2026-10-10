# 页面素材来源记录表

规则：每页至少 1 个 S 或 A 级来源才开写；只有 B/C 的页 draft。

来源缩写：
- G = https://games.roblox.com/v1/games?universeIds=10268960646（S）
- V = https://games.roblox.com/v1/games/votes?universeIds=10268960646（S）
- AGE = https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation（POST，S）
- GR = https://groups.roblox.com/v1/groups/84540135（S）
- RO = https://groups.roblox.com/v1/groups/84540135/roles（S）
- BD = https://badges.roblox.com/v1/universes/10268960646/badges?limit=100（S，空）
- GP = https://apis.roblox.com/game-passes/v1/universes/10268960646/game-passes?passView=Full&pageSize=100（S）
- DP = https://apis.roblox.com/developer-products/v2/universes/10268960646/developerproducts?limit=100（S）
- TH = https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=10268960646&size=768x432&format=Png&countPerUniverse=10（S）
- IC = https://thumbnails.roblox.com/v1/games/icons?universeIds=10268960646&size=512x512&format=Png（S）
- WD = https://games.roblox.com/v1/games?universeIds=9765324104（S，仅用于区分另一款 Wheelie District）
- EV = https://apis.roblox.com/virtual-events/v1/universes/10268960646/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA（S，2026-10-10 读，7 条活动公告；不带游标的请求时而只回 1 条）
- C1 = progameguides / nerdschalk / allthings.how 码页（B/C，只当线索，不链接、不引用码）

| 页 | 主来源 | 辅助 | 最高级 | 素材状态 | 图片 |
|---|---|---|---|---|---|
| index | G、GR、GP、DP | V、AGE、BD | S | 充足 | art01（封面）、art02 |
| beginner（栏目） | G | GP、DP | S | 充足 | art02 |
| how-to-play | G（描述原文） | GP、DP、TH | S | 玩法清单充足；按键/地图未获取，页内明说 | art02、icon |
| cops-fines | GP（NEVER PAY FINES）、DP（AVOID FINES） | G、TH、WD | S | 免罚方式与价格充足；罚款金额、追逐规则未获取 | art01 |
| community | GR、RO、G | WD、C1（只说「第三方码页存在」） | S | 充足；Discord 链接未获取 | icon |
| updates | GP、DP、G | — | S | 充足（时间戳≠补丁说明，页内明说） | art01 |
| upgrades（栏目） | GP、DP | G | S | 充足 | art02 |
| money | G、GP、DP | — | S | 收入来源与价格充足；报酬数额未获取 | art01 |
| bikes | GP、DP、G | — | S | 名称与价格充足；车辆清单/属性/卖车未获取 | art02、icon |
| gamepasses | GP | DP | S | 充足（描述为空的通行证只写名称与价格） | art02 |
| author | — | — | — | 编辑方针页 | icon |
| codes | C1 | — | B/C | **素材不足 → 不建** | — |
| patch-notes（2026-10-10 建） | EV | G、GP、DP | S | 充足：只印 7 条活动公告的原文与接口时间字段；是否如文上线、价格、别处是否另发更新说明 not confirmed | art02（封面）、art01 |
| cops-chase-rules（2026-10-10 建） | EV（AI COPS 👮 一条） | G、GP、DP | S | 充足：只印公告 12 行原文 + 白话解释（标明为本站解读）；罚款数额、加星条件、单人服入口 not confirmed | art01（封面） |
