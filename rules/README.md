# Atlantis: New Origins - Rules Wiki

> Complete rules reference for Atlantis New Origins v8.0.0 PBEM strategy game.
> Source: https://atlantis-pbem.com/rules

## Quick Reference

| Topic | Summary |
|-------|---------|
| [Playing Atlantis](playing-atlantis.md) | Factions, units, turns - how the game works |
| [The World](the-world.md) | Regions, terrain types, structures, the Nexus |
| [Movement](movement.md) | Walking, riding, flying, sailing mechanics |
| [Skills & Races](skills.md) | Skill system, studying, teaching, race specializations |
| [Economy](economy.md) | Maintenance, recruiting, items, production, income, trade |
| [Combat](combat.md) | Attitudes, attacking, battle mechanics, victory |
| [Stealth & Observation](stealth.md) | Hiding, stealing, assassination |
| [Magic](magic.md) | Foundations, spells, combat magic, apprentices |
| [Non-Player Units](non-player-units.md) | Guardsmen, wandering monsters, controlled monsters |
| [Turn Sequence](turn-sequence.md) | Complete order of event processing each turn |
| [Tables](tables.md) | Consolidated reference tables (items, buildings, ships, races) |
| [Report Format & Tips](report-and-tips.md) | How to read reports, hints for new players |

## Key Concepts Summary

- **Factions** have 5 points split between Martial and Magic categories
- **Units** are groups of people sharing skills, items, and orders
- **Turns** = 1 game month; each unit gets 1 month-long order + unlimited instant orders
- **Movement**: walk (2 pts), ride/fly (4 pts); terrain costs 1-2 pts
- **Economy**: maintenance is 10 silver/person, 50/leader; food substitutes at 30:1
- **Combat**: 50% base hit chance, modified by skill difference; armor gives survival %
- **Magic**: 3 foundations (force, pattern, spirit); spells discovered through play
- **Stealth**: hide from units with lower Observation; steal/assassinate with 1-man units

## For AI Order Generation

When generating orders, cross-reference:
- [Turn Sequence](turn-sequence.md) for execution order (critical for timing)
- [Economy](economy.md) for production/income calculations
- [Tables](tables.md) for item stats, building costs, ship capacities
- [Skills & Races](skills.md) for what each race can learn
- Orders syntax is documented in `.claude/skills/orders-maker/orders-reference.md`
