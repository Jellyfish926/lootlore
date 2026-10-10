# One Tap fix3:线上验收后的封面与来源链接修复(2026-10-10)

起因:独立线上验收(2026-10-10)对 /one-tap/ 报两项。① 通行证图标(700x700,圆盘 + 像素文字)被框架按 16:9 居中裁切,hub 的栏目卡、robux 栏目页的文章卡、gamepasses 页首封面上的图内文字被切断并放大发糊;② game-info 与 how-to-play 来源列表里的 experience-guidelines 接口链接用 GET 打开是 404(该接口只接受 POST)。

本次只改图片分配与一条来源链接,正文事实句没有改动;框架代码没有改动。

## 1. 封面分配(改后)

| 页 | 封面 key(改前 → 改后) | 是否 16:9 | 该图被几页用作封面 |
|---|---|---|---|
| index | th1 → th1(未变) | 是 | 1 |
| how-to-play | th2 → th2(未变) | 是 | 2 |
| cases | th3 → th3(未变) | 是 | 2 |
| shop | th4 → th4(未变) | 是 | 2 |
| updates | ev-summer → ev-summer(未变) | 是 | 1 |
| rewards | ev-valentines → ev-valentines(未变) | 是 | 2 |
| battle-pass | ev-update → ev-update(未变) | 是 | 2 |
| gamepasses | pass-2x-case-luck → th2 | 是 | 2 |
| game-info | icon → th3 | 是 | 2 |
| beginner | pass-2x-level-xp → ev-valentines | 是 | 2 |
| robux | pass-2x-money → th4 | 是 | 2 |
| author | pass-double-voting-value → ev-update | 是 | 2 |

框架自动页 /one-tap/all/ 取 `default`(th1),不在 `pages` 映射里。og:image 去重后 7 张(13 页)。

## 2. 逐字改动(content/one-tap/en/)

| 文件 | 改前 | 改后 |
|---|---|---|
| author.md | `images: ["pass-double-voting-value", "icon"]` | `images: ["ev-update", "icon"]` |
| beginner.md | `images: ["pass-2x-level-xp"]` | `images: ["ev-valentines"]` |
| robux.md | `images: ["pass-2x-money"]` | `images: ["th4"]` |
| game-info.md | `images: ["icon", "th4"]` | `images: ["th3", "icon", "th4"]` |
| gamepasses.md | `images: ["pass-2x-case-luck", "pass-2x-money", "pass-double-voting-value"]` | `images: ["th2"]` |
| cases.md | `images: ["th3", "pass-2x-case-luck", "ev-update"]` | `images: ["th3", "ev-update"]` |
| rewards.md | `images: ["ev-valentines", "pass-2x-level-xp"]` | `images: ["ev-valentines"]` |
| shop.md | `images: ["th4", "th3", "pass-2x-money"]` | `images: ["th4", "th3"]` |
| gamepasses.md | `![Game pass icon: a dark grey disc with pixel lettering, 2x Money in green and Grants double money from kills. in yellow](pass-2x-money "Official icon of the 2x Money pass, 299 Robux")` | (整行删除,连同其后的空行) |
| gamepasses.md | `![Game pass icon: a dark grey disc with pixel lettering, 2x Case Luck in green and Grants more luck when opening cases in yellow, the last line clipped by the round frame](pass-2x-case-luck "Official icon of the 2x Case Luck pass, 499 Robux")` | (整行删除,连同其后的空行) |
| gamepasses.md | `![Game pass icon: a dark grey disc with pixel lettering, 2x Votes in magenta and Your votes will count twice. in yellow](pass-double-voting-value "Official icon of the Double Voting Value pass, 79 Robux")` | (整行删除,连同其后的空行) |
| cases.md | `![Game pass icon: a dark grey disc with pixel lettering, 2x Case Luck in green and Grants more luck when opening cases in yellow, the last line clipped by the round frame](pass-2x-case-luck "Official icon of the 2x Case Luck pass, 499 Robux")` | (整行删除,连同其后的空行) |
| rewards.md | `![Game pass icon: a dark grey disc with yellow pixel lettering that reads 2x XP, Grants double XP.](pass-2x-level-xp "Official icon of the 2x Level XP pass, 149 Robux")` | (整行删除,连同其后的空行) |
| shop.md | `![Game pass icon: a dark grey disc with pixel lettering, 2x Money in green and Grants double money from kills. in yellow](pass-2x-money "Official icon of the 2x Money pass, 299 Robux")` | (整行删除,连同其后的空行) |

被删的 6 行都是独占一行的通行证图标 figure。四张图标上的文字仍在 gamepasses 页(Words on the official icon 列)与 hub 速查表里逐字转录;cases、rewards 正文各自引用的那一句(2x Case Luck、2x XP)也没有动;shop 页原本就没有引用 2x Money 图标上的那句,撤掉的只是配图。正文里没有任何一句指着这些图说话。

## 3. `content/one-tap/_images.json`

- `pages`:gamepasses → th2、game-info → th3、beginner → ev-valentines、robux → th4、author → ev-update。
- `_note`:原「12 页封面一页一张、无重复」「方形图进 16:9 封面位由框架居中裁切…」两段换成现在的分配与原因。
- `shots` 一条没动:4 张通行证图标留在池里作取证记录,但不再放进任何页面;方形游戏图标 icon 只在 index、game-info、author 正文里各出现一次(图上没有文字)。没有引入新的图片来源。

## 4. `data/one-tap/entities.json`(实体 one-tap)

| 字段 | 改前 | 改后 |
|---|---|---|
| source_urls[3] | `https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation` | `https://create.roblox.com/docs/production/promotion/content-maturity` |
| source_urls_note(新增,不渲染) | (无) | `The maturity label itself was read from Roblox's experience-guidelines API (see key_notes_source and key_notes_repro). That endpoint only answers POST requests and returns 404 to a plain GET, so it is not listed as a clickable source; the list links Roblox's Creator Hub page on content maturity labels instead (GET 200, read 2026-10-10).` |

原因:框架的来源列表把 `source_urls` 的每一条都渲染成超链接,没有纯文字来源的写法。替换页是 Roblox Creator Hub 的「Content maturity and compliance」,2026-10-10 GET 返回 200、无跳转,正文解释 Minimal / Mild / Moderate / Restricted 四档标签。分级取值的真实出处没有变:`key_notes_source` 与 `key_notes_repro` 仍记着 POST 接口与复现方法(这两个字段不渲染);game-info 与 index 正文里「来自 experience-guidelines API 的 POST 请求」两句没有动。

