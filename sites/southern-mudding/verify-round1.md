# Southern Mudding 对抗验证报告

取证时间 2026-10-02 11:49–11:58 UTC（自行重取，未使用 raw/）。证据副本：`live/`、`docs/`、`img/`，命题台账 `ledger.csv`（393 行，逐条带结果）。
脚本：`build_ledger.py`。被验文件未改动。

## 一、统计

| 项 | 数 |
| --- | --- |
| 命题总数（表格按行、散文按句拆） | 393 |
| A 级 | 354 |
| B 级 | 39（先按种子 20261002 抽 12 条；因出现 REFUTED 全部补验） |
| CONFIRMED | 361 |
| REFUTED | 8 行（合并为 5 个问题，见 F01–F05） |
| UNVERIFIED | 24 行（合并为 14 个问题，见 F06–F19） |

- 转全量的页：index、guides、updates、badges、community（各有 REFUTED），以及 `_images.json`（th1 alt）。其余 7 页仅有 UNVERIFIED，我也通读并核对了全部可由接口核对的行。
- UNVERIFIED 占比 24/393 = 6%，没有取证条件不足的问题。
- 12 页全部：无任何真实车厂/车型品牌名、无兑换码字符串、无占位符残留（author 的 `{{BRAND}}` 是仓内约定，README 写明构建期替换）。

### 通过的大块（接口逐项重数）
- 13 个在售通行证，名称、价格、描述、创建日期一致；合计 3,685（重算）；第 14 条 "Placeholder" 不在售、无价（一致）。无折扣。
- 61 个开发者商品 = 22 辆车 + 22 辆车礼物 + 13 通行证礼物 + 3 龙卷风 + 1 活动解锁；22 辆车 5,213 Robux，200–325；"Limited" 命名 20 个；括号风格 7/11/1/1/2；价格分布、月度计数全部一致；34 个礼物商品与本体同价同日（车辆 22 对）。
- 礼物差价表 13 行（65/50/45/45/40/40/40 更便宜，5 个同价，1 个贵 65）一致。
- 徽章 4 个，名称/描述/创建时间（2 分钟内）/启用状态一致；win rate 字段读数 0.561→56.1% 与 past-day 比值自洽；各比率重算一致。
- 星期统计（12 周五/6 周四/3 周三/1 周二，周五创建全部在 4 月起）一致；时区换算与夏令时日期（英国 10/25、美国 11/1）一致。
- 引号内官方原话（游戏描述 9 处、群组描述、通行证描述 12 条）逐字一致。
- 群组：认证、所有者 SouthernMudHold、公开加入、公开游戏 1、shout 为空、角色 1/1/3/9/2/2 = 18 一致；成熟度 Minimal / Suitable for everyone 一致；社交链接两个接口匿名返回 "Authentication token is missing" 一致。
- `_images.json` 15 个 URL 现在 curl 均 200 image/Png，全部 tr.rbxcdn.com；与缩略图接口一致；活动缩略图 81746768314421 与 th1 同 CDN 哈希；alt 非空、无品牌名。
- entities.json：81/82 实体的名称（strip 后）/价格/创建日/ID/在售标记逐条对接口一致，第 82 条（游戏本体）字段一致；config-snippet 数字一致。

## 二、修改清单（仅 REFUTED 与 UNVERIFIED）

### REFUTED

