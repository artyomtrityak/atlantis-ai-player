# Magic

[< Stealth](stealth.md) | [Back to Index](README.md) | [Non-Player Units >](non-player-units.md)

## Overview

Magic is a discovery-based system - specific spells and their effects are learned through gameplay, not documented in the rules. This page covers the known framework.

## Who Can Use Magic

- Only **one-man leader units** can become mages
- Once a unit becomes a mage (by studying any Foundation), **the unit number is fixed** — mages may not GIVE men at all (but the mage can be given to another faction via `GIVE <unit> UNIT`)
- Faction's max mages/apprentices depends on Magic faction points:

| Magic Points | Max Mages | Max Apprentices |
|-------------|-----------|-----------------|
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 5 |
| 3 | 4 | 7 |
| 4 | 5 | 10 |
| 5 | 6 | 15 |

## Three Foundations

All magic builds on three foundation skills:

| Foundation | Focus |
|-----------|-------|
| **Force** | Quantity of magical energy channeled |
| **Pattern** | Handling complex patterns; healing and nature spells |
| **Spirit** | Meta-effects outside the physical world |

**Dependency rule**: Magic skills cannot be learned to a higher level than the skills they depend upon. Foundation skills gate all dependent skills.

## Study Requirements

| Condition | Study Rate |
|-----------|-----------|
| Inside building with mage slots (Fort+) | Normal |
| Outside / building without mage slots | **Halved** |

Study cost: **$100 per month** per person (on top of maintenance).

Buildings with mage slots:
- Fort / Stockade: 1 mage slot
- Castle: 2 mage slots
- Citadel: 3 mage slots

## Further Magic Study

Once a mage begins studying foundations, additional skills appear in reports. Each new level provides a **skill report** describing capabilities unlocked. Use `SHOW SKILL <skill> <level>` to review.

## Using Magic

Three methods of spell use:

### 1. Automatic Spells
- Continuously active; no order required
- Always in effect once learned

### 2. Combat Spells
- Set via `COMBAT <spell_skill>` order
- Used automatically during battles
- Only one combat spell active at a time
- Setting COMBAT clears any PREPARE item (and vice versa)

### 3. Cast Spells
- Use `CAST <spell> [arguments]` to cast
- **CAST is NOT a month-long order** — a mage can CAST a spell and still MOVE, STUDY, or use any other month-long order in the same turn
- One cast per turn maximum (the magical drain limits it, not the time)
- Processed during the Cast phase (phase 13 in turn sequence, before movement)

## Known Spell Categories

From the orders reference, these spells are known to exist (discovered through play):

### Summoning
- Summon Imps, Demons, Balrogs
- Summon Skeletons, Raise Undead, Summon Lich
- Dragon Lore, Wolf Lore
- Create Phantasmal Beasts (wolf/eagle/dragon)
- Create Phantasmal Undead (skeleton/undead/lich)
- Create Phantasmal Demons (imp/demon/balrog)

### Enchanting / Crafting
- Enchant Swords, Enchant Armor, Enchant Shields
- Engrave Runes of Warding
- Create Ring of Invisibility, Cloak of Invulnerability
- Create Staff of Fire, Staff of Lightning, Staff of Healing
- Create Amulet of True Seeing, Amulet of Protection
- Create Runesword, Shieldstone, Magic Carpet, Flaming Sword
- Create Aegis, Windchime, Gate Crystal, Scrying Orb, Cornucopia
- Create Book of Exorcism, Holy Symbol, Censer

### Utility
- Mind Reading (target unit)
- Bird Lore (scouting direction or summon eagle)
- Invisibility (target units) — **multiple CAST invisibility orders are additive** (units accumulate)
- Earth Lore
- Farsight (region targeting)
- Weather Lore, Clear Skies (region targeting)
- Create Food
- Phantasmal Entertainment

### Teleportation
- Gate Lore (random, specific gate, or detect gates)
- Portal Lore (teleport to target mage)
- Teleportation (region targeting)
- Construct Portal, Construct Gate

### Transmutation
- Transmute: mithril, rootstone, ironwood, floater, yew, winged horse, adamantium

### Destruction
- Blasphemous Ritual
- Annihilate (destroy a region)
- Summon Wind

## Magic in Combat

Five attack/defense types:

| Type | Description |
|------|-----------|
| **Combat** | Physical magical combat |
| **Ranged** | Magical ranged attacks |
| **Energy** | Energy-based attacks |
| **Weather** | Weather-based attacks |
| **Spirit** | Spirit/mental attacks |

### Shield Mechanics
- Defensive spells ("Shields") cast at the start of each round
- Shields block same-type attacks
- Offensive spell contests shield skill (same formula as melee combat)
- If offensive spell wins: shield destroyed, spell hits army
- Unshielded men: **-2 effective skill** against spells

## Apprentices

- Created by studying **Manipulation**
- Must be one-man leader units
- **Cannot cast spells**
- Can use mage-restricted items
- Count against faction's apprentice limit (not mage limit)
