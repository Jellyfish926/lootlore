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
| 2 | ~~合并 main = 上线~~:已完成(2026-09-17,见「九、上线记录」) | 已完成 |
| 3 | 域名:当前 `base_url` 为 `lootlore-ten.vercel.app`;换域名按总站 README 执行 `python3 build.py --base https://新域名`,并同步 gates.yml / sync-sources.yml / freshness.yml 的 host | 站主 |
| 4 | GSC:重提 sitemap,并对 `/valheim/` 与 6 个栏目页请求编入索引(IndexNow 未生效,见「九、上线记录」) | 站主 |
| 5 | GA4 / Clarity:`config/hub.json` 的 `ga4_id` 仍为空(总站级),Clarity ID 同样未配置 | 站主 |
| 6 | title 长度:30 篇 `seoTitle` 显示宽度 62–73(>60,按 CJK 折算超 60 属 P1),6 个栏目页 20–24(<30);description 6 个栏目页 <70 宽。属内容层,建议随核验稿一起收短 | 内容方 |
| 7 | 正文深度:32 篇(article 页共 32 篇)中文正文 685–963 汉字(`chineseCharacters` 字段实测),按 800 汉字线有 22 篇偏薄,清单见「九、上线记录」 | 站主 |
| 8 | 4 个栏目页(新手入门/生存建设/区域推进/联机维护)正文入链仅 1 条(来自 hub 卡片),栏目导航与面包屑不计入;可在相关攻略正文里补语境链接 | 内容方 |
| 9 | `valheim.tools` / `mobalytics.gg` / `games.gg` 6 条来源未能验活(403) | 核验方 |
| 10 | 作者页只写了可确认的编写方式;真实作者简介、社交链接待站主提供 | 站主 |

## 九、上线记录(2026-09-17)

**分支状态**:`git fetch origin` 时 `origin/main` 与 valheim 分支点(`2a91a89`)完全重合,merge-base = origin/main HEAD,无需 rebase。`python3 build.py` 重建 `out/`:525 个 HTML(与 rebase/合并前一致,含五个既有游戏最新快照 + valheim 40 页),working tree 无差异。

**本地门禁**(对重建后的 `out/` 复现 `gates.yml` 全部步骤):

| 命令 | 结果 |
|---|---|
| `check_content.py` | 516 页 · 0 阻塞 · 0 警告 |
| `check_i18n.py`(6 个游戏目录) | 多语种 1 · 单语种/跳过 5(含 valheim)· 阻塞 0 · 警告 0 |
| `check_sitemap.py` | 524 条 loc · 0 阻塞 · 0 警告 |
| `link_check.py --out out` | 525 HTML,543 条站内链接,✓ 无死链 |
| `freshness_audit.py` | 全部在期内,无需动作 |
| `tech_audit.py`(只报告) | 与站点档案「五、门禁结果」一致 |

全绿,进入合并。

**合并与推送**:`git checkout main && git merge --ff-only valheim` 成功(fast-forward,无新合并提交),main 落在 `ba11d0204bf5d0ebafab91e413ca20fd68a2582a`(`docs: verification ledger 2026-09-17`)。`git push origin main`:`2a91a89..ba11d02 main -> main`。`git fetch` 后 `git status -sb` = `## main...origin/main`(ahead 0 / behind 0)。

**Vercel 部署**:GitHub Deployments API(`/repos/Jellyfish926/lootlore/deployments?per_page=3`,未按 environment 过滤)显示同一 sha 先建了一个 Preview 部署(id 6498624408),随后追加 Production 部署:

- deployment id `6498693668`,environment `Production`,sha `ba11d0204b…`,created_at `2026-09-17T08:28:34Z`
- 状态(`/deployments/6498693668/statuses`):`state=success`,`description=Deployment has completed`,`target_url=https://lootlore-hb50nxkop-1-6f9a.vercel.app`

**线上验证**(域名 `https://lootlore-ten.vercel.app`,2026-09-17 08:3x UTC):

| 检查项 | 结果 |
|---|---|
| `/` `/valheim/` `/valheim/kall/` HTTP 状态 | 均 200,`last-modified` 均为 `2026-09-17 08:28:4x GMT` |
| `/valheim/kall/` 内「无敌冰块」出现次数 | 4(≥1,含 description) |
| 首页「valheim」出现次数 | 5(≥1) |
| `/sitemap.xml` | 200,`/valheim/` 条目数 = 40 |
| `/robots.txt` | 200,`Sitemap: https://lootlore-ten.vercel.app/sitemap.xml`(无尾斜杠) |
| `/ads.txt` | 200 |
| 抽样 5 个 valheim URL(`/valheim/` `/valheim/bosses/` `/valheim/kall/` `/valheim/first-day/` `/valheim/save-1-0/`) | 全部 200 |
| `link_check.py --live lootlore-ten.vercel.app` | sitemap 524 页,543 条站内链接,✓ 无死链 |
| `/valheim/kall/` `<html lang>` | `<html lang="zh-CN"` |
| `/valheim/kall/` canonical | `<link rel="canonical" href="https://lootlore-ten.vercel.app/valheim/kall/">` |
| `/valheim/kall/` JSON-LD author | `"author":{"@type":"Person","name":"Jellyfi","url":"https://lootlore-ten.vercel.app/valheim/author/"}` |

