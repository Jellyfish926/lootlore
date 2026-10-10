# 核验：/blockspin/robux-shop/

33 条命题，1 条被推翻，1 条未验。取证时间 2026-10-10 02:23–02:28 UTC，全部自己重取（原始响应与脚本在 `v/` 与 `chk.py`、`chk-output.txt`，未使用写手 raw/）。

取证概况
- developer-products v2 `?limit=100`：HTTP 200，`developerProducts` 68 条，`nextPageCursor` null；`?limit=10` 返回 10 条并带 cursor（说明 limit=100 一页即全）。不带 limit 返回 InvalidPageSize 错误，不影响结论。
- 在售（IsForSale=true）66 条；不在售 2 条：`VideoAdTVProduct`、`DO  NOT USE`（两个空格）。名称以 OLD PRODUCT 开头且在售 2 条：`OLD PRODUCT DO NOT BUY`（850）、`OLD PRODUCT`（250）。页面计入 64 = 66 − 2。口径在文末「How did we read」自洽，但开头 / tldr / 标题把 64 说成「marked for sale」，见 R1。
- 68 条里 `Name` = `DisplayName`、`Description` = `DisplayDescription`，逐条一致。
- game-passes：`{"gamePasses":[],"nextPageToken":null}`；badges 默认排序与 `sortOrder=Asc` 各取一次：`data: []`，两个 cursor 均 null。
- virtual-events：不带参数轮询 10 次（间隔 2 秒），10 次全是 11 条（出现 10/10），nextPageCursor 均为 `id_2zwAAAZ4N4QSVzxqLvS9HAgIz`；顺此 cursor 取第二页 3 条（cursor 空串）。最多共 14 条。

DP = https://apis.roblox.com/developer-products/v2/universes/6765805766/developerproducts?limit=100；GP / BG / GM / EV 同草稿 sourceUrls。

