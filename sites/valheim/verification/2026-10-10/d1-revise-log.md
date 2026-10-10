# D1 收尾日志（Valheim；2026-10-10）

只改三处小问题，中英成对；抗性档位、召唤方式等事实不重核、不改口径（Iron Gate 官方公告与社区 wiki 两种口径页内原样分开标注）。

| 文件:行 | 条目 | 原句 → 新句 |
|---|---|---|
| content/valheim/en/bosses.md:12 | ① 要点框语病 | though Yagluth's has a very small chance of spawning and Kall's is listed on valheim.wiki alone; → though the Vegvisir for Yagluth has a very small chance of spawning and the one for Kall is listed on valheim.wiki alone; |
| content/valheim/en/queen.md:26 | ③ 括注里的事实挪进正文 | the entry requirements are described in the [Queen entry](https://valheim.fandom.com/wiki/The_Queen). → the entry requirements are described in the [Queen entry](https://valheim.fandom.com/wiki/The_Queen). Per the community wiki, the Sealbreaker is an entry key that is not consumed, the first fight needs no offering, and 3 Seeker soldier trophy summon her again after her first defeat. |
| content/valheim/zh/queen.md:26 | ③ 括注里的事实挪进正文 | 相关进入方式见[女王资料](https://valheim.fandom.com/wiki/The_Queen)。 → 相关进入方式见[女王资料](https://valheim.fandom.com/wiki/The_Queen)。按社区 wiki，破封者是进入用的钥匙、不消耗，首战不需要祭品，首次击败后献上 3 个 Seeker soldier 战利品可再次召唤。 |
| content/valheim/en/queen.md:18 | frontmatter updated（reviewed 不动） | updated: "2026-09-17" → updated: "2026-10-10" |
| content/valheim/zh/queen.md:18 | frontmatter updated（reviewed 不动） | updated: "2026-09-17" → updated: "2026-10-10" |

| data/valheim/entities.json 实体 | 字段 | 原值 → 新值 | 说明 |
|---|---|---|---|
| bonemass | resistant | ["Slash", "Fire (very resistant)", "Pierce (very resistant)"] → ["Slash"] | ② 被括注标成 very resistant 的项只留在 very_resistant 一行；very_resistant 字段未动 |
| bonemass | resistant_zh | ["斩击", "火焰（抗性很高）", "穿刺（抗性很高）"] → ["斩击"] | ② 被括注标成 very resistant 的项只留在 very_resistant 一行；very_resistant 字段未动 |
| yagluth | resistant | ["Fire", "Pierce (very resistant)"] → ["Fire"] | ② 被括注标成 very resistant 的项只留在 very_resistant 一行；very_resistant 字段未动 |
| yagluth | resistant_zh | ["火焰", "穿刺（抗性很高）"] → ["火焰"] | ② 被括注标成 very resistant 的项只留在 very_resistant 一行；very_resistant 字段未动 |
| queen | summon[0].qty / qty_zh | ["1 (entry key, not consumed; the first fight requires no sacrifice)", "1（进入用的钥匙，不消耗；首战不需要祭品）"] → ["1 (entry key, not consumed)", "1（进入钥匙，不消耗）"] | ③ 缩短召唤物括注；被拿掉的两句（首战不需要祭品、首次击败后再次召唤）在 bosses 页正文表格原本就有，并补进女王页正文 |
| queen | summon[1].qty / qty_zh | ["3 (to summon her again after her initial defeat)", "3（首次击败后再次召唤）"] → ["3 (re-summon)", "3（再次召唤）"] | ③ 缩短召唤物括注；被拿掉的两句（首战不需要祭品、首次击败后再次召唤）在 bosses 页正文表格原本就有，并补进女王页正文 |

中文 bosses 页要点框对应句（「亚格鲁斯的 Vegvisir 生成概率很小」）没有同样的语病，未动。

③ 手机宽度（390px）实测：/valheim/bosses/ 自动汇总表女王行行高 333px → 195px，/valheim/zh/bosses/ 同一行 254px → 195px；改后两页所有表格最高行为 235px（英文正文手写表女王行，未动）。

门禁：构建通过，check_content / check_i18n（含 valheim 成对校验）/ check_snapshot / check_ga / check_sitemap / link_check / url_consistency / hub_no_adsterra 全部 0 阻塞；sitemap 732；两次构建树哈希一致。
