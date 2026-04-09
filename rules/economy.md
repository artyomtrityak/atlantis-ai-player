# Economy

[< Skills](skills.md) | [Back to Index](README.md) | [Combat >](combat.md)

## Maintenance Costs

Every character requires monthly maintenance:

| Unit Type | Silver/Month |
|-----------|-------------|
| Normal person | 10 |
| Leader | 50 |

### Food Substitution
Food replaces silver at **30:1 ratio** - one unit of grain, livestock, fish, or meals replaces 30 silver (or fraction thereof).

### Payment Priority (highest to lowest)
1. Unit's own food items (if CONSUME UNIT set)
2. Faction food in same region (if CONSUME FACTION set)
3. Unit's own silver
4. Faction silver in same region
5. Unit's food items
6. Faction food items
7. Unclaimed silver pool
8. Allied units' silver in region (if SHARE flag set)
9. Allied units' food in region

Units that can't pay maintenance **starve and die**.

### CONSUME Order
```
consume unit|faction|none
```
- `unit` — unit prioritizes its own food/silver before faction pool
- `faction` — unit also draws from faction's unclaimed silver for food
- `none` — clears any consume preference (default behavior)

### WITHDRAW Order
```
withdraw [amount] <item>
```
- Withdraws items from faction's unclaimed pool to the unit
- **Cannot withdraw silver** (use `CLAIM` for silver)
- Amount defaults to **1** if not specified
- Processed at phase 20 in turn sequence

### CLAIM Order
```
claim <amount>
```
- Claims silver from faction's unclaimed pool
- Processed during order parsing (instant, before main sequence)

## Recruiting

Use `BUY` to recruit people in regions with available population.

- Available races vary by region
- New recruits arrive with **no skills or items**
- To create a new unit: `FORM` empty unit -> `GIVE` it money -> have it `BUY` people
- Leaders cost more to recruit than common folk

## GIVE Order

```
give <unit_id> <amount> [unfinished] <item>
give <unit_id> all [unfinished] <item> [except <amount>]
give <unit_id> all <category>
give <unit_id> unit
```

- `give 0` discards items
- `unfinished` keyword targets partially built items
- `except <amount>` keeps N items when giving all
- `give <unit_id> unit` transfers the **entire unit** to another faction
- Multiple GIVE orders execute sequentially

### Item Categories (for GIVE ALL / TAKE ALL)
`normal`, `advanced`, `trade`, `man`/`men`, `monster`/`monsters`, `magic`, `weapon`/`weapons`, `armor`, `mount`/`mounts`, `battle`, `special`, `food`, `tool`/`tools`, `item`/`items`, `ship`/`ships`

## Items

### Basic Resources

| Item | Skill (Level) | Material | Weight | Capacity | Notes |
|------|--------------|----------|--------|----------|-------|
| Silver | — | — | 0 | — | Currency |
| Grain | Farming (1) | — | 5 | — | Food (30 silver value) |
| Livestock | Farming (1) | — | 50 | 0 | Food |
| Iron | Mining (1) | — | 5 | — | Crafting material |
| Wood | Lumberjack (1) | — | 5 | — | Crafting material |
| Stone | Quarrying (1) | — | 50 | — | Building material |
| Fur | Hunting (1) | — | 1 | — | Crafting material |
| Fish | Fishing (1) | — | 1 | — | Food |
| Herb | Herb Lore (1) | — | 0 | — | Healing, crafting |
| Horse | Horse Training (1) | — | 50 | 20 | Mount, riding |
| Camel | Horse Training (1) | — | 50 | 20 | Mount, riding |

### Weapons

| Item | Skill (Level) | Material | Weight | Combat Effect |
|------|--------------|----------|--------|--------------|
| Sword | Weaponsmith (1) | 1 Iron | 1 | +2 attack, +2 defense |
| Crossbow | Weaponsmith (1) | 1 Wood | 1 | Ranged: 1 attack / 3 rounds |
| Longbow | Weaponsmith (1) | 1 Wood | 1 | Ranged: -1 attack, 0 defense |
| Javelin | Weaponsmith (1) | 1 Wood | 1 | Ranged: 1 attack / 2 rounds |
| Pike | Weaponsmith (2) | 1 Wood | 1 | +2 attack, +2 defense |
| Pick | Weaponsmith (1) | 1 Iron | 1 | +1 atk/def; +1 iron/stone production |
| Spear | Weaponsmith (1) | 1 Wood | 1 | +1 atk/def; +1 fur production |
| Axe | Weaponsmith (1) | 1 Wood | 1 | +1 atk/def; +bonus wood production |
| Hammer | Weaponsmith (1) | 1 Iron | 1 | +1 atk/def; +bonus metal production |

### Armor

| Item | Skill (Level) | Material | Weight | Survival Chance |
|------|--------------|----------|--------|----------------|
| Leather Armor | Armorer (1) | 1 Fur | 1 | 30% (usable in assassination) |
| Chain Armor | Armorer (1) | 1 Iron | 1 | 33% |
| Plate Armor | Armorer (3) | 3 Iron | 3 | 67% |
| Wooden Shield | Armorer (1) | 1 Wood | 1 | Shield defense |
| Iron Shield | Armorer (3) | 1 Iron | 1 | Shield defense |

