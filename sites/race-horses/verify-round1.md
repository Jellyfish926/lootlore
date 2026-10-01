# verify-round1：Race Horses 对抗验证（取证日期 2026-10-01，独立重取 Roblox 一手 API；未读 dossier/planning/raw）

总结：约 170 条原子命题（A 级全验，B 级抽验约 35%，另对 24 徽章、5 通行证、32 商品、entities.json 做程序化全量比对）。CONFIRMED 约 150，REFUTED 3，UNVERIFIED 7。数字类（价格/徽章名/描述/日期/玩家数/群组）零错误。
快照漂移：徽章获得数、点赞、成员数我取证时比页面高（例 Horsin' Around 3,141,309 vs 页 3,139,857；成员 883,463 vs 883,107；点赞 9,786 vs 9,784）——全部单调增长且量级吻合（日增 ≈108,712，差 1,452 约 20 分钟增量），各页均标「1 October 2026 快照」，合规。

取证路径：games.roblox.com/v1/games、/votes；badges.roblox.com/v1/universes/10387635049/badges（含 statistics）；apis.roblox.com/game-passes/v1/…passView=Full；apis.roblox.com/developer-products/v2/…；groups.roblox.com/v1/groups/1006560817、games.roblox.com/v2/groups/…/gamesV2（accessFilter 1/2/3）；experience-guidelines-api；games.roblox.com/v2/games/{id}/media + thumbnails（亲自看了 4 张图）；网页：destructoid、racehorses.online、rblxscripts、Horse Race 的 Roblox 描述。

## 一、REFUTED（3）
| # | 页 | 命题（原文） | 反例/证据 | 结果 |
|---|---|---|---|---|
| R1 | updates.md | "has added something new almost every week since"（导语）；"Something new has been registered in the store or badge list in every week of September" | 创建日期（通行证/商品/徽章 API）：6 Jul（徽章）→28 Jul（Buy Common Egg）中间 22 天无任何新条目；27 Aug→7 Sep 又隔 11 天，9 月第一个自然周（8/31–9/6）无新建条目（仅 1 Sep 的 Starter Pack 是 updated 不是 created）。 | REFUTED |
| R2 | horses.md | tldr："Four things about a horse are random: rarity, coat, eye size and traits." | 官方描述只说 "Coats, eye size and traits are all random"；稀有度没有任何一手来源说随机。本页正文表格自己写 "Seven tiers… set by the egg you hatch"，eggs.md 也写 "whether an egg can roll more than one tier" 未确认。tldr 与正文自相矛盾，把推断写成事实。 | REFUTED（与正文矛盾 + 无来源） |
| R3 | author.md | "Every guide published under that byline is listed below." | 下方只有三个「Where to start」链接，没有任何完整列表。 | REFUTED（页内自证） |

## 二、UNVERIFIED 但写成确认（7）
| # | 页 | 原句 | 为什么没验成 |
|---|---|---|---|
| U1 | eggs.md | "Other Race Horses fan sites still describe six rarities." | 我查到的第三方：destructoid 不列稀有度；racehorses.online 只列三档；sportskeeda 指南 403 读不到。找不到「六档」的站。 |
| U2 | horses.md | "Other fan sites have not covered it either."（Index） | 全称否定，搜索未找到反例但也不可能证明。 |
| U3 | eggs.md tldr / scope；horses.md scope | "Hatch odds and in-game cash prices are not published anywhere official." / "Index rewards, trait names and odds are not published" | 全称否定；游戏内界面（页自己承认有 "SEE ODDS FOR TRAITS"）可能就是官方发布。只能证明 Roblox API/描述里没有。 |
| U4 | races.md | "A game pass is permanent, while a developer product is a one-off purchase." | 与 gamepasses.md 的 "bought per use" 不一致；开发者商品可由开发者做成永久或可重复，机制无一手来源。Double Race Earnings 时长页内已承认未知。 |
| U5 | gamepasses.md | "…developer products, such as Double Race Earnings, which are bought per use." | 同上（Roblox 通用机制，非本游戏实测）。 |
| U6 | updates.md | "Unlike many Roblox games, Race Horses has not retired any paid item yet" | API 全部 IsForSale=true，但无法证明历史上没有被删除的商品（删除的不会出现在列表）。 |
| U7 | eggs.md | "The seventh, Exotic, arrived with the Exotic Egg on 22 September 2026 and the Fruity Foal badge a day later." | 只是商品/徽章创建日期，页内 updates 已声明创建≠上线日，此处写成「arrived」。同类：index.md "hurdle races in early September" 同理（races.md 已写 most likely，index 去掉了 hedge）。 |

