# Faction 75 Strategy Analysis

## Section 1: Observed Playstyle (Turns 1–76+)

### Starting Conditions

**Faction name:** Sea Guild (75)  
**Faction type:** Martial 1, Magic 1  
**Starting unit:** Unit (1092) — a single leader [LEAD]  
**Location:** nexus (0,0,nexus) in The Void (the Atlantis starting hub)  
**Starting silver (unclaimed):** 10,500 silver at turn 2  
**Starting skills (Turn 2):**
- observation [OBSE] 1 (35 XP)
- force [FORC] 1 (30 XP)
- pattern [PATT] 1 (30 XP)
- spirit [SPIR] 1 (30 XP)
- gate lore [GATE] 1 (30 XP)
- fire [FIRE] 1 (30 XP)
- combat [COMB] 3 (180 XP)

This is a Martial 1, Magic 1 faction. The starting mage has all three magical foundations (FORC, PATT, SPIR) at level 1, plus GATE, FIRE, OBSE, and an unusually high COMB 3. The faction began with 1 mage and capacity for 2 mages, 3 apprentices.

**Default attitude:** Neutral (Creatures set Unfriendly throughout all observed turns)

---

### Economic Strategy

Sea Guild pursued an extremely unusual and passive economic strategy: it never left the Nexus during the observed game period (76+ turns). All economic activity was minimal survival-mode spending.

**Income sources:**
- `CLAIM` from unclaimed treasury: 100 silver per turn when needed to fund study (drawn from the 10,500 initial pool)
- Periodic Times (newspaper) rewards: 200 silver (turns 12, 14, 15, 19, 20, 23, 25, 27, 29, 31, 32, 35, 36 and beyond)
- Unit (1092) also accumulated carried silver starting around turn 55: had 1,850 silver on hand (turn 55), growing to 2,300 silver by turn 76

**Expenses:**
- Unit maintenance: 50 silver/turn (1 leader)
- Magic study: 100 silver/turn when studying

**Treasury trajectory:**
- Turn 2: 10,500 unclaimed silver
- Turn 3: 10,350 (claimed 100, studied PATT, paid maintenance)
- Turn 7: 9,850 (slow drain from study + maintenance)
- Turn 12: 9,500 (Times reward brought it back up slightly)
- Turn 17: 9,250 (stagnant — no study this turn)
- Turn 20: 9,200 (PATT 3 achieved)
- Turn 25: 9,150 (error: not enough funds to study FORC — player forgot to CLAIM first)
- Turn 36: 9,800 (two Times rewards received)
- Turn 50: 10,500 (fully recovered — unclaimed pool rebuilt, unit carrying 2,000+ silver by turn 55–76)

**Key observation:** The player never taxed, never traded, never produced anything. They relied entirely on the starting 10,500 silver treasury + small unclaimed claims + newspaper rewards. By turn 36, unclaimed silver was back near starting levels due to Times rewards accumulating over time. The player was burning through the treasury slowly but the Times rewards partially offset the drain.

**Silver efficiency errors:**
- Turn 25: `STUDY: Not enough funds` — forgot to CLAIM before STUDY. This recurs at turns 28, 30, 33, 34, 40.
- The player sometimes forgot to include `claim 100` in orders, causing wasted turns.

---

### Military Strategy

**Zero military activity across 76+ turns.**

Unit (1092) was permanently positioned in the Nexus with `behind` flag. No combat was recorded, no units recruited, no attacks made. The faction never expanded out of the Nexus.

The unit had COMB 3 at game start — a significant martial investment — but it was never used. The player's Martial 1 faction type limits them to 1 leader plus potentially more martial units, but none were ever recruited.

**Diplomacy/threat response:** None. All attitudes were left at neutral (Creatures unfriendly). No ALLY, FRIENDLY, or HOSTILE declarations were ever made.

---

### Magic Development

Magic development is the entirety of this faction's activity. The single mage (Unit 1092) studied continuously throughout 76+ turns in the Nexus.

**Skill progression (by turn of achievement):**

