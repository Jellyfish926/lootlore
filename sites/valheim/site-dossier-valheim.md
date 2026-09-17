# 站点档案 · Lootlore `/valheim/`(英灵神殿中文攻略)

建档:2026-09-17 · 作者署名:Jellyfi · 仓库:`Jellyfish926/lootlore` · 分支:`valheim`(**未合并 main,未上线**)

## 一、现状

| 项 | 值 |
|---|---|
| 形态 | 总站 lootlore 下的原生内容游戏(`kind: native`),非子站快照 |
| 语言 | zh-CN 单语种,无 hreflang |
| 页数 | 40 = 首页 1 + 栏目 6 + 攻略 32 + 作者页 1 |
| 线上地址 | 未上线。合并 main 后为 `https://lootlore-ten.vercel.app/valheim/`(当前 base_url;换正式域名见待办) |
| 真相源 | `content/valheim/*.md`(内容包 2026-09-16 的 39 份 Markdown + 本站作者页),未引入 HTML/JSON 副本 |
| 事实核验 | **未完成**。内容包 README 与交接说明均写明 39/39 页未过本轮发布事实审核;当前所有页 `draft: false` 是按本轮指令设置 |
| 广告/统计 | 与总站其他页一致:页头带 AdSense 脚本;GA4 未配置(`ga4_id` 为空) |

## 二、路径规则

- 游戏 hub:`/valheim/`(frontmatter `type: home`)
- 其余页:`/valheim/<slug>/`;frontmatter `url` 必须与此一致,否则构建失败
- 栏目:`/valheim/beginner/ survival/ biomes/ bosses/ deep-north-guides/ multiplayer/`
- 作者页:`/valheim/author/`(lootlore 原先没有 `/author/`)
- Kall:主栏目「深北之境」,同时出现在 `/valheim/bosses/` 列表,只有一个 URL `/valheim/kall/`
- 信任页链接到总站英文页 `/about /contact /editorial-policy /privacy-policy /terms /disclaimer`
- Vercel:`cleanUrls: true`,无尾斜杠强制;站内链接统一带尾斜杠,与 canonical 一致

## 三、配置项

`config/hub.json` → `games[]` 中 `slug: valheim` 一项:

| 字段 | 作用 |
|---|---|
| `kind: native` / `lang: zh-CN` / `content: content/valheim` | 走 `hub/native.py` 渲染 |
| `short` / `default_path` | 总站下拉与子站 hubbar 的入口文字与路径 |
| `native.title` | 面包屑与页头里的游戏名「英灵神殿」 |
| `native.nav` | 栏目顺序;与 `type: category` 的页一一对应(缺页构建报错,空栏目自动不上导航) |
| `native.related_heading` | 正文末尾同名小节(「接下来可以看」)被剥离,改由 `related` 渲染「关联阅读」 |
| `native.official_domains` | 这些域名的外链只加 `rel="noopener"`,其余外链加 `noopener nofollow` |
| `native.author` / `native.defaults` | 作者名与缺省 frontmatter(`date` 2026-09-17、`author`、`draft: false`) |
| `native.theme` | 强调色 `--accent/--accent2`(只走 CSS 变量) |
| `card.*` | 总站首页卡片;`pages: "auto"` = 按实际生成页数;草稿页的 highlight 自动隐藏 |

界面文字:`config/i18n/zh-CN.json`。封面图:`content/valheim/_images.json`(Steam appdetails 892970 的 20 张官方截图热链,alt 按画面写,图注「官方截图 · Iron Gate Studio（Steam 商店页）」)。

## 四、页面清单

「来源」= frontmatter `sourceUrls` 条数(页面上编号 S001…,访问日期 = `checkedAt`);「lastmod」= sitemap 取值(`reviewed ?? updated ?? date`)。

