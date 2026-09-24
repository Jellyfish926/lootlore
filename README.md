# LootWiki — 游戏攻略总站

聚合站群内容的总站(品牌 **LootWiki**,仓名仍是 lootlore)。三层分离:

- **框架层** `build.py` + `hub/`
  - `hub/shell.py` —— 全站统一外壳组件:一级导航(实体×意图两栏)、面包屑、byline、
    **左侧常驻游戏内导航**(`game_nav`,hub 页与内容页共用,快照套壳也用这一个)、
    右栏小组件、FAQ 手风琴、页脚、全站搜索表单与内联脚本
  - `hub/pageindex.py` —— 全站索引:从 `sources/<game>/**.html`(栏目取页面自带的
    BreadcrumbList,扁平站退回 hub 页卡片网格分组)与原生内容自动发现页清单、栏目、更新日。
    **不手工维护任何链接清单**
  - `hub/snapshot.py` —— **快照游戏套壳渲染器**:把 `sources/<game>/**.html` 当内容源重新渲染,
    `<main>` 内的正文逐字节沿用子站产出,外壳换成 `hub/shell.py` 的同一套组件。
    只做三次"搬位置"(H1 → 标题区、子站面包屑 → 外壳面包屑、子站署名行 → byline 位)+
    给没有 id 的 h2/h3 补锚点;head 元数据(title/description/canonical/hreflang/JSON-LD/og)
    原值保留,只补子站没有的。界面文字跟每页 `<html lang>` 走 `config/i18n/<lang>.json`,缺 key 回退英文
  - `hub/hubbody.py` —— **游戏 hub 页正文的视觉模块组**:实体数据驱动的速查表、
    带缩略图+页数徽章的栏目磁贴、各栏目精选卡片、工具磁贴、统计胶囊、单行时间线、
    要点框、范围提示框(提示框的标题与正文逐字取自该游戏自己某一页的第 N 个 h2 与其后
    第一段,所以自动跟着页面语言走)。出哪张表/取哪几列/排序/行数上限全在
    `config/hub.json` 的 `games[].hub_body` 里声明;表头走 `config/i18n` 的
    `f_<字段>` / `tbl_<type>`,没登记标签的字段直接构建报错。
    两条失败关闭:整列全空不出列;某列含"指向同一条实体另一个字段名"的内部交叉引用不出列。
    快照 hub 页的插入方式见 `hub/snapshot.split_at_h2` —— 正文按 `<h2>` 序号分装进多个
    `.sn-body`,**逐字节零改动**,`.gates/check_snapshot.py` 每次构建后实测这一条
  - `hub/style.css` → `out/hub.css`(全站外壳样式)· `hub/native.css`(内容页专属件)·
    `hub/snapshot.css`(快照正文里子站自己的类名 `.wrap/.hero/.tablewrap/.tracker-*` 的统一皮肤,
    全部收在 `.sn-body` 作用域里,顺带中和 hub.css 的同名全站选择器)
  - `hub/hub_page.html` / `hub/native_page.html` / `hub/snapshot_page.html`(三个页型模板)
  - `hub/pages/*.html`(总站自有页面的**片段**:头部 `<!-- title/description/path/h1 -->`
    + 正文;外壳由 build.py 统一套)
  - 三个渲染器同一套外壳:总站自有页(`build.py`)、原生内容页(`hub/native.py`)、
    快照套壳页(`hub/snapshot.py`)—— 左侧常驻导航 / 面包屑 / byline / 右栏 / FAQ / 页脚全部走 `hub/shell.py`
- **配置层** `config/hub.json`(base_url、品牌、**站级视觉 token `theme`**、字体、
  一级导航意图栏 `intent_nav`、`/tools` 收录关键词 `tools_match`、首页 hero 取哪个游戏
  `hero_game`、游戏清单、剥离/映射/补丁规则、**实体数据绑定 `entities` + `entity_match`**)
  + 每个游戏的 **hub 页正文模块声明 `hub_body`**(`scope` 取哪一页哪一个 h2 当提示框、
  `tables` 出哪几张速查表、`slots` 插在正文第几个 `<h2>` 之前、`picks` 精选卡片条数)
  + `config/i18n/<lang>.json`(**全部界面文字**;现有 en / zh-CN / ja / de / es / fr / it)
