# 对抗验证 round1 —— Roblox Stock Exchange 2 十二页英文攻略

验证员:独立 subagent;取证日期 2026-10-08 04:19–04:55 UTC;被验对象 `PACK/content/en/*.md`(12 页)+ claims.md(467 条)+ entities.json + _images.json + config-snippet.json。取证全部重新请求线上来源,原始文件在 `evidence/`;raw/ 仅用于核对作者当时抄写。

**一句话:467 条作者命题全部验完(含 A 级 418 条 + 其余 49 条;因出现 REFUTED 而转全量),CONFIRMED 450 / REFUTED 1 / UNVERIFIED 16;另挖出漏列命题 53 条:CONFIRMED 2 / REFUTED 9 / UNVERIFIED 42。**

抽样记录:A 级(数字/价格/日期/名称/兑换码/开发者原话/规则/列表字段,共 418 条)全验;「其他」类 49 条按规定抽 30%,`random.seed(20261008)`、`random.sample(其他类编号, 15)` 得编号 49, 50, 76, 107, 115, 129, 133, 135, 136, 137, 229, 260, 261, 275, 298;验到 REFUTED 后该批已转全量,实际 49 条全部验证,抽样名单仅作记录。

## 0. 结论速览

- 数字/价格/日期/名称/描述原文的**事实层几乎全部对得上**(13 pass、31 product、11 badge、12 event、全部价格、徽章/通行证/商品名含 "Instant Acension"、"permeant" 的官方原拼写、时区换算、算术)。
- 问题集中在**推断写成确认的句子**:codes 页 "working"、兑换步骤、基础离线 8 小时/2 家公司、"每周更新"、时间跳转/AI Tokens 功能、bot 佣金按笔等;以及 10 条 REFUTED:gamepasses meta description "four passes that cost more as products"(实为 3 贵 1 便宜)、community "Nothing … says that joining the group gives an in-game reward"(Legacy 描述有 $10,000 入群奖励)、index+community "only developer text"(2 处)、community "every number here names the Roblox record"、beginner tldr "Every number … comes from Roblox official data"、author "Every guide … is listed below"、algo-bots meta description "no best settings exist"、index "each one has a specific description"(Bundle 例外)、community 表 INDEFINITE 名称缺 emoji。
- 未见现实投资建议口吻;未见声称与 Roblox/开发者有官方关系(index 末节明确 "not affiliated")。游戏内玩法建议(Try a short…、Leave futures for later)有"our suggestion"限定且有 simulated 声明,风险低。

## 1. 每页小结

| 页面 | 验证条数(作者表) | CONFIRMED | REFUTED | UNVERIFIED | 漏列命题(C/R/U) | 是否转全量 | 建议 |
|---|---|---|---|---|---|---|---|
| index | 55 | 55 | 0 | 0 | 0/2/5 | 是(全局出现 REFUTED,全部转全量) | 改后可发布 |
| how-to-play | 52 | 50 | 0 | 2 | 0/0/3 | 是(全局出现 REFUTED,全部转全量) | 改后可发布 |
| beginner | 10 | 9 | 0 | 1 | 0/1/0 | 是(全局出现 REFUTED,全部转全量) | 改后可发布 |
| codes | 36 | 27 | 0 | 9 | 0/0/6 | 是(全局出现 REFUTED,全部转全量) | 改后可发布(优先改 "working"/兑换步骤) |
| badges | 58 | 58 | 0 | 0 | 0/0/4 | 是(全局出现 REFUTED,全部转全量) | 改后可发布 |
| updates | 52 | 52 | 0 | 0 | 1/0/2 | 是(全局出现 REFUTED,全部转全量) | 改后可发布 |
| community | 40 | 38 | 1 | 1 | 0/3/3 | 是(全局出现 REFUTED,全部转全量) | 改后可发布(含 3 处 REFUTED) |
| gamepasses | 57 | 57 | 0 | 0 | 0/1/4 | 是(全局出现 REFUTED,全部转全量) | 改后可发布(含 meta description REFUTED) |
| shop | 63 | 62 | 0 | 1 | 0/0/4 | 是(全局出现 REFUTED,全部转全量) | 改后可发布 |
| algo-bots | 29 | 29 | 0 | 0 | 0/1/7 | 是(全局出现 REFUTED,全部转全量) | 改后可发布 |
| robux | 12 | 11 | 0 | 1 | 0/0/1 | 是(全局出现 REFUTED,全部转全量) | 改后可发布 |
| author | 3 | 2 | 0 | 1 | 0/1/1 | 是(全局出现 REFUTED,全部转全量) | 改后可发布({{BRAND}} 必须处理) |
| (跨页/frontmatter) | - | - | - | - | 1/0/2 | - | gameVersion、sourceUrls |

## 2. 统计

- 作者命题总数 467;实际验证 467;CONFIRMED 450;REFUTED 1;UNVERIFIED 16(UNVERIFIED 比例 3.4%,远低于 1/3,取证条件充分)。
- 漏列命题 53 条:CONFIRMED 2 / REFUTED 9 / UNVERIFIED 42。
- 抽样种子 20261008(见上)。
- 取不到的来源:twinfinite.net、progameguides.com(HTTP 403,Cloudflare 拦截,未绕过);Roblox 群组 wall(404)、game social-links(401 需登录)——后两者作者页面已如实写明,我复现了同样的错误码。

## 3. 漏列命题表(claims.md 没列的事实断言)

