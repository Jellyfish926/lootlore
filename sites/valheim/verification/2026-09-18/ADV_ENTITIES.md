# entities.json 独立对抗验证报告

- 验证方法论：见 anthropic-skills:adversarial-verify。本次验证与产出方（valheim.weirdgloop.org api.php wikitext）使用不同取证路径：优先 valheim.fandom.com api.php wikitext；fandom 未收录的 1.0 Deep North 内容改用 valheim.weirdgloop.org 渲染后 HTML 页面（同站不同路径，已标注）。
- 范围：A 级（8 boss 全部非 null 字段 + 4 船 + portal/portal-stone recipe）全验；B 级用 `random.seed(20260918)` 从 29 个非 A 级实体中抽 30%（round(29*0.3)=9）：`death, workbench, plains, eternal-pyre, black-forest, malicious-blood, mead-ketill, smelter, shield-generator`。
- **触发全量**：抽样验证中发现 `black-forest.enemies` 缺失 `Rancid Remains`（REFUTED），按协议“验出 1 条 REFUTED 就转全量”，随即将 B 级范围从 30% 抽样扩大到全部 29 个实体（100%）。
- 取证日期：均为 2026-09-18。

## 统计行

| 类别 | 总条目数 | CONFIRMED | REFUTED | UNVERIFIED |
|---|---|---|---|---|
| A 级（8 boss 全部非 null 字段 + 4 船 + 2 portal 的 recipe） | 约 95 个字段点 | 约 93 | 0 | 2（`queen.summon`/`queen.unlocks_en` 为空值，wiki 原文亦未给出对应数据，标记为「原始数据本身缺失，无法外部验证」） |
| B 级（29 个非 boss/boat/portal 实体，100% 覆盖，从 30% 抽样升级而来） | 29 个实体 / 约 60 个字段点 | 约 52 | 5（enemies/key_resources 列表不完整） | 3（Deep North 相关字段因 fandom 页面本身标注 Work-in-progress，二次源信息不全） |
| **合计** | — | **约 145** | **5** | **5** |

结论：核心数值字段（HP、HP 分阶段、summon 数量、伤害类型、抗性、掉落数量、天赋祝福、船/传送门/工作站 recipe 数量）**全部 CONFIRMED，零反例**。REFUTED 仅出现在部分 biome 的 `enemies`（怪物列表）字段——该字段被产出方精简/不完整，与 fandom 当前 infobox 的 hostile 生物列表相比缺少若干条目，不是数值错误，但会导致网站信息框展示的“该生物群系怪物列表”不完整。

---

## REFUTED 明细（全部 5 条）

| 实体.字段 | 数据值 | 验证路径 URL | 结果 | 证据原文 | 取证日期 |
|---|---|---|---|---|---|
| black-forest.enemies | `Greydwarf, Greydwarf brute, Greydwarf shaman, Troll, Skeleton, Bear, Ghost`（7项，缺 Rancid Remains） | https://valheim.fandom.com/api.php?action=parse&page=Black_Forest&prop=wikitext&format=json | REFUTED | infobox: `hostile = * Bear * Ghost * Greydwarf * Greydwarf brute * Greydwarf shaman * Rancid Remains * Skeleton * Troll`（8项，多出 Rancid Remains） | 2026-09-18 |
| mountains.enemies | `Wolf, Drake, Stone Golem, Fenring (at night), Cultist (Frost Cave), Ulv (Frost Cave)`（6项，缺 Draugr/Skeleton/Bat） | https://valheim.fandom.com/api.php?action=parse&page=Mountain&prop=wikitext&format=json | REFUTED | infobox: `hostile = Wolf, Drake, Stone Golem (Mountain/Frost Caves), Fenring (At nighttime), Draugr (Mountain towers), Skeleton (Mountain towers/Cabins), Bat (Frost Caves), Ulv (Frost Caves), Cultist (Frost Caves)`（9项，多出 Draugr、Skeleton、Bat） | 2026-09-18 |
| ashlands.enemies | `Asksvin, Charred Marksman, Charred Twitcher, Charred Warlock, Charred Warrior, Morgen, Bonemaw Serpent`（7项，缺 Fallen Valkyrie/Lava Blob/Volture/Skugg） | https://valheim.fandom.com/api.php?action=parse&page=Ashlands&prop=wikitext&format=json | REFUTED | infobox: `hostile = Asksvin, Bonemaw Serpent, Charred Marksman, Charred Twitcher, Charred Warlock, Charred Warrior, Fallen Valkyrie, Lava Blob, Morgen, Volture, Skugg`（11项，多出 Fallen Valkyrie、Lava Blob、Volture、Skugg） | 2026-09-18 |
| mistlands.enemies | `Tick, Seeker, Seeker Soldier, Gjall`（4项，缺 Seeker Brood） | https://valheim.fandom.com/api.php?action=parse&page=Mistlands&prop=wikitext&format=json | REFUTED | infobox: `hostile = Tick, Seeker, Seeker Brood, Seeker Soldier, Gjall`（5项，多出 Seeker Brood） | 2026-09-18 |
| mistlands.key_resources | `Yggdrasil wood, Black marble, Black core, Sap, Royal jelly, Soft tissue`（6项，缺 Dvergr extractor/Sealbreaker fragment/Blue jute） | https://valheim.fandom.com/api.php?action=parse&page=Mistlands&prop=wikitext&format=json | REFUTED | infobox: `unique = Yggdrasil wood, Black marble, Black cores, Dvergr extractors, Sap, Sealbreaker fragments, Royal jelly, Soft tissue, Blue jute`（9项，多出 Dvergr extractors、Sealbreaker fragments、Blue jute） | 2026-09-18 |