- **内容层** `sources/<game>/`(各子站静态快照,原样保存,变换只发生在构建时)
  + `content/<game>/*.md`(`kind: "native"` 的游戏:没有独立子站,Markdown 就是真相源,构建时渲染)

改名 / 换域名 / 换配色都是**改一处配置**:品牌 `brand`、域名 `base_url`、色板 `theme`。
框架层不写任何 hex、任何界面文字、任何游戏专属文字;门禁工作流的域名也从 `base_url` 读。

构建:`python3 build.py [--base https://域名]` → 产物在 `out/`(Vercel 直接服务,outputDirectory=out,无构建命令)。
构建日期可注入:`LOOTLORE_BUILD_DATE=YYYY-MM-DD python3 build.py`(不设就用今天)。每次构建把这个日期写进仓库根的 `build-stamp.json`(要提交);
CI 用它钉住日期重建,再 `git diff --exit-code -- out build-stamp.json` 校验「提交的 out/ 是否等于新鲜构建」—— 构建日会写进 12 个页面(byline / sitemap 兜底),不钉住的话次日起天天误红。

构建期自动产出(数字全部来自实际统计,页面上不写死):
- 首页游戏卡片的页数与最近更新日、`/updates/` 变更日志(跨游戏按复核日倒序)、
  `/guides/` 与首页的全量攻略索引、`/tools/` 工具页(按 `tools_match` 匹配真实存在的工具页)
- `out/search-index.json` —— **跨全部 6 个游戏**的全站搜索索引,每条带 `game` 与 `lang`;
  前端过滤脚本内联(≤3KB,DOM API 拼结果),无 JS 时退化到 `/guides`(总站)或
  `/<game>/all/`(游戏内)
- CSS / JS / 搜索索引按内容 sha1 打 `?v=xxxxxxxx`(配合 `vercel.json` 里
  `max-age=0, must-revalidate`)—— 改了样式但 URL 不变会让浏览器把缓存的旧 CSS 套在新 HTML 上,
  页面直接崩,这道必须留着

域名到位后:`python3 build.py --base https://新域名` 重建并提交。
新增游戏:快照放 `sources/`,在 `config/hub.json` 的 `games` 加一项,重建。

## 同步机制(sources/ 怎么来的)

`sources/<游戏>/` 不手改,全部由 `.github/workflows/sync-sources.yml` 自动从五个子站仓的**构建产物**全量刷新。

| sources 目录 | 子站仓 | 产物位置 |
| --- | --- | --- |
| `sources/beast` | `Beast-of-Reincarnation` | 仓根(手写静态 html;剔除 `.github` / `.gates` / `planning` / `reviews` / `scripts` / `README.md` / `site-dossier.md`) |
| `sources/shift` | `shift-at-midnight-wiki` | `public/`(`_src/` 下的 Python 生成器输出) |
| `sources/sephiria` | `sephiria-wiki` | `out/`(`npm ci && npm run build`,next `output:'export'`) |
| `sources/dragonsword` | `dragonsword-guide` | `out/`(同上) |
| `sources/orc` | `orc-problem-guide` | `out/`(同上) |

**触发方式**

- 每日定时:UTC 20:00 = 北京时间 04:00。
- 手动:GitHub 仓库页 → **Actions** → 左栏选 **sync-sources** → 右上 **Run workflow** → 分支选 `main` → 绿色 **Run workflow**。

**一次运行做什么**

1. 用 secret `SUBSITE_TOKEN`(repo scope PAT)checkout 五个子站;
2. Next 三站 `npm ci && npm run build`(node_modules 走 `actions/setup-node` 的 npm 缓存);
3. `python3 scripts/sync-sources.py --src-root subsites` —— 先删后拷,全量替换 `sources/<游戏>/`;
4. `python3 build.py` 重建 `out/`;
5. 跑与 `gates.yml` 同一批门禁脚本(check_content / check_i18n / check_snapshot / check_sitemap / link_check),**红一条就不提交**(`check_ga` 与产物漂移校验只在 `gates.yml` 提交后复核那一轮跑);
6. 有 diff 才提交(身份 `Jellyfish926 <zsn2740784715@gmail.com>`,信息列出五个子站来源 sha)并 push;无 diff 打印「无变化」。

