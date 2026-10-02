# +1 Stone Skipping 待办（2026-10-02）

## A. 有日期的动作

| 日期 | 动作 | 涉及文件 |
|---|---|---|
| **2026-10-04**（活动结束后） | 重读 virtual-events、game-passes、developer-products 三个接口与 icons 接口；把 ADMIN ABUSE + WORLD 5 写成过去时；记录活动后新增的通行证 / 商品；看图标横幅是否从 WORLD 4 变成 WORLD 5 | updates（活动一节、首段、tldr、scope）、index（What's happening 一节、tldr 第 3 条、faq 第 5 条、description）、beginner（首段）、how-to-play（Worlds 一节、tldr 第 3 条）、community（私服一节、官方消息一节）、entities.json（event 实体的 expiry_action）、config-snippet.json（card.blurb 与 highlights 的「World 5」） |
| 每次复核 | 重取 games / votes / group 快照数字（在线、访问、收藏、赞踩、群成员） | index、community |
| 每 60 天 | 重跑 thumbnails 接口刷新 `180DAY-` 图片 URL，逐个 curl 验 200 | _images.json、config-snippet.json 的 card.img |
| 官方发码当天 | 新建 codes 页（按 codes 页规格），community 页改口径 | 新页 + community + index |

## B. 需要进游戏核实（公开接口里没有，正文一律写了 not shown in public data / needs in-game check）

核心循环
1. 每次弹跳的 Skill 是不是固定 +1；随等级 / 石头 / 宠物怎么变（宣传图出现 +150M、+4B、+1M，只是美术）。
2. 「Train」具体怎么做（站在某个区域？点击？自动？）；等级门槛表；等级与投掷距离的关系。
3. zone 的名称、顺序、各自距离门槛、每个 zone 给多少 Wins；距离单位是不是米（宣传图有「999,999m」）。
4. 石头 / 投掷物清单、解锁方式与价格（Wins？Skill？）、各自加成；DONUT 在哪一档。
5. Rebirth 的条件、奖励、重置什么；Skip Rebirth（35 Robux）与 Auto Rebirth（149 Robux）在游戏里的说明文字。
6. World 1–4（10-03 后含 World 5）各自的解锁条件；图标上的「WORLD 4」是当前最高世界还是别的意思；游戏页 Servers 标签里有没有私服选项（接口字段不可靠，community 页现在写「无法确认」）。
7. Wins 能买什么（它是不是货币）。

宠物与蛋
8. 六种 Robux 蛋各自的宠物名单、概率、加成数值与加成对象；是否有用 Wins 等游戏币孵的蛋及其价格。
9. 不买通行证时的基础宠物装备数与单次孵化数；+1 / +3 / +6 Pets 是否就是装备栏位、三者是否叠加；Hatch +3 / +8 / +16 Eggs [STACKS] 是否叠加到 +27。
10. King Doggy（999）、Starter Pack（39）、Devil Pack（299）、Phoenix Relic [LIMITED STOCK]（499）买到的具体内容；Phoenix Relic 是否有库存计数。

商店
11. Skill Multiplier [TIER 1–10] 每档的倍率；是否必须按顺序买；是否叠加。
12. Skill Pack / Wins Pack 每个包给多少；Skill Pack 的 [TIER 1–3] 是按玩家进度显示不同档，还是三档同时可买。
13. Skill Boost / Wins Boost / Boost Pack 的时长与倍率；2x / 5x / 10x Wins [PERMANENT] 是否叠加。
14. Koi / Golden / Admin Training Zone 三个通行证的实际效果与差别；Auto Wins 的速率、离线是否生效。
15. 同名异价：游戏内现在卖的是通行证版 Admin Training Zone 599 / Golden Training Zone 249，还是商品版 195 / 315？商品「Golden Zone」115、「Admin Zone」289 是否还在卖？
16. Wins Pack 5：游戏里显示 459（[20% OFF]）还是 575。
17. Offline Reward x3、Claim All Gifts、Golden Skip、Diamond Skip 各是什么；游戏是否有离线收益和定时礼物。
18. Boost Bundle、Power Boost（接口显示未上架、无价格）是下架了还是没发布。
19. [GIFT] 商品的赠送流程。

码与社区
20. 游戏内有没有输码框、在哪；官方在哪发码（进游戏看 UI，或登录后看 social links）。
21. 官方 Discord / X 链接（游戏页 social links 需登录才显示）。
22. 加入 Meow Labs 群组是否有游戏内奖励（群成员 481,097，是收藏数的 2.37 倍）。

