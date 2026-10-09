---
slug: "mac-linux-steam-deck"
url: "/bongo-cat/mac-linux-steam-deck/"
title: "Bongo Cat on Mac, Linux and Steam Deck: What Works"
seoTitle: "Bongo Cat Mac, Linux and Steam Deck Support Explained"
description: "Bongo Cat on Mac, Linux and Steam Deck: macOS 11.0 minimum and an experimental build, a Linux test for X11 only, and a Playable result in Valve's Deck report."
category: "Getting Started"
language: "en"
checkedAt: "2026-10-09"
scope: "Steam store data, Valve's Steam Deck compatibility report and the developer's Steam posts as read on October 9, 2026; dates on this page, including that reading date, are UTC; anything those sources do not state is marked not confirmed"
type: "article"
tldr: ["Steam lists Bongo Cat for Windows and macOS; the developer introduced the Mac build as experimental on March 23, 2026.", "The Mac minimum on the store is OS 11.0, an Intel 64-Bit or Apple silicon processor, 1 GB RAM and 700 MB of storage.", "Linux is not listed on the store; the developer offers a test version through the beta code linuxtesting, described as X11 only in a developer thread of June 10, 2026.", "Valve's Steam Deck report returned category 2, which Steam's own search filter labels Playable, on October 9, 2026; no developer announcement mentions Steam Deck."]
related: ["how-to-play", "steam-error", "is-it-safe"]
sourceUrls: ["https://store.steampowered.com/api/appdetails?appids=3419430", "https://store.steampowered.com/news/app/3419430/view/1827626365763660", "https://steamcommunity.com/app/3419430/discussions/0/806846367620396268/", "https://store.steampowered.com/news/app/3419430/view/1830163047265223", "https://store.steampowered.com/news/app/3419430/view/1834602721190507", "https://steamcommunity.com/app/3419430/discussions/0/573792389464878955/", "https://store.steampowered.com/saleaction/ajaxgetdeckappcompatibilityreport?nAppID=3419430", "https://store.steampowered.com/search/?term=bongo+cat&deck_compatibility=2", "https://partner.steamgames.com/doc/steamdeck/compat", "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=3419430&count=200&maxlength=0&feeds=steam_community_announcements"]
images: ["ss04"]
date: "2026-10-10"
updated: "2026-10-10"
reviewed: "2026-10-10"
draft: false
author: "Jellyfi"
---
# Bongo Cat on Mac, Linux and Steam Deck: What Works

Bongo Cat runs on Mac: Steam lists macOS next to Windows, with OS 11.0 as the minimum, and the developer introduced that build as experimental. Linux is not listed on the store; a test version for X11 is offered through a beta code. On Steam Deck, Valve's compatibility report returned Playable, not Verified, on October 9, 2026.

## Can you play Bongo Cat on a Mac?