| 编号 | 文件 | 原句（逐字） | 问题 | 证据 | 改成什么 |
| --- | --- | --- | --- | --- | --- |
| F01 | updates.md（tldr 第 4 条、第 76 行、第 122 行） | tldr: "Older patch notes are not kept on Roblox; we rebuild the history from the dates products and passes were created." / "Roblox's public data keeps no archive of old descriptions, so earlier weekly notes cannot be read there." / "Not on Roblox. The description holds only the current week's notes, and the events data lists only current and upcoming events." | "events 数据只列当前和即将到来的活动" 不成立。给 virtual-events 接口加 `eventStatus` 参数后返回完整历史：43 条活动，2025-12-12 "Towing Update" 到 2026-10-09 "Next Week's Update!"，几乎每周一条，标题就是当周更新名（如 "🗺️ Map Expansion!" 2026-05-15、"Lift Kits!" 2026-03-06、"Engine Swaps!🛠️" 2026-06-26、"Tornado Chaser Upd!" 2026-07-31）。不带参数只返回 3 条，所以作者看到 3 条。 | `https://apis.roblox.com/virtual-events/v1/universes/8719555347/virtual-events?eventStatus=completed`（再用返回的 nextPageCursor 翻第 2 页，共 24+19=43 条）；存档 `live/ev_all.json` | tldr 改：`"Roblox keeps only the current description, but the developer's event listings name each week's update: the events API lists 43 of them, from \"Towing Update\" (12 Dec 2025) to \"Next Week's Update!\" (9 Oct 2026)."` 正文第 122 行改：`The description holds only the current week's notes. The developer's event listings keep a title for each weekly update back to 12 December 2025 (for example "🗺️ Map Expansion!" on 15 May 2026 and "Engine Swaps!🛠️" on 26 June 2026), but not the full notes.` 第 76 行 "keeps no archive of old descriptions" 保留可以，后半句加 "though event titles survive". 建议另加一节用 43 条标题补全更新史（含 Map Expansion、Towing、Boat、Motorcycle 等免费内容）。 |
| F02 | index.md 第 89 行；guides.md 第 27 行；updates.md 第 32 行 | index/guides: "…61 developer products and three event listings" / "…61 developer products, three event listings and the group page"；updates: "About 17:00 UTC, going by the three event listings the developer had on Roblox:" | "three event listings" 是只读了默认接口的结果；开发者实际有 43 条。updates 里的 "about 17:00 UTC, going by three listings" 证据面太窄：41 条周五开始的列表里，17:00–17:29 只有 20 条，17:30 起 3 条，18:00–18:29 14 条，18:30 起 1 条，19:30+ 3 条（如 2026-06-26 19:45、2026-09-04 18:00:57）。近 10 周中 9 周在 17:00–17:15。 | 同 F01，`live/ev_all.json` | index/guides 改 "…61 developer products, the developer's weekly event listings and the group page"；updates 第 32 行改：`Recent Friday event listings mostly start at 17:00 UTC (9 of the last 10), though some weeks start at 17:30 or 18:00; the three currently open listings are:`（该表仍可只列这三条）。 |
| F03 | community.md 第 90 行、第 108 行；index.md 第 81 行；updates.md 第 122 行；community scope | "The safe way to find it is from inside Roblox. Sign in, open the Southern Mudding game page or the group page, and use the social links shown there. Roblox displays those links only on the pages the developer controls, so a link found there is the developer's own." / 表格 "Game and group social links \| Roblox login required" / "need a sign-in" | 只说"登录"不对：Creator Docs 写明社交链接仅对完成年龄验证且 16 岁以上的用户可见；未验证或 16 岁以下登录后也看不到。"仅显示在开发者控制的页面" 文档原话是只允许分享在游戏主详情页。读者按文中步骤做会找不到却以为官方没有。 | https://create.roblox.com/docs/en-us/production/promotion/social-media-links.md ："Social media links are only visible to users who have verified their age as at least 16 years old." 另：匿名请求两个 social-links 接口返回 401 "Authentication token is missing"（这一点属实） | 改：`Roblox shows social links on a game's or group's page only to signed-in users who have verified their age as 16 or older, so we could not read them. If you meet that condition, check the Southern Mudding game page or group page; a link listed there is the developer's own. We do not publish an invite we could not trace to those pages.` 表格改 "Age-verified (16+) Roblox login required"；index/updates/scope 里 "need a sign-in" 同步改 "need an age-verified sign-in". |
| F04 | badges.md 第 93 行 | "A badge is awarded once per account, while a visit is counted every time someone joins, so the ratio of about 5.6 visits per Welcome badge points to players coming back." | "每账号一次" 说得太绝对：官方 BadgeService 文档写明发放条件是玩家当前没有该徽章，且玩家可在个人资料删除后被再次发放。"每次加入都计一次访问" 未找到官方出处（见 F20）。 | https://create.roblox.com/docs/en-us/reference/engine/classes/BadgeService.md ："The player must not already have the badge (note that a player may delete an awarded badge from their profile and be awarded the badge again)." | `A badge is normally awarded to an account once (Roblox's documentation says a player who already has it cannot be awarded it again), so Welcome to the game! counts roughly one award per account, while the visit count is a different measure. The gap of about 5.6 visits per Welcome badge is consistent with players coming back, but the visit definition is not published in the sources we read.` |
| F05 | index.md、nitrous.md 正文 alt；`_images.json` th1.alt | "Promotional art: a red pickup truck with a black hood stripe climbs a rutted mud track…" | 图里是黑色引擎盖上带红色条纹，不是"红车 + 黑色盖上条纹"这种读法；描述颠倒。 | 看图 `img/th1_src.png`（https://tr.rbxcdn.com/180DAY-6184923f287760b4ae77a8b1aed4c1d7/768/432/Image/Png/noFilter） | 改 "a red pickup truck with a black hood and a red stripe climbs a rutted mud track…"（_images.json 与两页正文 alt 同步）。 |