| 编号 | 页面 | 原句 | 类型 | 取证与依据 | 结论 | 原句 → 改成什么 |
|---|---|---|---|---|---|---|
| M1 | index | FAQ: "Is there a working code?" → "Yes. The official game description lists one code, TOOLS, and says the next code releases at 15,000 likes." (also frontmatter description "the one working code") | 规则/兑换码 | description 确有 TOOLS;但无人在游戏内实测,且 description 仍写 "THANKS FOR 10K LIKES" 而现有赞已 12,0xx,文本可能早于现状 | UNVERIFIED | FAQ question → "Is there a code?"; answer → "Yes. The official game description prints one code, TOOLS, and says the next code releases at 15,000 likes. We have not tested whether it redeems in the game." description → "…the one code printed in the official description, all 13 game passes with prices, 11 badges, …" |
| M2 | codes | seoTitle "Roblox Stock Exchange 2 Codes (October 2026): Working Code" | 名称 | 同上 | UNVERIFIED | seoTitle → "Roblox Stock Exchange 2 Codes (October 2026): TOOLS and Next Code" |
| M3 | index | "each one has a specific description: 24 hours of offline market time instead of 8, up to 50x leverage at any level, 0.02% fees."(前一句 "The 13 game passes are one-time purchases, priced from 39 to 999 Robux, and each one has a specific description") | 列表字段 | All Gamepasses Bundle 的描述只有 "All gamepasses, but at a lower cost.",并不 specific(robux 页自己写 "One line") | REFUTED | "…and each one has a specific description" → "…and twelve of them have a specific description" |
| M4 | index | "Its description is empty and it has no pinned shout, so the game description and the event listings are the only developer text we can quote." | 规则 | pass 描述(13)、徽章文本(11)、商品描述(1)、Legacy 游戏描述都是开发者文本,本站自己在多页引用;community 页 tldr 同句 "so the game description and event listings are the developer's only public text on Roblox" | REFUTED | → "…so the game description, the pass, badge and product texts, and the event listings are the developer text we can quote." (community tldr 同改) |
| M5 | index | "Facts come from Roblox's own records for the game: its description, badges, passes, store products and event listings."(How this guide uses its sources) | 规则 | community 页含 Discord 人数与第三方码站内容(已标注来源),不完全来自 Roblox 记录 | UNVERIFIED | → "Game facts come from Roblox's own records … ; the few Discord and code-site figures are labelled as such." |
| M6 | index | "You start with a small account and grow it by trading simulated stocks, ETFs, futures and IPOs, then add algorithmic bots, levels and rebirths."(how-to-play 同:"Algorithmic bots, levels and rebirths come later") | 规则 | description 只是并列功能清单,没有先后顺序 | UNVERIFIED | "then add algorithmic bots, levels and rebirths" → "with algorithmic bots, levels and rebirths on top"; how-to-play "come later" → "are also listed" |
| M7 | index | H2 "What can you trade?" 下表把 Hedge funds / Real estate / Bonds / Commodities 列为可交易项,"Since August the developer has announced more through official Roblox events." | 规则 | 事件文案: "Run a hedge fund"、"buy real estate"、"Trade debt…"、"Prices will be driven by…" —— 是预告,且 Hedge funds 描述不是交易品种 | UNVERIFIED | H2 → "What has the developer announced beyond the four markets?",表头 Event start → "Announced (event start, 2026)" |
| M8 | how-to-play | "The badge totals show the order most players follow." | 规则 | 徽章总数只能显示各步骤的到达比例,不显示玩家先后顺序(Hundred Trades 13.1% 高于 First Futures 9.4% 即说明徽章顺序≠到达顺序) | UNVERIFIED | → "The badge totals show how many players have reached each step; they do not show the order players do things in." |
| M9 | how-to-play | "1. **Redeem the code.** TOOLS is printed in the official description."(第一步)及 beginner 表 "Redeem TOOLS \| It is free and official"、"Then redeem the one official code" | 规则 | 码在 description 中,但游戏内兑换未验证,奖励未知 | UNVERIFIED | "Redeem the code." → "Try the code if you like."; beginner "Redeem TOOLS \| It is free and official" → "Try TOOLS \| It is printed in the official description (untested)" |
| M10 | how-to-play | "The official art above is the best public look at the trading screen." | 其他 | "best" 比较级,无依据;th2 与 ev_ui(终端截图)都是公开图 | UNVERIFIED | → "The official art above is one public look at the trading screen." |
| M11 | codes | Step list: "2. Find the code box in the game's menus." / "4. Confirm, then check your balance." | 规则 | 代码框位置/存在仅来自第三方码站(C 级);奖励官方未写,"check your balance" 预设奖励是现金 | UNVERIFIED | "2. Find the code box in the game's menus." → "2. Look for a code-entry box; no official source says where it is." / "4. Confirm, then check your balance." → "4. Confirm and see what the game tells you; the description does not say what TOOLS gives." |
| M12 | codes | "Learn the basics before you put the reward into a leveraged trade."(What should you do after redeeming?) | 规则 | 预设奖励可用于杠杆交易(奖励未知) | UNVERIFIED | → "Learn the basics before you use leverage." |
| M13 | codes | "If you try them, you lose nothing but a minute."(六个他站码) | 规则 | 无依据的"零风险"断言 | UNVERIFIED | → delete the sentence, or "If you try them, treat the result as unconfirmed." |
| M14 | codes | "Replaced. … If TOOLS is gone, the developer has moved on to the next code." | 规则 | 推断:码消失 ≠ 开发者发了下一个码(可能只是删除/改文案) | UNVERIFIED | → "If TOOLS is gone, the developer has changed the description; check whether a new code is printed there." |
| M15 | codes | "If you want the next code sooner, the description asks for exactly one thing: \"Like and favorite the game for future updates!\"" | 规则 | 原句是两个动作(like and favorite),且是 "for future updates" 的号召,并非针对码的触发条件(触发条件是 15,000 likes) | UNVERIFIED | → "The next code is tied to the like count. The description also asks players to \"Like and favorite the game for future updates!\"" |
| M16 | gamepasses | "Before spending, redeem the free code on the codes page." | 规则 | 同 codes:预设可兑换、"free" 奖励 | UNVERIFIED | → "Before spending, check the codes page for the code printed in the description." |
| M17 | badges | "First Short and First Futures Trade need you to use a part of the game many players never open." | 规则 | 徽章文本只说明做过什么;"many players never open" 是对低占比的解读 | UNVERIFIED | → "First Short and First Futures Trade need you to try shorting or futures; the low totals suggest many players have not." |
| M18 | badges | "It counts trades, not profit, so it comes with time."(Hundred Trades) | 规则 | 徽章文本 "You completed your first 100 trades!" 未说明是否排除亏损单/是否只计某类交易 | UNVERIFIED | → "The text counts completed trades; it does not mention profit." |
| M19 | badges | "On that one day, shorts and futures trades were being discovered far more often than the lifetime shares suggest." | 数字 | past-day 比值=当日某徽章授予数/当日 Welcome 授予数;分子含老玩家补拿,不能等同"新玩家发现率" | UNVERIFIED | → "On that day, First Short and First Futures Trade were awarded 63.7 and 40.1 times per 100 Welcome awards. The data does not show whether these went to new or returning players." |
| M20 | badges | "Roblox recorded 5,093,566 visits, which include repeat sessions." | 规则 | "visits 含重复进入" 无来源引用(Roblox 文档未在本页来源列表) | UNVERIFIED | → cite the Creator Hub definition of visits, or delete "which include repeat sessions" |
| M21 | gamepasses | Meta description: "…the 999-Robux bundle maths, and four passes that cost more as products." 及 H2 "Why do some passes cost more as products?" | 数字 | 表内:Watchlist Pro 49→99、Order Flow 199→249、VIP 229→399(更贵,3 个);Executive Terminal 159→139(更便宜)。"four passes that cost more" 错 | REFUTED | description → "…the 999-Robux bundle maths, and four passes whose product price differs."; H2 → "Why do four passes have a different product price?"; answer first line → "The store lists eleven of the passes twice, and in four cases the two prices differ. The listings do not say why." |
| M22 | gamepasses | "A single Simulate Day costs 39 Robux in the shop, so that last perk has a visible value."(shop 页:"One official line puts a value on a day.") | 规则 | 把 VIP 描述的 "Sim Day" 等同于商品 "Simulate Day" 是推断;两处描述均无关联 | UNVERIFIED | → "If a \"Sim Day\" is the same thing as the Simulate Day product (39 Robux), that perk would be worth that much; the listings do not say so." (shop: "One official line may put a value on a day.") |
| M23 | gamepasses | "Each pass has a specific official description, so you can see what you are paying for."(首段) | 列表字段 | Bundle 描述仅 "All gamepasses, but at a lower cost." | UNVERIFIED | → "Twelve of the thirteen passes have a specific official description." |
| M24 | gamepasses | "Pro Trader names a fee rate; if fees are eating your results, it is the one pass that addresses them." | 规则 | 无基础费率,无法知道 0.02% 是否低于默认费率;"addresses" 预设降费 | UNVERIFIED | → "Pro Trader names a fee rate (0.02%). The fee without the pass is not published, so we cannot say how much it changes." |
| M25 | shop | "Their names say it. … Simulate Day (39) and Simulate Week (99) move the simulation forward by a day or a week."(What do the time skips do?);"Skip to Market Open (9 Robux) implies the market has opening hours and that you can wait for them or pay." | 规则 | 31 个商品里只有 Trader Pass 有描述;时间跳转功能纯由名字推出,写成了确定句 | UNVERIFIED | "Their names say it." → "Their names suggest it, but none has an official description."; "move the simulation forward" → "appear to move the simulation forward" |
| M26 | shop | th1 caption: "Official promotional art: the market has an open state, which is what Skip to Market Open refers to" | 规则 | 图上只有 MARKET OPEN 标签;"which is what Skip to Market Open refers to" 为推断 | UNVERIFIED | → "Official promotional art: the card carries a MARKET OPEN label. The Skip to Market Open product has no official description." |
| M27 | shop | "So for 199 Robux you get a premium reward track, named The Golden Bell, with 22 animated cosmetic items and 20,000 AI tokens." | 名称 | 原文 "the premium track of Trader Pass Season 1, The Golden Bell" 中 The Golden Bell 更可能是赛季名,不一定是轨道名;"cosmetic items" 为 "animated exclusives"+"Cosmetic only" 的组合 | UNVERIFIED | → "So for 199 Robux you get the premium track of Trader Pass Season 1, \"The Golden Bell\": 22 animated exclusives and 20,000 AI tokens. The developer says it is cosmetic only, with no cash or boosts." |
| M28 | shop | "The tokens appear to pay for SummitAI, the assistant named in one pass." / "…which tells you free use is capped." | 规则 | 无官方文字把 AI Tokens 与 SummitAI 关联;"appear to" 未说明依据 | UNVERIFIED | → "No official text says what the AI Tokens are used for. The Unlimited AI Usage pass mentions SummitAI and \"no daily or weekly cap\", and the Trader Pass includes 20,000 AI tokens." ("free use is capped" → delete) |
| M29 | algo-bots | "From those lines we can say … that they scan markets, and that they pay a commission on what they do." | 规则 | Executive Terminal 原文是 "private market algorithmic bot scans"(歧义:可能是对私有市场的扫描功能);commission 来自宣传图 | UNVERIFIED | → "From those lines we can say that bots are created by the player, that they can be upgraded, that the Executive Terminal pass mentions \"bot scans\", and that the Hedge Funds art mentions bot commission." |
| M30 | algo-bots | "4. Count the commission. The HEDGE FUNDS event art shows that bots pay one, so a bot that trades more often also pays more often." | 规则 | art 只写 "your bots pay less commission",未说明按笔收取 | UNVERIFIED | → "4. Watch the commission. The Hedge Funds art mentions a bot commission; it does not say how it is charged." |
| M31 | algo-bots | "These figures come from promotional art made for the update. They show what the developer intended to ship" | 规则 | "intended to ship" 为动机推断(同页 updates 说 "numbers in it are illustrations") | UNVERIFIED | → "They show what the art displays, and the live numbers may differ." |
| M32 | algo-bots | "If the art still holds, a bot-heavy player would pick Quant and a manual trader Momentum." | 规则 | 基于宣传图文字的玩法推荐,无实测 | UNVERIFIED | → "The art pairs Quant with bots and Momentum with manual closes." |
| M33 | algo-bots | meta description: "…and why no best settings exist." | 规则 | "不存在最佳设置" 是绝对判断;官方只是没发布 | REFUTED | → "…and why we publish no best settings." |
| M34 | algo-bots | tldr: "Any list of best bot settings is community testing." | 规则 | 对没读过的清单下定性 | UNVERIFIED | → "The developer has published no bot settings; any list of best settings you find is unofficial." |
| M35 | algo-bots | "Whatever such a search turns up is one player's result on one account, in one stretch of the market." | 规则 | 对未读搜索结果下定性 | UNVERIFIED | → "Such lists are unofficial and we have not verified any of them." |
| M36 | algo-bots | "It lists every official line about bots in Roblox Stock Exchange 2"(开头段) | 规则 | 全称断言;作者未覆盖 Roblox 全部官方文字(如游戏页媒体/问答) | UNVERIFIED | → "It lists the official lines about bots that we could find" |
| M37 | community | "…its own profile description is empty, so the group tells you little about who the developers are. … The owner account is called SummitGroupHoIder, which reads like a holding account" | 规则 | "reads like a holding account" 是猜测 | UNVERIFIED | → delete "which reads like a holding account" |
| M38 | community | "And with an empty description and no shout, the group page carries no codes, links or rules." | 规则 | groups API 返回 hasSocialModules:true,wall 404、社交链接 401,作者自己也读不到;"no links or rules" 不可证 | UNVERIFIED | → "And with an empty description and no shout, the group description and shout carry no codes. We could not read the group wall or any social links." |
| M39 | community | "Nothing in the official text we read says that joining the group gives an in-game reward." | 规则 | 反例:同组 Legacy: Roblox Stock Exchange 的官方描述写 "Join the Main Group for a $10,000 starting cash bonus!"(现取 games v1 universeIds=7757905683),而本页前文正引用了该描述 | REFUTED | → "Roblox Stock Exchange 2's description does not mention a group reward. The Legacy game's description does offer a \"$10,000 starting cash bonus\" for joining \"the Main Group\"; that is the older game, not the sequel." |
| M40 | community | tldr: "…so the game description and event listings are the developer's only public text on Roblox." | 规则 | 同 index:pass/徽章/商品/Legacy 描述也是开发者文本 | REFUTED | → "…so the game description, pass, badge and product texts and the event listings are the developer text we can read." |
| M41 | community | "This guide is also unofficial; the difference is that every number here names the Roblox record it came from." | 规则 | 本页有 Discord 数字、第三方码站日期、自行计算值;且与他站对比属自夸 | REFUTED | → "This guide is also unofficial. Every number here names where it came from." |
| M42 | community | "So the safe way to check is from inside Roblox. Sign in, open the game's page and look for a Discord link there." | 规则 | 文档:社交链接仅对已验证 ≥16 岁用户可见;游戏是否配置了链接未知 | UNVERIFIED | → "…Sign in with an account verified as 16 or older, open the game's page and look for social links; the developer may not have set any." |
| M43 | updates | H2 "How often does the game update?" → "About once a week, on a Saturday." (及 beginner scope "The game changes weekly.") | 规则 | 事件列表是预告,本页自己声明 "does not prove when a feature went live" | UNVERIFIED | H2 → "How often are updates announced?"; answer → "Official event listings have appeared about once a week, usually on a Saturday."; beginner → "Official update events have been listed weekly." |
| M44 | updates | "A field that moves that often is tracking something other than releases" | 规则 | 合理推断,但未证实 updated 字段含义(我 04:16:34Z 再读又是新值,支持"频繁变动") | UNVERIFIED | → "so we do not use it as a patch date" |
| M45 | beginner | "Every number on these pages comes from Roblox's official data for the game and carries its check date."(tldr) | 规则 | community/codes 页含 Discord 人数、第三方码站日期/奖励;派生百分比不是 Roblox 数据 | REFUTED | → "Nearly every number on these pages comes from Roblox's official data for the game; Discord and code-site figures are labelled as such. Counters carry their check date." |
| M46 | robux | "Several passes only raise limits you may not have reached yet." | 规则 | 基础限额官方未公布,"may not have reached" 无依据 | UNVERIFIED | → delete, or "Several passes raise limits whose base values are not published." |
| M47 | author | "Every guide published under that byline is listed below." | 规则 | 页面下方只有 "Where to start" 3 个链接,不是全部 12 页 | REFUTED | → "Start with these guides:" 或补全 12 页列表 |
| M48 | author | "Jellyfi writes the {{BRAND}} guides…"(frontmatter description)及正文 "the editorial byline on {{BRAND}}" | 名称 | 未替换的模板变量(其他页不含) | UNVERIFIED | 确认构建期会替换 {{BRAND}};否则替换为站点品牌名 |
| M49 | (all) | frontmatter gameVersion: "UI Overhaul + Features (event from 3 Oct 2026)" | 名称 | Roblox 体验无版本号;事件名≠游戏版本;该事件挂牌 2026-10-09 04:00Z 结束,随后字段过期 | UNVERIFIED | → 字段改为 "Latest announced update: UI Overhaul + Features (3 Oct 2026)" 或删除;Custom Offices 起(10 Oct)需更新 |
| M50 | (all) | sourceUrls: "https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation" | 规则 | 该端点只接受 POST;GET 返回 404(我实测)。同时 virtual-events URL 带作者的不透明 cursor | UNVERIFIED | URL 后加 "(POST, body {universeId})" 或移除;virtual-events URL 去掉 ?cursor=…(现取不带 cursor 同样返回全部 12 条;但作者 03:39Z 的 raw/virtual_events.json 不带 cursor 只回 2 条,接口行为不稳,建议在页面注明"分页") |
| M51 | index | "The next listed update is Custom Offices, starting Saturday 10 October 2026 at 20:00 UTC."(tldr)、"What is coming next?"、updates 开篇 "The next Roblox Stock Exchange 2 update is Custom Offices"、codes/updates 同类表述 | 日期 | 相对 2026-10-08 成立(开始时间 2026-10-10T20:00:18Z 在未来)。但 entities/updates 把"改写成过去时"的时点定在 2026-10-16/17,而 "next/starts" 在 10 Oct 20:00 UTC 起即失效 | UNVERIFIED | 上线计划:把过期动作提前到 2026-10-10 20:00 UTC(index tldr、faq、What is coming next?、updates 开篇与 H2、config hub card highlights);在此之前页面可发布 |
| M52 | (all) | imgs: 16 个 tr.rbxcdn.com 180DAY- 图片 URL | 规则 | 全部 curl 200;且与现取 thumbnails API 返回的 URL 完全一致(icon 另取 games/icons) | CONFIRMED |  |
| M53 | updates | "The art is made to promote an update, so numbers in it are illustrations and the live game can differ."(art 表)与 community/algo-bots 的使用 | 规则 | 措辞正确(已限定);ev_bonds/ev_commodities 图脚均印 "COMING SOON",确为上线前宣传图 | CONFIRMED |  |

## 4. 作者命题验证表(467 条)

列:编号 | 页面 | 原句 | 类型 | 取证 URL 与取到的值 | 结论 | 改法(仅 REFUTED/UNVERIFIED)

