# free-items 核验

38 条命题，1 条被推翻，4 条未验。（取证窗口 2026-10-09T22:55Z–23:08Z；A 级全验；B 级 P26（events 页内容）未验、P27（未检查渠道声明）为作者自述无需验；P25 全称否定句按任务书重点证伪，结果见 F10。）

路径简写：NEWS = `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=3419430&count=100&maxlength=0&feeds=steam_community_announcements`（63 条，count=100 未满，已翻完）；APP = `https://store.steampowered.com/api/appdetails?appids=3419430&l=english`；STORE = `https://store.steampowered.com/itemstore/3419430/?cc=us&l=english`。除 F10/F27 外，引文均对 NEWS 的 contents 字段做子串匹配。

| 编号 | 命题 | 验证路径 | 结果 | 证据 | 取证时间(UTC) |
|---|---|---|---|---|---|
| F1 | is_free: true | APP | CONFIRMED | `is_free: True` | 22:55Z |
| F2 | 63 条公告，2025-02-03 至 2026-10-01 | NEWS | CONFIRMED | 63 条；最早 1738588746、最晚 1790869380（UTC） | 22:55Z |
| F3 | Chests：「only shows chest popup if you have 1000 clicks」，Bug fixes & Red Cross Fix，2025-03-18 | gid 1794102528240823 | CONFIRMED | 逐字一致；date 2025-03-18 16:04Z | 22:56Z |
| F4 | Exchange：「10 items of the same rarity can be upgraded to one of a higher tier」，2025-02-23 | gid 1792116353300258 | CONFIRMED | 逐字一致（引文正确） | 22:56Z |
| F5 | 隐含前提：10 合 1 在正式版成立（表中 Exchange 一行当作日常玩法） | NEWS 全 63 条 | UNVERIFIED | 该句出自 Steam Next Fest **Demo** Update；正式版公告只证明 exchange 存在，没有重述比例（见 legendary-odds L8） | 22:58Z |
| F6 | Free Paw Pass lane：「To automatically claim your free pass ticket, open Bongo Cat at least once a month.」，2026-09-01 | gid 1842212951313382 | CONFIRMED | 逐字一致 | 22:56Z |
| F7 | Fruit Fusion Sets：草莓/菠萝/西瓜三选一；至少一名其他玩家的联机会话；「can only be obtained by playing multiplayer, and you can only drop one of the item sets」，2025-08-11 | gid 1807332909696878 | CONFIRMED | 原文 `at least one other player`、`team Strawberry, Pineapple, or Watermelon`、引句逐字一致 | 22:56Z |
| F8 | 100 万点：「a special skin and hat for everyone who reaches 1 million clicks」，2026-02-05 | gid 1823825466497567 | CONFIRMED | 逐字一致（同句后有「edited back down from 5M」） | 22:56Z |
| F9 | 点击成就：「Not all achievements will give you new cosmetics, but the new tap amount ones will.」，2026-03-05 | gid 1826362059921578 | CONFIRMED | 逐字一致 | 22:56Z |
| F10 | **P25** 表 1 的 6 个来源，没有后续公告宣布停掉 | NEWS 全 63 条：①发布日之后所有 no longer / disabled / removed / ended / stop / discontinu / cannot 命中行逐条读；②chest / clicks / tap / pass 命中行逐条读；③exchange 命中行逐条读；④通读 2026-06-05、06-27、09-01、10-01、02-16、04-13、01-14 七帖全文；⑤STORE 与讨论区置顶帖 | CONFIRMED（证伪未成功） | 找到的相关后续变更全不构成停止：2025-10-02「removing Emojis from the drop pool … chests and exchanges will only contain skins + hats again」（改池子）；2025-10-06 新增第二个 emote 宝箱；2025-10-08 emoji exchange；2026-06-16「Fixes exchange bugs」；2026-06-27/07-12 可替好友开箱「costs you 1000 clicks」；2026-09-01/10-01 Paw Pass 仍在发。唯一的「disable」是 06-27 的 incentivized rewards（Nightwater 联动、wishlist 奖励），不在表 1 的 6 个来源内。该否定句成立范围：公告接口 63 条，不含游戏内与 Discord | 22:58–23:05Z |
| F11 | DEMO RELEASE 2025-02-03：Gamer hat；「play the demo, then play the full game once after launch」 | gid 1790214123211282 | CONFIRMED | `The Gamer hat`；`You get this item by playing the demo and once the full game launches, play it once` | 22:56Z |
| F12 | Release Date Announcement 2025-03-02：「two exclusive items」不经宝箱；30min demo | gid 1792751526108641 | CONFIRMED | 逐字一致（date 14:59Z） | 22:56Z |
| F13 | OKU 2025-06-08：「2 free items」「follow the steps in the game」 | gid 1801617199494974 | CONFIRMED | 逐字一致 | 22:56Z |
| F14 | Let Them Trade 2025-07-18：「these two cute items」、demo 5min | gid 1805431065363728 | CONFIRMED | 逐字一致 | 22:56Z |
| F15 | Paddle 2025-07-25：「this amazing paddle skin」、看商店页后点「the present in the Bongo Cat Collection」 | gid 1806064758642714 | CONFIRMED | 逐字一致 | 22:56Z |
| F16 | Tap Tap Loot 2026-02-21：「this cute skin and some glasses」、demo 1min | gid 1825093633190320 | CONFIRMED | `(you have to play for 1min), you will get this cute skin and some glasses` | 22:56Z |
| F17 | 四篇联动帖没有印出截止日期 | 上述四帖全文通读 | CONFIRMED | 四帖全文无任何日期/until/end | 22:58Z |
| F18 | 两个 demo 行「depended on playing the demo before the full game launched on March 5, 2025」；完整版 2025-03-05 | APP release_date；gid 1790214123211282、1792751526108641、1793384379332669 | UNVERIFIED | 发行日 Mar 5, 2025 CONFIRMED；但「必须在发行前玩 demo」没有任何一帖明说。Gamer hat 帖写的是玩 demo 且发行后再玩一次；Mar 2 帖只说「everyone who played the demo」；Mar 5 帖说「(if you have 30mins of playtime in the demo)」，无截止 | 22:58Z |
| F19 | 小标题「Which free giveaways have already ended?」与 tldr「Demo and collaboration giveaways … were time-limited」，对 OKU / Let Them Trade / Paddle³ / Tap Tap Loot 四项 | F13–F17 | UNVERIFIED | 四帖没有一帖写「ended」或限期（F17）；仅 06-27 帖泛称 incentivized rewards 被关/迁移，没点名这四项。Indie Demos 两轮确有截止（11-30、06-12），但那两轮是 events 页内容 | 22:58Z |
| F20 | 「The developer disabled wishlist and demo rewards on June 27, 2026」/ 标题「wishlist and demo rewards stop」 | gid 1836506165556399 | UNVERIFIED | 原句是「disable the incentivized rewards (f.e. collab with Nightwater or the wishlist ones)」，没有「demo」一词；「demo」来自 06-16 帖 Nightwater 奖励是玩 demo 5min 的推断；「June 27」是发帖日，不是关闭日 | 22:57Z |
| F21 | 06-27 引文整句；理由 Steam Guidelines | gid 1836506165556399 | CONFIRMED | `We had to disable the incentivized rewards (f.e. collab with Nightwater or the wishlist ones) and moved them to owning the full game or removed them entirely, because it was against Steam Guidelines to incentivize this, sorry for that.` 逐字一致 | 22:56Z |
| F22 | 06-16 Summer Event：「the Nightwater Backpack for wishlisting the game」「the Nightwater Cat for playing the demo for 5min」 | gid 1835236783574334 | CONFIRMED | 逐字一致 | 22:56Z |
| F23 | 09-18 Nightwater：拿到游戏送四件；这是购买赠品 | gid 1844115010495136；appdetails?appids=3983860&cc=us | CONFIRMED | `Getting the game will also grant you these four Bongo Cat items`；Nightwater is_free False，$14.99，Sep 18, 2026 | 22:57Z |
| F24 | 公告没说 2025 联动赠品哪些迁移/哪些取消 | gid 1836506165556399 全文 | CONFIRMED | 无逐件说明 | 22:57Z |
| F25 | 搜索统计：code(s) 6 次/5 帖（5 次联机房间码、1 次程序代码） | NEWS 63 条 title+contents，\bcodes?\b | CONFIRMED | 6 次：1809235871549290×2（lobby code generation）、1823825466497567（copy lobby code）、1829528821315214（Friends/Lobby Code）、1835236783574334（Persistent lobby codes）、1834602721190507（'write WAAAAY less code'） | 22:57Z |
| F26 | redeem 2 次/1 帖（Paw Pass Ticket）；promo 1 次（promotional discounts）；coupon、voucher、giveaway、police 均 0 | 同上 | CONFIRMED | redeem×2 均在 1842212951313382（'redeem it in-game'、'redeem Paw Pass rewards'）；promo×1 在 1829528821315214；其余 0 | 22:57Z |
| F27 | 商店描述里 code、redeem、promo、coupon 等为 0（B→A，全验） | APP about_the_game / detailed_description / short_description | CONFIRMED | 四词在三个字段均 0 | 22:55Z |
| F28 | 「no redeem-code system … Nothing describes a place to type a code or a code that grants an item」；房间码不发物品 | NEWS 63 条；另扩搜 key / secret / cheat / password / activat / serial / "enter a/the/your" / "type in/the" | CONFIRMED（证伪未成功） | 扩搜命中：F-Keys（键盘键）、transparency key color、'Activate' 仅 10-01 帖的通行证选择；无输入码兑换处。讨论区置顶帖 FAQ（带 developer 标，Spiced Pigeon）内无兑换码 | 22:57–23:06Z |
| F29 | 2025-12-01 Winter：free Advent calendar「will be available until December 31st, which means you can also open doors from the past」；Deluxe Calendar 购买 | gid 1817483467044521 | CONFIRMED | 逐字一致；`If you purchase the Deluxe Calendar (until December 31st)` | 22:56Z |
| F30 | 2025-11-17 首个 Indie Demos：「After that you can't get them anymore.」「(so Steam syncs your playtime)」「Don't forget to update your game!」 | gid 1816307528971434 | CONFIRMED | 逐字一致；截止 30 November | 22:56Z |
| F31 | 2025-11-10 Animal Shelter：「we will re-enable ALL items for trading with friends, so gift your duplicats to your friends!」；其后无关闭好友交易的帖子 | gid 1815580768395840；NEWS 里 trad* / gift 全量命中行 | CONFIRMED | 引文逐字一致；11-10 之后 trad* 命中只有 emoji exchange / Paw Pass 礼物，无关闭 | 22:58Z |
| F32 | 06-27「(it costs you 1000 clicks, for your friend it's free)」；09-01 通行证券「by using Steam's trading feature」 | gid 1836506165556399；1842212951313382 | CONFIRMED | 逐字一致 | 22:56Z |
| F33 | Item Store：Paw Pass Token $4.99，其余展示的商品都是 $2.50 | STORE | CONFIRMED | 17 个标价条目：2 条 Paw Pass Token $4.99 + 15 条 $2.50（Bumble Kitten、Meowxolotl、Sea Purrtle、Migrating Currents、Pollinating Breeze、Regenerating Bloom、Wrestler Cutie Punch、Yin、Yang、Spooky Skeleton、Hades 等，含重复展示） | 22:57Z |
| F34 | 公告称「Paw Pass Ticket」，Token 与 Ticket 是否同一件 not confirmed | gid 1842212951313382；STORE detail/992 | CONFIRMED（命名事实） | 公告原文「get the Paw Pass Ticket in the Steam Store」；公告里的商店链接 itemstore/3419430/detail/992/（锚文本「Paw Pass」）打开后标题是「Paw Pass Token」，$4.99。即公告自己链到的就是 Token 页（此条比草稿的「not confirmed」更强） | 22:57Z |
| F35 | 「Four things carry a price in the official text: supporter items, the DLC packs, the premium Paw Pass lane and the Deluxe Calendar that the Winter Event post offered」 | gid 1824644522846187；1815580768395840；1829528821315214 | REFUTED | 封闭式「Four」被官方文本反驳：02-16 帖「If you purchase the "Lunar New Year Deluxe" (until March 16th)」是另一份付费日历（草稿正文只点名 Winter 那份，tldr 写「Deluxe calendars」复数）；04-13 帖「Everyone who buys Tap Tap Loot will also receive 4 exclusive items」「Collection Bundle」等是另外标价的东西。定位：草稿「What is not free in Bongo Cat?」首句 | 22:58Z |
| F36 | 「The free pass lane is the only source here with a calendar condition」 | F3–F9 对应帖 | CONFIRMED | 其余 5 个来源在所引帖里都没有按月/日期的条件 | 22:58Z |
| F37 | 「Chests mostly pay out Commons」 | APP | CONFIRMED | Common - 90% | 22:55Z |
| F38 | 日期/标题标注：F3–F16、F21–F23、F29–F32 所有链接 gid 与草稿所写标题、日期（UTC 日）逐一对应 | NEWS title/date | CONFIRMED | 逐条核对，无错位；Free Halloween Treat 10-30（09:23Z）正确 | 22:57Z |

另：「October 10, 2026」写法与 legendary-odds L34 同问题：UTC 为 10-09，页面未标时区（不单列计数）。

## 三项机检
① 外链 20 个，全部 200，全部在 sourceUrls 内，sourceUrls 无多余（23:00Z curl -L）：appdetails、itemstore、公告 gid 1790214123211282 / 1792116353300258 / 1792751526108641 / 1794102528240823 / 1801617199494974 / 1805431065363728 / 1806064758642714 / 1807332909696878 / 1815580768395840 / 1816307528971434 / 1817483467044521 / 1823825466497567 / 1825093633190320 / 1826362059921578 / 1835236783574334 / 1836506165556399 / 1842212951313382 / 1844115010495136。
② 站内链接：events、exchange-trading、hats-skins、how-to-play、legendary-odds、multiplayer、paw-pass，均在名单内；无 market-prices。
③ 时效词：正文 0 处。

## 其他事实（非命题，供处理）
- 表 1「免费来源」漏列：2025-04-20 Collections Update（gid 1797185861746045）写「Special items for people who joined the Discord and Followed the game on Steam」，2025-05-08（gid 1799088287826807）「Follow reward should work more consistently now」。这是官方公告里的免费来源，草稿全文未出现；该奖励是否属 06-27 被关的 incentivized rewards，公告未写。
- 好友交易行：2026-09-01 通行证券「Steam's trading feature」礼物与 2025-11-10 好友交易，均有原文，无冲突。
