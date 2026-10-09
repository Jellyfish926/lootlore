# emotes 核验

48 条命题，1 条被推翻，2 条未验。（取证窗口 2026-10-09T22:55Z–23:05Z；P 编号沿用写手，V 为我补的。）

NEWS=我自己重取的 ISteamNews（count=100，返回 count=63，63 条）；STATS=steamcommunity.com/stats/3419430/achievements/；ACH=GetGlobalAchievementPercentagesForApp；公告引文均在接口 contents 原文中检索（去掉 BBCode 加粗标记后比对）。

| 编号 | 命题 | 验证路径 | 结果 | 证据 | 取证时间 |
|---|---|---|---|---|---|
| P1 | 官方用法：悬停自己的猫 | NEWS 1811772772443374 | CONFIRMED | "You can find your emojis in the bottom of your cosmetics tab! And you can use them by hovering a bit over your Bongo Cat in a multiplayer lobby."（2025-10-01 13:36 UTC） | 2026-10-09T22:59:53Z |
| P2 | 三条补丁说明含 "emote wheel" | NEWS 1811772772604122 / 1813041031365431 / 1840310314350721 | CONFIRMED | 三条均含 emote wheel | 2026-10-09T22:59:53Z |
| P3 | 无公告给出表情快捷键 | NEWS 13 条 | CONFIRMED | 在 13 条里检索 hotkey/shortcut/keybind/F键/key 与 emo 同句：0 命中（唯一近似命中是 09-01 公告的 "emote speed slider" 句，不是快捷键） | 2026-10-09T22:59:53Z |
| P4 | 送 4 个 emoji、最多 2 分钟 | NEWS 1811772772443374 | CONFIRMED | "you will receive 4 emojis as a starter pack"；"up to 2min" | 2026-10-09T22:59:53Z |
| P5 | 加入 100 多个 emoji 到道具池 | 同上 | CONFIRMED | "We have added over 100 new emojis to the item pool"（原文 over 与数字间有加粗标记，语义相同） | 2026-10-09T22:59:53Z |
| P6 | 10-06 emotes 有独立收藏分类 | NEWS 1811772772604122 | CONFIRMED | "Adds emotes as their own category in the collection"；2025-10-06 11:43 UTC | 2026-10-09T22:59:53Z |
| P7 | 2026 年 6 月、9 月改版 | NEWS 1834602721190507 / 1842212951313382 | CONFIRMED | "Improved experience for the inventory, settings, multiplayer ui"；标题 "New UI and monthly Skins, Hats and Emotes!" | 2026-10-09T22:59:53Z |
| P8 | 上线时表情绑定大厅 | NEWS 1811772772443374 | CONFIRMED | "Adds emojis that you can use in Meowtiplayer Lobbies." | 2026-10-09T22:59:53Z |
| P9 | 07-12 表情回到单人 | NEWS 1837955055360738 | CONFIRMED | "Brought back emotes to singleplayer (sorry on that note)"；2026-07-12 08:38 UTC | 2026-10-09T22:59:53Z |
| P10 | 没有公告说表情何时在单人失效 | NEWS 2025-10-01 至 2026-07-12 | CONFIRMED | single-player/alone/solo 检索：仅命中 1835236783574334（"developed this game solo"，说别的游戏）与 1829528821315214（"standalone DLC"，子串命中），均与表情无关 | 2026-10-09T22:59:53Z |
| P11 | 10-02 移出池并宣布第二宝箱 | NEWS 1811772772484130 | CONFIRMED | "removing Emojis from the drop pool RIGHT NOW"；"a SECOND chest which will ONLY contain emotes that will show up once you are in a multiplayer lobby"（粗体标记隔开 ONLY，语义相同）；2025-10-02 09:39 UTC | 2026-10-09T22:59:53Z |
| P12 | 第二宝箱 10-06 上线 | NEWS 1811772772604122 | CONFIRMED | "Adds a second chest, just for emojis" | 2026-10-09T22:59:53Z |
| P13 | 开朋友 emote 宝箱 1000 点击，双方须更新 | NEWS 1837955055360738 | CONFIRMED | "You can open up your friend's emote chests now (it costs you 1000 clicks, for your friend it's free; both must update their game)" | 2026-10-09T22:59:53Z |
| P14 | 自己 emote 宝箱的计时/点击成本/概率官方没写 | NEWS 13 条检索数字 | CONFIRMED | 与 chest/emoji/emote 同句的数字仅：100（池）、4（starter）、1000（友人宝箱）、3（UI 主题）；无分钟数、无百分比 | 2026-10-09T22:59:53Z |
| P15 | 商店掉率表不含 emote/emoji 字样 | appdetails about_the_game | CONFIRMED | 全文不含 emot、emoji；含 "Item drop pool chances*" 档位 | 2026-10-09T22:59:53Z |
| P16 | Paw Pass 含 emotes 与 emote 宝箱 | NEWS 1842212951313382 | CONFIRMED | "cosmetic/emote chests with up to legendary rarity" | 2026-10-09T22:59:53Z |
| P17 | UI 主题本月稍后进 emote 宝箱 | NEWS 1845383656381895 | CONFIRMED | "Later this month, they will be added to drop in the **emote chest**! So you will be able to collect all 3 of them"；2026-10-01 15:43 UTC | 2026-10-09T22:59:53Z |
| P18 | 截至取数没有后续公告 | NEWS | CONFIRMED | 最新一条为 1845383656381895（2026-10-01） | 2026-10-09T22:59:53Z |
| P19 | 63 条中 13 条含 emote/emoji | NEWS 全文 emot\|emoji | CONFIRMED | 恰 13 条，gid 与写手清单逐一相同；count=63 | 2026-10-09T22:59:53Z |
| P20 | 时间线表 13 行日期与标题 | NEWS | CONFIRMED | 13 条 date(UTC)/title 逐字核对一致：Emojis!!!(10-01)、Emojis 2.0, and a sorry.(10-02)、Emote 2.0 and bug fixes(10-06)、Bongo Cat 🍂Autumn Event🍂(10-08)、Small fixes(10-14)、Bongo Cat ❄Winter Event & Advent Calendar❄(2025-12-01)、Private Lobbies, Cosmetic Preview and QoL Changes(2026-01-14)、Steam Typing Fest(02-05)、Meowtiplayer Chat, DLC Release, Collection Bundle(04-13)、Pat Your Friends(07-12)、Multiplayer Layout Settings(08-10)、New UI and monthly Skins, Hats and Emotes!(09-01)、UI THEMES are here!(10-01) | 2026-10-09T22:59:53Z |
| P21 | 10-08 引文 | NEWS 1813041031167641 | CONFIRMED | "Adds an emoji exchange (emojis will trade up to other emojis)" | 2026-10-09T22:59:53Z |
| P22 | 10-14 两句引文 | NEWS 1813041031365431 | CONFIRMED | "Fixes the emote wheel, it should pop up more consistent"；"Fixes the exchange mixing things up with emojis and non emojis" | 2026-10-09T22:59:53Z |
| P23 | 12-01 引文 | NEWS 1817483467044521 | CONFIRMED | "Fixes a bug with emoji chests not dropping anymore" | 2026-10-09T22:59:53Z |
| P24 | 01-14 引文 | NEWS 1821922921810120 | CONFIRMED | "Emotes get scaled with ui" | 2026-10-09T22:59:53Z |
| P25 | 02-05 引文 | NEWS 1823825466497567 | CONFIRMED | "Fixed multiplayer emoji UI scale" | 2026-10-09T22:59:53Z |
| P26 | 04-13 聊天与表情可在多人页签关闭 | NEWS 1829528821315214 | CONFIRMED | "disable the chat and emotes directly in the multiplayer tab" | 2026-10-09T22:59:53Z |
| P27 | 08-10 引文 | NEWS 1840310314350721 | CONFIRMED | "Fixed randomly resetting emote wheel" | 2026-10-09T22:59:53Z |
| P28 | 09-01 emote speed slider 与关闭自己猫的表情 | NEWS 1842212951313382 | CONFIRMED | "added an emote speed slider (multiplayer settings)"；"clicking your own cat can be fine tuned, you can now turn off emotes, the patting itself and the “Meow Meow”" | 2026-10-09T22:59:53Z |
| P29 | 10-01 可静音其他玩家 | NEWS 1811772772443374 | CONFIRMED | "Adds an option to mute other players in your lobby." | 2026-10-09T22:59:53Z |
| P30 | 玩家被隐藏时表情不生成 | NEWS 1811772772604122 | CONFIRMED | "Emotes now don't spawn if players are hidden" | 2026-10-09T22:59:53Z |
| P31 | update and restart 按钮 | NEWS 1811772772443374 | CONFIRMED | 原文含 "update and restart" | 2026-10-09T22:59:53Z |
| P32 | 四条公告以提醒更新结尾 | NEWS 1813041031167641 / 1837955055360738 / 1840310314350721 / 1845383656381895 | CONFIRMED | 四条均含 "update your game" | 2026-10-09T22:59:53Z |
| P33 | 成就显示名：三条 Emoter、一条 Sparkly Emoter | STATS | CONFIRMED | "Emoter / Use emojis 10 times."、"Emoter / Use emojis 100 times."、"Emoter / Use emojis 1.000 times."、"Sparkly Emoter / Use emojis 10.000 times." | 2026-10-09T22:59:53Z |
| P34 | 统计页百分比 13.0/7.0/2.3/1.0 | STATS | CONFIRMED | 我取到 13.0% / 7.0% / 2.3% / 1.0%，与草稿完全一致 | 2026-10-09T22:59:53Z |
| P35 | 接口百分比 13.0/6.9/2.3/1.0 | ACH | CONFIRMED | EMOTER_10=13.0；EMOTER_100=6.9；EMOTER_1000=2.3；EMOTER_10000=1.0 | 2026-10-09T22:59:53Z |
| P36 | 接口只给内部名 | ACH | CONFIRMED | 响应仅 name/percent 两字段，无显示名 | 2026-10-09T22:59:53Z |
| P37 | 推导：6.9÷13.0≈53%；1.0÷13.0≈8%；28−4=24 | 算式 + ACH 条目数 | CONFIRMED | 6.9/13.0=53.1%；1.0/13.0=7.7%（≈8%）；ACH 28 条，STATS 28 行，28−4=24 | 2026-10-09T22:59:53Z |
| P38 | 官方没写"一次使用"的计数规则 | NEWS 13 条 + STATS 说明 | UNVERIFIED | 13 条公告里无计数规则、STATS 仅 "Use emojis N times."；但全称否定只覆盖我读到的两处，成就描述的游戏内版本不在允许来源 | 2026-10-09T22:59:53Z |
| P39 | 10-02 说拆分掉落池 | NEWS 1811772772484130 | CONFIRMED | "We will split up the drop pool for hats/skins and emojis." | 2026-10-09T22:59:53Z |
| P40 | 十换一规则出自 2025-02-23 demo 更新 | NEWS 1792116353300258 | CONFIRMED | "Adds exchanges (10 items of the same rarity can be upgraded to one of a higher tier)"；2025-02-23 20:24 UTC，早于 2025-10-01 | 2026-10-09T22:59:53Z |
| P41 | 13 条未提 emoji 好友交易/市场出售 | NEWS 13 条检索 trade/market/sell/gift | UNVERIFIED | 命中项：10-02 "trade up your emojis"（兑换）、10-08 "trade up to other emojis"（兑换）、09-01 "gift the pass ticket…Steam's trading feature"（通行证票）、08-10 "players couldn't be gifted"（Multiplayer Popup 设置，语境未判明与表情无关，需人工看原文）；无 market/sell 命中。其余命中均与 emoji 交易无关，但 08-10 一句无法排除，故不判 CONFIRMED | 2026-10-09T22:59:53Z |
| P42 | emoji 总数只有 "over 100" | NEWS 13 条 | CONFIRMED | emoji 邻近数字仅 100 | 2026-10-09T22:59:53Z |
| P43 | 宝箱称呼混用 | NEWS | CONFIRMED | 1817483467044521 "emoji chests"；1837955055360738 "emote chests"；1845383656381895 "emote chest" | 2026-10-09T22:59:53Z |
| V1 | 草稿「Oct 1, 2025 … option to mute other players」及「starter pack 4」并入时间线表 | 见 P4、P29 | CONFIRMED | 同上 | 2026-10-09T22:59:53Z |
| V2 | 草稿「June and September 2026」界面改版（正文第二段） | 见 P7 | CONFIRMED | 同上 | 2026-10-09T22:59:53Z |
| V3 | 草稿「The October 2 post had already said the drop pool … would be split」 | 见 P39 | CONFIRMED | 同上 | 2026-10-09T22:59:53Z |
| V4 | 「six days later」（10-08→10-14） | 日期差 | CONFIRMED | 2025-10-08 与 2025-10-14 相差 6 天 | 2026-10-09T22:59:53Z |
| V5 | 所有"read on October 10, 2026"取数日期（含 scope、tldr「on October 10, 2026 the rarest, Sparkly Emoter, stood at 1.0%」、表前「both sources were read on October 10, 2026」、「As of October 10, 2026」） | 写手 raw/mlsd-emotes-fetch.time；本机时钟 | REFUTED | 反例：写手取数时间戳 2026-10-09T22:40:07Z，我取数 2026-10-09T22:55Z–23:05Z，UTC 日期均为 10 月 9 日；10 月 10 日是北京时间。草稿 scope 与表头声明「dates are UTC」，此处与之矛盾。frontmatter checkedAt/date 同 | 2026-10-09T22:59:53Z |

## 机检
① 外链 17 个（正文去重后 16 个 + frontmatter 的 appdetails）：正文 16 个全部 HTTP 200，均在 sourceUrls 内；sourceUrls 里的 https://store.steampowered.com/api/appdetails?appids=3419430 在正文中未被引用（正文只写「store page prints drop chances」未挂链接），curl 同为 200。
② 站内链接 6 个：multiplayer、hats-skins、paw-pass、steam-error、achievements、exchange-trading，均在允许清单内；无 market-prices。
③ 时效词 now/currently/upcoming/soon/latest/recently：正文 0 处（"Later this month" 为引文，已带 2026-10-01 日期）。
④ 市场价格：正文无 Steam Community Market 价格结论。