**IndexNow**:仓内找到 32 位 hex 格式的 key 文件 `out/shift-at-midnight/c8ee8bae9e38c268a2e5c84fddfe8aca.txt`(源自 `sources/shift/`),线上可访问(`200`,内容即文件名)。但该 key 归属 shift-at-midnight 子站路径,不是站点根级或 valheim 专属配置;尝试以 `keyLocation=https://lootlore-ten.vercel.app/shift-at-midnight/c8ee8bae9e38c268a2e5c84fddfe8aca.txt` 提交 40 条 `/valheim/` URL 到 `https://api.indexnow.org/indexnow`,返回 **HTTP 422**:`{"errorCode":"InvalidRequestParameters","message":"One or more URLs are not related to your site verified through the keylocation parameter."}`。未生成新 key、未改仓库。结论:**未配置可用于 valheim 的 IndexNow**,GSC 手动提交 sitemap + 请求索引仍需站主执行。

**全量对抗验证补记**:BCD 其余 86 条核验结论中 82 条 CONFIRMED / 0 条 REFUTED / 4 条 UNVERIFIED——其中 3 条是站内结构类命题(不在事实取证范围内),1 条(P68「跨平台存档不同步」)已由主模型用 Valheim 官方 1.0 FAQ 原文核实成立:"Beyond this, there will be no cross platform sync for your save files"。

**待用户(汇总)**:

1. 在 GSC 重新提交 sitemap,并对 `/valheim/` 及 6 个栏目页手动请求编入索引(IndexNow 当前不可用)。
2. GA4 `ga4_id`(`config/hub.json`)与 Clarity ID 仍缺,需补齐。
3. 正式域名尚未换(当前为 `lootlore-ten.vercel.app` 临时域名)。
4. 30 篇 `seoTitle` 按 CJK 折算显示宽度 >60,属 P1,建议收短。
5. 中文正文 685–963 汉字,32 篇 article 中按 800 汉字线有 **22 篇**偏薄(数字取自各 `.md` frontmatter 的 `chineseCharacters` 字段):

   | slug | chineseCharacters |
   |---|---|
   | ashlands | 763 |
   | bonemass | 750 |
   | combat | 747 |
   | death-recovery | 782 |
   | deep-north | 742 |
   | eikthyr | 728 |
   | elder | 733 |
   | fader | 758 |
   | farming | 748 |
   | first-base | 741 |
   | food | 785 |
   | intricate-key | 685 |
   | mead | 725 |
   | mistlands | 773 |
   | moder | 752 |
   | mountains | 766 |
   | plains | 767 |
   | queen | 793 |
   | rested | 702 |
   | ships | 752 |
   | swamp | 767 |
   | traders | 725 |

   （其余 10 篇 ≥800:yagluth 809、bronze 859、crafting 959、first-day 858、progression 832、kall 836、portals 918、co-op 963、mods 875、save-1-0 851)

---

## 十、v2 结构(2026-09-18,分支 `valheim-v2`,未合并 main)

照 **valheim.wiki** 的结构重做,英文为默认语种、中文为第二语种。对标依据见
`scratchpad/research/report.md` 表 2/3/4/5 与 `research/2/shots/valheimwiki-{hub,guide}-1280.png`
(抄的是结构:左侧常驻游戏内导航 + 条目页右侧信息框 + 正文数据表 + 分类聚合排序表;不抄文案与视觉皮肤)。

### 10.1 目录与 URL

| 层 | 路径 | 说明 |
|---|---|---|
| 内容层 | `content/valheim/en/*.md` | 40 份(39 篇正文 + 作者页),`language: en`,**默认语种** |
| 内容层 | `content/valheim/zh/*.md` | 40 份,由 v1 的 `content/valheim/*.md` 整体迁入,`language: zh-CN` |
| 内容层 | `content/valheim/_images.json` | 两语种共用;`alt` 与 `credit` 改成 `{en, zh}` 两份 |
| 内容层 | `data/valheim/entities.json` | 43 个结构化实体(8 boss / 9 biome / 14 station / 4 boat / 5 item / 3 mechanic),数据 agent 产出,管线只补了 `page_slug` |
| 配置层 | `config/hub.json` → `games[valheim].native.langs` | 两语种声明:`code / i18n / dir / prefix / title / hreflang / label_key / default / related_headings` |
| 配置层 | `config/i18n/en.json`(新)、`config/i18n/zh-CN.json` | 全部界面文字;**代码层零游戏专属文案**(grep 验证:`hub/*.py`、`hub/native.css`、`build.py` 无 Valheim/Boss 名/区域名等可见文本,只有 `boss`/`biome` 这类实体 `type` 标识符) |
| 框架层 | `hub/native.py` | `NativeGame`(站点级,N 语种)+ `NativeLang`(单语种) |
| 框架层 | `hub/mdlite.py` | 新增图片支持:块级 `![alt](key "图注")` → `<figure>`,行内 `![]()` → `<img>` |
| 框架层 | `hub/native.css` / `hub/native_page.html` | 三栏骨架、抽屉、信息框、要点框、卡片、排序表样式;模板加 `{{SCRIPTS}}` 槽 |
| 脚本 | `scripts/valheim_stats.py` | 内容密度统计(只统计,不改内容) |

URL 规则:

- 英文(默认):`/valheim/` 与 `/valheim/<slug>/`
- 中文:`/valheim/zh/` 与 `/valheim/zh/<slug>/`
- 每语种另有构建期生成的 `/valheim/all/` 与 `/valheim/zh/all/`(无 JS 时的搜索退化页)
- 搜索索引:`/valheim/search-index.json`(两语种一份,每条带 `lang`)
- `<html lang>`:英文 `en`、中文 `zh-CN`;hreflang `en` / `zh-CN` / `x-default`(指英文)互指;canonical 自指
- 语言切换器只在该 slug 两语都已发布时出现(`/valheim/all/` 两语都有,所以也有)