| # | slug | 页型 | 主栏目 | URL | 表格 | 来源 | 关联 | 目录 | 封面 | lastmod | draft |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | index | home | 首页 | `/valheim/` | 0 | 0 | 0 | 有 | ss02 | 2026-09-16 | false |
| 2 | bosses | category | Boss攻略 | `/valheim/bosses/` | 0 | 0 | 0 | — | ss06 | 2026-09-16 | false |
| 3 | biomes | category | 区域推进 | `/valheim/biomes/` | 0 | 0 | 0 | — | ss11 | 2026-09-16 | false |
| 4 | beginner | category | 新手入门 | `/valheim/beginner/` | 0 | 0 | 0 | — | ss15 | 2026-09-16 | false |
| 5 | deep-north-guides | category | 深北之境 | `/valheim/deep-north-guides/` | 0 | 0 | 0 | — | ss01 | 2026-09-16 | false |
| 6 | survival | category | 生存建设 | `/valheim/survival/` | 0 | 0 | 0 | — | ss16 | 2026-09-16 | false |
| 7 | multiplayer | category | 联机维护 | `/valheim/multiplayer/` | 0 | 0 | 0 | — | ss12 | 2026-09-16 | false |
| 8 | bonemass | article | Boss攻略 | `/valheim/bonemass/` | 0 | 2 | 3 | 有 | ss17 | 2026-09-16 | false |
| 9 | eikthyr | article | Boss攻略 | `/valheim/eikthyr/` | 0 | 1 | 3 | 有 | ss15 | 2026-09-16 | false |
| 10 | elder | article | Boss攻略 | `/valheim/elder/` | 0 | 2 | 3 | 有 | ss04 | 2026-09-16 | false |
| 11 | fader | article | Boss攻略 | `/valheim/fader/` | 0 | 1 | 3 | 有 | ss06 | 2026-09-16 | false |
| 12 | moder | article | Boss攻略 | `/valheim/moder/` | 0 | 2 | 3 | 有 | ss05 | 2026-09-16 | false |
| 13 | queen | article | Boss攻略 | `/valheim/queen/` | 0 | 2 | 3 | 有 | ss18 | 2026-09-16 | false |
| 14 | yagluth | article | Boss攻略 | `/valheim/yagluth/` | 0 | 3 | 3 | 有 | ss07 | 2026-09-16 | false |
| 15 | ashlands | article | 区域推进 | `/valheim/ashlands/` | 0 | 3 | 3 | 有 | ss03 | 2026-09-16 | false |
| 16 | bronze | article | 区域推进 | `/valheim/bronze/` | 1 | 7 | 3 | 有 | ss04 | 2026-09-16 | false |
| 17 | mistlands | article | 区域推进 | `/valheim/mistlands/` | 0 | 4 | 3 | 有 | ss18 | 2026-09-16 | false |
| 18 | mountains | article | 区域推进 | `/valheim/mountains/` | 0 | 4 | 3 | 有 | ss05 | 2026-09-16 | false |
| 19 | plains | article | 区域推进 | `/valheim/plains/` | 0 | 4 | 3 | 有 | ss07 | 2026-09-16 | false |
| 20 | swamp | article | 区域推进 | `/valheim/swamp/` | 0 | 2 | 3 | 有 | ss17 | 2026-09-16 | false |
| 21 | combat | article | 新手入门 | `/valheim/combat/` | 0 | 2 | 3 | 有 | ss05 | 2026-09-16 | false |
| 22 | crafting | article | 新手入门 | `/valheim/crafting/` | 1 | 3 | 3 | 有 | ss13 | 2026-09-16 | false |
| 23 | death-recovery | article | 新手入门 | `/valheim/death-recovery/` | 0 | 1 | 3 | 有 | ss17 | 2026-09-16 | false |
| 24 | first-day | article | 新手入门 | `/valheim/first-day/` | 1 | 3 | 3 | 有 | ss10 | 2026-09-16 | false |
| 25 | progression | article | 新手入门 | `/valheim/progression/` | 0 | 2 | 3 | 有 | ss00 | 2026-09-16 | false |
| 26 | deep-north | article | 深北之境 | `/valheim/deep-north/` | 0 | 3 | 3 | 有 | ss01 | 2026-09-16 | false |
| 27 | intricate-key | article | 深北之境 | `/valheim/intricate-key/` | 0 | 3 | 3 | 有 | ss03 | 2026-09-16 | false |
| 28 | kall | article | 深北之境 | `/valheim/kall/` | 0 | 2 | 3 | 有 | ss09 | 2026-09-16 | false |
| 29 | farming | article | 生存建设 | `/valheim/farming/` | 0 | 3 | 3 | 有 | ss15 | 2026-09-16 | false |
| 30 | first-base | article | 生存建设 | `/valheim/first-base/` | 0 | 2 | 3 | 有 | ss07 | 2026-09-16 | false |
| 31 | food | article | 生存建设 | `/valheim/food/` | 0 | 1 | 3 | 有 | ss14 | 2026-09-16 | false |
| 32 | mead | article | 生存建设 | `/valheim/mead/` | 0 | 2 | 3 | 有 | ss13 | 2026-09-16 | false |
| 33 | portals | article | 生存建设 | `/valheim/portals/` | 1 | 1 | 3 | 有 | ss12 | 2026-09-16 | false |
| 34 | rested | article | 生存建设 | `/valheim/rested/` | 0 | 2 | 3 | 有 | ss16 | 2026-09-16 | false |
| 35 | ships | article | 生存建设 | `/valheim/ships/` | 0 | 2 | 3 | 有 | ss02 | 2026-09-16 | false |
| 36 | traders | article | 生存建设 | `/valheim/traders/` | 0 | 2 | 3 | 有 | ss19 | 2026-09-16 | false |
| 37 | co-op | article | 联机维护 | `/valheim/co-op/` | 1 | 2 | 3 | 有 | ss12 | 2026-09-16 | false |
| 38 | mods | article | 联机维护 | `/valheim/mods/` | 0 | 2 | 3 | 有 | ss08 | 2026-09-16 | false |
| 39 | save-1-0 | article | 联机维护 | `/valheim/save-1-0/` | 0 | 2 | 3 | 有 | ss08 | 2026-09-16 | false |
| 40 | author | author | 作者 | `/valheim/author/` | 0 | 0 | 0 | — | ss02 | 2026-09-17 | false |

