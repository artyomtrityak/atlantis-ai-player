---
name: Silver reserve buffer and transfer chains
description: Always keep 500+ unclaimed silver; set up QM or silver-runner routes early
type: feedback
---

Always keep at least **500 silver unclaimed** in the faction pool as an emergency reserve. Do not spend the pool down to zero or near-zero even if the math works out on paper.

**Why:** Unexpected expenses arise every turn — units failing to earn income, price fluctuations on BUY orders, new tactical needs. Running the pool to $20-60 (as happened in turn 7) leaves no room for error and forces starvation or abandoned plans.

**How to apply:**
- When budgeting CLAIMs for a turn, cap total planned claims at `(unclaimed pool − 500)`.
- If needed, reduce or defer new FORM units rather than drain the buffer.
- As early as possible, establish a **silver transfer chain** so on-hand silver from wealthy garrison units flows to where it's needed:
  - **Option A — Quartermaster route:** Designate one unit per hub as a Quartermaster (QM). Use `TRANSPORT`/`DISTRIBUTE` to move silver from taxing regions to the base or mage locations. Costs a faction QM slot (have 2 allowed).
  - **Option B — Silver runner unit:** FORM a single 1-man unit (cheapest available race) whose sole job is to carry silver from a wealthy garrison toward mages/new units. Use GIVE + MOVE each turn to relay silver. No QM slot cost.
- Once the transfer chain is active, mages can stop CLAIMing from the pool (use on-hand silver instead), preserving the unclaimed reserve.
