# mac-linux-steam-deck 核验

38 条命题，1 条被推翻，4 条未验。（取证窗口 2026-10-09T22:55Z–23:05Z；命题编号沿用写手 P1–P32，另加我补的 V1–V6。）

缩写：NEWS=我自己重取的 ISteamNews（count=100，返回 count=63、63 条、gid 无重复，全文已逐条正则检索）；APP=appdetails&l=english；DECK=ajaxgetdeckappcompatibilityreport；SEARCH=store 搜索页。

| 编号 | 命题 | 验证路径 | 结果 | 证据 | 取证时间 |
|---|---|---|---|---|---|
| P1 | platforms windows/mac true、linux false | APP | CONFIRMED | {"windows":true,"mac":true,"linux":false} | 2026-10-09T22:59:13Z |
| P2 | 商店页只有 Windows 与 Mac 平台图标 | store.steampowered.com/app/3419430/Bongo_Cat/ | CONFIRMED | HTML 中 platform_img 仅 win、mac 各 1 | 2026-10-09T22:59:13Z |
| P3 | 03-23 公告含实验性 Mac 句 | NEWS gid 1827626365763660 | CONFIRMED | "With this update we will launch an experimental mac build that you can try out."；日期 2026-03-23 14:40 UTC | 2026-10-09T22:59:13Z |
| P4 | 03-23 之后无公告说 Mac 脱离实验性 | NEWS 全文检索 \bmac\b\|macos | CONFIRMED | 全 63 条中 mac 只命中 1827626365763660 一条；之后 0 命中（另查 apple/osx/macbook 0 命中） | 2026-10-09T22:59:13Z |
| P5 | Irox Games、免费 | APP | CONFIRMED | developers=["Irox Games"]，is_free=true | 2026-10-09T22:59:13Z |
| P6 | 发行日 Mar 5, 2025 | APP；NEWS 1793384379332669 | CONFIRMED | release_date.date="Mar 5, 2025"；公告 "Bongo Cat is out meow!!!" 2025-03-05 08:00 UTC | 2026-10-09T22:59:13Z |
| P7 | Mac 最低配置六项 | APP mac_requirements.minimum | CONFIRMED | OS 11.0 / Intel 64-Bit or Apple silicon / 1 GB RAM / Graphics - / Broadband Internet connection / 700 MB available space | 2026-10-09T22:59:13Z |
| P8 | Mac 推荐配置 OS 13.0，其余同最低 | APP mac_requirements.recommended | CONFIRMED | OS 13.0，其余五项与最低逐字相同 | 2026-10-09T22:59:13Z |
| P9 | Windows 存储 100 MB；七倍 | APP pc_requirements | CONFIRMED | "Storage: 100 MB available space"（最低与推荐均是）；700÷100=7 | 2026-10-09T22:59:13Z |
| P10 | Mac Issues 帖：开发者发布、03-23 开帖、05-25 最后编辑、置顶、Input Monitoring | steamcommunity.com/app/3419430/discussions/0/806846367620396268/ | CONFIRMED（年份除外，见 V6） | 作者 Spiced Pigeon，带 commentthread_author_developer 与 "[developer]" 徽章；"Mar 23 @ 7:39am"；"Last edited by Spiced Pigeon; May 25 @ 10:17am"；页面含 "This topic has been pinned"；正文 "Input Monitoring…grant permissions to Steam and Bongo Cat" | 2026-10-09T22:59:13Z |
| P11 | 移植动机句 | NEWS 1827626365763660 | CONFIRMED | "I know a lot of you want to play with your friends (that are on Mac or Linux)." | 2026-10-09T22:59:13Z |
| P12 | 公告没有明说 Mac/Windows 同房 | NEWS 检索 cross、platform | CONFIRMED | "platform" 0 命中；"cross" 仅命中 Tap Tap Loot 的 "cross collab" 与 Red Cross 修复，均与跨平台无关 | 2026-10-09T22:59:13Z |
| P13 | Linux 配置块为空 | APP linux_requirements | CONFIRMED | minimum 与 recommended 均为 <ul class="bb_ul"></ul>（无 li） | 2026-10-09T22:59:13Z |
| P14 | Linux 测试帖标题/作者/日期/置顶/正文 | steamcommunity.com/app/3419430/discussions/0/573792389464878955/ | CONFIRMED | 标题 "Linux Testing X11"；作者 Spiced Pigeon [developer]（开发者标）；"Jun 10 @ 1:02am"；页面含 "This topic has been pinned"；正文 "Hello we have a linux version that you can test. The beta code is: linuxtesting / Only works on X11 right now but we would love to get more testers on board!" | 2026-10-09T22:59:13Z |
| P15 | 该帖只有这三句、无安装步骤/发行版/配置 | 同上首帖 | CONFIRMED | 首帖正文仅上述两段文字，无其他内容（回复不计） | 2026-10-09T22:59:13Z |
| P16 | 06-05 公告：X11 的 Linux 更新临近、Wayland 更晚 | NEWS 1834602721190507 | CONFIRMED | "Linux update will be out soon (for X11). Wayland will take more time."；2026-06-05 12:19 UTC | 2026-10-09T22:59:13Z |
| P17 | 06-05 之后恰 7 条公告、全不含 Linux/X11/Wayland | NEWS | CONFIRMED | 12:19 之后：06-16、06-27、07-12、08-10、09-01、09-18、10-01 共 7 条；linux\|x11\|wayland 0 命中 | 2026-10-09T22:59:13Z |
| P18 | DECK resolved_category=2 | DECK | CONFIRMED | "resolved_category":2 | 2026-10-09T22:59:13Z |
| P19 | 搜索过滤器 3=Verified、2=Playable（Valve 一手） | SEARCH ?term=bongo+cat | CONFIRMED | data-param="deck_compatibility" data-value="3" data-loc="Verified"；data-value="2" data-loc="Playable" | 2026-10-09T22:59:13Z |
| P20 | Playable 过滤搜得到、Verified 搜不到 | SEARCH …&deck_compatibility=2 / =3 | CONFIRMED | =2 结果仅 1 条 data-ds-appid="3419430"；=3 结果 0 条 | 2026-10-09T22:59:13Z |
| P21 | Playable 定义引文 | partner.steamgames.com/doc/steamdeck/compat（302 到 /doc/steamhardware/compat） | CONFIRMED | "Playable Your game functions on Deck/Machine, but may require manual work from the user." | 2026-10-09T22:59:13Z |
| P22 | 五条测试项及 display_type | DECK resolved_items | CONFIRMED | 3,3,3,3,4，token 顺序与表一致，前缀 #SteamDeckVerified_TestResult_ | 2026-10-09T22:59:13Z |
| P23 | steamos 与 machine 两值均为 2 | DECK | CONFIRMED | steamos_resolved_category:2，machine_resolved_category:2 | 2026-10-09T22:59:13Z |
| P24 | 商店含 Partial Controller Support | APP categories | CONFIRMED | id 18 "Partial Controller Support" | 2026-10-09T22:59:13Z |
| P25 | Proton 引文 | 同 P21 页 | CONFIRMED | "games without native Linux builds will be run through Proton" | 2026-10-09T22:59:13Z |
| P26 | 63 条，02-03-2025 至 10-01-2026，deck/steamos/proton 0 命中 | NEWS | CONFIRMED | count=63；最早 DEMO RELEASE 2025-02-03 13:19 UTC，最晚 UI THEMES are here! 2026-10-01 15:43 UTC；\bdeck\|steamos\|proton 全文 0 命中（另查 handheld/steam machine 0 命中；"gaming mode" 命中的是游戏自带的模式，非 Deck） | 2026-10-09T22:59:13Z |
| P27 | 只有 3 条公告把 Mac/Linux 作为平台提到 | NEWS 正则 \bmac\b\|macos\|linux\|x11\|wayland | CONFIRMED | 恰命中 1827626365763660、1830163047265223、1834602721190507 三条 | 2026-10-09T22:59:13Z |
| P28 | 04-20 引文 | NEWS 1830163047265223 | CONFIRMED | "We also set up a PC in our office with Linux, we are on it. But it takes time especially with all the different sub-OS."；2026-04-20 06:48 UTC | 2026-10-09T22:59:13Z |
| P29 | 03-23 Linux 引文 | NEWS 1827626365763660 | CONFIRMED | "We are preparing a PC in our office so we can actively develop on it and test with it." | 2026-10-09T22:59:13Z |
| P30 | 另有同名开源桌面程序在 Steam 之外分发 | 任务书禁用来源（GitHub/粉丝站不在允许清单） | UNVERIFIED | 允许来源内无法证实；原因：只能靠第三方仓库页 | 2026-10-09T22:59:13Z |
| P31 | display_type 数字含义无 Valve 公开说明 | partner.steamgames.com/doc/steamhardware/compat | UNVERIFIED | 该页不含 "display_type"（只证明这一页没有）；全称否定无法证全 Valve 文档 | 2026-10-09T22:59:13Z |
| P32 | Deck 接口无公开文档 | 同上页 | UNVERIFIED | 该页不含 ajaxgetdeckappcompatibilityreport；"no public documentation that we found" 是写手自述，不可证 | 2026-10-09T22:59:13Z |
| V1 | "Steam news feed 里 63 条是开发者公告" | NEWS feeds=steam_community_announcements | CONFIRMED | 全部 feedname=steam_community_announcements；count=63 与 items=63 一致，未漏翻 | 2026-10-09T22:59:13Z |
| V2 | 表中 06-05 行"A Linux update for X11 is close" | NEWS 1834602721190507 | CONFIRMED | 原句 "Linux update will be out soon (for X11)" | 2026-10-09T22:59:13Z |
| V3 | 正文"Windows … Released March 5, 2025"归在"开发者发布"列 | NEWS 1793384379332669 | CONFIRMED | 见 P6 | 2026-10-09T22:59:13Z |
| V4 | 「Mac Issues 帖开帖 2026-03-23」中的年份 | 帖子仅显示 "Mar 23 @ 7:39am" | UNVERIFIED | 页面不显示年份；与公告 2026-03-23 14:40 UTC 相符（7:39am PDT=14:39 UTC）属推断，非页面所载 | 2026-10-09T22:59:13Z |
| V5 | 所有"returned … on October 10, 2026"的读取日期 | 写手 raw/mlsd-emotes-fetch.time；本机时钟 | REFUTED | 草稿句：「On October 10, 2026 the Steam app details API returned…」「resolved_category: 2 on October 10, 2026」「(all read on October 10, 2026)」「as of October 10, 2026」。反例：写手取数时间戳为 2026-10-09T22:40:07Z，我取数时间 2026-10-09T22:55Z–23:05Z，UTC 日期均为 10 月 9 日；10 月 10 日是北京时间。frontmatter 的 checkedAt/date 同。 | 2026-10-09T22:59:13Z |
| V6 | 「Valve 一手页面证明 2=Playable」是否站得住 | SEARCH + 对照样本 | CONFIRMED | 对照：Cyberpunk 2077（appid 1091500）DECK resolved_category=3，且出现在 deck_compatibility=3 搜索结果；Bongo Cat 的 IStoreBrowseService 返回 steam_deck_compat_category:2。数值-档名对应有 Valve 搜索页 data-loc 为证 | 2026-10-09T22:59:13Z |

## 机检
① 外链 10 个（正文中去重）：全部 HTTP 200（api 公告、steamworks 文档[302→/doc/steamhardware/compat 后 200]、两个帖子、appdetails、三条公告页、DECK、搜索页），均在 sourceUrls 内；sourceUrls 中无多余项。注：公告网页是脚本渲染，curl 到的 HTML 不含正文，正文以接口为准。
② 站内链接 4 个：how-to-play、steam-error、is-it-safe、multiplayer，均在允许清单内；无 market-prices。
③ 时效词（now/currently/upcoming/soon/latest/recently）：正文 0 处（官方引文 "will be out soon" 已被草稿省略，仅转述）。