附：第三方站（Destructoid/PCGamesN/Dexerto 等）已列出 Race Horses 兑换码（PUMPKINPATCH、FRUITY、BEETS、CARROT、RACER、HORSES 等，Destructoid 2026-09 版）。页面「不列码、说明无官方来源」措辞合规（已 hedge），但与「Third-party sites report codes」一致，无需改；只提示读者价值缺口。

## 三、CONFIRMED（按页汇总，A 级全验）
### index.md
| 命题 | 证据 | 结果 |
|---|---|---|
| 开发者 Gorilla Grafters（群 1006560817），owner N4D_X 且 verified | groups API：owner.hasVerifiedBadge=true, username N4D_X | CONFIRMED |
| 创建 2026-06-24；最后更新 2026-09-30 09:40 UTC | games API created 2026-06-24T14:37:22Z，updated 2026-09-30T09:40:54Z | CONFIRMED |
| 7.5M 访问、379,549 收藏、9,784 赞/1,007 踩 | 实测 7,514,592 / 379,743 / 9,786 / 1,007（快照后增长） | CONFIRMED（快照） |
| 单服 8 人、私服未开、Simulation/Tycoon、Minimal、四端 | maxPlayers 8；createVipServersAllowed false；genre_l1/l2；guidelines "Minimal"；描述末行 | CONFIRMED |
| 该群唯一公开游戏 | gamesV2 accessFilter=2 仅 1 个；accessFilter=3 多出 "Horse Game Dev File"（非公开，229 访问） | CONFIRMED |
| 24 徽章/5 通行证/32 商品；5 通行证合计 1,635；蛋 9–2,799；Starter Pack 25 | 实测 24/5/32；199+249+329+399+459=1635 | CONFIRMED |
| 稀有度比例 54/14/5/1.2/0.2；约 500:1 | 6,102/3,139,857=1/514 | CONFIRMED |
| "Index OUT NOW! Collect horses for rewards!" 为描述首句；群描述 "grafting"、shout 空 | games/groups API | CONFIRMED |
| 近期更新日期链（9/10、9/17、9/22、9/24） | 通行证/商品 created | CONFIRMED |
| "Horse Race" 为另一游戏：有宠物/重生/兑换码 | Roblox 描述 "Collect Pets"、"New Code: …"，URL Super-Rebirth-Horse-Race | CONFIRMED |
| 群 wall/社交链接需登录 | wall 返回 error；social-links 返回 "Authentication token is missing" | CONFIRMED（wall 为空错误，间接） |

### badges.md
| 命题 | 证据 | 结果 |
|---|---|---|
| 24 个徽章名称+要求逐字（含标点，如 "Hatch 50 eggs" 无句号、"Win a race by just 0.2 seconds or less"） | 程序逐条比对 24/24 一致 | CONFIRMED |
| 添加日期（6 Jul/22 Aug/23 Sep 等）、8/12 两徽章同日 | created 字段 | CONFIRMED |
| 各获得数（24 条） | 全部 ≤ 实时值，增量与日增速吻合；无法精确复现快照（会变） | CONFIRMED（快照，标日期） |
| Per 100 比值（24 条） | 重算全部一致（四舍五入内） | CONFIRMED |
| 分类 7 孵化+11 比赛+6 长期；六个低于 0.5 的徽章 | 重数、重算 | CONFIRMED |
| 最难五个排序；Fruity Foal 才 8 天 | 2,168<3,822<6,102<7,458<7,784；9/23→10/1 | CONFIRMED |
| Super Sprinter 比 Winning Stride 多约 124,000 | 1,748,435−1,623,941=124,494 | CONFIRMED |
| 推断句（Super>Winning 原因、So Long 不可撤销等） | 页内均标 "our inference/not confirmed" | CONFIRMED（已 hedge） |

