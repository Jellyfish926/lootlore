# 站点档案 — lootwiki.com（LootWiki 总站）

> 每轮复盘开工先读这份档案，收尾更新它。公开仓：本档案不写收入、单价、成本、回本数字，这些栏一律「见私有记录」。
> 建档：2026-10-09（周检行动项 HUB-7，见 `reviews/fleet-2026-10-09.md`）。最后更新：2026-10-09

| 项 | 值 |
|---|---|
| 域名 | `https://lootwiki.com`（`config/hub.json` 的 `base_url`） |
| 仓库 | `Jellyfish926/lootlore`（公开） |
| 架构 | Python 生成器 `build.py` + `hub/`；产物 `out/` 与 `build-stamp.json` 都提交，Vercel 直接服务 `out/`，无构建命令 |
| 内容来源 | 原生栏目 `content/<game>/en/*.md`（valheim 另有 zh）+ 五个子站静态产物快照 `sources/{beast,dragonsword,orc,sephiria,shift}/`（`sync-sources.yml` 每天 20:37 UTC 同步并重建） |
| 上线日 | 2026-09-21（出处：`built-sites.md` 总站行） |
| 当前页数 | sitemap 688 条（2026-10-09 实测） |
| 原生栏目登记 | `built-sites.md` |

## 节点复盘日期

| 节点 | 日期 | 状态 |
|---|---|---|
| d14 | 2026-10-05 | 已做（10-09 补做）：`reviews/2026-10-09-d14.md` |
| d30 | 2026-10-21 | 待做 |
| d60 | 2026-11-20 | 待做 |
| d90 | 2026-12-20 | 待做 |

## 数据资源

| 平台 | 资源 |
|---|---|
| Google Search Console | `sc-domain:lootwiki.com` |
| GA4 | 媒体资源 555365709，衡量 ID `G-NPTYZWM9KD` |

## 审核状态表

> 审核结果只发邮件，不主动核对就会一直停在旧状态；每次周检顺带核对。拒信原文逐字保存，不要转述。

| 平台 | 状态 | 核对日 | 备注 |
|---|---|---|---|
| AdSense | 未获取：AdSense 账号网站列表为空，lootwiki.com 不在列表 | 2026-10-09（后台只读实测） | 后台「网站」页显示「没有可供显示的数据」；政策中心无问题。把站加进列表、提审属于站主操作，见 `reviews/fleet-2026-10-09.md`「需要你处理」 |
| Adsterra 及其他联盟 | 不接（总站禁用） | — | 总站只走 AdSense；子站的 Adsterra 装载脚本在快照进总站时被剥掉 |

变现数字（收入、单价、成本、是否回本）：见私有记录。

## canonical 归属记录

总站快照页与子站同文页的 canonical 归属按游戏逐个定：同一截止日的 GSC 近 28 天，总站该游戏路径前缀下的展示合计对子站展示合计，高的一方自指，低的一方同文页指向它。

| 游戏 | 决定 | 改前数据（GSC 28 天，截止 2026-10-06） | 执行 | 回滚条件 |
|---|---|---|---|---|
| sephiria | 按 6.12 ② 定为总站自指、子站同文页指向总站 | 总站 `/sephiria` 7,825 展示；子站 sephiriawiki.site 16 展示 | 子站侧改动 2026-10-09 推送（是否上线以子站仓记录为准）；总站不用改，保持自指 | 之后两次周检两边展示相加比改前降 ≥30% 就 revert |
| shift / beast / orc / dragonsword | 未改，各自自指 | 见 `reviews/fleet-2026-10-09.md` | — | — |