**旧中文 URL 变成英文页**:v1 的 `/valheim/<slug>/` 原本是中文,v2 起是英文页,中文移到 `/valheim/zh/<slug>/`。
**不做 301**——同一 URL 只是换了语言,canonical 自指即可;中文页通过 hreflang 与页内切换器可达。
上线后 GSC 里这批 URL 的语言判定会变,收录可能有波动,属预期。

### 10.2 组件清单(全部 frontmatter 驱动,字段缺就不渲染)

| 区域 | 组件 | 触发条件 |
|---|---|---|
| 壳 | 顶部总站导航(品牌 / Games 下拉 / 当前游戏 / 站内搜索框) | 全站 |
| 壳 | 左侧常驻游戏内导航:6 个栏目各自展开条目 + Tools(全部攻略)+ About(作者 / 关于 / 联系 / 编辑方针);当前页高亮 | 全站;≤1024px 收成汉堡抽屉(纯 CSS checkbox,无 JS) |
| 壳 | 右侧 Quick Facts 信息框 | 页面绑定了 `entity` / `entities`;≤1100px 移到标题下方 |
| 标题区 | byline(作者 / 发布 / 最后核对 / 核对版本)+ scope + 语言切换器 | 有对应字段 |
| 正文 | 「Key points」要点框 | `tldr:` 有值 |
| 正文 | 封面 figure + 图注 | `_images.json` 有映射 |
| 正文 | 「On this page」目录 | H2 ≥ 5(hub 页按生成区块数 ≥5) |
| 正文 | 正文 figure(图注 + 来源,img 带 width/height/lazy/alt) | 正文里写 `![alt](ssNN "图注")` |
| 正文 | 实体自动表:boss → Summon items + Drops;station/boat/item → Recipe | 实体有对应字段;表一律套 `.table-scroll` 横滑容器 |
| 正文 | 抗性行(Weak / Resistant / Very resistant / Immune)在信息框里 | 实体有对应字段 |
| 正文 | 「Sources」编号 S001… + 访问日期(合并页面 sourceUrls 与所绑实体的 source_urls) | 任一非空 |
| 正文 | 「Related guides」缩略图卡片 + 核对版本徽标 + 上一篇/下一篇 | `related` 或同栏目有前后篇 |
| 栏目页 | 文章卡片网格(缩略图 + 标题 + 摘要 + 版本徽标) | 栏目有已发布文章 |
| 栏目页 | 多列排序聚合表(`<th>` 可点击排序,904B 内联 JS) | `native.category_tables` 里登记了该栏目 |
| hub 页 | hero(封面 + 一句话)→ 栏目 tile 网格 → 「About this guide」折叠段(首页稿正文)→ Boss quick table → Start here 3 卡 → 全部攻略分栏目列表 | — |
| 结构化数据 | Article + BreadcrumbList(author Person=Jellyfi);栏目/hub 为 CollectionPage,作者页为 ProfilePage | 按页型 |

内联 JS 两段:排序 **904 B**(上限 3KB)、搜索 **1,221 B**(上限 4KB),都走 DOM API 拼结果、不拼 HTML 字符串。
颜色全部走 CSS 变量;主题色沿用 v1 的 `native.theme`(`--accent #8cc4d6` / `--accent2 #c3e2ec`)。

### 10.3 frontmatter 新字段

| 字段 | 类型 | 作用 |
|---|---|---|
| `tldr` | `["…","…","…"]` | 标题下的「Key points」要点框,建议 3–4 行;缺省不渲染 |
| `entity` | `"kall"` | 绑定 `data/valheim/entities.json` 的一个实体 → 右侧信息框 + 自动表 |
| `entities` | `["raft","karve","longship","drakkar"]` | 绑定多个实体(依次渲染多张信息框与 Recipe 表) |
| `images` | `["ss03","ss09"]` | 该页可引用的图片 key;**第一个覆盖 `_images.json` 的封面映射**。正文里 `![alt](ssNN "图注")` 直接按 key 取图 |

原有字段口径不变(`slug/url/title/seoTitle/description/category/language/type/related/sourceUrls/checkedAt/scope/date/updated/reviewed/gameVersion/draft/author`)。
`url` 必须与路由规则一致(中文页是 `/valheim/zh/<slug>/`),不一致构建直接报错。

实体绑定现状:每语种 21 页有信息框(8 boss + 7 biome/区域页 + crafting/mead/farming/portals/ships/intricate-key)。

### 10.4 门禁命令与结果(2026-09-18 本地对 `out/` 复现)

| 命令 | 最后一行 |
|---|---|
| `python3 build.py` | `built 567 html pages`(valheim 82 页 = 两语种各 41) |
| `python3 .gates/check_content.py out --locales de,es,fr,it,ja --default en --dir-lang valheim/zh=zh` | `check_content: 558 页 · 0 阻塞 · 0 警告 (trailingSlash=yes)` |
| `python3 .gates/check_i18n.py out --default en --locales de,es,fr,it,ja --games beast-of-reincarnation,dragonsword-awakening,orc-problem,sephiria,shift-at-midnight` | `5 个游戏目录 · 多语种 1 · 单语种/跳过 4 · 阻塞 0 · 警告 0` |
| `python3 .gates/check_i18n.py out --default en --locales zh --root-default --games valheim` | `1 个游戏目录 · 多语种 1(valheim) · 单语种/跳过 0 · 阻塞 0 · 警告 0` |
| `python3 .gates/check_sitemap.py --out out --host lootlore-ten.vercel.app` | `→ 0 阻塞 · 0 警告`(566 条 loc,其中 `/valheim/zh/` 41 条) |
| `python3 .gates/link_check.py --out out` | `✓ 无死链`(585 条站内链接) |
| `python3 .gates/freshness_audit.py --out out` | `全部在期内,无需动作。` |
| `python3 .gates/tech_audit.py --out out --base … --prefix /valheim/ --summary`(只报告) | canonical / JSON-LD / OG / alt / 宽高 / H1 全 0 问题;title 显示宽度 >60 共 31 页、<30 共 8 页;description <70 共 7 页;词数 <800 共 69 页 |
| 占位语 grep(`coming soon / 待补充 / TBD / TODO / lorem ipsum / 即将上线`) | content 与 out 均 0 命中 |
| 代码层游戏专属文字 grep | `hub/native.py`、`hub/mdlite.py`、`hub/native.css`、`build.py` 0 命中 |

