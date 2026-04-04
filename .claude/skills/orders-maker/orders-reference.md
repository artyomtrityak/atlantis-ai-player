# Orders Syntax Reference

## Order File Structure

```
#atlantis <faction_number> [password]
unit <unit_id>
  <orders for unit>
unit <unit_id>
  <orders for unit>
#end
```

- `#atlantis <number> [password]` — opens faction order block; password required if set
- `#end` — closes faction order block
- `unit <number>` — selects unit for subsequent orders
- Lines starting with `;` are comments
- `@` prefix on any order makes it repeat automatically each turn

### FORM/END — Create New Units
```
form <alias>
  ; orders for new unit
end
```
Creates a new unit with alias number (positive integer, unique per region per faction). The new unit inherits flags from the forming unit.

### TURN/ENDTURN — Delayed Orders
```
turn
  ; orders executed next turn
endturn
```
Can be nested to delay multiple turns. FORM blocks can appear inside TURN blocks.

---

## Parameter Types

### Unit ID Formats
| Format | Example |
|--------|---------|
| `<number>` (existing unit) | `1234` |
| `new <alias>` (unit from FORM) | `new 1` |
| `faction <fac> new <alias>` | `faction 5 new 1` |
| `0` (discard/no target for GIVE) | `0` |

### Direction Constants
`north`/`n`, `northeast`/`ne`, `southeast`/`se`, `south`/`s`, `southwest`/`sw`, `northwest`/`nw`, `in`, `out`, `pause`/`p`, `<number>` (enter object N)

SAIL only accepts the six compass directions and `pause`/`p`.

### Boolean Values
`1`/`0`, `true`/`false`, `on`/`off`, `yes`/`no`

### Attitude Values
`hostile`, `unfriendly`, `neutral`, `friendly`, `ally`

### Item Categories (for GIVE ALL)
`normal`, `advanced`, `trade`, `man`/`men`, `monster`/`monsters`, `magic`, `weapon`/`weapons`, `armor`, `mount`/`mounts`, `battle`, `special`, `food`, `tool`/`tools`, `item`/`items`, `ship`/`ships`

### Template Types (for OPTION TEMPLATE)
`off`, `short`, `long`, `map`

---

## Execution Order

Orders execute in this fixed sequence each turn:

| Phase | Orders |
|-------|--------|
| 1 | FIND |
| 2 | ENTER/LEAVE (initial) |
| 3 | PROMOTE/EVICT |
| 4 | ATTACK (player-initiated, then auto-attacks) |
| 5 | STEAL/ASSASSINATE |
| 6 | GIVE/TAKE |
| 7 | ENTER (into newly created objects) |
| 8 | EXCHANGE |
| 9 | DESTROY |
| 10 | PILLAGE |
| 11 | TAX |
| 12 | GUARD 1 (guard activation) |
| 13 | CAST (magic) |
| 14 | SELL |
| 15 | BUY |
| 16 | FORGET |
| 17 | Mid-turn processing |
| 18 | QUIT |
| 19 | Remove empty units |
| 20 | WITHDRAW |
| 21 | SACRIFICE |
| 22 | Movement (MOVE, ADVANCE, SAIL) — by speed phases |
| 23 | Sink uncrewed fleets, drown units |
| 24 | TEACH |
| 25 | Month-long orders (STUDY, PRODUCE, BUILD, WORK, ENTERTAIN) |
| 26 | Economics processing |
| 27 | Teleport (CAST teleportation) |
| 28 | TRANSPORT/DISTRIBUTE |
| 29 | ANNIHILATE |
| 30 | Maintenance assessment |
| 31 | Post-turn processing |

Instant orders (flags, NAME, DESCRIBE, CLAIM, SHOW) and FORM are processed during order parsing, before this sequence.

---

## Mutual Exclusivity

**Month-long orders** overwrite each other with a warning:
MOVE, ADVANCE, SAIL, STUDY, TEACH, PRODUCE, BUILD, WORK, ENTERTAIN, IDLE, TAX*, PILLAGE* (*when TAX_PILLAGE_MONTH_LONG enabled)

**Additive orders** (multiple of same type merge):
- MOVE + MOVE — directions appended
- ADVANCE + ADVANCE — directions appended
- SAIL + SAIL — directions appended
- TEACH + TEACH — students merged
- BUY + BUY (same item) — amounts merged
- SELL + SELL (same item) — amounts merged
- ATTACK + ATTACK — targets accumulated

**MOVE and ADVANCE overwrite each other** (but not themselves).

**STEAL and ASSASSINATE overwrite each other** (separate from month-long).

---

## All Orders

### Faction-Level Orders

#### PASSWORD
```
password [new_password]
```
Sets or clears faction password. No argument clears to "none".

#### OPTION
```
option times | notimes
option showattitudes | dontshowattitudes
option template off|short|long|map
```

#### QUIT
```
quit [password]
```
Permanently removes faction. Requires password if set.

#### RESTART
```
restart [password]
```
Removes faction, creates new one with same email/password.

