# 页面素材来源记录表

规则：每页至少 1 个 S 或 A 级来源才开写；只有 B/C 的页 draft。本轮 A 级来源 0 条（官方 Discord / X / wall 未获取），11 页全部由 S 级支撑。

来源缩写（取数 2026-10-02 UTC 11:19–11:38）：
- G = https://games.roblox.com/v1/games?universeIds=10765298801（S）
- V = https://games.roblox.com/v1/games/votes?universeIds=10765298801（S）
- AGE = https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation（POST，S）
- GP = https://apis.roblox.com/game-passes/v1/universes/10765298801/game-passes?passView=Full&pageSize=100（S）
- DP = https://apis.roblox.com/developer-products/v2/universes/10765298801/developerproducts?limit=100（S）
- BD = https://badges.roblox.com/v1/universes/10765298801/badges?limit=100（S，空）
- EV = https://apis.roblox.com/virtual-events/v1/universes/10765298801/virtual-events?limit=50（S；默认请求通常只返回即将开始的 1 条；带游标的请求 `?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA` 稳定返回 3 条含两场过往活动，见 dossier §6）
- GR = https://groups.roblox.com/v1/groups/207366578（S）
- RO = https://groups.roblox.com/v1/groups/207366578/roles（S）
- GG = https://games.roblox.com/v2/groups/207366578/games?accessFilter=Public&limit=50（S）
- OW = https://users.roblox.com/v1/users/2994850996（S）
- TH = https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=10765298801&countPerUniverse=10&size=768x432&format=Png（S）
- IC = https://thumbnails.roblox.com/v1/games/icons?universeIds=10765298801&size=512x512&format=Png（S）
- AS = https://thumbnails.roblox.com/v1/assets?assetIds=…&size=420x420&format=Png（S，通行证 / 商品 / 活动图标）
- PG = https://www.roblox.com/games/111543903102439/1-Stone-Skipping（S，未登录 HTML）
- DOC = https://create.roblox.com/docs/production/monetization/passes（旧地址 …/game-passes 301 到此）、…/monetization/developer-products、…/promotion/social-media-links（S，Roblox 官方文档）
- C3 = stoneskipping.wiki / stone-skipping.wiki / 1stoneskipping.wiki（C，只当线索与对标，不链接、不引用内容）

| 页 | 主来源 | 辅助 | 最高级 | 素材状态 | 图片 |
|---|---|---|---|---|---|
| index | G、GP、DP、EV、GR | V、AGE、BD、IC | S | 充足 | art01（封面）、art03 |
| beginner（栏目） | G | EV、GR | S | 充足 | art04 |
| how-to-play | G（description 原文六句） | TH（宣传图）、IC（WORLD 4）、EV（World 5）、GP / DP（只用名称证明系统存在） | S | 核心循环充足；一切数值未获取，页内逐项标明 | art03、art02、art04 |
| updates | EV（含 World 3 / World 4 两场过往活动）、DP（创建日）、GP（创建日）、G | IC、AS（活动图） | S | 充足（时间戳≠补丁说明，页内明说）；World 2 日期未获取 | event、icon |
| community | G、GR、RO、GG、OW、EV、PG | V、AGE、DOC（社交链接可见性）；C3（只写「专站有码表，没有一条追溯到 Meow Labs 官方帖」这一句） | S | 充足；Discord / wall / social links / 私服是否开放未获取 | art01、icon |
| robux（栏目） | GP、DP | G | S | 充足 | art02 |
| gamepasses | GP | DP（礼物版、同名商品）、DOC、AS（Koi 图标） | S | 名称 / 价格 / 日期充足；效果未获取，按名称与图标标 likely | art01、pass-koi |
| pets | DP（18 个蛋 + 3 个包）、GP（6 个通行证） | G（"pets for powerful boosts"）、AS（Dragon Egg、King Doggy 图标） | S | 价格充足；宠物名、加成、概率未获取 | art02、egg-dragon、pet-king-doggy |
| boosts | DP（31 个加成类商品） | G、DOC、TH | S | 价格充足；倍率、数量、时长未获取 | art04、art02 |
| shop | DP（78 个全表） | GP、BD、AS（Starter Pack、Devil Pack 图标） | S | 充足（78 个都无描述，只写名称 / 价格 / 创建日） | art03、pack-starter、pack-devil |
| author | — | — | — | 编辑方针页 | art04、icon |
| codes | C3 | — | C | **素材不足 → 不建** | — |
| zones / stones / rebirth / worlds | G（各一句）、IC、EV | C3 | S（仅一句话级别） | **素材不足 → 不建**，并入 how-to-play / updates | — |

## 悬而未决（两处来源说法不同 / 无法判定）

| 事项 | 来源 A | 来源 B | 处理 |
|---|---|---|---|
| 游戏名写法 | G `name`：+1 Stone Skipping | G `description` 首句：+1 Skipping Stones | 两个都照录；标题与正文用 `name`，首页速览表、FAQ、how-to-play、community 各说明一次 |
| 最近更新时间 | G `updated` 2026-09-30T18:09Z | GG `updated` 2026-09-23T02:50Z | 两个都记进 dossier，说明字段口径不同；正文只用 G |
| Admin / Golden Training Zone 价格 | GP：599 / 249 | DP 同名商品：195 / 315 | 两组都照录；gamepasses 页专设一节，写明无法从公开数据判断商品是否仍在售 |
| Wins Pack 5 价格 | DP「Wins Pack 5」575 | DP「Wins Pack 5 [20% OFF]」459 | 两条都是在售商品，照录；提示读者看购买弹窗 |
| 活动标题 | EV（10-02 取数）：ADMIN ABUSE + WORLD 5 | C3（stone-skipping.wiki/updates）：ADMIN ABUSE + UPDATE | 以 EV 为准（条目 updatedUtc 2026-10-01T14:47Z，可能改过标题 —— 这是推断，正文不写） |
| 活动条数 | EV 默认请求：通常 1 条 | 带游标请求：稳定 3 条（多出 World 3、WORLD 4 两场已结束活动） | 3 条的 universeId / host 都是本游戏，采信为 S 级；出处统一用游标 URL，updates 页内写明两种请求的差别 |
| 私服 | G `createVipServersAllowed` = false | 同字段对已知有私服的游戏也是 false | 不下结论，community 页写「无法确认」 |