门禁脚本本次改动(待同步回 `seo-jianzhan/scripts` 真相源):

- `check_content.py`:`--dir-lang` 支持多段前缀(`valheim/zh=zh`),取最长匹配。
- `check_i18n.py`:新增 `--root-default` —— 主语种页直接落在栏目根(`/valheim/…`)、其余语种在 `/valheim/<locale>/` 下的布局;`LANG_ATTR` 比较时按主语种码截断(`zh-CN` ↔ `zh`)。
- `gates.yml`:check_i18n 拆成两步(五个既有子站一步、valheim 一步)。

### 10.5 内容密度统计(`python3 scripts/valheim_stats.py`)

每页输出:语言 / 词数(英文按拉丁词数、中文按汉字数)/ 表格数 / 图片数(封面 + 正文 figure,不含卡片缩略图)/ 有无信息框 / 有无 tldr。

| 语言 | 页数 | 有信息框 | 有 tldr | 表格合计 | 图片合计 | 词数 min / 中位 / max |
|---|---|---|---|---|---|---|
| en | 40 | 21 | 1 | 41 | 41 | 193 / 715 / 1362 |
| zh-CN | 40 | 21 | 1 | 41 | 41 | 339 / 1031 / 2425 |

**本轮只统计,不做内容增强**:`tldr` 目前只有 kall 两语各一份(样板),正文配图也只有 kall 两语各一张(样板),其余由后续内容 agent 按这两个样板补。

### 10.6 截图(Playwright Chromium,本地产物,file 路由拦截)

位置:`/tmp/claude-0/-home-claude/656bc16e-3a77-5cd3-aef6-9c8bac0c32b8/scratchpad/v2/shots/`(会话临时目录,未入库),
脚本 `scratchpad/v2/shot.py`,量测数据 `shots/metrics.json`。

`hub-{390,1280}.png`、`bosses-{390,1280}.png`、`kall-{390,1280}.png`、`zh-kall-{390,1280}.png`、
`kall-drawer-390.png`(抽屉打开态)、`bosses-table-scrolled-390.png`(表格横滑后)。

实测:

- 8 张整页在 390 与 1280 下 `scrollWidth == clientWidth`(**无横向溢出**)。
- 抽屉:390 下汉堡按钮 `display:flex`,未开时侧栏 `translateX(-326px)` 在视口外;点击后 `x=0`、宽 320px、44 条链接可见;1280 下按钮 `display:none`、侧栏常驻(x=16,宽 230)。
- 信息框:1280 下在右栏(x=964,宽 300,与标题同一行起);390 下 y=523 落在标题区底(495)之下、正文顶(1042)之上 —— **窄屏在标题下方**。
- 表格横滑:390 下 Boss 聚合表容器 356px / 内容 967px,`scrollLeft` 可推到 611;文章内实体表 356 / 560 同样可滑。
- 修掉一处样式冲突:`hub/style.css` 的 `section{padding:44px 0 0}` 会在信息框顶部留一条空带,已在 `native.css` 里对 `.doc section` / `.rail section` 置 `padding:0`。

### 10.7 v2 待办

| # | 事项 | 谁 |
|---|---|---|
| 1 | ~~内容增强:39×2 页补 `tldr` 与正文配图~~ —— 已完成,见 §11 | 内容 agent |
| 2 | ~~中文实体名:统一译名~~ —— 部分完成(43 个实体中 24 个已填中文名,19 个仍为英文,多为专有名词/无通行译名),见 §11 | 站主 / 内容方 |
| 3 | ~~英文 title 长度~~ —— 已修,`tech_audit` 复测 title >60 = 0、<30 = 2 | 内容方 |
| 4 | 未绑实体的页面(新手/联机/生存类 19 页)没有信息框;是否需要为「机制类」实体(rested / food / death)设计另一种信息框样式,待定 —— **本轮已给 mechanic 类型加通用 key/value 信息框**(`hub/native.py` `_kv_rows`),rested/food/death 等页已用上;若还要覆盖新手/联机/生存类需先在 `entities.json` 补对应 `type: mechanic` 条目 | 站主 |
| 5 | 合并 main 与上线:本分支**未合并、未上线**;合并后需在 GSC 重提 sitemap,并留意旧 `/valheim/<slug>/` 由中文改英文带来的收录波动 | 站主 |

## 十一、内容增强 2026-09-18

本轮在 v2 结构基础上做内容填充与数据修正,不改门禁脚本逻辑(仅 §10.4 记录过的 `check_content.py --dir-lang`、`check_i18n.py --root-default` 两处沿用)。

### 11.1 做了什么

