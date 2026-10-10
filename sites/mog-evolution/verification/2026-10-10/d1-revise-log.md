# D1 更正日志（mog-evolution；2026-10-10）

## D1fix2b：私服句收紧（2026-10-10）

调度员定：以早先验证员的结论为准，createVipServersAllowed 单独不能说明能否开私服。行号是改动前（HEAD 6d3a5e71 + D1fix2 暂存）的 HEAD 行号。

| 文件:行 | 编号 | 原句 → 新句 | 出处 / 依据 |
|---|---|---|---|
| how-to-play.md:13 | 私服句：只陈述字段值，not confirmed | "Servers hold 12 players and private servers are switched off." → "Servers hold 12 players; whether private servers are offered is not confirmed." | games v1 的 createVipServersAllowed 字段（false）；stone-skipping 实体备注里早先验证员的结论：该字段对已知有私服的游戏同样为 false，单凭它不能下结论 |
| how-to-play.md:92 | 私服句：只陈述字段值，not confirmed | Private servers are switched off, so you always join a public server. → Whether private servers are offered is not confirmed: the game record's createVipServersAllowed field read false on 1 October 2026, which alone does not settle it. | games v1 的 createVipServersAllowed 字段（false）；stone-skipping 实体备注里早先验证员的结论：该字段对已知有私服的游戏同样为 false，单凭它不能下结论 |
| how-to-play.md:18 | frontmatter 日期 | updated: "2026-10-01" → updated: "2026-10-10" | 只改个别句，只动 updated |

## D1last：Quick facts 标签与在线人数约数（2026-10-10）

（1）Quick facts 标签：实体 mog-evolution 的 release_date_en「30 August 2026 (experience created)」→ record_created_en「30 August 2026」（出处字段 release_date_source 同步改名；该日期取自 games.roblox.com/v1/games 的 created，页内原文也写 created on）；标签由 config/i18n/en.json 的 f_record_created 输出「Record created」。（2）在线人数见下表；不重读接口、不动 reviewed。

| 文件:行 | 编号 | 原句 → 新句 | 出处 / 依据 |
|---|---|---|---|
| community.md:70 | 在线人数改约数 | \| Players online when we checked \| 7,523 \| → \| Players online when we checked \| about 7,500 when read on 1 October 2026 \| | 瞬时值，沿用该页原读数与读取时刻，四舍五入到两位有效数字 |
| index.md:55 | 在线人数改约数 | Roblox counted 7,523 players online when we checked on 1 October 2026, → Roblox counted about 7,500 players online when we checked on 1 October 2026, | 瞬时值，沿用该页原读数与读取时刻，四舍五入到两位有效数字 |
| community.md:17 | frontmatter 日期 | updated: "2026-10-01" → updated: "2026-10-10" | 只改个别句，只动 updated |
| index.md:18 | frontmatter 日期 | updated: "2026-10-01" → updated: "2026-10-10" | 只改个别句，只动 updated |
