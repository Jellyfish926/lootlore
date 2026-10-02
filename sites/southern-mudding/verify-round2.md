# Southern Mudding 第 2 轮复验

取证 2026-10-02 12:20–12:35 UTC。改动范围以 diff（现文件 vs `raw/en_round1_backup/`）为准，12 页全部 diff 通读，作者表没列的改动（badges 房屋表新增行、how-to-play 位置行、guides/index 的时点句等）也已核。证据在 `r2/`（ev_fresh.json、docs 原页、检查脚本输出）。

## 统计
复验 218 条（A 级 209、B 级 9）：CONFIRMED 215，REFUTED 0，UNVERIFIED 3。

## 活动接口可复现路径
我 11:49 UTC 不带参数的请求只回 3 条；12:32 UTC 再测，下列五种请求全部返回同样的第一页 24 条，翻 nextPageCursor（id_2zwAAAZ6YusqKzyVxK9IiggIy）得第二页 19 条，共 43 条，与我第 1 轮存档逐条一致（id、时间、标题、描述）：
1. 不带参数
2. `?eventStatus=completed`
3. `?limit=100`
4. `?eventStatus=completed&limit=100`
5. 作者的 `?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA`（也回第一页 24 条）

结论：接口行为随时间变过（我 11:49 不带参数时只有 3 条），现在 5 条路都能复现；作者引用的 cursor 路径可用。

## A. F01–F19 落实
全目录（正文、entities、_images、config-snippet）grep 旧句关键短语："three event listings"、"only current and upcoming"、"About 17:00"、"once per account"、"black hood stripe"、"removing the button"、"stays on your Roblox account"、"most active players"、"common way to deliver malware"、"backs a multi-axle trailer"、"launching a boat"、"Sign in, open"、"only check group membership"、"Every pass has a matching" 等，残留 0。F01–F19 逐条已改到位且替换句与证据一致，结果全 CONFIRMED。F16 之外无新增 hedge 缺口。

## B. 43 条活动相关
- updates.md 43 行表（日期、周几、标题含 emoji、UTC 开始时间）逐行对 ev_fresh.json：0 处不一致；标题无首尾空格。
- 周五开始 41 条，例外 2 条为 2025-12-23（周二，Winter Update Pt. 2，18:50）和 2025-12-31（周三，🎆 New Years Update，18:00）；2026-01-09 到 2026-10-09 间隔均为 7 天，共 40 条：属实。
- 分布 17:00–17:29 20、17:30–17:59 3、18:00–18:29 14、18:30–18:59 1、19:30 起 3：属实。
- 近 10 条（含 10-02、10-09 两条未开始）9 条在 17:00–17:15，例外 9 月 4 日 18:00:57：属实。
- 1 月 9 日至 2 月 20 日 7 条周五全部 18:00（秒数 18:00:00–18:00:20）：属实；"冬令时可能改到 18:00" 已显式写 "our inference… developer has not said so"：合格。
- 描述分类：34 条仅标准句；3 条变体（Police Update "…police update releases!"、Storm Chasing Update! 少了感叹号、License Plates+New ATVs "…is dropped!"）；6 条有更多内容（Towing、New Years、Chassis Cab、Trucking Event!、Lift Kits!、ATVs Update!）：属实，6 条描述逐字一致（Trucking 与 ATVs 含标准句，页面已注明）。
- "none of the 41 earlier listings carries a placeholder title"：属实（仅两条 This/Next Week's Update!）。
- 关联句核两边日期，全部属实：Tire Customization! 2-06；Lift Kits! 3-06 与描述；🔧Tires + Rock Lights!🔧 4-10 17:00，Rock Lights Customization 通行证 4-10 16:24 创建（同日）；Engine Swaps!🛠️ 6-26；License Plates+New ATVs 7-10；Storm Chasing Update! 4-03，龙卷风商品 4-01 创建（早两天）；📡Tornado Chaser Upd!🌪️ 7-31 与 Storm Chaser Vehicle 7-31 创建；Trucking Event! 2-13 至 2-20，subtitle "SM's First Event!"，描述 "Deliver cargo to unlock a new truck."，Delivery Event Unlock Now 2-12 创建（前一天）；Dirtbike 1-30、Lawn Mower 2-20、Boat 2-27、ATVs 3-13；Tiny Home Trailers! 6-05；🚐Stacker Trailer!🚐 8-07；Bed Cargo + Houses! 5-29；Nitrous Update 列表 9-11 创建。
- 由日期推出的因果均已标注：Delivery Event Unlock Now 写 "likely a paid shortcut… our inference from the dates"；Engine Swaps/License Plates 写 "sound like tuning features… no official text calls them customization"；Storm Chaser、Rock Lights 仅陈述同日，未写成因果。