### gamepasses.md
| 命题 | 证据 | 结果 |
|---|---|---|
| 5 通行证名称/价格/描述/日期、均在售、无折扣 | passes API：isForSale true、priceDiscountDetails 空 | CONFIRMED |
| 5 个 GIFT 商品价格/描述（含 "Gift  X2 RACE CASH" 双空格）；X2 RACE CASH 礼物 249 vs 通行证 329（差 80） | products API | CONFIRMED |
| X2 RACE CASH 通行证 updated 24 Sep，晚于礼物创建 22 Sep 两天 | pass.updated=2026-09-24 | CONFIRMED |
| 比价算术（<2 Mythic、≈4 Rare、5.05 Mythic skip、六/七次回本） | 重算 | CONFIRMED |
| "A new pass has arrived every one to two weeks" | 间隔 14/15/7/7 天；15 天略超 | 轻微不准（见修改清单 M5） |

### eggs.md
| 命题 | 证据 | 结果 |
|---|---|---|
| 七档蛋价、跳过价（9/19/39/59/79/99）、礼物蛋价全表 | products API | CONFIRMED |
| 2.8×/4.3×/3.2×/1.4×/2.9× 比率；Starter Pack 118 | 重算 | CONFIRMED |
| Buy Common Egg 描述 "Buy an uncommon egg" | API Description | CONFIRMED |
| 徽章/蛋日期阶梯（6 Jul、22 Aug、23 Sep；28 Jul、12 Aug、24 Aug、22 Sep） | created | CONFIRMED |
| Restock Shop! 59；Starter Pack 描述 | API | CONFIRMED |

### updates.md
时间线表 20 行逐行对 created 日期 → 全部 CONFIRMED（5 个种族徽章 12 Aug；22 Aug 六徽章；26 Aug 五徽章；27 Aug 四个 skip；9/10 三项；9/22 礼物含"四个当时在售通行证"；9/29 Skip Hatch (Exotic)）。"roughly a month apart"（8/22→9/23=32 天）CONFIRMED。"updated 30 Sep 09:40 UTC" CONFIRMED。"[NEW🎉] 第三方追踪站" CONFIRMED（rblxscripts.net 标题 "[NEW🎉] Race Horses Scripts"；未给 URL，见 M7）。

### races.md / horses.md / care-stable.md / how-to-play.md / guides.md
- 描述原话引用（"A new race every minute"、"All horses have a random chance…"、"Upgrade your stable to earn faster"、"no two horses match"、"ultra-rare 1-in-[X] traits and shiny variants"、"Care for your horses for extra XP bonus"）全部逐字一致 → CONFIRMED。
- 商品/通行证原话（Re-roll、Restock Trees、Golden Apple "Skips full cooldown + 1 Level Up!"、X2 FRUIT CAPACITY、X3 STORAGE 9→27、Double Race Earnings 59、Double Offline Earnings 39 无描述）→ CONFIRMED。
- Secret Victory 76,676、To Race Another Day 1,277,129、Apple A Day 903,613、Full House 14,160、So Long 2,168 均 ≤ 实时且标 1 Oct → CONFIRMED（快照）。
- 图片说明：th1（橙色马、鞍号 1、看台）、th2（E FEED 红苹果）、th3（E CLEAN 海绵+水桶+泥点）、icon（橙马+书）—— 我亲眼核对 media API 的 3 张图+图标，描述准确 → CONFIRMED。"三张官方图中两张展示照料" CONFIRMED。
- 群成员 883,107（1 Oct 快照；实时 883,463）→ CONFIRMED（快照）。
- how-to-play 七步表逐字 → CONFIRMED；"Price Free" → price=null → CONFIRMED。
- guides.md："Eight guides" 数量与链接 CONFIRMED。

### entities.json（程序化全量）
24 徽章名称/描述逐字、32 商品价格/日期/ProductId、5 通行证价格/描述全部与实时 API 一致；仅 2 处描述为规范化空白（Re-roll Horse! 的 \r\n→空格；Double Offline Earnings 空描述记为 None）→ 无错。徽章 awarded_count 与 badges.md 全部对得上；per-100 一致。entities 的 unverified_fields 与页面 hedge 一致。

## 四、不验/其他
- author.md 中 `{{BRAND}}` 模板变量未替换（description 与正文）。若构建期会替换则无事，否则会直接显示。已列入清单。
- B 级「操作建议类」（先买哪个通行证、徽章顺序）为意见，页内均标 "our view"，不计入验证。