- **tldr + 正文配图**:39×2 篇(kall 样板之外的全部文章页)补齐 `tldr`(3–4 行要点)与正文配图(`_images.json` 20 张范围内选取,中英同步同图不同 alt/图注);category/author/home 类页面不强制。
- **`entity`/`entities` 绑定扩面**:新增绑定页面,信息框从「8 boss + 7 biome/区域页 + 6 个专项页」扩到覆盖更多文章;`hub/native.py` 新增 `type == "mechanic"` 的通用 key/value 信息框(`_kv_rows`,字段清单读数据、标签读 i18n,代码不认识具体字段含义),用于 rested/food/death 等机制类页面。
- **entities.json 4 处 biome 漏项补全**(见 §11.2)。
- **英文 `seoTitle` 长度修正**:37 处 `seoTitle` 改动(en+zh 两语种合计),消除显示宽度 >60 的问题页。
- **`config/i18n/{en,zh-CN}.json`** 新增若干 `f_*` 字段标签(配合 mechanic 信息框与新增 frontmatter 字段)。

### 11.2 entities.json 补项(独立对抗验证发现,fandom API 复核)

验证方法论与结论见 `sites/valheim/verification/2026-09-18/ADV_ENTITIES.md`(完整报告,含 A/B 级抽样与全量核验记录)。触发原因:B 级抽样中命中 1 条 REFUTED(`black-forest.enemies` 缺 Rancid Remains),按协议升级为全量核验,又发现 3 处同类问题,合计 4 个 biome 5 处列表字段不完整。本次用 `https://valheim.fandom.com/api.php?action=parse&page=<Title>&prop=wikitext&format=json` 逐一复核 infobox 原文后补入(只加列表项与来源 URL,不改其他数值):

| biome | 字段 | 补入项 |
|---|---|---|
| black-forest | enemies | Rancid Remains |
| mountains | enemies | Draugr (Mountain towers)、Skeleton (Mountain towers / Cabins)、Bat (Frost Caves) |
| ashlands | enemies | Fallen Valkyrie、Lava Blob、Volture、Skugg |
| mistlands | enemies | Seeker Brood |
| mistlands | key_resources | Dvergr extractor、Sealbreaker fragment、Blue jute |

4 个 biome 的 `source_urls` 各追加对应 fandom 页面链接。

### 11.3 门禁与统计复测(build.py 重跑后)

门禁全绿,命令与 §10.4 一致,结果同为 0 阻塞 0 警告 / 无死链 / 全部在期内;`tech_audit`(只报告)较 §10.4 记录明显改善:title >60 从 31→0,<30 从 8→2;词数 <800 从 69→40(不阻塞,只报告)。占位语与 `待核验` grep 均为 0(`out/editorial-policy` 里 "coming soon" 是编辑方针原文里描述"我们不发布……"的否定句,非真实占位语)。

`python3 scripts/valheim_stats.py` 复测:

| 语言 | 页数 | 有信息框 | 有 tldr | 表格合计 | 图片合计 | 词数 min / 中位 / max |
|---|---|---|---|---|---|---|
| en | 40 | 26 | 40 | 60 | 112 | 266 / 891 / 1458 |
| zh-CN | 40 | 26 | 40 | 60 | 112 | 431 / 1250 / 2572 |

对比 §10.5(增强前):有 tldr 从 1→40,表格从 41→60,图片从 41→112;文章类页面(type=article)逐页复查,全部 ≥1 表、≥2 图,无 0 表或 <2 图的漏项。

### 11.4 截图复查

`scratchpad/v2/shots/enrich/{crafting,food,progression}-{390,1280}.png` 六张,390/1280 两档均无横向溢出、要点框（Key points）随内容正常撑高不溢出容器、表格在窄屏下仍套 `.table-scroll` 可横滑。各页第二张正文图在截图中呈空白色块——核实为 `loading="lazy"` 图片在全页截图工具未滚动到位时的常见捕获伪影(该图片实际 URL 直接 `curl` 返回 200,非死链),不是真实排版缺陷,未做改动。

## 十二、v2 上线记录(2026-09-18)

**移动端修正**:crafting 这类绑 4 个实体的页面,390 宽下 4 个 Quick Facts 信息框此前全部展开堆在正文前,把正文推到很下面(见 §10.6 截图观察)。改法:`hub/native.py` 的 `quick_facts()` 把每个信息框从 `<section class="qf">` 改成 `<details class="qf">`,首个实体 `open`、其余默认折叠,`summary` 显示实体名(原来的 `<h2 class="qf-h">` 移到 `<summary>` 里)。`hub/native.css` 加 `@media(min-width:1025px)` 规则,用 `::details-content` 伪元素强制覆盖浏览器对未展开 `<details>` 的原生折叠渲染(纯 `display:block!important` 不够,Chromium 对未 `open` 的 details 内容有独立于 `display` 的折叠机制,必须覆盖 `::details-content` 才能显示;外层再包一层 `@supports selector(::details-content)`,不支持该伪元素的浏览器退化为「可点击展开」而非强制展开,不影响可用性)。

Playwright 复测(`scratchpad/v2/shot_final.py`,crafting/kall × 390/1280 共 4 张,存于 `scratchpad/v2/shots/final/`,会话临时目录未入库):

- 390 宽:crafting 4 个信息框中仅第一个(Workbench)展开,Forge/Smelter/Charcoal Kiln 折叠为纯标题行,正文(Key points/目录/正文)紧随其后,不再被推到底部;`docTop` 从改动前的更深位置提到 y=887。kall(单实体)展开态与改动前一致,无回归。
- 1280 宽:crafting 4 个信息框全部强制展开、`summary` 隐藏,视觉与改动前(全展开)一致;kall 单实体信息框无变化。
- 两页两档 `scrollWidth == clientWidth`,均无横向溢出。

**门禁**(对重建后的 `out/` 复现 §10.4 全部命令):`check_content` 558 页 0 阻塞 0 警告;`check_i18n`(5 个既有游戏)0 阻塞 0 警告;`check_i18n`(valheim)41/41 页 0 阻塞;`check_sitemap` 566 条 loc 0 阻塞;`link_check --out out` 585 条链接 ✓ 无死链;`freshness_audit` 全部在期内;`tech_audit`(只报告)与 §11.3 一致(title >60=0、<30=2;词数 <800=40,不阻塞);占位语 grep 0(`out/editorial-policy` 的 "coming soon" 假阳性同 §11.3);代码层游戏专属文字 grep 0。

