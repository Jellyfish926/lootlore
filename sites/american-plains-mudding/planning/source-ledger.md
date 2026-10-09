# 页面素材来源记录表

规则：每页至少 1 个 S 或 A 级来源才开写；只有 B / C 的页 draft。本批 9 篇文章 + 首页全部有 S 级来源，无 draft；guides（栏目索引）与 author（编辑方针页）照基准 sourceUrls 为空，事实全部来自子页。A 级来源本轮 0 条（群组 shout 为 null、wall 404、社交链接 401、Discord 频道未进）。

来源缩写：
- G = https://games.roblox.com/v1/games?universeIds=2783797267 （S；描述全文、created、visits、playing、maxPlayers、genre）
- V = https://games.roblox.com/v1/games/votes?universeIds=2783797267 （S）
- FAV = https://games.roblox.com/v1/games/2783797267/favorites/count （S）
- BD = https://badges.roblox.com/v1/universes/2783797267/badges?limit=100&sortOrder=Asc （S；8 条，取两次 id 一致）
- GP = https://apis.roblox.com/game-passes/v1/universes/2783797267/game-passes?passView=Full&pageSize=100 （S；14 条）
- DP = https://apis.roblox.com/developer-products/v2/universes/2783797267/developerproducts?limit=100 （S；11 条）
- EVH = https://apis.roblox.com/virtual-events/v1/universes/2783797267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA （S；带零起点游标 3 页共 60 条）；EV = 同接口不带游标（S；只回 3 条当前 / 未开始）
- RS = https://apis.roblox.com/virtual-events/v1/virtual-events/<eventId>/rsvps/counters （S）
- GR = https://groups.roblox.com/v1/groups/4548068 ；GR2 = /v2/groups?groupIds=4548068 ；RO = /v1/groups/4548068/roles ；GG = https://games.roblox.com/v2/groups/4548068/games?accessFilter=Public&limit=50 ；OW = https://users.roblox.com/v1/users/292262212 （S）
- AG = https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation （S；只接受 POST，不放进页面 sourceUrls，页面改放游戏页 PAGE）
- PAGE = https://www.roblox.com/games/7171174521/American-Plains-Mudding （S；匿名 HTML 只有描述，没有社交链接与更新日志）
- TH = https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=2783797267&countPerUniverse=10&size=768x432&format=Png ；IC = …/games/icons?universeIds=2783797267&size=512x512&format=Png ；ETH = https://thumbnails.roblox.com/v1/assets?assetIds=119697635046294,110368663107405&size=768x432&format=Png （S；宣传图，画面由本人看图描述）
- DOC = create.roblox.com/docs（passes / developer-products / badges / private-servers / experience-events / social-media-links / update-games，S；平台机制只引原文，原文存 `raw/docs/`）
- 试过一个未经官方证实的邀请线索，未采用、不记录。
- SG = Google 下拉 `raw/suggest.jsonl`（B；只作需求证据）
- W1 = americanplainsmudding.wiki；W2 = plainsmudding.wiki；W3 = southernmudding.wiki（B；只作 benchmark 与线索，正文不取任何事实；W1 的「无码 + Like/Favorite 送车」线索已回到 G 核实）

| 页 | 主来源 | 辅助 | 最高级 | sourceUrls 里的 S 级条数 | 素材状态 | 图片 |
|---|---|---|---|---|---|---|
| index | G、V、GR、BD、GP、DP、EVH、PAGE | — | S | 8 | 充足 | th1（封面）、th10、ev_map |
| guides（栏目） | 经子页 | — | S（经子页） | 0（栏目索引，照基准 sourceUrls 空） | 充足 | th5（只封面） |
| how-to-play | G（描述原文） | GP、BD、TH、PAGE | S | 5 | 可写：玩法清单、免费车、白名单、人数都有原文；**菜单名、键位、游戏币、免费车是哪辆未获取** → 正文按「目标」写步骤并列出未确认表 | th3、th8 |
| updates | EVH、EV、G | GP、DP、BD、RS、DOC | S | 8 | 充足（60 条 listing；listing 是日程不是上线记录，页内写明）；**每次更新的完整补丁说明未获取**（描述只留最新一段） | th2、ev_map |
| badges | BD | G、EVH、RO、DOC | S | 5 | 数据充足（名称、描述、累计、昨日、创建 / 编辑时间）；**隐藏车 / 隐藏拖车位置与车型未获取** → 页内明说不提供 | th6、th9 |
| gamepasses | GP | DP、DOC | S | 4 | 充足（8 个在售全部有官方描述；Premium Vehicles / Premium Trailers 的内含车辆未获取） | th4 |
| spawning | GP（5 段通行证描述） | DP、G | S | 3 | 可写：「4-8 slots」「cap of 8」「2x … Up To 16」为原话；**默认分配与单通行证槽数未获取**（round1：首稿的默认分配推导不成立，已删）；生成点位置、清车规则未获取 | th8 |
| private-servers | GP（Premium Private Servers 描述） | DP、BD、G（createVipServersAllowed: false）、DOC | S | 5 | 官方信息少但全部列出（3 条命令 + 2x slots）；**完整命令表、输入位置、私服价格未获取** → 正文明说只列 3 条 | th9 |
| limited-vehicles | GP（5 条未在售记录） | DP、EVH、DOC | S | 4 | 可写：名称、描述、建档日、3 个礼物价；**是哪辆车、在售价、2026 是否返场未获取** → 以 not stated / our inference 口径写 | th7 |
| vehicles | G、EVH（17 条写了内容的 listing） | GP、BD、TH | S | 5 | 可写：类型清单全部有原话与日期；**具体车名、车价、性能、解锁条件未获取** → 不做强度榜 | th10、th5 |
| community | GR、GR2、RO、GG、OW | G、V、DOC；SG、W1、W2（B，只作需求证据与「有两个非官方站」一句） | S | 8 | 充足；官方 Discord 写「无法确认」（社交链接 401）；两个 created 日期并列 | ev_map（封面）、th2 |
| author | — | — | — | 0（编辑方针页，照基准 sourceUrls 空） | — | th6（封面）、icon |
| （不建）codes / hidden-vehicle-locations / commands 全表 / map / controls | — | 社区视频、W1 | C / B | 0 | **素材不足 → 不建** | — |

悬而未决（不上线或只以并列口径上线）：见 `dossier.md` 第 11 节「未获取项」与第 12 节「互相矛盾 / 需要谨慎的地方」。
