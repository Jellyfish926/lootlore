# 对抗验证报告：+1 Stone Skipping（11 页 + entities.json / _images.json / config-snippet.json）
取证日期 2026-10-02 11:50 UTC 前后，全部自己重新联网取证（证据文件在 ev/ 下，属验证方自取）。作者的 raw/ 未作证据。

## 统计
- 命题总数 524（按台账分组计原子命题）；A 级 506，B 级 18。
- 抽样：B 级仅 18 条，且已出现 REFUTED，按规则转全量，B 级全验，抽样数 18/18（无剩余可抽）。全部 11 页均被全量过一遍。
- CONFIRMED 500 / REFUTED 4 / UNVERIFIED 20。UNVERIFIED 占 3.8%，取证条件充分。
- 11 页全部转全量（因 REFUTED 出现在 community / gamepasses / _images 元数据，其余页同样逐条验过）。
- 自抽一条 CONFIRMED 回点：create.roblox.com/docs/production/monetization/passes 页 meta 原文 "Passes let you charge users a one-time Robux fee ..." 与正文引语一致，通过。

## 已 CONFIRMED 的大块（只列分组，不逐条）
| 分组 | 条数 | 取证 |
|---|---|---|
| 通行证 11 行（名称逐字含括号/价格/创建日） | 11 | game-passes API |
| 开发者商品 78 行（名称/价格/在售/创建日） | 78 | developer-products API（78 条，nextPageCursor 空，76 在售，2 条无价） |
| 页内 89 行表格与接口逐行脚本对账 | 含上两项 | 0 处不一致 |
| 合计重算：2,353 / 174 / 947 / 763 / 469 / 20,195 / 16,375 / 3,820 / 5,980 / 4,489 / 67 / 27 | 12 | 自行重算 |
| 单位价与蛋捆绑折扣（69.0/65.0/83.2/8.3/18.1/18.7；111(31%)/251(18%)/193(41%)；35%；约 3 倍/4 倍） | 14 | 自行重算 |
| 活动：标题/副标题/描述三行/主办/类别/26 Sep 09:04/1 Oct 14:47、周六、7 个时区换算（PDT-7 EDT-4 BRT-3 BST+1 CEST+2 UTC+8 次日 00:00） | 20 | virtual-events API；DST 均在 11 月/10 月 25 日才切换 |
| updates 时间线 13 行、蛋表 6 行、「12 个不同日」「五天后」「5-7 天间隔」「Dragon 早 World 5 两天」 | 23 | dp/passes 创建时间 UTC |
| 游戏事实：6 行官方描述引语逐字、首行 "+1 Skipping Stones"、创建 5 Sep、10 人、Simulation / Incremental Simulator、免费、Badges 空、Maturity: Minimal + "Suitable for everyone"（POST get-age-recommendation 实测 200） | 14 | games / badges / age API |
| 群组：ID、owner iPlayfade、注册 2021-10-20、5 个角色及人数、开放加入、无认证、公开体验 1、tier 3←2 于 24 Sep、shout null、描述 "meow?"、universe/place ID | 14 | groups / users / games v2 API |
| 兑换码：游戏描述、群描述、shout、活动列表均无码；全部 11 页及 json 无任何码字符串（正则扫描） | 6 | 自扫 |
| 第三方站陈述：三家站确有 codes 页（stoneskipping.wiki/codes/、stone-skipping.wiki/codes、1stoneskipping.wiki/codes/1-stone-skipping-codes）；有 zone 列表（stoneskipping.wiki/zones/）；stone-skipping.wiki/updates 给出 World 4 日期（2026-09-27）。页面均未搬运对方内容 | 3 | 实取 |
| 官方文档引语：passes 页 "let you charge users a one-time Robux fee" 逐字；developer-products 页 "purchase more than once" 逐字 | 2 | create.roblox.com |
| 结构/SEO：11 页 title 49–55（40-60）、description 154–160（140-160，boosts 恰 160）、首段 49–56 词、站内链接 ≥4 且目标均存在、/contact 与 /editorial-policy 在 lootlore/out 存在、date/updated/reviewed 均 2026-10-02、author=Jellyfi、H1=title、无 draft:true | 77 | 脚本 |
| 图片：16 个 URL 现 curl 全 200、image/Png、全部 tr.rbxcdn.com；与 thumbnails 接口返回的 URL 一致；11 张 alt 非空且与实看画面相符；5 个商品/通行证图标 asset id 与接口一致 | 54 | curl + 目视 |
| entities.json 89 个 item/gamepass 实体逐条对接口（名称含 "Dragon Egg " 尾空格已入 name_api_raw、价格、在售、创建/更新日、id）+ 2 个 mechanic 实体；page_slug 与 entities 引用全部存在 | 91 | 脚本，0 差异 |
| 图标描述（Starter/Devil/King Doggy/三瓶药水/Dragon/Koi/Auto Wins 奖杯/Auto Rebirth 箭头/灰方块占位/宠物 +1+3+6） | 12 | 目视 |
| 其他（96% 重算 95.97%；群成员 > 2 倍收藏） | 2 | 重算 |

