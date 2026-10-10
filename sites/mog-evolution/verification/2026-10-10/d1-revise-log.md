# D1 更正日志（mog-evolution；2026-10-10）

## D1fix2b：私服句收紧（2026-10-10）

调度员定：以早先验证员的结论为准，createVipServersAllowed 单独不能说明能否开私服。行号是改动前（HEAD 6d3a5e71 + D1fix2 暂存）的 HEAD 行号。

| 文件:行 | 编号 | 原句 → 新句 | 出处 / 依据 |
|---|---|---|---|
| how-to-play.md:13 | 私服句：只陈述字段值，not confirmed | "Servers hold 12 players and private servers are switched off." → "Servers hold 12 players; whether private servers are offered is not confirmed." | games v1 的 createVipServersAllowed 字段（false）；stone-skipping 实体备注里早先验证员的结论：该字段对已知有私服的游戏同样为 false，单凭它不能下结论 |
| how-to-play.md:92 | 私服句：只陈述字段值，not confirmed | Private servers are switched off, so you always join a public server. → Whether private servers are offered is not confirmed: the game record's createVipServersAllowed field read false on 1 October 2026, which alone does not settle it. | games v1 的 createVipServersAllowed 字段（false）；stone-skipping 实体备注里早先验证员的结论：该字段对已知有私服的游戏同样为 false，单凭它不能下结论 |
| how-to-play.md:18 | frontmatter 日期 | updated: "2026-10-01" → updated: "2026-10-10" | 只改个别句，只动 updated |
