# 旧页待修：因 patch-notes、cops-chase-rules 上线而不成立的句子

范围：`/home/claude/lootlore/content/untitled-wheelie-game/en/`。只列与两张新页直接矛盾的句子；访问数、成员数、listing updated 日期这类过期数字不在此表。本文件只是建议，旧页一个字没动。

出处代号（全部 2026-10-10 UTC 读取，原始响应在 `b5/raw/`）：
- EV = https://apis.roblox.com/virtual-events/v1/universes/10268960646/virtual-events?cursor=id_2zwAAAAAAAAAAzwAAAAAAAAAA（`w-events-full.json`，7 条）
- GP = game-passes 接口（`w-passes.json`）；DP = developer-products 接口（`w-devprod.json`）；GM = games 接口（`w-games.json`）

建议句里的日期都是读取日 10 October 2026；工程师改旧页时要同步把该页 checkedAt / updated / reviewed 和 sourceUrls（加 EV）改掉。

## A. 直接矛盾（17 行，22 处原句）

| # | 文件:行 | 原句 | 为什么不成立（出处） | 建议改成 |
|---|---|---|---|---|
| 1 | updates.md:10（scope） | …; the developer publishes no patch notes on Roblox | EV 有 7 条活动，description 是开发者写的更新公告 | …; the developer's own announcements are event listings, covered on the patch notes page |
| 2 | updates.md:29 | The developer does not publish patch notes on Roblox. What it does publish is the store: … | 同上；EV `data[0..6].description` | The developer's announcements are Roblox event listings; seven were listed on 10 October 2026, and the [patch notes page](/untitled-wheelie-game/patch-notes/) prints them. This page uses a second source, the store: … |
| 3 | updates.md:77 | None of this is a roadmap. The developer has not announced what comes next. | EV `data[6]`：HALLOWEEN UPDATE 🎃，start 2026-10-21T22:30Z，end 2026-11-01T08:00Z | None of this is a roadmap. On 10 October 2026 one event listing had a start time still ahead: HALLOWEEN UPDATE 🎃, from 21 October 2026 at 22:30 UTC to 1 November 2026 at 08:00 UTC. |
| 4 | index.md:65 | The developer does not post patch notes on Roblox, but every pass and product carries a creation date. | 同 #1 | The developer announces updates through Roblox event listings (seven on 10 October 2026, see the [patch notes page](/untitled-wheelie-game/patch-notes/)), and every pass and product carries a creation date. |
| 5 | index.md:86 | We do not list codes, bike stats, fine amounts or controls until an official source confirms them. | patch-notes 页列了公告里的四个 moped 速度；EV `data[5].description`：`Normal Moped, 40MPH stock, 80MPH modded 🛵` / `Junkyard Moped, 35MPH stock, 160MPH modded 🛠️` | We do not list codes, fine amounts or controls until an official source confirms them; for bike stats we print the four moped speeds from the developer's Mopeds + Rain announcement and nothing else. |
| 6 | cops-fines.md:10（scope） | …; fine amounts and chase rules are not published | EV `data[4].description`：AI COPS 👮 公告 9 + 3 条追逐规则；金额仍无 | …; fine amounts are not published; the chase rules the developer announced are on the cop chase rules page |
| 7 | cops-fines.md:13（tldr 第 3 条） | Fine amounts and how a chase ends are not published anywhere official. | 公告第 5 条：被抓罚款、逃脱拿钱；第 8 条：`If they lose sight of you for over 60 seconds, they give up.` | Fine amounts are not confirmed; the developer's AI COPS announcement says a chase ends in a fine if you are caught, in a payout if you escape, and when cops lose sight of you "for over 60 seconds". |
| 8 | cops-fines.md:34 | So a catch leads to a fine. The developer has not published: | 表里一部分已有公告答案（见 #9），引导句要改 | So a catch leads to a fine. The store records we read do not answer the following; the announced chase rules are on the [cop chase rules page](/untitled-wheelie-game/cops-chase-rules/): |
| 9 | cops-fines.md:42 | \| Are the cops computer-controlled? \| The promotional art is labelled "AI COPS" \| | EV `data[4]`：title `AI COPS 👮`，description 开头 `AI Cops are being added!` | \| Are the cops computer-controlled? \| The developer's event listing is titled "AI COPS 👮" and opens with "AI Cops are being added!" \| |
| 10 | bikes.md:10（scope） | …; the full bike list, in-game prices and stats are not published outside the game | 同 #5 的两行速度 | …; the full bike list and in-game prices are not published outside the game, and the four published speed figures (two mopeds) are on the patch notes page |
| 11 | bikes.md:13（tldr 第 4 条） | No official bike stats exist, so we do not rank a best bike. | 同 #5 | The developer's announcements give speed figures for two mopeds and for no other bike we could find on 10 October 2026, so we do not rank a best bike. |
| 12 | bikes.md:26 | The bikes the developer has named are the Tuttiro Bike, the Eblox Dragster and two bike groups called "Ebikes" and "Emotos". | EV 另有 `Normal Moped`、`Junkyard Moped`（`data[5]`）、`Jetson Ebike`（`data[3]` 第 5 项） | The store records name the Tuttiro Bike, the Eblox Dragster and two bike groups called "Ebikes" and "Emotos"; the developer's event announcements add Normal Moped, Junkyard Moped and Jetson Ebike. |
| 13 | bikes.md:26（同段末句）、bikes.md:28 | The full bike list, prices and stats are not published outside the game. / This page collects every bike-related name the developer has published on Roblox, checked on 30 September 2026. | 同 #12；「every」不再成立 | The full bike list and prices are not published outside the game. / This page collects the bike-related names in the store records; names from the event announcements are on the [patch notes page](/untitled-wheelie-game/patch-notes/). |
| 14 | bikes.md:46 | The developer has not published speed, handling or price data for any bike outside the game. | 同 #5 | The developer's Mopeds + Rain announcement lists "40MPH stock, 80MPH modded" for Normal Moped and "35MPH stock, 160MPH modded" for Junkyard Moped; we found no handling or price data, and no speed for any other bike, in the records we read on 10 October 2026. |
| 15 | money.md:13（tldr 第 1 条）、beginner.md:49、upgrades.md:33、how-to-play.md:39 | Pizza delivery is the one way to earn money that the developer names outright. / …they are the one way to earn money that the developer names outright. / Pizza delivery is the one income source the developer names. / The one money source named outright | EV `data[4].description` 第 5 条：`if you escape, then you will get the money that the fines would have costed you!`；`data[1].description`：`1 new job`（未命名） | Pizza delivery is the job the game description names. The developer's AI COPS announcement also says an escape from the cops pays "the money that the fines would have costed you", and the BIG UPDATE announcement lists "1 new job" without naming it. （四处按各自句式套用；how-to-play 表格单元可缩成「The job the description names」） |
| 16 | money.md:77 | Fines are the one penalty the developer mentions — … | 仍只有罚款一种处罚，但公告把追逐写成有赔有赚：`Getting chased will be a gamble, you either lose money or make money.` | Fines are the penalty the developer's records mention, and the AI COPS announcement describes a chase as "a gamble, you either lose money or make money". |
| 17 | upgrades.md:58、beginner.md:60 | There is no bike list with prices or stats, because the developer has not published one outside the game. / …controls, bike stats and place names do not appear in any official source we could check. | 同 #5；bike stats 有四个数 | There is no full bike list with prices, because the developer has not published one outside the game; the four moped speed figures the developer has announced are on the [patch notes page](/untitled-wheelie-game/patch-notes/). / …controls and place names do not appear in any official source we could check; for bike stats, two mopeds have announced speeds. |

