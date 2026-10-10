# One Tap round2 修改记录(fix2,2026-10-10)

对应 `verify/one-tap/round2.md` 的 N1–N3。只改了 `content/one-tap/` 目录。改前 / 改后句逐字取自文件(脚本断言过改后句在现文件里存在);`\|` 表示表格竖线。「N1 同类」「N2 同类」是按要求全栏目 grep(the season / season / timer / visible / progress / battle pass screen,范围:12 个页面 + entities.json + config-snippet.json,不含 todo.md)后连带统一的句子。

| 编号 | 文件 | 改前句(逐字) | 改后句(逐字) | 处理方式 |
|---|---|---|---|---|
| N1 | battle-pass.md | 3. Check how long the season has left. No listing gives an end date for a season. | 3. If the game shows a season, check how long it has left. No listing gives an end date for a season. | 照改 |
| N1 | battle-pass.md | - Whether Premium Battlepass covers one season or carries over. | - Whether Premium Battlepass, if it is a season purchase, covers one season or carries over. | 照改 |
| N1 | battle-pass.md | - What earns battle pass progress: kills, quests, XP or something else. | - Whether there is battle pass progress, and if so what earns it: kills, quests, XP or something else. | 照改 |
| N1 | battle-pass.md | 1. Open the battle pass screen and count the tiers. No official source we read gives that number. | 1. If the game has a battle pass screen, count the tiers on it. No official source we read gives that number. | 照改 |
| N1 同类 | battle-pass.md | 2. Read what the screen says the premium purchase includes. The record named Premium Battlepass has no description. | 2. If that screen exists, read what it says the premium purchase includes. The record named Premium Battlepass has no description. | 连带(预设有战令界面) |
| N1 同类 | battle-pass.md | it would cost less than single skips only when more than 30 tiers remain, and how many tiers a season has is not stated. | it would cost less than single skips only when more than 30 tiers remain, and the number of tiers is not stated. | 连带(预设赛季有层数) |
| N1 同类 | battle-pass.md | ## How do One Tap seasons and updates fit together? | ## Which One Tap update listings mention a season? | 连带(H2 预设有赛季在运行) |
| N1 同类 | battle-pass.md | So the records we read do not show whether a new season started after April 2026. | So the records we read contain no season line after the April 2026 listing. | 连带(预设赛季已开始过) |
| N1 同类 | battle-pass.md | - How many tiers a season has. | - How many tiers there are, if the game has tiers. | 连带 |
| N1 同类 | battle-pass.md | - What a season rewards, with or without the premium purchase. | - What a season rewards, if seasons are running, with or without the premium purchase. | 连带 |
| N1 同类 | battle-pass.md | - How long a season lasts, and when the current one ends. | - How long a season lasts, and whether one is running now. | 连带(去掉 the current one) |
| N2 | rewards.md | \| 2x Level XP pass \| 149 \| Not a timer; a one-time pass \| | \| 2x Level XP pass \| 149 \| A pass, paid once; no time in the name \| | 照改 |
| N2 同类 | rewards.md | whether a timer runs while you are offline | whether any time counts down while you are offline | 连带(去掉 timer) |
| N3 | updates.md | So some listings have been visible well ahead of their start date. | So some listing records existed well ahead of their start date; the records do not show when each one became visible. | 照改 |
| N1 同类 | updates.md | 12 content lines covering maps, cases, a battle pass season, leaderboards, player reports and crosshair size. | 12 content lines covering maps, cases, a Battlepass season line, leaderboards, player reports and crosshair size. | 连带(tldr 用 listing 原词) |
| N1 同类 | game-info.md | Progress is tracked inside the game: the description names levels, daily and quests as reward sources, | The description points to in-game rewards instead: it names levels, daily and quests as reward sources, | 连带(预设有进度追踪) |

grep 后保留不动的命中(不属于预设句):game-info.md 引用 Roblox 文档原话 "Social media links are only visible to users…";gamepasses.md 与 entities.json(pass-2x-case-luck.usage_en)里的 "a final full stop, if any, is not visible";battle-pass.md 里引 listing 原文的 "New Battlepass season" / "New BP Season"、"mention a season"、"has not stated a season length"、"No listing gives an end date for a season";updates.md 与 entities.json 两条活动实体里的 listing 原文;rewards.md 的 "two listing lines about a season";how-to-play.md / rewards.md 引官方小标题 "Progress & Customization";beginner.md 的 "levels, daily and quests are the progress the description names";rewards.md 的 H2 "Does anything else speed up progress?"。entities.json 与 config-snippet.json 没有需要改的命中,本轮未重新生成。

