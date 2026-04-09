# Combat

[< Economy](economy.md) | [Back to Index](README.md) | [Stealth >](stealth.md)

## Attitudes

Factions declare attitudes toward others using `DECLARE`:

| Attitude | Effects |
|----------|---------|
| **Ally** | Auto-defend in combat; prevent theft/assassination; share items if SHARE flag |
| **Friendly** | Accept gifts, allow structure entry; permit tax (not pillage) |
| **Neutral** | Default stance; no special interactions |
| **Unfriendly** | Block entry to guarded regions; no auto-attacks |
| **Hostile** | Auto-attack identified units on sight |

- `DECLARE DEFAULT <attitude>` sets stance toward unknown factions
- Specific declarations override default
- `DECLARE <faction_number>` with **no attitude** removes the override (reverts to default)
- Units need sufficient **Observation** to identify enemies
- If a unit is visible but faction is **unidentifiable** (insufficient Observation), it is treated using the **default attitude** — even if the unit belongs to a Hostile faction
- However, **Friendly/Ally** declarations are honored even without identification — units "produce proof of identity when relevant"

## Combat Equipment Orders

These instant orders configure a unit's combat loadout (processed during order parsing):

### PREPARE
```
prepare [item]
```
- Sets a battle item for use in combat. No argument clears it.
- Setting PREPARE **clears any combat spell** (and vice versa).

### WEAPON
```
weapon [item1] [item2] ...
```
- Sets preferred weapons (up to MAX_READY items). No arguments clears preference.
- Unit will use these weapons in order of preference during combat.

### ARMOR
```
armor [item1] [item2] ...
```
- Sets preferred armor (up to MAX_READY items). No arguments clears preference.

## Attacking

### Requirements
1. **Visibility**: attacker must see the target
2. **Catchability**: attacker's effective Riding skill must >= target's

### Effective Riding Levels
| Mode | Effective Riding |
|------|-----------------|
| Cannot ride | 0 |
| Can ride | 3 |
| Can fly | 5 |

**Attack vs Defense riding**: For **attack**, only one man in the unit needs to be able to ride or fly. For **defense**, the **entire unit** must be able to ride or fly. A unit inside a building, fleet, or any structure **cannot use defensive Riding** to avoid attack.

### ADVANCE vs ATTACK
- `ATTACK` declares attack on specific units
- `ADVANCE` forces entry through guarded regions, triggering combat
- Losers of ADVANCE combat retreat to their previous region
- **Victory continuation**: if the advancing unit wins and its army **doesn't lose any men**, it may continue moving (provided it has enough movement points remaining)

## The Muster

When combat begins, both sides assemble:

### Attacking Side
- Non-avoiding units of the attacking faction
- Units from other factions also attacking the target

### Defending Side
- Identifiable units of the defending faction
- Allied non-avoiding units (if target not flagged `NOAID`)

### Adjacent Reinforcements
Units from adjacent regions join if they:
- Have sufficient movement points to reach the battle hex
- Don't have the `HOLD` flag set
- Can reach the terrain (check weight capacity, not actual movement)

### Friendly Fire Prevention
If a faction attacks an ally, that faction's troops withdraw entirely.

## The Battle

### Tactics
- Best tactician (highest Tactics skill) leads each side
- Ties favor lower unit number
- **Tactics advantage** in round 1: bonus to attack and defense

### Attack Resolution (each round)
1. Combatants attack in random order against random enemies
2. **50% base chance** of getting a lethal blow attempt
3. Success based on skill comparison:

| Skill Difference | Hit Chance |
|-----------------|-----------|
| Equal | 50% |
| Attacker +1 | 66% |
| Attacker +2 | 80% |
| Attacker +3 | 88% |

### Weapon Effects
- **Melee weapons** (sword, pike, etc.): modify Combat skill for attack/defense
- **Ranged weapons** (crossbow, longbow, javelin): ignore defender's weapon bonuses; attacker treated as Combat 0
- **Mounted units**: gain bonus based on riding skill and mount type

### Weapon Attack Types
Weapons may have one of several attack types: **Slashing, Piercing, Crushing, Cleaving, Armor Piercing**. Different armor types may give different survival chances against different attack types.

### Long/Short Weapons
Some melee weapons are defined as **Long** or **Short**. A soldier wielding a **longer weapon** than his opponent gets a **+1 bonus to attack skill**.

### Armor Survival
When a hit lands, armor gives a chance to survive:

| Armor | Survival % |
|-------|-----------|
| None | 0% |
| Leather Armor | 30% |
| Chain Armor | 33% |
| Plate Armor | 67% |

### Formation
- **Front rank**: default position; can attack and be attacked
- **Behind flag**: rear rank; immune until front line eliminated; cannot melee attack
- Ranged weapons can attack from behind

### Building Defense
Buildings protect up to their capacity:
- Tower: 10 men
- Fort/Stockade: 50 men
- Castle: 300 men
- Citadel: 1000 men

If there are too many units to all gain protection, **units who have been in the building longest get priority** (these units appear first in the turn report). Excess units gain no building protection.

## Combat Termination

- Combat ends when one side takes **50%+ casualties**
- Winner gets **one free attack round**
- If both sides exceed 50% losses = **draw** (no bonus round)

## Victory

### Spoils
- **50% chance** of recovering each item from defeated enemies
- `SPOILS` order customizes what to pick up:

```
spoils none|walk|ride|fly|swim|sail|all
```

| Value | Effect |
|-------|--------|
| `none` | Pick up nothing |
| `walk` | Only pick up items that keep the unit walking |
| `ride` | Only items that keep the unit riding |
| `fly` | Only items that keep the unit flying |
| `swim` | Only items that keep the unit swimming |
| `sail` | Only items compatible with sailing |
| `all` | Pick up everything (default) |

`NOSPOILS <bool>` is deprecated — use `spoils none` / `spoils all` instead.

### Healing
- Units with Healing skill attempt casualty recovery post-battle
- Consumes **1 Herb per attempt**
- Max **5 casualties per skill level** healed
- Only winner's healers participate

### Post-Battle Effects
- If winning side casualties exceed **5%**, survivors cannot move or attack again that turn

## Magic in Combat

Five attack/defense types: **Combat, Ranged, Energy, Weather, Spirit**

### Shields (Defensive Spells)
- Cast at round start
- Block same-type attacks
- Must be overcome before attacks reach soldiers

### Spell vs Shield
- Offensive spell contests shield using same mechanics as warrior combat
- If spell wins, shield is destroyed and spell hits defending army
- Unshielded men suffer **-2 effective skill** against spells (unless they have shields or defensive magic)

See [Magic](magic.md) for spell details.