按文件计：updates 3 句、index 2 句、cops-fines 4 句、bikes 6 句（#13 含 2 句）、money 2 句、beginner 2 句、upgrades 2 句、how-to-play 1 句；表里 17 行对应 22 处原句（3+2+4+6+2+2+2+1）。

## B. 不矛盾，但建议顺手补一句（不计入上面的条数）

| 文件:行 | 现状 | 可补内容（出处） |
|---|---|---|
| bikes.md:58 | Backfire 写成「probably a cosmetic or sound effect」的猜测 | MAP REVAMP 第 4 项原文 `Backfire Mod for Gas Bikes`（EV `data[3]`）：公告说了它是给 Gas Bikes 的 mod，效果仍未说明 |
| community.md:64 | 「testing seems to happen privately」 | FULL GAME RELEASE 公告 `The full game will be set to release on july 23, 1:00PM MST (4:00 PM EST)!`（EV `data[0]`，start 2026-07-23T20:00Z）；AI COPS 公告 `Single player servers, seperate from the actual game.`。两句都没提 testing，`test\|beta\|alpha` 在全部记录里 0 命中，所以原句不算被推翻 |
| cops-fines.md:40–41 | 「What counts as being caught? / Can you go to jail or lose your bike?」两行写 Not published / Not mentioned | 公告仍没回答（`jail\|arrest\|prison` 0 命中），可保留，但「anywhere official」建议换成带范围的说法 |
| cops-fines.md:64 | 「The official art puts the police on the same highway…」 | 公告第 1 条 `Cops will park beside highways, in parking lots, or in random places` 可替换宣传图推断 |
| how-to-play.md:36 | 「Police chase riders; getting caught means a fine」 | 可加链到 cops-chase-rules |
| updates.md:81、cops-fines.md:73 | 「where announcements might appear」「Both are recent… the newest pass」 | 时效措辞，另行安排 |
