# codes 页终稿第二轮核验（r2）

40 条命题，0 条被推翻，2 条未验。取证时间 2026-10-10 00:27–00:31 UTC，全部自己重取（games / developerproducts / game-passes / badges / groups 34744238 / votes / virtual-events / 社交链接），未读 raw、sites、旧 verify 文件。
活动接口轮询：20 次、间隔 2 秒，8 条出现 14 次（第 7–20 次），1 条出现 6 次（第 1–6 次，且每次都是 "EGGS & PETS are COMING!"，end 2026-10-15T16:00:27Z）。最多 8 条。页面「有时 8 条、有时只回未结束的那 1 条」属实。
游戏：Deep Fishing🎣，creator = LazyGames.（id 34744238），playing 6300，visits 10,223,131。

## 新句（revise-log 全部 codes 行）与通读命题

| 编号 | 命题 | 验证路径 | 结果 | 证据 |
|---|---|---|---|---|
| 1 | 游戏描述末句为 "⭐ Like the game, favorite it, and join the group for rewards and updates!" | games?universeIds | CONFIRMED | description 末行逐字一致 |
| 2 | 游戏描述无 code、无兑换步骤 | 同上 | CONFIRMED | 全文无 code/redeem |
| 3 | 奖励内容、领取方式、频率未在描述 / 群 / 活动中给出（"not confirmed"） | games、groups、events | CONFIRMED | 三处均无相关文字 |
| 4 | 群 LazyGames.（带句点），ID 34744238，游戏记录以其为 creator | games、groups | CONFIRMED | creator.name "LazyGames."，id 34744238 |
| 5 | 群描述两行：welcome + "Home of Deep Fishing!"，无 code | groups/34744238 | CONFIRMED | "🔥Welcome to Lazy Games. 💤🎮\n🩵Home of Deep Fishing! 🐟" |
| 6 | 群 shout 为空（字段 null） | 同上 | CONFIRMED | shout: null |
| 7 | 八条活动、九个通行证、98 个商品、13 个徽章 | 各接口 | CONFIRMED | 8 / 9 / 98 / 13；商品 nextPageCursor null，徽章 null，通行证 nextPageToken "" |
| 8 | 五条活动描述是一行通知提醒（Update 6、Toxic、Fish Update、NEW WORLD、EGGS） | virtual-events | CONFIRMED | 5 条均为 "Turn on notifications…" 类 |
| 9 | 活动描述表逐字：Update 3 空；Update 4 "Introducing new features!"；Toxic "notifactios… event!"；Fish Update "…this Event"（无叹号）；EGGS "notifiactions…"；NEW WORLD / Update 6 带叹号 | 同上 | CONFIRMED | 拼写错误与叹号逐字一致 |
| 10 | Mutation Roll + Rarity💫 描述是 26 条项目行、以 "Mutation Reroll 🔄" 开头 | 同上 | CONFIRMED | 重算：5+5+4+4+4+3+1 = 26 |
| 11 | 通行证 9 个，一个描述提到 rewards（VIP） | game-passes | CONFIRMED | VIP "Exclusive VIP perks and rewards! ⭐" |
| 12 | 98 个商品描述字段全空 | developerproducts | CONFIRMED | Description / displayDescription / DisplayDescription 三个字段均全空 |
| 13 | 徽章描述各为玩或捕鱼里程碑 | badges | CONFIRMED | 13 条 "You played / caught …" |
| 14 | 活动表标题（含表情）：Update 3 👀、Update 4 🔥、Mutation Roll + Rarity💫、Update 6 🔥、Toxic + Kraken 🐙☢️、Fish Update + Rework、NEW WORLD IS COMING、EGGS & PETS are COMING! | virtual-events | CONFIRMED | 逐字一致 |
| 15 | 活动字幕与标语也过了词搜 | 同上 | CONFIRMED | 我的搜索含 subtitle、tagline |
| 16 | 命中表：code 0 / redeem 0 / promo 0 / coupon 0 | 六个响应全部字符串值 | CONFIRMED | 另搜 twitter、discord、codes 也为 0 |
| 17 | reward 4 处：游戏描述；VIP 通行证描述；活动描述 "Added Index Rewards"；活动标语 "daily rewards" | 同上 | CONFIRMED | 4 条不同字符串（game 1、gp 1、events 2） |
| 18 | gift 13：12 个商品名（Skip Gift [1]–[3] + 九个 [Gift]）+ 标语 "gifting" | 同上 | CONFIRMED | 重算 3+9+1 = 13；"gifting" 在 Fish Update + Rework 标语 |
| 19 | claim 1：Shop Daily Claimable Ad | 同上 | CONFIRMED | 仅此一条 |
| 20 | free 1：Freeze Fish (One Throw) | 同上 | CONFIRMED | 仅此一条（"Freeze" 内含 free） |
| 21 | 19 处命中分五类：14 商品名（12 gift + 1 claim + 1 free）、游戏描述末句、VIP 描述、一条活动描述、两条活动标语 | 同上 | CONFIRMED | 4+13+1+1 = 19；14+1+1+1+2 = 19 |
| 22 | 命中词表恰为八个词 | 页面自述 | CONFIRMED | code、redeem、promo、coupon、reward、gift、claim、free |
| 23 | "across every text field of the six responses" 无遗漏字符串 | 我对六个响应的全部字符串值（含 host、category）搜同样八词 | CONFIRMED | 全字符串搜结果与字段搜一致（reward 4、gift 13、claim 1、free 1） |
| 24 | NEW WORLD IS COMING 窗口 4–8 October 2026，标语含 "daily rewards" | virtual-events | CONFIRMED | 2026-10-04T16:00Z – 10-08T16:00Z |
| 25 | Shop Daily Claimable Ad 29 Robux，记录创建于 30 September 2026 | developerproducts | CONFIRMED | PriceInRobux 29，Created 2026-09-30T15:27:24 |
| 26 | "that is the only instruction that tells players how to get something for free"（范围：读过的记录） | 全部响应 | UNVERIFIED | 记录里写的是 "rewards"，没有一处写奖励免费；"for free" 是页面的推断，接口响应不含这个词 |
| 27 | 官方社交链接接口对匿名请求返回 401 | games.roblox.com/v1/games/10526853622/social-links/list | CONFIRMED | 401 {"errors":[{"code":9002,"message":"Authentication token is missing"}]} |
| 28 | 本页没有读任何 Discord 服务器 | 页面自述（无外链、sourceUrls 无 discord） | CONFIRMED | sourceUrls 仅六个 Roblox 接口 |
| 29 | 活动接口同几分钟内有时回 8 条、有时只回未结束那 1 条 | 20 次轮询 | CONFIRMED | 见上 |
| 30 | 页面没有写出任何具体的码、没有点名第三方站点、没有「working / active codes」暗示 | 通读正文 | CONFIRMED | 通读无；"third-party sites" 仅泛称、不指名 |
| 31 | 「seven published records」（正文 "a statement about seven published records"） | 表格七行：游戏描述、群描述、shout、活动、通行证、商品、徽章 | UNVERIFIED | 数字取决于怎么数（正文别处说「六个响应」），接口响应不能决定是 6 还是 7；仅作口径不一致记录 |
| 32 | tldr / 正文与表格所列数量一致（8/9/98/13） | 各接口 | CONFIRMED | 同第 7 条 |
| 33 | 标题 / description 月份 "October 2026"、checkedAt 2026-10-10 | 取证日 | CONFIRMED | 我取证日期 2026-10-10 UTC |
| 34 | 价格 / 其它数字：无其它计数类数字 | 通读 | CONFIRMED | 无 |
| 35 | 「当天读到 shout 为空」（How can you check, 第 2 条） | groups | CONFIRMED | null |
| 36 | 站内链接目标 | 机检② | CONFIRMED | 见下 |
| 37 | 外链 | 机检① | CONFIRMED | 正文外链 0 个 |
| 38 | 无日期的 now / currently / upcoming / soon / latest / recently | 机检③ | CONFIRMED | 正文 0 处（"new" 仅在 NEW WORLD 标题与 "brand new" 引文，"still" 在表格说明里，均不是时间副词误用） |
| 39 | 图说 "Promotional art: view from inside a giant pink fish mouth… pier"、署名 "Official thumbnail · LazyGames. (Roblox)" | content/deep-fishing/_images.json art02 | CONFIRMED | alt 与 credit 逐字一致；官方接口无图片内容可核，仅核到留档字段 |
| 40 | 「Whether the game has a code entry box is not confirmed」 | 全部响应无相关文字 | CONFIRMED | 无 code 相关词 |