说明：以上均为“列表不完整”，不是具体数值写错；受影响的是信息框里渲染的“怪物/资源列表”少列了几项，不影响 HP、伤害、recipe 等核心数字类字段。

---

## UNVERIFIED 明细（全部 5 条）

| 实体.字段 | 数据值 | 验证路径 URL | 结果 | 原因 | 取证日期 |
|---|---|---|---|---|---|
| queen.summon | `[]`（空数组） | https://valheim.fandom.com/api.php?action=parse&page=The_Queen&prop=wikitext&format=json | UNVERIFIED | fandom 正文明确写"her first fight requires no sacrifice"，与产出方 unverified_fields 说明一致，但 wiki 未给出结构化的"summon 物品列表"字段本身（本来就没有），无法用一个具体数字/名称去证实或证伪一个"空"字段，只能确认"无矛盾" | 2026-09-18 |
| queen.unlocks_en | `null` | https://valheim.fandom.com/api.php?action=parse&page=The_Queen&prop=wikitext&format=json | UNVERIFIED | fandom 正文只提到"解锁 Herbs of the Hidden Hills 商人道具"和"解锁 Seeker 夜间生成"，未见类似其他 boss 页面的统一"unlocks"字段表述，产出方标 null 属于保守处理，本方无法独立判定该 null 是否应替换为具体文本 | 2026-09-18 |
| deep-north.enemies（额外项 Greydwarf/Eyeless One/Hexen） | `Greydwarf (Deep North), Moose, Barka, Elaking, Eyeless One, Hexen, Krigen, Gammeltroll`（8项） | https://valheim.fandom.com/api.php?action=parse&page=Deep_North&prop=wikitext&format=json | UNVERIFIED | fandom Deep North 页面本身标注 `{{Unfinished}}`，infobox hostile 只列 5 项（Barka, Elaking, Gammeltroll, Krigen, Moose），缺 Greydwarf/Eyeless One/Hexen；但因 fandom 源页自认不完整，且协议未提供第三方独立来源核对 1.0 内容，无法判定产出方多出的 3 项是否为真（既不能 CONFIRM 也不能 REFUTE） | 2026-09-18 |
| deep-north.key_resources（Petrified Tissue / Luminous Larva） | `Ice, Timberwood, Petrified Tissue, Frostcore, Luminous Larva`（5项） | https://valheim.fandom.com/api.php?action=parse&page=Deep_North&prop=wikitext&format=json | UNVERIFIED | fandom Deep North 页面 unique 字段仅列 `Ice, Kale Seeds, Seal Blubber, Snowball, Timberwood`，与产出方列出的 Petrified Tissue、Frostcore、Luminous Larva 几乎不重叠；因源页标注 Work-in-progress 且未收录完整，无法判定孰是孰非，仅能确认双方分类口径不同 | 2026-09-18 |
| kall.forsaken_power | `null` | https://valheim.weirdgloop.org/w/Kall_Fimbulbringer（同站不同路径，fandom 未收录该页） | UNVERIFIED（倾向 CONFIRMED，但严格按协议单列） | weirdgloop 渲染页确实标注"This article is a work in progress"且无 Forsaken Power/祭坛章节，与产出方 unverified_fields 说明一致，null 值与页面现状相符；但因该词条内容本身可能随游戏更新随时补全，暂不升级为 CONFIRMED，仅记为"与当前页面状态一致的未验证项" | 2026-09-18 |

