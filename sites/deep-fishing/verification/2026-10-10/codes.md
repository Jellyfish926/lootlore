# codes 页核验（lootwiki.com/deep-fishing/codes/ 草稿）

36 条命题，1 条被推翻，4 条未验（C32–C35）。

取证：全部由核验方 2026-10-10 00:14–00:18 UTC 重新取得，存于 b2/v/（未采信 b2/raw）。URL 简写：G=games.roblox.com/v1/games?universeIds=10526853622；GR=groups.roblox.com/v1/groups/34744238；EV=apis.roblox.com/virtual-events/v1/universes/10526853622/virtual-events；GP=apis.roblox.com/game-passes/v1/universes/10526853622/game-passes?passView=Full&pageSize=100；DP=apis.roblox.com/developer-products/v2/universes/10526853622/developerproducts?limit=100；BD=badges.roblox.com/v1/universes/10526853622/badges?limit=100&sortOrder=Asc。

## EV 轮询结果
共轮询 44 次（间隔约 2 秒，00:14:28–00:17:53，明细 verify/events-poll.log）：最多 8 条，出现 40 次；只有 1 条出现 4 次（第 25–28 次，00:17:04–00:17:12，标题 EGGS & PETS are COMING!，997 字节）。8 条的 40 次响应 MD5 前缀一致（44d50d05）。nextPageCursor 恒为空串。

