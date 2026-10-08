# Roblox Stock Exchange 2 待办(2026-10-08)

本文件由接入时从内容包 README 的「到期动作」「未获取项」两节逐字摘出(README 本身不进仓)。

## A. 有日期的动作

| 日期 | 动作 | 涉及文件 |
|---|---|---|
| 2026-10-16 23:00 UTC 之后(Custom Offices listing 结束) | 重读 events / game-passes / developer-products / badges 接口,把新出现的活动、商品、徽章补进去。round1 起各页对 Custom Offices 只写绝对时间(listed to start on 10 October 2026 at 20:00 UTC),10-10 当天不会有句子过期 | updates、index、entities |
| 赞数过 15,000 当天 | 重读游戏描述:新码进码表,TOOLS 是否还在决定是否移入 Expired;index「Is there a code?」与 FAQ 同步 | codes、index、entities(code-tools) |
| 每月 1 日 | codes 页 title / seoTitle / description 里的 October 2026 改当月;重核码;超 7 天未核 = P0 | codes |
| 每次复核 | 重取快照数字(在线、访问、收藏、赞踩、群成员、徽章累计)并同步页内时刻 | index、community、badges、how-to-play、algo-bots |
| 每 60 天 | 重跑 thumbnails 接口刷新 `180DAY-` URL 并逐个验 200 | _images.json、config card.img |

## B. 未获取项及原因

| 项 | 原因 / 处理 |
|---|---|
| TOOLS 的奖励 | 官方描述没写;只有 Roblox Den(C)写 20K Cash → 页面写 not stated |
| 兑换界面位置 | 只有码站描述(右侧礼物图标 → ENTER CODE);10-03 官方活动称换了新界面 → 页面只写通用步骤并标明未在游戏内确认 |
| 群组 wall | `groups.roblox.com/v1` 与 `/v2` 的 `groups/33446529/wall/posts` 都返回 404(原因不明,不归因为需登录) |
| 游戏 / 群组 social links | 接口无令牌返回 401 "Authentication token is missing";所以 Discord 邀请 qR8v6Murp3(服务器自称 official,约 1,231 人)无法从 Roblox 站内自证 → 页面写 calls itself official |
| 官方 Discord 频道内容、开发者 X / YouTube | 需登录 / 未找到可证实的官方账号;没有任何内容来自 Discord 消息 |
| 旧通行证接口 | `games.roblox.com/v1/games/10495391267/game-passes` 404;用新接口取到 13 个 |
| 不买通行证时的手续费、各等级杠杆上限、等级 / XP 表、每日奖励数额 | 无一手来源(只有通行证描述里的 0.02% 与 50x) |
| rebirth 条件 / 重置 / 收益;「Instant Acension」是什么 | 无一手来源 |
| bot 的解锁条件、设置项、收益、游戏内现金价;bot 是否在离线时交易 | 无一手来源;「best bot settings」有搜索需求但不抄社区参数 |
| 30 个无描述商品的效果(Trader Spotlight、Skip Recovery、Double Earnings、Simulate Day / Week 的具体影响等);与通行证同名的 11 个商品的用途(是否赠送版) | 接口只有名称与价格 |
| 各更新是否在活动起始时刻实装;配图里数值的实装值 | 活动 listing 与配图是预告 / 宣传;页面均以 announced / the art shows 口径写 |
| 支持设备、私服是否开放 | 匿名接口读不到;`createVipServersAllowed=false` 按 SKILL 口径不可用,页面不写 |
| 群组置顶活动(featured event id 8663088123344584917) | 单条活动接口 401,不知道是哪个游戏的活动,未使用 |
| twinfinite.net、progameguides.com 的直取 | curl 403(Cloudflare);两站内容只经 WebFetch 读到,未换方式硬取(记录在 `raw/comp/webfetch-notes.md`) |
| nerdschalk / allthings.how / gamertweak / mrguider / earnaldo / rotrends | 只在搜索结果见到标题,未读取 |
| 搜索量 / KD | 未用 Semrush,未估算;需求证据只有 Google 下拉(`raw/suggest.jsonl`) |
| 游戏内实测 | 没有进游戏;所有「界面长什么样」的描述都来自官方宣传图并注明 |
