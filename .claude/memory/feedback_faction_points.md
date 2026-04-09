---
name: Always allocate all 5 faction points
description: New factions start with only 2/5 points spent — must issue FACTION order to use all 5 points, using keywords 'martial' and 'magic' (not 'war')
type: feedback
---

Always issue `FACTION martial <N> magic <M>` (where N+M=5) as early as possible. New factions start with only 1 Martial + 1 Magic = 2 points, wasting 3.

**Why:** Unspent faction points directly limit mages, apprentices, tax regions, and quartermasters. Wasting 3 points means significantly fewer mages and smaller economy cap.

**How to apply:** On the first turn you generate orders for any faction, check the report header (e.g. "Martial 1, Magic 1") and verify all 5 points are allocated. If not, add a FACTION order. For NewOrigins, the valid type keywords are `martial` and `magic` — NOT `war` or `trade` (those are for other rulesets). Also recruit additional mages early if mage slots are available.