| Skill | Level | Turn Achieved | Notes |
|-------|-------|---------------|-------|
| FORC | 1 | Start (T2) | Starting skill |
| PATT | 1 | Start (T2) | Starting skill |
| SPIR | 1 | Start (T2) | Starting skill |
| GATE | 1 | Start (T2) | Starting skill |
| FIRE | 1 | Start (T2) | Starting skill |
| COMB | 3 | Start (T2) | Starting skill — highest starting level |
| OBSE | 1 | Start (T2) | Starting skill |
| PATT | 2 | T3–T4 | First study action: studied PATT at T3 |
| SPIR | 2 | T7 | After 2 turns studying SPIR (T6–T7) |
| SPIR | 2 (deep) | T13–T18 | Extensive SPIR study at halved rate (above level 2 outside building) |
| PATT | 3 | T20 | After returning to PATT study (T14–T20) |
| FORC | 3 | T35 | Studied FORC for approximately 10 turns (T23–T35) |
| SPIR | 3 | T39 | Studied SPIR again (T38–T39) |
| GATE | 2 | T43 | Started GATE study at T42 |
| GATE | 3 | T49 | GATE fully leveled |
| ARTI | 1 | T50 | Artifact Lore unlocked after FORC/PATT/SPIR all at 3 |
| ARTI | 2 | T52 | Unlocks CGAT, ESWO, EARM, ESHD, CRGC |
| CGAT | 1 | T53 | Construct Gate learned |
| CGAT | 2 | T55 | Construct Gate 2 (40% success chance) |
| ARTI | 3 | T65 | Artifact Lore maxed |

**Warning recurring throughout:** "Magic study rate outside of a building cut in half above level 2." This means studying FORC, PATT, SPIR beyond level 2 in the Nexus (not inside a tower/mage building) is done at half speed. The player accepted this penalty and never built or entered a tower.

**Skill study order analysis:**
- Turns 3–4: PATT (to 2)
- Turns 6–7: SPIR (to 2) — switched away before reaching 3
- Turns 10–13: SPIR (halved rate above 2)
- Turn 14 pivot: switched to PATT
- Turns 14–20: PATT (to 3)
- Turns 18–20: PATT (to 3, confirmed T20)
- Turns 23–35: FORC (to 3)
- Turns 38–39: SPIR (to 3)
- Turns 42–49: GATE (to 3)
- Turns 50–52: ARTI (to 2)
- Turns 53–55: CGAT (to 2)
- Turns 56+: ARTI (to 3, continuing)

**Final skill state (Turn 76):**
- OBSE 1, FORC 3, PATT 3, SPIR 3, GATE 3, FIRE 1, COMB 3, ARTI 3, CGAT 2

**Unlocked spells by Turn 76:** fire, earthquake, force shield, energy shield, spirit shield, magical healing, farsight, mind reading, weather lore, earth lore, necromancy, demon lore, illusion, construct gate, enchant swords, enchant armor, enchant shields, create gate crystal, transmutation

---

### Expansion Pattern

**No expansion occurred across 76+ turns.**

Faction status showed "Regions: 0 (10)" every single report from turn 2 through turn 76. The faction had capacity for 10 regions but never claimed any. The single mage unit never left the Nexus. All 7 terrain gateways (plain, forest, mountain, swamp, jungle, desert, tundra) remained available but were never entered.

**Turning point that never came:** A Gate (Gate 557) appeared in the Nexus by turn 60 (January Year 6). This gave the mage a potential exit route via CAST Gate_Lore, but even this was not used through turn 76.

**Inactivity warnings:** By turn 75 (April Year 7), the game engine issued "WARNING: You have 2 turns until your faction is automatically removed due to inactivity!" By turn 76, the warning read "1 turns until automatic removal." The faction was approaching auto-deletion — evidence of a player who was playing in a very minimal/absentee manner.

---

### Turn-by-Turn Summary

**Phase 1: Mage Foundation (Turns 2–20)**