### Tools

| Item | Skill (Level) | Material | Weight | Effect |
|------|--------------|----------|--------|--------|
| Wagon | Carpenter (1) | 1 Wood | 50 | 200 capacity (with horse) |
| Net | Fishing (1) | 1 Herb | 1 | +2 fish production |
| Lasso | Herb Lore (1) | 1 Herb | 1 | +1 livestock/horses/camels |
| Bag | Herb Lore (1) | 1 Herb | 1 | +2 grain/herbs |
| Spinning Wheel | Carpenter (1) | 1 Wood | 1 | +2 nets/lassos/bags/leather armor |
| Meal | Cooking (1) | grain/livestock/fish | 1 | Food item |

### TAKE Order
```
take from <unit_id> <amount> [unfinished] <item>
take from <unit_id> all [unfinished] <item> [except <amount>]
take from <unit_id> all <category>
```
- Takes items from another unit (the `from` keyword is mandatory)
- Supports `unfinished` keyword for partially built items
- `except <amount>` keeps N items when taking all
- Same item categories as GIVE (see below)

### EXCHANGE Order
```
exchange <unit_id> <give_amount> <give_item> <expect_amount> <expect_item>
```
- Simultaneous item exchange between two units
- **Both units must issue matching EXCHANGE orders** for it to succeed
- Ships cannot be exchanged
- Processed at phase 8 in turn sequence (after GIVE/TAKE)

### SACRIFICE Order
```
sacrifice <amount> <item>
```
- Sacrifices items at a sacrifice-enabled structure in the same region
- Processed at phase 21 in turn sequence

### Building (BUILD Order)
```
build                           ; continue building current structure
build <object_type> [complete]  ; start building a new structure
build help <unit_id>            ; assist another unit's build
build complete                  ; continue building, auto-repeat next turn until done
```
- Month-long order requiring Building or Shipbuilding skill
- `complete` flag makes the order repeat automatically until the structure is finished
- `help` lets a unit contribute labor to another unit's build project
- Any faction can issue BUILD orders (no Martial restriction)

### Advanced Items
Highly skilled units can produce advanced items (mithril weapons, enchanted gear, etc.). These are **discovered through gameplay** - when a unit reaches sufficient skill, the report describes what can be produced.

### PRODUCE Syntax
```
produce [amount] <item>
```
- Optional `amount` caps production to that many items
- If the amount cannot be completed in one month, the order **carries over to subsequent months** automatically
- Higher skill = more output. Level 2 produces 2x what level 1 does
- Multi-month items benefit from skill but take longer

**Important: Only Martial factions can issue PRODUCE orders**, regardless of skill levels. Any faction can issue BUILD orders (for buildings and ships).

## Villages, Towns, and Cities

Settlements grow through trade:

| Settlement | Growth Mechanic |
|-----------|----------------|
| **Village** | Increased wages, population, tax income. Demands grain, livestock, fish |
| **Town** | Village that grew enough. Demands additional goods, sells new items |
| **City** | Grown town. Expanded markets, exclusive **trade items** with high profit margins |

**Trade items** exist only in cities - no practical use except commerce for profit.

### NAME Order for Settlements
```
name village|town|city <name>
```
- Renaming a **village** requires owning a Tower in the region
- Renaming a **town** requires owning a Fort
- Renaming a **city** requires owning a Castle (may cost silver)

## Income Sources

### WORK (no skill needed)
- Earns silver at regional wage rate (shown in report)
- Modest income, last resort

### ENTERTAIN (requires Entertainment skill)
- Level 1 earns **30 silver** per person per month
- Higher levels earn proportionally more
- Limited by regional entertainment demand
- Generally lower than tax income

### TAX (requires Martial faction points)
- Month-long order requiring combat-capable units:
  - Combat skill >= 1, OR
  - Weapon with appropriate skill, OR
  - Mount with riding skill, OR
  - Mage with damage spell
- Each taxer collects **$50**
- If taxers > available income, it splits evenly
- Region description shows available tax amount
- **Guard** units block unfriendly faction taxation

### PILLAGE (requires Martial faction points)
- Collects **double** available tax money
- Requires enough combat-ready personnel to tax half the region's income
- **Severely damages** regional economy (slow recovery)
- Guard units always block pillaging regardless of attitude

## Quartermaster Transportation

Requires Martial faction points and Quartermaster skill (leaders only).

### Setup
- Quartermaster must own a **Caravanserai** structure
- Single-person leader units only

### Range
- Accept/deliver items within **2 hexes**
- Transport to other quartermasters up to **3 hexes** (increases with skill)

### Cost
- **5 silver per weight unit** transported (higher cost at lower skill)

### Restrictions
Cannot transport: men, summoned creatures, ships, mounts, war machines, or artifact-created items.

Transport counts as **trade activity** in the hex. Target must be at least FRIENDLY.

### Syntax
```
transport <unit_id> <amount|all> <item> [except <value>]
distribute <unit_id> <amount|all> <item> [except <value>]
```
- `DISTRIBUTE` is an alias for `TRANSPORT` (same meaning and syntax, kept for historical reasons)
- `except <value>` keeps that many items when sending all