第三方线索（C 级，待上面各条核实后才可能进正文；现在一条都没用）
- zone 链五个名称与顺序（stoneskipping.wiki、stone-skipping.wiki）
- 「Hacked Admin」蛋的价格与概率（同上）
- Auto Throw、Friend boost、Rebirth pads、Gifts 等系统（stone-skipping.wiki、1stoneskipping.wiki 的页面标题）
- （已解决）9-27 的「WORLD 4 + UPDATE」活动：第 1 轮验证后已从 events 接口直接取到，updates / how-to-play / index 用的是接口数据
- 三站各自的码表（不抄；只有在官方来源亲眼见到才收）

## C. 未获取项及原因

| 项 | 原因 |
|---|---|
| 官方 Discord 公告、X 帖子 | 需登录，按规定不取，不凭印象补 |
| 群组 wall | `groups.roblox.com/v2/groups/207366578/wall/posts` 返回 404（errors code 0，无消息，原因不明） |
| 体验 / 群组 social links | 接口无令牌返回 401「Authentication token is missing」；Roblox 文档称社交链接只对已验证年龄 ≥16 的用户可见 |
| 旧通行证接口 | `games.roblox.com/v1/games/10765298801/game-passes` 返回 404；用新接口取到 11 个 |
| World 2 的日期 | 官方活动里没有标题含 World 2 的条目。取过往活动要用带游标的请求（`?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA`，稳定返回 World 3 + New Content、WORLD 4 + UPDATE、ADMIN ABUSE + WORLD 5 三条）；默认请求通常只返回即将开始的一条 |
| 私服是否开放 | createVipServersAllowed=false 不可靠（已知有私服的 Blox Fruits / Pet Simulator 99 / DOORS 同为 false）；私服接口 401 |
| World 2–5 的解锁条件、world 开放的确切时刻 | World 3 / 4 只有活动标题与窗口（无描述）；没找到名称写明跳到某个 world 的商品 |
| 支持设备 | 本轮没有找到可匿名读取的接口，未取 |
| progameguides.com、destructoid.com、twinfinite.net（对标用） | Cloudflare 拦截页 403；不过验证，停止该来源，benchmark 改用 beebom / deltiasgaming / pockettactics / tryhardguides |
| 搜索量 / KD | 未用 Semrush（dash.3ue.com），未估算 |
| A 级来源 | 0 条：群组 description 只有 "meow?"，shout 为 null |

## D. 接入总站时要做的（本轮没动仓库）

1. `content/en/*.md` → 仓内 `content/stone-skipping/en/`；`_images.json` → `content/stone-skipping/_images.json`；`entities.json` → `data/stone-skipping/entities.json`；`config-snippet.json` 的 `games_item` 追加进 `config/hub.json` 的 `games[]`。i18n 不需要新增键。
2. `dossier.md` → `sites/stone-skipping/site-dossier-stone-skipping.md`（照 mog-evolution 的文件名）；`benchmark.md`、`planning/` → `sites/stone-skipping/`。`raw/` 不进仓。
3. 已在仓库副本里试构建过（第 1 轮验证修改后重跑；LOOTLORE_BUILD_DATE=2026-10-02）：stone-skipping 生成 12 页（11 页 + /all/），check_content 0 阻塞 0 警告、check_sitemap 0 / 0、link_check 无死链、check_ga 0 错。正式接入后要在真仓里重跑。
4. 独立事实核验（adversarial-verify）第 1 轮：524 命题，4 REFUTED / 20 UNVERIFIED，已按清单全部修改（R1–R4、U1–U14），并用验证方给的新线索补入 World 3 / World 4 两场过往官方活动。修改后的句子待验证员复验；复验通过前 community / updates / gamepasses / how-to-play / author 五页不算可发布，而 index、beginner 链到 community / updates，要同批上线。
4b. 快照数字（在线、访问、收藏、赞踩、群成员）全部是 2026-10-02 11:19 UTC 的读数，页内都带了时点；如果隔天才发布，要重取并把时点一起改掉。
4c. Playwright 打不开本地预览（ERR_BLOCKED_BY_CLIENT），页面没做肉眼截图验收；author 页的作者文章列表与署名行标签（Last reviewed / Checked on version）已在构建产物 HTML 里核过。
5. 表格数：shop 页 6 张、gamepasses / pets / boosts / updates 各 4 张，shop 超过「每页 2–4 张」的规格（78 个商品分五组列表），接入时如要压到 4 张可把 Skill 与 Wins 两张合并、礼物表并入对应组。
