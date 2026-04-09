# Report Format & Tips

[< Tables](tables.md) | [Back to Index](README.md)

## Report Format

Turn reports contain standardized information organized by region.

### Region Header
Each region block shows:
- **Terrain type**, name, and coordinates
- **Population**: peasant race and count
- **Taxable income** and available tax amount
- **Wage rates** and maximum earnings
- **Available recruits** by race
- **Items for sale** and **items wanted** (market)
- **Entertainment demand**
- **Producible resources** with amounts
- **Directional exits** for all six hex directions

### Unit Markers
- `*` (asterisk) — your own units
- `-` (dash) — other factions' units
- `+` (plus) — units inside structures/objects

### Visibility
- **Large items** (buildings, fleets, etc.) are always visible in region descriptions
- **Small items** carried by units are only visible if the unit is seen
- Faction identification requires sufficient Observation skill (see [Stealth](stealth.md))

### Orders Template
The `OPTION TEMPLATE` setting controls what order template is appended to your report:
- `off` — no template
- `short` — unit numbers only
- `long` — unit numbers with existing orders
- `map` — includes ASCII map of known regions

## Hints for New Players

### Getting Started
- New factions begin in the **Atlantis Nexus** with 1 leader and 10,000 unclaimed silver
- Use portals to enter the main world — choose terrain matching your strategy
- Once you leave the Nexus, you **cannot return**

### Money Management
- Maintain a **cash reserve** — running out of silver means starvation (33% death chance per unpaid person per month)
- `WORK` is the easiest income but pays poorly
- `ENTERTAIN` pays better but needs the Entertainment skill
- `TAX` is the best regular income but requires Martial points and combat-ready units

### Unit Strategy
- Form **specialized units** for different tasks: military, production, mages, scouts
- Leaders are expensive but versatile (can learn any skill to level 5)
- Don't mix races in a unit — you get all weaknesses and no unique strengths

### Economic Growth
- Build **trade structures** (mines, farms, etc.) to boost regional production by 25%
- Grow villages into towns and cities by selling demanded goods
- Cities offer exclusive trade items with high profit margins

### Military
- Build armies gradually — don't rush into combat unprepared
- **Tactics skill** gives a significant round-1 advantage
- Equip units with weapons and armor before fighting
- Healing skill + herbs can recover casualties after winning

### Orders
- Submit orders **early** — late orders mean your units do nothing
- Use the `@` prefix for standing orders that repeat each turn
- Use `TURN`/`ENDTURN` blocks to plan multi-turn sequences
- Always check your report for errors and warnings after each turn
