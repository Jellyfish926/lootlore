# 核验：/blockspin/money-gear/

14 条命题，2 条被推翻，0 条未验。取证时间 2026-10-10 02:23–02:30 UTC，接口取证与 robux-shop 同一批响应（DP 68 条 / 66 在售 / 64 计入；GP、BG 空；EV 轮询 10 次均 11 条 + 第二页 3 条共 14 条；GM 游戏记录）。

| 编号 | 命题 | 验证路径 | 结果 | 证据 | 取证时间（UTC）|
|---|---|---|---|---|---|
| M1 | 「64 products on sale in the records read on October 10, 2026 (UTC)」（正文）；title / 描述中的 64 | DP `IsForSale` | REFUTED | IsForSale=true 共 66 条。64 是排除两条名称以 OLD PRODUCT 开头的在售记录（850、250 Robux）之后的数；本页没有说明这一排除，只有 robux-shop 文末写了。草稿原句：「64 products on sale in the records read on October 10, 2026 (UTC)」 | 02:23 |
| M2 | 「sorted into nine groups by name」 | robux-shop 分组脚本 | CONFIRMED | 9 组并集恰为 64 条（`chk.py`）。本页未写「分组是我们分的、不是官方分类」，只写「by name」；对应说明在 robux-shop 页内 | 02:25 |
| M3 | 「zero game passes and zero badges in the same day's records」 | GP；BG（默认与 Asc） | CONFIRMED | GP `{"gamePasses":[],"nextPageToken":null}`；BG `data: []` | 02:23 |
| M4 | 「cash packs worked out as in-game dollars per Robux」「safe slots, Stock Skips, gang products」 | DP | CONFIRMED | 现金包 7 条（12.0–60.6 美元 / Robux，见 robux-shop 核验）；Safe Slot ×5、Stock Skip ×6、Create Gang、+1 Gang Member 均在 DP 中 | 02:25 |
| M5 | 「The 17 products with a weapon, ammo or throwable word in the name, from 180 to 4,310 Robux, plus the three Revenge Packs」 | DP `Name` `PriceInRobux` | CONFIRMED | 按 robux-shop 词表命中 17 条，最小 Shotgun Ammo Boost 180，最大 RPG Kit 4310；Revenge Pack / 2 / 3 存在（190 / 290 / 390） | 02:25 |
| M6 | 「These are Robux prices and not in-game cash prices; damage and fire rate are not in the records」 | 全部响应搜 damage / fire rate / cash price | CONFIRMED | 三词在 DP、GP、BG、GM、EV 响应 0 命中 | 02:26 |
| M7 | 「The nine Mansion products from 150 to 8,000 Robux」 | DP | CONFIRMED | 以 Mansion 开头 9 条；最小 +1 Extra Car Space 150，最大 Humvee 8000（Forever Access 2999） | 02:25 |
| M8 | 「the four official descriptions for the underground garage upgrades copied as written」 | DP `Description`；EV | REFUTED | 有描述的 4 条：Personal Car Crate「Gives you access to roll cars in your underground car storage.」；Personal Car Customs「Allows you to roll car customisation crates and customise your car.」；Underground Car Garage「Gives you access to the underground car garage.」；+1 Extra Car Space「Gives you +1 extra car storage place (Max 6)」。其中 Customs 与 Extra Car Space 的描述不含 underground，接口没有把这两条归为「underground garage upgrades」。四条的创建日同为 2026-09-30，EV 的 [UPD] Mansion Underground 描述只点名 Underground Car Garage。草稿原句：「the four official descriptions for the underground garage upgrades」。「copied as written」属 mansion-upgrades 页的内容，不在本次范围，未验 | 02:28 |
| M9 | 「the record and event dates around the Mansion Underground update」 | EV `title` `eventTime` | CONFIRMED | 存在 "[UPD] Mansion Underground"，startUtc 2026-10-03T18:00:33.578+00:00，endUtc 2026-10-07T16:50:33.578+00:00；四条描述商品 Created 2026-09-30 | 02:28 |
| M10 | 「Job pay, map locations and in-game cash prices are not in those records」；「vehicle case odds ... not in those records」 | 全部响应大小写不敏感搜 pay / map / odds / cash price / job / case | CONFIRMED | `pay` 0、`map` 0、`odds` 0、`cash price` 0。`job` 命中 GM 描述 1 次（"Grind your way through jobs to unbox random reward cases"）与 EV 2 次（"NEW JOB - FISHING!"、FISHING UPDATE 相关），均无工资数字；`case` 仅 GM 描述 1 次，无概率 | 02:26 |
| M11 | 「the developer product list, the game pass and badge lists, the event listings and the game record」是这些指南使用的来源 | sourceUrls（robux-shop）的 5 个接口 | CONFIRMED | 五个接口 DP、GP、BG、EV、GM 全部 HTTP 200，与表述一一对应 | 02:23 |
| M12 | 「a record date is treated as the day a record was made, which is not proof of a release date」；本页未把 Created / Updated 说成功能上线日 | 页面文本 | CONFIRMED | 全文只有该一句涉及日期，且是限定性表述；无把记录日期写成上线时间的句子 | 02:26 |
| M13 | 「For the official code, the death-drop rule and the developer facts, see the getting started guides」 | GM `description`；站内 getting-started.md | CONFIRMED | GM 描述含 "Use code W7C28D for $500 free cash"（本页未印出码）与 "You drop everything in your inventory on death"；/blockspin/getting-started/ 为已发布页，正文含 code、death / drop、developer 内容（grep 命中 9、4、6） | 02:29 |
| M14 | 「Each price carries the date it was read」 | 页面文本 | CONFIRMED | 本页本身不列任何价格，只在 tldr 和 robux-shop 条目写「read on October 10, 2026 (UTC)」；此句指向各指南，robux-shop 页内有读取日。未发现价格数字无读取日的情形 | 02:29 |

说明：M8 为分类归属不实，不涉及价格数；M1 与 robux-shop 的 R1 同一口径问题。

## 机检
1. 外链：正文无外部链接；sourceUrls 为空数组（本页 frontmatter），无需核对。
2. 站内链接：/blockspin/robux-shop/、/blockspin/weapon-packs/、/blockspin/mansion-upgrades/ 为本批新页，合法；/blockspin/getting-started/（draft: false）、/blockspin/（index.md，draft: false）均已发布。无链向 draft 页（jobs、map-locations、vehicles、weapons 均为 draft: true，本页未链）。
3. 无日期时间词：now / currently / upcoming / soon / latest / recently / new / today 在正文 0 次（grep 无命中）。
4. 无具体兑换码、无第三方站名、无外挂 / 脚本 / 账号买卖内容。
5. 注意：`/home/claude/lootlore/content/blockspin/en/money-gear.md` 现有版本为 draft: true 的旧稿（标题 "Jobs, Weapons, Cars"），本批文件将替换它；旧稿里关于 jobs 和 vehicle 的承诺与本页说明的「无工作、无地图、无概率指南」方向不同，是内容替换而非冲突。
