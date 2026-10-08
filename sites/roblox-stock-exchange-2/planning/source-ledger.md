# 页面素材来源记录表

规则:每页至少 1 个 S 或 A 级来源才开写;只有 B/C 的页 draft。本批 12 页全部有 S 级来源,无 draft。A 级来源本轮 0 条(群组 description 空、shout null、wall 404、social links 401)。

来源缩写:
- G = https://games.roblox.com/v1/games?universeIds=10495391267 (S)
- V = https://games.roblox.com/v1/games/votes?universeIds=10495391267 (S)
- AGE = https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation (S,只接受 POST,GET 返回 404 → round1 起不放进页面 sourceUrls,改放游戏页 https://www.roblox.com/games/110527353762049/Roblox-Stock-Exchange-2;claims.md 仍标注 POST 取证)
- BD = https://badges.roblox.com/v1/universes/10495391267/badges?limit=100 (S)
- GP = https://apis.roblox.com/game-passes/v1/universes/10495391267/game-passes?passView=Full&pageSize=100 (S)
- DP = https://apis.roblox.com/developer-products/v2/universes/10495391267/developerproducts?limit=100 (S)
- EV = https://apis.roblox.com/virtual-events/v1/universes/10495391267/virtual-events (S;round1 起页面 sourceUrls 用不带游标的地址。2026-10-08 03:39 不带游标只回 2 条,04:19 之后多次回 12 条;raw 存档是带零起点游标取的 12 条)
- ETH = https://thumbnails.roblox.com/v1/assets?assetIds=…&size=768x432&format=Png(官方活动配图,S;图中文字本人看图抄录)
- TH = https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=10495391267&countPerUniverse=10&size=768x432&format=Png (S,宣传图)
- GR = https://groups.roblox.com/v1/groups/33446529 ;GR2 = /v2/groups?groupIds=33446529 ;ROLES = /v1/groups/33446529/roles ;GG = https://games.roblox.com/v2/groups/33446529/games?accessFilter=Public&limit=50 ;U = https://users.roblox.com/v1/users/6019489864 (S)
- DOC = create.roblox.com/docs(passes / developer-products / badges / experience-events / social-media-links,S,平台机制只引原文)
- DC = https://discord.com/api/v9/invites/qR8v6Murp3?with_counts=true (B,服务器自述)
- SG = Google 下拉(B,只作需求证据)
- C1 = robloxden.com;C2 = tryhardguides.com;C5 = robloxstockexchange2.wiki(C,只当线索与矛盾对照)。round1 修订:twinfinite.net / progameguides.com 验证员取证 403、无法独立复核,页面上已不再引用,只留在 benchmark / dossier 的调研记录里

| 页 | 主来源 | 辅助 | 最高级 | S/A 来源数 | 素材状态 | 图片 |
|---|---|---|---|---|---|---|
| index | G、V、GR、BD、GP、DP、EV、AGE | — | S | 8 | 充足 | th5(封面)、th1 |
| beginner(栏目) | G、BD、GP、EV(经子页) | — | S | 0(栏目索引,事实全部来自子页,sourceUrls 空,照基准) | 充足 | th4 |
| how-to-play | G(描述原文) | BD、GP、DP、EV、TH、AGE | S | 7 | 充足(界面按钮位置只按宣传图写并标未核实;手续费/杠杆基础值未获取) | th2、th4 |
| codes | G(描述里的码) | V、GR、EV;C1、C2(只作「别站怎么说」对照) | S | 4 | 充足(码 1 个,未进游戏实测;奖励官方未写 → 如实写 Not stated) | th4(只封面) |
| badges | BD | G、DP、DOC | S | 4 | 充足(解锁条件只有官方一句话;rebirth / bot 门槛未获取) | th3 |
| updates | EV、ETH | G、GP、DP、BD、DOC | S | 7 | 充足(listing 是预告,不证明上线时刻;配图数值标明出自宣传图) | ev_office、ev_seasons、ev_bonds |
| community | GR、GR2、ROLES、GG、U | G、V、EV、DOC;DC(B);C2、C5(C) | S(群组)/ B(Discord) | 9 | 充足;Discord 以「calls itself official」口径写 | th5、ev_ui |
| robux(栏目) | GP、DP、DOC(经子页) | — | S | 0(栏目索引,同上) | 充足 | ev_ui |
| gamepasses | GP | DP、DOC、ETH | S | 5 | 充足(13 个都有官方描述;基础手续费/杠杆未获取) | ev_ui、ev_tools |
| shop | DP | GP、DOC、TH、ETH | S | 4 | 名称与价格充足;31 个里 30 个无描述 → 正文逐项写 not stated | th1、ev_challenges |
| algo-bots | G、BD、DP、GP、EV、ETH | SG(需求证据) | S | 6 | 官方信息少但全部列出;设置项/收益/解锁条件未获取 → 正文明说没有官方设置 | ev_hedge、ev_script |
| author | — | — | — | 0(编辑方针页,照基准 sourceUrls 空) | — | th5、icon |
| (不建)bot-settings / rebirth / markets | — | 社区视频、C5 | C | 0 | **素材不足 → 不建** | — |

悬而未决(不上线或只以并列口径上线):见 dossier.md「互相矛盾」「未核实」两节。