## 修改清单（只列 REFUTED 与 UNVERIFIED）
| 编号 | 文件 | 原句（逐字） | 问题 | 证据 | 改成什么 |
|---|---|---|---|---|---|
| R1 REFUTED | community.md | "That rating covers content, not spending." | 平台规则陈述无官方出处，且与官方文档相左：Roblox 内容成熟度体系含付费相关披露（paid random items、paid item trading 描述符与问卷） | https://create.roblox.com/docs/production/promotion/content-maturity 正文含 "Paid random items"、"Paid item trading" 问卷与描述符 | "That label describes the content of the experience; it does not tell you how much a player could spend." |
| R2 REFUTED | gamepasses.md | "each icon shows a themed strip of water with a platform" | Admin / Golden 图标是绿色科技感与金色的长条道+平台，看不到水；只有 Koi 有水 | 取 asset 94146387429754、101348892947756、106296448970415 缩略图目视（https://thumbnails.roblox.com/v1/assets?assetIds=...） | "the Koi icon shows a strip of water with cherry trees, a red gate and a platform; the Admin and Golden icons show a green and a gold lane with a platform" |
| R3 REFUTED | community.md | "Because we cannot see where they come from." | 第三方站明写出处（RoGameCodes、GameRant、视频），不是「看不到出处」；真相是没有一条追溯到官方帖 | https://stoneskipping.wiki/codes/ 页内 "reported by RoGameCodes and GameRant with screenshots" | "Because none of them traces back to an official Meow Labs post." 同段 "A code that fails costs you nothing, but a page full of codes nobody checked is not worth much." 改为 "A page full of codes nobody checked is not worth much."（"fails costs nothing" 无出处，见 U7） |
| R4 REFUTED | _images.json `_note` | "同栏目内不重复" | 映射实际重复：beginner 与 how-to-play 同为 Getting Started 且都用 art03；robux 与 pets 同为 Robux Shop 且都用 art02 | _images.json pages 字段 | 把 beginner→art01 或 art04、pets→art04 之类调换，或删掉该句说明 |
| U1 UNVERIFIED（高） | community.md tldr、"Can you play on a private server?" 整节；entities.json stone-skipping.key_notes_en | "Private servers are switched off, and a public server holds 10 players." / "No. The Roblox listing has private servers switched off, so every session is on a public server with up to 10 players." / "Private servers not allowed" | 依据 createVipServersAllowed=false 无效：该字段对已知提供私服的游戏也为 false | https://games.roblox.com/v1/games?universeIds=994732206,3317771874,2440500124 （Blox Fruits / Pet Simulator 99 / DOORS）全部 createVipServersAllowed=false；私服接口 /v1/games/111543903102439/private-servers 需登录 401 | tldr：改为 "A public server holds 10 players; we could not confirm whether private servers are offered."；该节正文改为 "We could not confirm it. The public listing gives 10 players per server, but its private-server field is unreliable, so open the Servers tab on the game page to see whether a private server option exists. Start times for the ADMIN ABUSE + WORLD 5 event are on the [updates page](/stone-skipping/updates/)."；entities 删除 "Private servers not allowed" |
| U2 UNVERIFIED | community.md 首段、tldr、表格行、"Is there an official Discord?" | "Roblox hides the game's social links from logged-out visitors" / "because Roblox shows social links only to logged-in users" / "Roblox shows an experience's social links only to logged-in users, and the request we can make without logging in is refused." | 只证明了接口无令牌返回 401，未证明网页端不向游客展示；无官方出处 | https://games.roblox.com/v1/games/10765298801/social-links/list → 401 "Authentication token is missing"（同接口对别的游戏也 401） | 统一改为 "the social-links request returns 401 (\"Authentication token is missing\") without a Roblox login, so we could not read the links"；表格行 "Not readable without logging in" 改 "Request refused with 401 without a login"；frontmatter scope 同步 |
| U3 UNVERIFIED | community.md 表格 | "Could not be read; Roblox returned an error to logged-out requests" 及 scope "the group wall need a Roblox login" | 实际为 404 空消息，不是 401；换另一群组同样 404，原因不明 | https://groups.roblox.com/v2/groups/207366578/wall/posts?limit=10 → 404 {"errors":[{"code":0,"message":""}]} | "Could not be read; the wall request returned a 404 error with no message"；scope 删 "need a Roblox login" 对墙的归因 |
| U4 UNVERIFIED | how-to-play.md | "In Roblox simulators a rebirth usually resets progress in exchange for a permanent bonus; here the developer has not said what is reset or what you gain." | 通用机制陈述无官方出处 | 无 | "The developer has not said what Rebirth resets or what you gain." |
| U5 UNVERIFIED | updates.md | "On Roblox that phrase usually means developers join live servers and hand out boosts or spawn things for the players present. That is how the genre uses the term, not a promise in this listing." | 通用平台/社区用语陈述无出处 | 无官方出处 | "The subtitle calls this the game's first admin abuse, but the listing does not explain what that involves." |
| U6 UNVERIFIED | community.md | "A group shout is where many Roblox developers post news and codes, so the group is worth following even though the shout is empty today." | 通用陈述无出处 | 无 | "Joining the group is free; its shout is empty today." |
| U7 UNVERIFIED | community.md | "A code that fails costs you nothing" | 无出处 | 无 | 删除该分句（见 R3） |
| U8 UNVERIFIED | gamepasses.md（及 frontmatter sourceUrls） | "so each of these is bought once per account. That is standard Roblox behaviour, not something specific to this game." | 文档只说 "one-time Robux fee"，未写「每账号一次」；且 sourceUrls 中 .../monetization/game-passes 现 301 跳到 .../monetization/passes | https://create.roblox.com/docs/production/monetization/game-passes → 301 → /passes | "so each of these is a one-time purchase."；sourceUrls 改成 https://create.roblox.com/docs/production/monetization/passes（boosts.md 的 sourceUrls 同改） |
| U9 UNVERIFIED | updates.md | "Unlike some Roblox games, this one sells no \"skip to world\" product whose creation date would mark each world." | 不存在性断言；shop.md 自己说 Golden Skip / Diamond Skip 所跳为何「not stated」，Golden Zone / Admin Zone 亦无说明，两页互相矛盾 | dp API 有 Golden Skip(12)、Diamond Skip(19)、Golden Zone(115)、Admin Zone(289)，均无描述 | "We found no store product whose name says it skips to a world, so no creation date marks a world; what Golden Skip, Diamond Skip, Golden Zone and Admin Zone do is not stated." |
| U10 UNVERIFIED | updates.md 首段 | "Meow Labs has not published patch notes, so the history below is rebuilt" | 绝对断言；官方 Discord/X 需登录未查 | 无 | "We found no patch notes from Meow Labs, so the history below is rebuilt" |
| U11 UNVERIFIED | how-to-play.md tldr | "an official event on 3 October 2026 adds World 5" | 活动描述仅有一行 "- World 5"，「adds」是推断 | virtual-events API description "- Admin Abuse\n- World 5\n- New features" | "an official event on 3 October 2026 lists World 5" |
| U12 UNVERIFIED | author.md | "Zone names, pet boosts, egg odds and rebirth costs only appear on fan sites today" | 区域名与蛋概率确见于第三方站（stoneskipping.wiki/zones/、/pets/）；宠物具体倍率与 rebirth 费用我未在所取页找到（/rebirth 404） | 同左 | "Zone names and egg odds appear only on fan sites today; pet boosts and rebirth costs are not published in any official source we can read, so they stay out until they can be checked in the live game or in an official post." |
| U13 UNVERIFIED | index.md、community.md | 11:19 UTC 快照：20,948 在线、5,252,489 visits、202,909 收藏、10,362 / 435 赞踩、481,097 群成员 | 时点数据无法回溯。11:50 UTC 实测：22,204 / 5,291,083 / 204,622 / 10,425 / 437 / 484,476，方向合理但不能证实 11:19 的值 | games / votes / groups API | 保留并留存原始响应；上线前若隔天发布，把时点改成实际读取时点或刷新数值 |
| U14 UNVERIFIED | author.md | "Every guide published under that byline is listed below." / 'Under the heading of each article, "Published" ... "Last checked"' | 文件内无列表与这两个标签，依赖渲染模板 | lootlore 另一游戏 author.md 有同样措辞（模板约定） | 构建后在渲染产物里核对列表与标签存在 |

