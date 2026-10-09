# legendary-odds 核验

34 条命题，1 条被推翻，4 条未验。（取证窗口 2026-10-09T22:55Z–23:05Z；A 级全验，B 级仅 Irox Games 一条，已验；出现 1 条 REFUTED 后其余按全量处理。）

路径简写：NEWS = `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=3419430&count=100&maxlength=0&feeds=steam_community_announcements`（我取回 63 条，count=100 未满，故已翻完；最早 date 1738588746 = 2025-02-03 13:19Z，最晚 1790869380 = 2026-10-01 15:43Z）；APP = `https://store.steampowered.com/api/appdetails?appids=3419430&l=english`；gid 即公告 gid。数字推导全部用 Python 自己重算。

| 编号 | 命题 | 验证路径 | 结果 | 证据 | 取证时间(UTC) |
|---|---|---|---|---|---|
| L1 | 描述含标题「Item drop pool chances*:」及 Common 90% / Uncommon 9.5% / Rare 0.49% / Epic 0.01% / Legendary - 1 in 500000 / 「*Subject to change」，共五行 | APP about_the_game | CONFIRMED | 原文 HTML：`Item drop pool chances*:` + 五个 li + `*Subject to change` | 22:55Z |
| L2 | 同一段文字在商店页 | https://store.steampowered.com/app/3419430/Bongo_Cat/ | CONFIRMED | 商店页 HTML 同样出现该段，顺序一致 | 23:03Z |
| L3 | 90+9.5+0.49+0.01=100；1÷500000=0.0002% | 重算 | CONFIRMED | 100.0；0.0002 | 23:00Z |
| L4 | 平均箱数 Uncommon 10.5 / Rare 204.1 / Epic 10,000 / Legendary 500,000 | 重算 1/p | CONFIRMED | 10.526 / 204.08 / 10000 / 500000 | 23:00Z |
| L5 | 50%/90% 箱数：7/24、142/469、6,932/23,025、346,574/1,151,292 | 重算 ceil(ln(1-X)/ln(1-p)) | CONFIRMED | 6.94→7, 23.07→24; 141.1→142, 468.8→469; 6931.1→6932, 23024.7→23025; 346573.2→346574, 1151291.4→1151292 | 23:00Z |
| L6 | 1−0.9999^10000≈63.2%；500,000 箱处 Legendary 同为约 63.2% | 重算 | CONFIRMED | 0.63214 / 0.63212 | 23:00Z |
| L7 | 2025-02-23 Steam Next Fest Demo Update 含「10 items of the same rarity can be upgraded to one of a higher tier」 | NEWS gid 1792116353300258 | CONFIRMED | `Adds exchanges (10 items of the same rarity can be upgraded to one of a higher tier)`；date 20:24Z（UTC 日=02-23） | 22:56Z |
| L8 | 隐含前提：该 10 合 1 规则与 30min 计时适用于正式版 | 同上 + 全部 63 条 | UNVERIFIED | 出处公告标题是 Steam Next Fest **Demo** Update（demo 版补丁）；正式版 63 条里没有任何一条重述「10 个」或「30min」（搜 minute/timer/cooldown/10 items 全量无）。成就 Trader「Use the exchange once」只证明正式版有 exchange，不证明比例。正文只在 scope 里说「计时来自 2025 公告」，未说出处是 demo 补丁 | 22:58Z |
| L9 | 隐含前提：兑换只升一档（表中 Uncommon=10、Rare=100、Epic=1000、Legendary=10000 个 Common） | 同 L7 | UNVERIFIED | 原文是「one of a higher tier」，没有写「the next tier」；逐档级联是写手假设。算术本身 CONFIRMED（10/100/1000/10000） | 22:56Z |
| L10 | 只喂 Common：12/112/1,112/11,112；全部折算：5/41/407/4,066；2.46=0.9+0.95+0.49+0.1+0.02 | 重算 | CONFIRMED | ceil(n/0.9)=12,112,1112,11112；ceil(n/2.46)=5,41,407,4066；0.9+0.095×10+0.0049×100+0.0001×1000+10000/500000=2.46 | 23:00Z |
| L11 | 约 25 倍、约 123 倍 | 重算 | CONFIRMED | 10000/407=24.57，10000/406.5=24.6；500000/4066=122.97，/4065=123.0 | 23:00Z |
| L12 | 同公告含「Increase the drop timer to 30min」 | NEWS gid 1792116353300258 | CONFIRMED | `Increase the drop timer to 30min (sorry, but i need to do that to hopefully fix the red cross)` | 22:56Z |
| L13 | 2025-03-18 Bug fixes & Red Cross Fix 含「only shows chest popup if you have 1000 clicks」 | NEWS gid 1794102528240823 | CONFIRMED | 原句逐字一致；date 2025-03-18 16:04Z | 22:56Z |
| L14 | 2026-06-05 Backend Update 帖不提计时 | NEWS gid 1834602721190507 全文通读 | CONFIRMED | 全文无 timer / minute / cooldown / chest | 22:57Z |
| L15 | 63 条里没有任何一条写出不同于 30min 的宝箱计时 | NEWS 全 63 条，正则 minutes?/timer/cooldown/hours?/interval/every \d/seconds? 全量 | CONFIRMED（证伪未成功） | 命中只有：30min 本条、Mar 18 'Shows timer…/Saves the cooldown'、Mar 28 'preset locations for the chest timer'、AFK 2 分钟、demo 5min/1min、auto randomizer 'every X minutes'、May 8 2025 'keep running for 30min'。无另一个宝箱间隔 | 22:58Z |
| L16 | 2026-06-27 帖含「(it costs you 1000 clicks, for your friend it's free)」 | NEWS gid 1836506165556399 | CONFIRMED | 原句逐字一致 | 22:56Z |
| L17 | 点击/小时表：407→407,000/203.5；10,000→10,000,000/5,000；4,066→4,066,000/2,033；500,000→500,000,000/250,000 | 重算 | CONFIRMED | 全部吻合 | 23:00Z |
| L18 | 约 8.5 天、约 85 天、约 28.5 年 | 重算 | CONFIRMED | 203.5/24=8.48；2033/24=84.7；250000/8760=28.54 | 23:00Z |
| L19 | 500,000,000 点是最稀有成就 25 million 的 20 倍；25M 对应最稀有成就 | ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/?gameid=3419430；https://steamcommunity.com/stats/3419430/achievements | CONFIRMED | PET_25M 0.4%（全表最低）；成就页「Bongo Beat Diamond | 25.000.000 bongo beats」；5e8/2.5e7=20 | 22:59Z |
| L20 | 2025-03-02 Release Date Announcement 引文与「30min of playtime in the demo」 | NEWS gid 1792751526108641 | CONFIRMED | `The items will not be available via chests, so there will only be a limited number. They are legendary by definition (because there are only a few of them).` / `You must have 30min of playtime in the demo`；date 2025-03-02 14:59Z | 22:56Z |
| L21 | 2026-09-01 帖引文「These items are not droppable and are claimed through special events like the advent calendar.」 | NEWS gid 1842212951313382 | CONFIRMED | 逐字一致（前文「added a unique rarity.」） | 22:56Z |
| L22 | 季节事件结束后「the items will no longer be dropable」，2025-10-08 Autumn Event | NEWS gid 1813041031167641 | CONFIRMED | `After October 31th the items will no longer be dropable.` | 22:56Z |
| L23 | 秋季事件：uncommon 掉落更可能是事件物品，且「we didn't adjust the overall drop chances」 | 同上 | CONFIRMED | `if you drop an uncommon item it is now higher that the item is an event item, we didn't adjust the overall drop chances.`（同段另有 `The chances to drop event items are also significantly higher than before`） | 22:56Z |
| L24 | 2025-12-01 冬季：「I moved many items to lower rarity tiers so that you will see a wider variety of items!」且是 temporary measure | NEWS gid 1817483467044521 | CONFIRMED | `For this event, I moved many items to lower rarity tiers so that you will see a wider variety of items! … it's only a temporary measure` | 22:56Z |
| L25 | Paw Pass 引文：9-01「cosmetic/emote chests with up to legendary rarity」；10-01「chest with guaranteed rarity up to legendary」 | gid 1842212951313382；1845383656381895 | CONFIRMED | 两句逐字一致 | 22:56Z |
| L26 | 「The Paw Pass works outside the roll」 | 同上两帖 | UNVERIFIED | 两帖只说通行证含带稀有度上限/保底的宝箱，没有任何一句说它绕过或独立于掉率表；「outside the roll」是写手推断 | 22:57Z |
| L27 | 两帖都没列出每种稀有度的箱数 | 同上两帖通读 | CONFIRMED | 无数量 | 22:57Z |
| L28 | tldr：「The developer has published no per-item odds or item counts」 | NEWS gid 1795283637960385；1803527891535449；1813041031167641；1824644522846187；1792116353300258 | REFUTED | 反例：Apr 2025 帖「20 exclusive April Fools' items! There will be 4 for each rarity.」；Summer 2025 帖「20 exclusive summer items! There will be 4 for each rarity.」；Autumn 2025「20 exclusive autumn items! There will be 4 for each rarity.」；2025-02-23「Adds over 50 new items」。官方发布过事件物品数。草稿原句在 tldr 第 4 条（正文用的是「how many copies of any item exist」，那一句无误） | 22:58Z |
| L29 | 开发商没公布任何物品的存世份数 | NEWS 63 条通读相关句 | CONFIRMED | 仅「only a limited number」「only a few of them」，无数字 | 22:58Z |
| L30 | 公告接口 63 条，2025-02-03 至 2026-10-01 | NEWS | CONFIRMED | count=63，见上方 date 范围 | 22:55Z |
| L31 | 开发商 Irox Games（B 级） | APP developers | CONFIRMED | `['Irox Games']` | 22:55Z |
| L32 | 「the game slots duplicates and skips favourites」 | NEWS gid 1795283637857596；1797185861746045 | CONFIRMED | 03-28「Auto slot all duplicates for quicker exchanges」；04-20「Favorites get ignored in the auto exchange」 | 22:58Z |
| L33 | 公告没说明兑换产出的物品怎么选 | NEWS 全 63 条 exchange 命中行 | CONFIRMED | 所有 exchange 命中行均为修 bug/UI/事件提示，无产出规则 | 22:58Z |
| L34 | 「On October 10, 2026 we read…」（正文、tldr、checkedAt 均为 10-10） | 写手 raw 时间戳 2026-10-09T22:45:58Z；我的取证 10-09 22:55Z | UNVERIFIED | 页面未写时区；UTC 日期是 10-09，10-10 只在 UTC+8 成立；与公告日期口径（UTC）不一致，读者无法核对 | 22:55Z |

另：L35「剩余 0.0002% 不会移动任何数字」按重算：Epic 平均箱数相对变化约 2e-6，CONFIRMED（不单列计数）。

## 三项机检
① 外链 11 个，全部 200，全部在 sourceUrls 内，sourceUrls 无多余：appdetails、store 页、公告 gid 1792116353300258 / 1792751526108641 / 1794102528240823 / 1813041031167641 / 1817483467044521 / 1834602721190507 / 1836506165556399 / 1842212951313382 / 1845383656381895（23:00Z 经 curl -L）。
② 站内链接：achievements、events、exchange-trading、hats-skins、how-to-play、paw-pass，均在名单内；无 market-prices。
③ 时效词（now/currently/upcoming/soon/latest/recently）：正文 0 处。

## 其他事实（非命题，供处理）
- 2025-10-02/10-06 公告新增「第二个宝箱，只出 emote」，并「split up the drop pool for hats/skins and emojis」（gid 1811772772484130、1811772772604122）。正文「每箱 1 件」「30 分钟一箱」的假设没有提这个第二宝箱，其计时与掉率公告未写。
- 公告原文 gid 1792116353300258 的 date 是 2025-02-23 20:24Z，北京时间已是 02-24；正文用 UTC 日，一致。