| 编号 | 命题 | 验证路径 | 结果 | 证据 | 取证时间（UTC）|
|---|---|---|---|---|---|
| R1 | 「BlockSpin's Robux shop held 64 products marked for sale」（正文首句；tldr 第 1 条「hold 64 BlockSpin products marked for sale」） | DP `IsForSale` | REFUTED | IsForSale=true 的有 66 条，不是 64。另 2 条在售的 OLD PRODUCT 被排除，排除理由只在文末写明（「we left those four out」）。首句与 tldr 把 64 说成「标为在售的全部」，与接口 66 不符；文末口径本身自洽 | 02:23 |
| R2 | 开发者商品接口 68 条、一页翻全 | DP `developerProducts` 长度、`nextPageCursor` | CONFIRMED | 68；nextPageCursor null | 02:23 |
| R3 | 「Two records were not marked for sale, and two more marked for sale have names beginning OLD PRODUCT」 | DP `IsForSale`、`Name` | CONFIRMED | 不在售：VideoAdTVProduct、DO  NOT USE；OLD PRODUCT 在售 2 条（850、250） | 02:23 |
| R4 | 价格 25（Tiny Money: $300）到 16,500（Supreme: $1,000,000），64 条口径 | DP `PriceInRobux` | CONFIRMED | min 25 Tiny Money: $300；max 16500 Supreme: $1,000,000（脚本） | 02:25 |
| R5 | 页内每个商品行（现金包 7、Safe Slot 5 + Inventory Slot + Protect Item、Stock Skip 6、车辆 5、十条清单 10，共 35 行）名称逐字、Robux 价格、Created 的 UTC 日期 | DP `Name` `PriceInRobux` `Created` | CONFIRMED | `chk.py` 解析页内表格与列表逐行与响应比对：35 行名称逐字相同（含 `Passive Mode #2 [15 minutes]`、`Stock Skip (24 Hours - 7 Days)`、`Hustler: $3000` 无逗号、`Great: $12,000` 有逗号）、价格相同、带日期的 18 行日期相同（按 UTC 转换）。脚本对 1 行报 PRICE 不符，是我的正则把分组表 `Skip Crate Animation (Forever) \| 1 \| 499 \| 499` 的商品数列 1 当价格，非页面错误 | 02:25 |
| R6 | 页内提到的单价：Mansion (Forever Access) 2,999；+1 Extra Car Space 150；Mansion Upgrade: Humvee 8,000；Shotgun Ammo Boost 180；RPG Kit 4,310；Revenge Pack / 2 / 3 为 190 / 290 / 390 | DP `PriceInRobux` | CONFIRMED | 2999；150；8000；180；4310；190、290、390 | 02:25 |
| R7 | 页内只写 Created 不写 Updated；正文无逐行 Updated 日期。「record dates」仅用于 Created 与 56 条同一编辑日 | DP `Created` `Updated` | CONFIRMED | 页内没有逐行 Updated 声称；唯一的 Updated 声称见 R9 | 02:25 |
| R8 | 「Four of the 64 records have a description」「Five of the 68 have text in the description field, four of those five are among the 64」；这 4 条全是名称含 Car 的 Mansion Upgrade | DP `Description` | CONFIRMED | 非空 5 条：Personal Car Crate、Personal Car Customs、Underground Car Garage、+1 Extra Car Space（均在售、在 64 内），以及 `DO  NOT USE`（不在售）。其余 63 条 `Description` 为空串（64 内 60 条为空） | 02:25 |
| R9 | 「Fifty-six of the 68 share an edit date of May 13, 2026」 | DP `Updated` | CONFIRMED | `Updated` 以 2026-05-13 开头的 56 条（含 Rezvani 的 14:26:07Z） | 02:25 |
| R10 | 分组计数：现金 7、Mansion 9、武器类 20（17 + 3 Revenge）、车辆 5、保险箱槽 / 背包 / Protect Item 7、Stock Skip 6、Gang 2、护甲 / 复活 / 被动 / 补给 7、Skip Crate 1，合计 64 | DP，按页内分组规则脚本分组 | CONFIRMED | 9 组并集恰为 64 条，无重叠、无遗漏（脚本 `groups cover S exactly: True 64 64`）；每组条数同页面 | 02:25 |
| R11 | 每组价格区间：现金 25–16,500；Mansion 150–8,000；武器类 180–4,310；车辆 350–8,000；槽 / 保护 90–1,950；Stock Skip 40–5,000；Gang 90–300；护甲类 60–350；Skip Crate 499 | DP `PriceInRobux` | CONFIRMED | 脚本输出：25/16500、150/8000、180/4310、350/8000、90/1950、40/5000、90/300、60/350、499 | 02:25 |
| R12 | 每组合计：23,825 / 20,149 / 27,588 / 12,759 / 5,833 / 7,090 / 390 / 1,638 / 499 | DP，脚本求和 | CONFIRMED | 完全一致 | 02:25 |
| R13 | 总和 99,771（等号右边展开式 23,825 + … + 499） | 脚本求和 | CONFIRMED | 64 条价格直接求和 = 99,771，分组求和 = 99,771 | 02:25 |
| R14 | 「no bundle at that price is in the records」 | DP `PriceInRobux` 搜 99771 | CONFIRMED | 68 条中最高价 16500；无 99771 | 02:25 |
| R15 | 五个 Safe Slot 合计 4,335 | DP 脚本 | CONFIRMED | 90+270+675+1350+1950 = 4335 | 02:25 |
| R16 | 现金包换算：12.0 / 12.0 / 12.0 / 16.0 / 25.0 / 47.3 / 60.6 | DP `Name` 的 $ 数 ÷ `PriceInRobux` | CONFIRMED | 12.0、12.0、12.0、16.0、25.0、47.337→47.3、60.606→60.6；页内表格四列价格与美元数与接口一致 | 02:25 |
| R17 | 「Supreme gives about five times as many dollars per Robux as Tiny Money (60.6 ÷ 12.0 ≈ 5.05)」 | 脚本 | CONFIRMED | 60.606/12 = 5.0505 | 02:25 |
| R18 | 「$500 ... about 42 Robux (500 ÷ 12 ≈ 41.7)」 | 脚本 | CONFIRMED | 41.667 | 02:25 |
| R19 | 「The three cheapest packs share one rate, and the rate climbs from Great upward」 | 脚本 | CONFIRMED | 前三个均 12.0，之后 16.0、25.0、47.3、60.6 递增 | 02:25 |
| R20 | 「Seventeen product names include a weapon, ammo or throwable word, from Shotgun Ammo Boost at 180 to RPG Kit at 4,310」 | DP `Name` | CONFIRMED | 按页内词表（AK47、Glock、RPG、MP5、P226、Remington、Hunting Rifle、Sledge Hammer、Slap Tool、Firework Launcher、Ammo、Molotov、Grenade）在 64 内命中 17 条；最小 Shotgun Ammo Boost 180，最大 RPG Kit 4310。词表是写手的，Brainrot Slap Tool / Sledge Hammer / Firework Launcher Pack 是否算「weapon」属分类，非接口事实 | 02:25 |
| R21 | 「Nine records have a name starting with 'Mansion'」「Mansion (Forever Access) at 2,999 and eight named 'Mansion Upgrade:'」；「Four of the eight carry an official description; all four have 'Car' in the product name」 | DP `Name` `Description` | CONFIRMED | 以 Mansion 开头 9 条，其中 8 条 `Mansion Upgrade:`；8 条里 4 条有描述，名称均含 Car | 02:25 |
| R22 | 「Roblox's records carry no category field」；分组是写手按名称分的，不是官方分类（页内是否明说） | DP 记录全部键；页面文本 | CONFIRMED | 记录键为 AssetId、AssetTypeId、Created、Creator、Description、DeveloperProductId、DisplayDescription、DisplayIconImageAssetId、DisplayName、IconImageAssetId、IsForSale、IsLimited、IsLimitedUnique、IsNew、IsPublicDomain、MinimumMembershipLevel、Name、PriceDiscountDetails、PriceInRobux、ProductId、ProductType、TargetId、UniverseId、Updated、UserBasePriceInRobux 及小写重复键；无 category 字段；「category」在 DP/GP/BG/GM 全文 0 命中。页内明说：正文「The groups are ours: we sorted the products by the words in their names, and Roblox's records carry no category field」、表头「Group (our label)」、scope「Groups are ours, sorted by product name, not official categories」 | 02:25 |
| R23 | 「Whether prices differ inside the game from the record」、「Whether a product can be bought more than once」等 not confirmed | DP 全文搜 once / limit / max / purchase | CONFIRMED | 68 条描述中仅 +1 Extra Car Space 写 `(Max 6)`，那是车位数，不是购买次数；无任何描述写购买次数。IsLimited / IsLimitedUnique 为布尔字段，页面未引用 | 02:26 |
| R24 | 「None of the seven records [cash packs] has a description」；Safe Slot 七条、Stock Skip 六条、十条清单均无描述 | DP `Description` | CONFIRMED | 上述共 30 条商品 `Description` 全为空串 | 02:25 |
| R25 | 否定：Protect Item、Passive Mode、Stock Skip、Revenge Pack、Quick Revive、Mazede、Stang、Christmas Low Rider Pack 的功能 not confirmed | 全部响应文本大小写不敏感搜索 | CONFIRMED | 命中表：protect 3（全在 Protect Item 的 Name / DisplayName / displayName）；passive 6（两条名称 × 3）；stock 18（六条名称 × 3）；revenge 9（三条 × 3）；revive 3；Mazede 3、Stang 3、Low Rider 3（均仅为 DP 名称字段）；在 GP / BG / GM / EV 响应中均 0 命中；这些商品 `Description` 为空串 | 02:26 |
| R26 | 「The same day's records held zero game passes and zero badges」 | GP；BG（默认与 Asc） | CONFIRMED | GP `{"gamePasses":[],"nextPageToken":null}`；BG `{"previousPageCursor":null,"nextPageCursor":null,"data":[]}` ×2 | 02:23 |
| R27 | 事件：标题 "NEW CAR DROPPING!"、副标题 "Introducing the Rezvani"、列于 2025-08-02 至 2025-08-03；「gives no price」；Rezvani 被另一官方记录称为 car | EV `title` `subtitle` `eventTime` `description` | CONFIRMED | startUtc 2025-08-02T18:00:09+00:00，endUtc 2025-08-03T18:15:09+00:00；description 空串、tagline 空串，无价格 | 02:24 |
| R28 | 「the other four names are in no event listing we read that day」（Mazede、Christmas Low Rider Pack、Dirt Bike、Stang） | EV 两页全文 14 条，搜 Mazede / Stang / Dirt Bike / Low Rider | CONFIRMED | 4 个关键词在 EV 响应 0 命中（Rezvani 命中 2 次，均是该活动的 subtitle 与 displaySubtitle） | 02:26 |
| R29 | 「Damage, fire rate and in-game cash prices are not in the records we read」 | 全部响应搜 damage / fire rate / cash price | CONFIRMED | 三词在全部 7 个响应中 0 命中 | 02:26 |
| R30 | 游戏描述含「free code worth $500」和 "place items into the safe in your house to keep them secure"；页内不写具体码 | GM `description`；页面 | CONFIRMED | 描述原文：「Use code W7C28D for $500 free cash if you're a new player!」「...place items into the safe in your house to keep them secure.」；页面全文不含 W7C28D | 02:24 |
| R31 | 页内「Skip Crate Animation (Forever): 499」等 Updated 之外的 created 日期以 UTC 表述；开头 scope「all dates UTC」 | DP `Created` | CONFIRMED | 日期取自 Created 的 UTC 日历日（`chk.py` 用 UTC 转换，全部相符） | 02:25 |
| R32 | 正文配图 th1 的 alt 与署名 "Official thumbnail · Cinnamon Go! (Roblox)"：蓝色跑车、深色街道、火花、红白 BlockSpin 标 | thumbnails.roblox.com 返回的 th1 图片（faec41da…）；GM `creator.name` | CONFIRMED | 重取并目视：蓝色跑车、深色街景、火花、左上红白 BlockSpin 标；GM `creator.name` = "Cinnamon Go!"（Group 33720745）。「drifting」为目视解读 | 02:27 |
| R33 | 「The sums are ... checked with a script against the saved response」 | 无法从接口验证 | UNVERIFIED | 属写手过程声明，接口无法证明；数值本身见 R10–R13 已由我自己的脚本重算，全部一致 | 02:26 |


## 机检
1. 外链：正文无外部链接；frontmatter 的 5 个 sourceUrls 即我取证用的 5 个接口，全部 HTTP 200（DP、GP、BG、GM、EV）。
2. 站内链接目标：/blockspin/codes/、/blockspin/beginner/、/blockspin/game-info/、/blockspin/author/ 均在 `content/blockspin/en/` 且 draft: false；/blockspin/weapon-packs/、/blockspin/mansion-upgrades/ 为本批新页，合法。无链向 draft 页。related 里的 weapon-packs、mansion-upgrades、codes、beginner 同样合法。
3. 无日期时间词：now / currently / upcoming / soon / latest / recently / today 在正文 0 次；"new" 仅出现一次，在官方活动标题引文 "NEW CAR DROPPING!" 内。
4. 兑换码：页内无具体兑换码；无第三方站名；无外挂 / 脚本 / 账号买卖内容。
