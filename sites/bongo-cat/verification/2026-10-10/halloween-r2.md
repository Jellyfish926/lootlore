# halloween 第二轮核验（终稿 /home/claude/lootlore/content/bongo-cat/en/halloween.md）+ paw-pass diff

32 条命题，0 条被推翻，0 条未验。取证自行重取：公告 feed（63 条，最新 2026-10-01 15:43Z）、道具商店三页（含 ajaxgetitemdefs 全 37 条）、取证时间 2026-10-09 23:18-23:22Z。

| 编号 | 命题（终稿原句） | 验证路径 | 结果 | 证据 | 取证时间 |
|---|---|---|---|---|---|
| H1 | 读取日统一 October 9, 2026，scope 写明 UTC：scope「as read on October 9, 2026 (dates on this page are UTC)」、checkedAt 2026-10-09、tldr/正文/表头「as of October 9」 | 全文 grep | CONFIRMED | 全文无 October 10 残留（frontmatter date/updated/reviewed 为 2026-10-10，是发布字段，非读取日） | 2026-10-09 23:18-23:22Z |
| H2 | 2026 Halloween 内容是 Paw Pass: Halloween Edition，10 月 1 日公告，帖中不点名单件物品 | https://store.steampowered.com/news/app/3419430/view/1845383656381895 | CONFIRMED | 小节「Paw Pass: Halloween Edition」；只写「all sorts of skins, hats, emotes…」；无物品名 | 2026-10-09 23:18-23:22Z |
| H3 | 「free lane、premium lane、no-deadline」出处写成 Sept 1 launch post（首段、tldr2、表格 Cost 行、正文） | https://store.steampowered.com/news/app/3419430/view/1842212951313382 | CONFIRMED | 「The pass also drops Bongo Coins in both lanes, free and premium」「There is also a paid version of the pass」「rewards are claimable forever and do not have a deadline」。10 月 1 日帖不含 free/premium/deadline 字样 | 2026-10-09 23:18-23:22Z |
| H4 | tldr2 引语 "do not have a deadline" | 同上 | CONFIRMED | 原文「…claimable forever and do not have a deadline」 | 2026-10-09 23:18-23:22Z |
| H5 | 首段/正文：Oct 1 帖「does not restate them」（lane 规则） | https://store.steampowered.com/news/app/3419430/view/1845383656381895 | CONFIRMED | 全帖无 free/premium/ticket/月度领取描述 | 2026-10-09 23:18-23:22Z |
| H6 | "This month's theme is Halloween"；"you will be able to get all sorts of skins, hats, emotes, as well as chest with guaranteed rarity up to legendary" | 同上 | CONFIRMED | 原文（去掉 [b] 标记）逐字一致 | 2026-10-09 23:18-23:22Z |
| H7 | 「up to legendary」只引原文、不做解读；「it does not explain what "guaranteed" covers」 | 同上 | CONFIRMED | 终稿第 33、44 行均为直接引文，无「Legendary 物品」类解读；原帖未解释 guaranteed | 2026-10-09 23:18-23:22Z |
| H8 | 通行证奖励名：终稿未出现公告没列的通行证奖励名 | 全文读 + 公告全文 | CONFIRMED | 全文无任何通行证单品名；Spooky Skeleton 明确写为商店付费品、「no official text we read ties it to the pass」 | 2026-10-09 23:18-23:22Z |
| H9 | "this month's pass will also include 3 UI themes"；"The Paw Pass also includes three UI themes this month"；"Later this month, they will be added to drop in the emote chest" | 同上 | CONFIRMED | 原文一致（emote chest 在原文为 **加粗**） | 2026-10-09 23:18-23:22Z |
| H10 | 「choose one of three UI themes in October」 | 同上 | CONFIRMED | 「this month you can choose between one of 3 new UI Themes」 | 2026-10-09 23:18-23:22Z |
| H11 | UI 主题在 Inventory tab 的 UI Themes 子页 | 同上 | CONFIRMED | 「Inventory tab, under the UI Themes subtab」 | 2026-10-09 23:18-23:22Z |
| H12 | 帖标题 UI THEMES are here! | feed | CONFIRMED | title 一致 | 2026-10-09 23:18-23:22Z |
| H13 | Paw Pass Token 商店标价 US$4.99、描述原文、Tradable、「will not be tradable for one week」 | https://store.steampowered.com/itemstore/3419430/detail/992/ | CONFIRMED | 「Redeem in-game to unlock the premium lane of one Paw Pass. You will be able to access all items from the premium lane when completing the milestones. The redeemed pass will never expire.」$4.99；Tags: Tradable；「will not be tradable for one week」 | 2026-10-09 23:18-23:22Z |
| H14 | 公告称 Paw Pass Ticket，商店标题 Paw Pass Token | Sept 1 帖 + detail/992 | CONFIRMED | 帖：「get the Paw Pass Ticket in the Steam Store」，链接即 detail/992 | 2026-10-09 23:18-23:22Z |
| H15 | 商店全列表 37 件，名称无一含 Halloween | https://store.steampowered.com/itemstore/3419430/ajaxgetitemdefs/render/?query=&start=0..36&count=12&filter=All | CONFIRMED | total_count 37；37 个名称无 Halloween | 2026-10-09 23:18-23:22Z |
| H16 | Spooky Skeleton 标价 US$2.50，描述「Thank you very much for supporting Bongo Cat!」 | detail/594 | CONFIRMED | 原文一致 $2.50 | 2026-10-09 23:18-23:22Z |
| H17 | 63 条公告均不含 spooky | feed 全文 | CONFIRMED | spooky 0 命中 | 2026-10-09 23:18-23:22Z |
| H18 | Bongo Coins "can be used later" 买 premium 500 coins；是否已开启「not confirmed」 | Sept 1 帖 | CONFIRMED | 「These coins can be used later to buy the premium version of the pass for 500 coins」 | 2026-10-09 23:18-23:22Z |
| H19 | 10 月帖：选中 "All Passes" 列表、点 "Get Pass" 或 "Unlock" 拿上月通行证；激活引文；完成后自动选下一个 | Oct 1 帖 | CONFIRMED | 原文一致 | 2026-10-09 23:18-23:22Z |
| H20 | 终稿结尾引文 "Don't forget to update your game, keep tapping and claim your rewards!"；两篇 2025 帖也要求更新 | Oct 1 2026 / Autumn / Free Halloween Treat | CONFIRMED | 三帖均有；Autumn「don't forget to update your game!」 | 2026-10-09 23:18-23:22Z |
| H21 | Free Halloween Treat（2025-10-30）：7 天、至 5 日 November；可选 Zombie/Nosfergato/Frankittystein；follow the giftbox；analytics 引文；无兑换码 | https://store.steampowered.com/news/app/3419430/view/1815034432865853 | CONFIRMED | 原文「for the next 7 days (until the 5th of November)」等；全帖无 code | 2026-10-09 23:18-23:22Z |
| H22 | 「The post does not say whether the two costumes you did not pick could be obtained another way」 | 同上 | CONFIRMED | 全帖无此说明 | 2026-10-09 23:18-23:22Z |
| H23 | Autumn Event（2025-10-08）：until 31st of October、20 exclusive autumn items、4 for each rarity、"After October 31th the items will no longer be dropable."、不列 20 件名、3 skins + 3 hats、三只松鼠名、33% | https://store.steampowered.com/news/app/3419430/view/1813041031167641 | CONFIRMED | 原文一致 | 2026-10-09 23:18-23:22Z |
| H24 | 三只松鼠商店各 US$2.50 | ajaxgetitemdefs 全列表 | CONFIRMED | Calabrian Black / Eastern Grey / Eurasian Red 均 $2.50 | 2026-10-09 23:18-23:22Z |
| H25 | 搜 halloween、spooky、autumn、pumpkin、costume：3 帖命中，表中三行命中词（autumn / halloween+costume / halloween）正确，spooky 与 pumpkin 0 | feed 全文（标题+正文，不分大小写） | CONFIRMED | halloween：2026-10-01、2025-10-30；autumn：2025-10-08；costume：仅 2025-10-30；三帖并集=3 | 2026-10-09 23:18-23:22Z |
| H26 | 「One post from 2026 contains the word Halloween … No post from 2026 mentions a free costume, a giftbox for Halloween, or a return of the 2025 three」 | feed 2026 年各帖 | CONFIRMED | 2026 年仅 10-01 含 Halloween；costume/zombie/nosfer/frankit 在 2026 帖 0 命中；giftbox 仅 2026-02-05 Steam Typing Fest（Mecha，非 Halloween） | 2026-10-09 23:18-23:22Z |
| H27 | Sept 1 帖引文 "Events like the summer event, lunar new year, april fools or the winter event will still happen"、"will then also drop event chests"；Halloween/autumn 不在名单 | Sept 1 帖 | CONFIRMED | 原文一致，名单无 Halloween/autumn | 2026-10-09 23:18-23:22Z |
| H28 | 「None of the 63 announcements announces an autumn drop event for 2026」 | feed | CONFIRMED | autumn 仅 2025-10-08 帖 | 2026-10-09 23:18-23:22Z |
| H29 | 「The Autumn Event post says its items would no longer be droppable after October 31, 2025, … Whether they can be traded is not stated in any announcement」 | feed | CONFIRMED | Autumn 帖无交易说明（限定「in any announcement」，范围与来源相符） | 2026-10-09 23:18-23:22Z |
| H30 | 2025 年 vs 2026 对比表：Announced 日期、Deadline、Autumn drop event 栏 | 以上各帖 | CONFIRMED | Oct 30 2025 / Oct 1 2026 / Nov 5 2025 一致 | 2026-10-09 23:18-23:22Z |
| H31 | 「It is a monthly pass」 | Sept 1 帖 | CONFIRMED | 「Every month, the pass includes…」「there will be new cosmetics every month」 | 2026-10-09 23:18-23:22Z |
| H32 | tldr 与 description、首段、正文互相矛盾？ | 通读 | CONFIRMED（无矛盾） | description「What the October 1 post confirms」与正文一致；tldr 价格/日期与正文一致 | 2026-10-09 23:18-23:22Z |

