# 页面素材来源记录表(Get Your Driver's License!)

规则:每页至少 1 个 S 或 A 级来源才开写;只有 B/C 的页 draft。本批 11 页里 8 页直接引用 S 级来源,3 页(两个栏目索引 + 作者页)照基准 sourceUrls 为空、事实全部来自子页;无 draft。A 级来源本轮 0 条(群组 description 空、shout null、wall 404、social links 401、官方活动 0 条)。C 级 0 条(未检索到任何视频评论 / 论坛帖 / 攻略文)。

来源缩写:
- G = https://games.roblox.com/v1/games?universeIds=10768565603 (S;description 全文、created、visits、playing、maxPlayers、genre)
- V = https://games.roblox.com/v1/games/votes?universeIds=10768565603 (S)
- GP = https://apis.roblox.com/game-passes/v1/universes/10768565603/game-passes?passView=Full&pageSize=100 (S;5 个)
- DP = https://apis.roblox.com/developer-products/v2/universes/10768565603/developerproducts?limit=100 (S;13 个,每个都有官方描述)
- BD = https://badges.roblox.com/v1/universes/10768565603/badges?limit=100&sortOrder=Asc (S;0 个,读 4 次)
- EV = https://apis.roblox.com/virtual-events/v1/universes/10768565603/virtual-events (S;0 条,带游标与不带游标各一次)
- GR = https://groups.roblox.com/v1/groups/356677783 ;GR2 = /v2/groups?groupIds=356677783 ;ROLES = /v1/groups/356677783/roles ;GG = https://games.roblox.com/v2/groups/356677783/gamesV2?accessFilter=2&limit=100&sortOrder=Asc ;U = https://users.roblox.com/v1/users/10383353739 (S)
- LG = https://gameinternationalization.roblox.com/v1/supported-languages/games/10768565603 (S;18 种语言)
- AGE = https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation (S,只接受 POST → 不放进页面 sourceUrls,改放游戏页 URL)
- TH = https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=10768565603&countPerUniverse=10&size=768x432&format=Png ;IC = https://thumbnails.roblox.com/v1/games/icons?universeIds=10768565603&size=512x512&format=Png ;AT = https://thumbnails.roblox.com/v1/assets?assetIds=…&size=420x420&format=Png (S;官方图,图中文字本人看图抄录)
- DOC = create.roblox.com/docs(passes / developer-products / social-media-links / content-maturity,S,平台机制只引原文)
- RM = https://www.rolimons.com/game/104416416393862 ;RT = https://rotrends.com/game/10768565603 (B,统计站)
- SG = Google 下拉(B,只作需求证据)

| 页 | 主来源 | 辅助 | 最高级 | S/A 来源数 | 素材状态 | 图片 |
|---|---|---|---|---|---|---|
| index | G、V、GR、GP、DP、LG | AGE(经游戏页 URL) | S | 7 | 充足 | th1(封面)、icon、prod-skip-to-end |
| beginner(栏目) | G、GP、DP(经子页) | — | S | 0(栏目索引,事实全部来自子页,sourceUrls 空,照基准) | 充足 | prod-skip(封面 / 卡图) |
| how-to-play | G(描述原文)、DP | GP、LG、AT、游戏页;RM(B,平均游玩时长一句,标明第三方) | S | 6 | 充足(笔试内容、考场路线未获取 → 正文明写不覆盖) | prod-retake-test(封面)、prod-skip-test、prod-revenge |
| waiting-line | DP | G、DOC、AT | S | 4 | 充足(队伍长度、等候室总时长、Skip To End 是否跳笔试未获取 → 文末列出) | prod-kill(封面)、prod-skip、prod-kill-all |
| driving-test | G、DP | BD、TH、IC、DOC | S | 6 | 一手信息少但全部列出(障碍 3 个名词、结局 2 个名字、Retake Test、考官 2 个商品);路线 / 评分 / 结局全表未获取 → 文末列表 | prod-plus-minute(封面)、prod-retake-test、prod-examiner |
| community | GR、GR2、ROLES、U、GG | G、V、EV、DOC;RM、RT(B,只在「Is there an official wiki?」里点名) | S | 11 | 充足;Discord 以「could not confirm」口径写 | icon(封面,正文也用) |
| robux(栏目) | GP、DP、DOC(经子页) | — | S | 0(栏目索引,同上) | 充足 | prod-vip-ticket(封面 / 卡图) |
| cars | G、DP | DOC、AT、IC | S | 5 | 一手只有 6 句话,全部列出;18 辆车名 / 档位表 / 概率 / The Loop 未获取 → 文末「What still has to be checked in the game?」表 | prod-golden-supercar(封面,正文也用)、prod-vip-ticket |
| gamepasses | GP | DP、DOC、AT | S | 5 | 充足(5 个都有官方描述;效果细节未获取 → 正文明写未测试) | pass-time-out(封面)、pass-gravity-gun、pass-ban-hammer |
| shop | DP | GP、G、DOC、AT | S | 5 | 充足(13 个都有官方描述) | prod-revenge(封面)、prod-scare-all、prod-plus-minute |
| author | — | — | — | 0(编辑方针页,照基准 sourceUrls 空) | — | prod-examiner(封面)、icon |
| (不建)codes | — | — | — | 0 | **官方来源 0 个码 → 不建** | — |
| (不建)written-test / endings | — | — | — | 0 | **素材不足 → 不建**(written-test 连 B/C 都没有;endings 只有 2 个名字) | — |

悬而未决(不上线或只以并列口径上线):见 dossier.md「10. 互相矛盾」「11. 未核实」两节。