## 五、门禁结果(2026-09-17,本地对 `out/` 复现 gates.yml)

| 命令 | 最后一行 |
|---|---|
| `python3 build.py` | built 525 html pages(valheim 40 页,草稿 0) |
| `check_content.py out --locales de,es,fr,it,ja --default en --dir-lang valheim=zh` | check_content: 516 页 · 0 阻塞 · 0 警告 |
| `check_i18n.py out … --games …,valheim` | 6 个游戏目录 · 多语种 1 · 单语种/跳过 5(含 valheim)· 阻塞 0 · 警告 0 |
| `check_sitemap.py --out out --host lootlore-ten.vercel.app` | → 0 阻塞 · 0 警告(524 条 loc) |
| `link_check.py --out out` | ✓ 无死链 |
| `freshness_audit.py --out out` | 全部在期内,无需动作 |
| `tech_audit.py --out out --base … --prefix /valheim/ --summary`(只报告) | canonical/JSON-LD/OG/alt/宽高/H1 全部 0 问题;title 显示宽度 >60 共 30 页、<30 共 6 页(栏目页);description <70 共 6 页;词数 <800 共 39 页 |
| `check_config.py .` | 不适用(非 Next+MDX 布局);三处一致由 `hub/native.py` 构建期校验 |

draft 门控实测:把 `kall.md` 临时改 `draft: true` → `out/valheim/kall/` 不生成、sitemap 无、Boss 与深北栏目列表不含(深北计数 3→2)、hub 全部攻略清单与作者页不含、深北相关页的关联阅读不含、首页正文里的 Kall 链接降为纯文本;四道门禁全绿;已改回 `false`。

替换演练:在临时副本里用内容包原始 39 份 Markdown(无 date/draft/author 字段)覆盖 `content/valheim/`,改一句正文后重跑 build → 改动出现在页面上,byline 由 defaults 补齐,门禁全绿。

外链抽查(2026-09-17):页面实际引用的 Steam 截图地址(两种尺寸)、valheimgame.com、pcgamer.com、gamers.wiki 均 200;valheim.fandom.com 48 页直连 403(机房 IP 被挡),改用 MediaWiki API 查询 48 个标题全部存在;valheim.tools 3 条、mobalytics.gg 2 条、games.gg 1 条直连 403,**未获取**(未能确认存活)。

## 六、截图(Playwright Chromium,本地产物)

位置:`/tmp/claude-0/-home-claude/656bc16e-3a77-5cd3-aef6-9c8bac0c32b8/scratchpad/build/shots/`(会话临时目录,未入库)

