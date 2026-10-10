# Phasmophobia round3 复验（2026-10-10 13:0x UTC，证据今天自取）

## 统计
- 复验 18 条：fix2.md 16 行 + entities.json 的 crimson-eye-2026、drop-crimson-eye-tee 两个实体。通过 18，不通过 0。
- 16 行改后句逐字 grep 全部在文件里，改前句 0 处残留。
- 时效：今天再取 ISteamNews（steam_community_announcements）最新帖仍是 2026-10-07 09:01 UTC 的 v0.19.1.0，其后依次为 10/1「The Crimson Eye Approaches Once More」、9/18；官网 kineticgames.co.uk/news 列表最新为 10/6（v0.19.1.0）、10/1。10/7 之后没有新帖，没有任何官方帖确认 Crimson Eye 已开始，所以 announced / scheduled 口径成立。
- 事实核对：改后各句里的日期（10/8–11/1、Twitch Drop 至 10/15 11:59 PM BST、Double XP 10/15–22、Ghost Hunts 4 Hearts 10/26–11/1）与 10/1 公告原文逐字一致；R2-02 括注 "XBOX & Steam only" 与官网 v0.19.1.0 页原文一致，Steam 帖版确实没有该括注。
- 实体：crimson-eye-2026 与 drop-crimson-eye-tee 现为 announced / scheduled 口径，`unverified_fields` 分别为 started_in_game 与 started，口径一致，与页面不再矛盾。
- 全栏目 grep（still open / is live / has started / now live / underway / currently / has begun / kicked off / ongoing / in progress 等，以及带 Crimson Eye / Twitch Drop / Double XP 的 runs / begins / ends / ran / returns 等动词句）：
  - 唯一命中 "still open / currently" 类词的是 platforms-price 引用的 Game Pass 原话，与活动无关。
  - 其余带动词的句子都在引官方原话（"will begin on…"）或已是 announced / scheduled / is due 口径。
  - 没有再把 Crimson Eye 2026 及其 Twitch Drop / Double XP 写成已开始或已发生的句子。
- 新引入的错误：无。新增的引文只有 "XBOX & Steam only"，在官网原文命中。
- 非阻塞备注（不算不通过）：crimson-eye.md 末段 "the patch that shipped the event" 指 10/7 的 v0.19.1.0，该补丁已发布（Steam 10/7）且公告写 "An update containing the event"，成立。

## 不通过清单
无。

## 逐页最终结论
| 页面 | 结论 | 原因 |
|---|---|---|
| index | 可发布 | round1 的 V-19 等已改；活动句均为 announced 口径；价格、版本、日期当天复核一致 |
| getting-started | 可发布 | V-14、V-18 已改且出处补齐；无时态问题 |
| author | 可发布 | `{{BRAND}}` 构建会替换、标签与渲染页一致（仓内证据已核）；无事实性问题 |
| updates-events | 可发布 | 状态表已写 "Announced for"；最新版本与官方最新帖一致 |
| patch-notes | 可发布 | Firelight/Igniter 与 "XBOX & Steam only" 两处差异都已披露；16 个版本日期与 Steam 一致 |
| crimson-eye | 可发布 | 全部活动句改为 announced / scheduled / due；2025 目标列表出处与说明已补；日期与 10/1 公告逐字一致 |
| events | 可发布 | Twitch Drop 标题与末行、Double XP 表、活动表均改为 announced 口径；7 条 Drop 与 4 个 Double XP 窗口逐条核实 |
| roadmap | 可发布 | 两张路线图转录已看图核对；末格收窄后与 6/24 帖 "second half of 2027" 一致 |
| difficulty | 可发布 | 15x 与 Apocalypse 档位已标年份；多人限制已补 2023-01 原话；出处补齐 |
| how-to-play | 可发布 | V-16、V-17 已改；等级门槛与媒体上限逐条对上原帖 |
| platforms-price | 可发布 | 语言数 28、评价口径均已改对（今天再取：28 项；全语言 840,984 条、约 94% 好评） |
| achievements | 可发布 | 54 条名称、描述、百分比与成就页逐字一致；"about ten of the 54" 与披露括注已补 |

结论：12 页全部可发布，无页转 draft。
