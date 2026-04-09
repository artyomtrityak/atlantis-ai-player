---
name: Always include all orders for every unit
description: The @ prefix on orders does NOT carry over between turns — every unit must have explicit orders every turn
type: feedback
---

Every unit must have explicit orders in every turn's orders file. The `@` prefix does NOT persist across turn submissions.

**Why:** Orders files are standalone per turn. The engine only sees what's in the current file. A unit with no orders in the file will do nothing, even if previous turns had `@`-prefixed repeating orders.

**How to apply:** When generating orders, never skip a unit assuming its repeating orders carry over. Always write out all orders (including `@GUARD`, `@TAX`, etc.) for every unit in every turn's orders file.