**提交与合并**:commit `5149b20`(`fix(valheim): 移动端 Quick Facts 信息框改为可折叠 details`)push 到 `valheim-v2`。`git fetch origin main` 显示 main 未新增提交(main 与 valheim-v2 分叉点相同,`main..valheim-v2` 14 commits,`valheim-v2..main` 0 commits),**无需 rebase**。`git checkout main && git merge --ff-only valheim-v2` 成功(fast-forward,无新合并提交),main 落在 `5149b20`。`git push origin main`:`f1a9355..5149b20`。`git fetch` 后 `git status -sb` = `## main...origin/main`(ahead 0 / behind 0)。

**Vercel 部署**:`/repos/Jellyfish926/lootlore/deployments?per_page=5`(未按 environment 过滤)显示同一 sha `5149b20` 先建 Preview 部署(id `6518734480`,来自 valheim-v2 分支推送),随后 main 推送追加 Production 部署:

- deployment id `6518737567`,environment `Production`,sha `5149b20`,created_at `2026-09-18T06:16:26Z`
- 状态(`/deployments/6518737567/statuses`):`state=success`,`description=Deployment has completed`

**线上验证**(`https://lootlore-ten.vercel.app`,2026-09-18 06:1x UTC):

| 检查项 | 结果 |
|---|---|
| `/` `/valheim/` `/valheim/kall/` `/valheim/bosses/` `/valheim/zh/` `/valheim/zh/kall/` `/valheim/all/` `/valheim/search-index.json` | 均 200,`last-modified` 均为 `2026-09-18 06:17:1x GMT` |
| `/valheim/kall/` | `lang="en"` 有、`Quick facts` 有、`hreflang="zh-CN"` 有 |
| `/valheim/zh/kall/` | `lang="zh-CN"` 有、`无敌` 有 |
| `/valheim/bosses/` `/valheim/` | 均含 `<table`;`/valheim/` 另含 `class="tile` 网格 |
| `/valheim/crafting/`(线上,验证本次修复) | `<details class="qf">` 出现 4 次 |
| `/sitemap.xml` | 200,`/valheim/` 条目数 82(含 `/valheim/zh/` 41) |
| `/robots.txt` | 200,`Sitemap: https://lootlore-ten.vercel.app/sitemap.xml`(无尾斜杠) |
| `/ads.txt` | 200 |
| `link_check.py --live lootlore-ten.vercel.app` | sitemap 566 页,585 条站内链接,✓ 无死链 |
| GitHub Actions 最近一次 `gates` run(main,sha `5149b20`) | `conclusion: success`(run id `35314163925`) |

**旧中文 URL 说明**:v1 的 `/valheim/<slug>/` 原为中文页,v2 起是英文页,中文移到 `/valheim/zh/<slug>/`;未做 301(同一 URL 只是换了语言,canonical 自指即可),中文页通过 hreflang 与页内切换器可达,详见 §10.1。

