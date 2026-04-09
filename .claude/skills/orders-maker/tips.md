# This file is intended to be tips to improve gameplay of the AI player

- Monsters can be deadly especially in the early game, so be cautious when moving into new regions without proper scouting or preparation.

- CAST GATE allows both studying and teleporting in the same turn (unlike MOVE)

- Make sure all mages and important leaders have `BEHIND 1` flag set so they are not easily killed in a fight

- Prefer behind flag for any archers

- Only 1 spell can be set active `COMBAT` spell so do not focus on multiple `COMBAT` spells at once

- Mages (any unit with magic skill) can only have 1 leader inside. Never buy directly men, create new units

- Once you cast `CAST GATE random` it is almost impossible to come back to region you teleported from

- Magic study rate is only halved outside a building with mage slots (Fort/Castle/Citadel) **above level 2**. Studying magic skills up to level 2 is at full rate (30 days/month) anywhere. Above level 2, studying outside a suitable building gives only 15 days/month. Source: engine code `monthorders.cpp` — "Magic study rate outside of a building cut in half above level 2."

- TURN/ENDTURN blocks cannot be nested. If you need multi-turn delayed orders, use a single TURN block for the next turn and handle subsequent turns in future order submissions.

- The `@` prefix on orders (e.g. `@GUARD 1`, `@TAX`) does NOT carry over between turns automatically. You MUST explicitly include all orders for every unit every turn, including `@`-prefixed repeating orders. The `@` prefix only means "repeat within the engine's processing of that turn's orders file" — it does not persist across turn submissions.

- **Scouts as garrison seeders:** Every turn a scout enters a new region with men for sale, FORM a new garrison unit, CLAIM silver, GIVE to the new unit, have it BUY local men + STUDY COMB. Use a TURN block so the new garrison activates @GUARD 1 + @TAX next turn. The scout continues moving. This expands your tax empire every turn at minimal cost (~$300-500 per garrison, pays back in 1-2 turns).

- Set `NOAID 1` for scounts to make sure when they are attacked, they not pulling everyone from adjustent regions. This is helpful for example when scout is in monster region.

- Always allocate ALL 5 faction points using the `FACTION` order. New factions start with only 2 points spent (1 Martial, 1 Magic) — the remaining 3 are wasted if you don't issue a FACTION order. Issue `FACTION martial <N> magic <M>` where N+M=5 on the first turn you generate orders. The valid type keywords for NewOrigins are `martial` and `magic` (NOT `war` or `trade`). Check the report header (e.g. "Martial 1, Magic 1") to see current allocation.