- Turn 2 (March Y1): First report. Single mage in Nexus, 10,500 silver. No orders submitted yet — unit did nothing.
- Turn 3 (April Y1): First active turn. Claimed 100, studied PATT. PATT rises to 1 (60 XP).
- Turn 4 (May Y1): Claimed 100, studied PATT. PATT reaches 2 (90 XP).
- Turn 5 (June Y1): No orders submitted (blank turn). Paid maintenance only.
- Turn 6 (July Y1): Claimed 100, studied SPIR. SPIR rises to 1 (60 XP).
- Turn 7 (Aug Y1): Claimed 100, studied SPIR. SPIR reaches 2 (90 XP).
- Turn 8 (Sep Y1): Blank orders — no study this turn. Maintenance only.
- Turn 9 (Oct Y1): Blank orders — no study this turn. Maintenance only.
- Turn 10 (Nov Y1): Claimed 100, studied SPIR. Triggered half-rate warning (above level 2 outside building). SPIR at 105 XP.
- Turn 11 (Dec Y1): Claimed 100, studied SPIR. SPIR at 120 XP.
- Turn 12 (Jan Y2): Times reward 200. Claimed 100, studied SPIR. SPIR at 135 XP.
- Turn 13 (Feb Y2): Claimed 100, studied SPIR. SPIR at 150 XP — still in level 2 (needs 180 for level 3 but studying at half rate).
- Turn 14 (Mar Y2): Pivoted to PATT. Claimed 100, studied PATT. Times reward 200.
- Turn 15 (Apr Y2): Claimed 100, studied PATT. Times reward 200. PATT at 120 XP.
- Turn 16 (May Y2): Claimed 100, studied PATT. PATT at 135 XP.
- Turn 17 (Jun Y2): Blank orders — no study. Maintenance only.
- Turn 18 (Jul Y2): Claimed 100, studied PATT. PATT at 150 XP.
- Turn 19 (Aug Y2): Claimed 100, studied PATT. Times reward 200. PATT at 165 XP.
- Turn 20 (Sep Y2): Claimed 100, studied PATT. Times reward 200. PATT achieves level 3 (180 XP).

**Phase 2: Force Development (Turns 21–39)**

- Turns 21–22: No study (blank orders). Maintenance only. FORC not yet started.
- Turn 23 (Dec Y2): Claimed 100, studied FORC. Introduced `@TURN/@ENDTURN` template blocks. FORC at 60 XP.
- Turn 24 (Jan Y3): Claimed 100, studied FORC. FORC reaches level 2.
- Turn 25 (Feb Y3): Error — `STUDY: Not enough funds`. Player forgot to claim properly. FORC stagnant.
- Turn 26 (Mar Y3): Claimed 100, studied FORC. FORC at 105 XP.
- Turn 27 (Apr Y3): Claimed 100, studied FORC. Times reward 200. FORC at 120 XP.
- Turn 28 (May Y3): Error — not enough funds. Times reward 200 came but study failed again. FORC at 120 XP.
- Turn 29 (Jun Y3): Claimed 100, studied FORC. Times reward 200. FORC at 135 XP.
- Turn 30 (Jul Y3): Error — not enough funds. No study. FORC stagnant.
- Turn 31 (Aug Y3): Claimed 100, studied FORC. Times reward 200. FORC at 150 XP.
- Turn 32 (Sep Y3): Claimed 100, studied FORC. Times reward 200. FORC at 165 XP.
- Turn 33 (Oct Y3): Error — not enough funds. Times reward 200 received. FORC stagnant.
- Turn 34 (Nov Y3): Error — not enough funds. FORC stagnant.
- Turn 35 (Dec Y3): Claimed 100, studied FORC. Times reward 200. FORC achieves level 3 (180 XP).
- Turn 36 (Jan Y4): Error — not enough funds. Two Times rewards (400 silver). FORC stagnant.
- Turn 37: Orders file exists but no report (likely turn 37 report is missing). Switched to SPIR.
- Turn 38 (Mar Y4): Claimed 100, studied SPIR. SPIR at 165 XP.
- Turn 39 (Apr Y4): Claimed 100, studied SPIR. SPIR achieves level 3 (180 XP).

**Phase 3: Gate Lore Development (Turns 40–49)**

