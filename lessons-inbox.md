# lessons-inbox(待并入 skill 的实测经验)

格式:日期 · 实验条件 · 结论 · 建议并入位置。只记实测。

## 2026-09-17 · lootlore `/valheim/` 原生中文内容接入(分支 valheim,40 页 zh-CN)

1. **[已并入 2026-09-17] 中文 title/description 按字符数判长度会误判,改按显示宽度(1 汉字 ≈ 2 字符),不放松阈值。**
   条件:`seo-jianzhan/scripts/tech-audit.py` 原样跑 lootlore 产物,只看新增 40 页。
   原口径(`len()`):title 30 页「30–60 合格」、10 页「<30 过短」;description 39/40 页不足 70。
   显示宽度口径:title **30 页 >60(62–73,SERP 会截断)**、6 页 <30(栏目页 20–24 宽,真偏短)、首页与作者页从「过短」变为合格;description 只剩 6 页(栏目页)<70。
   即字符口径对中文**同时误报(过短)又漏报(过长)**。lootlore 已在 `.gates/tech_audit.py` 实装 `display_len()`(CJK/全角记 2)。
   → 并入 `seo-jianzhan/scripts/tech-audit.py`(title/description 两项)、`check_config.py` 的 TITLE_LEN、`references/audit-rules.md` 在「CJK 词数计算」旁加「CJK 长度计算」小节。

2. **[已并入 2026-09-17] tech-audit 把外部热链 og:image 当本地文件查,40/40 页误报 `og_image_file_missing`。**
   条件:封面用 Steam 商店页官方截图热链(shared.akamai.steamstatic.com)。
   修法:og:image 域名 ≠ 本站时单独计 `og_image_external`,不查本地文件(本地图仍按原规则查)。
   → 并入 `tech-audit.py` 第 5 项与 SKILL.md ⑥「技术 SEO 审计」表第 5 行的说明。

3. **[已并入 2026-09-17] `check_content.py` 解析时跳过 `<header>` 内的全部内容,把 H1 包在 `<header>` 里会被判 H1=0。**
   条件:文章标题区最初写成 `<article><header class="doc-hd"><h1>…`,40 页全部报 `H1_COUNT 0`。改成 `<div class="doc-hd">` 后清零。
   → 并入 SKILL.md ⑥ 八道门禁表 `check_content` 行备注:「页内标题区不要用 `<header>` 元素包 H1(门禁把 header 当站点框架跳过)」。

4. **[已并入 2026-09-17] 总站里「整个游戏目录是单一非英语、没有语种子目录」时,`check_content` 的 LANG_ATTR 会整目录误报。**
   条件:`/valheim/` 全站 `lang="zh-CN"`,脚本把无语种段的页当主语种 en,报 40 条 LANG_ATTR 警告(与 2026-09-11 `/beast-of-reincarnation/` 那次是同一类路径假设)。
   修法:`check_content.py --dir-lang valheim=zh`(按目录声明语种,并对这些目录跳过 LOCALE_LINK)。`check_i18n --games` 对该目录会明确打印「单语种跳过」。
   → 并入 `seo-jianzhan/scripts/check_content.py` 真相源,SKILL.md ⑥ 2026-09-11 那段后补一句。

5. **[已并入 2026-09-18] 云容器里 Playwright 访问本地预览服务器会被 agent proxy 拦成 405。**
   条件:`HTTPS_PROXY` 指向 127.0.0.1 上的 agent proxy;Chromium 带 proxy 启动后,`bypass: 127.0.0.1` 无效,请求 `http://127.0.0.1:8765/` 返回代理的 405 页面。
   修法:不起 HTTP 服务,用 `context.route("https://preview.<任意>.test/**", …)` 直接从 `out/` 读文件 fulfill;外部图片仍走代理正常加载。
   → 并入 `gongzuo-jichu` 执行环境一节(或 seo-jianzhan Gate 1.5「肉眼看页面」的云端做法)。

6. **[已并入 2026-09-17] 中文攻略按「拉丁词 + 汉字/2」折算后普遍达不到 800 词下限——需要站主定中文页的字数口径。**
   条件:32 篇攻略正文 685–963 个汉字,渲染后按 `tech_audit` 口径(`<main>` 内正文,含来源与关联阅读区)折算为 518–665 词、中位 568,按现行 ④⑤「内页 800–1500 词」全部算薄页。
   结论:折算公式本身没问题(防的是按空格分词的严重低估),问题在中文页的下限尚无单独规定;是否要求中文长文 ≥1600 汉字,待拍板。
   → 拍板后并入 SKILL.md ④⑤ 硬规格表「内页正文」行。

7. **[2026-09-18 hotfix,待并入] 静态站改 CSS 后 URL 不变,Vercel `Cache-Control: max-age=86400` 会让老访客继续用浏览器缓存的旧 CSS 套在新 HTML 上——必须给 CSS(和 JS)URL 做内容哈希版本化,光靠改响应头不够。**
   条件:`/native.css``/hub.css` 内容 v1→v2,URL 不变,响应头 `public, max-age=86400`;站主前一天访问过 v1,浏览器命中缓存直接用旧 CSS 渲染新 HTML,左侧菜单裸列表、checkbox 露出。改响应头为 `max-age=0, must-revalidate` 只能防未来的老缓存问题,不能让已经缓存了 v1(且未过期)的浏览器立刻拿到 v2——真正生效的是让 URL 随内容变化(`/hub.css?v=<sha1 前 8 位>`),这样新 HTML 天然指向新 URL,与响应头无关。
   修法:`build.py` 新增 `version_css()`,构建期对 `hub.css`/`native.css` 源文件内容取 sha1 前 8 位,全局改写 `out/**/*.html` 里的 `href="/hub.css"`→`href="/hub.css?v=<hash>"`(同 native.css);子站快照(`sources/`)引用各自文件名的 css,不受影响,不用改。同时把 vercel.json 里 `*.css`/`*.js` 的 headers 从 `max-age=86400` 改成 `max-age=0, must-revalidate`(双保险,即使以后漏打版本号也不会被长缓存钉住)。
   → 拍板后并入 `seo-jianzhan` §上线清单/发布前检查:「静态 HTML+CSS 分离站改 CSS 内容前,先确认引用 URL 是版本化的(哈希/查询参数),否则线上访客会花一整个 max-age 周期才看到修好的样式」。
