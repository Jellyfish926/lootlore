# Guide Atlas — 游戏攻略总站

聚合站群内容的总站。三层分离:

- **框架层** `build.py` + `hub/`(总站壳:首页/信任页模板与样式)
- **配置层** `config/hub.json`(base_url、品牌、游戏清单、剥离/映射/补丁规则)
- **内容层** `sources/<game>/`(各子站静态快照,原样保存,变换只发生在构建时)

构建:`python3 build.py [--base https://域名]` → 产物在 `out/`(Vercel 直接服务,outputDirectory=out,无构建命令)。

域名到位后:`python3 build.py --base https://新域名` 重建并提交。
新增游戏:快照放 `sources/`,在 `config/hub.json` 的 `games` 加一项,重建。

真相源说明:两站快照取自 2026-09-01 的 GitHub 仓库(Beast-of-Reincarnation / shift-at-midnight-wiki)最新 main。子站后续更新需重新快照再构建。