## 改后自检(`tools/check.py`,12 页全部通过,无告警行)

```
author       author   T45 S54 D150 w 499 fp57 h2  6 ln 5 tb0 im1 OT 5 1.00% 
battle-pass  article  T55 S56 D158 w1252 fp54 h2  8 ln 6 tb4 im2 OT13 1.04% 
beginner     category T51 S54 D149 w 555 fp53 h2  5 ln 5 tb1 im0 OT 6 1.08% 
cases        article  T50 S57 D159 w1232 fp51 h2  8 ln 7 tb4 im2 OT13 1.06% 
game-info    article  T51 S58 D160 w 981 fp53 h2  9 ln 7 tb3 im2 OT16 1.63% 
gamepasses   article  T47 S58 D154 w1115 fp60 h2 11 ln 6 tb2 im3 OT12 1.08% 
how-to-play  article  T51 S57 D160 w1145 fp52 h2  9 ln10 tb2 im2 OT14 1.22% 
index        home     T49 S54 D154 w1013 fp58 h2  9 ln21 tb3 im2 OT11 1.09% 
rewards      article  T52 S55 D152 w1145 fp56 h2  8 ln 6 tb4 im2 OT12 1.05% 
robux        category T49 S56 D156 w 593 fp63 h2  5 ln 6 tb1 im0 OT 7 1.18% 
shop         article  T44 S58 D160 w1384 fp57 h2  8 ln12 tb5 im2 OT14 1.01% 
updates      article  T52 S55 D158 w1423 fp53 h2  9 ln 6 tb2 im2 OT15 1.05% 
```

`numcheck.py`:0 条缺失;`quotecheck.py`:0 条不匹配。封面仍是 12 页 12 张不同的图。

## 用仓里 `hub/mdlite.py` 对 12 个最终文件的只读解析(`python3 -B`,未写 `__pycache__`;解析后仓 `git status --short` 0 行)

```
author.md fm keys 17 blocks {'h': 7, 'p': 9, 'img': 1} html bytes 3120 sha1 1718ea7ba5
battle-pass.md fm keys 20 blocks {'h': 9, 'p': 17, 'table': 4, 'img': 2, 'ol': 1, 'ul': 2} html bytes 8831 sha1 ab300db8db
beginner.md fm keys 19 blocks {'h': 10, 'p': 11, 'table': 1} html bytes 3882 sha1 eea9b1efa4
cases.md fm keys 20 blocks {'h': 9, 'p': 16, 'table': 4, 'img': 2, 'ul': 3} html bytes 9393 sha1 8a3d9c9976
game-info.md fm keys 20 blocks {'h': 10, 'p': 16, 'table': 3, 'img': 2, 'ul': 1} html bytes 7194 sha1 e5f089a4b9
gamepasses.md fm keys 20 blocks {'h': 12, 'p': 15, 'table': 2, 'img': 3, 'ul': 2} html bytes 7350 sha1 bfc5bd6cb0
how-to-play.md fm keys 20 blocks {'h': 10, 'p': 17, 'table': 2, 'img': 2, 'ul': 3, 'ol': 1} html bytes 8053 sha1 6c17ea6f3a
index.md fm keys 20 blocks {'h': 10, 'p': 12, 'ul': 2, 'img': 2, 'table': 3} html bytes 8267 sha1 08fe1f0670
rewards.md fm keys 20 blocks {'h': 9, 'p': 17, 'table': 4, 'img': 2, 'ul': 2} html bytes 8133 sha1 722146d870
robux.md fm keys 19 blocks {'h': 10, 'p': 10, 'table': 1} html bytes 4109 sha1 0bba846b31
shop.md fm keys 20 blocks {'h': 9, 'p': 19, 'table': 5, 'img': 2, 'ul': 2} html bytes 11219 sha1 eb9f19f947
updates.md fm keys 20 blocks {'h': 10, 'p': 18, 'table': 2, 'ul': 4, 'img': 2} html bytes 9946 sha1 98c515db47
parsed 12 files; distinct covers 12
```

每个文件:`split_frontmatter` 得到的 frontmatter 键数、`parse` 得到的块类型计数、`render` 输出字节数、文件 sha1 前 10 位(供复验时确认是同一版本)。断言项:slug / title 存在、tldr 与 images 是列表、draft 为 false、`_images.json` 的 pages 映射等于 images[0]、frontmatter 引用的实体键都在 entities.json 里、渲染结果恰好 1 个 H1。