## 命题表
| 编号 | 命题 | 验证路径 | 结果 | 证据 | 取证时间(UTC) |
|---|---|---|---|---|---|
| C1 | 游戏描述末行逐字为「⭐ Like the game, favorite it, and join the group for rewards and updates!」 | G | CONFIRMED | description 末行与之逐字相同 | 00:14:10 |
| C2 | 开发者是群组 LazyGames.（带句点），ID 34744238，游戏记录把它列为 creator | G | CONFIRMED | creator={"id":34744238,"name":"LazyGames.","type":"Group"} | 00:14:10 |
| C3 | 群描述两行：欢迎 + 「Home of Deep Fishing!」，无码 | GR | CONFIRMED | "🔥Welcome to Lazy Games. 💤🎮\n🩵Home of Deep Fishing! 🐟" | 00:14:11 |
| C4 | 群 shout 为空（字段 null） | GR | CONFIRMED | "shout": null | 00:14:11 |
| C5 | 活动 8 条，标题依次为 Update 3 👀 / Update 4 🔥 / Mutation Roll + Rarity💫 / Update 6 🔥 / Toxic + Kraken 🐙☢️ / Fish Update + Rework / NEW WORLD IS COMING / EGGS & PETS are COMING! | EV | CONFIRMED | 40 次 8 条，标题与顺序逐字一致（含表情、空格） | 00:14:28 |
| C6 | 各条 description：Update 3 空；Update 4「Introducing new features!」；Update 6「Turn on notifications to not miss this Event!」；Toxic「Turn on notifactios to not miss this event!」；Fish Update「Turn on notifications to not miss this Event」（无叹号）；NEW WORLD「…Event!」；EGGS「Turn on notifiactions to not miss this Event!」 | EV | CONFIRMED | 逐条逐字一致（拼写错误 notifactios / notifiactions 均在原文） | 00:14:28 |
| C7 | 8 条里 5 条 description 是一行通知提醒 | EV | CONFIRMED | Update 6、Toxic、Fish Update、NEW WORLD、EGGS 共 5 条 | 00:14:28 |
| C8 | Mutation Roll + Rarity💫 description 为 26 行变更清单，以「Mutation Reroll 🔄」开头 | EV | CONFIRMED | 974 字符，以 "- " 开头的行 26 条，首行 "Mutation Reroll 🔄" | 00:14:28 |
| C9 | 通行证 9 个；VIP 描述含 rewards（"一条描述提到 rewards"） | GP | CONFIRMED | gamePasses 长 9，nextPageToken 空；VIP displayDescription "Exclusive VIP perks and rewards! ⭐"；9 条中仅此一条含 reward | 00:14:13 |
| C10 | 商品 98 个、一页取完、98 条描述字段全空 | DP | CONFIRMED | developerProducts 长 98，ProductId 98 个不重复，无 nextPageCursor；Description / displayDescription / DisplayDescription 非空数均为 0 | 00:14:13 |
| C11 | 徽章 13 个，每条描述是游玩或捕获里程碑 | BD | CONFIRMED | data 长 13，nextPageCursor 空；描述为「You played Deep Fishing!」及 12 条「You caught …」 | 00:14:15 |
| C12 | 检索：code / redeem / promo / coupon 在六个响应全部字符串中均 0 命中 | G GR EV GP DP BD | CONFIRMED | 大小写不敏感子串检索，4 词均 0；另查 twitter / discord / giveaway / bonus / http / x.com / youtube 均 0 | 00:14:40 |
| C13 | reward 4 处：游戏描述、VIP 描述、「Added Index Rewards」、「daily rewards」tagline | 同上 | CONFIRMED | G description；GP[VIP]；EV[2].description；EV[6].tagline，共 4 条不同文本 | 00:14:40 |
| C14 | gift 13 处：12 个商品名（Skip Gift [1]–[3] + 九个 [Gift]）+ 1 条活动 tagline（gifting） | 同上 | CONFIRMED | DP[40..42]、DP[72..80]；EV[5].tagline "…F2P skins, gifting, reworks…" | 00:14:40 |
| C15 | claim 1 处：商品名 Shop Daily Claimable Ad | 同上 | CONFIRMED | 仅 DP[96].Name | 00:14:40 |
| C16 | free 仅出现在商品名 Freeze Fish (One Throw) 的子串里 | 同上 | CONFIRMED | free 命中 DP[71] 三个重复名字段，无其他 | 00:14:40 |
| C17 | 「No code」=无形似码的字符串，也无让玩家输入/兑换的句子 | 同上 | CONFIRMED | 全响应扫描大写字母数字混合 5 位以上词，仅命中 ISO 时间戳；搜 box / enter / type in / input / menu 无命中 | 00:17:50 |
| C18 | 页面「In every hit, though, the word belongs to a product name, a pass perk or an update summary」 | 同上 | REFUTED | 反例：reward 的命中之一是游戏描述末行「join the group for rewards and updates!」，既不是商品名，也不是通行证权益，也不是更新摘要（页面本身下一节单独讲它） | 00:14:40 |
| C19 | 描述末行是所读记录里「唯一一条告诉玩家如何免费拿东西的指示」 | 全部响应 | CONFIRMED | 对 like/favorite/join/follow/claim/collect/get/free/group/daily 等词逐行检索：仅游戏描述末行是对玩家的指示；其余命中为 Rekin Shark 概率、「Complete the Luck boost to get Big Mouth Fish」（更新清单条目，无「免费」字样）、F2P skins/gifting/daily rewards（tagline）、Get better luck!（付费通行证描述）。「免费」的判定带解读成分 | 00:17:00 |
| C20 | NEW WORLD IS COMING 排期 2026-10-04 至 10-08，tagline 含「daily rewards」 | EV | CONFIRMED | startUtc 2026-10-04T16:00:03.218，endUtc 2026-10-08T16:00:03.218；tagline "Deep Fishing expands with a brand new Volcano World, 30 fish, boats, daily rewards, and much more." | 00:14:28 |
| C21 | Mutation Roll + Rarity💫 含「Added Index Rewards」 | EV | CONFIRMED | 清单中 "- Added Index Rewards" | 00:14:28 |
| C22 | Shop Daily Claimable Ad：29 Robux，2026-09-30 创建 | DP | CONFIRMED | PriceInRobux 29，Created 2026-09-30T15:27:24.246Z | 00:14:13 |
| C23 | 群 ID 34744238（正文「its ID is 34744238」） | GR | CONFIRMED | "id": 34744238 | 00:14:11 |
| C24 | 游戏社交链接接口对匿名请求返回认证错误 | games.roblox.com/v1/games/10526853622/social-links/list | CONFIRMED | HTTP 401 {"errors":[{"code":9002,...,"message":"Authentication token is missing"}]}（此地址取自写手声明；任务书允许域名） | 00:14:23 |
| C25 | 活动接口同一时段有时回 8 条、有时只回未结束的 1 条 | EV | CONFIRMED | 44 次轮询：40 次 8 条、4 次 1 条（EGGS & PETS are COMING!，窗口 10-11 至 10-15，截至读取时未开始） | 00:17:12 |
| C26 | 群描述/shout/任何活动列表都没说明入群奖励是什么、怎么领、领几次 | G GR EV | CONFIRMED | 搜 group/join/reward：群记录无；活动文本无相关句 | 00:17:00 |
| C27 | 「no text we read says the game has a code box, and no text says it lacks one」 | 全部响应 | CONFIRMED | code 0 命中；box/enter/menu 0 命中 | 00:17:50 |
| C28 | 九个 [Gift] 商品与九个通行证一一对应 | DP GP | CONFIRMED | [Gift] 名：VIP、Auto Sell、Fish Magnet、Double Coins、Double XP、More Mutations、Ultra Lucky、Super Lucky、Lucky，与 9 个通行证名相同 | 00:14:13 |
| C29 | 正文称活动表「Titles and descriptions are copied as written, spelling included」 | EV | CONFIRMED | 见 C5、C6；标题含「Mutation Roll + Rarity💫」（无空格）一致 | 00:14:28 |
| C30 | 所有日期按 UTC | EV DP GP | CONFIRMED | 接口时间戳均为 Z 或 +00:00 | 00:14:28 |
| C32 | 「Discord 服务器自称官方，公告频道需 Discord 账号」 | — | UNVERIFIED | Discord 不在允许来源内，未取证；Roblox 接口响应里也无任何 Discord 链接（discord 检索 0 命中） | — |
| C33 | 「At least one third-party site lists codes」 | — | UNVERIFIED | 第三方站点被任务书禁止访问，未取证 | — |
| C34 | 「按开发者社交链接登录后可看到开发者自己的帖子」（流程步骤 4） | — | UNVERIFIED | 需登录态，匿名只得 401（C24），未验 | — |
| C35 | 图片 art02 的描述（粉色巨鱼口内、岸边钓手）及「来自 Roblox 体验页的官方宣传图」 | — | UNVERIFIED | 图片不在允许取证范围内，未核 | — |
| C36 | 群 shout「On 10 October 2026 the shout was empty」 | GR | CONFIRMED | 同 C4 | 00:14:11 |
| C37 | 页面未写出任何具体码、未点名第三方站点、无暗示有码措辞（working / active codes） | 草稿全文 | CONFIRMED | 全文检索 working、active：0；除 C33 一句泛指外无站点名、无码字符串 | 00:17:50 |

## 机检
1. 正文外链：0 个（正文只有站内链接和图片 key art02）。sourceUrls 6 个地址 curl 均 200（games、groups、virtual-events、game-passes、developer-products、badges，00:14–00:18 UTC）；正文提到但不是链接的 social-links 接口为 401（匿名）。
2. 站内链接目标：badges、discord、gamepasses、how-to-play、shop、updates，全部在允许 slug 内，没有 waters 或其他。
3. 无日期限定的 now / currently / upcoming / soon / latest / recently：0 处（grep 仅命中 new，位于活动标题与「Introducing new features!」引文内）。
4. 页面日期口径：title / seoTitle 写「October 2026」，checkedAt 2026-10-10，与读取日一致。
