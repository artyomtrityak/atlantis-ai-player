---
name: Maximize tax in every region
description: Always calculate men needed to max region tax (economy/$50), FORM secondary units instead of BUYing into existing ones (skill dilution), and invest unclaimed silver to scale garrisons
type: feedback
---

Always maximize tax extraction in every taxed region. Each man taxes $50/turn, capped at region economy (the dollar value in the region description line, e.g. "forest (8,12), 2172 peasants, $912" means $912 max tax).

**Why:** With 5 men ($250 tax) in a $912 region, we waste $662/turn. Scaling to 19 men costs ~$1,100 one-time but yields $912/turn — ROI under 2 turns. Leaving money on the table compounds into massive lost income over many turns.

**How to apply:**
1. For each taxed region, calculate: `ceil(economy / 50)` = men needed to max tax
2. NEVER BUY more men into an existing unit with COMB 1 — this dilutes the skill below level 1 (30 days), making the entire unit unable to tax
3. Instead, FORM a separate secondary unit (Cohors) in the same region: the new unit BUYs men, STUDYs COMB for 1 turn, then TAXes starting next turn
4. Budget: each new man costs BUY price + $10 study + $10 first-turn maintenance
5. Execution order matters: CLAIM (phase 3) → GIVE (phase 4) → TAX (phase 11) → BUY (phase 15). Garrisons must CLAIM enough to GIVE before TAX income arrives.
6. Prioritize cheapest races first (orcs/gnolls $37-38 > elves $40 > centaurs $68-76) for best ROI
7. When forming new garrison via scout, buy enough men to max the region from the start if budget allows