---

## A 级 CONFIRMED 摘要（全部 8 boss + 4 船 + portal/portal-stone，逐项已核）

以下每行代表已交叉核实并 **CONFIRMED** 的字段组（因字段点数量大，按实体汇总，未逐字段单独列行；核心数值/名称/recipe 与产出方数据 100% 一致，未发现任何数值或数量错误）：

| 实体 | 已验证字段 | 验证路径 URL | 结果 | 证据摘录 | 取证日期 |
|---|---|---|---|---|---|
| Eikthyr | hp=500, damage_types=[Pierce,Lightning], immune=[Stagger], weak/resistant/very_resistant=[], drops=[Eikthyr trophy x1, Hard antler x3], summon=[Deer trophy x2] | https://valheim.fandom.com/api.php?action=parse&page=Eikthyr&prop=wikitext&format=json | CONFIRMED | `health 0star = 500`；`damage 0star = Antler: Pierce; Charge/Stomp: Lightning`；`immune = Stagger`；`drops = Eikthyr trophy, Hard antler x3`；`summon = Deer trophy x2` | 2026-09-18 |
| The Elder | hp=2500, damage_types=[Pierce,Blunt], weak=[Fire], immune=[Poison,Spirit,Stagger], drops=[trophy x1, Swamp key "1 per player"], summon=[Ancient seed x3] | https://valheim.fandom.com/api.php?action=parse&page=The_Elder&prop=wikitext&format=json | CONFIRMED | `health 0star = 2500`；`veryweak = Fire`；`immune = Poison, Spirit, Stagger`；drop table: `Swamp key｜0star=1 per player` | 2026-09-18 |
| Bonemass | hp=5000, damage_types=[Poison,Blunt], weak=[Blunt,Frost], resistant=[Slash], very_resistant=[Fire,Pierce], immune=[Poison,Stagger], drops=[trophy x1, Wishbone "1 per player"], summon=[Withered bone x10] | https://valheim.fandom.com/api.php?action=parse&page=Bonemass&prop=wikitext&format=json | CONFIRMED | `health 0star = 5000`；`weak=Blunt, Frost`；`resistant=Slash`；`veryresistant=Fire, Pierce`；drop table `Wishbone｜0star=1 per player` | 2026-09-18 |
| Moder | hp=7500, damage_types=[Pierce,Slash,Frost], weak=[Fire], immune=[Frost,Spirit,Stagger], drops=[Dragon tear x10, trophy x1], summon=[Dragon egg x3] | https://valheim.fandom.com/api.php?action=parse&page=Moder&prop=wikitext&format=json | CONFIRMED | `health 0star = 7500`；damage: Bite=Pierce, Claw=Slash, Spit/Cold breath=Frost；drop table `Dragon tear｜0star=10` | 2026-09-18 |
| Yagluth | hp=10000, damage_types=[Fire,Lightning,Blunt], resistant=[Fire], very_resistant=[Pierce], immune=[Poison,Stagger], drops=[Torn spirit x3, trophy x1], summon=[Fuling totem x5] | https://valheim.fandom.com/api.php?action=parse&page=Yagluth&prop=wikitext&format=json | CONFIRMED | `health 0star = 10,000`；`resistant=Fire`；`veryresistant=Pierce`；drop table `Torn spirit｜0star=3` | 2026-09-18 |
| The Queen | hp=12500, damage_types=[Slash,Pierce,Poison,Blunt], resistant=[Pierce], immune=[Spirit], drops=[Majestic carapace x5, trophy x1], forsaken_power 文本 | https://valheim.fandom.com/api.php?action=parse&page=The_Queen&prop=wikitext&format=json | CONFIRMED | `health 0star = 12,500`；`resistant=Pierce`；`immune=Spirit`；drop table `Majestic carapace｜0star=5`；Forsaken Power 段落文字与产出方 effect_en 逐句一致 | 2026-09-18 |
| Fader | hp=25000, damage_types=[Fire,Spirit,Pierce], resistant=[Pierce], immune=[Fire,Spirit], drops=[Fader relic x5, trophy "100%"], summon=[Bell x3], forsaken_power/unlocks 文本 | https://valheim.fandom.com/api.php?action=parse&page=Fader&prop=wikitext&format=json | CONFIRMED | `health 0star = 25000`；`resistant=Pierce`；`immune=Fire, Spirit`；drop table `Fader trophy｜0star=100%`；"placing three Bells"；Forsaken Power 与"Fiery Spice Powder... 200 Coins"逐句一致 | 2026-09-18 |
| Kall Fimbulbringer | hp=null, hp_phases=[10000,7000,30000], damage_types 6项, resistant=[Pierce,Fire,Frost,Lightning], immune=[Spirit], drops=[Sacrificial Blood x1, Crown Jewel x1], summon=[Malicious Blood x3], unlocks_en | https://valheim.weirdgloop.org/w/Kall_Fimbulbringer（同站不同路径，fandom 未收录） | CONFIRMED | `Health 0★ = 10000 + 7000 + 30000`；`Resistant to = Pierce, Fire, Frost, Lightning`；`Immune to = Spirit`；drops表 `Sacrificial Blood 1, Crown Jewel 1`；"Three Malicious Blood are required"；"unlocks Seasoning of the Gourd... for 220 Coins" | 2026-09-18 |
| Raft | recipe=[Wood x20, Leather scraps x6, Resin x6], hp=300 | https://valheim.fandom.com/api.php?action=parse&page=Raft&prop=wikitext&format=json | CONFIRMED | `materials = Wood x20, Leather scraps x6, Resin x6`；`durability = 300` | 2026-09-18 |
| Karve | recipe=[Finewood x30, Deer hide x10, Resin x20, Bronze nails x80], hp=500, cargo_slots=4 | https://valheim.fandom.com/api.php?action=parse&page=Karve&prop=wikitext&format=json | CONFIRMED | `materials = Finewood x30, Deer hide x10, Resin x20, Bronze nails x80`；`durability = 500`；`storage = 2x2`（=4 格）| 2026-09-18 |
| Longship | recipe=[Iron nails x100, Deer hide x10, Finewood x40, Ancient bark x40], hp=1000, cargo_slots=18 | https://valheim.fandom.com/api.php?action=parse&page=Longship&prop=wikitext&format=json | CONFIRMED | `materials = Iron nails x100, Deer hide x10, Finewood x40, Ancient bark x40`；`durability = 1,000`；正文"18 storage slots" | 2026-09-18 |
| Drakkar | recipe=[Iron nails x100, Ceramic plate x30, Finewood x50, Yggdrasil wood x25], hp=3000, cargo_slots=32 | https://valheim.fandom.com/api.php?action=parse&page=Drakkar&prop=wikitext&format=json | CONFIRMED | `materials = Iron nails x100, Ceramic plate x30, Finewood x50, Yggdrasil wood x25`；`durability = 3000`；正文"storage space has 32 item slots" | 2026-09-18 |
| Portal | recipe=[Greydwarf eye x10, Finewood x20, Surtling core x2] | https://valheim.fandom.com/api.php?action=parse&page=Portal&prop=wikitext&format=json | CONFIRMED | `materials = Greydwarf eye x10, Finewood x20, Surtling core x2` | 2026-09-18 |
| Portal – Stone | recipe=[Greydwarf eye x10, Grausten x30, Molten core x2] | https://valheim.fandom.com/api.php?action=parse&page=Portal%20stone&prop=wikitext&format=json | CONFIRMED | `materials = Greydwarf eye x10, Grausten x30, Molten core x2` | 2026-09-18 |

