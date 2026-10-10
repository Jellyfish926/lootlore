# B4 category 方案（/blockspin/）

读取日 2026-10-10 UTC。只读了仓，没改仓。

## 现状（仓里实测）

| 栏目页 | category 字符串 | draft | 已发布成员 |
|---|---|---|---|
| getting-started.md | "Getting Started" | false | codes、beginner、game-info、cheats-bans（4 篇） |
| money-gear.md | "Money & Gear" | **true** | 0（原承诺的 jobs / map-locations / weapons / vehicles 全是 draft） |

`config/hub.json` 的 blockspin `native.nav` 已是 `["getting-started", "money-gear"]`，**不用改 config**。`hub/native.py:333-372`：文章的 category 只要对得上任一栏目页（含 draft）就不报错，但栏目页是 draft 或没有已发布成员时不进 `live_cats`，不生成、不进导航。

## 方案

1. robux-shop、weapon-packs、mansion-upgrades 三页都挂 `category: "Money & Gear"`（三份源文件已这样写）。理由：三页讲的都是「花 Robux 买什么」，不属于新手四篇；且三页正好满足规范 A1「新栏目先有 3–5 篇」。
2. **money-gear 栏目页要翻正**，并且必须整页重写：旧稿的 4 张卡片全部指向 draft 页，正文还写着「every detail checked against the live game」，和新页的取证方式（官方接口记录）不符。改写后的完整源文件：`drafts/money-gear.md`（格式照 getting-started.md：`### [标题](url)` 卡片 + 一段说明；`draft: false`；date / updated / reviewed 2026-10-10；title 55 / seoTitle 59 / description 156 字符，全仓 grep 无重复）。
3. 四个文件要**同批接入**：只上文章不翻栏目页，三页会没有可用的栏目（面包屑 / 上下篇落空）；只翻栏目页不上文章，构建会警告「栏目没有已发布文章」。
4. 如果验收后只有 1–2 页能发：把能发的页改挂 `"Getting Started"`，money-gear 保持 draft（不为 1–2 篇开栏目）。

## 我在自己的拷贝里验过的

`$SP/b4/lootcopy`（content / hub / .gates / config / data + build.py、build-stamp.json 的拷贝，原仓未动）放入四个文件后 `LOOTLORE_BUILD_DATE=2026-10-10 python3 build.py`：

- 日志：`[blockspin] native: 1 语种,生成 12 页,草稿跳过 4(en/jobs, en/map-locations, en/vehicles, en/weapons)`，blockspin 0 条警告（无「外链不在 sourceUrls」「链到草稿」「related 不存在」）。
- 产物里有 /blockspin/robux-shop/、/weapon-packs/、/mansion-upgrades/、/money-gear/，四页各 1 个 H1，面包屑含 Money & Gear；三篇文章 `<main>` 内表格 4 / 3 / 3。
- tech_audit `--prefix /blockspin/`：title 12 页全在 30–60、description 无超长 / 重复、img 无缺 alt、h1 无缺 / 多。
- check_content 在这份**不完整拷贝**上报 86 条 DEAD_INTERNAL，全部指向 /guides/、/index、/reviews/（拷贝里没带 sources / reviews 等目录造成，来源页是各游戏全站页脚），没有一条来自新页自己的链接；sitemap 门禁同理因拷贝不全没产出 sitemap.xml。**这两道要在完整仓里由工程师重跑**，我这里不算通过也不算失败。输出存 `raw/w-gate-check_content.txt`、`raw/w-gate-link_check.txt`。

## 留给工程师的事

- `_images.json` 的 `pages` 映射要加 4 行（我没改）：robux-shop→th3、weapon-packs→th4、mansion-upgrades→th1、money-gear→th2（源文件 `images:` 已按此写；money-gear 从 th1 换成 th2，是为了让 index th3 / getting-started th4 / author th1 / money-gear th2 四个 native 页封面互不相同）。
- 图片池只有 4 张 16:9 + 1 个方形图标，12 页必然重复封面（th3：index、cheats-bans、robux-shop；th4：beginner、getting-started、weapon-packs；th1：codes、author、mansion-upgrades）。规范 B6 允许官方 16:9 不够时用商品图标补池（商品记录里有 `IconImageAssetId`），要不要补由工程师定；我没自造任何图片 URL。
- 旧草稿 weapons.md、vehicles.md、jobs.md、map-locations.md 保持 draft，未动。weapons 与 weapon-packs 同主题，以后不要两页同时发布。