## C. 官方引语逐字（打开原页）
- update-experiences："players aren't immediately removed from old versions"、"as the servers running old versions eventually empty and shut down"：逐字一致（原句 "If you don't restart servers, players transition… as the servers running old versions eventually empty and shut down"）。
- social-media-links 的 16 岁句、experience-events 的 "will receive stream notifications in their Roblox inbox when the event starts"（及 Notify Me）、BadgeService "The player must not already have the badge"、passes "a one-time Robux fee"、Community Standards "Using or sharing exploits to help yourself or others gain an unfair advantage anywhere on the platform"：均逐字一致。

## D. 改动后重核
- 长度（title/seoTitle/description/首段词数）：title 53–59、seoTitle 50–59、description 全部 156–160（updates 160、community 160、nitrous 160、how-to-play 160、guides 160，边界但达标）；spawning 158、author 156（含 `{{BRAND}}`，替换为 LootWiki 后 155）；首段 45–60，badges 因加了时点句现为 60 词，处在上限，再加一词即超。
- 站内链接 ≥3 且目标存在、date/updated/reviewed=2026-10-02、署名 Jellyfi：12 页全部通过。
- 把 25 September 称为最新/当前的句子：index、updates、nitrous、badges、guides、limiteds 均带 "as of 2 October 2026, before that day's update" 或具体时点（11:19–11:23 UTC）；无遗漏。
- entities.json 活动实体 43 条（我全对，不止抽 10）：名称、开始/结束时间、event_id、subtitle、description、"Listed" 日期与接口 0 处不一致；page_slug 全部存在。
- `_images.json` th1 alt 已为 "…a black hood and a red stripe…"，th5 alt 已为 "…tows a multi-axle trailer … to the water's edge"；4 个 URL（th1/th5 的 768 与 480）现取均 200。

## E. 红线
全目录（12 页、entities、_images、config-snippet）无真实车厂/车型品牌名，无兑换码字符串。43 个活动的标题、副标题、描述也扫过：0 个真实品牌名（含 "Chassis Cab"、"Military Vehicles"、"Wrecker"、"Show Trucks" 等均为通用词）。

## 仍有问题的条目

| 编号 | 文件 | 现句 | 问题 | 证据 | 改成什么 |
| --- | --- | --- | --- | --- | --- |
| G1（UNVERIFIED） | vehicles.md 第 "What do the official images show…" 节 | "…but the developer's event listings include "Dirtbike Update" (30 January 2026), "Lawn Mower Update" (20 February 2026), "Boat Update" (27 February 2026) and "ATVs Update!" (13 March 2026), so the roster is wider than the store." | 活动标题只显示更新主题，没写新增了可驾驶车辆；"so the roster is wider than the store" 是推断写成确认（ATVs 描述 "Introducing many new ATVs and UTVs" 支持 ATV，其余三条只有标题）。 | `r2/ev_fresh.json`：Dirtbike/Lawn Mower/Boat 三条 description 均为标准句 | 改成 `…"Boat Update" (27 February 2026) and "ATVs Update!" (13 March 2026), which suggests the roster is wider than the store; the ATVs listing says "Introducing many new ATVs and UTVs".` |
| G2（UNVERIFIED） | community.md 表格 | "\| Discord server \| Login required \| Patch notes, sneak peeks, any codes \|" | 与 scope 里 "a Discord server needs an account" 不一致，且我们并不知道有官方 Discord 邀请，原因其实是"没有可追溯的链接"。 | 同页 "We could not confirm one from public data"；Discord 本身可无 Roblox 登录 | 第二列改 "No invite we could trace to an official page". |
| G3（UNVERIFIED，轻） | updates.md | "Roblox's public data keeps no archive of old descriptions, so earlier weekly notes cannot be read there, though the event titles survive." | 否定式全称，无法证明；只能说"我们没找到"。 | 无（只能证明现行接口只回当前描述） | 改 "We found no archive of old descriptions in Roblox's public data, so earlier weekly notes could not be read there, though the event titles survive." |

另记两点（非错误）：badges.md 首段正好 60 词；updates/community/nitrous/how-to-play/guides 的 description 正好 160 字符。后续任何改动都要重量。

## 逐页结论

| 页 | 结论 | 理由 |
| --- | --- | --- |
| updates | 可发布（今天 17:00 UTC 之前，G3 顺手改） | 43 行表与全部统计属实；F01/F02/F06/F07 已落实 |
| community | 可发布（改 G2） | F03/F14/F15/F16 已落实，引语逐字属实 |
| badges | 可发布 | F04/F17 已落实；首段词数在上限 |
| index、guides | 可发布 | F02 已落实，时点限定齐全 |
| spawning | 可发布 | F10–F13、F19 已落实 |
| gamepasses、limiteds | 可发布 | F08–F10 已落实；新增关联句均核实且标注推断 |
| vehicles | 改 G1 后发布 | 唯一的推断写成确认 |
| nitrous、how-to-play、author | 可发布 | 无问题 |

共同前提：今天约 17:00 UTC 新版本落地后，描述、updated 时间戳、活动列表、徽章/成员/RSVP 计数都会变；若在 17:00 UTC 之后才发布，需先重取一次并更新各页的 "25 September 为最新" 叙述。若在其前发布，所有时点限定句仍然成立。
