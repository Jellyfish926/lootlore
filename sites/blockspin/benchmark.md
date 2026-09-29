# 同类站架构对比（BlockSpin，2026-09-29 抓取）

结论：对手分两类——「兑换码单页」（Pocket Gamer / Pocket Tactics / Roblox Den，更新勤、全是码表）和「价值表工具站」（blockspinvalues.com，Google 表驱动）。**没有一家有可信的机制 wiki**（Fandom 主页还是模板字、2025 年后没人编辑）。我们的栏目按「codes 页 + 新手/规则页先上、机制页等一手核实再翻正」做，不跟 values 站拼价值表。

## 对比表

| 站 | 抓取状态 | 页型 | 栏目/导航 | 表格/信息框 | 更新频率（页面自报） | 值得学的 | 不学的 |
|---|---|---|---|---|---|---|---|
| blockspinvalues.com | 200，JS 渲染，数据来自 Google Sheets gviz | 价值表工具站 | Home / Common-Uncommon / Rare / Epic / Legendary / Omega / Misc / Vehicles / Money & Game Guide / Richest Players / Crew Logos；另有税费计算器、任务指南 | 按稀有度分页的物品卡（修理价/典当价按耐久度） | 公告栏：2025-11-29 改版、2025-12-03、2026-04-17；CSS 版本号 2026-09-25 | 按稀有度分栏、公告区写「上次改了什么」 | 社区自定价值（意见不是事实） |
| robloxblockspin.fandom.com | api.php 410，/wiki/ 403（Cloudflare），rest.php 可读 | 社区 wiki | 主页仍为 Fandom 模板；可见页 Cars、Weapons、Elite_Vehicle_Crate、F-150 | 纯列表，无信息框 | 最后编辑 2025-10-24（主页 2026-04-28 仅模板改动） | 载具按箱子分组的结构 | 数据已过期 |
| Pocket Gamer /roblox/blockspin-codes/ | 200 | codes 单页 | H2：Active / Referral codes / Expired / How to redeem / Alt Account 报错 / About | 0 张表，码是纯列表 | 「Updated on September 26th, 2026 - checked for codes」 | 「普通码 vs 推荐码」分栏；报错排障小节 | 码无来源，和 Roblox Den 状态打架 |
| Pocket Tactics /blockspin-codes | 200 | codes 单页 | H2：codes / How do I redeem / What are codes / Discord / How to get more | 0 张表 | dateModified 2026-06-19 | FAQ 式 H2 | 3 个月没更新仍挂「active」 |
| Roblox Den /game-codes/blockspin | 200 | codes 数据库页 | 单页：码表 + How to claim + About | 1 张表（码/描述/状态/投票）；5 active、159 expired | 「Last checked 26th September 2026」 | 过期码全保留（长尾）、每码一行结构化 | 靠用户投票判状态 |
| blockspintools.com | 200 | 小型 wiki + 工具 | Weapons DB / Vehicles DB / Jobs / Codes / Beginner / Map & Locations / Houses & Safes / Airdrops / Updates + 载具箱计算器 | Jobs 页 1 张表（工作/地点） | 未标 | 「只写已确认的、其余标复核中」的口径 | ——（同为 C 站，素材不引作唯一来源） |
| deltiasgaming.com 物品指南 | 200 | 单篇清单 | H3：Equipment & Consumables / Weapons / Vehicles | 0 张表 | dateModified 2025-03-26 | —— | 过旧 |
| block-spin.com | 代理 502，未获取 | —— | —— | —— | —— | —— | —— |
| progameguides.com codes | 403，未获取 | —— | —— | —— | —— | —— | —— |

## 我们采用的栏目结构

| 栏目（category） | slug | 页 | 首发状态 |
|---|---|---|---|
| Home | index | hub 首页 | 发布 |
| Getting Started | getting-started | codes、beginner、game-info、cheats-bans | 发布（4 篇有 S/A 来源） |
| Money & Gear | money-gear | jobs、map-locations、weapons、vehicles | 全部 draft（只有 B/C），栏目页也 draft，不进导航 |
| Author | author | 作者页 | 发布 |

砍掉的：values（只有社区自定价值）、tier list（无官方数值）、fandom 式单物品页（无一手数据）。
