---
name: orders-maker
description:  Use when creating, modifying, or understanding turn orders for the Atlantis PBEM game. Covers all order syntax, parameters. ALWAYS use this skill when generating orders files, writing unit commands, planning turn actions, checking if orders are valid, or discussing what orders a unit should issue — even if the user just says "make orders" or "what should unit X do".
---

# Turn Orders Skill

This skill provides comprehensive reference material for the Atlantis PBEM game engine's turn order system.

## Order of execution

- Generate new orders using Order generation workflow below.
- Validate orders using Validation checkist below before submitting.

## Order generation workflow

- Read the report/game state in the current turn (todo: link to report parsing skill and provide details how to load current turn report)
- Identify what each unit can do
- Generate orders

## Common pitfalls

- Month-long mutual exclusivity is the #1 source of invalid orders - only 1 month order per unit.
- MOVE and ADVANCE overwrite each other.
- GIVE is executed before BUY.

## Validation checkist

- Make sure that syntax is correct - use .claude/skills/orders-maker/orders-reference.md to check exact syntax for each order
- Make sure that orders are valid for the unit (e.g. can't CAST if the unit doesn't have the spell, can't MOVE if overloaded, etc)
- Check syntax for each order, no guessing

## Sub-files

- @orders-reference.md — Complete orders syntax reference (all order types, parameters, execution order, mutual exclusivity). Load first when creating orders or to understand order interactions.
- @order-examples.md — Real-world order patterns and usage examples from game data. Load when creating orders for inspiration or to see how specific orders are used in practice.

## Quick Overview

Each game turn follows this cycle:
1. Players submit text order files (starting with `#atlantis`, ending with `#end`)
2. The engine validates orders (producing `orders-checked` files)
3. Orders execute in a fixed sequence (see orders-reference.md for full execution order)
4. Reports are generated per faction (JSON + text format)
5. An order template is included in the report for the next turn

Key concepts:
- **Month-long orders** are mutually exclusive (MOVE, STUDY, PRODUCE, BUILD, WORK, ENTERTAIN, IDLE, TEACH)
- **Instant orders** execute during parsing or specific phases and can coexist with month-long orders
- **FORM/END** blocks create new units; **TURN/ENDTURN** blocks delay orders to future turns
- The `@` prefix makes any order repeat automatically on subsequent turns
- CAST spells have varied sub-syntaxes depending on the spell type
- A unit CAN both CAST and STUDY in the same turn (CAST has its own execution phase)