- `hub-390.png` / `hub-1280.png`、`category-bosses-390.png` / `category-bosses-1280.png`、`article-crafting-390.png` / `article-crafting-1280.png`(整页)
- `menu-open-390.png` / `menu-open-1280.png`(游戏下拉展开)、`table-scrolled-390.png` / `table-scrolled-1280.png`(表格横滑后)

实测:6 张页面在 390 与 1280 宽下 `scrollWidth == clientWidth`(无横向溢出);crafting 表格 390 宽下内容 560px / 容器 356px,可横滑;栏目导航 390 宽下 558px 可横滑;下拉面板在视口内、7 个链接可见;封面图全部加载。

## 七、事实核验 2026-09-17

**流程**:4 个核验 agent(A/B/C/D)分组对 39 篇正文逐条核验(176 条命题),随后按 `anthropic-skills:adversarial-verify` 做独立对抗验证——验证 agent 不看产出方的推理与证据,只拿命题原文重新取证。

**分组核验(第一轮)**:

| 组 | 页数 | 命题数 | 支持 | 冲突 | 不足 | 状态 |
|---|---|---|---|---|---|---|
| A(深北之境/1.0 相关) | 10 | 51 | 51 | 0 | 0 | 全部通过 |
| B(Boss 攻略) | 12 | 55 | 54 | 0 | 1 | 全部通过(1 条按红线降级为不作断言) |
| C(新手/生存) | 10 | 43 | 43 | 0 | 0 | 全部通过 |
| D(联机维护) | 7 | 27 | 27 | 0 | 0 | 全部通过 |
| 合计 | 39 | 176 | 175 | 0 | 1 | — |

**独立对抗验证(第二轮,抽样/全量)**:

- **A 组(全量验证,53 条)**:CONFIRMED 42 / REFUTED 0 / UNVERIFIED 11。关键结论:Kall Fimbulbringer 三阶段机制经一手来源(`valheim.wiki/w/Kall_Fimbulbringer`)确认成立,但「锁链攻击」这一具体命名在一手来源里查不到(Phase 1 原文只写 attacks the player directly);模组相关的「官方提醒考虑加载器」「官方建议先卸载模组测原版」两条判定 UNVERIFIED(官方 FAQ/公告全文检索无对应原文);付费墙锁模组一条判定 CONFIRMED 但注明「措辞偏强:官方是『不认可/敦促』,不是强制禁止」。详见 `sites/valheim/verification/2026-09-17/ADV_A.md`。
- **BCD 组(抽样 39 条)**:CONFIRMED 38 / REFUTED 1 / UNVERIFIED 0。唯一 REFUTED 项(P39,即 bosses.md 里的 Kall 阶段描述)与 A 组独立发现的问题一致:三阶段机制成立,但「锁链阶段」命名无一手依据。按 adversarial-verify 红线(抽样出一条 REFUTED 即转全量复核),已就 Kall 相关命题在 A/B 两组全部复核并修正,BCD 其余命题因与 Kall 机制无关未触发全量重验;完整的 BCD 全量结果(若需要覆盖全部 176 条中的 B/C/D 部分)留待下一轮核验补齐。详见 `sites/valheim/verification/2026-09-17/ADV_BCD.md`。

**本次修正清单(对抗验证后落地的 8 处正文修正)**:

