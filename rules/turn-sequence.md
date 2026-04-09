# Turn Sequence

[< Non-Player Units](non-player-units.md) | [Back to Index](README.md) | [Tables >](tables.md)

## Instant Pre-Sequence Processing

Before the main sequence, these are processed during **order parsing**:
- `FORM` / `END` (create new units)
- Flag orders: `GUARD`, `AVOID`, `BEHIND`, `HOLD`, `NOAID`, `SHARE`, `AUTOTAX`, `NOCROSS`
- `NAME`, `DESCRIBE`
- `CLAIM` (silver from unclaimed pool)
- `SHOW`
- `CONSUME`, `REVEAL`, `SPOILS`
- `COMBAT`, `PREPARE`, `WEAPON`, `ARMOR`
- `OPTION`, `PASSWORD`, `ADDRESS`, `DECLARE`, `FACTION`

## Main Sequence

Orders execute in this fixed order each turn:

| Phase | Orders | Type |
|-------|--------|------|
| 1 | `FIND` | Instant |
| 2 | `ENTER` / `LEAVE` (initial) | Instant |
| 3 | `PROMOTE` / `EVICT` | Instant |
| 4 | `ATTACK` (player-initiated, then auto-attacks) | Instant |
| 5 | `STEAL` / `ASSASSINATE` | Special |
| 6 | `GIVE` / `TAKE` | Instant |
| 7 | `ENTER` (into newly created objects) | Instant |
| 8 | `EXCHANGE` | Instant |
| 9 | `DESTROY` | Instant |
| 10 | `PILLAGE` | Month-long |
| 11 | `TAX` | Month-long |
| 12 | `GUARD 1` (guard activation) | Instant |
| 13 | `CAST` (magic) | Special (not month-long) |
| 14 | `SELL` | Instant |
| 15 | `BUY` | Instant |
| 16 | `FORGET` | Instant |
| 17 | Mid-turn processing | System |
| 18 | `QUIT` | Faction |
| 19 | Remove empty units | System |
| 20 | `WITHDRAW` | Instant |
| 21 | `SACRIFICE` | Instant |
| 22 | `MOVE` / `ADVANCE` / `SAIL` — by speed phases | Month-long |
| 23 | Sink uncrewed fleets, drown units | System |
| 24 | `TEACH` | Month-long |
| 25 | Month-long orders: `STUDY`, `PRODUCE`, `BUILD`, `WORK`, `ENTERTAIN` | Month-long |
| 26 | Economics processing | System |
| 27 | Teleport (`CAST` teleportation) | Special (not month-long) |
| 28 | `TRANSPORT` / `DISTRIBUTE` | Instant |
| 29 | `ANNIHILATE` | Special |
| 30 | Maintenance assessment | System |
| 31 | Post-turn processing | System |

## Key Timing Implications

### Early Phase (1-6)
- Enter structures before attacks happen
- Promote/evict before combat
- Attacks resolve before item transfers
- Give/take happens after combat

### Mid Phase (7-16)
- Exchange after give/take
- Destroy structures after exchanges
- Pillage and tax before selling/buying
- Guard activates after tax (can't guard and tax same turn)
- Cast spells after guard activation
- Sell before buy (get silver first)

### Late Phase (17-31)
- Movement happens AFTER most other orders
- Teaching happens after movement (teacher and student must end up in same region)
- Study/produce/build happen after movement and teaching
- Teleportation happens after normal movement
- Maintenance is assessed last (ensure units have silver before end of turn)

## Mutual Exclusivity Rules

### Month-Long Orders (overwrite each other)
`MOVE`, `ADVANCE`, `SAIL`, `STUDY`, `TEACH`, `PRODUCE`, `BUILD`, `WORK`, `ENTERTAIN`, `IDLE`, `TAX`*, `PILLAGE`*

TAX and PILLAGE are month-long orders.

### Additive Orders (multiple of same type merge)
- `MOVE` + `MOVE` → directions appended
- `ADVANCE` + `ADVANCE` → directions appended
- `SAIL` + `SAIL` → directions appended
- `TEACH` + `TEACH` → students merged
- `BUY` + `BUY` (same item) → amounts merged
- `SELL` + `SELL` (same item) → amounts merged
- `ATTACK` + `ATTACK` → targets accumulated

### Cross-Overwrite
- `MOVE` and `ADVANCE` overwrite each other (but not themselves)
- `STEAL` and `ASSASSINATE` overwrite each other (separate from month-long track)