**待站主**:GSC 重提 sitemap 并留意旧 `/valheim/<slug>/` 因语言判定变化带来的收录波动(同 §10.7 #5);§10.7 其余未完成项(机制类实体信息框覆盖范围、19 个未译中文实体名)仍待站主拍板。

## 十三、线上问题 hotfix(2026-09-18)

**问题**:站主浏览器里 `/valheim/` 完全没样式(左侧菜单裸列表、`.navtoggle` checkbox 露出)。根因:`/native.css`/`/hub.css` URL 不变但内容 v1→v2 换了,Vercel 响应 `cache-control: public, max-age=86400`,站主昨天访问过 v1,浏览器缓存的旧 CSS 套在新 HTML 上。另有次要问题:hero 封面图 `loading="lazy"` + 1920×1080 原图,首屏留一块空黑框。

**改动**:
1. `build.py` 新增 `version_css()`:构建期对 `hub/style.css`/`hub/native.css` 源内容取 sha1 前 8 位,构建结束后全局改写 `out/**/*.html` 里 `href="/hub.css"`→`?v=<hash>`、`href="/native.css"`→`?v=<hash>`(子站快照 `sources/` 引用各自文件名的 css,不受影响)。`gen_vercel_json()` 里 `*.css`/`*.js` 的 headers 从 `max-age=86400` 改成 `max-age=0, must-revalidate`(双保险)。
2. `hub/native.py`:`cover()` 改用 `_images.json` 里已有的 `src_small`(600×338)做 hero 的实际 `src`,`loading="eager" fetchpriority="high"`(原图 1920×1080 仍留在 `srcset` 里给大屏用);`img_cb_factory`/`figure_cb_factory` 的正文图也改用 600×338 做 `src`,保持 `loading="lazy"`。栏目页(`type=category`)去掉 hero 大图,排序表(`agg_table`)从文末 `extra` 移到要点框(`kp`)之后渲染。`hub/native.css` 给 `.body-fig img` 补 `aspect-ratio:16/9` 与占位背景(`.cover img` 已有)。
3. `.navtoggle` checkbox 隐藏样式(`position:absolute;opacity:0`)本已存在,未改;根因是 CSS 没命中,不是选择器缺失。

**门禁**(本地对重建后的 `out/` 复现 §10.4/§11.3 全部命令):`build.py` → `built 567 html pages`,`css 版本化: hub.css?v=2c0919a4 native.css?v=ad4ae3d6(改写 93 个 html)`;`check_content` 558 页 0 阻塞 0 警告;`check_i18n`(5 个既有游戏)0 阻塞 0 警告;`check_i18n`(valheim)41/41 页 0 阻塞;`check_sitemap` 566 条 loc 0 阻塞;`link_check --out out` 585 条链接 ✓ 无死链;`freshness_audit` 全部在期内;`tech_audit`(只报告)`missing_width_or_height` 0、og:image 缺 2(与改动前一致,非本次引入)。`grep -rl 'href="/hub\.css"' out/` 与 `href="/native.css"` 均为 0 处裸引用。

**截图**(Playwright Chromium,`out/` 本地静态服务器,视口截图非全页):`/valheim/` 与 `/valheim/bosses/` 1280/1920 宽首屏均落在 `scratchpad/v2/shots/hotfix/`。观察:CSS 命中,左侧导航正常分组样式,`.navtoggle` checkbox 不可见;`/valheim/` 首屏可见完整加载的 hero 图(非空黑框);`/valheim/bosses/`(栏目页)无 hero,要点框下直接是可排序表格。

**提交与合并**:`git fetch` 确认本地 main 与 `origin/main` 同点(`42fc881`),直接在 main 上提交,无需 rebase/合并。commit 见下方,`git push origin main`。

**线上验证**(部署成功后):
| 项 | 结果 |
|---|---|
| `curl -s .../valheim/ \| grep -o 'href="/[^"]*\.css[^"]*"'` | 待填 |
| `curl -sI .../native.css` cache-control | 待填 |
| hero `<img>` 含 `600x338` 与 `eager` | 待填 |
| deployment 状态 | 待填 |

---

## 十四、视觉精修 2026-09-18

站主反馈「字体和排版细节还需要调整」。只动 Valheim 栏目:`hub/native.css`(重写)、
`config/hub.json` → `games[valheim].native.theme` / `native.font_css`、`hub/native.py` 与
`hub/mdlite.py` 的少量结构微调。Valheim 是唯一 `kind:native` 的游戏,`native.css` 只被
`/valheim/*` 加载,`git status` 复核:`out/` 里改动的 html 全部在 `out/valheim/` 下。

### 1. 取证(2026-09-18 实测)

| 来源 | 取到的东西 |
|---|---|
| `curl -sL https://www.valheimgame.com/` | `@font-face`:`norsebold` / `norseregular`(`/fonts/norse-*-webfont.woff2`),另引 Google Fonts `Roboto Slab`。页面里可数的 hex:`#ad2817`(锈红)、`#dd6119`(余烬橙)、`#195d8c`(深蓝)、`#0e161d`(近黑)、`#9ca3af`(灰)。CSS 自定义变量:**未获取**(站点是 Tailwind 编译产物,除 `--tw-gradient-from:#000` 外无主题变量) |
| Steam `appdetails?appids=892970` → `header_alt_assets_6.jpg`,PIL MEDIANCUT 取 5 色 | `#202c2e` 22.9% · `#031118` 22.7% · `#445855` 19.8% · `#0e1618` 18.6% · `#221b17` 16.0% —— 整体是**冷调深青灰** |

结论:官网气质 = 近黑底 + 锈红/余烬橙点缀 + 碑刻感标题字;Steam 头图 = 冷调深青灰。
**不取资产**:没有用官方 logo、没有嵌 `norse-*.woff2`(官网自托管字体,授权不明)、没有抄官方文案。

### 2. 字体(落在 `native.theme` / `native.font_css`)

- 标题 **Cinzel**(Google Fonts,SIL OFL,可商用;罗马碑刻大写体,对上「北欧/维京、粗犷、雕刻感」,
  比 Uncial Antiqua / Almendra 可读性高一档)—— 只用于 `h1`、`h2`、站名 `.brand`。
- 正文 **Inter**(400/600)。
- 只加载 2 个字重/家族:`family=Cinzel:wght@600;700&family=Inter:wght@400;600&display=swap`,
  并加 `preconnect` 到 `fonts.googleapis.com` / `fonts.gstatic.com`。
- 中文页(`html[lang^="zh"]`)不下载 CJK 字体:标题回退
  `'Noto Serif SC','Songti SC','Source Han Serif SC','Noto Serif CJK SC',Georgia,serif`,
  正文回退 `system-ui,'PingFang SC','Hiragino Sans GB','Microsoft YaHei','Noto Sans CJK SC'`。
- 中英混排:`text-autospace:normal` + `text-spacing-trim:trim-start`(支持的浏览器自动加四分空);
  中文小标签(`.sn-t/.kp-t/.toc-t/.qf-sub`)把 `letter-spacing` 降到 `.02em`,避免两个汉字被拉开。

### 3. 色板与对比度(全部落 `config/hub.json`,CSS 里 grep 不到 hex)

暗色单主题。总站 `hub.css` 是暗色,所以**不做** `prefers-color-scheme:light`——
只给一个栏目做浅色会和其他游戏页一暗一亮地割裂;`:root{color-scheme:dark}`。

| token | 值 | 出处 | 对 `--bg` 对比度 |
|---|---|---|---|
| `bg` | `#0d1316` | Steam 头图 `#0e1618`/`#031118` | — |
| `bg2` | `#131c20` | 同上,顶栏/页脚 | — |
| `panel` | `#161f23` | Steam 头图 `#202c2e` | — |
| `line` | `#2a383e` | 推导 | — |
| `ink`(正文标题) | `#eef3f4` | 推导 | **16.72:1** |
| `mut`(正文) | `#b6c4c9` | 推导 | **10.45:1**(要求 ≥7:1 ✓) |
| `dim`(面包屑/图注/页脚) | `#8b9ba1` | 推导 | **6.51:1**(要求 ≥4.5:1 ✓) |
| `accent` | `#7fc7dc` | Deep North 冰蓝,站群内与其他游戏不重色 | **9.90:1** |
| `accent2`(hover) | `#bfe6f1` | 推导 | **14.09:1** |
| `visited`(已访问链接) | `#c79a72` | 官网余烬橙 `#dd6119` 降饱和 | 7.3:1 |

派生底色(`color-mix`)上的对比:表头/信息框标题带 `--band` ≈ `#2d444c` 上 `ink` **9.18:1**;
要点框 `--band-soft` ≈ `#203036` 上 `mut` **7.63:1**;表格斑马纹行上 `mut` ≈ 8.4:1。
计算脚本:相对亮度按 WCAG 2.x sRGB 公式,`scratchpad/v2/visual/`。

### 4. 字号阶梯(1280 桌面 / 390 移动,Playwright `getComputedStyle` 实测)

| 元素 | 桌面 | 移动 | 行高 |
|---|---|---|---|
| h1 | 36px(Cinzel) | 28.5px | 1.22 |
| h2 | 24px(Cinzel,带底部细线) | 21px | 1.3,上 44px / 下 12px |
| h3 | 19px | 17px | 1.4 |
| 正文 | 17px(Inter) | 16px | 1.65,栏宽 720px(≈70ch) |
| 表格 | 15px | 14px | 1.4,单元格 9px×12px |
| 信息框 | 标签 13px / 值 14px | 同 | 1.4 |
| 面包屑 / byline | 13px `--dim` | 同 | 1.5 |
| 图注 / 适用范围 | 12px `--dim` | 同 | 1.5 |

### 5. 细节清单

- [x] hero 图注与来源 12px、`--dim`
- [x] 信息框在桌面右栏顶部与 H1 顶对齐 —— 面包屑提出 `.doc-hd` 单独占一行网格
      (`"nav crumb crumb" / "nav head rail" / "nav doc rail"`),实测 `h1.top == qf.top == 104px`
- [x] 卡片图 16:9 裁切一致(`aspect-ratio:16/9;object-fit:cover`)
- [x] 表格横滑右侧渐隐提示(`local` 渐变 + `scroll` 阴影),表头深底 + 字重 600 + 顶部 2px 强调线,
      斑马纹,hover 行高亮;整列纯数字自动右对齐 + `tabular-nums`(`mdlite.is_numeric_cell`,
      `native.py::_table` 与 `mdlite` 表格两处都判)
- [x] `<details>` summary 有指示箭头(`▸`,展开旋转 90°);信息框折叠态 `▾/▴`
- [x] 搜索框与总站顶栏风格一致(同一套 `--rad-sm` / `--box-bd` / 14px 字号)
- [x] 页脚不与正文抢眼(13px、`--dim`、链接也走 `--dim`)
- [x] 中文页标点全角(内容层本来就是);中英混排空格用 `text-autospace` 兜,不改内容
- [x] 移动端 h1 28px / 正文 16px / 表格 14px / 信息框默认折叠
      (`native.py` 去掉首个 `<details open>`,桌面由 `::details-content` 强制展开)
- [x] 一页最多 6 个信息框,桌面改为**显示实体名做标题栏**(原先 `summary{display:none}`,
      6 个框全叫 "QUICK FACTS" 分不清);`pointer-events:none` 使其不可点,仅在支持
      `::details-content` 时生效,老浏览器仍可点开
- [x] 左侧导航当前页 2px 强调色高亮条 + 淡底;分组标题 11px 大写 `.14em` 字距 + 下细线(去掉原来的强调色色块)
- [x] 链接色 `--accent` / 已访问 `--visited` 可区分,hover 加下划线
- [x] 要点框/目录/来源区/卡片/信息框统一 `--rad` `--box-bd` `--box-pad` 一套 token
- [x] 正文限宽 720px,但**标题分隔线、要点框、目录、表格、卡片占满栏宽**,右边缘对齐

### 6. 门禁与截图

`python3 build.py` → 568 页。门禁全绿(与 `gates.yml` 同一批):
`check_content 559 页 · 0 阻塞 · 0 警告` / `check_i18n` 两轮 `阻塞 0 · 警告 0` /
`check_sitemap 0 阻塞 · 0 警告` / `link_check ✓ 无死链` /
`tech_audit missing_alt 0 · h1 missing 0 · multiple 0`。

截图(Playwright Chromium,`color_scheme=dark`,全页):
`scratchpad/v2/shots/design/{hub,bosses,kall,zh-kall}-{1280,390}.png`,
度量落 `metrics.json`;对照改前 `scratchpad/v2/shots/hotfix/` 与 `final/`。

### 7. 线上验证(2026-09-18,commit `1dbcb18`)

| 项 | 结果 |
|---|---|
| `curl .../valheim/` CSS 版本 | `hub.css?v=2c0919a4` · `native.css?v=d87cfa5d`(改前 `eed98701` 之前,版本号已变) |
| Google Fonts `<link>` | 存在:`css2?family=Cinzel:wght@600;700&family=Inter:wght@400;600&display=swap` |
| 线上 `native.css` 与本地 `out/native.css` | md5 一致 `0c4959e411d6fb16bd5b9fc4e2142a9c` |
| Playwright 打真实线上 `/valheim/kall/` | `document.fonts.check('700 36px Cinzel') === true`;h1 36px;`h1.top === qf.top === 104`;`td.num` 3 个;无横向溢出 |
| `/valheim/bosses/` 线上 `class="num"` | 18 个 |
| `/valheim/zh/kall/` 线上 `--font-head-zh` | 注入正常 |
| GitHub Actions `gates` @ `1dbcb18` | completed · **success** |
