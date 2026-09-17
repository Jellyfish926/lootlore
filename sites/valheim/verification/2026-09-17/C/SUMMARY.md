# C 组核验总结

核验日期：2026-09-17　核到的当前游戏版本：**1.0.12**（Steam 公告显示 Valheim 1.0 已于 2026-09 正式发布，含深北之境 Deep North 内容；最新公告为 Hotfix 1.0.10 & 1.0.12）。

## 核验结果表

| slug | 页面标题 | 命题数 | 支持 | 冲突 | 不足 | 状态 | 一句话说明 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| first-day | 英灵神殿新手第一天 | 6 | 6 | 0 | 0 | 通过 | 锤子(3木2石)、工作台(10木)等数值与机制均与 fandom 一致 |
| first-base | 英灵神殿基地怎么建 | 4 | 4 | 0 | 0 | 通过 | 排烟/遮蔽/建筑稳定性均为一般性描述，与 Environment、Building_stability 页面一致 |
| crafting | 英灵神殿制作与修理指南 | 5 | 5 | 0 | 0 | 通过 | 熔炉/锻造台材料需求、修理免耗材等描述均与 fandom 一致 |
| bronze | 英灵神殿青铜时代怎么发展 | 8 | 8 | 0 | 0 | 通过 | 木炭窑/熔炉(各20石+5焰灵之核)、锻造台(4石4煤10木6铜)、青铜(2铜+1锡，锻造台制作)全部精确对应 |
| food | 英灵神殿食物怎么搭配 | 4 | 4 | 0 | 0 | 通过 | 三食物槽机制、同类食物刷新规则均与 Food 页面一致 |
| mead | 英灵神殿蜜酒怎么做 | 5 | 5 | 0 | 0 | 通过 | Mead ketill(4锡6铜2碎皮)、需要火源、Fermenter需遮蔽+两天发酵周期，全部精确对应 |
| farming | 英灵神殿种田指南 | 4 | 4 | 0 | 0 | 通过 | 大麦仅限平原、芜菁留种机制、区域/空间/阳光三条件均与 fandom 一致 |
| rested | 英灵神殿休息好了怎么获得 | 5 | 5 | 0 | 0 | 通过 | Resting→20秒→Rested 的机制顺序、舒适度决定持续时间、下线清空效果均与 Resting/Rested/Comfort 页面一致 |
| beginner | 新手入门攻略导航 | 1 | 1 | 0 | 0 | 通过 | 纯导航页，链接与被引用文章标题一致 |
| survival | 生存建设攻略导航 | 1 | 1 | 0 | 0 | 通过 | 纯导航页，链接与被引用文章标题一致 |

**合计：10 页，43 条命题，全部「支持」，0 冲突，0 不足。**

## 正文改动

无。10 篇稿件的所有可核事实命题均在 valheim.fandom.com 找到直接、明确的支持来源，数值（配方材料数量、机制顺序、区域限制等）与原文完全一致，未发现任何冲突或需要删除的断言。唯一改动是按输出规范统一给 frontmatter 追加了：
- `checkedAt` 改为 `"2026-09-17"`
- 新增 `gameVersion: "1.0.12"`

正文本身未做任何文字修改，`verified/` 目录下的 10 份文件即为原文 + 上述 frontmatter 更新。

## 来源打架 / 未获取清单

- 无来源矛盾（fandom 各相关页面之间、以及与正文描述之间均一致）。
- 无「未获取」来源：sources.json 中列出的 fandom 页面直接访问返回 403（反爬），但通过 `https://valheim.fandom.com/api.php?action=parse&page=<Title>&prop=wikitext&format=json` 均成功获取（HTTP 200），已在各 ledger 中以该方式记录访问状态。
- 官方 FAQ（valheimgame.com/faq/）与 mead 页面引用的第三方站点 gamers.wiki 均直接可访问（HTTP 200），mead 页面已明确 gamers.wiki 仅作交叉验证，主依据为 fandom。
- Comfort 页面注明"This article is not fully updated to match the Valheim 1.0 Deep North release"，但其舒适度→持续时间的机制方向与 Rested 页面的公式（BaseDuration 7分钟 + ComfortLevel）互相印证，未发现冲突，且本组两篇涉及的正文（rested.md）未引用具体分钟数，不受此提示影响。

## 补充说明

- Deep North / 1.0 版本背景核实：Steam 官方公告（appid 892970）显示 Valheim 1.0（含 Deep North 深北之境）已于 2026 年 9 月正式发布并出过 1.0.10、1.0.12 两个 Hotfix，本组分到的 10 页内容未对 1.0/Deep North 发布状态做出任何断言，不涉及冲突。
- 青铜配方特别核实：正文强调"青铜在锻造台制作，不是直接把两种矿石放进普通熔炉"，与 fandom Bronze 页面完全吻合（"crafted by processing two Copper and one Tin at the Forge"；普通熔炉仅能通过熔炼稀有的 Scrap bronze 间接获得青铜）。
- 焰灵之核"同时被生产设施和交通建设消耗"的表述，核实焰灵之核的 Usage/Building 列表确实同时包含 Charcoal kiln、Smelter 与 Portal（传送门），断言成立。
