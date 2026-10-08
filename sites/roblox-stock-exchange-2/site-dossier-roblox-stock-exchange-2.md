# Roblox Stock Exchange 2 事实底稿(dossier)

取证日:2026-10-08(UTC 03:39–04:03 抓取;快照型数字只代表那一刻。games / votes / group 取 03:39 那次,badges 取 03:47 那次)。
范围:Roblox 体验「Roblox Stock Exchange 2」,universeId 10495391267,rootPlaceId 110527353762049,创作者群组 Summit Productions Development(groupId 33446529)。同群组的前作「Legacy: Roblox Stock Exchange」(universe 7757905683)与其它同名/近名体验(如 RBLX Exchange)的内容一律不混入。
原始抓取文件:`raw/`(fetch-log.txt 记录每个 URL 的 HTTP 状态;games.json / votes.json / favorites.json / age.json / badges.json(+badges_p1.json、badges_recheck.json 复查)/ passes.json / devprod_p1.json / virtual_events_cursor.json(+ virtual_events*.json 其它翻页与过滤口径)/ group*.json / group_games.json / owner_user.json / thumbs_*.json / icons.json / event_thumbs_all*.json / media.json / discord_invite.json / docs/*.html / comp/* / img/*.png(本人看图用)/ suggest.jsonl / gates/*(试构建门禁输出))。

来源分级(按 seo-jianzhan ①.8 表 3):**S** = 一手官方(Roblox 官方 API 返回的开发者自填数据:游戏描述、徽章、通行证、开发者商品、官方活动 listing 与其配图、群组资料;Roblox 官方文档 create.roblox.com);**A** = 平台一手/开发者官方渠道原话(本次 **0 条**:群组 description 为空、shout 为 null、wall 接口 404、social links 接口 401);**B** = 社区/服务器自述(Discord invite API 返回的服务器自述);**C** = 二手 SEO 站(码页、小 wiki),只当线索与交叉。

结论:S 级素材很厚——官方描述 7 条功能线 + 1 个兑换码、11 个徽章(带累计/昨日获得数)、13 个通行证(每个都有具体的官方描述,含手续费率/杠杆上限/离线时长等硬数字)、31 个开发者商品(仅 1 个有描述)、12 条官方更新活动(标题+一句话描述+配图)。**没有任何一手来源的**:兑换码 TOOLS 的奖励、兑换界面位置、不买通行证时的手续费与各等级杠杆上限、等级/经验表、rebirth 条件与收益、bot 的设置项/收益/解锁条件、游戏内现金价格、支持设备。这些全部进「未核实」,正文写 not stated / not published 或不写。

**round1 修订(2026-10-08,独立验证之后)**:① 兑换码 TOOLS 只证明「印在官方描述里」,**没有进游戏实测**,页面口径已全部改成 printed in the official description (not tested in game);② Twinfinite / Pro Game Guides 两站验证员取证 403、无法独立复核,**页面上已不再引用**(本底稿下文保留它们只作调研记录);③ 通行证描述里的 "instead of 8" / "instead of 2" 只能「推出」基础值,页面改成 implies;④ 活动 listing 一律写成预告与绝对时间(listed to start on …),不写 next / starts;⑤ 页面 sourceUrls 里 virtual-events 用不带游标的地址(2026-10-08 03:39 不带游标只回 2 条,04:19 后多次回 12 条),分级接口(只接受 POST)不放进 sourceUrls;⑥ 群组游戏表里 INDEFINITE 的名称恢复接口原样(含两个 emoji);⑦ 前作描述里有 "Join the Main Group for a $10,000 starting cash bonus!",community 页已写明那是前作、不是 2 代。

## 1. 基本信息

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 取得日 | 级 |
|---|---|---|---|---|---|
| F001 | 正式名 | `Roblox Stock Exchange 2`(无 emoji、无方括号更新标签) | https://games.roblox.com/v1/games?universeIds=10495391267 | 2026-10-08 | S |
| F002 | universeId / rootPlaceId | 10495391267 / 110527353762049 | https://games.roblox.com/v1/games?universeIds=10495391267 | 2026-10-08 | S |
| F003 | 创作者 | 群组 `Summit Productions Development`(id 33446529,type Group,hasVerifiedBadge=false) | https://games.roblox.com/v1/games?universeIds=10495391267 `creator` | 2026-10-08 | S |
| F004 | 创建时间 | `2026-07-13T06:42:35.832Z` → 13 July 2026 | https://games.roblox.com/v1/games?universeIds=10495391267 `created` | 2026-10-08 | S |
| F005 | `updated` 字段(不可当更新日) | 三次读取三个值:03:39 读到 `2026-10-08T03:36:09.953Z`;03:47 读到 `2026-10-08T03:44:15.692Z`;04:03 读到 `2026-10-08T03:56:24.481Z`。24 分钟内变三次 → 不是补丁日期,正文不拿它当「最近更新」。另:群组游戏列表接口同一字段是 `2026-09-30T00:00:33.24Z`,两个接口口径不同 | https://games.roblox.com/v1/games?universeIds=10495391267 `updated`;https://games.roblox.com/v2/groups/33446529/games?accessFilter=Public&limit=50 | 2026-10-08 | S |
| F006 | 类型 | genre_l1 `Simulation`,genre_l2 空串 | https://games.roblox.com/v1/games?universeIds=10495391267 | 2026-10-08 | S |
| F007 | 单服人数上限 | 35 | https://games.roblox.com/v1/games?universeIds=10495391267 `maxPlayers` | 2026-10-08 | S |
| F008 | 价格 | 免费(`price: null`) | https://games.roblox.com/v1/games?universeIds=10495391267 | 2026-10-08 | S |
| F009 | 私服 | `createVipServersAllowed: false` —— 按 SKILL 2026-10-02 口径不能据此判「不开放私服」,正文不写 | https://games.roblox.com/v1/games?universeIds=10495391267 | 2026-10-08 | S |
| F010 | 访问量(03:39 快照) | 5,093,566 | https://games.roblox.com/v1/games?universeIds=10495391267 `visits` | 2026-10-08 | S |
| F011 | 在线(03:39 快照) | 1,123 | https://games.roblox.com/v1/games?universeIds=10495391267 `playing` | 2026-10-08 | S |
| F012 | 收藏(03:39 快照) | 61,993(favorites/count 接口同值 61,993) | https://games.roblox.com/v1/games?universeIds=10495391267;https://games.roblox.com/v1/games/10495391267/favorites/count | 2026-10-08 | S |
| F013 | 点赞 / 点踩(03:39 快照) | 12,004 / 890(好评率 93.1%,我们计算) | https://games.roblox.com/v1/games/votes?universeIds=10495391267 | 2026-10-08 | S |
| F014 | 内容分级 | `Maturity: Minimal`;描述项 displayName `Suitable for everyone` | https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation(POST `{"universeId":"10495391267"}`) | 2026-10-08 | S |
| F015 | 游戏页媒体 | 5 张图片 + 1 个 GamePreviewVideo(预览视频未下载) | https://games.roblox.com/v1/games/10495391267/media | 2026-10-08 | S |

## 2. 官方描述(逐行原文;emoji 在正文引用时去掉,其余逐字)

来源:https://games.roblox.com/v1/games?universeIds=10495391267 `description`(S,2026-10-08 03:39 取;03:47 复取一致)

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 取得日 | 级 |
|---|---|---|---|---|---|
| F016 | 描述第 1 行(标题口号) | "📈 BUILD YOUR TRADING EMPIRE!" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F017 | 描述第 2 行(核心循环:小账户起步;「even while you’re offline」= 离线也在跑) | "Start with a small account and work your way toward becoming a market legend. Study price action, discover leading stocks, manage risk, and grow your portfolio, even while you’re offline!" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F018 | 描述第 3 行(四类市场) | "💰 Trade stocks, ETFs, futures, and IPOs" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F019 | 描述第 4 行(指标 + 订单流) | "📊 Use advanced indicators and live order flow" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F020 | 描述第 5 行(三种订单工具) | "⚡ Place limit orders, stop losses, and take profits" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F021 | 描述第 6 行(bot:先解锁后升级) | "🤖 Unlock and upgrade algorithmic trading bots" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F022 | 描述第 7 行(等级 / rebirth) | "🏆 Level up, rebirth, and expand your financial empire" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F023 | 描述第 8 行(按日盈亏日历) | "📅 Track your performance with a P&L calendar" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F024 | 描述第 9 行(杠杆 / 做空) | "🔥 Use leverage, short the market, and master every market cycle" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F025 | 描述第 10 行 | "Can you read the market, manage risk, and build the ultimate trading empire?" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F026 | 描述第 11 行(兑换码三行之一) | "THANKS FOR 10K LIKES" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F027 | 描述第 12 行(**兑换码**(本人 2026-10-08 亲眼所见,唯一一个)) | "CODE: TOOLS" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F028 | 描述第 13 行(下一码门槛:15,000 赞) | "NEXT CODE RELEASES AT 15,000 LIKES" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F029 | 描述第 14 行 | "⭐ Like and favorite the game for future updates!" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |
| F030 | 描述第 15 行(官方免责:全部模拟、非真钱交易、非投资建议) | "All markets and currencies are simulated. This game does not involve real-money trading or provide financial advice." | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |

## 3. 兑换码

| # | 码 | 奖励 | 状态 | 来源原文 | 来源 URL | 看到日期 | 级 |
|---|---|---|---|---|---|---|---|
| K01 | `TOOLS` | **官方未写**(描述里只有码本身) | 2026-10-08 仍在官方描述中 → active | "THANKS FOR 10K LIKES" / "CODE: TOOLS" / "NEXT CODE RELEASES AT 15,000 LIKES" | https://games.roblox.com/v1/games?universeIds=10495391267 `description` | 2026-10-08 | S |

- K02 下一码触发条件:15,000 赞;03:39 赞数 12,004,差 2,996(我们相减)。来源 https://games.roblox.com/v1/games/votes?universeIds=10495391267(S)。
- K03 其它官方位置无码:群组 description 空串、shout null(https://groups.roblox.com/v1/groups/33446529);12 条官方活动的 title/subtitle/description 均无码(https://apis.roblox.com/virtual-events/v1/universes/10495391267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA);群组 wall 接口 404、social links 接口 401,读不到。
- 交叉(C,只作线索,**不进码表**;读取记录见 `raw/comp/webfetch-notes.md`):Roblox Den(10/07 检查)列 7 个 active:TOOLS、STOCKMARKET、MEMECOINS、FUTURES、BULLMARKET、UPDATE、RELEASE;Try Hard Guides(09-29)同 7 个;Twinfinite(10-01)与 Pro Game Guides(09-07)列后 6 个、不含 TOOLS。四站都没给码的开发者出处。奖励互相打架:FUTURES 在 Roblox Den 是 "20,000 Cash and 20 XP",在 PGG / Twinfinite 是 10k Cash;TOOLS 的奖励只有 Roblox Den 写 "20K Cash"。
- 兑换入口(C):Roblox Den "Gift icon at the top-right side of the screen" + "ENTER CODE box" + "REDEEM button";Try Hard Guides "yellow gift/present button in the right corner" + "ENTER CODE text box";Twinfinite "gift box button in the top-right corner" + "'Enter Code' text box";PGG "Gift Box icon" + "PROMO CODE box"。无 S/A 来源,且 10-03 官方活动称换了全新界面 → 正文只写通用步骤并标注未一手核实。

## 4. 徽章(11 个,全部官方)

来源:https://badges.roblox.com/v1/universes/10495391267/badges?limit=100(S;2026-10-08 03:47 取;nextPageCursor=null;awardingUniverse.id 逐条 = 10495391267;03:39 那次取数 id 完全一致,Welcome 累计 2,288,054 → 03:47 为 2,288,320,8 分钟 +266)。「占 Welcome 比」= 该徽章累计 ÷ Welcome 累计,我们计算。

| # | 徽章名(逐字) | 官方描述(逐字) | 创建日 | 累计获得 | 过去一天获得 | 占 Welcome 比 | enabled |
|---|---|---|---|---|---|---|---|
| B01 | Welcome to Roblox Stock Exchange 2 | Thank you for playing! | 2026-07-13 | 2,288,320 | 47,508 | 100% | true |
| B02 | First Trade | You made your first trade! | 2026-07-13 | 2,061,945 | 46,499 | 90.1% | true |
| B03 | First Profit | You made your first profit trading! | 2026-07-13 | 1,569,182 | 46,436 | 68.6% | true |
| B04 | First Short | You shorted your first stock! | 2026-07-13 | 616,376 | 30,247 | 26.9% | true |
| B05 | Hundred Trades | You completed your first 100 trades! | 2026-07-14 | 299,258 | 8,331 | 13.1% | true |
| B06 | First Futures Trade | You made your first futures trade! | 2026-07-13 | 214,382 | 19,052 | 9.4% | true |
| B07 | Millionaire | Your total net-worth is over $1,000,000! | 2026-07-14 | 100,099 | 1,913 | 4.4% | true |
| B08 | First Algo Bot | You created your first algorithmic trading bot! | 2026-07-14 | 50,910 | 1,404 | 2.2% | true |
| B09 | First Rebirth | You rebirthed for the first time! | 2026-07-14 | 42,936 | 394 | 1.9% | true |
| B10 | $10,000,000 Net Worth | Your net worth exceeded $10,000,000 | 2026-07-14 | 39,765 | 406 | 1.7% | true |
| B11 | Met the game owners! | Wow, 150% profit. You were in a server with one of the game owners | 2026-08-15 | 1,305 | 0 | 0.06% | true |

推导(我们算的,页面上注明是计算/推断):
- First Profit ÷ First Trade = 76.1% → 约四分之一下过单的玩家没拿到盈利徽章。
- $10,000,000 Net Worth ÷ Millionaire = 40%。
- First Rebirth(42,936)> $10,000,000 Net Worth(39,765)→ 至少有一部分玩家 rebirth 时没有千万徽章(抽屉原理;**不能**推出 rebirth 的门槛)。
- Millionaire(100,099)约为 First Algo Bot(50,910)的 2 倍。
- 过去一天:First Short 30,247、First Futures Trade 19,052,相对当日 Welcome(47,508)为 63.7 / 40.1 每百,远高于累计占比(26.9% / 9.4%)。原因未知(10-03 换界面可能相关,无证据)。
- `winRatePercentage` 字段含义不明,未使用。
- 「Met the game owners!」2026-08-15 创建,累计 1,305,过去一天 0;怎么触发只有描述那一句。

## 5. 通行证 Game Passes(13 个,全部官方;全部在售,无折扣)

来源:https://apis.roblox.com/game-passes/v1/universes/10495391267/game-passes?passView=Full&pageSize=100(S;nextPageToken 空)。旧接口 games.roblox.com/v1/games/10495391267/game-passes 返回 404。

| # | 名称(逐字) | Robux | 官方描述(逐字;接口里的 \r\n 换成空格) | 创建日 | 更新日 | passId |
|---|---|---|---|---|---|---|
| P01 | Custom Timeframes | 39 | Access to any custom timeframes, such as 1 second charts and more. | 2026-08-08 | 2026-08-08 | 1942182816 |
| P02 | Watchlist Pro | 49 | 10 custom watchlists with up to 50 symbols in each list. | 2026-07-13 | 2026-08-12 | 1906088154 |
| P03 | Unlimited AI Usage | 79 | Ask SummitAI as much as you like: no daily or weekly cap, a much larger conversation memory, and the top effort tiers always available. | 2026-08-09 | 2026-08-09 | 1940299048 |
| P04 | Pro Trader | 99 | 0.02% fees, unlimited drawings, pro stats. | 2026-07-13 | 2026-08-12 | 1907618177 |
| P05 | Indicator Pro | 129 | Run up to 8 community or custom indicators at the same time. | 2026-07-13 | 2026-08-12 | 1907414205 |
| P06 | Max Leverage | 149 | Up to 50x leverage at any level. | 2026-07-13 | 2026-08-12 | 1907612139 |
| P07 | More Player Companies | 149 | Launch up to 5 player-founded stocks instead of 2. | 2026-07-14 | 2026-08-15 | 1907894508 |
| P08 | Executive Terminal | 159 | Permanent gold terminal branding and Executive status treatment. Gives access to an exclusive set of stocks, and unlocks private market algorithmic bot scans. | 2026-07-13 | 2026-08-12 | 1907396210 |
| P09 | Order Flow | 199 | Level 2 order book data, shows placed orders along the book, and shows bias direction based off the flow of orders. | 2026-07-13 | 2026-08-15 | 1907012158 |
| P10 | Overnight Desk | 199 | Your market keeps running for 24 hours offline instead of 8. | 2026-07-19 | 2026-08-12 | 1918719154 |
| P11 | VIP | 229 | 2x XP, 2x daily rewards, VIP badge, 1 free Sim Day per day. | 2026-07-13 | 2026-08-12 | 1906688160 |
| P12 | Insider | 299 | Early alerts before news hits + IPO intel. | 2026-07-13 | 2026-08-12 | 1907396178 |
| P13 | All Gamepasses Bundle | 999 | All gamepasses, but at a lower cost. | 2026-08-15 | 2026-08-15 | 1949660750 |

推导:
- 12 个单项合计 1,778 Robux;Bundle 999;差 779(约 44%)。Bundle 描述没列出包含哪些通行证。
- 通行证描述反推出的**基础值**(S,出自描述原话):离线市场时长 8 小时("24 hours offline instead of 8");玩家创办公司上限 2("up to 5 player-founded stocks instead of 2")。
- 通行证描述证明存在但基础值**未公布**的系统:手续费(Pro Trader "0.02% fees")、按等级的杠杆上限(Max Leverage "Up to 50x leverage at any level")、XP 与每日奖励(VIP)、Sim Day(VIP "1 free Sim Day per day")、SummitAI 的日/周上限(Unlimited AI Usage)、自定义/社区指标数量上限(Indicator Pro "up to 8")、新闻提前预警与 IPO 情报(Insider)、Level 2 订单簿(Order Flow)、专属股票与 private market bot scans(Executive Terminal)、自定义周期如 1 秒图(Custom Timeframes)、自选列表(Watchlist Pro "10 custom watchlists with up to 50 symbols")。

## 6. 开发者商品(31 个,全部官方;全部在售;只有 1 个有描述)

来源:https://apis.roblox.com/developer-products/v2/universes/10495391267/developerproducts?limit=100(S;nextPageCursor=null)。分组是我们按名称归的,不是官方分类。

| # | 分组(我们归类) | 名称(逐字) | Robux | 官方描述 | 创建日 | 更新日 | productId |
|---|---|---|---|---|---|---|---|
| D01 | Time skips | Skip to Market Open | 9 | (空) | 2026-07-13 | 2026-08-12 | 3609583116 |
| D02 | Time skips | Simulate Day | 39 | (空) | 2026-07-13 | 2026-08-12 | 3609583136 |
| D03 | Time skips | Simulate Week | 99 | (空) | 2026-07-13 | 2026-08-12 | 3609583154 |
| D04 | Algo bots | Algo Scan Upgrade | 39 | (空) | 2026-07-13 | 2026-08-12 | 3609599329 |
| D05 | Algo bots | Algo Expertise Upgrade | 79 | (空) | 2026-07-13 | 2026-08-12 | 3609599357 |
| D06 | Algo bots | Deploy Algo Bot | 149 | (空) | 2026-07-13 | 2026-07-13 | 3609599145 |
| D07 | Algo bots | Tune Entire Algo Fleet | 249 | (空) | 2026-07-13 | 2026-07-13 | 3609583227 |
| D08 | Trader Spotlight | 15-Min Trader Spotlight | 49 | (空) | 2026-07-13 | 2026-07-13 | 3609583175 |
| D09 | Trader Spotlight | 1-Hour Trader Spotlight | 149 | (空) | 2026-07-13 | 2026-07-13 | 3609583181 |
| D10 | Trader Spotlight | 1-Day Trader Spotlight | 499 | (空) | 2026-07-13 | 2026-07-13 | 3609583213 |
| D11 | AI Tokens | 5,000 AI Tokens | 29 | (空) | 2026-08-09 | 2026-08-11 | 3661727368 |
| D12 | AI Tokens | 20,000 AI Tokens | 49 | (空) | 2026-08-09 | 2026-08-11 | 3661732347 |
| D13 | AI Tokens | 75,000 AI Tokens | 69 | (空) | 2026-08-09 | 2026-08-11 | 3661736099 |
| D14 | Season pass | Trader Pass - Season 1 | 199 | Unlocks the premium track of Trader Pass Season 1, The Golden Bell: 22 animated exclusives and 20,000 AI tokens. Cosmetic only, no cash or boosts. | 2026-10-02 | 2026-10-02 | 3715974979 |
| D15 | One-off purchases | Skip Recovery | 19 | (空) | 2026-07-13 | 2026-07-13 | 3609600647 |
| D16 | One-off purchases | Double Earnings | 19 | (空) | 2026-07-14 | 2026-08-15 | 3609771491 |
| D17 | One-off purchases | Trader Starter Pack | 19 | (空) | 2026-07-14 | 2026-08-12 | 3609786399 |
| D18 | One-off purchases | Instant Acension | 249 | (空) | 2026-08-15 | 2026-08-19 | 3708158573 |
| D19 | Named after a game pass | Custom Timeframes | 39 | (空) | 2026-08-15 | 2026-08-15 | 3708157443 |
| D20 | Named after a game pass | Unlimited AI Usage | 79 | (空) | 2026-08-15 | 2026-08-15 | 3708157417 |
| D21 | Named after a game pass | Pro Trader | 99 | (空) | 2026-07-19 | 2026-07-19 | 3610606448 |
| D22 | Named after a game pass | Watchlist Pro | 99 | (空) | 2026-07-19 | 2026-07-19 | 3610606621 |
| D23 | Named after a game pass | Indicator Pro | 129 | (空) | 2026-07-19 | 2026-07-19 | 3610606635 |
| D24 | Named after a game pass | Executive Terminal | 139 | (空) | 2026-07-19 | 2026-08-12 | 3610606656 |
| D25 | Named after a game pass | Max Leverage | 149 | (空) | 2026-07-19 | 2026-07-19 | 3610606511 |
| D26 | Named after a game pass | Order Flow | 249 | (空) | 2026-07-19 | 2026-07-19 | 3610606567 |
| D27 | Named after a game pass | Insider | 299 | (空) | 2026-07-19 | 2026-07-19 | 3610606482 |
| D28 | Named after a game pass | VIP | 399 | (空) | 2026-07-19 | 2026-07-19 | 3610606532 |
| D29 | Named after a game pass | All Gamepasses Bundle | 999 | (空) | 2026-08-15 | 2026-08-15 | 3708157510 |
| D30 | Pass-style names with no matching pass | Offline Earnings | 199 | (空) | 2026-07-19 | 2026-07-19 | 3610606692 |
| D31 | Pass-style names with no matching pass | Company Mogul | 249 | (空) | 2026-07-19 | 2026-07-19 | 3610606671 |

要点:
- 「Instant Acension」是接口里的原拼写(少一个 s),正文照抄并注明。
- 与通行证**同名**的商品 11 个,其中 4 个价格不同:Watchlist Pro 49→99、Executive Terminal 159→139、Order Flow 199→249、VIP 229→399(通行证价→商品价)。用途官方没写(是不是赠送版**未获取**,正文不猜)。
- 「Offline Earnings」199、「Company Mogul」249 没有同名通行证(名字像 Overnight Desk / More Player Companies,但接口没有关联,正文只说 resemble)。
- AI Tokens 三档 5,000 / 20,000 / 75,000 = 29 / 49 / 69 Robux → 每 Robux 约 172 / 408 / 1,087 token(我们计算)。token 与 SummitAI 的对应关系是按名称推断(Unlimited AI Usage 通行证描述提到 SummitAI),正文写 appear to。
- Trader Pass - Season 1(2026-10-02 创建)是唯一有描述的商品:"Unlocks the premium track of Trader Pass Season 1, The Golden Bell: 22 animated exclusives and 20,000 AI tokens. Cosmetic only, no cash or boosts."
- bot 相关 4 个:Algo Scan Upgrade 39 / Algo Expertise Upgrade 79 / Deploy Algo Bot 149 / Tune Entire Algo Fleet 249,均 2026-07-13 创建,无描述。

## 7. 官方活动 virtual-events(12 条,全部官方)

来源:https://apis.roblox.com/virtual-events/v1/universes/10495391267/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA(S;带零起点游标的请求,返回 12 条;`?eventStatus=completed` 同样返回这 12 条;默认请求只返回最后 2 条;沿 previousPageCursor 往回翻没有更早的条目)。host 全部是群组 Summit Productions Development(hostId 33446529),eventCategories 全部 newContent。eventStatus 字段 12 条全是 "active"(含早已结束的),不可用。**活动 listing 是预告,不等于功能在起始时刻上线**,正文每处都这么写。

| # | title(逐字) | subtitle | description(逐字) | 开始 UTC | 结束 UTC | 登记 UTC | 开始星期 |
|---|---|---|---|---|---|---|---|
| E01 | HEDGE FUNDS | UPDATE | Run a hedge fund | 2026-08-17 23:00 | 2026-08-19 23:00 | 2026-08-16 21:22 | Mon |
| E02 | NEW FUNCTIONS | Scripting Overhaul | Tons of new functions and additions to the script editor so you can continue to make advanced indicators! | 2026-08-19 21:00 | 2026-08-22 22:00 | 2026-08-17 20:16 | Wed |
| E03 | NEW MEMECOINS | UPDATE | This update will feature new meme coins in the Crypto tab. This system will work in a different way, they will launch at random in the game, and have different results. | 2026-08-22 21:00 | 2026-08-25 22:00 | 2026-08-16 20:33 | Sat |
| E04 | CHALLENGES | UPDATE | New challenges, this will feature starting at a low amount to make a much higher amount, your reward will be a permeant perk + exclusive cosmetic | 2026-08-26 20:00 | 2026-08-29 04:55 | 2026-08-24 00:41 | Wed |
| E05 | NEW TOOLS | UPDATE | New tools such as fib extension, trailing stops, and so much more! | 2026-08-29 22:00 | 2026-08-31 23:00 | 2026-08-22 21:50 | Sat |
| E06 | NEWS OVERHAUL | "THE WIRE" | This update will feature a brand new news system, and more news events. | 2026-09-02 22:00 | 2026-09-04 23:00 | 2026-08-30 09:06 | Wed |
| E07 | REAL ESTATE | UPDATE | In this update, you'll be able to buy real estate across a global map. | 2026-09-05 10:00 | 2026-09-08 00:00 | 2026-08-25 09:16 | Sat |
| E08 | SEASONS | New content | This update will include seasons. | 2026-09-12 20:00 | 2026-09-16 20:00 | 2026-09-05 18:12 | Sat |
| E09 | BONDS | UPDATE | Trade debt, earn interest, weigh the risk. | 2026-09-19 20:00 | 2026-09-26 02:00 | 2026-09-13 00:43 | Sat |
| E10 | COMMODITIES EXCHANGE | NEW UPDATE | Prices will be driven by new news events, such as weather reports and more | 2026-09-26 20:00 | 2026-09-29 16:00 | 2026-09-20 14:39 | Sat |
| E11 | UI Overhaul + Features | Content Update | This update will feature a brand new interface for the game, reorganized interfaces, and new game features! | 2026-10-03 06:00 | 2026-10-09 04:00 | 2026-09-27 21:40 | Sat |
| E12 | Custom Offices | New Update | Your own 3d office you can walk inside of and upgrade | 2026-10-10 20:00 | 2026-10-16 23:00 | 2026-10-03 09:08 | Sat |

推导:12 条里 8 条周六开始,且 2026-08-22 到 2026-10-10 每个周六都有一条开始;另 4 条在周一/周三(08-17、08-19、08-26、09-02)。Custom Offices 是今天(10-08)之后唯一未开始的一条;UI Overhaul + Features 的 listing 到 10-09 04:00 UTC 才结束。描述里的 "permeant" 是开发者原拼写。REAL ESTATE 描述写 "global map",配图却是美国地图 + "50 STATES"(见下节,矛盾已记录)。

## 8. 官方图片(S;开发者上传到 Roblox 的宣传图 / 活动配图;图中文字为本人逐张看图抄录,小字放大后核对)

游戏页缩略图来源:https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=10495391267&countPerUniverse=10&size=768x432&format=Png;活动配图来源:https://thumbnails.roblox.com/v1/assets?assetIds=121284725743266,125686998013653,138795582610576,139806771152562,115813324738139,87490447307325,123328159651891,132073765112234,113157896906250,122510452839688,80151539995844,127393833886466&size=768x432&format=Png(mediaId 取自活动 listing 的 thumbnails[].mediaId);图标:https://thumbnails.roblox.com/v1/games/icons?universeIds=10495391267&size=512x512&format=Png

| key | 画面与图中文字(本人看图) | URL(768×432) | 级 |
|---|---|---|---|
| th1 | 单只股票卡片:代码 OBBY、公司名 Obby Dynamics、价格 154.87、+6.47 (4.35%)、LIVE;K 线图,周期 1D 1W 1M 3M 1Y ALL;绿色 BUY、红色 SELL;BUYING POWER $532,456;PORTFOLIO VALUE $1,247,891;MARKET OPEN | https://tr.rbxcdn.com/180DAY-372b4db32bb2a0c404902c94c98f91a5/768/432/Image/Png/noFilter | S |
| th2 | 交易终端:左上 RSE EXECUTIVE,标签 Trade / Discover / Portfolio,NET WORTH $124,850;OBBY STOCK 168.42;周期 1m 5m 15m 1H 1D,Indicators / Compare / Save / Listen;右侧 Trades LIVE(All / Whales / You),BUY 78% / 22% SELL;Long / Short 切换,按钮 Buy OBBY;底部标签 Positions / Orders / History / P&L / Feed / News;持仓行 SIDE LONG、SIZE 1,000、AVG PRICE 159.66、P&L +$8,760,红色 Close 按钮 | https://tr.rbxcdn.com/180DAY-a9c036ca3582a1172abeaf1aa29f0d65/768/432/Image/Png/noFilter | S |
| th3 | 暴跌 K 线 + 红色大字 -48.7% TODAY;绿色大 BUY、红色小 SELL | https://tr.rbxcdn.com/180DAY-1425f129f6ee253c234930ce645ee8e6/768/432/Image/Png/noFilter | S |
| th4 | $100 → $1,284,593 的绿色箭头,上涨 K 线,绿色 BUY | https://tr.rbxcdn.com/180DAY-7647c220050d0bade4122235790e71ad/768/432/Image/Png/noFilter | S |
| th5 | 面板拼贴:Market Overview、Portfolio $85,355.45、Top Movers(RBIX/BLOX/RBLX/TIX/INDEX 等小字,未采用)、Market Sentiment 仪表 Bullish、Trade(Amount $10,000、Leverage 5x、BUY / SELL)、Holdings、Market Activity;中央白色上涨图标;现金与金币 | https://tr.rbxcdn.com/180DAY-dbb508c1d8dd413050d120b50015ee1d/768/432/Image/Png/noFilter | S |
| ev_hedge | 标题 Run a hedge fund;副题 "Name it, pick a strategy, and specialise it three tiers deep.";页脚 4 STRATEGIES · 3 TIERS EACH · RSE STOCK 2;四张卡:MOMENTUM "Compound expertise faster from profitable manual closes."(MASTERY & CLOSE XP +10% / +20% / +30%);QUANT "Sharper algorithmic execution: your bots pay less commission."(BOT COMMISSION -5% / -10% / -15%);INCOME "Boost dividends and Treasury Desk interest."(DAILY INCOME +10% / +25% / +45%);VENTURE "Launch player-founded companies with more simulated-investor hype."(LAUNCH HYPE +5 / +10 / +15) | https://tr.rbxcdn.com/180DAY-268547a21276a80d562ce5b413cac169/768/432/Image/Png/noFilter | S |
| ev_script | 标题 Scripting overhaul;副题 "Write it once. The chart draws every line of it.";页脚 48 FUNCTIONS · 10 SOURCES · RSE STOCK 2;SCRIPT EDITOR 里一段 MACD 脚本;六个计数:48 FUNCTIONS、10 PRICE SOURCES、10 PLOTS / SCRIPT、3 PLOT STYLES、40 NAMED VALUES、8 LINE COLOURS | https://tr.rbxcdn.com/180DAY-21e042de0d7e6c629cf671d3a2b2d355/768/432/Image/Png/noFilter | S |
| ev_challenges | 标题 Challenges;副题 "Start small, hit the number, keep what nobody else can buy.";页脚 4 TIERS · UP TO 10,000x · RSE STOCK 2;CHALLENGE RUN · TIER III · THE FLOOR,START $5K → TARGET $5M,1,000x;THE LADDER:I BOOTSTRAP 25x、II SIZE UP 100x、III THE FLOOR 1,000x、IV WHALE 10,000x;"Challenge-only cosmetics — Not in the shop. Not on the item market." | https://tr.rbxcdn.com/180DAY-3f21c97d8404c5d0533c4d5ac12e325a/768/432/Image/Png/noFilter | S |
| ev_tools | 标题 New tools;副题 "Trailing stops that follow the run, and fibs that find the fade.";页脚 8 NEW TOOLS · 14 ON THE CHART · RSE STOCK 2;列表:TRAILING STOP、FIB RETRACEMENT、FIB EXTENSION、POSITION TOOL、RECTANGLE ZONE、RAY、PARALLEL CHANNEL、TEXT NOTE | https://tr.rbxcdn.com/180DAY-d750ae19911ec713b4adfa27f18e18bf/768/432/Image/Png/noFilter | S |
| ev_wire | 标题 The wire;副题 "What the market expected, what printed, and what it did about it.";页脚 NEWS OVERHAUL · 8 NEW · RSE STOCK 2;THE WIRE · LIVE,头条 Obby Corp beats on earnings and raises guidance(CONSENSUS / ACTUAL / SURPRISE);列表:THE WIRE、CONSENSUS、THE SURPRISE、ON YOUR BOOK、STORY TO CHART、SOURCES、IMPACT PRINTED、REACTION REPLAY | https://tr.rbxcdn.com/180DAY-d8e6a78f97ce74d41bb64af3fed61821/768/432/Image/Png/noFilter | S |
| ev_empire | 标题 Empire Map;副题 "Buy the block. Collect the rent. Own the country.";页脚 50 STATES · TILE BY TILE · RSE STOCK 2;美国形状的像素地图,5 个地产标注及日租(示意数据,未采用) | https://tr.rbxcdn.com/180DAY-e81bd0b436c2dc5d8d993b16f5150192/768/432/Image/Png/noFilter | S |
| ev_seasons | 标题 Seasons;副题 "Every Monday the board goes back to zero. Rank on return, not balance.";页脚 SEASONS UPDATE · 7-DAY LADDER · RSE STOCK 2;SEASON 1 排行榜(示意玩家名,未采用),RESETS MONDAY;列表:WEEKLY RESET、RANKED ON RETURN、SIX TIERS "from Paper Hands up to The Floor"、YOUR DIVISION、RANK BADGE、PLACEMENT WEEK、SEASON REWARDS、SEASON RECAP | https://tr.rbxcdn.com/180DAY-f55adaff6497ba8feeaf15467e85b93b/768/432/Image/Png/noFilter | S |
| ev_bonds | 标题 Introducing bonds.;副题 "Trade debt. Earn interest. Weigh the risk.";三张卡:GOVERNMENT BONDS AAA "Government debt. Lower credit risk.";CORPORATE BONDS BBB "Investment-grade debt. Back the business.";HIGH-YIELD BONDS BB "Higher potential yield. Higher default risk."(页脚含 coming-soon 字样,正文与 alt 不抄,免得触发占位语门禁) | https://tr.rbxcdn.com/180DAY-9822c6b389da34e4f460c196d4091f58/768/432/Image/Png/noFilter | S |
| ev_commodities | 标题 Introducing commodities.;副题 "Trade the harvest. Watch the weather. Ride the shock.";三张卡:ENERGY OIL "Crude, gas and power. Moves on supply shocks.";METALS GOLD "Gold, silver and copper. Where money hides.";AGRICULTURE WHEAT "Wheat, coffee and lumber. Trade the harvest."(页脚同上) | https://tr.rbxcdn.com/180DAY-dee559a4e85d3bf24f9277c0990551ad/768/432/Image/Png/noFilter | S |
| ev_ui | 标题 The terminal, reimagined.;副题 "Live order flow. Pro charts. Every market on one screen.";RSE STOCK 2 · NEW ON ROBLOX;下方是新终端宽幅截图(小字放大后仍模糊,只采用左上角 RSE EXECUTIVE,其余不引) | https://tr.rbxcdn.com/180DAY-5431ba7effb1d21e89c1b87130ad082f/768/432/Image/Png/noFilter | S |
| ev_office | 黄昏的转角办公室:落地窗外城市天际线、带上涨行情显示器的办公桌、办公椅、刻有 RSE 的底座上的铜牛;无说明文字 | https://tr.rbxcdn.com/180DAY-5dd1e65cf8ab2df0712cfc4a8869dc1e/768/432/Image/Png/noFilter | S |
| icon | 上涨箭头形状的拼图:K 线图、芯片、太阳能板、数据服务器、园区建筑 | https://tr.rbxcdn.com/180DAY-78f78579c7191ea99ca1a6eace72525b/512/512/Image/Png/noFilter | S |

说明:活动配图是更新前做的宣传图,图里的数值(层级倍率、佣金百分比等)代表「开发者打算上线的样子」,实装可能不同——正文凡引用都写明「the art shows」。NEW MEMECOINS 的配图只有一个问号,未入池。33 个图片 URL 2026-10-08 逐个 curl 200(raw/image-check.txt)。

## 9. 开发者与社区

| # | 事实 | 值 / 原文摘录(英文原句逐字) | 来源 URL | 取得日 | 级 |
|---|---|---|---|---|---|
| F031 | 群组资料 | name `Summit Productions Development`;description 空串;shout null;memberCount 276,709;publicEntryAllowed true;hasVerifiedBadge false;communityTier.currentTier 3 | https://groups.roblox.com/v1/groups/33446529 | 2026-10-08 | S |
| F032 | 群组创建日 | `2023-11-28T20:59:24.157Z` | https://groups.roblox.com/v2/groups?groupIds=33446529 | 2026-10-08 | S |
| F033 | 群主 | userId 6019489864,username `SummitGroupHoIder`(第 12 位是大写 I),账号创建 `2024-05-12T21:10:23.58Z`,个人简介空 | https://groups.roblox.com/v1/groups/33446529;https://users.roblox.com/v1/users/6019489864 | 2026-10-08 | S |
| F034 | 群组角色名 | Guest、Member、Client、Staff、Contracted Developer、Developer、Operations Director、President、Holder(各角色人数接口有给,Client 的计数大于群总人数,不可靠,未采用) | https://groups.roblox.com/v1/groups/33446529/roles | 2026-10-08 | S |
| F035 | 群组公开体验 5 个 | Legacy: Roblox Stock Exchange(2025-05-23,8,600 visits); INDEFINITE | Dreamcore 🌫️ Backrooms 🚪(2025-11-18,14,346 visits); Rocket Wars Tycoon(2026-05-05,512,502 visits); Roblox Stock Exchange 2(2026-07-13,5,093,566 visits); Hex(2026-07-24,740,416 visits) | https://games.roblox.com/v2/groups/33446529/games?accessFilter=Public&limit=50 | 2026-10-08 | S |
| F036 | 前作描述(只用于提醒别混用) | 「Legacy: Roblox Stock Exchange」描述含 "Options Chain for advanced trading (2 Rebirths)"、"Options Chain unlocks at 2 Rebirths"、"Measuring Tool unlocks at 1 Rebirth" —— 属于前作,不适用于 2 代 | https://games.roblox.com/v2/groups/33446529/games?accessFilter=Public&limit=50 | 2026-10-08 | S |
| F037 | 群组 wall | v1 / v2 wall/posts 均 404(errors code 0)→ 未获取,不能归因为需登录 | https://groups.roblox.com/v2/groups/33446529/wall/posts?limit=10&sortOrder=Desc | 2026-10-08 | S |
| F038 | 社交链接 | 游戏与群组 social-links 接口均 401 "Authentication token is missing" → 未获取 | https://games.roblox.com/v1/games/10495391267/social-links/list | 2026-10-08 | S |
| F039 | Roblox 文档:社交链接可见性 | "Social media links are only visible to users who have verified their age as at least 16 years old." | https://create.roblox.com/docs/production/promotion/social-media-links | 2026-10-08 | S |
| F040 | Roblox 文档:通行证定义 | "Passes let you charge users a one-time Robux fee to access special privileges inside your game, such as entry to a restricted area, an in-game avatar item, or a permanent power-up." | https://create.roblox.com/docs/production/monetization/passes(由 /game-passes 301 而来) | 2026-10-08 | S |
| F041 | Roblox 文档:开发者商品定义 | "A developer product is an item or ability that a user can purchase more than once, such as in-game currency, ammo, or potions." | https://create.roblox.com/docs/production/monetization/developer-products | 2026-10-08 | S |
| F042 | Roblox 文档:徽章定义 | "A badge is a special award you can gift players when they meet a goal within your game, such as completing a difficult objective or playing for a certain amount of time." | https://create.roblox.com/docs/production/publishing/badges | 2026-10-08 | S |
| F043 | Roblox 文档:活动通知 | "Players can discover your events on the experience's detail page and through an event details page, and they can opt into notifications that they'll receive when your event begins." | https://create.roblox.com/docs/production/promotion/experience-events | 2026-10-08 | S |
| F044 | Discord 邀请 qR8v6Murp3 | 服务器名 `Roblox Stock Exchange 2`,自述 "Official server for RSE: Roblox Stock Exchange 2",约 1,231 成员 / 182 在线,expires_at null;邀请线索来自 Pro Game Guides 与 Try Hard Guides。Roblox 站内无法自证 → 页面写「calls itself official」 | https://discord.com/api/v9/invites/qR8v6Murp3?with_counts=true | 2026-10-08 | B |
| F045 | Google 下拉词(需求证据) | roblox stock exchange 2 codes / promo codes / discord / wiki / how to play / how to sell / best bot settings / bot settings / indicator / method / strategy / tips / tutorial / guide / is ... realistic / script / script pastebin(后两个不做) | https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=roblox+stock+exchange+2(raw/suggest.jsonl) | 2026-10-08 | B |

## 互相矛盾

| 项 | 说法 A | 说法 B | 处理 |
|---|---|---|---|
| 「最近更新」时间 | games API `updated`:24 分钟内三读三值(03:36 / 03:44 / 03:56 UTC) | 群组游戏列表接口同字段:2026-09-30T00:00:33Z | 两个都不当补丁日;更新史只用官方活动 listing 与商品/徽章创建日 |
| REAL ESTATE 的范围 | 活动描述:"buy real estate across a global map"(S) | 同一活动配图:美国地图、"50 STATES"(S) | 两个都如实写,注明未核实实装是哪一个 |
| 活跃码数量 | 官方描述:只有 TOOLS(S) | 码站:6–7 个(C),且两站不含 TOOLS | 码表只收 TOOLS;其余在正文点名为「未核实、不收录」 |
| FUTURES 码奖励 | Roblox Den:20,000 Cash and 20 XP(C) | PGG / Twinfinite:10k Cash(C) | 都不采用,只作为「码站互相打架」的例子 |
| 同名通行证 / 商品价格 | VIP 通行证 229、Order Flow 199、Watchlist Pro 49、Executive Terminal 159(S) | 同名开发者商品 399 / 249 / 99 / 139(S) | 两套都是官方数据,并列写,提醒读者看购买弹窗价格;用途未获取 |
| 徽章数量 | 官方接口 11 个(S) | robloxstockexchange2.wiki 列 10 个(漏 Met the game owners!)(C) | 以 S 为准 |
| 开发者拼写 | 商品「Instant Acension」、活动描述「permeant perk」(S) | 正常拼写 Ascension / permanent | 照抄原拼写并注明 spelled that way |

## 未核实(线索,不进正文或只以 not stated / not confirmed 出现)

| 项 | 线索来源 | 为什么不写 |
|---|---|---|
| TOOLS 的奖励(20K Cash) | Roblox Den(C) | 官方描述没写;单一 C 来源 |
| 其余 6 个码是否有效及奖励 | 四个码站(C) | 无官方出处,奖励互相矛盾 |
| 兑换入口(右上角礼物图标 → ENTER CODE) | 三个码站(C) | 无 S/A;10-03 界面大改后可能已变 |
| 不买通行证时的手续费率 | — | 只有 Pro Trader 的 0.02% |
| 各等级的杠杆上限 | — | 只有 Max Leverage 的 "50x at any level";ev_ui 小字里疑似有 1x–100x 档位但放大仍模糊,不引 |
| 等级 / XP 表、每日奖励数额 | — | 无来源 |
| rebirth 的条件、重置内容、收益;「Instant Acension」是什么 | — | 无来源 |
| bot 的解锁条件、设置项、收益、游戏内现金价;bot 是否在离线时交易 | Google 下拉有 best bot settings 需求 | 无任何一手来源;不抄社区设置 |
| Simulate Day / Week 对持仓、bot、利息的具体影响;开市时间 | — | 只有商品名 |
| Trader Spotlight、Skip Recovery、Double Earnings、Trader Starter Pack 的效果与时长 | — | 只有商品名与价格 |
| 同名商品是不是赠送版 | — | 接口无描述 |
| 界面按钮位置(Long/Short、Close 等) | 官方缩略图 th2(S,但属宣传图且为旧界面);robloxstockexchange2.wiki 的 captured gameplay 标签(C) | 10-03 换了新界面,未进游戏核对 → 正文写「art shows…not confirmed in the live game」 |
| 各更新是否在活动起始时刻实装;赛季时长、挑战奖励细节、债券/商品/地产的具体数值 | 活动配图(S,宣传) | 宣传图 ≠ 实装;只以 the art shows 口径出现 |
| 支持设备、私服 | — | 匿名接口读不到 / 字段不可靠 |
| Discord 是否为开发者所挂 | Discord API(B) | Roblox social links 401 |
| 群组 wall、Discord 频道、开发者 X/YouTube | — | 404 / 需登录 / 未找到官方账号 |
| 搜索量 / KD | — | 未用 Semrush(dash.3ue.com),不估算 |

