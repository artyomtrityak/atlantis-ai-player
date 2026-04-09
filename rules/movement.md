# Movement

[< The World](the-world.md) | [Back to Index](README.md) | [Skills >](skills.md)

## Movement Points

| Mode | Points/Turn | Requirements |
|------|------------|-------------|
| Walking | 2 | Default mode |
| Riding | 4 | Horse capacity >= total weight of personnel + goods |
| Flying | 4 | Flying items/creatures carrying all weight |

Units automatically use their fastest available mode.

### NOCROSS Flag
```
nocross 1|0
```
Setting `nocross 1` prevents the unit from crossing water (even if it could fly or swim). Useful to prevent accidental drowning.

## Terrain Costs

| Terrain | Walk/Ride Cost | Fly Cost |
|---------|---------------|----------|
| Plain, Desert, Ocean* | 1 | 1 |
| Forest, Mountain, Swamp, Jungle, Tundra | 2 | 1 |

*Ocean only accessible by flying or sailing.

**Roads** halve movement cost (minimum 1). Requires matching roads in both origin and destination hexes.

## Normal Movement

### MOVE Order
- Unit moves through listed directions spending movement points
- **Stops** (does not fight) if blocked by hostile units
- Remaining moves queue for next turn with `@` prefix
- Cannot enter guarded regions of unfriendly factions

### ADVANCE Order
- Same as MOVE but **initiates combat** against blockers
- Overwrites any existing MOVE order (and vice versa)
- Losers retreat to previous region

### Carrying Capacity
- **Walking**: combined capacity of people + horses + wagons must cover all non-people items; horses must number >= wagons
- **Riding**: horse capacity must >= total weight of personnel and goods
- **Flying**: flying creature/item capacity must cover everything

### Key Weights
| Item | Weight | Capacity |
|------|--------|----------|
| Person (most races) | 10 | 5 |
| Horse/Camel | 50 | 20 |
| Wagon | 50 | 200 (with horse) |

### JOIN Order
```
join <unit_id> [nooverload|merge]
```
- Follows/joins the target unit (enters whatever building/fleet they're in)
- `nooverload` — prevents joining if it would overload a fleet
- `merge` — merges into the target unit (units combine)

### Structure Entry/Exit
- `ENTER` and `LEAVE` are instant (no movement point cost)
- `MOVE IN` traverses interior passages, costs normal terrain entry
- `LEAVE` at sea: if a unit can **swim or fly**, it can leave a fleet while at sea

## Sailing

Fleets move using the `SAIL` order (not MOVE/ADVANCE).

### Requirements
- Must be fleet owner to issue the primary SAIL with directions
- Total cargo weight <= fleet capacity
- Sufficient sailors with SAIL orders aboard
- Higher sailing skill = more effective per sailor
- **Non-owner units should also issue `SAIL`** to contribute their sailing skill to the fleet's total

### Fleet Movement
- Ships provide **4 movement points** per turn
- Can traverse: ocean-to-ocean, coastal-to-ocean, ocean-to-coastal
- Only compass directions and `pause` are valid for SAIL

### Sailing Restrictions
- A unit on board a fleet while it is sailing **may not MOVE** later in the turn, even if it doesn't issue SAIL — sailing consumes the whole month
- Non-sailing passengers may execute other month-long actions (STUDY, etc.) but not MOVE
- Units **may not remain on guard** while on board a sailing fleet — they must reissue `GUARD 1` after sailing

### Sailing Through Land
- Ships may **not** sail through single-hex land masses
- Must leave via the **same side they entered** or a side **adjacent** to that one
- Ships ending their movement in a land hex may sail out along any side connecting to water

### Fleets vs Guarded Regions
- Unlike land movement (where units are blocked from entering), fleets **enter the guarded region and then are stopped** by the guards

### Overloaded Fleets
- An overloaded fleet (cargo exceeds capacity) can **stay afloat but cannot move**
- Only movement is prevented; the fleet does not sink from overloading

### Drowning
- Flying units over ocean drown if movement ends over water
- Fleets that lose all sailors sink; occupants drown
- Units on sinking uncrewed fleets drown

## Order of Movement

Movement is processed **one hex at a time**, region by region. Atlantis cycles through all regions, finds units due to move, and moves them one hex per phase. Units' movement is spread out over **8 phases** proportionally to their speed.

| Speed | Ph 1 | Ph 2 | Ph 3 | Ph 4 | Ph 5 | Ph 6 | Ph 7 | Ph 8 |
|-------|------|------|------|------|------|------|------|------|
| 1 | x | | | | | | | |
| 2 | x | x | | | | | | |
| 3 | x | x | x | | | | | |
| 4 | x | x | x | x | | | | |
| 5 | x | x | x | x | x | | | |
| 6 | x | x | x | x | x | x | | |
| 7 | x | x | x | x | x | x | x | |
| 8 | x | x | x | x | x | x | x | x |

- A unit riding at speed 4 moves twice as often as one walking at speed 2
- Combat resolves after each movement phase
- Use `PAUSE` (or `P`) as a movement direction to spend one movement point waiting (useful to coordinate with slower companions)
- Movement points **carry over** from one month to another if a MOVE/ADVANCE command did not complete (e.g., a walking unit with 2 points trying to enter mountains costing 2 points will accumulate points across turns if blocked by insufficient points mid-route)
