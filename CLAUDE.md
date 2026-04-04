# CLAUDE.md

## Primary role

AI agent that plays Atlantis New Origins — a Play-by-Email fantasy strategy game where players submit text orders each turn and the engine processes them into reports. Work in progress.

The goal: parse game-generated reports → make strategic decisions → produce turn orders.

Pipeline: report parsing → game state analysis → strategy → order generation.

## Always do

- Validate everything you produce: orders, code, scripts, etc
- Write unittests for code you create or modify
- If you create or modify code, run unittest to make sure it works
- Prefer correctness over guessing

## Writing or executing code

- Main language is python version 3
- Always before writing, executing any python code or adding dependencies, activate virtual environment `source venv/bin/activate`
- Always use pytest when writing tests
- Always use `mypy <path to file> <arguments>` to check types after any code added or changed
- Use `pip freeze > requirements.txt` to save new dependencies. Always ask if you want to install new python libraries.

## Never do
- Don't guess when there is not enough information - clarify and ask questions

## Important paths

- `atlantis-core-engine/` - C/C++ core engine that runs the Atlantis game, only used for references
- `client-examples/` - C++ GUI client (Atlantis-Little-Helper) that parses reports and generates orders; read-only reference for game mechanics
- `game-examples/` - examples of multiple turns of the previously run Atlantis games

## Game data format

Each `game-examples/N/` folder represents a game instance with these files:
- `game.in` — game rules and setup configuration
- `players.in` / `players.out` — player configuration
- `report.N` — text-format turn report for faction N (canonical source of truth)
- `report.N.json` — JSON-format report for faction N
- `orders.N` — submitted orders for faction N
- `template.N` — order template for faction N
- `orders-checked.N` — validated orders

Text reports are canonical; JSON reports are new feature - might not have all data. 

## Skills and reference docs

- `.claude/skills/report-parser/` — Rules for report structure and report parsing. Has scripts to parse report and reference docs on report format.
- `.claude/skills/orders-maker/` — Rules for order generation; reference docs on order syntax and examples