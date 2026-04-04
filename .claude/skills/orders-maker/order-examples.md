# Real-World Order Examples

Patterns observed across game-examples turns 1 through 83 (NewOrigins ruleset).

---

## Early Game (Turn 1) — Starting Unit Orders

A fresh faction's starting unit in the Nexus:
```
unit 857
move 6 in
declare default unfriendly
reveal faction
spoils walk
name unit "Alfred"
Faction magic 5 martial 0
option template long
combat "fire"
behind 1
withdraw 1 meal
consume unit
```

Pattern: First turn sets up faction options, declares attitudes, configures flags, and moves to enter the world. `move 6 in` enters shaft 6 then goes "in" to a starting region. Uses WITHDRAW for initial supplies.

---

## Standard Turn Pattern — Economy + Military

Typical mid-game turn (turn 15, faction 15) showing common structure:

### Tax collectors give silver to mages/students
```
unit 1264
GIVE 1258 100 SILVER
GIVE 1260 100 SILVER
GIVE 1262 40 SILVER
```

### Mage: cast + study (both in same turn)
```
unit 1258
CAST FARS 23 43 2
STUDY TELE
```
Farsight cast uses coordinates directly (shorthand for `CAST FARS REGION 23 43 2`). The unit both casts and studies.

### Combat mage with explicit REGION keyword
```
unit 869
CAST FARS REGION 18 42 2
STUDY FIRE
```

### Resource producer
```
unit 4290
PRODUCE STON
```

### Skill student with funding
```
unit 2896
STUDY BUIL
```

### Fleet sailing with multi-direction path
```
unit 1851
SHARE 1
SAIL SW NW NW
```
Sets sharing flag then sails three legs in one turn.

### Necromancer: give skeletons, cast summon, study
```
unit 1261
GIVE 4292 ALL SKEL
CAST SUSK
STUDY SUSK
```

### Movement order
```
unit 4292
MOVE N
```

---

## Creating New Units — FORM Patterns

### Basic FORM: buy troops and train
```
unit 1852
CLAIM 468
GIVE NEW 1 468 SILVER
WORK

FORM 1
  NAME UNIT "Guards"
  BUY 12 GNOM
  STUDY COMB
END
```
Parent unit claims silver, gives it to the new unit, then works. New unit buys men and starts training.

### Multiple FORM blocks (turn 50, mass recruitment)
```
unit 1852
SHARE 1
GIVE 8135 100 SILVER
GIVE 8928 100 SILVER
GIVE NEW 2 500 SILVER
GIVE NEW 3 500 SILVER
GIVE NEW 4 500 SILVER

FORM 2
  NAME UNIT "II VIII"
  HOLD 1
  BEHIND 0
  BUY 10 DRLF
  STUDY COMB
END

FORM 3
  NAME UNIT "II IX"
  HOLD 1
  BEHIND 0
  BUY 10 DRLF
  STUDY COMB
END

FORM 4
  NAME UNIT "II X"
  HOLD 1
  BEHIND 0
  BUY 10 DRLF
  STUDY COMB
END
```
Creates three army units at once, each buying 10 drow elves and starting combat training. HOLD prevents them from wandering. BEHIND 0 ensures they fight in front.

### FORM with undead army
```
unit 1261
HOLD 1
GIVE NEW 1 5 UNDE
STUDY SULI
CAST RAIS

FORM 1
  NAME UNIT "Ungratefull Dead"
  BEHIND 0
  HOLD 1
END
```
Necromancer creates a unit, transfers undead to it, casts raise undead, and studies summon lich.

---

## Gate Teleportation Patterns

### Random gate teleport with companions
```
unit 869
CLAIM 50
STUDY STEA
CAST GATE GATE 765 UNITS 9394 7463
```
Teleports self plus two other units to specific gate 765.

### Random gate (exploration)
```
unit 1262
CLAIM 10
STUDY COMB
CAST GATE RANDOM
```

### Targeted teleportation to coordinates
```
unit 1258
STUDY STEA
CAST TELE REGION 43 85 1
```
Teleports to surface region (43,85,1).

### Late-game teleport (no z coordinate for underworld)
```
unit 1263
STUDY FARS
CAST TELE REGION 18 42
```
When z is omitted, defaults to current level.

---

## Quartermaster / Transport Patterns