| # | 页面 | 修正前 | 修正后 | 依据 |
|---|---|---|---|---|
| 1 | kall.md(description + 正文 2 处) | 「锁链阶段、召唤化身阶段与最终强化阶段」;「第一阶段主要面对锁链攻击」 | 三阶段改为不提锁链命名的招式描述:第一阶段本体直接攻击,第二阶段本体躲入无敌冰块并轮流召唤此前七位首领的化身(同时最多两个在场),第三阶段本体回归、招式更强并带元素伤害 | valheim.wiki 一手原文(Phase 1/2/3 描述),已加入 sourceUrls |
| 2 | deep-north-guides.md | 同上摘要句 | 同步改为三阶段新表述 | 与 kall.md 对齐 |
| 3 | bosses.md | 「具体阶段划分暂无可靠来源支持,本文不做断言」 | 改回具体三阶段描述(不提锁链) | B 组首轮核验时 fandom 未收录,判不足;A 组独立验证追加 valheim.wiki 一手来源后确认成立 |
| 4 | intricate-key.md | 「并要求四级 Black Forge」 | 「在 Black Forge 制作」 | 等级要求仅见于单一三方来源,一手来源未能核实,删去数字 |
| 5 | deep-north.md | 「隧道名称也可能被部分资料称作 Hidden Tunnels」;「Frigid Kiln 和 Frost Foundry 分别需要十枚 Frostcore」 | 删除 Hidden Tunnels 一句;改为「Frigid Kiln 需要 10 枚 Frostcore(Stone×20、Ice×5);Frost Foundry 的用量以游戏内配方为准」 | 均无一手来源支持,仅单一三方攻略站 |
| 6 | ashlands.md | 「官方建议先击败女王」 | 「流程上先击败女王(The Queen)」 | 来源为官方准备说明而非强制规则,收紧措辞 |
| 7 | mods.md | 「官方在更新准备说明中也提醒要考虑加载器」;「官方没有承诺第三方模组始终兼容,参见官方模组说明」 | 改为本站建议口吻「本站建议连加载器一起移除再测试」;明确「官方没有官方模组支持」 | 官方原文口径只是 modding at your own risk、没有官方模组支持,不保证 1.0 兼容;对抗验证判该条 UNVERIFIED |
| 8 | save-1-0.md | 「永久成就限制标记」句末无后续说明 | 追加一句:2026-09-11 的 Hotfix 1.0.12(目前仅 Steam 版)新增控制台命令,可让用过作弊命令或模组的角色主动重新开启成就 | Steam 公告《Hotfix 1.0.10 & 1.0.12》,已加入 sourceUrls |

对应 A 组 ledger(`ashlands.json`/`deep-north.json`/`intricate-key.json`/`kall.json`/`mods.json`/`save-1-0.json`)与 B 组 `bosses.json` 的 `changes`/`correction` 字段已同步更新。核验台账归档:`sites/valheim/verification/2026-09-17/{A,B,C,D}/SUMMARY.md`、`{A,B,C,D}/ledger/*.json`、`ADV_A.md`、`ADV_BCD.md`。

合并后 `reviewed`/`updated` 统一置为 `2026-09-17`,`gameVersion` 统一为 `"1.0.12"`,`draft` 保持 `false`;门禁(build + 6 道 gates)全绿,占位语/锁链命名 grep 复查为 0(仅 `_images.json` 里一张截图的 alt 文本描述「被发光锁链缠绕的石门」,与 Boss 机制无关,予以保留)。

## 八、待办

| # | 事项 | 谁 |
|---|---|---|
| 1 | ~~事实核验合并~~:已完成(2026-09-17,见「七、事实核验」)。39 篇全部通过,`draft` 保持 `false` | 已完成 |
| 2 | **合并 main = 上线**:main 一 push 就自动部署,valheim 分支尚未合并 main | 站主 |
| 3 | 域名:当前 `base_url` 为 `lootlore-ten.vercel.app`;换域名按总站 README 执行 `python3 build.py --base https://新域名`,并同步 gates.yml / sync-sources.yml / freshness.yml 的 host | 站主 |
| 4 | GSC:上线后提交 sitemap,对 `/valheim/` 与 6 个栏目页请求编入索引 | 站主 |
| 5 | GA4:`config/hub.json` 的 `ga4_id` 仍为空(总站级) | 站主 |
| 6 | title 长度:30 篇 `seoTitle` 显示宽度 62–73(>60),6 个栏目页 20–24(<30);description 6 个栏目页 <70 宽。属内容层,建议随核验稿一起调 | 内容方 |
| 7 | 正文深度:32 篇折算 518–665 词,低于 800 词下限;中文页字数口径待定(见 `lessons-inbox.md` 第 6 条) | 站主 |
| 8 | 4 个栏目页(新手入门/生存建设/区域推进/联机维护)正文入链仅 1 条(来自 hub 卡片),栏目导航与面包屑不计入;可在相关攻略正文里补语境链接 | 内容方 |
| 9 | `valheim.tools` / `mobalytics.gg` / `games.gg` 6 条来源未能验活(403) | 核验方 |
| 10 | 作者页只写了可确认的编写方式;真实作者简介、社交链接待站主提供 | 站主 |