唯一一处对快照的加工:Next 三站的随机 `buildId` 会被换成固定串 `static-export`
(`next build` 每次都换一个,不归一化的话内容一字未改也会有 ~300 个文件的假 diff;
`build.py` 本来就会剥掉 `__next_f` 脚本,这个串在 `out/` 里不出现)。

push 用的是 PAT 而不是 `GITHUB_TOKEN`,所以这次 push 会正常触发 `gates.yml`(`GITHUB_TOKEN` 推的 commit 不会触发其它 workflow)。工作流内部那一轮门禁是提交前闸门,`gates.yml` 是提交后复核,两道都要绿。

**来源 sha 在哪看**

- `config/sources.json`:每个游戏一条 `{repo, product, sha, files, html, synced_at}`,由同步脚本生成;
- 同步 commit 的正文也逐行列出五个子站的 `repo @ sha`。

手动同步(本地调试)也走同一个脚本:

```
python3 scripts/sync-sources.py --game sephiria --src ../sephiria-wiki
python3 build.py
```

真相源说明:所有快照均来自各子站仓 `main` 分支的构建产物,由上述工作流保持同步。

## 原生内容游戏(kind: native)

有的游戏不来自子站快照,而是直接在本仓写 Markdown(目前:`/valheim/`,中文)。`build.py` 主流程会渲染它们,
所以 `sync-sources.yml` 重建 `out/` 时也会一起生成,不会丢页;同步脚本只动 `sources/<五个子站>/`,不碰 `content/`。

| 层 | 文件 |
| --- | --- |
| 框架 | `hub/native.py`(页型、面包屑、目录、来源、关联阅读、JSON-LD、draft 过滤)· `hub/mdlite.py`(纯标准库 Markdown 渲染)· `hub/native_page.html` · `hub/native.css` |
| 配置 | `config/hub.json` 里该游戏一项:`kind/lang/content/native{title,nav,related_heading,official_domains,author,defaults,search,start_here,entities,hub_table,category_tables}/card{…}`(想给单个游戏换配色再加 `native.theme`,只写与站级 `theme` 不同的键) · `config/i18n/<lang>.json`(界面文字) |
| 内容 | `content/<game>/<slug>.md`(frontmatter + 正文,正文自带 H1)· `content/<game>/_images.json`(封面截图与 alt、图注) |

**路由**:`type: home` → `/<game>/`,其余 → `/<game>/<slug>/`;frontmatter 的 `url` 必须与之相同,否则构建报错。

**frontmatter 字段**(只加不改名):`slug title seoTitle description category type(home|category|article|author) tldr faq related sourceUrls checkedAt scope date updated reviewed gameVersion draft author`。
`faq`(只在 `type: home` 上有效)= `[[问, 答], …]` 的单行 JSON;答里可以写 markdown 链接,走与正文同一条链接校验,指向不存在的页直接构建报错。渲染成 hub 页底部的 `<details>` 手风琴 + `FAQPage` JSON-LD;**没有这个字段就不出 FAQ 区块**(不许为了有区块而编问答)。
正文里可以写 `{{BRAND}}`,构建期替换成 `config/hub.json` 的 `brand`。
缺省值取 `native.defaults`;`updated` 缺省 = `date`,`reviewed` 缺省 = `checkedAt`;`gameVersion` 为空时 byline 不显示该项。

**更新内容**:直接替换 `content/<game>/*.md` → `python3 build.py` → 跑门禁。正文末尾与 `native.related_heading` 同名的小节会被剥掉,改由 `related` 渲染「关联阅读」;
栏目页里 `### [标题](/<game>/<slug>/)` + 说明段的卡片块按数据重渲染(栏目成员 = 卡片顺序 + 同 `category` 的其余文章,可跨栏目列出而不重复 URL)。

