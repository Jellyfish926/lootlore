# Lootlore — 游戏攻略总站

聚合站群内容的总站。三层分离:

- **框架层** `build.py` + `hub/`(总站壳:首页/信任页模板与样式)
- **配置层** `config/hub.json`(base_url、品牌、游戏清单、剥离/映射/补丁规则)
- **内容层** `sources/<game>/`(各子站静态快照,原样保存,变换只发生在构建时)

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
