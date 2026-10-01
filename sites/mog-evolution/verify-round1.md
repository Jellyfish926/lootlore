# verify-round1 对抗验证表（+1 Mog Evolution，取证日 2026-10-01）

109 条命题，4 条被推翻，15 条未验/不可复现（CONFIRMED 90）。

取证路径：games/groups/badges/game-passes/developer-products/virtual-events/places/votes 等 Roblox 一手接口自行调用；get-age-recommendation 用 POST；thumbnails 接口取回 8 张图肉眼核对标签；fan 站（urgametips、aprasi）与 Roblox Help 文章核对三条外部命题。未读 dossier/planning/raw。抽样：A 级全验；index、appeal 出 REFUTED 后两页转全量；B 级几乎全验（量小）。

| # | 页面 | 命题 | 级 | 结果 | 证据 / 说明 |
|---|---|---|---|---|---|
| 1 | index | 创建日期 30 Aug 2026 | A | **CONFIRMED** | games.roblox.com/v1/games?universeIds=10764479526 created=2026-08-30T13:57Z |
| 2 | index | 31.7M visits / 344,000 favourites | A | **CONFIRMED** | games.roblox.com/v1/games?universeIds=10764479526 复核时 visits 31,795,406 / favoritedCount 345,049(单调增，与页面快照一致) |
| 3 | index | 265,568 likes vs 5,291 dislikes, 约 98% | A | **CONFIRMED** | games.roblox.com/v1/games/votes?universeIds=10764479526 复核 265,614/5,292 → 98.05% |
| 4 | index | 7,523 players online (1 Oct 快照) | A | **UNVERIFIED** | 实时值已变(7,490)，过去快照无法复现；属时间点快照，不构成错误 |
| 5 | index | Navoj Mog 群 5.46M 成员 | A | **CONFIRMED** | groups.roblox.com/v1/groups/426881025 memberCount=5,457,887 |
| 6 | index | 12 人/服、Simulation·Incremental Simulator、Free | A | **CONFIRMED** | games.roblox.com/v1/games?universeIds=10764479526 |
| 7 | index | Maturity Minimal | A | **CONFIRMED** | POST apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation {"universeId":10764479526} → displayName=Minimal, "Suitable for everyone" |
| 8 | index | 无 badges / 无 game passes | A | **CONFIRMED** | badges 接口 data=[]；game-passes 接口 gamePasses=[] |
| 9 | index | 43 个 developer products 全部在售，1–999 Robux | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 43 条，IsForSale 全 true，min1 max999，无 nextPageCursor |
| 10 | index | Auto Clicker 22 cps(39 R)；VIP 10x(99 R) | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 11 | index | 9 个 Power x1.5–x256；9 条跑步机 x2–x999 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 12 | index | tldr：「The store descriptions confirm … Stage teleports and Worlds 2 and 3」 | A | **REFUTED** | Skip to World 2 / Skip to World 3 的 Description 均为空字符串(dpu)；只有商品名，没有描述可“确认” |
| 13 | index | 活动 Admin Abuse & Update 4：3 Oct 23:00 UTC–7 Oct 23:00 UTC | A | **CONFIRMED** | apis.roblox.com/virtual-events/v1/universes/10764479526/virtual-events startUtc=2026-10-03T23:00:21Z endUtc=2026-10-07T23:00:21Z |
| 14 | index | 活动列表只有标题、无其它细节 | A | **CONFIRMED** | title/subtitle/description 三字段均为 "Admin Abuse & Update 4" |
| 15 | index | 无 codes：描述/群/活动均无 | A | **CONFIRMED** | 游戏描述无码；group description=""、shout=null；活动描述无码；urgametips.com/plus-1-mog-evolution-codes/ 写 "No working codes are listed right now"(updated 26 Sep) |
| 16 | index | 当前标题 [W3] +1 Mog Evolution | A | **CONFIRMED** | games.roblox.com/v1/games?universeIds=10764479526 name |
| 17 | index | 5 个 399 Robux 商品 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 18 | index | Rebirth 需 level cap；Ascend 到 next body | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 Skip Rebirth / Skip Ascend 描述原文 |
| 19 | index | 测试版副本存在(TESTING) | B | **CONFIRMED** | games.roblox.com/v1/games?universeIds=10765888078 |
| 20 | index | 图注：art02/art06 画面描述 | B | **CONFIRMED** | thumbnails 接口取回的图，画面与图注一致 |
| 21 | shop | 43 条商品名/价格/描述逐字一致 | A | **CONFIRMED** | 逐条程序比对 43 条 Name/PriceInRobux/Description 与 data/entities.json 及页面表格，0 差异 |
| 22 | shop | 总价 5,910 Robux | A | **CONFIRMED** | 43 项 PriceInRobux 求和=5910 |
| 23 | shop | 28 条有描述 / 15 条无描述 | A | **CONFIRMED** | 程序统计 28/15 |
| 24 | shop | 最便宜 x1.5 Power=1；最贵 x999 Treadmill=999 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 25 | shop | 分组表：Appeal packs 4(49–499)、Power 9(1–199)、Treadmill 9(9–999)、Auto/VIP 2、Hammer 2(29–79)、Skips&Wins 10(2–99)、399 ×5、undescribed packs 2(99)，合计 43 | A | **CONFIRMED** | 逐组核对，4+9+9+2+2+10+5+2=43 |
| 26 | shop | 26 of 43 are about Appeal | A | **CONFIRMED** | 4+9+9+1+1+2=26 |
| 27 | shop | 三个 Appeal pack 描述写 Power、+100M 写 Appeal | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 28 | shop | x8 Treadmill(79) 贵于 x9(69) | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 29 | shop | Mogger Pack 18 Sep 创建、次日编辑；Revenge 24 Sep 创建 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 Created 2026-09-18T00:37Z / Updated 2026-09-19T05:13Z；Revenge 2026-09-24T21:54Z |
| 30 | shop | Gigachad / Claviculars / Smoothie 描述原文 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 31 | shop | game-pass 与 badge 列表为空；商品接口一页返回全部 | A | **CONFIRMED** | 同上，nextPageCursor=null |
| 32 | shop | "We read them as the same resource; the developer has not said so"(Power=Appeal) | B | **CONFIRMED** | 措辞已标推断，非确认 |
| 33 | limiteds | 五件商品价格 399 与各自 Added 日期(10 Sep/10 Sep/24 Sep/26 Sep/26 Sep) | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 Created 字段(UTC 日期) |
| 34 | limiteds | Gigachad 描述含 "1,500-copy counter is informational; purchases remain available…" | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 35 | limiteds | Claviculars x1024 Appeal while equipped；Smoothie x2048 Charisma while equipped | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 36 | limiteds | "Charisma appears nowhere else in the game's official text" | A | **CONFIRMED** | 游戏描述与 43 条商品描述 grep 无其它 Charisma |
| 37 | limiteds | LOOKSMEOWXER / MANGO MOGGER 无描述 | A | **CONFIRMED** | Description 为空 |
| 38 | limiteds | x1024 为商店措辞中最大的 Appeal 倍率(超过 x999) | A | **CONFIRMED** | Smoothie 的 x2048 为 Charisma，页内已排除 |
| 39 | limiteds | 对比表 VIP 99/x256 199/x99 249/x999 999 价格与措辞 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 40 | limiteds | "None of the five is mentioned in the game description" | B | **CONFIRMED** | 游戏描述全文无这五个名字 |
| 41 | limiteds | "[W2/W3 LIMITED] point to World 2 / World 3"、"wording suggests other bodies have multipliers" | B | **UNVERIFIED** | 页内已用 point to / suggests 弱化，属推断，未写成确认 |
| 42 | appeal | Power 9 项合计 395 Robux；每 Robux 倍率列 | A | **CONFIRMED** | 1+2+5+12+19+29+49+79+199=395；倍率/价格复算全部一致 |
| 43 | appeal | Appeal pack 每 Robux：2,041 / 6,711 / 33,445 / 200,401 | A | **CONFIRMED** | 100000/49=2040.8；1e6/149=6711.4；1e7/299=33444.8；1e8/499=200400.8 |
| 44 | appeal | x999 为跑步机中每 Robux 价值最高(恰好 1x) | A | **CONFIRMED** | x999 999/999=1.00，其余 ≤0.40 |
| 45 | appeal | Starter Pack 9 Robux，+2,000 Appeal +50 Wins + LTN body，最便宜的 bundle | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100（Mogger Pack/Revenge 为 99 且无描述） |
| 46 | appeal | 表中引文：Auto Clicker / VIP / treadmill 描述 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 47 | appeal | Hammer Upgrade 29 / 79 Robux 无描述 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 48 | appeal | VIP 行 "The largest flat multiplier under 100 Robux" | A | **REFUTED** | 同页表格里 x64 Power(49 R)、x128 Power(79 R) 的倍率都大于 10x；若 Power≠Appeal 则页面自称无法确认；原句与页内数据冲突 |
| 49 | appeal | "That wording suggests belts can also be unlocked through rebirths" | B | **UNVERIFIED** | 已用 suggests 弱化，属推断 |
| 50 | appeal | Power 等同 Appeal / 倍率是否叠加 —— 页面声明 not confirmed | B | **CONFIRMED** | 表述正确地写成未确认 |
| 51 | updates | 活动时间换算：UTC/EDT/PDT/BST/UTC+8 与星期 | A | **CONFIRMED** | Oct 3 2026 为周六；BST(+1) 至 25 Oct，EDT(-4) 至 1 Nov 均生效；4 Oct 00:00 BST、07:00 UTC+8 均正确 |
| 52 | updates | 活动创建于 28 Sep、categories=newContent、host=Navoj Mog | A | **CONFIRMED** | createdUtc=2026-09-28T02:24Z；eventCategories newContent；host group 426881025 |
| 53 | updates | 时间线 30 Aug：18 个商品 | A | **CONFIRMED** | 按 Created 日期程序计数=18 |
| 54 | updates | 时间线 31 Aug：7 项(Starter/VIP/+100M/x9/x99/x999/Auto) | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 55 | updates | 9 Sep 2x Win Pad；10 Sep Gigachad/Claviculars/Skip to World 2 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 56 | updates | 18 Sep：Hammer [1][2]、Mogger Pack、x2–x18 六条跑步机 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 57 | updates | 24 Sep：Smoothie/Skip to World 3/Revenge；26 Sep：两个 LIMITED | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 58 | updates | 时间线日期的时区(表头 "Date (2026)" 未标 UTC) | A | **UNVERIFIED** | 日期取自 API 的 UTC 时间戳(如 18 Sep 00:29Z、24 Sep 03:08Z，美国时区会落在前一天)，页面未标 UTC，属时区缺失 |
| 59 | updates | 30 Sep 17:52 UTC 为最近一次更新；30 Aug 创建 | A | **CONFIRMED** | games.roblox.com/v1/games?universeIds=10764479526 updated=2026-09-30T17:52:34Z |
| 60 | updates | TESTING：10 Sep 创建、1,287 visits、0 在线、无描述、50 人 | A | **CONFIRMED** | games.roblox.com/v1/games?universeIds=10765888078 |
| 61 | updates | RANKED place 存在且描述为空；两个 place | A | **CONFIRMED** | develop.roblox.com/v1/universes/10764479526/places place 88916320688607 description="" |
| 62 | updates | "seven different days"；"roughly once a week" | B | **CONFIRMED** | 新品日=30,31 Aug,9,10,18,24,26 Sep=7 天；间隔约 7–9 天 |
| 63 | updates | "Fan sites report the title read [W2] in mid-September" | B | **CONFIRMED** | aprasi.com 文章标题 "[W2]+1 Mog Evolution"，日期 13 Sep 2026；scriptblox 亦为 [W2] |
| 64 | updates | "The launch-day store already included Rebirth, Ascend, Stages and the Power multipliers, so those systems have been in the game from the start. Worlds, the Win Pad, hammer upgrades and the limited items came later." | A | **UNVERIFIED** | 商品创建时间只证明商品存在；页面前文自己写 "A new product tells you a system existed by that date"，此处却写成系统自启动即有、其它"later"。无一手来源(无补丁日志) |
| 65 | updates | "admin abuse events usually mean developers hand out boosts" | B | **UNVERIFIED** | 类型惯例，页内已声明 not a promise；未验证 |
| 66 | community | 群组：ID 426881025、owner CreatorExchangeInc、Open entry、非 verified | A | **CONFIRMED** | groups.roblox.com/v1/groups/426881025 |
| 67 | community | Roles：Guest/Member/Admin(1 人) | A | **CONFIRMED** | groups.roblox.com/v1/groups/426881025/roles Admin memberCount=1 |
| 68 | community | tier 3 于 11 Sep 2026 | A | **CONFIRMED** | communityTier.currentTier=3, tierUpdatedTime=2026-09-11T00:12Z |
| 69 | community | Public experiences = 2 | A | **CONFIRMED** | games.roblox.com/v2/groups/426881025/games 返回 2 项 |
| 70 | community | 群成员 5,456,141 / visits 31,783,618 / fav 344,986 / votes / 7,523 | A | **CONFIRMED** | 与实时值相比均为合理的单调快照(见 index)；7,523 不可复现 |
| 71 | community | 群墙 Could not be read (Roblox returned an error) | A | **CONFIRMED** | groups.roblox.com/v2/groups/426881025/wall/posts → {"errors":[{"code":0}]} |
| 72 | community | 社交链接需登录 | A | **CONFIRMED** | games.roblox.com/v1/games/10764479526/social-links/list → 9002 Authentication token is missing |
| 73 | community | private servers off、TESTING 50 vs 12 | A | **CONFIRMED** | createVipServersAllowed=false；maxPlayers 50 / 12 |
| 74 | community | "Admin Abuse & Update 4 was listed there on 28 September, six days before it starts" | A | **REFUTED** | createdUtc 2026-09-28T02:24Z → start 2026-10-03T23:00Z = 5 天 20.6 小时，不是 six days（日历日差为 5） |
| 75 | community | "'Mog evolution script' is one of the top searches for this game" | A | **UNVERIFIED** | 无搜索量/趋势来源，页面未给出处；仅能确认 rscripts.net、scriptblox 有该游戏脚本页 |
| 76 | community | "Two fan wikis for the game also showed no active codes" | A | **UNVERIFIED** | 实测 urgametips.com(updated 26 Sep)与 aprasi.com(13 Sep)均写无码，但二者是攻略博客非 wiki，页面也未写出名称/URL |
| 77 | community | scripts break Roblox ToU and can get account banned；常见账号盗窃/恶意软件载体 | A | **CONFIRMED** | en.help.roblox.com/hc/en-us/articles/203312450-Cheating-and-Exploiting：“violation of the Roblox Terms of Use, and will lead to the deletion of an account”，并警告 keylogger/phishing |
| 78 | community | "the group is far larger than favourites, which suggests many join without favouriting" | B | **UNVERIFIED** | 推断，已用 suggests |
| 79 | community | universe/root place ID 正确 | A | **CONFIRMED** | games.roblox.com/v1/games?universeIds=10764479526 |
| 80 | how-to-play | 官方描述四行逐字(含 emoji) | A | **CONFIRMED** | games.roblox.com/v1/games?universeIds=10764479526 description |
| 81 | how-to-play | Skip Ascend / Skip Rebirth / Claviculars 引文 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 82 | how-to-play | Hammer Upgrade 29/79 无描述 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 83 | how-to-play | LTN body 在 Starter Pack；Gigachad body | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 84 | how-to-play | 服务器 12 人、私服关闭 | A | **CONFIRMED** | maxPlayers=12；createVipServersAllowed=false |
| 85 | how-to-play | Maturity Minimal "Suitable for everyone"、免费 | A | **CONFIRMED** | get-age-recommendation POST；price=null。但 sourceUrls 未列此接口 |
| 86 | how-to-play | Robux 购买从 1 起、上限 999 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 87 | how-to-play | "Official art shows labels such as SUB 3, Chad and True Adam" | A | **CONFIRMED** | thumbnails 接口 8 张图，肉眼核验：Sub 3 / MTN / Chad / SUB 3→True Adam / TRUE ADAM·SUBHUMAN / CHOPPED·MOGGER |
| 88 | how-to-play | "The bodies are the 'evolution' in the name." | A | **UNVERIFIED** | 无官方来源把 bodies 与游戏名 "Evolution" 对应；推断被写成事实 |
| 89 | how-to-play | "Parents can use Roblox's own spending controls to cap purchases." | B | **UNVERIFIED** | 未给来源，本轮未核 |
| 90 | how-to-play | 表：Stage 1–3 teleports / World skips / Win Pad / Ranked place | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100；places 接口 |
| 91 | progression | Stage 1/2/3 teleport 2/5/9 Robux；两 World skip 99 且无描述 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 92 | progression | X2 Wins 49、Starter Pack 9、2x Win Pad 49 无描述 | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 93 | progression | 体名表：LTN/Gigachad(商品)；SUB 3/MTN/Chad/Chopped·Mogger/Subhuman·True Adam(官方图) | A | **CONFIRMED** | thumbnails 图肉眼核验，标签出现 |
| 94 | progression | "x9/x99/x999 … no rebirths needed. That suggests some belts are normally unlocked through rebirths" | B | **UNVERIFIED** | 推断，已用 suggests |
| 95 | progression | tldr "at least three Worlds" | A | **UNVERIFIED** | 一手证据只有 Skip to World 2、Skip to World 3 与标题 [W3]；World 1 与"三个 World"是推断 |
| 96 | progression | 配图 art05 alt：「a slim one on green and two muscular ones on red and blue backgrounds」 | B | **REFUTED** | thumbnail 肉眼核验：Sub 3 角色是偏胖(chubby)而非 slim，背景为蓝天+绿地板；同页体名表写它是 "small, chubby"，自相矛盾 |
| 97 | progression | "Stages and Worlds are places you move through" | B | **UNVERIFIED** | Stage 仅有 teleport 商品，页内后文自己写 "what a stage is, is not described" |
| 98 | progression | Ranked 描述为空、无官方规则 | A | **CONFIRMED** | places 接口 |
| 99 | beginner | 43 store items；Admin Abuse 3–7 Oct 2026；30 Aug launch | A | **CONFIRMED** | 同上 |
| 100 | beginner | "Rebirth needs you to reach the level cap" | A | **CONFIRMED** | Skip Rebirth 描述 |
| 101 | upgrades | "Fifteen of them have no description"；$ 每项价格范围 1–999 | A | **CONFIRMED** | 程序计数 15 |
| 102 | upgrades | Gigachad x4 body / Claviculars x1024 / Smoothie x2048 "Charisma" | A | **CONFIRMED** | apis.roblox.com/developer-products/v2/universes/10764479526/developerproducts?limit=100 |
| 103 | upgrades | "The complete store in four tables" | B | **CONFIRMED** | shop 页含 1 张总览 + 3 张商品表 = 4 张 |
| 104 | author | 研究方法、编辑流程、Contact/Editorial Policy 页面 | B | **UNVERIFIED** | 站内模板内容；页面含未解析占位符 {{BRAND}}；/contact、/editorial-policy 不在本次对象中，未核 |
| 105 | author | "On 1 October 2026 no code could be confirmed" | A | **CONFIRMED** | 同 index |
| 106 | entities | 43 条 item 的 name/price/description/product_id/created/updated 与 API 逐字段比对 | A | **CONFIRMED** | 程序比对 0 差异(含 ProductId 3710629270 等) |
| 107 | entities | event-admin-abuse-update-4：deadline 2026-10-07T23:00:21Z、event_id 56687495873692415、listed 28 Sep | A | **CONFIRMED** | virtual-events 接口 |
| 108 | entities | mog-evolution：universeId/rootPlace 92648272637932/rankedPlace 88916320688607/testing 10765888078/group 426881025 | A | **CONFIRMED** | games/places/group 接口 |
| 109 | entities | 页面 frontmatter 引用的 entity id 全部存在；站内 /mog-evolution/ 链接无死链 | B | **CONFIRMED** | 程序检查：0 缺失，0 死链 |

## 需修改清单
见最终回复（同内容）：
1. index.md tldr 第 3 条：Worlds 2 and 3 非"description confirm"。
2. appeal.md VIP 行："The largest flat multiplier under 100 Robux"。
3. community.md："six days before it starts"。
4. progression.md 图注 art05 alt "a slim one on green"。
5. UNVERIFIED 写成确认：updates.md 启动日系统句；community.md top searches / two fan wikis；how-to-play.md bodies=evolution、spending controls；progression.md at least three Worlds / places you move through。
6. 时区：updates.md 时间线表头加 UTC。
7. sourceUrls 缺口：how-to-play / index 缺 get-age-recommendation(POST)；community 缺 Roblox Help 作弊条目。
