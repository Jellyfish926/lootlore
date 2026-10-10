# 关键词清单(One Tap,英文)

需求证据:2026-10-10 实测 Google 下拉(suggestqueries.google.com,client=firefox,hl=en gl=us,28 组前缀,原始返回在 `raw/suggest.jsonl`)+ 两个抢注站的栏目(见 benchmark.md,只作「有人在做这类页」的线索)。**搜索量 / KD:未获取(本任务不查 Semrush)**,不估算。

下拉实测结论:`one tap roblox` 与 `one tap roblox ` 返回同一组 5 条(game / codes / bots / wiki / discord);`roblox one tap ` 另有 thumbnail / fps / reddit;`one tap roblox how to` 返回 how to scope / how to aim;`one tap roblox g` 里有 best gun in one tap roblox。带实体的前缀(case / skins / battle pass / gems / karambit / update)6 组全部返回空数组。下拉里混着另一款游戏的词(one touch … / one tap pistols codes),全部剔除。含 script / pastebin 的词不做。

## 通用需求(不带游戏内实体名)

| 词 | 下拉实测 | 搜索量 | 用户想知道什么 | 归属页 | 页型 |
|---|---|---|---|---|---|
| one tap roblox / fps one tap roblox | 有 | 未获取(本任务不查 Semrush) | 这是什么游戏、谁做的、从哪看起 | /one-tap/ | 首页 |
| one tap roblox game / fps one tap roblox game | 有 | 未获取(本任务不查 Semrush) | 同上;玩法一句话 | /one-tap/ | 首页 |
| one tap roblox wiki | 有 | 未获取(本任务不查 Semrush) | 有没有查资料的地方 | /one-tap/ | 首页 |
| one tap roblox codes / fps one tap roblox codes / roblox one tap codes | 有 | 未获取(本任务不查 Semrush) | 有没有兑换码 | 不建页;/one-tap/「Why is there no codes page?」一节 + FAQ | 首页一节 |
| one tap roblox discord / discord server / fps one tap roblox discord | 有 | 未获取(本任务不查 Semrush) | 官方 Discord 在哪 | /one-tap/game-info/「Is there an official One Tap Discord?」(写 could not confirm,不放链接) | 攻略 |
| one tap roblox gameplay / how to play | 有(gameplay) | 未获取(本任务不查 Semrush) | 怎么玩、规则是什么 | /one-tap/how-to-play/ | 攻略 |
| how to scope in one tap roblox / how to aim in one tap roblox | 有 | 未获取(本任务不查 Semrush) | 怎么开镜 / 瞄准 | 无官方来源 → /one-tap/how-to-play/ 与 /one-tap/game-info/ 明写未说明;进游戏核实后补(见 todo.md) | 攻略(缺口) |
| one tap roblox bots | 有 | 未获取(本任务不查 Semrush) | 大厅里是不是 bot | 无官方来源 → /one-tap/how-to-play/「What does the developer not state?」列为未说明 | 攻略(缺口) |
| one tap roblox xbox / playstation / mobile | 未返回(`one tap roblox x` 空) | 未获取(本任务不查 Semrush) | 主机 / 手机能不能玩 | /one-tap/game-info/ | 攻略 |
| stringless banjo | 有 | 未获取(本任务不查 Semrush) | 开发者是谁 | /one-tap/game-info/ | 攻略 |
| one tap roblox update | 无(空数组) | 未获取(本任务不查 Semrush) | 最近更新了什么 | /one-tap/updates/ | 攻略 |
| one tap roblox guide / beginner | 未测 | 未获取(本任务不查 Semrush) | 新手按什么顺序看 | /one-tap/beginner/ | 栏目 |
| roblox one tap reddit / thumbnail / logo | 有 | 未获取(本任务不查 Semrush) | 社区讨论 / 找图 | 不做(导航型 / 找图型,非攻略意图) | — |

## 个性需求(指名实体)

实体组:武器规则组、奖励组、通行证组、箱子组、战令组、商店组、更新组。