### UNVERIFIED

| 编号 | 文件 | 原句（逐字） | 问题 | 证据 | 改成什么 |
| --- | --- | --- | --- | --- | --- |
| F06 | updates.md seoTitle/description/第 32 行 | seoTitle "Southern Mudding Update Time: Fridays, About 17:00 UTC"；description "…every Friday at about 17:00 UTC per its Roblox event listings…" | 活动开始时间 ≠ 实际更新时间。能实测的实际更新只有 1 次：游戏 updated=2026-09-25T17:20:11Z。"每个周五约 17:00" 是泛化。近 10 周活动 9 条在 17:00–17:15，但历史上多次 18:00–19:45。 | `live/ev_all.json`；games API `updated` | description 改：`When Southern Mudding updates: Fridays, with Roblox event listings that usually start at 17:00 UTC, what the 25 September notes added, and a dated history since 2025.`（保持 140–160 字符需再核长度）；seoTitle 可保留 "Fridays, Usually 17:00 UTC"。正文加一句：`The one release we could time from the game listing, 25 September, landed at 17:20 UTC.` |
| F07 | updates.md 第 59 行 | "Servers that were already running keep the old version until they close; that is how Roblox works in general." | 无官方出处。Creator Docs 发布页只写"如果游戏在线，建议重启服务器（restart its servers）"，未写"旧服务器保留旧版本"。 | https://create.roblox.com/docs/production/publishing/publish-experiences-and-places ："OPTIONAL If the game is live, it's recommended that you restart its servers." | 改：`Roblox's publishing guide recommends that developers restart servers after publishing a live game, so a server that was already running may still be on the old version. If the notes have changed but your game has not, join a fresh server.` 或删除第一句。 |
| F08 | limiteds.md 第 62 行 | "In practice a Roblox developer can stop offering a product inside the game without changing that flag, simply by removing the button." | 无官方出处（官方文档只说明 `IsForSale` 是商品信息字段，并用它判断能否购买）。 | https://create.roblox.com/docs/en-us/production/monetization/developer-products ：示例 "Checks if product is for sale … productInfo.IsForSale" | 改：`The flag belongs to the Roblox product record. Whether the in-game shop still shows an older Limited is controlled by the game itself and is not visible in public data, so the flag is a necessary condition, not proof.` |
| F09 | gamepasses.md 第 62 行 | "A game pass is a one-time purchase that stays on your Roblox account; that is standard Roblox behaviour, not something specific to this game." | "一次性" 有出处；"stays on your account" 官方原文未写。 | https://create.roblox.com/docs/en-us/production/monetization/passes ："let you charge users a one-time Robux fee to access special privileges … a permanent power-up." | 改：`Roblox's Creator Docs describe a game pass as "a one-time Robux fee" for a permanent privilege in the experience.` |
| F10 | gamepasses.md tldr 第 3 条；spawning.md 成本表 "Gift product Robux" 列 | "Every pass has a matching gift product, and seven of those gifts are listed 40 to 65 Robux below the pass price." | 第 13 个"礼物"（商品 "Deluxe Trailer Pack"，名称不含 Gift）是页面自己正文承认的推断。tldr 与 spawning 表把它写成确定。 | `live/dp1.json`：ProductId 3412339155 "Deluxe Trailer Pack" 200，Description 为空 | tldr 改：`Twelve passes have a product named as their gift, and a thirteenth product, "Deluxe Trailer Pack", is probably the gift for the pass of the same name; seven of the gifts are listed 40 to 65 Robux below the pass price.` spawning 表该行 "200" 后加 "(probable gift)". |
| F11 | spawning.md 第 57 行 | "\| Gooseneck Camper \| "(Limited Special Offer) Gooseneck Camper + Truck" \| Developer product, 325 Robux, with a truck \|" 位于 "Which trailers are named in official data?" 表 | 商品名只有 "Gooseneck Camper + Truck"，描述为空，数据没说它是拖车。 | `live/dp1.json` ProductId 3487035699，Description "" | 删除该行；或在表后加：`The product "(Limited Special Offer) Gooseneck Camper + Truck" (325 Robux) includes a camper; the data does not say whether it is a trailer.` |
| F12 | spawning.md 第 71 行 | "By that measure, towing is something most active players try." | 徽章是历史累计，非"活跃玩家"；59/100 是 Spawned a Trailer 对 Spawned a Vehicle 的累计比，不能推出"多数活跃玩家"。 | badges API：37,092,072 / 62,452,273 = 59.4% | 改：`By that measure, about 59 accounts have spawned a trailer for every 100 that have spawned a vehicle, so towing is common, though the badge totals do not tell us how many of today's players do it.` |
| F13 | spawning.md description、第 94 行；guides.md 第 41 行；badges.md 第 47 行 | spawning description "…2 vehicles and 2 trailers by default…"；"**You are new:** none yet. Two vehicles and two trailers cover the first sessions…"；guides "The default of two vehicles and two trailers…"；badges "explains the default limit of two" | 默认值 2/2 是从两个 Spawn 4 通行证描述反推的（正文已 hedge，但这四处未带"据通行证描述"）。 | game-passes API：描述 "Increases vehicle spawn limit from 2 to 4!"、"Increases trailer spawn limit from 2 to 4!" | spawning description 改 "…2 vehicles and 2 trailers by default according to the pass descriptions…"（核长度）；第 94 行改 `Two vehicles and two trailers, going by the pass descriptions, should cover the first sessions…`；guides 改 "The default of two vehicles and two trailers, as implied by the pass descriptions, …"；badges 改 "explains the default limit of two that the pass descriptions imply". |
| F14 | community.md 第 100 行 | "Third-party scripts break Roblox's rules, can cost you the account, and are a common way to deliver malware." | "违反规则" 有出处；"可能失去账号""常见恶意软件来源"无官方出处（Terms 页 403 取不到）。 | https://about.roblox.com/community-standards ："Roblox doesn't allow cheating, exploits… Using or sharing exploits to help yourself or others gain an unfair advantage anywhere on the platform" | 改：`Roblox's Community Standards say it does not allow "Using or sharing exploits to help yourself or others gain an unfair advantage anywhere on the platform". Everything the guides on this site describe can be done with the normal game client.` |
| F15 | community.md 第 106 行 | "\| Group wall \| Not available to anonymous readers \| Announcements, player questions \|" | 实测 wall 接口返回 404 NotFound（空错误体），不是鉴权错误，无法证明"匿名不可读"。 | `https://groups.roblox.com/v2/groups/33504096/wall/posts?limit=10` → 404 `{"errors":[{"code":0,"message":""}]}`；v1 路径 404 "NotFound" | 第二列改 "Public endpoint returned 404 when we asked". |
| F16 | community.md 第 51 行 | "If it does not appear, leave and rejoin; many Roblox games only check group membership when you enter. That last sentence is general experience, not a confirmed rule here." | 已自标为经验，无出处。 | 无 | 保留需标成 hedge（现状已满足）；稳妥做法删除 "many Roblox games only check group membership when you enter" 一句，改 "If it does not appear, try rejoining the server."（也是未证实，但不再给出理由）。 |
| F17 | badges.md 第 39 行 | "The win rate is a figure Roblox computes itself from recent play and attaches to each badge; we quote it as given, converted to a percentage." | 数值读法自洽（0.561→56.1%，past-day 比值 11.6% 与 0.065/0.561 一致），但没找到官方文档对 winRatePercentage 的定义，"来自近期游玩" 是未证实说法。 | `live/badges.json`；Creator Docs badges 页无该字段说明 | 改：`The win rate is the winRatePercentage field Roblox returns with each badge; it is a fraction, so 0.561 reads as 56.1%. Roblox's Creator Docs do not define how it is calculated, so we quote it as given.` |
| F18 | vehicles.md 第 88–89 行 | "**Pickup trucks get the most attention.** They are named first in the description, they received nitrous on 25 September, and six of the 22 Robux vehicles are 6x6 pickup trucks." / "**Trailers matter as much as trucks.**" | 列在 "What the official data supports" 下，实为编辑判断。 | 数据只支持三个事实：描述里 pickup 排第一、nitrous 限 pickup、6 个商品名含 6x6 pickup | 第一条改 `Pickup trucks come up often.`；删除 "Trailers matter as much as trucks."，或改为 "The description names towing, hauling and boating, and the spawning guide covers the trailer passes." |
| F19 | `_images.json` th5.alt；spawning.md 图注 | "…a red pickup truck backs a multi-axle trailer down a ramp into the water, carrying a large red and white speedboat with four outboard engines" / 图注 "launching a boat from a trailer" | 图中可见皮卡在前方拖着载船拖车靠近水边，看不出"倒车下坡道"或"下水"。 | `img/th5_src.png` | alt 改 "a red pickup truck tows a multi-axle trailer carrying a large red and white speedboat with four outboard engines to the water's edge"；图注改 "towing a boat on a trailer". |

