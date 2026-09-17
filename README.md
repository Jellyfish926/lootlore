# Lootlore — 游戏攻略总站

聚合站群内容的总站。三层分离:

- **框架层** `build.py` + `hub/`(总站壳:首页/信任页模板与样式)
- **配置层** `config/hub.json`(base_url、品牌、游戏清单、剥离/映射/补丁规则)
- **内容层** `sources/<game>/`(各子站静态快照,原样保存,变换只发生在构建时)
  + `content/<game>/*.md`(`kind: "native"` 的游戏:没有独立子站,Markdown 就是真相源,构建时渲染)

构建:`python3 build.py [--base https://域名]` → 产物在 `out/`(Vercel 直接服务,outputDirectory=out,无构建命令)。

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
5. 跑与 `gates.yml` 同一批门禁脚本(check_content / check_i18n / check_sitemap / link_check),**红一条就不提交**;
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
| 配置 | `config/hub.json` 里该游戏一项:`kind/lang/content/native{title,nav,related_heading,official_domains,author,defaults,theme}/card{…}` · `config/i18n/<lang>.json`(界面文字) |
| 内容 | `content/<game>/<slug>.md`(frontmatter + 正文,正文自带 H1)· `content/<game>/_images.json`(封面截图与 alt、图注) |

**路由**:`type: home` → `/<game>/`,其余 → `/<game>/<slug>/`;frontmatter 的 `url` 必须与之相同,否则构建报错。

**frontmatter 字段**(只加不改名):`slug title seoTitle description category type(home|category|article|author) related sourceUrls checkedAt scope date updated reviewed gameVersion draft author`。
缺省值取 `native.defaults`;`updated` 缺省 = `date`,`reviewed` 缺省 = `checkedAt`;`gameVersion` 为空时 byline 不显示该项。

**更新内容**:直接替换 `content/<game>/*.md` → `python3 build.py` → 跑门禁。正文末尾与 `native.related_heading` 同名的小节会被剥掉,改由 `related` 渲染「关联阅读」;
栏目页里 `### [标题](/<game>/<slug>/)` + 说明段的卡片块按数据重渲染(栏目成员 = 卡片顺序 + 同 `category` 的其余文章,可跨栏目列出而不重复 URL)。

**draft 门控**:`draft: true` 的页不生成、不进 sitemap、不进栏目列表 / hub 清单 / 关联阅读 / 作者页;正文里指向它的链接降级为纯文本(构建日志会打印警告)。
没有已发布文章的栏目不生成、不进导航。

**sitemap**:原生页 `lastmod = reviewed ?? updated ?? date`,其余页仍用构建日。

**门禁**(与 gates.yml 一致):`check_content.py … --dir-lang <game>=zh`(单语种非英文游戏目录的 lang 判定)、`check_i18n.py --games …,<game>`(单语种会明确打印跳过)、
`check_sitemap.py`、`link_check.py`;另有只报告的 `tech_audit.py --out out --base <域名> --prefix /<game>/ --summary`(title/description 按显示宽度,CJK 记 2)。
