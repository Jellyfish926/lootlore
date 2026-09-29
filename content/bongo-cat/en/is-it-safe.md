---
slug: "is-it-safe"
url: "/bongo-cat/is-it-safe/"
title: "Is Bongo Cat Safe? The Keylogger Question"
seoTitle: "Is Bongo Cat on Steam Safe? Keylogger & Auto Clickers"
description: "Is Bongo Cat safe? What the developer has said about keylogging, internet use and anti-cheat, what you can verify yourself, and what is still open."
category: "Getting Started"
language: "en"
checkedAt: "2026-09-29"
scope: "Developer statements and official announcements only; this page is not a security audit"
type: "article"
tldr: ["The developer says Bongo Cat only counts how many keys you press and does not process them any further.", "The developer says the code is not obfuscated and ships with .pdb files, so anyone with the skills can inspect it; this page has not audited it.", "Online features grew over time: multiplayer, chat, Discord integration and the Paw Pass all arrived after the early 'no internet needed' statements.", "No official rule on auto clickers has been published; the only official automation is The Typer Was Replaced collab."]
related: ["steam-error", "achievements", "how-to-play"]
sourceUrls: ["https://steamcommunity.com/app/3419430/discussions/0/595142635298013586/", "https://steamcommunity.com/app/3419430/discussions/0/597398346071595150/", "https://steamcommunity.com/app/3419430/discussions/0/597399326497452033/", "https://steamcommunity.com/app/3419430/discussions/0/500576094581177001/", "https://steamcommunity.com/app/3419430/discussions/0/597398871354738307/", "https://store.steampowered.com/news/app/3419430/view/1815034432865853", "https://store.steampowered.com/news/app/3419430/view/1807332909696878", "https://store.steampowered.com/news/app/3419430/view/1830163047257430", "https://steamcommunity.com/app/3419430/discussions/0/597395881634853843/", "https://steamcommunity.com/app/3419430/discussions/0/785451333487492012/", "https://store.steampowered.com/news/app/3419430/view/1793384379535358", "https://store.steampowered.com/news/app/3419430/view/1829528821315214", "https://steamcommunity.com/app/3419430/discussions/0/598526935953404271/"]
date: "2026-09-29"
updated: "2026-09-29"
reviewed: "2026-09-29"
draft: false
author: "Jellyfi"
---
# Is Bongo Cat Safe? The Keylogger Question

Bongo Cat is a Steam release from Irox Games, and the developer says it only counts how many keys you press and does not process them any further. The developer says the code is not obfuscated and ships with .pdb debug files so it can be inspected. This page collects those statements with dates; it is not a security audit.

## Why do people ask whether it is a keylogger?

A tapping pet has to notice every key press and click, even while another window is focused, and that is also what a keylogger does. The Steam discussions have many threads asking the same thing, from launch week to 2026. The difference between the two is what the program does with each press, and that is the part only the developer's statements and the code itself can answer.

## What has the developer said about keylogging?

All of these were posted by the account with the [developer] badge in the official Steam discussions:

