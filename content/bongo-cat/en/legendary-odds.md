---
slug: "legendary-odds"
url: "/bongo-cat/legendary-odds/"
title: "Bongo Cat Legendary Odds: Chests Needed per Tier"
seoTitle: "Bongo Cat Legendary Drop Rate: How Many Chests It Takes"
description: "Bongo Cat Legendary odds are listed at 1 in 500000 and Epic at 0.01%. See the derived average chests, taps and exchange trade-ups per tier, with the math."
category: "Hats, Skins & Achievements"
language: "en"
checkedAt: "2026-10-09"
scope: "Official tier odds read from the Steam store description on October 9, 2026 (dates on this page are UTC); every chest count, tap count and hour figure is our own derivation with the formula shown; the 10-for-1 exchange rule and the 30-minute drop timer come from the February 23, 2025 demo update; later announcements do not repeat the 10-item figure or call any length of time the drop timer; per-item odds are not confirmed"
type: "article"
tldr: ["The Steam store page lists Epic at 0.01% and Legendary at 1 in 500000 under \"Item drop pool chances\", with the note \"Subject to change\" (read October 9, 2026).", "Derived, assuming one item per chest: an average of 10,000 chests per Epic drop and 500,000 per Legendary drop; a 50% chance of one Epic takes 6,932 chests.", "Derived, assuming the February 2025 demo update's 10-for-1 exchange applies and each exchange moves up exactly one tier: about 407 chests per Epic and 4,066 per Legendary, as a best case.", "The developer has published event item counts (20 exclusive items, 4 per rarity, in three 2025 event posts) but no per-item odds or per-item supply in the sources we read, so the rarest single item is not confirmed."]
related: ["hats-skins", "exchange-trading", "how-to-play", "achievements"]
sourceUrls: ["https://store.steampowered.com/api/appdetails?appids=3419430", "https://store.steampowered.com/app/3419430/Bongo_Cat/", "https://store.steampowered.com/news/app/3419430/view/1792116353300258", "https://store.steampowered.com/news/app/3419430/view/1794102528240823", "https://store.steampowered.com/news/app/3419430/view/1834602721190507", "https://store.steampowered.com/news/app/3419430/view/1836506165556399", "https://store.steampowered.com/news/app/3419430/view/1792751526108641", "https://store.steampowered.com/news/app/3419430/view/1842212951313382", "https://store.steampowered.com/news/app/3419430/view/1813041031167641", "https://store.steampowered.com/news/app/3419430/view/1817483467044521", "https://store.steampowered.com/news/app/3419430/view/1845383656381895", "https://store.steampowered.com/news/app/3419430/view/1795283637960385", "https://store.steampowered.com/news/app/3419430/view/1803527891535449", "https://store.steampowered.com/news/app/3419430/view/1811772772484130", "https://store.steampowered.com/news/app/3419430/view/1811772772604122", "https://store.steampowered.com/news/app/3419430/view/1799088287821846"]
images: ["ss00"]
date: "2026-10-10"
updated: "2026-10-10"
reviewed: "2026-10-10"
draft: false
author: "Jellyfi"
---
# Bongo Cat Legendary Odds: Chests Needed per Tier

Bongo Cat's Steam store page lists Epic at 0.01% and Legendary at 1 in 500000 under "Item drop pool chances", marked "Subject to change". By our arithmetic, assuming one item per chest, that averages 10,000 chests per Epic and 500,000 per Legendary, and fewer if the demo-era 10-for-1 exchange still applies. The rarest single item is not confirmed.

## What are the official Epic and Legendary odds?

On October 9, 2026 (UTC) we read the game's description through the [Steam app details API](https://store.steampowered.com/api/appdetails?appids=3419430). Under the heading "Item drop pool chances*:" it prints five lines, the last two being "Epic - 0.01%" and "Legendary - 1 in 500000", followed by the footnote "*Subject to change". The same text sits on the [store page](https://store.steampowered.com/app/3419430/Bongo_Cat/). The full tier table, including the Unique tier that cannot drop, is in [hats and skins](/bongo-cat/hats-skins/); this page only does the arithmetic on it.

Two limits apply to everything below. First, the odds are per tier. The store page does not say how a drop picks one item inside a tier, so the chance of one specific Legendary hat is not confirmed. Second, the four percentage lines already add up to exactly 100% (90 + 9.5 + 0.49 + 0.01), which leaves no room for the Legendary line (1 ÷ 500,000 = 0.0002%). How the game fits Legendary into the roll is not stated. The gap is too small to move any figure on this page.

