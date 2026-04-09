---
name: Silver management — use taxed silver first, CLAIM is last resort
description: Always fund study/hiring from on-hand (taxed) silver via GIVE chains; CLAIM from unclaimed pool only when genuinely necessary
type: feedback
---

Always use on-hand (taxed) silver first. CLAIM from the unclaimed pool only as a last resort.

**Why:** CLAIM drains the unclaimed pool unnecessarily. Garrison units collect tax silver every turn (sitting on units), which should flow to mage study units and new formations via GIVE orders. Claiming on top of this depletes the faction's emergency reserve and creates confusion about true financial health.

**How to apply:**

## 1. Check silver on units BEFORE claiming

Before writing CLAIM for any unit, check:
- How much silver does this unit already have on hand?
- What are the expected tax receipts for garrison units this turn?
- Can a nearby garrison unit GIVE silver to cover the need?

**Example:** If Gravewatch has 805 silver and Seraphel needs 150 for study+maintenance, Gravewatch should GIVE 150 to Seraphel — not Seraphel CLAIM 150.

## 2. Silver flow pattern: Tax unit → GIVE → Recipient

Standard chain:
```
unit <taxer>
@GUARD 1
@TAX
@GIVE <mage_or_new_unit> <amount> SILV   ; Give taxed silver to mages/study units
```

Taxers collect $50/man/turn from TAX. Pass the surplus to study units and new formations in the same region.

## 3. Regions with mages: garrison funds the mages

If mages are in the same region as a garrison (e.g., Taso), the garrison unit GIVES silver to the mages each turn:

```
unit 178   ; Gravewatch — 5 goblins = $250 tax
@GUARD 1
@TAX
@GIVE 142 100 SILV   ; Fund Seraphel's study ($100)
@GIVE 200 100 SILV   ; Fund Kael's study
@GIVE 201 100 SILV   ; Fund Morrith's study
@GIVE 202 100 SILV   ; Fund Valdris's study
```

Mages then have NO CLAIM order — they're funded by the garrison.

## 4. CLAIM is only valid when:

- Unit is isolated (no nearby garrison to GIVE to it)
- Unit is a scout passing through with no tax income
- Forming a new unit in a region where the local garrison doesn't have enough silver yet
- The unclaimed pool is large (>3,000) AND you've verified on-hand silver is truly insufficient

Even then, CLAIM only the minimum needed: study cost + maintenance, minus what's already on hand.

## 5. New unit formation — fund from parent's on-hand silver

When forming a new garrison unit, calculate if the parent unit can GIVE silver to fund the new unit rather than CLAIMING inside the FORM block:

```
unit <parent_garrison>  ; Has 500 silver after tax
@GUARD 1
@TAX
FORM <n>
  NAME UNIT "New Unit"
  GIVE UNIT <n> 400 SILV   ; Parent gives from its own silver to the new unit
  BUY 10 GNOM
  STUDY COMB
  TURN
    @GUARD 1
    @TAX
  ENDTURN
END
```

Only add CLAIM inside FORM if the parent's on-hand silver is genuinely insufficient.

## 6. Quartermasters (TRANSPORT) for cross-region silver flow

When silver needs to travel across multiple regions, use Quartermasters (QUAR faction type allows 2 quartermasters):

```
unit <taxer_region_A>
@TAX
@TRANSPORT <quartermaster> ALL SILV except 120   ; Keep 120 for maintenance, send rest

unit <quartermaster>          ; In central location
; Receives silver from remote regions
; Delivers to study region via TRANSPORT
@TRANSPORT <mage_region_unit> 500 SILV
```

Quartermasters enable a hub-and-spoke model: distant garrisons funnel silver to a central QM who delivers to the main mage study base.

## 7. Track silver carefully each turn

Before writing orders, calculate:

| Category | Amount |
|----------|--------|
| On-hand silver (all units combined) | +X |
| Expected TAX income this turn | +Y |
| Expected STUDY costs | -A |
| Expected MAINTENANCE costs | -B |
| Expected BUY costs (new hires) | -C |
| **Net this turn** | X+Y-A-B-C |

If net is positive → NO CLAIM needed, use GIVE chains from taxers.
If net is negative → Claim only the shortfall, not more.

## 8. When garrisons accumulate excess silver

Garrisons that can't be taxed (city guard blocks) still need maintenance. Don't have them CLAIM — instead let the silver accumulate naturally from previous turns, or have other units GIVE to them if they're running low.

## 9. Specific faction 4 silver routes

Current setup: Mages (142, 200, 201, 202) are all at Taso (30,8) with Gravewatch (178, 5 goblins, @TAX) and Taso Cohors (220, 8 goblins, @TAX). Combined tax = ~$650/turn.

Mage costs per turn: 4 × ($100 study + $50 maint) = $600/turn.
Garrison maintenance: 5+8 = 13 goblins × $10 = $130/turn.
Total Taso expenses: $730/turn. Tax income: $650/turn. Shortfall: ~$80/turn.

This $80 shortfall CAN be covered by claiming, or by bringing silver from other garrisons via quartermaster. Once Kael/Morrith/Valdris finish their prerequisites and no longer need $100/month study, the balance improves.

**Rule:** Always check if the local garrison's on-hand silver covers expenses before adding CLAIM orders.
