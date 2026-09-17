# Valheim（Steam appid 892970）命题对抗验证表 — BCD 抽样（39 条）

取证日期：均为 2026-09-17。主要取证路径：`https://valheim.fandom.com/api.php?action=parse&page=<Title>&prop=wikitext&format=json`（下表简写为 fandom:<Title>）；官方 Steam 公告 JSON `GetNewsForApp` for appid 892970；`https://valheim.wiki/w/<Title>`（P39 用，因 fandom 尚未收录 1.0 版新增的 Deep North 最终 Boss）。

| 命题 | 验证路径(URL) | 结果 | 证据（原文一句，含数字） | 取证日期 |
|---|---|---|---|---|
| P1 工作台基础材料为 10 木头 | fandom:Workbench | CONFIRMED | infobox materials: `* [[Wood]] x10`（Workbench 唯一建造材料） | 2026-09-17 |
| P2 赤血灵鹿祭坛位于青青草原，附近有 Vegvisir 符石指路 | fandom:Eikthyr | CONFIRMED | "Eikthyr's Forsaken Altar is located in the Meadows. To the left of his Sacrificial Stone is a small glowing Runestone called a Vegvisir" | 2026-09-17 |
| P3 玩家可同时维持三种不同食物效果（三个食物槽） | fandom:Food | CONFIRMED | "A player can consume up to three different types of food at any given time for a combined increase in buff strength." | 2026-09-17 |
| P4 Rested 效果会在角色下线后消失，不持续到新会话 | fandom:Rested | CONFIRMED | "The effect is removed when the player character logs out and does not persist into new game sessions." | 2026-09-17 |
| P5 木传送门与石传送门能力不同（存在可解除限制的高级传送门） | fandom:Portal_stone | CONFIRMED | "Portal – Stone is an improved Portal... It allows players to teleport with items that Wooden portals disallow, such as Ores, Metals, Dragon eggs, Hildir's chests and Mechanical springs." | 2026-09-17 |
| P6 大麦与亚麻只能在平原种植 | fandom:Barley | CONFIRMED | "Barley can only be planted and harvested in the Plains biome, using a Cultivator." | 2026-09-17 |
| P7 龙母祭坛位于雪山，龙蛋重量较大 | fandom:Moder；fandom:Dragon_Egg | CONFIRMED | "Moder's Forsaken Altar is located in the Mountains."；Dragon egg infobox `weight = 200.0`，正文注 "one of the heaviest items overall at 200.0 units" | 2026-09-17 |
| P8 作物不长可能因区域错误、空间不足或缺阳光 | fandom:Cultivator | CONFIRMED | "Crops will not grow if any of the three conditions are met: Wrong biome / Not enough space / Not enough sunlight." | 2026-09-17 |
| P9 冰霜龙母需要三枚龙蛋召唤 | fandom:Creatures（Bosses 表） | CONFIRMED | Boss 表 Moder 行 "Items to Summon: 3 [[Dragon egg]]s"（fandom:Moder 亦载 `summon = [[Dragon egg]] x3`） | 2026-09-17 |
| P10 沼泽开荒需要沼泽钥匙，沉没墓穴是第一批铁的主要来源 | fandom:Swamp | CONFIRMED | "Sprinkling the landscape... are Sunken Crypts, which require a Swamp key to unlock... caved in and blocked by Muddy scrap piles, which can be mined for Scrap iron, Leather scraps, and Withered bones." | 2026-09-17 |
| P11 鹿战利品为随机掉落而非每次必得 | fandom:Deer | CONFIRMED | drop table: "Deer trophy \| 0star=50% \| 1star=50% \| 2star=50%"（50% 掉率，非必掉） | 2026-09-17 |
| P12 给两座门设置相同标签以配对连接 | fandom:Portal | CONFIRMED | "When two portals are built, they will automatically attempt to connect with any other portal with the same case-sensitive tag... a player simply has to step into one portal to teleport to the position of the paired portal."（配对基于相同标签自动完成，原文未描述额外"确认"步骤，但核心配对机制成立） | 2026-09-17 |
| P13 迷雾女王首次挑战无需祭品即可进入战斗 | fandom:The_Queen | CONFIRMED | "Unlike all previous bosses, she must be fought in a dungeon, the Infested Citadel, and her first fight requires no sacrifice." | 2026-09-17 |
| P14 大麦只能在平原区域种植 | fandom:Barley（同 P6） | CONFIRMED | 同 P6 引文 | 2026-09-17 |
| P15 召唤亚格鲁斯需要收集丑地精图腾 | fandom:Creatures（Bosses 表） | CONFIRMED | Boss 表 Yagluth 行 "Items to Summon: 5 [[Fuling totem]]s" | 2026-09-17 |
| P16 Hildir 位于青青草原，涉及服饰与对应支线 | fandom:Hildir | CONFIRMED | "Hildir is a character found in Meadows... At her camp... Hildir sells several unique items"；Trading 表出售 Shawl dress / Beaded dress 等服饰；并有三处迷你 Boss 支线任务地点（Smouldering Tombs / Howling Caverns / Sealed Tower） | 2026-09-17 |
| P17 部分蔬菜可再种植获得种子（如芜菁留种） | fandom:Turnip | CONFIRMED | "3 [[Turnip seeds]] can be obtained by planting and growing a 'Seed-turnip' using the Cultivator." | 2026-09-17 |
| P18 熔炉需建在工作台附近才能解锁建造 | fandom:Smelter | CONFIRMED | "It will be unlocked when the player acquires a Surtling core. It must be constructed near a Workbench." | 2026-09-17 |
| P19 黑核与 Sealbreaker fragment 主要产自被侵染的矿洞 | fandom:Black_Core；fandom:Sealbreaker_Fragment | CONFIRMED | "Black cores are resources obtained from Infested Mines..."；"Sealbreaker fragments are resources obtained from Infested Mines in the Mistlands that are used to build the Sealbreaker." | 2026-09-17 |
| P20 沼泽女巫位于沼泽，提供宴席与酿造相关材料 | fandom:The_Bog_Witch | CONFIRMED | "The Bog Witch is a Greydwarf trader found in the Swamp biome... Her spices and serving tray are required to prepare and eat a Feast."；交易表内多项材料标注 "Required for [Berserkir mead] / [Draught of Vananidir]" 等酿造用途 | 2026-09-17 |
| P21 树液提取器需要矮人提取器部件，来自矮人组件箱 | fandom:Sap_Extractor | CONFIRMED | "It requires Black metal, Yggdrasil wood and a Dvergr extractor, obtained from Dvergr component crates." | 2026-09-17 |
| P22 格挡效果与装备/受击/角色状态有关；盾反需要合适时机 | fandom:Blocking | CONFIRMED | "Raw damage is reduced... by using only the blocking item's (shield or weapon) armor and resistances"；"Parrying happens when a block action is performed shortly (less than 0.25 seconds) before an attack lands" | 2026-09-17 |
| P23 锻造台建设需要 4 石头、4 煤、10 木头、6 铜 | fandom:Forge | CONFIRMED | infobox materials: `[[Stone]] x4`, `[[Coal]] x4`, `[[Wood]] x10`, `[[Copper]] x6` | 2026-09-17 |
| P24 盾牌近战与最大生命值(最大架势值)相关，翻滚偏体力，法术偏魔力 | fandom:Food | CONFIRMED | "Maximum health is essential for effective shield use due to its link to maximum Stagger capacity... Players preferring to exclusively Dodge attacks will benefit from maximizing their Stamina, while those who favor magic in combat will benefit from maximizing their eitr." | 2026-09-17 |
| P25 沼泽怪物几乎全部敌对，常年下雨（持续 Wet） | fandom:Swamp | CONFIRMED | "every last creature here is hostile to the player. It is always raining in the mire regardless of the weather elsewhere; this means the player will always be Wet when traversing the terrain." | 2026-09-17 |
| P26 平原开荒关键资源含大麦/亚麻，威胁含死亡蚊/丑地精营地 | fandom:Plains | CONFIRMED | unique 资源列 "[[Flax]] / [[Barley]]"；hostile 列含 "[[Deathsquito]]"；structures 列含 "[[Fuling Village]] / [[Fuling Outpost]] / [[Fuling Ruin]]" | 2026-09-17 |
| P27 标准设置下部分矿石/金属/特殊物品会阻止普通传送 | fandom:Portal | CONFIRMED | "Some objects in the game prevent the player from teleporting... All ores and their smelted counterparts cannot be teleported"，并列出 Copper/Iron/Silver/Tin/Dragon egg/Hildir's chests 等清单 | 2026-09-17 |
| P28 Resting 是获得增益的过程，Rested 是离开营地带走的效果，二者不同 | fandom:Resting；fandom:Rested | CONFIRMED | "After 20 uninterrupted seconds with the resting effect, the player will receive the Rested effect."（Rested 页同样载 "Rested is a status effect applied after having the Resting effect for 20 seconds"，二者为不同 status effect） | 2026-09-17 |
| P29 舒适度决定 Rested 持续时间，Rested 改善生命/体力等恢复 | fandom:Rested | CONFIRMED | "The duration of the effect depends on the Comfort level... base duration 7 minutes, with each comfort level adding an additional minute"；效果栏 "Health regen +50%, Stamina regen +100%, Eitr regen +100%" | 2026-09-17 |
| P30 邪骨恶灵对钝击弱、对劈砍有抗性、对火/穿刺高度抗性 | fandom:Bonemass | CONFIRMED | infobox: `weak = Blunt, Frost`；`resistant = Slash`；`veryresistant = Fire, Pierce`；`immune = Poison, Stagger` | 2026-09-17 |
| P31 古树长老需要三颗上古种子召唤 | fandom:Creatures（Bosses 表） | CONFIRMED | Boss 表 The Elder 行 "Items to Summon: 3 [[Ancient seed]]s" | 2026-09-17 |
| P32 室内火源需要通风排烟，处理不当影响火源/角色状态 | fandom:Campfire；fandom:Smoked | CONFIRMED | "If the Campfire is created within an enclosed space, the smoke can build up, causing any players inside to be Smoked and take 2 hp/tick damage. To safely place a Campfire indoors, the interior space must be large enough to let the smoke naturally dissipate or be vented out through a chimney or other holes." | 2026-09-17 |
| P33 击败赤血灵鹿获得硬鹿角，用于制作早期镐具开始采矿 | fandom:Eikthyr | CONFIRMED | "Defeating Eikthyr allows the player to craft the first pickaxe to begin mining ore..."；掉落表 "Hard antler \| 0star=3" | 2026-09-17 |
| P34 银矿石（银锭前置）不能通过普通传送门运输 | fandom:Portal | CONFIRMED | 禁止传送清单含 `{{item link|Silver}}` 与 `{{item link|Silver ore}}` | 2026-09-17 |
| P35 迷雾之地开荒需要驱雾工具，关键资源含黑核/树液/精炼魔力设施 | fandom:Mistlands；fandom:Eitr_Refinery | CONFIRMED | "Wisplights and placeable Wisp torches can be used to clear out the permeating mist, but both require Yagluth to be defeated."；Eitr refinery "used for processing Sap and Soft tissue into Refined eitr"，建造需 `Black core x5` | 2026-09-17 |
| P36 青铜斧需要才能砍伐部分树种（桦树/橡树），涉及精细木材料关系 | fandom:Bronze_Axe；fandom:Birch；fandom:Oak | CONFIRMED | Bronze axe "can be used to chop down... Birch... Oak..."；Birch/Oak 页各载 "A Bronze axe or better is required to damage it." 且 "trees produce Wood and Finewood when destroyed" | 2026-09-17 |
| P37 Karve 配方为 30 精细木、10 鹿皮、20 树脂、80 青铜钉 | fandom:Karve | CONFIRMED | infobox materials: `[[Finewood]] x30`, `[[Deer hide]] x10`, `[[Resin]] x20`, `[[Bronze nails]] x80` | 2026-09-17 |
| P38 Mead ketill 制作材料为 4 锡、6 铜、2 碎皮 | fandom:Mead_Ketill | CONFIRMED | infobox materials: `[[Tin]] x4`, `[[Copper]] x6`, `[[Leather scraps]] x2` | 2026-09-17 |
| P39 Kall Fimbulbringer 分为"锁链阶段、召唤化身阶段与最终强化阶段"三个明确阶段 | Steam 公告 "Valheim 1.0 Has Arrived!"（确认该 Boss 存在）；valheim.wiki/w/Kall_Fimbulbringer（阶段细节，fandom 尚未收录该 1.0 新 Boss） | REFUTED | valheim.wiki 原文："The encounter has three phases. Phase 1: Kall Fimbulbringer attacks the player directly. Phase 2: Kall Fimbulbringer hides inside an invincible block of ice. During this phase, spirits of the previous Bosses are summoned... Phase 3: Kall Fimbulbringer attacks the player directly, with more powerful attacks than phase 1."——阶段确为三段，且 Phase 2 近似"召唤化身"、Phase 3 近似"最终强化"，但 Phase 1 并无任何"锁链"描述（原文仅为直接攻击），命题中"锁链阶段"这一具体命名与一手资料不符 | 2026-09-17 |

## 统计
39 条，CONFIRMED 38 / REFUTED 1 / UNVERIFIED 0