## 机检
① 正文外链：0 个。frontmatter sourceUrls 六个地址我逐个 curl，全部 200；六个都是 Roblox 官方接口。
② 站内链接：badges、discord、gamepasses、how-to-play、shop、updates（另 related 为 discord、how-to-play、shop）。全部在白名单内，无 waters 或其它。
③ 无日期时间词：0 处。
其它观察（不是事实错误）：正文插图用 art02，而 _images.json 的 pages 把 codes 映射为 art05、frontmatter images 写 art05；updates 同理（正文 art01，frontmatter 与映射 art04）。

## 旧页 diff 结论（index.md、discord.md、beginner.md；git diff --cached HEAD）
- 三页的改动只落在与 codes / 更新说明有关的句子，另有 frontmatter updated 改为 2026-10-10；其余文字未动，reviewed 未改。工作树文件里能 grep 到新句，与 diff 一致。
- index：faq 答案、「What has changed since launch?」首句、整节 H2 改为问句，三处新句与 codes 页终稿说法一致。「八条活动里有一条（Mutation Roll + Rarity💫）的 description 是更新清单」与接口相符（26 行变更清单，其余七条为空或一行提醒 / 一句话）。「every store item and badge carries the date it was created」：98 个商品、13 个徽章均有 Created，成立。
- index 新节列出「game description, the LazyGames. group record, event listings, game passes, store products and badges」，与 codes 页一致。
- discord：新增一句指向 codes 页，并把 "we will add a page" 改成 "it will go on that page"；未改动的原句 "official description and the LazyGames group carry no codes" 与接口相符。
- beginner：卡片句与「不覆盖」一节的新句与 codes 页一致；「fish list 与 waters 页仍没有」说法保留，站内确有 waters.md 文件（beginner 的这句是旧话，不在本轮改动内；若 waters 页同批上线则该句需另核，我没有验）。
- 旧页内本轮没有 REFUTED 项。
