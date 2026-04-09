# Non-Player Units

[< Magic](magic.md) | [Back to Index](README.md) | [Turn Sequence >](turn-sequence.md)

## City and Town Guardsmen

All cities and towns spawn guardsmen at game start.

### Behavior
- **Defend** any units attacked in the city/town
- **Prevent** theft and assassination (if Observation is high enough)
- Remain on **guard** (block taxation/pillaging by unfriendly factions)
- Can be killed in combat
- **Respawn** if the city/town remains unguarded after they're eliminated

### Implications
- New players are protected in starting cities
- To tax/pillage a guarded town, you must defeat the guardsmen first
- Maintaining a guard unit in the region prevents guardsman respawn

## Wandering Monsters

Monsters roam freely throughout Atlantis.

### Behavior
- Occasionally attack player units
- Spawn in **unguarded regions**
- May advance to adjacent hexes
- Prefer specific terrains (affects movement probability)

### Lairs
- Lair-dwelling monsters **never leave** their structures
- Attack units present in the region based on aggression level
- Empty lairs **respawn monsters** regularly
- **Guarding** a region prevents both monster spawning and lair respawning

### Monster Movement
Monsters have terrain preferences that determine movement probability between preferred, neutral, and avoided terrain types.

## Controlled Monsters

Magically summoned/obtained monsters function as **inventory items**.

### Properties
- Carry things at their speed of movement
- Fight for their controlling unit in combat
- **Always fight from front rank** even if controlling unit has `BEHIND` flag
- Use `SHOW ITEM <monster>` to check capacity and speed

### Transfer Rules
- Some monsters transfer freely between units
- Others remain **bound** to their original controller
- Transfer rules vary by monster type
