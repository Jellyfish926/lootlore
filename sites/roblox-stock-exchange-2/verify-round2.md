# round2 复验(2026-10-08)

方法:对当前 content/en/*.md 全文 grep(working/Active/best/every/only/next/upcoming/coming/Twinfinite/Pro Game Guides/holding account/8 hours/gameVersion/get-age-recommendation/cursor=);当前页对 tools/src_round0 逐行 diff(diff_new.txt)得全部新增/改写句;claims.md 507 条中与 round1 文本不同的 97 条全验;自行重新取证(game/votes/badges/passes/products/events/group/legacy/Roblox Den/Try Hard Guides/docs)。sourceUrls 逐个 GET:evidence/sourceurl-status-r2.txt,全部 200(含新增 www.roblox.com/games/110527353762049/Roblox-Stock-Exchange-2)。

## 结果
- round1 的 68 条(10 REFUTED + 58 UNVERIFIED):已落实 66(含作者保留的 M47、M48 经读 native.py 判定成立),未完全落实 2。
- 新写句子:全部事实/数字/日期/引语核对一致;新问题 1(低)。
- 未完全落实/新问题清单见下。

## 逐项独立判断
- author "Every guide published under that byline is listed below.":native.py 1201-1208 作者页分支在正文后追加 "Guides by Jellyfi",成员为 nav 各分类里 type=article 且 author 同名的页;8 个文章页(how-to-play/codes/badges/updates/community/gamepasses/shop/algo-bots)全部 author=Jellyfi,故成立(home 与 category 页不属 article,不算 guide)。CONFIRMED。
- {{BRAND}}:native.py 304-305 在 frontmatter 解析前对全文 replace 为 cfg["brand"];config/hub.json brand="LootWiki"。CONFIRMED。
- Custom Offices:全站均为绝对日期("is listed to start on Saturday 10 October 2026 at 20:00 UTC"、"listing ends on 16 October 2026 at 23:00 UTC");grep 无 next/upcoming/coming/about to;"runs until 9 October 2026 at 04:00 UTC" 为绝对日期。无 10-10 后会变错的将来时。title/seoTitle/description 数字(All 13/All 31/All 11/October 2026)与一手一致。
- 码页:Twinfinite/Pro Game Guides 全文无残留;"Two code pages/sites" 在 tldr、正文、community 计数自洽;Roblox Den(TOOLS 20K Cash;FUTURES 20,000 Cash and 20 XP;UPDATE 20 XP and 7,500 Cash;gift icon top-right;最后检查 10/07/2026 03:04PM UTC)与 Try Hard Guides(FUTURES/MEMECOINS/STOCKMARKET 仅 "Redeem code for Cash";UPDATE 7,500 Cash;"right corner";dateModified 2026-09-29;链接游戏页/群组页/Discord 邀请,无开发者帖)重新取证一致。