- Turn 40 (May Y4): Error — not enough funds. Player had orders to study SPIR but SPIR already at 3? Actually studying SPIR still (uncapped). No study happened.
- Turns 41–42: Orders show `study SPIR` then switch to `study GATE` at T42.
- Turn 42 (Jul Y4): Claimed 100, studied GATE. Two Times rewards 400. GATE reaches level 1 (60 XP).
- Turn 43 (Aug Y4): Claimed 100, studied GATE. GATE achieves level 2 (90 XP). Gate lore 2 skill report received.
- Turns 44–49: Continuous GATE study. Times rewards bolstering funds.
- Turn 45 (Oct Y4): GATE 2 (120 XP). Unclaimed treasury climbed back to 10,250.
- Turn 49 (Feb Y5): GATE achieves level 3 (180 XP). Unclaimed silver at 10,450.

**Phase 4: Artifact Lore and Construct Gate (Turns 50–65+)**

- Turn 50 (Mar Y5): Switched to ARTI. Studied artifact lore. ARTI 1 achieved. Unclaimed silver 10,500.
- Turn 51: Continued ARTI study.
- Turn 52 (May Y5): ARTI achieves level 2. Unlocks CGAT, ESWO, EARM, ESHD, CRGC, TRNS.
- Turn 53 (Jun Y5): Pivoted immediately to CGAT. CGAT 1 achieved. Construct Gate 1 = 20% success chance.
- Turn 55 (Aug Y5): CGAT reaches level 2 (40% success chance). Unit is now carrying 1,850 silver personally. Unclaimed pool 8,700.
- Turn 56–59: Continued ARTI study (returned to ARTI after CGAT 2).
- Turn 60 (Jan Y6): Gate 557 appears in the Nexus. ARTI at 2 (170 XP). Unclaimed 7,000. Unit carries 1,600 silver.
- Turn 65 (Jun Y6): ARTI achieves level 3 (185 XP). Error: "STUDY: Doesn't have the pre-requisite skills to study that" — attempted a skill requiring more prerequisites. Unclaimed 7,100.
- Turns 66–76: Continued studying — likely CGAT or higher tier skills, but hitting prerequisite walls.
- Turn 70 (Nov Y6): Error — same prerequisite failure. Unclaimed 6,800. Unit carries 2,000 silver.
- Turn 75 (Apr Y7): Inactivity warning (2 turns). Skills frozen at ARTI 3, CGAT 2.
- Turn 76 (May Y7): Final inactivity warning (1 turn). Regions utterly annihilated in the world — end-of-game events visible. Auto-removal imminent.

---

### Strengths & Weaknesses

**Strengths:**

1. **Extremely deep magic investment**: By turn 76, the mage has FORC 3, PATT 3, SPIR 3, GATE 3, ARTI 3, CGAT 2, COMB 3. This is an exceptionally powerful foundational mage with gate construction capability, enchanting capability (swords, armor, shields), transmutation access, and full magical school coverage.

2. **Silver preservation**: Starting with 10,500 silver, the faction only spent 50 silver/turn maintenance + 100 silver when studying. The drain was slow. Times rewards partially offset expenses. By turn 50+, the unclaimed pool was still above 10,000 silver in many turns. The mage also accumulated personal silver (2,000+ by turn 70).

3. **Low risk**: No military exposure. No territorial expansion meant no conflicts, no losses.

4. **Times rewards**: Collected many 200-silver Times rewards across the game — at least 15+ visible in 76 turns, contributing 3,000+ total silver.

5. **Gate 557 in Nexus**: A gate appeared in the Nexus, giving the mage ability to teleport directly to a specific location anywhere in the world when they finally choose to enter.

**Weaknesses:**

1. **Never entered the world**: 76 turns and zero regions controlled. The faction has no economy, no income, no territory, no army. The entire strategy is conceptually a "mage preparation" phase that never resolved into actual play.

2. **Repeated "not enough funds" errors**: Turns 25, 28, 30, 33, 34, 40, 65, 70 all showed failed study attempts. The player's order management was sloppy — they sometimes forgot to include `claim 100` before `study`, or ran out of monthly unclaimed silver because the TURN/ENDTURN blocks didn't re-claim properly.

3. **Wasted turns**: Turns 5, 8, 9, 17, 21, 22 had blank or near-blank orders — the mage did nothing. That's at least 6 full turns of lost study progress, potentially 6 additional skill levels or 600 silver-worth of development.