## How many chests does an Epic or Legendary take on average?

Only the "Official chance" column is official. The other three columns are derived, assuming one item per chest and independent rolls, neither of which the developer has spelled out. Average chests per drop is 1 ÷ chance. Chests for an X% chance of at least one drop is ln(1 − X) ÷ ln(1 − chance), rounded up.

| Tier | Official chance | Average chests per drop (derived) | Chests for a 50% chance (derived) | Chests for a 90% chance (derived) |
| --- | --- | --- | --- | --- |
| Uncommon | 9.5% | 10.5 | 7 | 24 |
| Rare | 0.49% | 204.1 | 142 | 469 |
| Epic | 0.01% | 10,000 | 6,932 | 23,025 |
| Legendary | 1 in 500000 | 500,000 | 346,574 | 1,151,292 |

The average is easy to misread. After exactly 10,000 chests the chance of having seen at least one Epic is 1 − 0.9999^10,000, about 63.2%, so more than a third of players would still have none. For a Legendary the same 63.2% point sits at 500,000 chests.

## Is trading up through the exchange faster than waiting for a drop?

On paper, yes, if two assumptions hold. The rule comes from the developer's Steam Next Fest Demo Update of February 23, 2025: "10 items of the same rarity can be upgraded to one of a higher tier" ([announcement](https://store.steampowered.com/news/app/3419430/view/1792116353300258)). That post patched the demo, before the full release of March 5, 2025, and none of the 63 announcements restates the 10-item figure for the full release, so whether it still applies is not confirmed. The quote also says "one of a higher tier", not the next tier. The buttons and the rule changes since then are on the [exchange and trading page](/bongo-cat/exchange-trading/). The cascade below assumes ten items per exchange and exactly one tier up per exchange; every number in it is derived.

| Target | Commons' worth needed (10 per step) | Chests if only Common drops are fed in (÷ 0.9) | Chests if every drop is traded up (÷ 2.46) |
| --- | --- | --- | --- |
| Uncommon | 10 | 12 | 5 |
| Rare | 100 | 112 | 41 |
| Epic | 1,000 | 1,112 | 407 |
| Legendary | 10,000 | 11,112 | 4,066 |

The 0.9 is the Common chance: you need 1,000 ÷ 0.9 chests, rounded up, to collect 1,000 Commons. The 2.46 is what an average chest is worth in Commons once the higher tiers are counted at their exchange value: 0.9 × 1 + 0.095 × 10 + 0.0049 × 100 + 0.0001 × 1,000 + (1 ÷ 500,000) × 10,000 = 0.9 + 0.95 + 0.49 + 0.1 + 0.02.

Read the last column as a best case. It assumes every item you drop goes into the exchange and nothing is left over, while the game slots duplicates and skips favourites, so the first copy of anything you keep does not count. The announcements we read also do not say how the item you receive from an exchange is chosen, so aiming the cascade at one particular hat is not confirmed to work.

On those assumptions the gap is wide: about 407 chests against 10,000 for an Epic (roughly 25 times fewer) and about 4,066 against 500,000 for a Legendary (roughly 123 times fewer).

## How long would those chests take in real time?