| When | Statement (quoted) | Thread |
| --- | --- | --- |
| March 2025 | "i just count how many keys are pressed i don't process them any further" | [Keylogger or crypto miner?](https://steamcommunity.com/app/3419430/discussions/0/595142635298013586/) |
| March 2025 | Mining: "there i no real impact regarding GPU/CPU" | Same thread |
| April 2025 | "the game requires no internet connection so it can't send out anything"; "i ship the .pdb files so you can take a look what the code does" | [Keylogger or malware?](https://steamcommunity.com/app/3419430/discussions/0/597398346071595150/) |
| April 2025 | "the code is not obfuscated for that reason, so you can just look at the code yourself with softwares like dnspy" | [Key tracker thread](https://steamcommunity.com/app/3419430/discussions/0/597399326497452033/) |
| 2025 | "no there is no malicious code but yes let others verify it for you.." | [Has anyone verified?](https://steamcommunity.com/app/3419430/discussions/0/500576094581177001/) |

The developer also argued that Windows Defender and similar antivirus tools would flag the app if it logged keys to a file or sent them over the internet. That is the developer's reasoning, not a test result, so treat it as context rather than proof.

![A black cat skin in a ninja headband tapping on the taskbar counter](ss02 "The counter shows a number of taps, not the keys themselves")

## Does Bongo Cat connect to the internet?

The early "no internet connection" answer describes the app as it was in 2025. Since then several online features have shipped, each announced by the developer:

- Multiplayer lobbies, handled "by Steam, so no servers" ([August 2025](https://store.steampowered.com/news/app/3419430/view/1807332909696878)).
- Anonymised analytics through Steam Stats, "mainly used by me to see what costume you pick" ([October 2025](https://store.steampowered.com/news/app/3419430/view/1815034432865853)).
- Lobby chat, which can be disabled in the Multiplayer tab ([April 13, 2026](https://store.steampowered.com/news/app/3419430/view/1829528821315214)), and a Discord integration that can be switched off in settings ([April 2026](https://store.steampowered.com/news/app/3419430/view/1830163047257430)).
- The Paw Pass, which cannot be redeemed offline (September 2026).

None of these announcements describe sending your typed keys anywhere. If you want the smallest footprint, you can turn off the Discord integration and chat, and skip multiplayer; single-player tapping and chest drops still work.

## Will an auto clicker get you banned?

No official rule has been published either way. We searched the Steam discussions for auto clicker, macro and ban threads on September 29, 2026, and none of the replies we read from the developer allows or forbids them. The closest statement is the developer telling a player who asked for a clicker that "typing 1000 letters in 30min should be possible :P no need for clickers" ([reply](https://steamcommunity.com/app/3419430/discussions/0/597395881634853843/)). Asked for an automatic chest-opening feature, the developer replied that it "won't be a feature sorry, it's always meant to be similar like a pomodoro timer" ([Auto-Chest thread](https://steamcommunity.com/app/3419430/discussions/0/598526935953404271/)).

The only automation the studio itself promotes is The Typer Was Replaced, a collaboration where The Farmer Was Replaced's `tap()` function drives your cat; you need to own that game. There is also no official "unlock all" method for items or achievements. When the 5 million tap achievement drew backlash, the developer removed it from Steam and said it would come back as an in-game achievement, "just not in Steam" ([announcement thread](https://steamcommunity.com/app/3419430/discussions/0/785451333487492012/)). As of September 29, 2026 the Steam list includes a 5 million tier (Bongo Beat Sapphire); no announcement says whether it is the achievement that was removed in February. For what each milestone takes, see the [achievements page](/bongo-cat/achievements/).

## Can it cause trouble in other games?

| Question | Developer's answer | Source |
| --- | --- | --- |
| VAC ban in CS2? | "nope, but cs2 will kick you out of the ranked lobby if you have it over the same window ... but no bans tho" | [CS2 thread](https://steamcommunity.com/app/3419430/discussions/0/597398871354738307/) |
| Clicks not counted in a game | Use the opt-in admin mode | [How to play](/bongo-cat/how-to-play/) |
| Hovering the cat tabbed you out of a fullscreen game | Fixed in the March 11, 2025 update | [Patch notes](https://store.steampowered.com/news/app/3419430/view/1793384379535358) |

Why would a tapping app want administrator rights at all? Admin mode is opt-in. The March 11, 2025 update introduced it, saying "this will make Bongo Cat start as admin, which solves a lot of issues regarding clicks not getting tracked in several games" ([patch notes](https://store.steampowered.com/news/app/3419430/view/1793384379535358)). Leave it off unless clicks in a specific game are not being counted.

That CS2 answer is the developer's view, not a statement from Valve. If you play competitive games with strict anti-cheat, the cautious choice is to close Bongo Cat for those sessions. Display and admin-mode fixes are on the [Steam Error and fixes page](/bongo-cat/steam-error/).

## Read next

- [Bongo Cat Steam Error: Fixes and Hotkeys Guide](/bongo-cat/steam-error/)
- [All 28 Bongo Cat Achievements and Unlock Rates](/bongo-cat/achievements/)
- [How to Play Bongo Cat: Taps, Chests and Drops](/bongo-cat/how-to-play/)