## 三、已过时清单（作者取数 11:19–11:23 UTC，我取数 11:49–11:58 UTC；非作者错误）

| 项 | 页面写的 | 现值（取数时间） | 涉及页 |
| --- | --- | --- | --- |
| 访问量 | 428,075,692（badges）/ "428 million" | 428,122,284（11:58Z） | badges, index |
| 收藏 | 625,025 | 625,081 | index |
| 点赞/点踩 | 221,349 / 17,627 | 221,360 / 17,628 | index |
| 在线人数 | 14,526 | 15,534 | index |
| 群组成员 | 649,071 | 649,127 | community, how-to-play, nitrous, entities |
| 徽章累计 | 76,022,926 / 62,448,163 / 37,089,920 / 7,164,284 | 76,027,977 / 62,452,273 / 37,092,072 / 7,164,825（11:49Z） | badges, spawning, entities（past-day 值未变） |
| 对应比率 | 82.1 / 48.8 / 9.4；59% | 82.1 / 48.8 / 9.4；59.4%（不变） | — |
| RSVP "going" | 43,785 / 8,044（Nitrous 67,491 / 10,758 未变） | 43,914 / 8,076；not going 5,335 / 606 | updates, community, entities |
| 通行证数/价格、商品数/价格、描述、版本 | 13 在售+1 Placeholder，3,685；61 商品；描述 "September 25th Update"；updated 2026-09-25T17:20:11Z | 11:58Z 全部相同 | — |