That depends on the chest timer and the tap cost, and the sources for both are old. The same February 23, 2025 demo update says "Increase the drop timer to 30min", and the patch notes of March 18, 2025 say the game "only shows chest popup if you have 1000 clicks" ([Bug fixes & Red Cross Fix](https://store.steampowered.com/news/app/3419430/view/1794102528240823)). The basics are in [how to play](/bongo-cat/how-to-play/).

Whether the 30-minute timer carried over to the full release is not confirmed: it comes from a demo patch, and after that February 23, 2025 update no announcement calls any length of time the drop timer. The [Steam Error Fix](https://store.steampowered.com/news/app/3419430/view/1799088287821846) post of May 8, 2025 says "You might need to keep Bongo Cat running for 30min until it will work normally again", without saying that this is the chest timer. The [June 5, 2026 post](https://store.steampowered.com/news/app/3419430/view/1834602721190507) on the backend update does not mention the timer, and none of the 63 developer announcements in the Steam news feed up to October 1, 2026 gives the drop timer a different length. The 1,000 figure does reappear after that update: the post of [June 27, 2026](https://store.steampowered.com/news/app/3419430/view/1836506165556399) says opening a friend's chest "costs you 1000 clicks".

| Goal | Chests | Taps at 1,000 per chest (derived) | Hours at one chest per 30 minutes (derived) |
| --- | --- | --- | --- |
| Epic through the exchange, every drop traded up | 407 | 407,000 | 203.5 |
| Epic as a direct drop, average | 10,000 | 10,000,000 | 5,000 |
| Legendary through the exchange, every drop traded up | 4,066 | 4,066,000 | 2,033 |
| Legendary as a direct drop, average | 500,000 | 500,000,000 | 250,000 |

Hours are chests × 0.5 and assume the app runs around the clock with every chest opened the moment it is ready, so they are a floor, not a forecast. They also leave out the second chest: [Emojis 2.0, and a sorry.](https://store.steampowered.com/news/app/3419430/view/1811772772484130) of October 2, 2025 announced a chest that "will ONLY contain emotes", and [Emote 2.0 and bug fixes](https://store.steampowered.com/news/app/3419430/view/1811772772604122) of October 6, 2025 added it. Its timer and odds are not in the announcements, and no chest count on this page includes it. In days that is about 8.5 for the exchange route to an Epic and about 85 for a Legendary; the direct-drop average for a Legendary works out to roughly 28.5 years (250,000 ÷ 8,760 hours). The 500,000,000 taps in the last row are 20 times the 25 million behind the rarest achievement, and the time that one takes is worked out on the [achievements page](/bongo-cat/achievements/).

## What is the rarest item in Bongo Cat?

Not confirmed. In the announcements and store text we read, Irox Games has not published how many copies of any item exist, and the store page gives odds by tier, not by item. Event posts do give item counts: the [April Event](https://store.steampowered.com/news/app/3419430/view/1795283637960385), [Summer Event](https://store.steampowered.com/news/app/3419430/view/1803527891535449) and Autumn Event posts of 2025 each announce 20 exclusive items with "4 for each rarity". Those are counts of items, not odds or supply for any one of them. What the official text does say is which groups do not drop from chests, or stop dropping after a date:

| Group | What the developer wrote | Announcement |
| --- | --- | --- |
| Two demo items | "The items will not be available via chests, so there will only be a limited number. They are legendary by definition (because there are only a few of them)." Players needed 30min of playtime in the demo | [Release Date Announcement - March 5th](https://store.steampowered.com/news/app/3419430/view/1792751526108641), March 2, 2025 |
| Unique rarity | "These items are not droppable and are claimed through special events like the advent calendar." | [New UI and monthly Skins, Hats and Emotes!](https://store.steampowered.com/news/app/3419430/view/1842212951313382), September 1, 2026 |
| Seasonal event items | After the end date "the items will no longer be dropable" | For example the [Autumn Event post](https://store.steampowered.com/news/app/3419430/view/1813041031167641), October 8, 2025 |

None of those lines ranks one item above another, and "legendary by definition" is the developer's description of scarcity, not a count. A ranking of single items would have to rest on third-party lists, so this page does not print one.

## Do events or the Paw Pass change the odds?

Not the headline numbers, as far as the announcements go. For the 2025 autumn event the developer wrote that an uncommon drop was more likely to be an event item, but "we didn't adjust the overall drop chances". For the 2025 winter event the change was to the items, not the tiers: "I moved many items to lower rarity tiers so that you will see a wider variety of items!", which the [same post](https://store.steampowered.com/news/app/3419430/view/1817483467044521) calls a temporary measure. Dates for each event are on the [events timeline](/bongo-cat/events/).

The Paw Pass posts mention chests with a stated rarity. The September 1, 2026 post describes "cosmetic/emote chests with up to legendary rarity", and the [October 1, 2026 post](https://store.steampowered.com/news/app/3419430/view/1845383656381895) says "chest with guaranteed rarity up to legendary". Neither post says how those chests relate to the store page's drop chances or how many chests of each rarity a pass holds, so both are not confirmed; the lanes are explained in the [Paw Pass guide](/bongo-cat/paw-pass/).

## What is still not confirmed?

- The chance of any single item inside a tier.
- Whether the demo update's 30-minute timer and 10-for-1 rule apply to the full release.
- Whether an exchange moves up exactly one tier, and how it picks the item it hands back.
- The timer and odds of the emote-only chest.
- Whether the odds have moved since they were first published. The footnote says they can, and we can only vouch for the reading of October 9, 2026.

We checked the store description and the full text of the 63 developer announcements in the game's Steam news feed, dated February 3, 2025 to October 1, 2026. We did not read the developer's Discord, and we have not timed a chest in the game ourselves.
