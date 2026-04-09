---
name: Do not rename factions after first naming
description: Never issue NAME faction after the faction has already been named — only name once
type: feedback
---

Do not issue `NAME faction` orders after the faction has already been named. Only name a faction once (on the first turn you generate orders). Subsequent NAME faction orders are wasteful and risk unintended changes.

**Why:** The user explicitly requested this. Tips also state "Once your faction name is set, never change it." Renaming is irreversible and confusing for other players.

**How to apply:** Before adding a NAME faction order, check if the faction already has a non-default name (i.e., not "AI_faction_N"). If it does, skip the NAME order entirely.