提示：今天（周五）约 17:00 UTC 会落地新版本（"This Week's Update!" 列表 2026-10-02T17:00:46Z 开始）。上线前必须重取：游戏描述的更新说明与标题前缀、updated 时间戳、通行证/商品数量与价格、活动列表（新事件标题）、各徽章计数；之后所有页的 "25 September" 叙述、gameVersion 字段与"read before that day's update"措辞都要改。

## 四、结构 / SEO / 图片

| 检查 | 结果 |
| --- | --- |
| title 40–60 字符 | 12 页均 53–59，通过 |
| description 140–160 | 11 页 155–160 通过；author.md 原文 161（含 `{{BRAND}}`），仓 hub.json 的 brand 为 "LootWiki"（8 字符，替换后 160）通过，但换站名会超 |
| 首段 40–60 词 | 12 页 45–60；community 恰为 60（边界，改一个词即超），其余通过 |
| 站内链接 ≥3 且目标存在 | 全部通过（最少 badges、community 各 3 个）；author.md 链 `/contact`：本目录无此页，仓内 `repos/lootlore/hub/pages/contact.html` 存在，上线构建后需实测 200 |
| date / updated / reviewed = 2026-10-02；署名 Jellyfi | 12 页全部通过 |
| 品牌名 / 兑换码 | 全部 12 页 + entities + _images + config-snippet 均为 0 |
| 图片 URL | 15/15 现取 200 image/Png，tr.rbxcdn.com；与缩略图接口一致 |
| alt | 非空、无品牌名；F05（th1）、F19（th5）两处描述偏差 |
| 图片尺寸 | 最大 768×432，低于 Discover 1200 宽要求（_images.json 已自述） |
| 图片 URL 时效 | 180DAY 前缀 CDN 缓存期，需定期刷新（_images.json 已自述） |

## 五、发布建议（问题修完前保持 draft）

| 页 | 建议 | 理由 |
| --- | --- | --- |
| updates | draft | F01、F02 是事实错误（"只有 3 条活动 / 旧记录不在 Roblox"），整页"历史"章节需据 43 条活动重写；F06/F07 需 hedge；且 17:00 UTC 后整页数据已过期 |
| community | draft | F03 的操作指引会让读者找不到链接；F14 无出处的安全断言 |
| badges | draft | F04 平台规则表述绝对；F17 win rate 定义无出处；计数已过时 |
| index、guides | draft（随 updates） | F02 "three event listings"；index 含 F03；index 数据已过时 |
| spawning | draft | F10/F11/F12/F13 四处推断写成确认 |
| gamepasses、limiteds、vehicles | 改完 F08/F09/F10/F13/F18 后可发 | 数字全部通过，仅是措辞需 hedge |
| nitrous、how-to-play、author | 可在重取今天更新数据后发 | 无 REFUTED；nitrous 需随今日更新改写；`_images.json` F05/F19 随改 |

另：作者说明"这批站点上线 17:00 UTC 后数据即变"，建议今天 17:30 UTC 之后重取一次再统一发布，避免整批页面在发布当天就写着 "25 September update" 为最新版。