## paw-pass.md 这次新加的站内链接（git diff --cached HEAD，只读）

结论：只新增 3 条站内链接，其余文字一字未动。验证方法：把 diff 里新旧行的链接标记剥掉后逐字比对，3 行剥除后均与旧行相同。
- 第 59 行（First Paw Pass 行）：emotes → [emotes](/bongo-cat/emotes/)
- 第 60 行（Halloween Edition 行）：Halloween（Theme 栏）→ [Halloween](/bongo-cat/halloween/)
- 第 62 行：Legendary → [Legendary](/bongo-cat/legendary-odds/)
- 三个目标 slug 均在允许清单内，目录下文件均存在。
- 旁注（不在 diff 内、未改）：paw-pass.md 第 55 行、第 86 行仍写「October 10, 2026」，与这三页统一的 October 9, 2026 不一致；这两处都不在本次 diff 内（本次只读，未改）。

## 三项机检

① 外链全部 curl（-L）：13 个 store/news/itemstore 链接 + feed，全部 200；正文外链全部在 sourceUrls 内（含 detail/594、detail/992、itemstore、1813…、1815…、1842…、1845…、feed）。
② 站内链接目标：emotes、events、exchange-trading、free-items、hats-skins、paw-pass，均在允许 slug 内，无 market-prices。
③ 时效词（now/currently/upcoming/soon/latest/recently/today）：0 处。
