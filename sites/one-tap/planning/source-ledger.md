# 页面素材来源记录表(One Tap)

规则:每页至少 1 个 S 或 A 级来源才开写;只有 B/C 的页 draft。本批 12 页里 9 页直接引用 S 级来源,3 页(两个栏目索引 + 作者页)照基准 sourceUrls 为空、事实全部来自子页;无 draft。独立于 S 的 A 级来源本轮 0 条(群组 shout null、wall 404、social links 401;开发者原话都已在 S 级的 description 与 6 条活动文本里)。B 级 0 条(无 Fandom / 成熟 wiki)。C 级 2 个抢注站只用于 benchmark,不进任何页面的事实。

来源缩写:
- G = https://games.roblox.com/v1/games?universeIds=9294074907 (S;description 全文 18 行、name、created、visits、playing、maxPlayers、genre_l1 / genre_l2)
- V = https://games.roblox.com/v1/games/votes?universeIds=9294074907 ;FV = https://games.roblox.com/v1/games/9294074907/favorites/count (S)
- GP = https://apis.roblox.com/game-passes/v1/universes/9294074907/game-passes?passView=Full&pageSize=100 (S;4 个,description 全空)
- PI = https://thumbnails.roblox.com/v1/assets?assetIds=126028198454624,128625042989986,126925465702985,130506004802111&size=700x700&format=Png (S;4 张通行证图标,图内文字本人看图抄录)
- DP = https://apis.roblox.com/developer-products/v2/universes/9294074907/developerproducts?limit=100 (S;97 个,Description 全空,nextPageCursor=null)
- DPI = https://thumbnails.roblox.com/v1/assets?assetIds=88963008124478&size=700x700&format=Png (S;97 个商品共用的占位图标)
- EV = https://apis.roblox.com/virtual-events/v1/universes/9294074907/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA (S;6 条。**不带游标的同一接口返回 0 条**,复核必须带游标)
- EVG = https://apis.roblox.com/virtual-events/v1/virtual-events/groups/1047647644 (S;群组维度的同一批 6 条,交叉路径)
- EI = https://thumbnails.roblox.com/v1/assets?assetIds=88388513445715,127182754594072,134947861539288,111201366562498,106005103409162,82429300588092&size=768x432&format=Png (S;活动配图)
- BD = https://badges.roblox.com/v1/universes/9294074907/badges?limit=100 (S;0 个,读 3 次)
- GR = https://groups.roblox.com/v1/groups/1047647644 ;GR2 = https://groups.roblox.com/v2/groups?groupIds=1047647644 ;ROLES = https://groups.roblox.com/v1/groups/1047647644/roles ;GG = https://games.roblox.com/v2/groups/1047647644/gamesV2?accessFilter=2&limit=100&sortOrder=Asc ;U = https://users.roblox.com/v1/users/9098936033 (S)
- SV = https://games.roblox.com/v1/games/90568084448279/servers/Public?limit=10 (S;时点值,round1 U2 后页面不再引用)
- LG = https://gameinternationalization.roblox.com/v1/supported-languages/games/9294074907 (S;18 种语言)
- AGE = https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation (S,只接受 POST → 不放进页面 sourceUrls,改放游戏页 URL)
- PG = https://www.roblox.com/games/90568084448279/One-Tap (S;游戏页 HTML:og:url、data-private-server-price)
- TH = https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=9294074907&countPerUniverse=10&size=768x432&format=Png ;IC = https://thumbnails.roblox.com/v1/games/icons?universeIds=9294074907&size=512x512&format=Png (S;官方图)
- DOC = create.roblox.com/docs(passes / developer-products / social-media-links / private-servers,S,平台机制只引原文)
- SG = Google 下拉(C,只作需求证据,不进页面)
- CP = onetap.wiki / onetaproblox.wiki(C,只作架构对比,不进页面)

| 页 | 主来源 | 辅助 | 最高级 | S/A 来源数(页面 sourceUrls 条数) | 素材状态 | 图片 |
|---|---|---|---|---|---|---|
| index | G、V、GR、GP、DP、EV | BD、LG、PG(承载 AGE 的分级)、DOC(passes) | S | 10 | 充足 | th1(封面)、icon、th3 |
| beginner(栏目) | G、EV(经子页) | — | S | 0(栏目索引,事实全部来自子页,sourceUrls 空,照基准) | 充足 | pass-2x-level-xp(封面 / 卡图) |
| how-to-play | G(描述原文) | EV(Update 2 的对局功能行)、GP + PI(Double Voting Value 图标)、TH | S | 5 | 充足(操作、计分、地图名、武器数值、bot 未获取 → 正文末节列出) | th2(封面)、th4 |
| rewards | G、EV、DP | GP、PI、DOC ×2、EI | S | 8 | 一手信息零散但全部列出(描述 1 行 + 活动 6 行 + 5 个商品 + 2 个通行证);任务清单 / 等级表 / 每日奖励未获取 → 正文明写 | ev-valentines(封面,正文也用)、pass-2x-level-xp |
| updates | EV、EVG | DP、GP(创建日)、G + GG(updated 字段两个值)、EI | S | 7 | 充足(6 条活动原文完整);实际上线时刻、lunar update 内容未获取 → 正文明写 | ev-summer(封面)、ev-update、ev-valentines |
| game-info | G、GR、GR2、ROLES、U、GG | V、FV、LG、BD、PG、EV、DOC ×2 | S | 14 | 充足;Discord 以 could not confirm 口径写;私服把页面属性 49 Robux 与 createVipServersAllowed=false 并列写出、不下结论(round1 U1) | icon(封面,正文也用)、th4 |
| robux(栏目) | GP、DP(经子页) | — | S | 0(栏目索引,同上) | 充足 | pass-2x-money(封面 / 卡图) |
| gamepasses | GP、PI | DP、G、EV、DOC ×2 | S | 7 | 充足(4 个通行证 description 为空,图标文字是唯一官方说明;效果细节未获取 → 正文明写未测试) | pass-2x-case-luck(封面,正文也用)、pass-2x-money、pass-double-voting-value |
| cases | DP | G(描述 1 行)、EV(4 行)、GP + PI(2x Case Luck)、DOC | S | 6 | 价格充足(49 条);内容 / 概率 / 非 Robux 获取途径未获取 → 末节列表 | th3(封面)、pass-2x-case-luck、ev-update |
| battle-pass | DP | EV(2 行赛季公告)、G、DOC、EI | S | 5 | 名称与价格充足(7 条);7 条都没有描述,「跳几层」「同属一个战令」只是名称读法 → 全页加限定(round1 U3–U7);层数 / 赛季时长 / 奖励未获取 → 末节列表 | ev-update(封面,正文也用)、ev-summer |
| shop | DP | DPI、GP、G、EV、DOC | S | 6 | 充足(97 条名称与价格);每条功能未获取 → 全页按 not confirmed 口径 | th4(封面)、th3、pass-2x-money |
| author | — | — | — | 0(编辑方针页,照基准 sourceUrls 空) | — | pass-double-voting-value(封面)、icon |
| (不建)codes | — | — | — | 0 | **官方来源 0 个码 → 不建** | — |
| (不建)skins / weapons / maps / aim-settings | — | — | — | 0 | **素材不足 → 不建**(无名单、无数值、无图名、无操作说明) | — |

悬而未决(不上线或只以并列口径上线):见 dossier.md「11. 互相矛盾 / 未核实」。