### Distribute from quartermaster
```
unit 9881
GIVE 7365 32 SILVER
DISTRIBUTE 8928 10 DBOW
DISTRIBUTE 9960 10 PARM
DISTRIBUTE 9060 5 ISHD
DISTRIBUTE 5023 1500 SILVER
```
Quartermaster distributes equipment and silver to multiple units across regions.

### Transport to quartermaster
```
unit 7459
GIVE 1261 100 SILVER
GIVE 7823 100 SILVER
GIVE 11126 50 SILVER
TRANSPORT 1852 1500 SILVER
```
Local unit sends silver to a distant quartermaster via transport network.

---

## Stealth / Assassination Patterns

### Steal attempt
```
unit 1263
STEAL 1625 SILVER
CLAIM 50
STUDY STEA
```
Attempts theft, also claims silver and studies. STEAL is a stealth-track order (separate from month-long).

### Assassination with movement escape
```
unit 878
@prepare staf
assassinate 15227
move sw sw s
```
Prepares staff of fire for combat, assassinates target, then moves away. The `@prepare` repeats each turn.

### Invisibility cast for stealth group
```
unit 1186
@prepare staf
@cast invi UNITS 857 1184 1185 1186
move nw
```
Makes multiple units invisible each turn (repeating order), then moves.

---

## Repeating Order Patterns (`@`)

### Common repeating orders
```
@study invi           ; study until manually changed
@prepare staf         ; always have staff readied
@cast invi units ...  ; maintain invisibility each turn
@work                 ; work every turn
@guard 0              ; keep guard off
@declare 33 ally      ; maintain alliance
@share 0              ; keep sharing off
@avoid 1              ; always avoid combat
```

### Commented-out notes with @ (persist across turns)
```
@; 28, 42, 44, 49, 52, 55, 79 bad
@; 8, 27, 32, 33, 53, 69, 83, 95, 103 good
```
Using `@;` creates repeating comments — a way to keep notes in the order template across turns.

---

## Late Game Patterns (Turn 83)

### Large army management
```
unit 8048
GIVE 7365 100 SILVER
GIVE 1727 200 SILVER
GIVE 63 200 SILVER
GIVE 117 200 SILVER
GIVE 11440 50 SILVER
GIVE 665 120 SILVER
GIVE 355 200 SILVER
GIVE 6945 50 SILVER
GIVE 7463 100 SILVER
GIVE 4186 19 SILVER
GIVE 869 700 SILVER
```
Guard unit distributes silver to 11 different units (army, mages, scouts, healers).

### Apprentice with cornucopia and earth lore
```
unit 6945
STUDY OBSE
CAST EART
```
Apprentice-level mage studies observation while casting earth lore (creates food).

### Guard + Tax with FORM
```
unit 7124
GUARD 1
TAX
GIVE NEW 1 255 SILVER

FORM 1
  NAME UNIT "Guards"
  BUY 5 DRLF
  STUDY COMB
END
```
Sets guard, taxes, then creates a new guard unit with the tax income.

### Combat-specialist army units doing WORK
```
unit 4479
WORK
unit 6522
WORK
unit 5229
WORK
```
Elite combat units (COMB 5) working for silver when not in battle — common late-game pattern for armies waiting to deploy.

---

## Edge Cases and Unusual Patterns

### Unit comment after unit number
```
unit 857 ; Alfred
unit 689 ; Unit
unit 74 ; Speculation
```
Comments on the `unit` line are valid and commonly used for human-readable labels.

### Double-space in order (still works)
```
STUDY  ILLU
```
Extra whitespace between keyword and argument is tolerated by the parser.

### Quoted skill name in combat spell
```
combat "fire"
```
Quotes around the skill name are accepted.

### Items with underscores vs spaces
Both `winged_horse` and `WING` work as item identifiers. Skill names like `gate_lore`, `mind_reading` use underscores. Abbreviation tags like `GATE`, `MIND` are also accepted.

### No orders for a unit (empty section)
```
unit 1265
```
Unit with no orders will use any standing repeating orders, or default to idle/autotax based on flags.

### Multiple orders that conflict
```
unit 1263
STEAL 1625 SILVER
CLAIM 50
STUDY STEA
```
STEAL is stealth-track (phase 5). CLAIM is instant (parsing). STUDY is month-long (phase 25). All three execute because they're in different tracks.
