# The World

[< Playing Atlantis](playing-atlantis.md) | [Back to Index](README.md) | [Movement >](movement.md)

## Regions

Atlantis is divided into **hexagonal regions**, each with a name, terrain type, and coordinates.

- Two units in the same region can interact (unless concealed)
- Units in different regions cannot interact (except adjacent combat)
- Six directions: north, northeast, southeast, south, southwest, northwest
- The hex grid has "holes" (e.g., region (1,2) does not exist due to hex geometry)

## Terrain Types

| Terrain | Properties |
|---------|-----------|
| Ocean | Water; ships can sail; ground units drown |
| Plain | Easy terrain; horses available |
| Forest | Difficult terrain (2 pts walk/ride); wood and fur |
| Mountain | Difficult terrain (2 pts walk/ride); iron and stone |
| Swamp | Difficult terrain (2 pts walk/ride); wood and herbs |
| Jungle | Difficult terrain (2 pts walk/ride); wood and herbs |
| Desert | Normal terrain; iron, stone, camels |
| Tundra | Difficult terrain (2 pts walk/ride); fur and herbs |
| Volcano | Special terrain; rich in minerals |

## Region Resources

Each terrain type produces specific harvestable resources (% = chance the resource exists in a given region):

| Terrain | Resources (probability) |
|---------|------------------------|
| Ocean | Fish (100%), Giant Turtle (30%) |
| Plain | Horse (100%), Winged Horse (20%) |
| Forest | Wood (100%), Fur (100%), Ironwood (20%), Yew (25%) |
| Mountain | Iron (100%), Stone (100%), Mithril (35%), Rootstone (35%), Adamantium (15%) |
| Swamp | Wood (100%), Floater Hide (40%), Herb (100%), Mushroom (30%) |
| Jungle | Wood (100%), Herb (100%), Mushroom (35%), Ironwood (35%), Fur (80%) |
| Desert | Iron (100%), Stone (100%), Rootstone (30%), Camel (80%), Mithril (20%) |
| Tundra | Fur (100%), Herb (100%), Mushroom (35%), Iron (30%) |
| Volcano | Stone (100%), Mithril (50%), Rootstone (50%), Adamantium (50%), Iron (100%) |

## Structures

Structures appear in regions as buildings or fleets.

- First unit to enter becomes **owner** (controls access)
- Units inside structures are visible and in the region
- Structures may provide **defensive bonuses** in combat
- Owner can `EVICT` other units or `PROMOTE` new owner
- Owner can `DESTROY` the structure (instant order, phase 9 in turn sequence)

### Defensive Buildings

| Type | Capacity | Cost | Material | Skill (Level) | Mage Slots |
|------|----------|------|----------|---------------|------------|
| Tower | 10 | 10 | Stone | Building (1) | 0 |
| Fort | 50 | 40 | Stone | Building (1) | 1 |
| Castle | 300 | 300 | Stone | Building (2) | 2 |
| Citadel | 1000 | 800 | Stone | Building (3) | 3 |
| Stockade | 50 | 60 | Wood | Building (1) | 1 |

- **Capacity** = max sheltered population
- **Cost** = man-months of labor AND material units required
- **Mage Slots** = allows mages to study magic above level 2 without penalty

### Trade Structures (Production Boosters)

| Structure | Cost | Material | Skill (Level) | Product Boosted |
|-----------|------|----------|---------------|----------------|
| Mine | 10 | Wood/Stone | Mining (3) | Iron |
| Farm | 10 | Wood/Stone | Farming (3) | Grain |
| Ranch | 10 | Wood/Stone | Farming (3) | Livestock |
| Timber Yard | 10 | Wood/Stone | Lumberjack (3) | Wood |
| Inn | 10 | Wood/Stone | Building (3) | Entertainment |
| Quarry | 10 | Wood/Stone | Quarrying (3) | Stone |
| Temple | 10 | Stone | Building (3) | Herbs |
| Trapping Hut | 10 | Wood/Stone | Hunting (3) | Furs |
| Stables | 10 | Wood/Stone | Horse Training (3) | Horses |
| Oasis | 10 | Wood/Stone | Horse Training (3) | Camels |

**Production bonus**: first structure adds **25%**, each additional adds half the previous bonus (diminishing returns).

### Roads

Roads are directional connections between hexes:

| Structure | Cost | Material | Skill (Level) |
|-----------|------|----------|---------------|
| Road (per direction) | 30 | Stone | Building (2) |
| Caravanserai | 20 | Wood/Stone | Building (2) |

- **Movement bonus**: halves movement cost (minimum 1 point); requires road in BOTH hexes (matching directions)
- **Economy bonus**: hex with roads to 2+ adjacent hexes gains +1 wage
- **Caravanserai**: enables quartermaster transport functionality

## Ships

Built with Shipbuilding skill and wood. See [Tables](tables.md) for full ship stats.

| Class | Capacity | Cost (wood) | Sailors Needed | Min Skill |
|-------|----------|-------------|---------------|-----------|
| Longship | 150 | 10 | 4 | 1 |
| Raft | 450 | 10 | 2 | 1 |
| Cog | 750 | 25 | 6 | 2 |
| Galleon | 2700 | 75 | 15 | 3 |

- Unfinished ships stay in builder's inventory; moving/sailing discards them
- Completed ships join builder's fleet or create a new one
- Fleet capacity and sailor requirements are cumulative
- Fleet speed = slowest ship's speed

## Atlantis Nexus

The starting region for all new factions.

- Isolated from the normal world
- Contains **portals** providing one-way transport to matching terrain types
- Portal destinations avoid occupied towns when possible
- **No return** to the Nexus once departed (advanced magic may offer alternatives)
- No products or marketplaces available