| 词 | 下拉实测 | 搜索量 | 用户想知道什么 | 归属页 | 页型 | 组 |
|---|---|---|---|---|---|---|
| one tap roblox sniper / secondary / melee / headshot | 未测 | 未获取(本任务不查 Semrush) | 三类武器的规则 | /one-tap/how-to-play/ | 攻略 | 武器规则 |
| best gun in one tap roblox | 有 | 未获取(本任务不查 Semrush) | 哪把枪最强 | 不建榜(无任何官方数值);how-to-play 的「not stated」清单说明 | — | 武器规则 |
| one tap roblox ban / alt farming | 未测 | 未获取(本任务不查 Semrush) | 什么行为会被封 | /one-tap/how-to-play/「What gets you banned in One Tap?」 | 攻略 | 武器规则 |
| one tap roblox quests / daily / levels / leaderboard / xp boost / refresh quest | 未测 | 未获取(本任务不查 Semrush) | 奖励从哪来、XP 加成多少钱 | /one-tap/rewards/ | 攻略 | 奖励 |
| one tap roblox gamepass / 2x money / 2x case luck / 2x xp / double voting value | 未测 | 未获取(本任务不查 Semrush) | 4 个通行证各做什么、多少钱 | /one-tap/gamepasses/ | 攻略 | 通行证 |
| one tap roblox case(s) / case prices / karambit case / energy sword case / proto case / cosmic case / moon case 等 | 无(case、karambit 两组空) | 未获取(本任务不查 Semrush) | 每种箱子多少 Robux、多买是否划算 | /one-tap/cases/ | 攻略 | 箱子 |
| one tap roblox battle pass / premium battlepass / skip tiers | 无(空数组) | 未获取(本任务不查 Semrush) | 战令多少钱、跳层哪个划算 | /one-tap/battle-pass/ | 攻略 | 战令 |
| one tap roblox gems / sun points / robux shop / starterpack / bundle / limited | 无(gems 空) | 未获取(本任务不查 Semrush) | 全店有什么、各多少钱 | /one-tap/shop/ | 攻略 | 商店 |
| one tap roblox skins / kill effects / name tags | 无(skins 空) | 未获取(本任务不查 Semrush) | 有哪些皮肤、怎么拿 | 暂归 /one-tap/how-to-play/(官方四行)+ /one-tap/shop/(limited 名称表);皮肤清单页见砍掉清单 | 攻略 | 商店 |
| one tap roblox update 2 / summer update / valentines / revert / lunar update | 未测 | 未获取(本任务不查 Semrush) | 每次更新加了什么、为什么回滚 | /one-tap/updates/ | 攻略 | 更新 |
| one tap roblox maps / crosshair | 未测 | 未获取(本任务不查 Semrush) | 有哪些地图、准星怎么调 | 暂归 /one-tap/how-to-play/(只有 Update 2 的两行) | 攻略 | 更新 |

## 砍掉的词 / 页(留痕)

| 词 / 页 | 为什么砍 |
|---|---|
| codes 页 | 官方来源 0 个码(描述 18 行无码;群组 description 一句话无码;shout null;6 条活动文本无码;社交链接 401 未获取)。硬做只能是「Active Codes: 0」→ 不建;hub 用一节说明原因。抢注站上的内容不采信 |
| discord 单独成页 | 官方一手页面上看不到任何邀请;单页只能写「未确认」→ 合并为 game-info 的一节,不放任何邀请链接 |
| badges 页 | 官方徽章 0 个(3 次读取均为空)→ 不建;game-info 一节说明 |
| weapons / best gun / tier list | 0 个官方数值(伤害、射速、换弹都没有);唯一的官方文字是三行武器规则 → 不做榜、不建武器表;规则并进 how-to-play |
| skins 清单页 / all skins | 官方只有「70+」与活动里的「28 total new weapons」,没有名单 → 不建;进游戏抄到名单后再建 /one-tap/skins/ |
| maps 页 | 只有 Update 2 一行(3 张新图且被临时撤下),没有图名 → 不建 |
| aim / settings / sensitivity 教学 | 0 来源,且需要实测 → 不建;how to scope / how to aim 两个词先在 how-to-play 与 game-info 明写「无官方说明」 |
| bots 页 | 0 来源 → 不建 |
| case contents / drop rates | 0 来源 → 不建;cases 页写 not stated |
| script / pastebin / no key | 外挂。官方描述明写永久封禁,且违反 Roblox 条款,总站不做 |
| one touch … / one tap pistols … | 下拉里混入的其他游戏的词,与本游戏无关,全部剔除 |
| platforms 单独成页 | 一手只有描述里的 4 行(约 6 条事实),单页不到 800 词 → 合并进 game-info |
| faq 单独成页 | 与 hub 的 frontmatter faq(6 条)重复 → 不建 |