4. **Studying SPIR above level 2 outside a building**: Turns 10–20 were spent studying SPIR at half rate due to not being in a mage tower. The player could have built or entered a building to double the study speed. This likely cost 4–5 turns of progress across FORC, PATT, SPIR.

5. **Inactivity deletion**: By turn 75–76, the engine is about to auto-remove the faction. The player was barely submitting orders and the faction never activated.

6. **No recruitment, no military, no expansion**: Faction had capacity for 10 regions and 2 mages, but used none of it. While the mage became extremely powerful, it can be destroyed by any military force that finds it alone.

7. **STUDY prerequisite errors (Turns 65, 70, 75, 76)**: Attempted to study skills they lacked prerequisites for. Suggests the player was copy-pasting old orders without updating them for the current skill state.

---

## Section 2: AI Agent Strategy (Based on This Playstyle)

### What the AI Would Keep

1. **The core magic investment plan**: Reaching FORC 3, PATT 3, SPIR 3 as the foundation for high-level magic is sound. These three skills together unlock the most powerful spells and artifact creation. The AI should pursue this same trio.

2. **Gate Lore 3 as a strategic priority**: Reaching GATE 3 enables carrying 500 weight through a specific gate — meaning the mage can transport a small army. This is essential for faction mobility if entering the world late.

3. **Artifact Lore leading to Construct Gate**: The ARTI → CGAT path is correct if the faction intends to build gates in controlled territory for economic or military use. CGAT 2 gives 40% success per attempt.

4. **Claiming silver conservatively from treasury**: The nexus + unclaimed silver model is valid for early-game magic study if the player plans to enter the world with a powerful mage.

5. **Times rewards as supplemental income**: Submitting to the Times (if available) is worth doing. Collect as many 200-silver rewards as possible.

### What the AI Would Change

1. **Enter the world far earlier**: Staying in the Nexus for 76 turns was strategically disastrous. By turn 10–12, the mage had PATT 2 and SPIR 2 — enough to survive in an early region. The AI should enter no later than turn 8–10, choosing the gateway most appropriate for the faction's race and goals (forest, mountain, or plain are typically productive). Entering early allows tax income, territory control, and gate building.

2. **Build a Tower or Mage Tower before studying above level 2**: The game explicitly warns that study above level 2 is halved outside a building. As soon as the mage enters the world and controls a region, the first economic priority should be constructing a Tower (or Mage Tower) so that FORC/PATT/SPIR 3 study runs at full speed. This alone could save 10–15 turns of study time.

3. **Recruit additional units early**: The faction had Martial 1 — allowing additional combat units. Even 3–5 heavy infantry would allow taxing, protecting the mage, and clearing monster lairs. The unclaimed silver pool (10,500) was more than enough to recruit 5–10 units in early turns.

4. **Use CLAIM reliably every turn**: The repeated "not enough funds" errors (turns 25, 28, 30, 33, 34, 40) are unacceptable for an AI agent. The AI should always calculate whether sufficient silver is on hand before issuing STUDY, and always include a CLAIM if needed. Better: have the mage hold 500+ personal silver buffer.

5. **Never submit blank orders**: Turns 5, 8, 9, 17, 21, 22 were wasted. The AI should always have a valid STUDY order queued.

6. **Develop an economy**: With 10 region slots and 2 mage slots, the faction should establish tax income and production by turn 5–8. Even 3 regions taxing $100/turn = $300/month, covering all expenses and enabling faster unit recruitment.

7. **Correct skill transition timing**: The faction studied SPIR to 2, stopped, studied other skills, then came back to SPIR later. While this may have been intentional, it caused suboptimal XP distribution. The AI should plan the full PATT → FORC → SPIR → (all to 3) sequence, committing to one skill at a time and finishing it.

8. **Avoid prerequisite errors**: Turns 65, 70, 75, 76 all failed with "doesn't have prerequisite skills." The AI must always verify the Can Study list from the current report before issuing STUDY orders.

### Recommended Opening (Turns 1–5)

**Turn 1 (Nexus — before first report)**:
- Submit basic orders: `claim 100` + `study PATT` (claim from treasury, study the weaker starting skill first)
- Choose the gateway to enter: forest [2] or plain [1] are good starting regions for expansion