Yes. On October 9, 2026 the [Steam app details API](https://store.steampowered.com/api/appdetails?appids=3419430) returned `windows: true`, `mac: true` and `linux: false` for the game, and the store page showed a Windows and a Mac icon beside the Play button. Irox Games, the developer, shipped the Mac build with the post [Regional Pricing, Experimental Mac Support, QoL Changes](https://store.steampowered.com/news/app/3419430/view/1827626365763660) on March 23, 2026: "With this update we will launch an experimental mac build that you can try out."

No announcement after that one says the Mac build has left the experimental stage, so whether the word still applies is not confirmed. The game is free and installs through Steam on both systems; what the cat does once it is running is covered in [how to play](/bongo-cat/how-to-play/).

| Platform | Steam store data on October 9, 2026 | What the developer has posted | How you get it |
| --- | --- | --- | --- |
| Windows | Listed | Released March 5, 2025 | Install from Steam |
| macOS | Listed | "an experimental mac build", March 23, 2026 | Install from Steam |
| Linux | Not listed; the Linux requirements block is empty | A version "that you can test", "Only works on X11", June 10, 2026 | Steam beta code `linuxtesting` |
| Steam Deck | Deck report category 2 (Playable) | No announcement mentions Steam Deck | Which build the Deck runs is not confirmed |

This page covers only Bongo Cat on Steam by Irox Games, app ID 3419430; any other project that uses the same name is outside its scope.

## What does the Mac version need?

The store's Mac requirements, copied from the same API response on October 9, 2026:

| Field | Minimum | Recommended |
| --- | --- | --- |
| OS | 11.0 | 13.0 |
| Processor | Intel 64-Bit or Apple silicon | Intel 64-Bit or Apple silicon |
| Memory | 1 GB RAM | 1 GB RAM |
| Graphics | "-" (the store gives no value) | "-" (the store gives no value) |
| Network | Broadband Internet connection | Broadband Internet connection |
| Storage | 700 MB available space | 700 MB available space |

The store prints the OS line as a bare version number. The storage figure is the one that differs most from Windows: 700 MB against the 100 MB the store asks for on Windows, which is seven times as much by our division (700 ÷ 100). The Windows figures are in the table on the how to play page.

The Mac version may also need one permission. The developer's [Mac Issues thread](https://steamcommunity.com/app/3419430/discussions/0/806846367620396268/) says that if tapping does not work you should go to the Input Monitoring section, which lists the apps allowed to read input "(keyboard, mouse, etc.)", and grant permissions to Steam and Bongo Cat. The thread was posted on March 23, 2026 and last edited on May 25, 2026. The click-by-click path is on the [Steam Error and fixes page](/bongo-cat/steam-error/), and the reason a tapping game reads input at all is explained in [is Bongo Cat safe](/bongo-cat/is-it-safe/).

The March post gives the motive for the port: "I know a lot of you want to play with your friends (that are on Mac or Linux)." It does not state in so many words that Mac and Windows players share lobbies, so treat cross-platform lobbies as not confirmed until you have joined one; lobby types are in the [multiplayer guide](/bongo-cat/multiplayer/).

## Is there a Linux version of Bongo Cat?

Two official sources give two different answers, and both are true for what they measure.

The store says no. The API returns `linux: false`, the Linux requirements block comes back with empty minimum and recommended lists, and the store page shows no Linux icon (all read on October 9, 2026).

The developer says there is one to test. A pinned thread titled [Linux Testing X11](https://steamcommunity.com/app/3419430/discussions/0/573792389464878955/), posted by the developer account on June 10, 2026, reads: "Hello we have a linux version that you can test. The beta code is: linuxtesting". It adds that the build "Only works on X11" and that the team would like more testers. Beyond the code, the opening post gives no install steps, no distribution list and no system requirements.

Wayland is the open question. The [June 5, 2026 announcement](https://store.steampowered.com/news/app/3419430/view/1834602721190507) said a Linux update for X11 was close and that "Wayland will take more time." Seven announcements were posted after that one, the last on October 1, 2026, and none of them contains the words Linux, X11 or Wayland. Wayland support, and a date for Linux appearing on the store listing, are not confirmed. None of the 63 announcements explains why the test version sits outside the public listing, and because the store's requirements block is empty, memory, storage and supported distributions for it are not confirmed either.

## Does Bongo Cat work on Steam Deck?

Valve's [Steam Deck compatibility report](https://store.steampowered.com/saleaction/ajaxgetdeckappcompatibilityreport?nAppID=3419430) for the game returned `resolved_category: 2` on October 9, 2026. The Valve page we read for this, the Steamworks Deck compatibility page linked below, does not mention that endpoint, and we looked at no other Valve documentation, so we checked the number against Steam itself: the store search filter "Narrow by Deck Compatibility" uses value 3 for Verified and value 2 for Playable, and a [search for the game with the Playable filter](https://store.steampowered.com/search/?term=bongo+cat&deck_compatibility=2) returned Bongo Cat while the Verified filter did not. Valve's [Steamworks documentation](https://partner.steamgames.com/doc/steamdeck/compat) defines Playable as "Your game functions on Deck/Machine, but may require manual work from the user."

The report lists five test results. Each token starts with `SteamDeckVerified_TestResult_`; the right-hand column is our plain reading of the token name, because the wording Valve shows on the store page is filled in by a script and we did not capture it.

| Token ending | display_type | Our reading |
| --- | --- | --- |
| `DefaultControllerConfigNotFullyFunctional` | 3 | The default controller layout does not reach every function |
| `ControllerGlyphsDoNotMatchDeckDevice` | 3 | Button icons on screen do not match the Deck's controls |
| `TextInputDoesNotAutomaticallyInvokesKeyboard` | 3 | Text entry does not open the on-screen keyboard by itself |
| `InterfaceTextIsNotLegible` | 3 | Some interface text is too small on the Deck's screen |
| `DefaultConfigurationIsPerformant` | 4 | The default settings perform acceptably |

The Steamworks Deck compatibility page (the one Valve page we checked, on October 9, 2026) does not contain the term `display_type`, so what those numbers stand for is not confirmed. The same response also returned `steamos_resolved_category: 2` and `machine_resolved_category: 2`; the search filter above only maps the Deck value, so the labels for those two are not confirmed.

Three things the report does not tell you. It does not say whether presses on the Deck's buttons count as taps; the store lists the game under "Partial Controller Support", and the controller settings the developer has described are on the Steam Error and fixes page. It does not say which build was tested. Valve's documentation states that "games without native Linux builds will be run through Proton", and the store lists no Linux build, but the report names neither Proton nor the test version. And the announcements are silent: none of the 63 announcements from February 3, 2025 to October 1, 2026 contains "Steam Deck", "SteamOS" or "Proton".

## What has the developer said about Mac and Linux, by date?

We searched the full text of all 63 developer announcements in the game's [Steam news feed](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=3419430&count=200&maxlength=0&feeds=steam_community_announcements) on October 9, 2026. Three of them mention Mac or Linux as a platform; the two threads are developer posts in the Steam discussions.

| Date | Where | What it says |
| --- | --- | --- |
| March 23, 2026 | Announcement: Regional Pricing, Experimental Mac Support, QoL Changes | Launches "an experimental mac build"; for Linux, "We are preparing a PC in our office so we can actively develop on it and test with it." |
| March 23, 2026 | Developer thread: Mac Issues | The place to report Mac problems, with the Input Monitoring fix |
| April 20, 2026 | Announcement: [Community Voting, Language Filter & Fixes](https://store.steampowered.com/news/app/3419430/view/1830163047265223) | "We also set up a PC in our office with Linux, we are on it. But it takes time especially with all the different sub-OS." |
| June 5, 2026 | Announcement of June 5, 2026 | A Linux update for X11 is close; "Wayland will take more time." |
| June 10, 2026 | Developer thread: Linux Testing X11 | A Linux version to test, beta code `linuxtesting`, "Only works on X11" |

## Which platform questions are still open?

As of October 9, 2026, these are not answered by the store data, Valve's report or the developer's posts:

- Whether the Mac build is still experimental.
- Whether Mac, Windows and Linux players can share a lobby (implied by the March post, not stated).
- When Wayland will be supported, and when Linux will be listed on the store.
- Which build a Steam Deck runs, and whether Deck button presses count as taps.
- The official wording of the five Deck test results, and the labels for the SteamOS and Steam Machine values.
