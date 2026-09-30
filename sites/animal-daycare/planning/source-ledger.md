# 页面素材来源记录表

规则：每页至少 1 个 S 或 A 级来源才开写；只有 B/C 的页 draft。

来源缩写：
- G = https://games.roblox.com/v1/games?universeIds=10701628624（S）
- V = https://games.roblox.com/v1/games/votes?universeIds=10701628624（S）
- GR = https://groups.roblox.com/v1/groups/235484791（S）
- GG = https://games.roblox.com/v2/groups/235484791/games?accessFilter=Public&limit=50（S）
- U = https://users.roblox.com/v1/users/7164437913（S）
- BD = https://badges.roblox.com/v1/universes/10701628624/badges?limit=100（S）
- GP = https://apis.roblox.com/game-passes/v1/universes/10701628624/game-passes?passView=Full&pageSize=100（S，返回 0 个）
- DP = https://apis.roblox.com/developer-products/v2/universes/10701628624/developerproducts?limit=100（S）
- PL = https://develop.roblox.com/v1/universes/10701628624/places?limit=50（S）
- AG = https://apis.roblox.com/experience-guidelines-api/experience-guidelines/get-age-recommendation（S，POST {"universeId":"10701628624"}）
- TH = https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=10701628624&size=768x432&format=Png&countPerUniverse=10（S）
- IC = https://thumbnails.roblox.com/v1/games/icons?universeIds=10701628624&size=512x512&format=Png（S）
- Y1 = https://www.youtube.com/watch?v=B1IY_XEyedU（B，Zac Worthy 新手视频自动字幕，1,510 播放）
- Y2/Y3/Y4 = YouTube 标题与描述（B，仅标题）
- C1 = animaldaycare.wiki；C2 = animal-daycare.wiki（C，只看结构，不作事实、不链接）

| 页 | 主来源 | 辅助 | 最高级 | 素材状态 | 图片 |
|---|---|---|---|---|---|
| index | G、BD、DP | V、GR、AG | S | 充足 | th1（封面）、th3 |
| guides（栏目） | G | BD、DP | S | 充足 | th2 |
| how-to-play | G（描述原文） | DP（道具描述）、BD、PL | S | 充足（只写官方描述与商品描述里有的；具体操作与威胁清单未获取 → 放 draft 页） | th2、th3 |
| badges | BD | G | S | 充足 | th3 |
| shop | DP | GP（0 个） | S | 名称/价格/描述充足；职业名、Boss、Starter Pack 内容未获取 → 正文写「官方没说明」 | th1、icon |
| game-info | G、GR、GG、U、V、AG、PL | GP | S | 充足；官方社媒/Discord 未获取 | icon、th1 |
| author | — | — | — | 编辑方针页 | th2 |
| impostors | Y1 | G（描述框架）、BD（Imposter Hunter） | S 仅框架 / 具体特征 B | **具体特征只有 B → draft** | th2 |
| night-events | Y1 | G、DP（Water Gun、Coffee、Toy Hammer 描述）、BD | S 仅框架 / 具体威胁 B | **具体威胁只有 B → draft** | th3 |
| codes | — | — | — | **无任何来源 → 不建** | — |

## 悬而未决 / 来源冲突（页面照实写两边，不挑边）

| 项 | 说法 A | 说法 B | 处理 |
|---|---|---|---|
| Water Gun 容量 | 名称：20 Bullets（DP） | 描述：15 shots（DP） | shop 页两者并列 |
| 2/3 星 Level 2 解锁描述 | 名称：Level 2（DP） | 描述：third level（DP） | shop 页注明描述不一致，按名称列表 |
| 鬼怎么赶 | 官方 Water Gun：scare away ghosts（DP，S） | Y1：只有相机闪光能吓走鬼（与玩具锤对比）（B） | night-events（draft）并列；how-to-play 只写 S |
| sanity vs Calm | Y1 用 sanity（B） | 官方用 Calm（DP Lunchbox、G 描述）（S） | 已发布页只用 Calm；不写二者等同 |
| night vs shift | 徽章 1-2 用 night | 徽章 3-4 用 shifts | 逐字照抄，不写等同 |