---

## B 级（全量 29 项）CONFIRMED 摘要

除上表 5 条 REFUTED 及 3 条相关 UNVERIFIED 外，其余全部核对一致，含所有 recipe / 数量字段：

| 实体 | 已验证关键字段 | 验证路径 URL | 结果 | 证据摘录 | 取证日期 |
|---|---|---|---|---|---|
| Death（mechanic） | skill_loss_pct_default=5, no_skill_drain_minutes=10, corpse_run_seconds=50 | https://valheim.fandom.com/api.php?action=parse&page=Death&prop=wikitext&format=json | CONFIRMED | "lose 5% of their total levels"；"No skill drain... duration 10 minutes"；"Corpse run effect... lasts for 50 seconds" | 2026-09-18 |
| Rested（mechanic） | base_minutes=7, min_comfort_duration=8, max_comfort_normal=22, max_duration_normal=29, max_duration_seasonal=31 | https://valheim.fandom.com/api.php?action=parse&page=Comfort&prop=wikitext&format=json | CONFIRMED | "Minimum duration is 8 minutes (at 1 comfort)... up to 29 minutes... 31 minutes with rare seasonal items"；"max comfort reachable normally is 22... Maypole 23... Yule tree 24" | 2026-09-18 |
| Food（mechanic） | max_food_slots=3 | https://valheim.fandom.com/api.php?action=parse&page=Food&prop=wikitext&format=json | CONFIRMED | "consume up to three different types of food at any given time" | 2026-09-18 |
| Workbench | recipe=[Wood x10] | https://valheim.fandom.com/api.php?action=parse&page=Workbench&prop=wikitext&format=json | CONFIRMED | `materials = Wood x10` | 2026-09-18 |
| Forge | recipe=[Stone x4, Coal x4, Wood x10, Copper x6] | https://valheim.fandom.com/api.php?action=parse&page=Forge&prop=wikitext&format=json | CONFIRMED | `materials = Stone x4, Coal x4, Wood x10, Copper x6` | 2026-09-18 |
| Smelter | recipe=[Stone x20, Surtling core x5] | https://valheim.fandom.com/api.php?action=parse&page=Smelter&prop=wikitext&format=json | CONFIRMED | `materials = Stone x20, Surtling core x5` | 2026-09-18 |
| Charcoal Kiln | recipe=[Stone x20, Surtling core x5] | https://valheim.fandom.com/api.php?action=parse&page=Charcoal_Kiln&prop=wikitext&format=json | CONFIRMED | `materials = Stone x20, Surtling core x5` | 2026-09-18 |
| Mead Ketill | recipe=[Tin x4, Copper x6, Leather scraps x2] | https://valheim.fandom.com/api.php?action=parse&page=Mead_Ketill&prop=wikitext&format=json | CONFIRMED | `materials = Tin x4, Copper x6, Leather scraps x2` | 2026-09-18 |
| Fermenter | recipe=[Finewood x30, Bronze x5, Resin x10] | https://valheim.fandom.com/api.php?action=parse&page=Fermenter&prop=wikitext&format=json | CONFIRMED | `materials = Finewood x30, Bronze x5, Resin x10` | 2026-09-18 |
| Cultivator | recipe=[Corewood x5, Bronze x5] | https://valheim.fandom.com/api.php?action=parse&page=Cultivator&prop=wikitext&format=json | CONFIRMED | `materials 1 = Corewood x5, Bronze x5` | 2026-09-18 |
| Black Forge | recipe=[Black marble x10, Yggdrasil wood x10, Black core x5] | https://valheim.fandom.com/api.php?action=parse&page=Black_Forge&prop=wikitext&format=json | CONFIRMED | `materials = Black marble x10, Yggdrasil wood x10, Black core x5` | 2026-09-18 |
| Frigid Kiln | recipe=[Stone x20, Frostcore x10, Ice x5] | https://valheim.weirdgloop.org/w/Frigid_Kiln（同站不同路径，fandom 未收录） | CONFIRMED | `Crafting Materials: Stone x20, Frostcore x10, Ice x5`；"produces 1 Liquid Frost every 30 seconds by consuming 5 ice"、"hold up to 25 Ice" | 2026-09-18 |
| Frost Foundry | recipe=null；requires_en 描述 | https://valheim.weirdgloop.org/w/Frost_Foundry（同站不同路径） | CONFIRMED | 页面无 materials 字段（与产出方 recipe=null 一致）；"Cast placed at center... consumes 5 Liquid Frosts and takes 50 seconds" | 2026-09-18 |
| Eternal Pyre | recipe=[Stone x10, Fader Relic x1] | https://valheim.weirdgloop.org/w/Eternal_Pyre（同站不同路径，fandom 未收录） | CONFIRMED | `Crafting Materials: Stone x10, Fader Relic x1` | 2026-09-18 |
| Shield Generator | recipe=[Iron x5, Copper x5, Shield core x1] | https://valheim.fandom.com/api.php?action=parse&page=Shield_Generator&prop=wikitext&format=json | CONFIRMED | `materials = Iron x5, Copper x5, Shield core x1` | 2026-09-18 |
| Intricate Key（item） | recipe=[Cast: Intricate Key(qty null), Liquid Frost x5]；crafted_at 文本 | https://valheim.weirdgloop.org/w/Intricate_Key（同站不同路径） | CONFIRMED | "Obtained by using a Cast: Intricate Key in a Frost Foundry, requires 5 Liquid Frost"；"Cast... crafted at Black Forge using: Bloodgold, Mould: Intricate Key" | 2026-09-18 |
| Ember Charge（item） | recipe=[Seal Pelt x2, Embers x1], crafts_quantity=10 | https://valheim.weirdgloop.org/w/Ember_Charge（同站不同路径） | CONFIRMED | `Crafting Materials: Crafts 10, Seal Pelt x2, Embers x1` | 2026-09-18 |
| Bloodgold（item） | recipe=null, weight=14, stack=30 | https://valheim.weirdgloop.org/w/Bloodgold（同站不同路径） | CONFIRMED | `Weight 14, Stack 30`；"obtained by smelting Petrified Tissue in a Blast Furnace" | 2026-09-18 |
| Frostcore（item） | recipe=null, weight=1, stack=20 | https://valheim.weirdgloop.org/w/Frostcore（同站不同路径） | CONFIRMED | `Weight 1, Stack 20`；"Inside the Winding Tunnels found in the Deep North" | 2026-09-18 |
| Malicious Blood（item） | crafted_at_en/usage_en 文本, weight=1, stack=50 | https://valheim.weirdgloop.org/w/Malicious_Blood（同站不同路径，fandom 未收录） | CONFIRMED | "dropped by destroying Malicious Ice found at the center of Jotun Invasions"；"three Malicious Blood are required to open the Aesir Passage"；`Weight 1, Stack 50` | 2026-09-18 |
| Meadows（biome） | boss=eikthyr, enemies含 Draugr(Draugr Village) | https://valheim.fandom.com/api.php?action=parse&page=Meadows&prop=wikitext&format=json | CONFIRMED | `boss = Eikthyr`；Meadows 生物表明确列出 Draugr "In the Meadows, will only spawn in a Draugr Village" | 2026-09-18 |
| Swamp（biome） | boss=bonemass, enemies 9项完全一致 | https://valheim.fandom.com/api.php?action=parse&page=Swamp&prop=wikitext&format=json | CONFIRMED | `hostile = Blob, Oozer, Draugr, Draugr elite, Leech, Skeleton, Surtling, Wraith, Abomination` 与数据完全一致 | 2026-09-18 |
| Plains（biome） | boss=yagluth, enemies 7项完全一致, key_resources=[Flax,Barley,Tar] | https://valheim.fandom.com/api.php?action=parse&page=Plains&prop=wikitext&format=json | CONFIRMED | `hostile = Deathsquito, Fuling, Fuling berserker, Fuling shaman, Growth, Lox, Vile`；`unique = Flax, Barley, Tar` | 2026-09-18 |
| Ocean（biome） | boss=null, enemies=[Serpent,Leviathan] | https://valheim.fandom.com/api.php?action=parse&page=Ocean&prop=wikitext&format=json | CONFIRMED | `boss = `（空）；`hostile = Serpent`，正文另提及 Leviathan | 2026-09-18 |
| Deep North（biome） | boss=kall（经 Kall 词条交叉确认）；key_resources 部分项（Ice, Timberwood）、enemies 部分项（Barka, Elaking, Gammeltroll, Krigen, Moose） | https://valheim.fandom.com/api.php?action=parse&page=Deep_North&prop=wikitext&format=json | 部分 CONFIRMED（其余见上方 UNVERIFIED） | `unique = Ice, Kale Seeds, Seal Blubber, Snowball, Timberwood`；`hostile = Barka, Elaking, Gammeltroll, Krigen, Moose` | 2026-09-18 |

（black-forest / mountains / ashlands / mistlands 的其余字段——recipe 不适用，biome 无 recipe 字段——除上方已列入 REFUTED 的 enemies/key_resources 外，boss 归属、name_en 等均 CONFIRMED，未单独列出。）
