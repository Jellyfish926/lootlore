---
slug: "co-op"
url: "/valheim/co-op/"
title: "Valheim Co-op: Host, Crossplay and Servers"
seoTitle: "Valheim Co-op: Host, Crossplay and Servers | Valheim Guide"
description: "Choose between a host-run session and a dedicated server, run a join test, work through connection problems, and set co-op rules a long world can survive."
category: "Multiplayer & Maintenance"
language: "en"
checkedAt: "2026-09-17"
scope: "Vanilla standard survival; world modifiers, mods and later patches may change the rules"
type: "article"
tldr: ["Play at the same time? Use an in-game hosted session. Need the world up when the host is offline? Then look at a dedicated server.", "Run a minimal join test with one friend — see the same place, complete one interaction, quit normally — before you invite everyone.", "When nobody can connect, work through four layers: versions, then join code and access, then connection method, then networking.", "Agree progression and storage rules before you open the server, and name at least one admin who owns backups."]
related: ["save-1-0", "mods", "death-recovery"]
chineseCharacters: 963
sourceUrls: ["https://www.valheimgame.com/support/crossplay-faq/", "https://www.valheimgame.com/support/a-guide-to-dedicated-servers/"]
date: "2026-09-17"
updated: "2026-09-17"
reviewed: "2026-09-17"
gameVersion: "1.0.12"
draft: false
author: "Jellyfi"
---
# Valheim Co-op: Host, Crossplay and Servers

If you only ever play at the same time, start with an in-game hosted session; if your friends need the world available while the host is offline, then look at a dedicated server. Decide how you will play before you argue about hardware and cost, so you are not maintaining a long-term service for two or three weekend sessions.

## Run a minimal test the first time

Have the host create or load the world you plan to use, set the access method and password, then invite one friend to test joining. Confirm you can both see the same place, complete a simple interaction and quit normally, and only then bring everyone in.

![The interior of a Viking longhouse: long tables and wooden chairs, chandeliers lighting a throne under a red banner](ss16 "Confirm you can both see the same place and quit normally before inviting everyone")

Cross-platform joining works through the join code and similar features the game provides — the steps are in the [official Crossplay FAQ](https://www.valheimgame.com/support/crossplay-faq/). Crossplay is not the same thing as automatic cross-platform save syncing; those are separate features.

## When a dedicated server is the right answer

A dedicated server gives you a world that stays available, but somebody has to own updates, access control and backups. Steam players will find the server application under the tools category in their library; installation and startup requirements are in the [official dedicated server guide](https://www.valheimgame.com/support/a-guide-to-dedicated-servers/).

Do not drop a stranger's config file over an existing world. Use a test world to confirm that starting, connecting, saving and reloading all work, then migrate your real progress. Two servers having the same name does not tell you which world data is actually loaded — check.

## Four layers to work through when nobody can connect

Start with game and server versions; then the join code, address, password and access list; then the connection method you are using; and only then lower-level networking. The Steam backend and the crossplay backend follow different rules, and the developers state that the crossplay backend cannot be joined via a local or loopback IP — take the details from the [server guide](https://www.valheimgame.com/support/a-guide-to-dedicated-servers/).

If only one player cannot join, look at that player's platform, version and permissions. If everyone fails, check whether the service actually started. Do not open by rebuilding the world or switching off all your security — those moves rarely target the real cause.

## Agree on progression and storage rules before you open the server

Decide up front whether players may beat main-line bosses alone, whether they can take key summon materials, whether outside characters may bring gear in, and who is allowed to change world modifiers. None of this is a technical fault, but it often decides whether a co-op world lasts.

![The build menu open in front of a village of wooden Viking huts, listing roof, wall and stair pieces](ss08 "Three storage categories are enough: shared, personal and key progression materials")

Three storage categories — shared, personal and key progression materials — are enough; you do not need an elaborate system. Talk before changing portals, keep outpost names consistent, and do not empty the emergency food. The point of splitting jobs is to avoid duplicated work, not to make one person the permanent farmer.

## Finally, decide who owns backups

Name at least one admin to make a restorable copy before every update, and to save a new restore point after key progression. Backups should not live only inside the world that is running. When something goes wrong, stop and protect the data first, record the error and the recent changes, then decide which copy to restore. A server you can play on for years needs both a way in and a way back.

## Which hosting method to choose

| Situation | Suggested method | What you take on |
| --- | --- | --- |
| Playing with friends at a fixed time | In-game hosted session | Host online, saving works |
| Same world accessed at different times | Dedicated server | Hosting, updates, permissions, backups |
| Trying a mod list for the first time | Separate test world | Check dependencies and both-side configs, never test on the real save |

These suggestions are based on maintenance cost. They do not mean a dedicated server is inherently smoother, and they are not a recommendation to buy any hosting provider's plan.

## What to read next

- [Valheim 1.0: Restart Your World or Keep It?](/valheim/save-1-0/)
- [Valheim Mods Broken After Update: What to Do](/valheim/mods/)
- [Valheim Death Recovery: Get Your Gear Back](/valheim/death-recovery/)
