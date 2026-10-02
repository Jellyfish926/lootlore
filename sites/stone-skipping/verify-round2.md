# 第 2 轮复验（取证 2026-10-02 约 12:20 UTC 起，自己重新联网）
## 统计
复验 70 条：CONFIRMED 65 / REFUTED 2 / UNVERIFIED 3。
- A 清单 21 条（R1-R4、U1-U14、X1、X2、social-media-links 引语）：19 通过；U13（11:19 时点数）、U14（模板标签）按原因仍 UNVERIFIED。
- B 新增活动事实 30 条全通过，另 2 条来源 URL 不符（REFUTED）。
- D/E 16 条全通过。boosts.md 新增 1 条推断句 UNVERIFIED。

## 取证
- 默认路 /virtual-events 我请求 6 次 + limit=10/50 + eventStatus=completed/active/ended，始终只回 1 条（ADMIN ABUSE + WORLD 5）。
- 游标路 ?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA（universeId 10765298801）稳定返回 3 条，翻 previous 游标可回溯，共 3 条，无 World 2：
  - "World 3 + New Content"：listed 2026-09-15T14:32:14Z；starts 2026-09-20T18:00:01Z；ends 2026-09-23T18:00:01Z；subtitle "World 3 + New Content"，description 空
  - "WORLD 4 + UPDATE"：listed 2026-09-22T11:53:59Z；starts 2026-09-27T16:00:56Z；ends 2026-10-01T16:00:56Z；subtitle "CLICK TO NOTIFY!"，description 空
  - "ADMIN ABUSE + WORLD 5"：listed 2026-09-26T09:04:02Z；2026-10-03T16:00:15Z–18:00:15Z
  标题大小写、listed/starts/ends 逐个与页面一致；「No event listing names World 2」成立；蛋创建日与活动关系成立（Astronaut 9-19 对 9-20，Chocolatier 9-26 对 9-27，Dragon 10-1 对 10-3）；updates 时间线 15/20/22/26/27 Sep 行成立。
- 引语核对：https://create.roblox.com/docs/production/promotion/social-media-links 正文 "Social media links are only visible to users who have verified their age as at least 16 years old." 作者引的 "are only visible to users who have verified their age as at least 16 years old" 逐字一致。boosts.md 新引的 "an item or ability that a user can purchase more than once"、"a one-time Robux fee" 也逐字（developer-products 页、passes 页）。

## 仍有问题的条目
| 编号 | 文件 | 现句 | 问题 | 证据 | 改成什么 |
|---|---|---|---|---|---|
| N1 REFUTED | updates.md frontmatter sourceUrls | ".../virtual-events?eventStatus=completed" | 该 URL 并不返回过往活动，只回 1 条 ADMIN ABUSE + WORLD 5，不能作为 World 3 / World 4 的出处 | 我请求 eventStatus=completed / ended / active、limit=50 均只 1 条；能取到 3 条的是游标路 | 换成 https://apis.roblox.com/virtual-events/v1/universes/10765298801/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA |
| N2 REFUTED | entities.json event-admin-abuse-world-5 的 source_urls 与 key_notes_source | 同上 eventStatus=completed；key_notes_source 为 ?limit=50 | key_notes_en 含 World 3 / WORLD 4 日期，但引的两个 URL 都取不到这两条 | 同 N1 | key_notes_source 与 source_urls 补/换为上述游标 URL |
| N3 UNVERIFIED | boosts.md "Are the Wins multipliers really permanent?" | "So a developer product is permanent only if the game saves it that way. The tag is the developer's promise, not a platform rule." | 两句引语逐字属实，但这一推论文档里没有 | 引语页只写 "purchase more than once" / "one-time Robux fee" | "The tag is the developer's wording; the listing does not say how the game stores the purchase." |
| U13 UNVERIFIED（沿用） | community.md tldr 及表格、index.md | 481,097 members at 11:19 UTC 等时点数 | 无法回溯（11:50 实测 484,476 等） | 同第 1 轮 | 可发布，留存原始响应即可 |
| U14 UNVERIFIED（沿用） | author.md | "Every guide published under that byline is listed below." | 依赖渲染模板 | lootlore 同模板 | 构建后核渲染产物 |

## A 清单核对结果
R1、R2、R3、R4（_note 改为如实披露：Getting Started 内互不重复；robux 与 pets 共用 art02 属已披露保留项，pages 映射与 _note 自洽）、U1-U12、X1、X2 均已改到位。全目录 grep 旧句关键短语（"covers content, not spending"、"switched off"、"only to logged-in users"、"once per account"、"costs you nothing"、"usually resets progress"、"usually means developers"、"has not published patch notes"、"adds World 5"、"skip to world"、"同栏目内不重复"、"themed strip of water"、"shout is where many"、"usually points to rarer"）在 content/en 与 json 中无残留；"skip to world" 现仅出现在 updates 新的带 hedge 写法里。entities.json 中不再有 "Private servers not allowed" 的实体陈述（只有 sources_note 的中文修订记录提到它被删）。

## D/E
- updates description 157（140-160 ✓）；11 页首段 49–57 词（community 57 ✓）；title 49–55、站内链接 ≥4 且目标存在、日期与署名不变、draft 全 false。
- _images.json pages 映射与 _note 自洽；beginner frontmatter images ["art04","art01"] 与映射 art04 同步。
- entities 89 条与接口 0 差异。
- 红线扫描：全目录无任何兑换码字符串；无第三方站的 zone 名、概率、域名等内容搬运。

## 逐页结论
| 页 | 结论 |
|---|---|
| index、beginner、shop、robux、pets、gamepasses、how-to-play、community、author | 可发布（community 与 author 仅带 U13/U14，不阻塞） |
| boosts | 改掉 N3 后发布（单句，改完即可，不影响其他页） |
| updates | 改 N1 的 sourceUrls 后发布；须在 2026-10-03 16:00 UTC 前上线，10-04 改过去时 |
| entities.json | 改 N2 后可接入 |
