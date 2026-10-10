# 旧页待修（因 robux-shop / weapon-packs / mansion-upgrades 上线而直接矛盾的句子）

读取日 2026-10-10 UTC。只列直接矛盾，不列访问数等过期数字。我没有改任何旧页。出处文件都在 `raw/`（w-games.json、w-dp-p1.json、w-events.json、w-events-p2.json）。

| # | 文件 : 行 | 原句 | 为什么矛盾 | 建议改法（英文成句） | 今天的接口出处 |
|---|---|---|---|---|---|
| 1 | content/blockspin/en/index.md : 56 | "A short list. The official sources we reached contain a short game description, four promotional thumbnails and one code." | 新三页用的官方来源还有 68 条开发者商品记录和 14 条活动列表 | "The official sources we reached are the game description with its one code, four promotional thumbnails, and Roblox's public records for the game: 68 developer product records and 14 event listings, read on October 10, 2026 (UTC)." | developer-products v2：`developerProducts` 长度 68；virtual-events：14 条（首读 11 + 3） |
| 2 | content/blockspin/en/index.md : 58 | "Job names, map locations, weapon lists, vehicle case odds and trading values are not published anywhere official that we could reach. … Pages on jobs, locations, weapons and vehicles stay unpublished here until each fact is checked in-game." | weapon-packs 发布后，「weapons 页不发布」「武器清单官方哪里都没有」两处都不成立：官方商品记录里有 17 个带武器 / 弹药 / 投掷物词的 Robux 商品；另外原句是无范围的否定（anywhere） | "A list of jobs and what each pays, map locations, weapon stats, vehicle case odds and trading values are not in the official records we read on October 10, 2026. What those records do hold is the Robux shop: product names and Robux prices, covered in the [Robux shop guide](/blockspin/robux-shop/) and the [weapon packs guide](/blockspin/weapon-packs/). Pages on jobs and map locations stay unpublished here until each fact is checked in-game." | developer-products v2：17 条名称含武器词的在售记录（w-calc-output.txt 的 weapon 组）；全量检索 damage / fire rate / pay / salary / location / map / odds / chance / trad / value 在名称与描述类字段 0 命中（raw/w-neg-extra-search.txt）；注意 job 有 2 处命中：游戏描述 "jobs" 与活动标题 "NEW JOB - FISHING!"，所以建议句不写「没有 job names」 |
| 3 | content/blockspin/en/getting-started.md : 48 | "Guides on jobs, map locations, weapons and vehicles are being prepared, but they stay unpublished until each detail has been checked in the live game. The game updates often — the last update on Roblox was September 19, 2026 — so a list that was right a few months ago can easily be wrong today." | ① weapon-packs 已发布，且依据是官方记录不是实机；② mansion-upgrades 写的游戏记录 `updated` 是 2026-10-03，这句无日期范围地写 9 月 19 日；③ "being prepared" 是占位式承诺 | "Guides on jobs and map locations stay unpublished until each detail has been checked in the live game. Robux prices are a different case: they come from Roblox's own product records and are in the [Money & Gear guides](/blockspin/money-gear/). The game record's \"updated\" timestamp read October 3, 2026 when we checked on October 10, 2026 (UTC), so a list that was right a few months earlier can be wrong on the day you read it." | games v1：`updated` = 2026-10-03T18:00:48.126Z |
| 4 | content/blockspin/en/game-info.md : 43 | "Roblox records the experience as created on November 6, 2024, and last updated on September 19, 2026. The game's title on Roblox carries a tag in square brackets — \"[WEATHER]\" at the time of checking — that the developers change to flag the current update, so the name you see may differ." | mansion-upgrades 写：读取日游戏名是 "BlockSpin 🔪 [MANSION UNDERGROUND]"、`updated` 是 2026-10-03。「last updated on September 19, 2026」没挂读取日，两页同站并存即互相矛盾 | "Roblox records the experience as created on November 6, 2024. On October 10, 2026 (UTC) the record's \"updated\" timestamp read October 3, 2026, and the game's title carried the tag \"[MANSION UNDERGROUND]\" in square brackets; on September 29, 2026 the tag was \"[WEATHER]\". The developers change the tag, so the name you see may differ." （同时把该页 checkedAt / reviewed 改到实际复核日；页内其余 2026-09-29 的数字若不重取就保留原日期） | games v1：`name` = "BlockSpin 🔪 [MANSION UNDERGROUND]"，`created` = 2024-11-06T14:19:35.68Z，`updated` = 2026-10-03T18:00:48.126Z |

## 看过但没列入的（带日期范围或不构成直接矛盾）

- index.md : 46 表格行 `Last game update | September 19, 2026 | 2026-09-29`：有 Checked 列，是带日期的读数；过期但不算直接矛盾。改 #4 时建议一并更新。
- game-info.md : 83 "The game description on Roblox is the one place we have seen the developers publish a code and a gameplay warning."：今天读到的活动列表里有两条 2025 年的官方活动提到发码（"10 DRACO CODES"、"CODES DROPPING ON STREAM"），但都**没有印出任何码**，原句仍成立。codes 页的「官方来源」清单可以考虑把活动列表加进巡检范围（建议，不是矛盾）。
- beginner.md : 68、author.md : 30、cheats-bans.md、codes.md：没有与三张新页冲突的句子。
- money-gear.md：整页重写，见 `drafts/money-gear.md` 与 `category-plan.md`。

## 建议句里不是今天取证的片段（接入前要么重取、要么照旧页原有出处保留）

- #1 的 "four promotional thumbnails"：沿用旧页说法，thumbnails 接口我今天没重取。
- #4 的 "on September 29, 2026 the tag was \"[WEATHER]\""：沿用 game-info 旧页 2026-09-29 的读数，今天的接口只能证明 10-10 的 tag。

## 顺带发现（不是矛盾，供决定要不要另开任务）

- 活动列表里有一条官方活动标题是 "NEW JOB - FISHING!"（subtitle "GO FISH"，2025-08-09 至 2025-08-16 UTC）。beginner.md : 64 把钓鱼写成「除 jobs 之外的活动」（依据是缩略图），与官方标题把它叫 JOB 的说法不一致；不是新三页引起的，未列入上表。
- 矩阵 01:10 UTC 记录「活动只有 1 条」。我 02:11 首读是两页 11 + 3 = 14 条，02:18 两次复读单页 14 条。该接口返回不稳定，以后取活动要翻页并复读。
