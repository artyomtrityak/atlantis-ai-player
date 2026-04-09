---
name: create-strategy
description:  Use when creating a strategy for a AI faction in Atlantis game. This skill will guide you through analyzing the first turns of the game to understand the playstyle of the faction, and then creating a comprehensive plan for the first X turns based on that analysis. The plan should be flexible and allow for dynamic reactions based on the current state of the game.
---

You are tasked to analyze factions playstyle to understand the way players play first X turns. Then based on your behavioral strategy located in `players/faction_<faction number>/faction_<number>_behavior.md`, create a comprehensive plan that will guide you through your first X turns.

Make sure that the plan is flexible and you can dynamically react based on current state of the game. Your plan will be for Faction <faction number> and will be located in `players/faction_<faction number>/turnsY_X_plan.md`.
To create a plan use report-parser skill and parse first X turns of reports located in game-examples/ folder. Deeply understand the strategy patterns and adapt your plan accordingly.

To understand strategy patterns, analyze the following aspects of the game:
- Orders files located in game-examples/ for the first X turns to understand what orders players are using, what units they are creating, and how they are using them. Orders files can be found in `game-examples/N/` folders, for example `game-examples/5/orders.3` for player number 3, turn 5.

Make sure you analyzing all factions behavior and orders to understand the overall strategy patterns in the game, and then create your own plan based on that analysis and your faction behavior rules.