**Turn 2 (Nexus, first report received)**:
- Unit 1092: `claim 100`, `study PATT`
- Scout the available gateways' inner locations — the faction needs to know what resources are available before committing

**Turn 3 (Nexus)**:
- Unit 1092: `claim 100`, `study PATT` — push to PATT 2 immediately
- FORM a second unit using treasury silver: recruit 3–5 leaders or soldiers using FORM + BUY if possible in Nexus (though Nexus has no market, this waits until exiting)

**Turn 4 (Nexus)**:
- Unit 1092: `claim 100`, `study PATT` — PATT 2 achieved
- Unit 1092: `ENTER [gateway to forest or plain]` — exit Nexus this turn
- Note: once you leave, you cannot return. Choose a gateway with good terrain. Plain [1] or forest [2] are recommended.

**Turn 5 (First Region)**:
- Unit 1092 is now in the world
- Immediately: `CLAIM` silver, `TAX` the region if possible, `STUDY FORC` (push foundation skills)
- FORM new unit: recruit cheap labor for future taxing/production
- Assess region — what does it produce, what are wages, are there monsters?

*Alternative if the mage needs more skills before entering:*
- Delay entry until turn 6–7, pushing PATT to 2 and SPIR to 2 first, then enter with a stronger skill base. This is safer if monsters in available regions are dangerous.

### Mid-Game Plan (Turns 6–15)

**Strategic goals:**
1. Control 3–5 regions for steady tax income
2. Build a Tower or Mage Tower in the mage's home region (costs 200–1000 silver depending on structure type)
3. Complete the FORC → PATT → SPIR all-to-3 sequence using the building bonus
4. Recruit a military escort of 5–10 combat-capable units
5. Begin GATE study at turn 10–12 once all three foundations are at 3

**Priority skill sequence (in a building):**
- Turn 5–7: PATT to 3 (already started, finish it)
- Turn 8–11: FORC to 3 (requires PATT 2, have it)
- Turn 12–14: SPIR to 3 (may already be at 2 from early study)
- Turn 15+: GATE to 3 then ARTI to 2 then CGAT to unlock gates

**Economy:**
- Tax income from 3–5 regions: target $300–$600/month by turn 10
- Sell or produce items via production workers if region has resources
- Keep the mage's silver reserves above 500 at all times

**Military:**
- 5–10 infantry with swords/armor for region clearing
- Position the mage behind the army (`behind` flag) for safety
- Clear monster-controlled regions before claiming them

### Adaptations for Dynamic Conditions

**If the chosen gateway region is monster-heavy:**
- Delay entry by 1–2 turns, study SPIR to 2 for spirit shield defense
- Enter with a 5-unit guard recruited via FORM (split silver from treasury before exiting)

**If another faction is already in the target region:**
- Try a different gateway. The 7 gateways offer significant choice. Forest and plain are often contested; mountain and swamp are sometimes neglected.
- Declare Friendly/Ally immediately to avoid accidental combat

**If treasury runs low:**
- Prioritize TAX over STUDY for 1–2 turns
- The mage can work (WORK) if wages are positive, though this conflicts with STUDY

**If the mage cannot study above level 2 (no building):**
- Build a Tower immediately. The formula is `BUILD TOWER` and costs 10 wood + stone depending on rules.
- Accept the halved rate for 1–2 turns while building, then resume full-speed study

**If CGAT fails repeatedly (20–40% per attempt):**
- The mage needs CGAT 3 (60%) or higher for reliable gate construction
- Budget multiple attempts: at 40%, expect ~2.5 attempts on average per gate placement
- Each attempt costs 1,000 silver; budget 3,000 silver per gate

**If the faction falls behind militarily:**
- Use GATE 3 to rapidly reposition: teleport through Gate 557 (the nexus gate) or any known gate
- Gate lore can be a powerful surprise attack or retreat mechanism
- ARTI 3 + ESWO/EARM/ESHD allows enchanting weapons for military units, dramatically boosting their effectiveness

**If inactivity warnings appear:**
- This should never happen for an AI agent, but if it does: submit any valid order set immediately. The warning threshold is approximately 3 turns of no submitted orders.