#### FIND
```
find <faction_number>
find all
```
Requests email address of another faction.

#### DECLARE
```
declare <faction_number> [attitude]
declare default <attitude>
```
Sets diplomatic attitude. No attitude on specific faction removes override (reverts to default).

#### FACTION
```
faction <type1> <points1> [type2] [points2] ...
faction generic
```
Changes faction type point allocation.

#### ADDRESS
```
address <new_address>
```
Changes faction email.

---

### Movement Orders (month-long)

#### MOVE
```
move <dir1> [dir2] [dir3] ...
```
Moves unit through directions. Stops (doesn't fight) if blocked. Remaining moves queue for next turn.

#### ADVANCE
```
advance <dir1> [dir2] [dir3] ...
```
Like MOVE but initiates combat against blockers. Overwrites MOVE.

#### SAIL
```
sail <dir1> [dir2] [dir3] ...
```
Sails a fleet. Must be fleet owner. Compass directions and pause only. Other units on the fleet can also issue SAIL to contribute sailing skill.

#### ENTER
```
enter <object_number>
```
Enters structure/fleet. Instant.

#### LEAVE
```
leave
```
Leaves current structure/fleet. Instant.

---

### Production Orders (month-long)

#### PRODUCE
```
produce [amount] <item>
```
Produces items. Optional amount caps production. Requires appropriate skill.

#### BUILD
```
build
build <object_type> [complete]
build help <unit_id>
build complete
```
Builds/continues structures or ships. `complete` auto-repeats until done. `help` assists another unit.

#### WORK
```
work
```
Earns silver through labor. No skill required.

#### ENTERTAIN
```
entertain
```
Earns silver through entertainment. Requires entertainment skill.

#### STUDY
```
study <skill> [level]
```
Studies a skill. Optional level used with `@` to auto-stop at target.

#### TEACH
```
teach <unit_id1> [unit_id2] ...
```
Doubles study rate of target units. Teacher needs higher skill level. Multiple TEACH orders merge.

#### IDLE
```
idle
```
Does nothing. Prevents default work order.

---

### Economy Orders

#### TAX
```
tax
```
Taxes region for silver. Requires combat-capable men.

#### PILLAGE
```
pillage
```
Pillages region (more silver, damages region). Mutual exclusion with TAX.

#### BUY
```
buy <amount|all> <item>
```
Buys from regional market. Multiple BUY for same item merge.

#### SELL
```
sell <amount|all> <item>
```
Sells to regional market. Multiple SELL for same item merge.

---

### Combat Orders (instant)

#### ATTACK
```
attack <unit_id1> [unit_id2] ...
```
Declares attack. Multiple ATTACK orders accumulate targets.

#### COMBAT
```
combat [skill]
```
Sets combat spell (magic skill with COMBAT flag). No argument clears it. Also clears any prepared item.

#### PREPARE
```
prepare [item]
```
Sets battle item. No argument clears. Clears combat spell. Only if USE_PREPARE_COMMAND enabled.

#### WEAPON
```
weapon [item1] [item2] ...
```
Sets preferred weapons (up to MAX_READY items). No arguments clears. Only if USE_WEAPON_ARMOR_COMMAND enabled.

#### ARMOR
```
armor [item1] [item2] ...
```
Sets preferred armor (up to MAX_READY items). No arguments clears. Only if USE_WEAPON_ARMOR_COMMAND enabled.

#### EVICT
```
evict <unit_id1> [unit_id2] ...
```
Evicts units from owned structure.

---

### Stealth Orders (month-long, separate track)

#### STEAL
```
steal <unit_id> <item>
```
Steals item from target. Requires stealth skill. Cannot steal men.

#### ASSASSINATE
```
assassinate <unit_id>
```
Assassinates target. Requires stealth skill.

---

### Item Management Orders (instant)

#### GIVE
```
give <unit_id> <amount> [unfinished] <item>
give <unit_id> all [unfinished] <item> [except <amount>]
give <unit_id> all <category>
give <unit_id> unit
```
Transfers items or entire unit. `give 0` discards. `except` keeps N when giving all. Multiple GIVE orders execute sequentially.

#### TAKE
```
take from <unit_id> <amount> [unfinished] <item>
take from <unit_id> all [unfinished] <item> [except <amount>]
take from <unit_id> all <category>
```
Takes items from unit. `from` keyword mandatory.

#### WITHDRAW
```
withdraw [amount] <item>
```
Withdraws from faction unclaimed pool. Not silver. Amount defaults to 1. Only if ALLOW_WITHDRAW enabled.

#### CLAIM
```
claim <amount>
```
Claims silver from faction unclaimed pool to unit. Processed during parsing.

#### EXCHANGE
```
exchange <unit_id> <give_amount> <give_item> <expect_amount> <expect_item>
```
Simultaneous exchange. Both units must issue matching orders. Ships cannot be exchanged.

#### TRANSPORT
```
transport <unit_id> <amount|all> <item> [except <value>]
```
Sends items via quartermaster network.

#### DISTRIBUTE
```
distribute <unit_id> <amount|all> <item> [except <value>]
```
Distributes items from quartermaster outward.

---

### Flag Orders (instant, boolean)

| Order | Effect |
|-------|--------|
| `guard <bool>` | Guard status (prevents others from taxing) |
| `avoid <bool>` | Avoid combat (clears guard) |
| `behind <bool>` | Fight from rear |
| `hold <bool>` | Don't follow allies to adjacent combat |
| `noaid <bool>` | Refuse healing from other factions |
| `share <bool>` | Share items for maintenance |
| `autotax <bool>` | Auto-tax when idle |
| `nocross <bool>` | Don't cross water |

#### REVEAL
```
reveal [unit|faction|none]
```
Controls visibility of stealthy units. No argument or `none` hides.

#### CONSUME
```
consume [unit|faction|none]
```
Controls silver consumption for food. `unit` uses own silver first; `faction` uses unclaimed.

#### SPOILS
```
spoils none|walk|ride|fly|swim|sail|all
```
Controls battle spoils pickup. Movement types limit spoils to maintain that mode.

#### NOSPOILS (deprecated)
```
nospoils <bool>
```
Deprecated — use `spoils none`/`spoils all` instead. Still functional.

---

### Information Orders (instant)

#### NAME
```
name unit|faction|building|ship|object|structure|village|town|city <name>
```
Renames entity. Building/structure requires ownership. Village requires tower, town requires fort, city requires castle. City rename may cost silver.

#### DESCRIBE
```
describe unit|building|ship|object|structure <description>
```
Sets description. Empty description clears.

#### SHOW
```
show skill <skill> <level>
show item <item>
show object <object_type>
```
Requests detailed info in report. Max 100 per faction per turn. Faction must have knowledge of the requested skill/item.

---

### Magic Orders

#### CAST
```
cast <spell_skill> [arguments]
```
Month-long, executed during cast phase. Requires mage with the skill.

##### Generic spells (no extra arguments)
```
cast <spell>
```
Applies to: construct_portal, enchant_swords, enchant_armor, enchant_shields, construct_gate, engrave_runes_of_warding, summon_imps, summon_demon, summon_balrog, summon_skeletons, raise_undead, summon_lich, dragon_lore, wolf_lore, earth_lore, summon_wind, create_ring_of_invisibility, create_cloak_of_invulnerability, create_staff_of_fire, create_staff_of_lightning, create_amulet_of_true_seeing, create_amulet_of_protection, create_runesword, create_shieldstone, create_magic_carpet, create_flaming_sword, create_food, create_aegis, create_windchime, create_gate_crystal, create_staff_of_healing, create_scrying_orb, create_cornucopia, create_book_of_exorcism, create_holy_symbol, create_censer, blasphemous_ritual, phantasmal_entertainment.

##### Mind Reading
```
cast mind_reading <unit_id>
```

##### Bird Lore
```
cast bird_lore direction <dir>
cast bird_lore eagle
```

##### Invisibility
```
cast invisibility units <unit_id1> [unit_id2] ...
```
Multiple CAST invisibility orders are additive (units accumulated).

##### Gate Lore
```
cast gate_lore random [level] [units <unit_id1> ...]
cast gate_lore gate <gate_number> [units <unit_id1> ...]
cast gate_lore detect
```
`random` teleports through random gate. `gate <N>` teleports to specific gate. `detect` finds nearby gates. `units` specifies who travels.

##### Portal Lore
```
cast portal_lore <target_mage_id> units <unit_id1> [unit_id2] ...
```

##### Region-Targeted Spells (Farsight, Teleportation, Weather Lore, Clear Skies)
```
cast <spell>
cast <spell> region <x> <y> [z]
```
Without `region` targets current location. With `region` targets coordinates.

##### Phantasmal Beasts
```
cast create_phantasmal_beasts wolf|eagle|dragon [amount]
```

##### Phantasmal Undead
```
cast create_phantasmal_undead skeleton|undead|lich [amount]
```

##### Phantasmal Demons
```
cast create_phantasmal_demons imp|demon|balrog [amount]
```

##### Transmutation
```
cast transmutation [amount] <item>
```
Valid items: mithril, rootstone, ironwood, floater, yew, winged_horse, admantium.

#### FORGET
```
forget <skill>
```
Permanently forgets skill (all experience lost). Executed during forget phase.

---

### Special Orders

#### DESTROY
```
destroy
```
Destroys owned structure. Instant.

#### PROMOTE
```
promote <unit_id>
```
Promotes unit to structure owner. Must be current owner.

#### JOIN
```
join <unit_id> [nooverload|merge]
```
Follows/joins target unit. `nooverload` prevents overloading fleets. `merge` merges into target.

#### SACRIFICE
```
sacrifice <amount> <item>
```
Sacrifices items at sacrifice-enabled structure.

#### ANNIHILATE
```
annihilate region <x> <y> [z]
```
Annihilates a region. Requires Annihilation skill.