| # | 页面 | 原句 | 类型 | 取证(来源 → 值) | 结论 | 原句 → 改成什么 |
|---|---|---|---|---|---|---|
| 1 | index | made by the group Summit Productions Development | 名称 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 2 | index | created on 13 July 2026 | 日期 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 3 | index | Roblox Stock Exchange 2 is a free trading simulator on Roblox | 其他 | games → 现取 games v1 price=null(免费入场) ✓ | CONFIRMED |  |
| 4 | index | trading simulated stocks, ETFs, futures and IPOs | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 5 | index | then add algorithmic bots, levels and rebirths | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 6 | index | then add algorithmic bots, levels and rebirths | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 7 | index | "All markets and currencies are simulated. This game does not involve real-money trading or provide financial advice." | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 8 | index | \| Developer \| Summit Productions Development (Roblox group) \| | 名称 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 9 | index | \| Created \| 13 July 2026 \| | 日期 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 10 | index | \| Genre on Roblox \| Simulation \| | 列表字段 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 11 | index | \| Players per server \| 35 \| | 数字 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 12 | index | \| Content maturity \| Minimal ("Suitable for everyone") \| | 列表字段 | age(POST) → 现取 POST get-age-recommendation → displayName Minimal / "Maturity: Minimal" ✓ | CONFIRMED |  |
| 13 | index | \| Content maturity \| Minimal ("Suitable for everyone") \| | 列表字段 | age(POST) → 现取 POST get-age-recommendation → descriptor displayName "Suitable for everyone" ✓ | CONFIRMED |  |
| 14 | index | \| Price \| Free, with optional Robux purchases \| | 价格 | games → 现取 games v1 price=null(免费入场) ✓ | CONFIRMED |  |
| 15 | index | \| Visits \| 5,093,566 \| | 数字 | games → games v1 现取04:19Z visits=5,097,144(作者03:39Z=5,093,566,raw一致;增量合理) | CONFIRMED |  |
| 16 | index | \| Favourites \| 61,993 \| | 数字 | games → 现取 favoritedCount=62,033(作者 61,993,量级吻合) | CONFIRMED |  |
| 17 | index | \| Likes / dislikes \| 12,004 / 890 \| | 数字 | votes → 现取 votes 12,014 / 891(作者 12,004 / 890) | CONFIRMED |  |
| 18 | index | \| Players online \| 1,123 \| | 数字 | games → 现取 playing=1,049(作者 1,123;在线数日内波动,页面带时间戳) | CONFIRMED |  |
| 19 | index | \| Game passes \| 13 \| | 数字 | passes → 现取 passes API:13 条,nextPageToken 空 ✓ | CONFIRMED |  |
| 20 | index | \| Developer products \| 31 \| | 数字 | prod → 现取 developerproducts:31 条,nextPageCursor=null ✓ | CONFIRMED |  |
| 21 | index | \| Badges \| 11 \| | 数字 | badges → 现取 badges:11 条,nextPageCursor=null ✓ | CONFIRMED |  |
| 22 | index | \| Official update events listed \| 12, the first starting 17 August 2026 \| | 数字 | events → 现取 virtual-events:12 条(带/不带 cursor 均 12;另试 previous cursor 返回 11 条为子集,未发现更早事件) ✓ | CONFIRMED |  |
| 23 | index | \| Official update events listed \| 12, the first starting 17 August 2026 \| | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 24 | index | Near its end the game description has three lines: "THANKS FOR 10K LIKES", "CODE: TOOLS" and "NEXT CODE RELEASES AT 15,000 LIKES" | 兑换码 | games → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 25 | index | The game had 12,004 likes when we checked | 数字 | votes → 现取 votes 12,014 / 891(作者 12,004 / 890) | CONFIRMED |  |
| 26 | index | so the next code is 2,996 likes away | 数字 | 自行重算 → 15,000−12,004=2,996(作者快照);按现取12,014 则差2,986,页面写成带时间的快照,可 | CONFIRMED |  |
| 27 | index | What TOOLS gives is not stated in the description. | 兑换码 | games → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 28 | index | The description names four markets and says you can use leverage and short the market. | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 29 | index | \| Hedge funds \| HEDGE FUNDS event \| 17 August \| | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 30 | index | \| Meme coins in a Crypto tab \| NEW MEMECOINS event \| 22 August \| | 开发者原话 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 31 | index | \| Meme coins in a Crypto tab \| NEW MEMECOINS event \| 22 August \| | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 32 | index | \| Real estate \| REAL ESTATE event \| 5 September \| | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 33 | index | \| Bonds \| BONDS event \| 19 September \| | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 34 | index | \| Commodities \| COMMODITIES EXCHANGE event \| 26 September \| | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 35 | index | The 13 game passes are one-time purchases, priced from 39 to 999 Robux | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 36 | index | The 13 game passes are one-time purchases, priced from 39 to 999 Robux | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 37 | index | The 13 game passes are one-time purchases | 规则 | docs → 现取 create.roblox.com 文档 HTTP 200,原句逐字在页 ✓ | CONFIRMED |  |
| 38 | index | 24 hours of offline market time instead of 8 | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 39 | index | up to 50x leverage at any level | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 40 | index | 0.02% fees | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 41 | index | The 31 developer products cost 9 to 999 Robux | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 42 | index | include time skips, AI Tokens and four algo bot purchases | 列表字段 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 43 | index | about 90 First Trade badges and 69 First Profit badges have been awarded | 数字 | 自行重算 → 重算 2,061,945÷2,288,320=90.11%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 44 | index | Shorting is much rarer at 27 | 数字 | 自行重算 → 重算 616,376÷2,288,320=26.94%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 45 | index | only about 2 in 100 have built an algo bot or rebirthed | 数字 | 自行重算 → 重算 50,910÷2,288,320=2.22%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 46 | index | An official event called Custom Offices starts on Saturday 10 October 2026 at 20:00 UTC | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 47 | index | "Your own 3d office you can walk inside of and upgrade" | 开发者原话 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 48 | index | Summit Productions Development is a Roblox group with 276,709 members | 数字 | group → 现取 memberCount=276,833(作者 276,709) | CONFIRMED |  |
| 49 | index | Its description is empty and it has no pinned shout | 其他(抽样:是) | group → 现取 group 对应字段一致 ✓ | CONFIRMED |  |
| 50 | index | Its description is empty and it has no pinned shout | 其他(抽样:是) | group → 现取 group 对应字段一致 ✓ | CONFIRMED |  |
| 51 | index | tldr: The game sells 13 game passes (39 to 999 Robux) and 31 developer products (9 to 999 Robux). | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 52 | index | faq: Up to 35, according to the Roblox game record we read on 8 October 2026. | 数字 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 53 | index | faq: Custom Timeframes, at 39 Robux on 8 October 2026. | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 54 | index | alt th5: a market sentiment gauge reading Bullish | 其他 | image → Read 亲眼看图 evidence/img/th5_src.png:Market Sentiment 仪表盘指针指向 Bullish | CONFIRMED |  |
| 55 | index | alt th1: a trading card for a stock called OBBY, Obby Dynamics, at 154.87 | 其他 | image → Read 亲眼看图 evidence/img/th1_src.png:OBBY / Obby Dynamics / 154.87 / BUY / SELL / BUYING POWER $532,456 / PORTFOLIO VALUE $1,247,891 | CONFIRMED |  |
| 56 | how-to-play | you start with a small simulated account and grow it by trading stocks, ETFs, futures and IPOs | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 57 | how-to-play | You can go long or short, add leverage, and place limit orders, stop losses and take profits | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 58 | how-to-play | your market keeps running for a while after you log off | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 59 | how-to-play | The description opens with "BUILD YOUR TRADING EMPIRE!" | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 60 | how-to-play | "Study price action, discover leading stocks, manage risk, and grow your portfolio, even while you’re offline!" | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 61 | how-to-play | Seven feature lines follow. | 数字 | games → 现取 description 的七个功能行(📈标题后🔥前)数得 7 行 ✓ | CONFIRMED |  |
| 62 | how-to-play | \| Trade stocks, ETFs, futures, and IPOs \| | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 63 | how-to-play | \| Use advanced indicators and live order flow \| | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 64 | how-to-play | \| Place limit orders, stop losses, and take profits \| | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 65 | how-to-play | \| Unlock and upgrade algorithmic trading bots \| | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 66 | how-to-play | \| Level up, rebirth, and expand your financial empire \| | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 67 | how-to-play | \| Track your performance with a P&L calendar \| | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 68 | how-to-play | \| Use leverage, short the market, and master every market cycle \| | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 69 | how-to-play | Roblox had awarded the Welcome badge 2,288,320 times by 8 October 2026 | 数字 | badges → raw 03:47Z 快照一致(Welcome to Roblox Stock Exchange 2 2288320);现取04:19Z awardedCount=2,289,357 pastDay=47,808,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 70 | how-to-play | TOOLS is printed in the official description. | 兑换码 | games → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 71 | how-to-play | The First Trade badge reads "You made your first trade!" | 开发者原话 | badges → 现取 badges 对应字段一致 ✓ | CONFIRMED |  |
| 72 | how-to-play | About 90 in 100 Welcome badge holders have it. | 数字 | 自行重算 → 重算 2,061,945÷2,288,320=90.11%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 73 | how-to-play | First Profit ("You made your first profit trading!") sits at about 69 in 100. | 数字 | 自行重算 → 重算 1,569,182÷2,288,320=68.57%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 74 | how-to-play | First Short ("You shorted your first stock!") drops to about 27 in 100. | 数字 | 自行重算 → 重算 616,376÷2,288,320=26.94%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 75 | how-to-play | First Futures Trade is under 10 in 100. | 数字 | 自行重算 → 重算 214,382÷2,288,320=9.37%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 76 | how-to-play | It shows a Long and Short toggle above a single "Buy OBBY" button, and an open position row with a red Close button. | 其他(抽样:是) | image → Read 亲眼看图 evidence/img/th2_src.png:Long/Short 切换在 Buy OBBY 按钮上方;持仓行 OBBY LONG 右侧红色 Close 按钮 | CONFIRMED |  |
| 77 | how-to-play | Tabs under the chart read Positions, Orders, History, P&L, Feed and News. | 列表字段 | image → Read 亲眼看图 evidence/img/th2_src.png:底部标签 Positions/Orders/History/P&L/Feed/News | CONFIRMED |  |
| 78 | how-to-play | A second official image shows large BUY and SELL buttons beside a chart. | 其他 | image → Read 亲眼看图 evidence/img/th1+th3_src.png:th1 与 th3 均有大号绿 BUY + 红 SELL | CONFIRMED |  |
| 79 | how-to-play | an official event starting 3 October 2026 announced "a brand new interface for the game, reorganized interfaces, and new game features" | 开发者原话 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 80 | how-to-play | an official event starting 3 October 2026 | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 81 | how-to-play | \| Leverage \| Max Leverage pass: "Up to 50x leverage at any level." \| | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 82 | how-to-play | \| Fees \| Pro Trader pass: "0.02% fees, unlimited drawings, pro stats." \| | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 83 | how-to-play | \| Offline market \| Overnight Desk pass: "Your market keeps running for 24 hours offline instead of 8." \| | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 84 | how-to-play | \| XP and daily rewards \| VIP pass: "2x XP, 2x daily rewards, VIP badge, 1 free Sim Day per day." \| | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 85 | how-to-play | \| Market hours \| A 9-Robux product is named "Skip to Market Open" \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 86 | how-to-play | \| Player companies \| More Player Companies pass: "Launch up to 5 player-founded stocks instead of 2." \| | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 87 | how-to-play | \| News \| Insider pass: "Early alerts before news hits + IPO intel." \| | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 88 | how-to-play | And the base game gives 8 hours of offline market time. | 规则 | passes → 只有 Overnight Desk 描述里的 "instead of 8" 这一间接依据;如游戏后来改了基础值则错 | UNVERIFIED | "And the base game gives 8 hours of offline market time." → "The Overnight Desk description says 24 hours offline \"instead of 8\", which implies a default of 8 hours; no source states the base value directly." |
| 89 | how-to-play | Millionaire ("Your total net-worth is over $1,000,000!") | 开发者原话 | badges → 现取 badges 对应字段一致 ✓ | CONFIRMED |  |
| 90 | how-to-play | they had been awarded 100,099 and 39,765 times | 数字 | badges → raw 03:47Z 快照一致(Millionaire 100099);现取04:19Z awardedCount=100,144 pastDay=1,917,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 91 | how-to-play | they had been awarded 100,099 and 39,765 times | 数字 | badges → raw 03:47Z 快照一致($10,000,000 Net Worth 39765);现取04:19Z awardedCount=39,776 pastDay=408,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 92 | how-to-play | First Algo Bot stood at 50,910 and First Rebirth at 42,936. | 数字 | badges → raw 03:47Z 快照一致(First Algo Bot 50910);现取04:19Z awardedCount=50,945 pastDay=1,401,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 93 | how-to-play | First Algo Bot stood at 50,910 and First Rebirth at 42,936. | 数字 | badges → raw 03:47Z 快照一致(First Rebirth 42936);现取04:19Z awardedCount=42,950 pastDay=398,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 94 | how-to-play | including four Robux products | 数字 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 95 | how-to-play | \| 17 August \| HEDGE FUNDS \| "Run a hedge fund" \| | 开发者原话 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 96 | how-to-play | \| 17 August \| HEDGE FUNDS \| "Run a hedge fund" \| | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 97 | how-to-play | \| 22 August \| NEW MEMECOINS \| "new meme coins in the Crypto tab" \| | 开发者原话 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 98 | how-to-play | \| 5 September \| REAL ESTATE \| "you'll be able to buy real estate across a global map" \| | 开发者原话 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 99 | how-to-play | \| 19 September \| BONDS \| "Trade debt, earn interest, weigh the risk." \| | 开发者原话 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 100 | how-to-play | \| 26 September \| COMMODITIES EXCHANGE \| "Prices will be driven by new news events, such as weather reports and more" \| | 开发者原话 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 101 | how-to-play | a Level 2 order book, trailing stops and fib extensions all appear in official text | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 102 | how-to-play | a Level 2 order book, trailing stops and fib extensions all appear in official text | 开发者原话 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 103 | how-to-play | the developer states that "All markets and currencies are simulated" | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 104 | how-to-play | the ticker in the official art is OBBY, for a company called Obby Dynamics | 名称 | image → Read 亲眼看图 evidence/img/th2/th1_src.png:OBBY / Obby Dynamics | CONFIRMED |  |
| 105 | how-to-play | Roblox rates the experience Minimal, "Suitable for everyone" | 列表字段 | age(POST) → 现取 POST get-age-recommendation → descriptor displayName "Suitable for everyone" ✓ | CONFIRMED |  |
| 106 | how-to-play | tldr: Your market keeps running for 8 hours while you are offline, or 24 hours with the Overnight Desk pass. | 规则 | passes → 同 #88 | UNVERIFIED | tldr: "Your market keeps running for 8 hours while you are offline, or 24 hours with the Overnight Desk pass." → "The Overnight Desk pass says your market keeps running for 24 hours offline \"instead of 8\", which implies a default of 8 hours." |
| 107 | how-to-play | alt th4: a green arrow curves from a glowing $100 to $1,284,593 | 其他(抽样:是) | image → Read 亲眼看图 evidence/img/th4_src.png:$100 → 绿色箭头 → $1,284,593,右下绿色 BUY | CONFIRMED |  |
| 108 | codes | The working Roblox Stock Exchange 2 code for October 2026 is **TOOLS**. | 兑换码 | games → 描述里印着 ≠ 游戏内能兑换;描述写 "THANKS FOR 10K LIKES",而现有赞 12,0xx,说明这段文字可能早于现状;无人在游戏内实测 | UNVERIFIED | "The working Roblox Stock Exchange 2 code for October 2026 is TOOLS." → "The only code printed in the official Roblox Stock Exchange 2 description in October 2026 is TOOLS. We have not tested it in the game." |
| 109 | codes | right under the line "THANKS FOR 10K LIKES" | 开发者原话 | games → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 110 | codes | it was still there when we checked on 8 October 2026 | 日期 | games → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 111 | codes | The description does not say what the code gives. | 兑换码 | games → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 112 | codes | The next code is promised at 15,000 likes. | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 113 | codes | \| TOOLS \| Not stated officially \| Active \| Official game description on Roblox \| 8 October 2026 \| | 兑换码 | games → 同 #108 | UNVERIFIED | table cell "Active" → "Listed in the description (not tested in game)" |
| 114 | codes | On 8 October 2026 the group description was empty, the group had no shout | 其他 | group → 现取 group 对应字段一致 ✓ | CONFIRMED |  |
| 115 | codes | On 8 October 2026 the group description was empty, the group had no shout | 其他(抽样:是) | group → 现取 group 对应字段一致 ✓ | CONFIRMED |  |
| 116 | codes | none of the 12 event listings contained a code | 其他 | events → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 117 | codes | "THANKS FOR 10K LIKES", then "CODE: TOOLS", then "NEXT CODE RELEASES AT 15,000 LIKES" | 开发者原话 | games → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 118 | codes | \| Milestone named above the TOOLS code \| 10,000 \| | 数字 | games → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 119 | codes | \| Likes at 03:39 UTC on 8 October 2026 \| 12,004 \| | 数字 | votes → 现取 votes 12,014 / 891(作者 12,004 / 890) | CONFIRMED |  |
| 120 | codes | \| Milestone for the next code \| 15,000 \| | 数字 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 121 | codes | \| Still needed \| 2,996 \| | 数字 | 自行重算 → 同上 2,996 | CONFIRMED |  |
| 122 | codes | "Like and favorite the game for future updates!" | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 123 | codes | Four code pages we read list up to six more codes: STOCKMARKET, MEMECOINS, FUTURES, BULLMARKET, UPDATE and RELEASE. | 兑换码 | robloxden → Roblox Den ✓(6 个码全在)、Try Hard Guides ✓(6 个全在)、另两站 403 | UNVERIFIED | "Four code pages we read list up to six more codes" → keep only if the two 403 sites are re-read; otherwise "Two of the four code pages we read ..." |
| 124 | codes | None of the six is in the official description today. | 兑换码 | games → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 125 | codes | \| Roblox Den \| Checked 7 October 2026 \| Yes \| 6 \| | 其他 | robloxden → robloxden 现取(UA 浏览器): "last checked for codes 13 hours ago at 03:04PM (10/07/2026) Times shown in UTC";列 7 码含 TOOLS(20K Cash)+STOCKMARKET 50,000 Cash/FUTURES 20,000 Cash and 20 XP/MEMECOINS 10,000 Cash and 20 XP/BULLMARKET 5,000 Cash and 40 XP/UPDATE 20 XP and 7,500 Cash/RELEASE 10,000 Cash ✓ | CONFIRMED |  |
| 126 | codes | \| Roblox Den \| Checked 7 October 2026 \| Yes \| 6 \| | 兑换码 | robloxden → robloxden 现取(UA 浏览器): "last checked for codes 13 hours ago at 03:04PM (10/07/2026) Times shown in UTC";列 7 码含 TOOLS(20K Cash)+STOCKMARKET 50,000 Cash/FUTURES 20,000 Cash and 20 XP/MEMECOINS 10,000 Cash and 20 XP/BULLMARKET 5,000 Cash and 40 XP/UPDATE 20 XP and 7,500 Cash/RELEASE 10,000 Cash ✓ | CONFIRMED |  |
| 127 | codes | \| Try Hard Guides \| 29 September 2026 \| Yes \| 6 \| | 其他 | tryhard → tryhardguides 现取 HTTP 200: dateModified 2026-09-29T23:02:03-07:00;列 TOOLS(NEW)+STOCKMARKET/MEMECOINS/FUTURES/UPDATE/BULLMARKET/RELEASE;"Press the yellow gift/present button in the right corner of the screen. Enter a working code in the ENTER CODE text box and hit the yellow Redeem button." ✓ | CONFIRMED |  |
| 128 | codes | \| Try Hard Guides \| 29 September 2026 \| Yes \| 6 \| | 兑换码 | tryhard → tryhardguides 现取 HTTP 200: dateModified 2026-09-29T23:02:03-07:00;列 TOOLS(NEW)+STOCKMARKET/MEMECOINS/FUTURES/UPDATE/BULLMARKET/RELEASE;"Press the yellow gift/present button in the right corner of the screen. Enter a working code in the ENTER CODE text box and hit the yellow Redeem button." ✓ | CONFIRMED |  |
| 129 | codes | \| Twinfinite \| 1 October 2026 \| No \| 6 \| | 其他(抽样:是) | twinfinite → twinfinite.net 对我 HTTP 403(Cloudflare),无法复核其更新日期与"不含 TOOLS" | UNVERIFIED | keep only if re-read in a browser; otherwise delete the Twinfinite row |
| 130 | codes | \| Pro Game Guides \| 7 September 2026 \| No \| 6 \| | 其他 | progameguides → progameguides.com 对我 HTTP 403,无法复核 | UNVERIFIED | keep only if re-read in a browser; otherwise delete the Pro Game Guides row |
| 131 | codes | Roblox Den gives FUTURES as "20,000 Cash and 20 XP" | 兑换码 | robloxden → robloxden 现取 HTTP 200: "First, click the Gift icon at the top-right side of the screen" / ENTER CODE / REDEEM ✓ | CONFIRMED |  |
| 132 | codes | while Pro Game Guides and Twinfinite both give it as 10k Cash | 兑换码 | twinfinite → 两站均 403;Roblox Den 的 20,000 Cash and 20 XP ✓ | UNVERIFIED | "while Pro Game Guides and Twinfinite both give it as 10k Cash" → "while Roblox Den gives it as 20,000 Cash and 20 XP" (drop the 10k half unless re-verified) |
| 133 | codes | None of the four pages links a developer post for any code. | 其他(抽样:是) | twinfinite → Roblox Den 无任何开发者/官方链接(仅游戏页链接);Try Hard Guides 仅链接游戏页、群组页与 Discord 邀请,无开发者帖 ✓;另两站 403 | UNVERIFIED | "None of the four pages links a developer post for any code." → "Neither Roblox Den nor Try Hard Guides links a developer post for any code." (unless the other two are re-read) |
| 134 | codes | Three of the code sites above describe a gift or present button on the right of the screen (two of them say top-right) | 其他 | robloxden → robloxden 现取 HTTP 200: "First, click the Gift icon at the top-right side of the screen" / ENTER CODE / REDEEM ✓ | CONFIRMED |  |
| 135 | codes | Three of the code sites above describe a gift or present button on the right of the screen (two of them say top-right) | 其他(抽样:是) | tryhard → tryhardguides 现取 HTTP 200: dateModified 2026-09-29T23:02:03-07:00;列 TOOLS(NEW)+STOCKMARKET/MEMECOINS/FUTURES/UPDATE/BULLMARKET/RELEASE;"Press the yellow gift/present button in the right corner of the screen. Enter a working code in the ENTER CODE text box and hit the yellow Redeem button." ✓ | CONFIRMED |  |
| 136 | codes | Three of the code sites above describe a gift or present button on the right of the screen (two of them say top-right) | 其他(抽样:是) | twinfinite → Twinfinite 对我 HTTP 403(未绕过),无法复核;Roblox Den 写 top-right ✓,Try Hard Guides 写 "right corner of the screen"(不是 top-right) | UNVERIFIED | "(two of them say top-right)" → "(Roblox Den says top-right, Try Hard Guides says \"the right corner\")"; drop Twinfinite from the "three" until it can be re-read |
| 137 | codes | that opens an "ENTER CODE" box with a Redeem button | 其他(抽样:是) | tryhard → tryhardguides 现取 HTTP 200: dateModified 2026-09-29T23:02:03-07:00;列 TOOLS(NEW)+STOCKMARKET/MEMECOINS/FUTURES/UPDATE/BULLMARKET/RELEASE;"Press the yellow gift/present button in the right corner of the screen. Enter a working code in the ENTER CODE text box and hit the yellow Redeem button." ✓ | CONFIRMED |  |
| 138 | codes | the interface was overhauled in an update announced for 3 October 2026 | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 139 | codes | It is five letters, no spaces. | 兑换码 | games → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 140 | codes | The description prints it in capitals | 兑换码 | games → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 141 | codes | the [game pass guide](/roblox-stock-exchange-2/gamepasses/) compares all 13 passes | 数字 | passes → 现取 passes API:13 条,nextPageToken 空 ✓ | CONFIRMED |  |
| 142 | codes | tldr: The game had 12,004 likes on 8 October 2026, so 2,996 to go. | 数字 | votes → 现取 votes 12,014 / 891(作者 12,004 / 890) | CONFIRMED |  |
| 143 | codes | frontmatter codes[]: {"code": "TOOLS", "reward": "Not stated in the official description", "status": "active", "firstSeen": "2026-10-08"} | 兑换码 | games → 同 #108 | UNVERIFIED | codes[] status "active" → "listed" (or keep "active" only if the site schema defines it as "present in the official source"); reward field → "Not stated in the official description; in-game redemption not tested" |
| 144 | badges | Roblox Stock Exchange 2 has 11 Roblox badges. | 数字 | badges → 现取 badges:11 条,nextPageCursor=null ✓ | CONFIRMED |  |
| 145 | badges | Nine mark trading milestones, from your first trade to a net worth above $10,000,000, one welcomes you to the game, and one was given for sharing a server with a game owner. | 列表字段 | badges → 现取 badges 对应字段一致 ✓ | CONFIRMED |  |
| 146 | badges | Welcome had been awarded 2,288,320 times and First Rebirth 42,936 times | 数字 | badges → raw 03:47Z 快照一致(Welcome to Roblox Stock Exchange 2 2288320);现取04:19Z awardedCount=2,289,357 pastDay=47,808,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 147 | badges | Welcome had been awarded 2,288,320 times and First Rebirth 42,936 times | 数字 | badges → raw 03:47Z 快照一致(First Rebirth 42936);现取04:19Z awardedCount=42,950 pastDay=398,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 148 | badges | Ten of the eleven were created on 13 and 14 July 2026, the game's first two days. | 日期 | badges → 现取 badges 对应字段一致 ✓ | CONFIRMED |  |
| 149 | badges | Ten of the eleven were created on 13 and 14 July 2026, the game's first two days. | 日期 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 150 | badges | Roblox describes a badge as "a special award you can gift players when they meet a goal within your game" | 规则 | docs → 现取 create.roblox.com 文档 HTTP 200,原句逐字在页 ✓ | CONFIRMED |  |
| 151 | badges | 90.1% of Welcome holders have it | 数字 | 自行重算 → 重算 2,061,945÷2,288,320=90.11%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 152 | badges | 68.6% have managed that | 数字 | 自行重算 → 重算 1,569,182÷2,288,320=68.57%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 153 | badges | Roughly one in four players who placed a trade has never had the profit badge. | 数字 | 自行重算 → 1−1,569,182/2,061,945=23.9% ✓ | CONFIRMED |  |
| 154 | badges | the Welcome badge's past-day awards (47,508) | 数字 | badges → raw 03:47Z 快照一致(Welcome to Roblox Stock Exchange 2 pastDay=47508);现取 pastDay=47,808 | CONFIRMED |  |
| 155 | badges | An interface overhaul was announced for 3 October 2026 | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 156 | badges | Millionaire asks for a total net worth over $1,000,000 and had 100,099 awards, or 4.4% of Welcome holders. | 数字 | badges → raw 03:47Z 快照一致(Millionaire 100099);现取04:19Z awardedCount=100,144 pastDay=1,917,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 157 | badges | $10,000,000 Net Worth had 39,765. | 数字 | badges → raw 03:47Z 快照一致($10,000,000 Net Worth 39765);现取04:19Z awardedCount=39,776 pastDay=408,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 158 | badges | about 40 in 100 players who reach the first million go on to ten | 数字 | 自行重算 → 重算 39,765÷100,099=39.73%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 159 | badges | Hundred Trades ("You completed your first 100 trades!") is the volume badge, held by 13.1%. | 数字 | badges → 现取 badges 对应字段一致 ✓ | CONFIRMED |  |
| 160 | badges | Hundred Trades ("You completed your first 100 trades!") is the volume badge, held by 13.1%. | 数字 | 自行重算 → 重算 299,258÷2,288,320=13.08%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 161 | badges | None of the 13 passes in the [game pass guide](/roblox-stock-exchange-2/gamepasses/) is described as speeding up a badge. | 其他 | passes → 现取 games v1 description 原文含 "THANKS FOR 10K LIKES\nCODE: TOOLS\nNEXT CODE RELEASES AT 15,000 LIKES",TOOLS 后无任何奖励文字;六个他站码(STOCKMARKET 等)均不在 description ✓ | CONFIRMED |  |
| 162 | badges | \| First Algo Bot \| You created your first algorithmic trading bot! \| 50,910 \| 1,404 \| | 数字 | badges → raw 03:47Z 快照一致(First Algo Bot 50910);现取04:19Z awardedCount=50,945 pastDay=1,401,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 163 | badges | \| First Rebirth \| You rebirthed for the first time! \| 42,936 \| 394 \| | 数字 | badges → raw 03:47Z 快照一致(First Rebirth 42936);现取04:19Z awardedCount=42,950 pastDay=398,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 164 | badges | The store does sell a product called Deploy Algo Bot for 149 Robux | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 165 | badges | First Rebirth (42,936) has been awarded more often than $10,000,000 Net Worth (39,765) | 数字 | 自行重算 → 42,936>39,765 ✓ (raw badges 03:47Z;现取 42,950>39,776 同向) | CONFIRMED |  |
| 166 | badges | "Wow, 150% profit. You were in a server with one of the game owners" | 开发者原话 | badges → 现取 badges 对应字段一致 ✓ | CONFIRMED |  |
| 167 | badges | The badge was created on 15 August 2026, a month after the others. | 日期 | badges → 现取 badges 对应字段一致 ✓ | CONFIRMED |  |
| 168 | badges | It had been awarded 1,305 times in total and 0 times in the day before our check. | 数字 | badges → raw 03:47Z 快照一致(Met the game owners! 1305);现取04:19Z awardedCount=1,305 pastDay=0,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 169 | badges | The badge is still enabled on Roblox | 其他 | badges → 现取 badges 对应字段一致 ✓ | CONFIRMED |  |
| 170 | badges | Between two reads eight minutes apart on 8 October, the Welcome total rose by 266. | 数字 | badges → 现取 badges 对应字段一致 ✓ | CONFIRMED |  |
| 171 | badges | Roblox recorded 5,093,566 visits | 数字 | games → games v1 现取04:19Z visits=5,097,144(作者03:39Z=5,093,566,raw一致;增量合理) | CONFIRMED |  |
| 172 | badges | tldr: About 90 in 100 Welcome badge holders have First Trade, but only about 27 in 100 have First Short. | 数字 | 自行重算 → 自行重算,与摘录一致 | CONFIRMED |  |
| 173 | badges | tldr: First Algo Bot (50,910) and First Rebirth (42,936) are each held by about 2 in 100. | 数字 | 自行重算 → 自行重算,与摘录一致 | CONFIRMED |  |
| 174 | badges | alt th3: a large red -48.7% TODAY | 其他 | image → Read 亲眼看图 evidence/img/th3_src.png:-48.7% TODAY, BUY 大按钮, SELL 小按钮, 纵轴到 -60% | CONFIRMED |  |
| 175 | badges | \| Welcome to Roblox Stock Exchange 2 \| Thank you for playing! \| 13 Jul 2026 \| 2,288,320 \| | 名称 | badges → raw 03:47Z 快照一致(Welcome to Roblox Stock Exchange 2 2288320);现取04:19Z awardedCount=2,289,357 pastDay=47,808,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 176 | badges | Share column for Welcome to Roblox Stock Exchange 2: 100% | 数字 | 自行重算 → 重算 2,288,320÷2,288,320=100.00%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 177 | badges | \| First Trade \| You made your first trade! \| 13 Jul 2026 \| 2,061,945 \| | 名称 | badges → raw 03:47Z 快照一致(First Trade 2061945);现取04:19Z awardedCount=2,062,970 pastDay=46,796,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 178 | badges | Share column for First Trade: 90.1% | 数字 | 自行重算 → 重算 2,061,945÷2,288,320=90.11%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 179 | badges | \| First Profit \| You made your first profit trading! \| 13 Jul 2026 \| 1,569,182 \| | 名称 | badges → raw 03:47Z 快照一致(First Profit 1569182);现取04:19Z awardedCount=1,570,195 pastDay=46,716,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 180 | badges | Share column for First Profit: 68.6% | 数字 | 自行重算 → 重算 1,569,182÷2,288,320=68.57%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 181 | badges | \| First Short \| You shorted your first stock! \| 13 Jul 2026 \| 616,376 \| | 名称 | badges → raw 03:47Z 快照一致(First Short 616376);现取04:19Z awardedCount=617,054 pastDay=30,393,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 182 | badges | Share column for First Short: 26.9% | 数字 | 自行重算 → 重算 616,376÷2,288,320=26.94%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 183 | badges | \| First Futures Trade \| You made your first futures trade! \| 13 Jul 2026 \| 214,382 \| | 名称 | badges → raw 03:47Z 快照一致(First Futures Trade 214382);现取04:19Z awardedCount=214,794 pastDay=19,157,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 184 | badges | Share column for First Futures Trade: 9.4% | 数字 | 自行重算 → 重算 214,382÷2,288,320=9.37%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 185 | badges | \| First Algo Bot \| You created your first algorithmic trading bot! \| 14 Jul 2026 \| 50,910 \| | 名称 | badges → raw 03:47Z 快照一致(First Algo Bot 50910);现取04:19Z awardedCount=50,945 pastDay=1,401,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 186 | badges | Share column for First Algo Bot: 2.2% | 数字 | 自行重算 → 重算 50,910÷2,288,320=2.22%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 187 | badges | \| First Rebirth \| You rebirthed for the first time! \| 14 Jul 2026 \| 42,936 \| | 名称 | badges → raw 03:47Z 快照一致(First Rebirth 42936);现取04:19Z awardedCount=42,950 pastDay=398,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 188 | badges | Share column for First Rebirth: 1.9% | 数字 | 自行重算 → 重算 42,936÷2,288,320=1.88%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 189 | badges | \| Millionaire \| Your total net-worth is over $1,000,000! \| 14 Jul 2026 \| 100,099 \| | 名称 | badges → raw 03:47Z 快照一致(Millionaire 100099);现取04:19Z awardedCount=100,144 pastDay=1,917,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 190 | badges | Share column for Millionaire: 4.4% | 数字 | 自行重算 → 重算 100,099÷2,288,320=4.37%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 191 | badges | \| $10,000,000 Net Worth \| Your net worth exceeded $10,000,000 \| 14 Jul 2026 \| 39,765 \| | 名称 | badges → raw 03:47Z 快照一致($10,000,000 Net Worth 39765);现取04:19Z awardedCount=39,776 pastDay=408,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 192 | badges | Share column for $10,000,000 Net Worth: 1.7% | 数字 | 自行重算 → 重算 39,765÷2,288,320=1.74%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 193 | badges | \| Hundred Trades \| You completed your first 100 trades! \| 14 Jul 2026 \| 299,258 \| | 名称 | badges → raw 03:47Z 快照一致(Hundred Trades 299258);现取04:19Z awardedCount=299,437 pastDay=8,379,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 194 | badges | Share column for Hundred Trades: 13.1% | 数字 | 自行重算 → 重算 299,258÷2,288,320=13.08%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 195 | badges | \| Met the game owners! \| Wow, 150% profit. You were in a server with one of the game owners \| 15 Aug 2026 \| 1,305 \| | 名称 | badges → raw 03:47Z 快照一致(Met the game owners! 1305);现取04:19Z awardedCount=1,305 pastDay=0,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 196 | badges | Share column for Met the game owners!: 0.06% | 数字 | 自行重算 → 重算 1,305÷2,288,320=0.06%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 197 | badges | \| First Trade \| 90.1% \| 46,499 \| 97.9 \| | 数字 | badges → raw 03:47Z 快照一致(First Trade 2061945);现取04:19Z awardedCount=2,062,970 pastDay=46,796,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 198 | badges | \| First Profit \| 68.6% \| 46,436 \| 97.7 \| | 数字 | badges → raw 03:47Z 快照一致(First Profit 1569182);现取04:19Z awardedCount=1,570,195 pastDay=46,716,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 199 | badges | \| First Short \| 26.9% \| 30,247 \| 63.7 \| | 数字 | badges → raw 03:47Z 快照一致(First Short 616376);现取04:19Z awardedCount=617,054 pastDay=30,393,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 200 | badges | \| First Futures Trade \| 9.4% \| 19,052 \| 40.1 \| | 数字 | badges → raw 03:47Z 快照一致(First Futures Trade 214382);现取04:19Z awardedCount=214,794 pastDay=19,157,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 201 | badges | \| Hundred Trades \| 13.1% \| 8,331 \| 17.5 \| | 数字 | badges → raw 03:47Z 快照一致(Hundred Trades 299258);现取04:19Z awardedCount=299,437 pastDay=8,379,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 202 | updates | The next Roblox Stock Exchange 2 update is Custom Offices, an official Roblox event starting Saturday 10 October 2026 at 20:00 UTC. | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 203 | updates | Its listing promises "Your own 3d office you can walk inside of and upgrade". | 开发者原话 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 204 | updates | It follows eleven earlier events since 17 August | 数字 | events → 现取 virtual-events:12 条(带/不带 cursor 均 12;另试 previous cursor 返回 11 条为子集,未发现更早事件) ✓ | CONFIRMED |  |
| 205 | updates | We found no patch notes for Roblox Stock Exchange 2 from Summit Productions Development. | 其他 | group → 现取 group 对应字段一致 ✓ | CONFIRMED |  |
| 206 | updates | The listing runs from 20:00 UTC on 10 October to 23:00 UTC on 16 October (the exact timestamps are 20:00:18 and 23:00:18). | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 207 | updates | \| US Pacific (PDT) \| Sat 10 Oct, 13:00 \| Fri 16 Oct, 16:00 \| | 日期 | 自行重算 → 20:00 UTC−7=13:00; 23:00−7=16:00 ✓ | CONFIRMED |  |
| 208 | updates | \| US Eastern (EDT) \| Sat 10 Oct, 16:00 \| Fri 16 Oct, 19:00 \| | 日期 | 自行重算 → UTC−4: 16:00/19:00 ✓ | CONFIRMED |  |
| 209 | updates | \| Brazil (BRT) \| Sat 10 Oct, 17:00 \| Fri 16 Oct, 20:00 \| | 日期 | 自行重算 → UTC−3: 17:00/20:00 ✓ | CONFIRMED |  |
| 210 | updates | \| UK (BST) \| Sat 10 Oct, 21:00 \| Sat 17 Oct, 00:00 \| | 日期 | 自行重算 → UTC+1: 21:00 / 次日00:00(Sat 17 Oct) ✓;英国夏令时 2026-10-25 结束 ✓ | CONFIRMED |  |
| 211 | updates | \| Central Europe (CEST) \| Sat 10 Oct, 22:00 \| Sat 17 Oct, 01:00 \| | 日期 | 自行重算 → UTC+2: 22:00 / Sat 17 Oct 01:00 ✓ | CONFIRMED |  |
| 212 | updates | \| UTC+8 (Manila, Singapore) \| Sun 11 Oct, 04:00 \| Sat 17 Oct, 07:00 \| | 日期 | 自行重算 → UTC+8: Sun 11 Oct 04:00 / Sat 17 Oct 07:00 ✓ | CONFIRMED |  |
| 213 | updates | Roblox's event system lets players "opt into notifications that they'll receive when your event begins" | 规则 | docs → 现取 create.roblox.com 文档 HTTP 200,原句逐字在页 ✓ | CONFIRMED |  |
| 214 | updates | The listing's title is Custom Offices and its subtitle is "New Update". | 名称 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 215 | updates | The host is Summit Productions Development, the category is new content, and the listing was created on 3 October 2026 at 09:08 UTC. | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 216 | updates | The event art shows a single room, and no trading screen. | 其他 | image → Read 亲眼看图 evidence/img/ev_office_src.png:办公室一间房、桌上显示器K线、铜牛雕像底座刻 RSE,无交易界面 | CONFIRMED |  |
| 217 | updates | Eleven events, all hosted by the developer group and all filed under new content. | 列表字段 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 218 | updates | The listing for UI Overhaul + Features stays open until 9 October at 04:00 UTC | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 219 | updates | the newest badge was created on 15 August, two days before the first event | 日期 | badges → 现取 badges 对应字段一致 ✓ | CONFIRMED |  |
| 220 | updates | \| HEDGE FUNDS \| "Name it, pick a strategy, and specialise it three tiers deep." Four strategies: Momentum, Quant, Income and Venture \| | 列表字段 | image → Read 亲眼看图 evidence/img/ev_hedge_src.png:Name it, pick a strategy, and specialise it three tiers deep. 四张卡 MOMENTUM/QUANT/INCOME/VENTURE | CONFIRMED |  |
| 221 | updates | \| NEW FUNCTIONS \| A script editor with a MACD example, labelled 48 functions and 10 price sources \| | 数字 | image → Read 亲眼看图 evidence/img/ev_script_src.png:MACD 脚本;计数 48 FUNCTIONS / 10 PRICE SOURCES / 10 PLOTS/SCRIPT / 3 PLOT STYLES / 40 NAMED VALUES / 8 LINE COLOURS | CONFIRMED |  |
| 222 | updates | \| CHALLENGES \| Four tiers named Bootstrap, Size Up, The Floor and Whale, marked 25x, 100x, 1,000x and 10,000x, with "Challenge-only cosmetics" \| | 列表字段 | image → Read 亲眼看图 evidence/img/ev_challenges_src.png:I BOOTSTRAP 25x / II SIZE UP 100x / III THE FLOOR 1,000x / IV WHALE 10,000x;Challenge-only cosmetics | CONFIRMED |  |
| 223 | updates | \| NEW TOOLS \| Eight drawing and order tools: Trailing Stop, Fib Retracement, Fib Extension, Position Tool, Rectangle Zone, Ray, Parallel Channel and Text Note \| | 列表字段 | image → Read 亲眼看图 evidence/img/ev_tools_src.png:8 项: Trailing Stop, Fib Retracement, Fib Extension, Position Tool, Rectangle Zone, Ray, Parallel Channel, Text Note | CONFIRMED |  |
| 224 | updates | \| REAL ESTATE \| The headline "Empire Map", a map shaped like the United States and the tag "50 STATES" \| | 其他 | image → Read 亲眼看图 evidence/img/ev_empire_src.png:Empire Map;美国地图;50 STATES · TILE BY TILE | CONFIRMED |  |
| 225 | updates | \| SEASONS \| "Every Monday the board goes back to zero. Rank on return, not balance." Six tiers, from Paper Hands up to The Floor \| | 规则 | image → Read 亲眼看图 evidence/img/ev_seasons_src.png:Every Monday the board goes back to zero. Rank on return, not balance.;SIX TIERS from Paper Hands up to The Floor | CONFIRMED |  |
| 226 | updates | \| BONDS \| Three cards: Government Bonds (AAA), Corporate Bonds (BBB) and High-Yield Bonds (BB) \| | 列表字段 | image → Read 亲眼看图 evidence/img/ev_bonds_src.png:GOVERNMENT BONDS AAA / CORPORATE BONDS BBB / HIGH-YIELD BONDS BB | CONFIRMED |  |
| 227 | updates | \| COMMODITIES EXCHANGE \| Three cards: Energy (oil), Metals (gold) and Agriculture (wheat) \| | 列表字段 | image → Read 亲眼看图 evidence/img/ev_commodities_src.png:ENERGY OIL / METALS GOLD / AGRICULTURE WHEAT | CONFIRMED |  |
| 228 | updates | \| UI Overhaul + Features \| "The terminal, reimagined. Live order flow. Pro charts. Every market on one screen." \| | 开发者原话 | image → Read 亲眼看图 evidence/img/ev_ui_src.png:The terminal, reimagined. / Live order flow. Pro charts. Every market on one screen. | CONFIRMED |  |
| 229 | updates | The REAL ESTATE description says "a global map", while its art shows a United States map and says 50 states. | 其他(抽样:是) | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 230 | updates | Eight of the twelve events start on a Saturday, and every Saturday from 22 August to 10 October 2026 has one. | 日期 | 自行重算 → 22,29 Aug;5,12,19,26 Sep;3,10 Oct 2026 均为周六(自行 datetime 核算);共 8 个周六事件 ✓ | CONFIRMED |  |
| 231 | updates | The other four started on a Monday or a Wednesday: HEDGE FUNDS, NEW FUNCTIONS, CHALLENGES and NEWS OVERHAUL, all between 17 August and 2 September. | 日期 | 自行重算 → 17 Aug=周一;19 Aug,26 Aug,2 Sep=周三 ✓ | CONFIRMED |  |
| 232 | updates | Recent Saturday events began at 20:00 UTC three times in September, then 06:00 UTC for the interface overhaul, and Custom Offices is back at 20:00 UTC. | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 233 | updates | its "updated" field showed a different time on each read: 03:36:09, 03:44:15 and 03:56:24 UTC | 日期 | games → raw/games_updated_probe 三次读值 03:36:09/03:44:15/03:56:24Z 一致;我现取 04:16:34Z 又是新值,支持"updated 不是补丁日期" ✓ | CONFIRMED |  |
| 234 | updates | \| 13 July \| The experience itself; 8 game passes; 11 developer products, including the four algo bot products and the three time skips; 5 badges \| | 日期 | 自行重算 → 13 Jul: 8 passes/11 products/5 badges(自行按 created 字段统计) ✓ | CONFIRMED |  |
| 235 | updates | \| 14 July \| More Player Companies pass; Double Earnings and Trader Starter Pack; 5 more badges \| | 日期 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 236 | updates | \| 19 July \| Overnight Desk pass; 10 products with pass-style names \| | 日期 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 237 | updates | \| 8 and 9 August \| Custom Timeframes and Unlimited AI Usage passes; three AI Token packs \| | 日期 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 238 | updates | \| 15 August \| All Gamepasses Bundle pass; Instant Acension and three products with pass names; the Met the game owners! badge \| | 日期 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 239 | updates | \| 2 October \| Trader Pass - Season 1 \| | 日期 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 240 | updates | After the Custom Offices listing ends on 16 October | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 241 | updates | alt ev_seasons: a list of eight new features including Weekly Reset, Ranked on Return and Six Tiers | 列表字段 | image → Read 亲眼看图 evidence/img/ev_seasons_src.png:右栏 8 NEW: Weekly Reset, Ranked on Return, Six Tiers, Your Division, Rank Badge, Placement Week, Season Rewards, Season Recap | CONFIRMED |  |
| 242 | updates | alt ev_bonds: above the line Trade debt. Earn interest. Weigh the risk. | 开发者原话 | image → Read 亲眼看图 evidence/img/ev_bonds_src.png:Trade debt. Earn interest. Weigh the risk. | CONFIRMED |  |
| 243 | updates | \| HEDGE FUNDS \| UPDATE \| Mon 17 Aug, 23:00 \| Run a hedge fund \| | 开发者原话 | events → events 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 244 | updates | \| NEW FUNCTIONS \| Scripting Overhaul \| Wed 19 Aug, 21:00 \| Tons of new functions and additions to the script editor so you can continue to make advanced indicators! \| | 开发者原话 | events → events 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 245 | updates | \| NEW MEMECOINS \| UPDATE \| Sat 22 Aug, 21:00 \| This update will feature new meme coins in the Crypto tab. This system will work in a different way, they will launch at random in the game, and have different results. \| | 开发者原话 | events → events 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 246 | updates | \| CHALLENGES \| UPDATE \| Wed 26 Aug, 20:00 \| New challenges, this will feature starting at a low amount to make a much higher amount, your reward will be a permeant perk + exclusive cosmetic \| | 开发者原话 | events → events 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 247 | updates | \| NEW TOOLS \| UPDATE \| Sat 29 Aug, 22:00 \| New tools such as fib extension, trailing stops, and so much more! \| | 开发者原话 | events → events 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 248 | updates | \| NEWS OVERHAUL \| "THE WIRE" \| Wed 2 Sep, 22:00 \| This update will feature a brand new news system, and more news events. \| | 开发者原话 | events → events 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 249 | updates | \| REAL ESTATE \| UPDATE \| Sat 5 Sep, 10:00 \| In this update, you'll be able to buy real estate across a global map. \| | 开发者原话 | events → events 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 250 | updates | \| SEASONS \| New content \| Sat 12 Sep, 20:00 \| This update will include seasons. \| | 开发者原话 | events → events 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 251 | updates | \| BONDS \| UPDATE \| Sat 19 Sep, 20:00 \| Trade debt, earn interest, weigh the risk. \| | 开发者原话 | events → events 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 252 | updates | \| COMMODITIES EXCHANGE \| NEW UPDATE \| Sat 26 Sep, 20:00 \| Prices will be driven by new news events, such as weather reports and more \| | 开发者原话 | events → events 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 253 | updates | \| UI Overhaul + Features \| Content Update \| Sat 3 Oct, 06:00 \| This update will feature a brand new interface for the game, reorganized interfaces, and new game features! \| | 开发者原话 | events → events 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 254 | community | Roblox Stock Exchange 2 is made by the Roblox group Summit Productions Development, which had 276,709 members on 8 October 2026. | 数字 | group → 现取 memberCount=276,833(作者 276,709) | CONFIRMED |  |
| 255 | community | because the game's social links cannot be read without a Roblox login | 其他 | social → 现取 social-links/list → 401 {"message":"Authentication token is missing"} ✓ | CONFIRMED |  |
| 256 | community | \| Group ID \| 33446529 \| | 数字 | group → 现取 group 对应字段一致 ✓ | CONFIRMED |  |
| 257 | community | \| Created \| 28 November 2023 \| | 日期 | groupv2 → 现取 groups v2 created=2023-11-28T20:59:24Z ✓ | CONFIRMED |  |
| 258 | community | \| Owner account \| SummitGroupHoIder (account created 12 May 2024) \| | 名称 | owner → 现取 users v1 created=2024-05-12T21:10Z ✓ | CONFIRMED |  |
| 259 | community | \| Owner account \| SummitGroupHoIder (account created 12 May 2024) \| | 名称 | group → 现取 group 对应字段一致 ✓ | CONFIRMED |  |
| 260 | community | \| Verified badge \| No \| | 其他(抽样:是) | group → 现取 group 对应字段一致 ✓ | CONFIRMED |  |
| 261 | community | \| Entry \| Open; anyone can join \| | 其他(抽样:是) | group → 现取 group 对应字段一致 ✓ | CONFIRMED |  |
| 262 | community | \| Description \| Empty \| | 其他 | group → 现取 group 对应字段一致 ✓ | CONFIRMED |  |
| 263 | community | \| Shout \| None \| | 其他 | group → 现取 group 对应字段一致 ✓ | CONFIRMED |  |
| 264 | community | \| Roles \| Guest, Member, Client, Staff, Contracted Developer, Developer, Operations Director, President, Holder \| | 列表字段 | roles → 现取 roles: Guest, Member, Client, Staff, Contracted Developer, Developer, Operations Director, President, Holder ✓ | CONFIRMED |  |
| 265 | community | its own profile description is empty | 其他 | owner → 现取 owner 对应字段一致 ✓ | CONFIRMED |  |
| 266 | community | Five public experiences are attached to the group. | 数字 | groupgames → 现取 group games:5 条 ✓ | CONFIRMED |  |
| 267 | community | its description still talks about its own features, such as an options chain that unlocks at two rebirths | 开发者原话 | groupgames → 现取 legacy universe 7757905683 description 含 "Options Chain unlocks at 2 Rebirths" ✓(同一描述另含 "Join the Main Group for a $10,000 starting cash bonus!",见漏列表 community 页 "Nothing in the official text we read says that joining the group gives an in-game reward" 一条) | CONFIRMED |  |
| 268 | community | Discord's public data for the invite code qR8v6Murp3 | 其他 | discord → 现取 code=qR8v6Murp3 ✓ | CONFIRMED |  |
| 269 | community | \| Server name \| Roblox Stock Exchange 2 \| | 名称 | discord → 现取 discord 对应字段一致 ✓ | CONFIRMED |  |
| 270 | community | \| Self-description \| "Official server for RSE: Roblox Stock Exchange 2" \| | 开发者原话 | discord → 现取 discord 对应字段一致 ✓ | CONFIRMED |  |
| 271 | community | \| Members (approx.) \| 1,231 \| | 数字 | discord → 现取 Discord invite 04:19Z approximate_member_count=1,232(作者 1,231) | CONFIRMED |  |
| 272 | community | \| Online (approx.) \| 182 \| | 数字 | discord → 现取 approximate_presence_count=175(作者 182,在线数波动) | CONFIRMED |  |
| 273 | community | \| Invite expiry \| None set \| | 其他 | discord → 现取 expires_at=null ✓ | CONFIRMED |  |
| 274 | community | Two code sites, Pro Game Guides and Try Hard Guides, link the same invite | 其他 | tryhard → tryhardguides 现取 HTTP 200: dateModified 2026-09-29T23:02:03-07:00;列 TOOLS(NEW)+STOCKMARKET/MEMECOINS/FUTURES/UPDATE/BULLMARKET/RELEASE;"Press the yellow gift/present button in the right corner of the screen. Enter a working code in the ENTER CODE text box and hit the yellow Redeem button." ✓ | CONFIRMED |  |
| 275 | community | Two code sites, Pro Game Guides and Try Hard Guides, link the same invite | 其他(抽样:是) | progameguides → progameguides 403;Try Hard Guides 页面含 discord.com/invite/qR8v6Murp3 ✓ | UNVERIFIED | "Two code sites, Pro Game Guides and Try Hard Guides, link the same invite" → "Try Hard Guides links the same invite" (unless Pro Game Guides is re-read) |
| 276 | community | Roblox refused our request for the game's social links with a 401 error because we were not signed in | 其他 | social → 现取 social-links/list → 401 {"message":"Authentication token is missing"} ✓ | CONFIRMED |  |
| 277 | community | social media links "are only visible to users who have verified their age as at least 16 years old" | 规则 | docs → 现取 create.roblox.com 文档 HTTP 200,原句逐字在页 ✓ | CONFIRMED |  |
| 278 | community | \| Players online \| 1,123 \| | 数字 | games → 现取 playing=1,049(作者 1,123;在线数日内波动,页面带时间戳) | CONFIRMED |  |
| 279 | community | \| Visits \| 5,093,566 \| | 数字 | games → games v1 现取04:19Z visits=5,097,144(作者03:39Z=5,093,566,raw一致;增量合理) | CONFIRMED |  |
| 280 | community | \| Favourites \| 61,993 \| | 数字 | games → 现取 favoritedCount=62,033(作者 61,993,量级吻合) | CONFIRMED |  |
| 281 | community | \| Likes / dislikes \| 12,004 / 890 (about 93.1% positive) \| | 数字 | votes → 现取 votes 12,014 / 891(作者 12,004 / 890) | CONFIRMED |  |
| 282 | community | \| Likes / dislikes \| 12,004 / 890 (about 93.1% positive) \| | 数字 | 自行重算 → 12,004/(12,004+890)=93.10% ✓ | CONFIRMED |  |
| 283 | community | there have been 12 since 17 August 2026 | 数字 | events → 现取 virtual-events:12 条(带/不带 cursor 均 12;另试 previous cursor 返回 11 条为子集,未发现更早事件) ✓ | CONFIRMED |  |
| 284 | community | the group wall, where our request came back with a 404 error | 其他 | groupv2 → 现取 groups v1/v2 wall/posts → 404 ✓ | CONFIRMED |  |
| 285 | community | One independent fan site, robloxstockexchange2.wiki, had five pages when we checked | 数字 | wiki → 现取 robloxstockexchange2.wiki/sitemap.xml:5 个 URL;首页 "independent learning guide. It is not affiliated with Roblox or the game's developer" ✓ | CONFIRMED |  |
| 286 | community | states that it is not affiliated with the developer | 其他 | wiki → 现取 robloxstockexchange2.wiki/sitemap.xml:5 个 URL;首页 "independent learning guide. It is not affiliated with Roblox or the game's developer" ✓ | CONFIRMED |  |
| 287 | community | tldr: The same group also publishes Legacy: Roblox Stock Exchange, the earlier game, created on 23 May 2025. | 日期 | groupgames → 现取 group games Legacy created=2025-05-23T22:22Z ✓ | CONFIRMED |  |
| 288 | community | alt ev_ui: the words The terminal, reimagined above a wide screenshot of the trading terminal | 其他 | image → Read 亲眼看图 evidence/img/ev_ui_src.png:The terminal, reimagined.;下方为交易终端截图(市场列表/K线/Trades 列/下单面板) | CONFIRMED |  |
| 289 | community | 23 May 2025 \| 8,600 \| | 数字 | groupgames → 现取 group games placeVisits:Legacy 8,600 / INDEFINITE 14,348 / Rocket Wars 512,506 / RSE2 5,097,313 / Hex 740,462(作者值同量级) | CONFIRMED |  |
| 290 | community | 18 Nov 2025 \| 14,346 \| | 数字 | groupgames → 名称必须逐字:接口 name 为 "INDEFINITE \| Dreamcore 🌫️ Backrooms 🚪" | REFUTED | "INDEFINITE \\| Dreamcore Backrooms" → "INDEFINITE \\| Dreamcore 🌫️ Backrooms 🚪" (the listed title contains two emoji) or add "(title shortened)" |
| 291 | community | 5 May 2026 \| 512,502 \| | 数字 | groupgames → 现取 group games placeVisits:Legacy 8,600 / INDEFINITE 14,348 / Rocket Wars 512,506 / RSE2 5,097,313 / Hex 740,462(作者值同量级) | CONFIRMED |  |
| 292 | community | 13 Jul 2026 \| 5,093,566 \| | 数字 | groupgames → 现取 group games placeVisits:Legacy 8,600 / INDEFINITE 14,348 / Rocket Wars 512,506 / RSE2 5,097,313 / Hex 740,462(作者值同量级) | CONFIRMED |  |
| 293 | community | 24 Jul 2026 \| 740,416 \| | 数字 | groupgames → 现取 group games placeVisits:Legacy 8,600 / INDEFINITE 14,348 / Rocket Wars 512,506 / RSE2 5,097,313 / Hex 740,462(作者值同量级) | CONFIRMED |  |
| 294 | gamepasses | Roblox Stock Exchange 2 sells 13 game passes. | 数字 | passes → 现取 passes API:13 条,nextPageToken 空 ✓ | CONFIRMED |  |
| 295 | gamepasses | Twelve are single passes priced from 39 Robux (Custom Timeframes) to 299 Robux (Insider) | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 296 | gamepasses | the thirteenth is the All Gamepasses Bundle at 999 Robux | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 297 | gamepasses | Bought separately the twelve cost 1,778 Robux. | 价格 | 自行重算 → 39+49+79+99+129+149+149+159+199+199+229+299=1,778 ✓(我跑脚本得 1778) | CONFIRMED |  |
| 298 | gamepasses | All 13 were on sale and none showed a discount. | 其他(抽样:是) | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 299 | gamepasses | Eight of the passes were created on 13 July 2026, the day the game was created. | 日期 | 自行重算 → 8 个 pass created=2026-07-13;game created 2026-07-13T06:42Z ✓ | CONFIRMED |  |
| 300 | gamepasses | More Player Companies followed on 14 July, Overnight Desk on 19 July, Custom Timeframes and Unlimited AI Usage on 8 and 9 August, and the bundle on 15 August. | 日期 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 301 | gamepasses | \| All 12 single passes bought separately \| 1,778 \| | 价格 | 自行重算 → 同上 1,778 ✓ | CONFIRMED |  |
| 302 | gamepasses | \| Difference \| 779 (about 44% less) \| | 价格 | 自行重算 → 1,778−999=779;779/1,778=43.8% ✓ | CONFIRMED |  |
| 303 | gamepasses | "All gamepasses, but at a lower cost." | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 304 | gamepasses | Insider, VIP, Order Flow, Overnight Desk and Executive Terminal together already come to 1,085. | 价格 | 自行重算 → 299+229+199+199+159=1,085 ✓ | CONFIRMED |  |
| 305 | gamepasses | \| Overnight Desk \| Market runs 24 hours offline \| 8 hours \| | 规则 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 306 | gamepasses | \| More Player Companies \| Up to 5 player-founded stocks \| 2 \| | 规则 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 307 | gamepasses | \| Max Leverage \| Up to 50x leverage at any level \| Not stated \| | 规则 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 308 | gamepasses | \| Pro Trader \| 0.02% fees, unlimited drawings \| Not stated \| | 规则 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 309 | gamepasses | **Order Flow** shows "Level 2 order book data" and "bias direction based off the flow of orders" | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 310 | gamepasses | **Insider** gives "Early alerts before news hits + IPO intel." | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 311 | gamepasses | **Indicator Pro** lets you "Run up to 8 community or custom indicators at the same time." | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 312 | gamepasses | **Watchlist Pro** gives "10 custom watchlists with up to 50 symbols in each list." | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 313 | gamepasses | **Custom Timeframes** unlocks "any custom timeframes, such as 1 second charts and more." | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 314 | gamepasses | **Unlimited AI Usage** lets you "Ask SummitAI as much as you like", with "no daily or weekly cap". | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 315 | gamepasses | **Executive Terminal** adds gold branding, "an exclusive set of stocks" and "private market algorithmic bot scans" | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 316 | gamepasses | "2x XP, 2x daily rewards, VIP badge, 1 free Sim Day per day." | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 317 | gamepasses | A single Simulate Day costs 39 Robux in the shop | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 318 | gamepasses | Eleven of the 13 passes have a developer product with exactly the same name, and four of those carry a different price | 数字 | 自行重算 → 同名 11 个(Pro Trader, Insider, Max Leverage, VIP, Order Flow, Watchlist Pro, Indicator Pro, Executive Terminal, Unlimited AI Usage, Custom Timeframes, All Gamepasses Bundle);价格不同 4 个 ✓ | CONFIRMED |  |
| 319 | gamepasses | If it shows 399 for VIP, you are looking at the product, and the pass itself costs 229. | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 320 | gamepasses | If it shows 399 for VIP, you are looking at the product, and the pass itself costs 229. | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 321 | gamepasses | Roblox defines a pass as "a one-time Robux fee to access special privileges inside your game" | 规则 | docs → 现取 create.roblox.com 文档 HTTP 200,原句逐字在页 ✓ | CONFIRMED |  |
| 322 | gamepasses | Roblox defines a developer product as "an item or ability that a user can purchase more than once" | 规则 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 323 | gamepasses | Overnight Desk triples the offline window from 8 to 24 hours. | 规则 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 324 | gamepasses | Custom Timeframes (39) and Watchlist Pro (49) are the two cheapest passes. | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 325 | gamepasses | alt ev_ui: with the label RSE EXECUTIVE in the top-left corner of the interface | 其他 | image → Read 亲眼看图 evidence/img/ev_ui_src.png:终端左上 RSE EXECUTIVE | CONFIRMED |  |
| 326 | gamepasses | caption ev_tools: drawing tools were expanded in an update announced for 29 August 2026 | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 327 | gamepasses | \| All Gamepasses Bundle \| 999 \| All gamepasses, but at a lower cost. \| | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 328 | gamepasses | \| Executive Terminal \| 159 \| Permanent gold terminal branding and Executive status treatment. Gives access to an exclusive set of stocks, and unlocks private market algorithmic bot scans. \| | 价格 | passes → passes 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 329 | gamepasses | \| Insider \| 299 \| Early alerts before news hits + IPO intel. \| | 价格 | passes → passes 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 330 | gamepasses | \| Max Leverage \| 149 \| Up to 50x leverage at any level. \| | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 331 | gamepasses | \| Pro Trader \| 99 \| 0.02% fees, unlimited drawings, pro stats. \| | 价格 | passes → passes 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 332 | gamepasses | \| Order Flow \| 199 \| Level 2 order book data, shows placed orders along the book, and shows bias direction based off the flow of orders. \| | 价格 | passes → passes 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 333 | gamepasses | \| VIP \| 229 \| 2x XP, 2x daily rewards, VIP badge, 1 free Sim Day per day. \| | 价格 | passes → passes 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 334 | gamepasses | \| Unlimited AI Usage \| 79 \| Ask SummitAI as much as you like: no daily or weekly cap, a much larger conversation memory, and the top effort tiers always available. \| | 价格 | passes → passes 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 335 | gamepasses | \| Overnight Desk \| 199 \| Your market keeps running for 24 hours offline instead of 8. \| | 价格 | passes → passes 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 336 | gamepasses | \| Custom Timeframes \| 39 \| Access to any custom timeframes, such as 1 second charts and more. \| | 价格 | passes → passes 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 337 | gamepasses | \| Watchlist Pro \| 49 \| 10 custom watchlists with up to 50 symbols in each list. \| | 价格 | passes → passes 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 338 | gamepasses | \| Indicator Pro \| 129 \| Run up to 8 community or custom indicators at the same time. \| | 价格 | passes → passes 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 339 | gamepasses | \| More Player Companies \| 149 \| Launch up to 5 player-founded stocks instead of 2. \| | 价格 | passes → passes 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 340 | gamepasses | \| Pro Trader \| 99 \| 99 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 341 | gamepasses | \| Insider \| 299 \| 299 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 342 | gamepasses | \| Max Leverage \| 149 \| 149 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 343 | gamepasses | \| VIP \| 229 \| 399 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 344 | gamepasses | \| Order Flow \| 199 \| 249 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 345 | gamepasses | \| Watchlist Pro \| 49 \| 99 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 346 | gamepasses | \| Indicator Pro \| 129 \| 129 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 347 | gamepasses | \| Executive Terminal \| 159 \| 139 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 348 | gamepasses | \| Unlimited AI Usage \| 79 \| 79 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 349 | gamepasses | \| Custom Timeframes \| 39 \| 39 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 350 | gamepasses | \| All Gamepasses Bundle \| 999 \| 999 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 351 | shop | Roblox Stock Exchange 2 has 31 developer products, priced from 9 to 999 Robux. | 数字 | prod → 现取 developerproducts:31 条,nextPageCursor=null ✓ | CONFIRMED |  |
| 352 | shop | Only one carries an official description. | 数字 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 353 | shop | Roblox defines a developer product as "an item or ability that a user can purchase more than once" | 规则 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 354 | shop | All 31 were on sale on 8 October 2026. | 其他 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 355 | shop | "Instant Acension" is spelled that way in the listing. | 名称 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 356 | shop | eight products cost under 40 Robux, and four cost 249 | 数字 | 自行重算 → <40: 9,39,39,19,19,19,29,39 = 8 个;=249: Tune Entire Algo Fleet, Order Flow, Company Mogul, Instant Acension = 4 个 ✓ | CONFIRMED |  |
| 357 | shop | The VIP game pass includes "1 free Sim Day per day", and a single Simulate Day is 39 Robux here. | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 358 | shop | It is the newest product, created on 2 October 2026 | 日期 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 359 | shop | "Unlocks the premium track of Trader Pass Season 1, The Golden Bell: 22 animated exclusives and 20,000 AI tokens. Cosmetic only, no cash or boosts." | 开发者原话 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 360 | shop | So for 199 Robux you get a premium reward track | 价格 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 361 | shop | A 20,000 AI Tokens pack on its own costs 49 Robux. | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 362 | shop | Seasons themselves arrived with an event on 12 September | 日期 | events → 事件列表是预告,页面自己也说"不证明功能上线时间" | UNVERIFIED | "Seasons themselves arrived with an event on 12 September" → "Seasons were announced with an event starting 12 September" |
| 363 | shop | Three packs, all created on 9 August 2026 | 日期 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 364 | shop | \| 5,000 AI Tokens \| 29 \| about 172 \| | 价格 | 自行重算 → 5000/29=172.4 ✓ | CONFIRMED |  |
| 365 | shop | \| 20,000 AI Tokens \| 49 \| about 408 \| | 价格 | 自行重算 → 20000/49=408.2 ✓ | CONFIRMED |  |
| 366 | shop | \| 75,000 AI Tokens \| 69 \| about 1,087 \| | 价格 | 自行重算 → 75000/69=1086.96 ✓ | CONFIRMED |  |
| 367 | shop | 15 times the tokens of the small pack for a little over twice the price | 数字 | 自行重算 → 75000/5000=15;69/29=2.38 ✓ | CONFIRMED |  |
| 368 | shop | That pass, Unlimited AI Usage (79 Robux), is described as "no daily or weekly cap, a much larger conversation memory, and the top effort tiers always available" | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 369 | shop | 15 minutes for 49 Robux, one hour for 149 and one day for 499 | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 370 | shop | Eleven do, and for seven of them the price matches the pass. | 数字 | 自行重算 → 11 同名;价格相同 7 (Custom Timeframes, Unlimited AI Usage, Pro Trader, Indicator Pro, Max Leverage, Insider, Bundle);不同 4 ✓ | CONFIRMED |  |
| 371 | shop | \| Watchlist Pro \| 49 \| 99 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 372 | shop | \| Executive Terminal \| 159 \| 139 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 373 | shop | \| Order Flow \| 199 \| 249 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 374 | shop | \| VIP \| 229 \| 399 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 375 | shop | Two more products, Offline Earnings (199) and Company Mogul (249), have pass-style names but no pass with the same name. | 价格 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 376 | shop | Skip Recovery, Double Earnings and Trader Starter Pack cost 19 Robux each, and Instant Acension costs 249. | 价格 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 377 | shop | describes "Challenge-only cosmetics" as "Not in the shop. Not on the item market." | 开发者原话 | image → Read 亲眼看图 evidence/img/ev_challenges_src.png:Challenge-only cosmetics / Not in the shop. Not on the item market. | CONFIRMED |  |
| 378 | shop | Deploy Algo Bot, the two upgrades and Tune Entire Algo Fleet range from 39 to 249 Robux | 价格 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 379 | shop | tldr: the 75,000 pack costs 69 Robux, about six times more tokens per Robux than the 5,000 pack | 数字 | 自行重算 → 1,087/172=6.3 ✓ | CONFIRMED |  |
| 380 | shop | tldr: Thirteen products carry pass-style names, and VIP costs 399 as a product against 229 as a game pass. | 数字 | 自行重算 → 11+2=13 ✓ | CONFIRMED |  |
| 381 | shop | alt th1: the label MARKET OPEN | 其他 | image → Read 亲眼看图 evidence/img/th1_src.png:右下 MARKET OPEN | CONFIRMED |  |
| 382 | shop | alt ev_challenges: a challenge run chart climbing to a 5 million target | 其他 | image → Read 亲眼看图 evidence/img/ev_challenges_src.png:START $5K / TARGET $5M | CONFIRMED |  |
| 383 | shop | \| Skip to Market Open \| 9 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 384 | shop | \| Simulate Day \| 39 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 385 | shop | \| Simulate Week \| 99 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 386 | shop | \| 15-Min Trader Spotlight \| 49 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 387 | shop | \| 1-Hour Trader Spotlight \| 149 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 388 | shop | \| 1-Day Trader Spotlight \| 499 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 389 | shop | \| Tune Entire Algo Fleet \| 249 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 390 | shop | \| Deploy Algo Bot \| 149 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 391 | shop | \| Algo Scan Upgrade \| 39 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 392 | shop | \| Algo Expertise Upgrade \| 79 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 393 | shop | \| Skip Recovery \| 19 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 394 | shop | \| Double Earnings \| 19 \| 14 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 395 | shop | \| Trader Starter Pack \| 19 \| 14 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 396 | shop | \| Pro Trader \| 99 \| 19 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 397 | shop | \| Insider \| 299 \| 19 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 398 | shop | \| Max Leverage \| 149 \| 19 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 399 | shop | \| VIP \| 399 \| 19 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 400 | shop | \| Order Flow \| 249 \| 19 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 401 | shop | \| Watchlist Pro \| 99 \| 19 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 402 | shop | \| Indicator Pro \| 129 \| 19 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 403 | shop | \| Executive Terminal \| 139 \| 19 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 404 | shop | \| Company Mogul \| 249 \| 19 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 405 | shop | \| Offline Earnings \| 199 \| 19 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 406 | shop | \| 5,000 AI Tokens \| 29 \| 9 Aug 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 407 | shop | \| 20,000 AI Tokens \| 49 \| 9 Aug 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 408 | shop | \| 75,000 AI Tokens \| 69 \| 9 Aug 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 409 | shop | \| Unlimited AI Usage \| 79 \| 15 Aug 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 410 | shop | \| Custom Timeframes \| 39 \| 15 Aug 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 411 | shop | \| All Gamepasses Bundle \| 999 \| 15 Aug 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 412 | shop | \| Instant Acension \| 249 \| 15 Aug 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 413 | shop | \| Trader Pass - Season 1 \| 199 \| 2 Oct 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 414 | algo-bots | Algorithmic bots in Roblox Stock Exchange 2 are something you "unlock and upgrade", in the words of the official description. | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 415 | algo-bots | four Robux products priced from 39 to 249 | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 416 | algo-bots | a First Algo Bot badge held by about 2 in 100 players | 数字 | 自行重算 → 重算 50,910÷2,288,320=2.22%(raw 03:47Z 值);现取值同量级 | CONFIRMED |  |
| 417 | algo-bots | \| Game description \| "Unlock and upgrade algorithmic trading bots" \| | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 418 | algo-bots | \| First Algo Bot badge \| "You created your first algorithmic trading bot!" \| | 开发者原话 | badges → 现取 badges 对应字段一致 ✓ | CONFIRMED |  |
| 419 | algo-bots | \| Executive Terminal pass \| "unlocks private market algorithmic bot scans" \| | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 420 | algo-bots | \| HEDGE FUNDS event art \| Quant strategy: "Sharper algorithmic execution: your bots pay less commission." \| | 开发者原话 | image → Read 亲眼看图 evidence/img/ev_hedge_src.png:QUANT: Sharper algorithmic execution: your bots pay less commission. | CONFIRMED |  |
| 421 | algo-bots | All four were created on 13 July 2026, the day the game was created, and none has a description. | 日期 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 422 | algo-bots | "best bot settings" is one of Google's suggested searches for the game | 其他 | google-suggest → 现取 suggestqueries.google.com q="roblox stock exchange 2 b" → 首条 "roblox stock exchange 2 best bot settings" ✓(B级,随时间会变) | CONFIRMED |  |
| 423 | algo-bots | The description promises a P&L calendar to "Track your performance" | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 424 | algo-bots | the game does not "provide financial advice" | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 425 | algo-bots | An official event titled HEDGE FUNDS started on 17 August 2026 with the description "Run a hedge fund". | 日期 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 426 | algo-bots | Its art says you "Name it, pick a strategy, and specialise it three tiers deep", and shows four strategies. | 开发者原话 | image → Read 亲眼看图 evidence/img/ev_hedge_src.png:Name it, pick a strategy, and specialise it three tiers deep. 4 STRATEGIES · 3 TIERS EACH | CONFIRMED |  |
| 427 | algo-bots | \| Momentum \| "Compound expertise faster from profitable manual closes." \| Mastery & close XP: +10%, +20%, +30% \| | 列表字段 | image → Read 亲眼看图 evidence/img/ev_hedge_src.png:MOMENTUM: Compound expertise faster from profitable manual closes.;MASTERY & CLOSE XP I +10% II +20% III +30% | CONFIRMED |  |
| 428 | algo-bots | \| Quant \| "Sharper algorithmic execution: your bots pay less commission." \| Bot commission: -5%, -10%, -15% \| | 列表字段 | image → Read 亲眼看图 evidence/img/ev_hedge_src.png:QUANT: BOT COMMISSION I -5% II -10% III -15% | CONFIRMED |  |
| 429 | algo-bots | \| Income \| "Boost dividends and Treasury Desk interest." \| Daily income: +10%, +25%, +45% \| | 列表字段 | image → Read 亲眼看图 evidence/img/ev_hedge_src.png:INCOME: Boost dividends and Treasury Desk interest.;DAILY INCOME +10% +25% +45% | CONFIRMED |  |
| 430 | algo-bots | \| Venture \| "Launch player-founded companies with more simulated-investor hype." \| Launch hype: +5, +10, +15 \| | 列表字段 | image → Read 亲眼看图 evidence/img/ev_hedge_src.png:VENTURE: Launch player-founded companies with more simulated-investor hype.;LAUNCH HYPE +5 +10 +15 | CONFIRMED |  |
| 431 | algo-bots | The First Algo Bot badge had 50,910 awards when we checked, against 2,288,320 for the Welcome badge. | 数字 | badges → raw 03:47Z 快照一致(First Algo Bot 50910);现取04:19Z awardedCount=50,945 pastDay=1,401,量级吻合;页面均带 8 Oct 日期 | CONFIRMED |  |
| 432 | algo-bots | In the day before our check it was awarded 1,404 times. | 数字 | badges → raw 03:47Z 快照一致(First Algo Bot pastDay=1404);现取 pastDay=1,401 | CONFIRMED |  |
| 433 | algo-bots | the Millionaire badge had 100,099 awards, about twice as many | 数字 | 自行重算 → 100,099/50,910=1.966 ✓ | CONFIRMED |  |
| 434 | algo-bots | The description says you can grow your portfolio "even while you’re offline" | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 435 | algo-bots | the Overnight Desk pass says "Your market keeps running for 24 hours offline instead of 8." | 开发者原话 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 436 | algo-bots | the NEW FUNCTIONS event describes it as a way "to make advanced indicators" | 开发者原话 | events → 现取 events API 对应字段一致 ✓ | CONFIRMED |  |
| 437 | algo-bots | tldr: Algo Scan Upgrade (39), Algo Expertise Upgrade (79), Deploy Algo Bot (149) and Tune Entire Algo Fleet (249) | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 438 | algo-bots | alt ev_script: six counters, including 48 functions and 10 price sources | 数字 | image → Read 亲眼看图 evidence/img/ev_script_src.png:六个计数 48/10/10/3/40/8,含 48 FUNCTIONS、10 PRICE SOURCES | CONFIRMED |  |
| 439 | algo-bots | \| Algo Scan Upgrade \| 39 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 440 | algo-bots | \| Algo Expertise Upgrade \| 79 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 441 | algo-bots | \| Deploy Algo Bot \| 149 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 442 | algo-bots | \| Tune Entire Algo Fleet \| 249 \| 13 Jul 2026 \| | 价格 | prod → prod 现取04:19Z,名称/价格/描述/创建日期与作者行逐字一致 | CONFIRMED |  |
| 443 | beginner | the game description, 11 badges, 13 pass descriptions and 12 event listings | 数字 | events → 现取 virtual-events:12 条(带/不带 cursor 均 12;另试 previous cursor 返回 11 条为子集,未发现更早事件) ✓ | CONFIRMED |  |
| 444 | beginner | the 15,000-like target for the next one, and why six more codes from other sites are not listed | 数字 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 445 | beginner | The next official event with start times in seven zones, all eleven earlier events in the developer's words | 数字 | events → 现取 virtual-events:12 条(带/不带 cursor 均 12;另试 previous cursor 返回 11 条为子集,未发现更早事件) ✓ | CONFIRMED |  |
| 446 | beginner | The group behind the game in numbers, its four other experiences | 数字 | groupgames → 现取 group games:5 条 ✓ | CONFIRMED |  |
| 447 | beginner | nearly everyone gets First Trade, about two thirds get First Profit, and only about a quarter ever short a stock | 数字 | 自行重算 → 自行重算,与摘录一致 | CONFIRMED |  |
| 448 | beginner | \| Read the order tools \| Limit orders, stop losses and take profits are named in the description \| How to play \| | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 449 | beginner | An official event has started every Saturday since 22 August, and the next is listed for 10 October | 日期 | 自行重算 → 22 Aug…3 Oct 每个周六均有 startUtc;下一个 2026-10-10 ✓ | CONFIRMED |  |
| 450 | beginner | lists all 13 passes and 31 products with official prices | 数字 | prod → 现取 developerproducts:31 条,nextPageCursor=null ✓ | CONFIRMED |  |
| 451 | beginner | what the pass descriptions reveal about leverage, fees and the 8-hour offline window | 规则 | passes → 同 #88(低严重度) | UNVERIFIED | "what the pass descriptions reveal about leverage, fees and the 8-hour offline window" → "what the pass descriptions say about leverage, fees and offline time" |
| 452 | beginner | All markets and currencies in the game are simulated | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 453 | robux | 13 game passes that you buy once, and 31 developer products that you can buy again | 数字 | passes → 现取 passes API:13 条,nextPageToken 空 ✓ | CONFIRMED |  |
| 454 | robux | from Custom Timeframes at 39 Robux to the All Gamepasses Bundle at 999 | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 455 | robux | Time skips from 9 Robux, three AI Token packs, Trader Spotlight by the minute, hour or day | 价格 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 456 | robux | the Season 1 Trader Pass, which the developer describes as cosmetic only | 开发者原话 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 457 | robux | the hedge fund strategy that lowers bot commission | 其他 | image → Read 亲眼看图 evidence/img/ev_hedge_src.png:QUANT / BOT COMMISSION -5% -10% -15% | CONFIRMED |  |
| 458 | robux | \| Single game pass \| 12 \| 39 to 299 \| No \| All 12 \| | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 459 | robux | \| All Gamepasses Bundle \| 1 \| 999 \| No \| One line \| | 价格 | passes → 现取 passes 对应字段一致 ✓ | CONFIRMED |  |
| 460 | robux | \| Developer product \| 31 \| 9 to 999 \| Yes \| 1 of 31 \| | 数字 | prod → 现取 developerproducts:31 条,nextPageCursor=null ✓ | CONFIRMED |  |
| 461 | robux | A pass is "a one-time Robux fee to access special privileges inside your game" | 规则 | docs → 现取 create.roblox.com 文档 HTTP 200,原句逐字在页 ✓ | CONFIRMED |  |
| 462 | robux | a developer product is "an item or ability that a user can purchase more than once" | 规则 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 463 | robux | including 8 hours of offline market time and two player-founded companies | 规则 | passes → 同 #88;两处基础值均为推断 | UNVERIFIED | "including 8 hours of offline market time and two player-founded companies" → "including, according to the pass descriptions, an 8-hour offline window and two player-founded companies" |
| 464 | robux | The developer added a product as recently as 2 October | 日期 | prod → 现取 prod 对应字段一致 ✓ | CONFIRMED |  |
| 465 | author | The developer states that all markets and currencies in the game are simulated. | 开发者原话 | games → 现取 games v1 description/字段一致 ✓ | CONFIRMED |  |
| 466 | author | The game updates about once a week. | 日期 | 自行重算 → 由事件列表推出"游戏每周更新",事件≠上线 | UNVERIFIED | "The game updates about once a week." → "Official update events have been listed about once a week since 17 August 2026." |
| 467 | author | alt icon: a rising arrow filled with scenes of a candlestick chart, a computer chip, solar panels, data servers and a city campus | 其他 | image → Read 亲眼看图 evidence/img/icon_src.png:上升箭头内嵌 K线、芯片、太阳能板、服务器、城市楼群 | CONFIRMED |  |