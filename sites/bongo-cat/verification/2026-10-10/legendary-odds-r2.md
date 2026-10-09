# legendary-odds 第二轮核验（终稿 /home/claude/lootlore/content/bongo-cat/en/legendary-odds.md）

35 条命题，0 条被推翻，1 条未验。

取证时间（UTC）：2026-10-09 23:18–23:26。路径缩写：FEED = https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=3419430&count=200&maxlength=0&feeds=steam_community_announcements（取回 63 条，全文，自行重取，未用 raw/）；N(gid) = https://store.steampowered.com/news/app/3419430/view/<gid>；APP = https://store.steampowered.com/api/appdetails?appids=3419430&l=english；ACH = https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/?gameid=3419430 与 https://steamcommunity.com/stats/3419430/achievements 。公告日期为 FEED 的 UTC 时间戳换算。算术全部用 Python 重算。

| 编号 | 命题（终稿原句要点） | 验证路径 | 结果 | 证据 | 取证时间 |
|---|---|---|---|---|---|
| R1 | description / 首段 / tldr1：Epic 0.01%，Legendary 1 in 500000，列在 "Item drop pool chances"，注 "Subject to change" | APP + https://store.steampowered.com/app/3419430/Bongo_Cat/ | CONFIRMED | `<h2>Item drop pool chances*:</h2>` 下五行 Common - 90% / Uncommon - 9.5% / Rare - 0.49% / Epic - 0.01% / Legendary - 1 in 500000；`*Subject to change`；商店页 HTML 同样含 "Legendary - 1 in 500000" 与 "Subject to change" | 23:18 |
| R2 | 「it prints five lines, the last two being Epic - 0.01% and Legendary - 1 in 500000」 | APP | CONFIRMED | 五个 `<li>`，末两行即此 | 23:18 |
| R3 | 四条百分比 90+9.5+0.49+0.01 恰为 100%；1÷500,000=0.0002% | APP | CONFIRMED | 90+9.5+0.49+0.01=100；1/500000=0.0002% | 23:18 |
| R4 | 平均 10,000 箱/Epic、500,000 箱/Legendary；50% 概率 Epic 需 6,932 箱 | Python 重算 | CONFIRMED | 1/0.0001=10000；ceil(ln0.5/ln(1-0.0001))=6932 | 23:20 |
| R5 | 表：Uncommon 10.5/7/24；Rare 204.1/142/469；Epic 10,000/6,932/23,025；Legendary 500,000/346,574/1,151,292 | Python 重算 | CONFIRMED | 重算值逐格一致 | 23:20 |
| R6 | 10,000 箱后至少见 1 个 Epic 的概率约 63.2%；Legendary 同点在 500,000 箱 | Python 重算 | CONFIRMED | 1-0.9999^10000=0.63214；1-(1-2e-6)^500000=0.63212 | 23:20 |
| R7 | 出处限定：「Feb 23, 2025 Steam Next Fest Demo Update」含 "10 items of the same rarity can be upgraded to one of a higher tier" | N(1792116353300258) via FEED | CONFIRMED | 标题 "Steam Next Fest Demo Update"，2025-02-23 20:24Z；原文 "Adds exchanges (10 items of the same rarity can be upgraded to one of a higher tier)" | 23:19 |
| R8 | 「That post patched the demo, before the full release of March 5, 2025」 | N(1792116353300258)；N(1793384379332669) | CONFIRMED | 原文 "Steam Next Fest will start tomorrow… one final push for the demo"；发行贴 "Bongo Cat is out meow!!!" 2025-03-05 08:00Z "The full version of the game is finally here" | 23:19 |
| R9 | 「none of the 63 announcements restates the 10-item figure for the full release」 | FEED 全文检索 `\b10 (items|of)|ten items|upgrad` | CONFIRMED | 全部 63 条中仅 2025-02-23 一条命中，其余 0 | 23:21 |
| R10 | 「The quote also says 'one of a higher tier', not the next tier」 | N(1792116353300258) | CONFIRMED | 原文确为 "one of a higher tier"，无 next/下一档字样 | 23:19 |
| R11 | 级联表：Common 折算 12/112/1,112/11,112；全部上交 5/41/407/4,066；2.46 = 0.9+0.95+0.49+0.1+0.02 | Python 重算 | CONFIRMED | ceil(10/0.9)=12，ceil(100/0.9)=112，ceil(1000/0.9)=1112，ceil(10000/0.9)=11112；权重和 2.46；ceil(10/2.46)=5，ceil(100/2.46)=41，ceil(1000/2.46)=407，ceil(10000/2.46)=4066 | 23:20 |
| R12 | 「about 407 vs 10,000 (roughly 25 times fewer)；4,066 vs 500,000 (roughly 123 times fewer)」 | Python 重算 | CONFIRMED | 10000/407=24.57；500000/4066=122.97 | 23:20 |
| R13 | 「the game slots duplicates and skips favourites」 | N(1795283637857596)；N(1797185861746045) | CONFIRMED | 2025-03-28 "Auto slot all duplicates for quicker exchanges"；2025-04-20 "Favorites get ignored in the auto exchange" | 23:19 |
| R14 | 「announcements we read do not say how the item you receive from an exchange is chosen」 | FEED 检索 random/pick/which item | CONFIRMED | 63 条中无任何讲换回物品如何选取的句子（命中的 random/pick 均与 Cat Randomizer、Halloween 选择、大厅有关） | 23:21 |
| R15 | 「Increase the drop timer to 30min」（Feb 23, 2025 demo update） | N(1792116353300258) | CONFIRMED | 原文 "Increase the drop timer to 30min (sorry, but i need to do that to hopefully fix the red cross)" | 23:19 |
| R16 | Mar 18, 2025 notes：game "only shows chest popup if you have 1000 clicks"；标题 Bug fixes & Red Cross Fix | N(1794102528240823) | CONFIRMED | 原文 "only shows chest popup if you have 1000 clicks"；2025-03-18 16:04Z | 23:19 |
| R17 | 「no announcement from March 5, 2025 onward restates [the timer] length」「none of the 63 states a different length」 | FEED 检索 timer / 30 ?min | CONFIRMED | "timer" 仅在 02-23、03-18（缩短/保存冷却、"timer desynced"）、03-28（"3 preset locations for the chest timer"）、2026-04-20（AFK timer），均无时长；"30min" 另见 2025-05-08 Steam Error Fix（"keep Bongo Cat running for 30min until it will work normally again"，非掉落计时器长度，记录备查） | 23:21 |
| R18 | 「June 5, 2026 post on the backend update does not mention the timer」 | N(1834602721190507) | CONFIRMED | 全文（1160 字符）无 timer / 30min / cooldown；标题 "Backend Update, UI Rework, Upcoming Event"，2026-06-05 12:19Z | 23:19 |
| R19 | 「the post of June 27, 2026 says opening a friend's chest 'costs you 1000 clicks'」 | N(1836506165556399) | CONFIRMED | "You can open up your friends chests now (it costs you 1000 clicks, for your friend it's free)"；2026-06-27 12:30Z | 23:19 |
| R20 | 时长表：203.5 / 5,000 / 2,033 / 250,000 小时；约 8.5 天、85 天；约 28.5 年 | Python 重算 | CONFIRMED | 407×0.5=203.5；4066×0.5=2033；203.5/24=8.48；2033/24=84.7；250000/8760=28.54；对应 taps 407,000 / 10,000,000 / 4,066,000 / 500,000,000 | 23:20 |
| R21 | 「Emojis 2.0, and a sorry. of October 2, 2025 announced a chest that 'will ONLY contain emotes'」 | N(1811772772484130) | CONFIRMED | 2025-10-02 09:39Z；原文 "We introduce a SECOND chest which will ONLY contain emotes that will show up once you are in a multiplayer lobby" | 23:19 |
| R22 | 「Emote 2.0 and bug fixes of October 6, 2025 added it」 | N(1811772772604122) | CONFIRMED | 2025-10-06 11:43Z；"Adds a second chest, just for emojis" | 23:19 |
| R23 | 「Its timer and odds are not in the announcements」 | FEED 检索 emote chest / emoji chest 相关贴 | CONFIRMED | 10-01、10-02、10-06、10-08（emoji exchange）及 2026-10-01 贴均无该箱计时或概率 | 23:21 |
| R24 | 「500,000,000 taps are 20 times the 25 million behind the rarest achievement」 | ACH | CONFIRMED | PET_25M 全球 0.4%（28 个成就中最低）；成就页 "Bongo Beat Diamond — 25.000.000 bongo beats. You did it."；500M/25M=20 | 23:22 |
| R25 | 「Irox Games has not published how many copies of any item exist」（正文，未加「in the sources we read」限定） | FEED + APP 检索 | UNVERIFIED | 63 条公告与商店描述中确无「副本数量」，但该句主语是 Irox Games，范围是「任何地方是否发布过」；开发者 Discord、讨论区未读（页末自己写明未读 Discord）。tldr4 的写法带了「in the sources we read」，正文这句没带 | 23:21 |
| R26 | 「the [April Event], [Summer Event] and Autumn Event posts of 2025 each announce 20 exclusive items with '4 for each rarity'」；tldr4 同 | N(1795283637960385)；N(1803527891535449)；N(1813041031167641) | CONFIRMED | 2025-03-31 "20 exclusive April Fools' items! There will be 4 for each rarity"；2025-06-27 "20 exclusive summer items! There will be 4 for each rarity"；2025-10-08 "20 exclusive autumn items! There will be 4 for each rarity" | 23:19 |
| R27 | Mar 2, 2025 引文："The items will not be available via chests, so there will only be a limited number. They are legendary by definition (because there are only a few of them)." 及「Players needed 30min of playtime in the demo」 | N(1792751526108641) | CONFIRMED | 2025-03-02 14:59Z；两句逐字一致；"You must have 30min of playtime in the demo to be eligible for the drop." | 23:19 |
| R28 | Unique 引文："These items are not droppable and are claimed through special events like the advent calendar."，Sept 1, 2026 | N(1842212951313382) | CONFIRMED | 2026-09-01 13:17Z；原文 "added a unique rarity. These items are not droppable and are claimed through special events like the advent calendar." | 23:19 |
| R29 | 活动道具 "the items will no longer be dropable"，Autumn Event post, October 8, 2025 | N(1813041031167641) | CONFIRMED | 2025-10-08 08:03Z；"After October 31th the items will no longer be dropable." | 23:19 |
| R30 | 2025 秋季："we didn't adjust the overall drop chances"，且 uncommon 掉落更可能是活动道具 | N(1813041031167641) | CONFIRMED | 原文 "if you drop an uncommon item it is now higher that the item is an event item, we didn't adjust the overall drop chances" | 23:19 |
| R31 | 2025 冬季："I moved many items to lower rarity tiers so that you will see a wider variety of items!"，同贴称 temporary measure | N(1817483467044521) | CONFIRMED | 2025-12-01；"it's only a temporary measure while I think about future events" | 23:19 |
| R32 | Sept 1, 2026 帖："cosmetic/emote chests with up to legendary rarity"；Oct 1, 2026 帖："chest with guaranteed rarity up to legendary" | N(1842212951313382)；N(1845383656381895) | CONFIRMED | 前者原文 "themed skins, hats, emotes, and cosmetic/emote chests with up to legendary rarity"；后者 "as well as chest with guaranteed rarity up to legendary"（2026-10-01 15:43Z） | 23:19 |
| R33 | 「Neither post says how those chests relate to the store page's drop chances or how many chests of each rarity a pass holds」 | 同上两贴全文 | CONFIRMED | 两贴均无箱数、无与商店概率的关系说明 | 23:19 |
| R34 | 正文/scope/tldr 的读取日统一为 October 9, 2026，scope 写明 UTC；checkedAt 2026-10-09 | 终稿文本 + `date -u` | CONFIRMED | 全文 "October 9" 6 处，无 "October 10"；scope 含 "(dates on this page are UTC)"；本次取证时 UTC 日期为 2026-10-09 | 23:24 |
| R35 | tldr / description / 首段 / 正文自洽：tldr3 的「10-for-1 applies / exactly one tier」假设、正文「On paper, yes, if two assumptions hold」、scope「not restated for the full release」互相一致 | 通读 | CONFIRMED | 未发现 tldr、description、首段、正文互相矛盾之处；各处对 10 合 1 与 30 分钟均带「Feb 23, 2025 demo update」出处限定 | 23:24 |

## 机检

① 外链：正文 15 个外链 + sourceUrls 15 条，逐个 `curl -L`：全部 200；正文外链全部在 sourceUrls 内，sourceUrls 无未用项。所有 gid 均在 FEED 的 63 条里存在。读者可见的 "Steam app details API" 链接仍指向 appdetails JSON（sourceUrls 内有）。
② 站内链接：hats-skins、exchange-trading、how-to-play、achievements、events、paw-pass，均在允许 slug 内；无 market-prices。
③ 时效词：正文无 now / currently / upcoming / soon / latest / recently。
另记：frontmatter `date` / `updated` / `reviewed` 为 2026-10-10，而 checkedAt 与读取日为 2026-10-09（UTC）；取证时 UTC 日期仍是 2026-10-09。
