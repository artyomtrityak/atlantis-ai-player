# Playing Atlantis

[< Back to Index](README.md) | [The World >](the-world.md)

## Factions

A faction is a player's position in the game, identified by a name and number.

### Faction Composition
- Factions consist of multiple **units** (groups of people)
- Start with **1 unit** containing a single leader and **10,000 silver** unclaimed
- Faction is destroyed only when ALL units are eliminated
- The starting character holds no special status

### Faction Points

Each faction receives **5 Faction Points** split between Martial and Magic:

| Points | Martial: Tax/Trade Regions | Martial: Quartermasters | Magic: Mages | Magic: Apprentices |
|--------|---------------------------|------------------------|--------------|-------------------|
| 0 | 0 | 0 | 1 | 1 |
| 1 | 10 | 2 | 2 | 3 |
| 2 | 25 | 5 | 3 | 5 |
| 3 | 40 | 9 | 4 | 7 |
| 4 | 60 | 14 | 5 | 10 |
| 5 | 90 | 25 | 6 | 15 |

- **Martial points** control: regions you can tax/pillage, trade activity (production), and quartermasters
- **Magic points** control: maximum mages and apprentices
- Faction type is changeable each turn via the `FACTION` order
- New factions start with 1 Martial, 1 Magic, 2 unspent points

### Unclaimed Funds
- 10,000 silver starting pool accessible by all units
- Cannot be lost in battle
- Access via `CLAIM` (silver) or `WITHDRAW` (goods)

### Faction-Level Orders

| Order | Syntax | Effect |
|-------|--------|--------|
| `PASSWORD` | `password [new_password]` | Sets or clears faction password. No argument clears to "none" |
| `OPTION` | `option times\|notimes` | Toggle timestamps in report |
| | `option showattitudes\|dontshowattitudes` | Toggle attitude display |
| | `option template off\|short\|long\|map` | Set order template format |
| `FACTION` | `faction <type1> <pts1> [type2] [pts2] ...` | Reallocate faction points |
| `ADDRESS` | `address <new_address>` | Change faction email |
| `FIND` | `find <faction_number>` or `find all` | Request email of another faction |
| `QUIT` | `quit [password]` | Permanently remove faction. Requires password if set |
| `RESTART` | `restart [password]` | Remove faction and create new one with same email/password |

## Units

A unit groups people of the same faction sharing skills, items, and orders.

### Key Properties
- All members occupy the same location
- All members share the same skills and execute the same orders
- The game tracks units, not individuals
- To send members different places, you must split the unit

### Leaders vs Normal People
- **Leaders**: special individuals, can learn any skill to level 5, cost more to recruit/maintain (50 silver/month)
- **Normal people**: race-specific, can learn specialized skills to level 5, others to level 2, cost 10 silver/month
- Leaders and normal people **cannot mix** in the same unit
- Units with multiple races function at the **least common denominator** (all weaknesses, no unique strengths)

### Unit Merging and Splitting
- When units merge, skills average (training months tracked to prevent loss)
- When units split, training months distribute evenly

## Turns

Each turn = **1 game month**. The server processes orders and distributes reports.

### Action Types

**Instant orders** (take no time):
- Buying, selling, giving items, attacking, flag changes, naming, describing

**Month-long orders** (consume the entire month - only ONE per unit):
- `MOVE`, `ADVANCE`, `SAIL`, `STUDY`, `TEACH`, `PRODUCE`, `BUILD`, `WORK`, `ENTERTAIN`, `TAX`, `PILLAGE`, `IDLE`

A unit issues exactly **one** month-long order per turn, plus any number of instant orders.

### Delayed Orders (TURN/ENDTURN)

You can queue orders for future turns using `TURN`/`ENDTURN` blocks:

```
turn
  ; these orders execute next turn
  move n n
endturn
```

- Can be **nested** to delay multiple turns (each `TURN`/`ENDTURN` layer adds one turn of delay)
- `FORM` blocks can appear inside `TURN` blocks
- Useful for planning multi-turn sequences in advance

### Order File Structure

Orders are submitted as text files with this structure:

```
#atlantis <faction_number> [password]

unit <unit_id>
  ; comments start with semicolon
  move n n
  @study combat    ; @ prefix = repeat this order every turn automatically

unit <unit_id>
  work

form <alias>
  ; orders for newly created unit
  name unit "New Scout"
  buy 1 leader
end

#end
```

- `#atlantis <number> [password]` — opens faction order block; password required if set
- `#end` — closes faction order block
- `unit <number>` — selects unit for subsequent orders
- Lines starting with `;` are comments
- **`@` prefix** on any order makes it repeat automatically each turn (e.g., `@study combat 3` will auto-study until level 3)

### Unit ID Formats

| Format | Example | Usage |
|--------|---------|-------|
| `<number>` | `1234` | Existing unit by number |
| `new <alias>` | `new 1` | Unit created by FORM in same turn |
| `faction <fac> new <alias>` | `faction 5 new 1` | Another faction's newly formed unit |
| `0` | `0` | Discard target (for GIVE 0) |

### FORM/END — Creating New Units

```
form <alias>
  ; orders for the new unit
end
```

- Alias must be a **positive integer**, unique per region per faction
- The new unit **inherits flags** from the forming unit
- FORM blocks can appear inside TURN/ENDTURN blocks
- Processed during order parsing (before the main sequence)

### Turn Processing
Orders execute in a fixed sequence each turn - see [Turn Sequence](turn-sequence.md) for the complete order.
