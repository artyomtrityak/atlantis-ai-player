# Stealth & Observation

[< Combat](combat.md) | [Back to Index](README.md) | [Magic >](magic.md)

## Core Mechanics

- Units with **Stealth** skill can hide from observation
- Detection requires an observer in the same region with **Observation >= Stealth**
- If Observation = Stealth: unit visible but **faction name hidden**
- If Observation > Stealth: unit and faction fully visible

### Always Visible
Units are always visible when:
- Participating in combat
- Guarding a region (`GUARD 1`)
- Inside buildings or fleets

Even when visible, faction identification still requires superior Observation.

### REVEAL Order
- `REVEAL UNIT` - makes the unit visible
- `REVEAL FACTION` - makes faction visible too
- `REVEAL NONE` (or no argument) - hides again

## Stealing

Use `STEAL <unit_id> <item>` to steal without combat.

### Requirements
- **One-man unit only**
- Thief's Stealth must exceed ALL defenders' Observation in the region

### Amounts
- Silver: **$200 or half available** (whichever is less)
- Other items: **1 unit** stolen

### Detection
- Target faction learns what was stolen but **not the thief's identity**
- Allied units with sufficient Observation can prevent theft and identify the thief

## Assassination

Use `ASSASSINATE <unit_id>` to kill without full battle.

### Requirements
- **One-man unit only**
- Assassin's Stealth must exceed ALL defenders' Observation

### Combat
- One-on-one fight: assassin vs random member of target unit
- Assassin gets **one free round of attacks** before normal combat
- Neither combatant may use armor **except leather armor**
- Victory grants **50% of the loser's property**

### STEAL vs ASSASSINATE
- These two orders **overwrite each other** (can only do one per turn)
- They are on a **separate track** from month-long orders