**draft 门控**:`draft: true` 的页不生成、不进 sitemap、不进栏目列表 / hub 清单 / 关联阅读 / 作者页;正文里指向它的链接降级为纯文本(构建日志会打印警告)。
没有已发布文章的栏目不生成、不进导航。

**sitemap**:原生页 `lastmod = reviewed ?? updated ?? date`,其余页仍用构建日。

**Consent Mode v2 默认值**:每页 `<head>` 里由 `build.py:head_scripts()` 统一注入,顺序固定 consent default → AdSense → gtag.js → `gtag('config')`。同意弹窗用的是 Google 自家 CMP(AdSense「欧洲法规消息」,只对 EEA/UK/瑞士弹),它只更新弹窗用户的同意状态,所以非弹窗地区的默认值必须站点自己设:`CONSENT_DENIED_REGIONS`(EEA 30 国 + GB + CH)那条全 denied 并 `wait_for_update:500` 等 CMP 回写,不带 region 的兜底条全 granted。这段必须排在所有 Google 脚本之前——gtag.js / adsbygoogle.js 一旦先跑,default 就不生效(Google 文档原话:「If your consent code is called out of order, consent defaults won't work」);dataLayer / gtag 的定义也只在这一段里出现一次,GA 片段不再重复定义。`ga4_id` 留空时 consent 段照常输出(AdSense 也吃这个信号)。`404.html` 走 `head_scripts(ads=False)`:AdSense 政策不许错误页带广告代码,404 只留 consent 段 + GA 片段(`check_ga` 的 `ADS_ON_404` 断言兜底)。

**提需求弹窗(Web3Forms)**:每页最多三个入口——右栏「Missing something?」卡片(`hub/shell.py:request_card`,只挂在本来就有右栏的页的右栏末尾;`no-rail` 页不为它硬加右栏)、页脚链接(`request_link`,每页都有)、右下角浮动按钮(`request_fab`,手机端每页显示;桌面端只在没有右栏卡片的页显示——首页和所有 `no-rail` 页,CSS 选择器 `main.home~.req-fab,main.no-rail~.req-fab`)——都打开同一个原生 `<dialog>`(`request_dialog` + `REQUEST_JS`,不依赖任何三方 JS)。字段:需求类型 / 游戏(自动选中当前页所属游戏,选项来自 `games`)/ 内容(必填 ≥10 字)/ 联系邮箱(选填,Web3Forms 拿它当 reply-to);隐藏字段自动带 `page_url` / `page_lang` / `user_agent`,蜜罐 `botcheck`(checkbox,display:none,提交时显式带 boolean)。提交 `POST https://api.web3forms.com/submit`(JSON,按其 API Reference),邮件主题由 i18n 的 `req_subject` 拼出。**开通**:到 web3forms.com 用 `contact_email` 申请 Access Key,填进 `config/hub.json → web3forms_key`,重建即通;key 为空时弹窗照常渲染,只是发送按钮 disabled + 显示「暂未开通」+ mailto 兜底(主题预填)。文案全部在 `config/i18n/*.json` 的 `req_*` 键(七语种各 28 个);样式在 `hub/style.css` 末尾「提需求」段,只用 token。入口链接的 href 本身就是 mailto,无 JS 时退化为直接写邮件。

**门禁**(与 gates.yml 一致):`check_content.py … --dir-lang <game>/<locale>=<lang>`(单语种非英文游戏目录的 lang 判定)、`check_i18n.py --games …,<game>`(单语种会明确打印跳过)、
`check_ga.py --out out`(GA4 只许 `config/hub.json` 的 `ga4_id` 那一个 ID,每页外链 + 内联各恰好 1 次且都在 `<head>`;`ga4_id` 留空则产物里一处都不许有;另查 Consent Mode v2 默认值:带 region 的 denied 条 + 不带 region 的 granted 兜底条每页各恰好 1 次、`window.dataLayer=…||[]` 恰好 1 次、consent 段按字节偏移排在 adsbygoogle.js / gtag.js / `gtag('config')` 之前)、
`check_sitemap.py`、`link_check.py`;另有只报告的 `tech_audit.py --out out --base <域名> --prefix /<game>/ --summary`(title/description 按显示宽度,CJK 记 2)。
