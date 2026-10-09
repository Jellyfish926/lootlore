# mac-linux-steam-deck 第二轮核验（终稿 /home/claude/lootlore/content/bongo-cat/en/mac-linux-steam-deck.md）

30 条命题，2 条被推翻（M17、M18，同一缺陷分属两个帖子），3 条未验（M20、M21、M22）。取证自行重取（公告 feed 63 条、appdetails、Deck 报告、搜索页、Steamworks 文档、两个讨论帖原始 HTML），取证时间 2026-10-09 23:18-23:22Z。

| 编号 | 命题（终稿原句） | 验证路径 | 结果 | 证据 | 取证时间 |
|---|---|---|---|---|---|
| M1 | 读取日统一 October 9, 2026，scope 写明「dates on this page, including that reading date, are UTC」；checkedAt 2026-10-09 | 全文 grep | CONFIRMED | 无 October 10 残留 | 2026-10-09 23:18-23:22Z |
| M2 | appdetails：windows true、mac true、linux false；商店页有 Windows 与 Mac 图标 | https://store.steampowered.com/api/appdetails?appids=3419430&l=english ；商店页 HTML | CONFIRMED | platforms {windows:true, mac:true, linux:false}；页内仅 platform_img win、platform_img mac | 2026-10-09 23:18-23:22Z |
| M3 | Mac 要求表：OS 11.0 / 13.0、Intel 64-Bit or Apple silicon、1 GB RAM、Graphics "-"、Broadband、700 MB | appdetails mac_requirements | CONFIRMED | 逐项一致 | 2026-10-09 23:18-23:22Z |
| M4 | Windows 存储 100 MB；700÷100=7 倍 | appdetails pc_requirements | CONFIRMED | Storage 100 MB available space；算式正确 | 2026-10-09 23:18-23:22Z |
| M5 | Linux requirements 块 minimum/recommended 均为空列表 | appdetails linux_requirements | CONFIRMED | `<ul class="bb_ul"></ul>` | 2026-10-09 23:18-23:22Z |
| M6 | 3 月 23 日公告标题与引文 "With this update we will launch an experimental mac build that you can try out." | https://store.steampowered.com/news/app/3419430/view/1827626365763660 | CONFIRMED | 标题「Regional Pricing, Experimental Mac Support, QoL Changes」，date 2026-03-23 14:40Z | 2026-10-09 23:18-23:22Z |
| M7 | 「I know a lot of you want to play with your friends (that are on Mac or Linux).」；Linux 句 "We are preparing a PC in our office so we can actively develop on it and test with it." | 同上 | CONFIRMED | 原文一致 | 2026-10-09 23:18-23:22Z |
| M8 | 「No announcement after that one says the Mac build has left the experimental stage」 | feed 全文搜 experimental | CONFIRMED | 仅 3 月 23 日一帖含该词 | 2026-10-09 23:18-23:22Z |
| M9 | 4 月 20 日公告标题与引文 "We also set up a PC in our office with Linux, we are on it. But it takes time especially with all the different sub-OS." | https://store.steampowered.com/news/app/3419430/view/1830163047265223 | CONFIRMED | 原文一致，date 2026-04-20 | 2026-10-09 23:18-23:22Z |
| M10 | 6 月 5 日公告：Linux update for X11 close；"Wayland will take more time." | https://store.steampowered.com/news/app/3419430/view/1834602721190507 | CONFIRMED | 原文「Linux update will be out soon (for X11). Wayland will take more time.」；date 2026-06-05 12:19Z | 2026-10-09 23:18-23:22Z |
| M11 | 「Seven announcements were posted after that one, the last on October 1, 2026, and none of them contains the words Linux, X11 or Wayland」 | feed | CONFIRMED | 6/5 12:19Z 之后 7 帖（6/16、6/27、7/12、8/10、9/1、9/18、10/1）；linux/x11/wayland 只命中 3/23、4/20、6/5 | 2026-10-09 23:18-23:22Z |
| M12 | 「Three of them mention Mac or Linux as a platform」 | feed | CONFIRMED | 命中 3/23、4/20、6/5 三帖 | 2026-10-09 23:18-23:22Z |
| M13 | 「none of the 63 announcements … contains "Steam Deck", "SteamOS" or "Proton"」（2025-02-03 至 2026-10-01） | feed | CONFIRMED | 三词 0 命中；首帖 2025-02-03 13:19Z，末帖 2026-10-01 | 2026-10-09 23:18-23:22Z |
| M14 | 「None of the 63 announcements explains why the test version sits outside the public listing」 | feed | CONFIRMED | Linux 相关三帖均无此解释 | 2026-10-09 23:18-23:22Z |
| M15 | 「Mac Issues」帖：开发者账号发帖（带 [developer] 标）、置顶、Input Monitoring 步骤、"grant permissions to Steam and Bongo Cat" | https://steamcommunity.com/app/3419430/discussions/0/806846367620396268/ | CONFIRMED | 楼主 Spiced Pigeon [developer]，「This topic has been pinned」；原文「grant permissions to Steam and Bongo Cat」 | 2026-10-09 23:18-23:22Z |
| M16 | 终稿 Mac 帖显示时间 "Mar 23 @ 7:39am"、最后编辑 "May 25 @ 10:17am" | https://steamcommunity.com/app/3419430/discussions/0/806846367620396268/ | CONFIRMED | 页面可见文本即「Mar 23 @ 7:39am」「Last edited by Spiced Pigeon; May 25 @ 10:17am」 | 2026-10-09 23:18-23:22Z |
| M17 | 「it prints no year」「thread shows no year」（Mac 帖）；「2026 is our inference」 | https://steamcommunity.com/app/3419430/discussions/0/806846367620396268/ 页面 HTML | REFUTED | 可见文本确无年份，但同页 HTML 的时间戳 title 属性写明：`title="March 23, 2026 @ 7:39:39 am PDT"`、`title="May 25, 2026 @ 10:17:19 am PDT"`（data-timestamp 1774276779 / 1779729439）。即页面本身显示年份 2026（悬停可见），并非只能推断。终稿「prints no year」不属实（年份结论本身 2026 正确；可见文本的时间是页面按浏览器时区渲染，抓取端为 PDT，终稿没写时区） | 2026-10-09 23:18-23:22Z |
| M18 | Linux 帖：置顶、开发者账号发帖；日期显示 "Jun 10 @ 1:02am"；「no year shown; 2026 is our inference」 | https://steamcommunity.com/app/3419430/discussions/0/573792389464878955/ | REFUTED（同 M17 的同类缺陷） | 可见文本「Jun 10 @ 1:02am」✓；开发者标 ✓；置顶 ✓；但 HTML 带 `title="June 10, 2026 @ 1:02:54 am PDT"`（data-timestamp 1781078574 = 2026-06-10 08:02:54Z）。终稿三处「no year shown」（正文、表格 Mar 23/Jun 10 行、tldr3 的「no year shown」）与此不符 | 2026-10-09 23:18-23:22Z |
| M19 | 引文 "Hello we have a linux version that you can test. The beta code is: linuxtesting"；"Only works on X11"；「would like more testers」 | https://steamcommunity.com/app/3419430/discussions/0/573792389464878955/ | CONFIRMED | 原文「Only works on X11 right now but we would love to get more testers on board!」 | 2026-10-09 23:18-23:22Z |
| M20 | 「Beyond the code, the thread gives no install steps, no distribution list and no system requirements」 | https://steamcommunity.com/app/3419430/discussions/0/573792389464878955/ | UNVERIFIED | 楼主帖正文确实只有 3 句；但帖子共 304 条回复（total_count 304），本次只取到首屏 15 条，其中无开发者标回复，其余 289 条未读。「the thread」范围大于已读范围 | 2026-10-09 23:18-23:22Z |
| M21 | 「Bongo Cat counts key presses and clicks made in other apps」 | https://steamcommunity.com/app/3419430/discussions/0/806846367620396268/ ；商店描述 | UNVERIFIED | Mac 帖只说要给 Steam 与 Bongo Cat 开「read input (keyboard, mouse, etc.)」权限；商店描述「Every time you press a key, Bongo cat will punch your taskbar」。「clicks … in other apps」是推断，两处出处均无此句 | 2026-10-09 23:18-23:22Z |
| M22 | 同名项目那句：「searches that add github to the name point to a different project with the same name」 | 无允许来源可查 | UNVERIFIED | 终稿没有描述该项目（已满足不描述的要求），但「搜索加 github 会指向另一个同名项目」这一断言无 sourceUrls、也不在允许来源范围内（只能靠搜索引擎/GitHub 才能验证）。注意：这是关于搜索结果的断言，不是 Steam 官方内容 | 2026-10-09 23:18-23:22Z |
| M23 | Deck 报告 resolved_category 2；steamos_resolved_category 2、machine_resolved_category 2 | https://store.steampowered.com/saleaction/ajaxgetdeckappcompatibilityreport?nAppID=3419430 | CONFIRMED | 三个值均为 2 | 2026-10-09 23:18-23:22Z |
| M24 | 五条测试结果 token 与 display_type（四条 3、DefaultConfigurationIsPerformant 为 4） | 同上 | CONFIRMED | 一致 | 2026-10-09 23:18-23:22Z |
| M25 | 搜索筛选：值 3=Verified、值 2=Playable；Playable 筛选返回 Bongo Cat，Verified 不返回 | https://store.steampowered.com/search/?term=bongo+cat&deck_compatibility=2 / =3 | CONFIRMED | data-value="3" data-loc="Verified"、data-value="2" data-loc="Playable"；=2 结果含 data-ds-appid="3419430"，=3 结果 0 命中 | 2026-10-09 23:18-23:22Z |
| M26 | Steamworks 文档引文 "Your game functions on Deck/Machine, but may require manual work from the user."；"games without native Linux builds will be run through Proton" | https://partner.steamgames.com/doc/steamdeck/compat | CONFIRMED | 原文一致 | 2026-10-09 23:18-23:22Z |
| M27 | 「The Steamworks Deck compatibility page … does not mention that endpoint」「does not contain the term display_type」 | 同上 | CONFIRMED | 渲染文本中 ajaxgetdeck、display_type、loc_token 均 0 命中 | 2026-10-09 23:18-23:22Z |
| M28 | 「the store lists the game under "Partial Controller Support"」 | 商店页 HTML | CONFIRMED | 页内 props `bPartialXboxControllerSupport:true`、`bFullXboxControllerSupport:false`（屏幕文字由脚本渲染，未直接抓到字符串） | 2026-10-09 23:18-23:22Z |
| M29 | Windows 表行「Released March 5, 2025」 | feed | CONFIRMED | 「Bongo Cat is out meow!!!」date 2025-03-05 08:00Z | 2026-10-09 23:18-23:22Z |
| M30 | tldr/description/首段与正文互相矛盾？ | 通读 | CONFIRMED（无矛盾） | description「macOS 11.0 minimum … Playable」「Linux test for X11 only」与正文一致 | 2026-10-09 23:18-23:22Z |

## 重点项结论
- 两个开发者讨论帖的日期写法：终稿用页面可见文本「Mar 23 / May 25 / Jun 10」且标注「无年份」；没有把推断的年份写成事实，但「无年份」本身被页面 HTML 的 title 属性推翻（见 M17、M18）。页面所示时间为抓取端时区（PDT），终稿正文给出「7:39am」「1:02am」未标时区。
- 同名开源项目句：未描述该项目，但断言本身无出处（M22）。

## 三项机检
① 外链 curl -L：feed、appdetails、1827626365763660、1830163047265223、1834602721190507、两个讨论帖、Deck 报告、搜索页、partner 文档，全部 200；全部在 sourceUrls 内。备注：正文给读者的链接仍指向 appdetails JSON 与 Deck ajax JSON 两个机器接口（其他页已把 appdetails 读者链接换成商店页）。
② 站内链接：how-to-play、is-it-safe、multiplayer、steam-error，均在允许清单内。
③ 时效词：0 处。
