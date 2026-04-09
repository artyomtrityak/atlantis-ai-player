# Skills & Races

[< Movement](movement.md) | [Back to Index](README.md) | [Economy >](economy.md)

## Skill System Overview

Characters are distinguished by their skills. Each skill has a **level** determining effectiveness - level 2 is twice as effective as level 1.

### Available Skills
Mining, Lumberjack, Quarrying, Hunting, Fishing, Herb Lore, Horse Training, Weaponsmith, Armorer, Carpenter, Building, Shipbuilding, Entertainment, Tactics, Combat, Riding, Crossbow, Longbow, Stealth, Observation, Healing, Sailing, Farming, Cooking, Quartermaster, Annihilation.

## Race Specializations

Each race can learn specialized skills to level 5 and non-specialized skills to level 2. Leaders can learn any skill to level 5.

| Race | Specialized Skills (max 5) |
|------|---------------------------|
| **Leaders** | All skills (max 5) |
| **Wood Elves** | Lumberjack, Longbow, Entertainment, Carpenter, Fishing, Cooking |
| **High Elves** | Horse Training, Fishing, Longbow, Shipbuilding, Sailing |
| **Ice Dwarves** | Combat, Weaponsmith, Mining, Fishing, Armorer |
| **Hill Dwarves** | Armorer, Weaponsmith, Quarrying, Mining, Building |
| **Under Dwarves** | Weaponsmith, Armorer, Quarrying, Mining, Building |
| **Orcs** | Mining, Lumberjack, Combat, Building, Shipbuilding |
| **Gnomes** | Herb Lore, Quarrying, Entertainment, Crossbow, Healing |
| **Centaurs** | Lumberjack, Horse Training, Riding, Healing, Farming |
| **Humans** | Building, Riding, Combat, Mining, Farming, Cooking (max **4**) |
| **Lizardmen** | Hunting, Herb Lore, Carpenter, Sailing, Healing |
| **Goblins** | Quarrying, Crossbow, Shipbuilding, Weaponsmith, Entertainment |
| **Gnolls** | Horse Training, Hunting, Combat, Armorer, Carpenter, Cooking |
| **Drow Elves** | Combat, Hunting, Longbow, Lumberjack, Cooking |

**Note**: Humans cap specialized skills at level 4 (not 5). All other races cap at 5.

### Multi-Race Units
Units containing multiple races gain **all weaknesses and no unique strengths** of constituent races. Avoid mixing races.

## Studying

### Training Time
Progression is cumulative:
- Level 1: 1 month
- Level 2: 1 + 2 = 3 months total
- Level 3: 1 + 2 + 3 = 6 months total
- Level 4: 1 + 2 + 3 + 4 = 10 months total
- Level 5: 1 + 2 + 3 + 4 + 5 = 15 months total

Training months need not be consecutive. Units can study intermittently.

### STUDY Syntax
```
study <skill> [level]
```
- The optional `level` parameter is used with the `@` repeat prefix to auto-stop at a target level
- Example: `@study combat 3` will study combat each turn until level 3 is reached, then stop

### Study Costs (per person per month, on top of maintenance)

| Skill Category | Cost |
|---------------|------|
| Standard skills | $10 |
| Stealth, Observation | $50 |
| Magic skills | $100 |
| Tactics | $200 |

### Practice
Units can advance through practice (using the skill) but this is much slower than formal study. Only applies to the first skill used per month.

### Magic Study Restriction
Studying magic above level 2 requires being inside a building with **mage slots**:
- Fort / Stockade: 1 mage
- Castle: 2 mages
- Citadel: 3 mages
- Tower: 0 mages (no magic study benefit)

Without mage facilities, magic study rate is **halved**.

## Teaching

- Only **leaders** can teach
- Teacher's skill level must **exceed** student's level
- Students learn at **double rate** when taught
- Each teacher can effectively teach **10 students** per month
- More than 10 students dilutes the bonus (e.g., 20 students = 1.5x rate instead of 2x)
- A single teacher can teach multiple skills simultaneously
- Target faction must declare you **Friendly** for teaching

### Teaching Formula
With T teachers (each at 10 student capacity) and S students:
- If S <= 10*T: students get 2 months of training
- If S > 10*T: students get (1 + 10*T/S) months of training

## Skill Reports

When a faction first achieves a new skill level, the report includes a description of capabilities unlocked.

### SHOW Order
```
show skill <skill> <level>
show item <item>
show object <object_type>
```
- Review previously received skill reports, item descriptions, or object info
- Maximum **100 SHOW requests** per faction per turn
- Faction must have prior knowledge of the requested skill/item