## 小问题（不属 REFUTED，建议顺手改）
- 活动时间：接口为 16:00:15–18:00:15 UTC，页面写 16:00–18:00，可在 updates 表注一句 "listing shows 16:00:15"，或保持取整。
- "a span of 22 days"（10 Sep–1 Oct）：按日历含首尾是 22，按间隔是 21。建议 "within 22 calendar days"。
- updates / community "新增的蛋每 5–7 天"：共 3 个间隔（7、7、5），样本小，已用 "roughly" 可保留。
- 结构：config-snippet.json、entities.json、_images.json 除 R4 外无差错；image 实际 767x432，作者已自注。

## 哪些页在问题修完前保持 draft
| 页 | 保持 draft 原因 | 阻塞项 |
|---|---|---|
| community.md | 含平台规则/安全类错误陈述，读者会据此买入私服或判断分级 | R1、R3、U1、U2、U3、U6、U7 |
| updates.md | 含自相矛盾与未证实断言；另需在 2026-10-03 16:00 UTC 前上线才有意义，4 日要改过去时 | U5、U9、U10 |
| gamepasses.md | 图标描述不实、官方文档推论越界、sourceUrls 过期 | R2、U8 |
| how-to-play.md | 通用机制句无出处；tldr 推断写成事实 | U4、U11 |
| author.md | 方法论里一句关于第三方站的陈述不全属实 | U12、U14（渲染后核） |
| entities.json / _images.json | 私服字段、_note 不实 | U1、R4 |

可先放行：shop、boosts、pets、robux、beginner、index（价格、日期、计数、名称全部 CONFIRMED；index 仅含 U13 的时点数据，风险低）。注意 index 的 FAQ 与 beginner 链接到 community / updates，放行后这两页保持 draft 会产生死链，建议这几页与其链接目标同批上线或暂去链接。
