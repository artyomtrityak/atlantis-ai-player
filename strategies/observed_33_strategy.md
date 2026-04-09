# Faction 33 Strategy Analysis

## Section 1: Observed Playstyle (Turns 1–20)

### Starting Conditions

- **Faction name**: Greywolf (33)
- **Faction type**: Martial 1, Magic 4 (one combat unit slot, four mage slots)
- **Starting location**: plain (17,57) in Siaghhath, contains Mesengoa [town] — a major centaur town with 7271 peasants and $5962 income
- **Starting units** (Turn 1 report / Turn 2 orders):
  - Grey (887): leader, the head mage. Skills at start: observation 1, force 1, pattern 1, spirit 1, gate lore 1, fire 1, combat 3. Combat spell: fire.
  - Matt (1389), Timothy (1390), Charles (1391), Wilfred (1392): 4 newly formed leaders (apprentice mages), each starting with force 1 (60 exp).
  - Taxer (1393): 6 centaurs, combat 1 — the initial combat/tax unit.
  - 6 scout centaurs (1394–1399): sent in all 6 directions from Mesengoa in turn 1.
  - Otello (1400): newly formed leader studying tactics.
- **Starting silver**: unclaimed 4,719 silver at turn 2 start (after spending on unit formation, leaders, and mage study in turn 1).
- **Starting diplomacy**: Unfriendly to Creatures (2), everything else neutral. By turn 3 declared Friendly to Brutals (50), Archon Dominion (53), The Gaggle (22); Ally to Guardsmen (1).
- **Neighbors at start**: Brutals (50) also running centaur scouts; The Gaggle (22) with wood elves; Wistful Thinking (27) active in the Feltiuckfex city to the south.

### Economic Strategy

Faction 33 pursued an aggressive, multi-pillar economic strategy that can be broken into three phases:

**Phase 1 (Turns 1–3): Foundation — Tax, Claim, Study**

- All units start with CLAIM orders funded by unclaimed silver (pre-positioned silver from the nexus phase). Grey uses `WITHDRAW 1 MEAL` each turn to cover mage maintenance costs (leaders cost 20 silver but meals cover 30).
- In turn 1 orders, Grey forms 12 new units from nexus: 4 mage leaders, 1 centaur tax unit, 6 centaur scouts, 1 Otello (tactics). Each newly formed unit uses `CLAIM` to pull their buy silver directly.
- By turn 3 (April), two TAX operations begin: Taxer (1393) with 12 centaurs moves to plain (17,55) and taxes $599; Taxer (1967) with 9 humans taxes $448. Taxer (1968) with 18 high elves taxes $876 in plain (18,56).
- Total taxable income by turn 4 (May): ~$2,386 from three regions.

**Phase 2 (Turns 4–8): Rapid Tax Expansion**

- Each taxing unit becomes a "seeder" for the next: when taxing, they also use `GIVE NEW X [silver]` to fund newly formed buying units that expand to adjacent regions.
- By turn 5 (June), they have taxers in: jungle (19,49), jungle (15,53), plain (19,53), plain (18,54), plain (17,55), plain (18,56), plain (19,57), desert (19,59). That is 8 regions being taxed.
- Turn 5 events show total tax collection: taxer 2342 $150, taxer 1394 $150, Taxer 1967 $447, Taxer 1393 $597, taxer 1968 $892, taxer 2344 $150 = ~$2,386/turn from 6 regions.
- Turn 6 (July): Taxers 1967 and 1393 **PILLAGE** (17,55), extracting $893 and $1,191 (total $2,084 from one region in one turn), then shift their region base. Pillaging is used selectively when moving on, not as the primary income strategy.
- By turn 7 (August): taxers in town Mesengoa ($3,250 alone), plus all satellite regions. Total tax revenue visible in turn 10 report: $50 + $400 + $550 + $300 + $131 + $900 + $3,250 + $600 + $50 + $280 = **$6,511 in a single turn**.
- The faction used "runner" units to move silver from taxers to the mage cluster and study units. Turn 5 shows runner (2662) carrying silver to mages, runner (2664) moving to desert for fishing setup.

**Phase 3 (Turns 9–20): Systematic Exploitation and Production Diversification**

- Tax income grows steadily as more centaurs/high-elves/humans are added to taxer units each turn. By turn 10, Taxer (3274) alone collects $3,250 from Mesengoa.
- By turn 16 (May Year 2): Mesengoa Guard (3738) collects $3,850 and taxer (4299) collects $3,950 from the same town — two separate tax units in one town.
- Treasury silver in reports: turn 4 = 1,537 silver; turn 5 = 1,640; turn 6 = 4,040; turn 7 = 4,358; turn 9 = 4,535; turn 10 = 5,931; turn 11 = 9,931; turn 12 = 13,831; turn 13 = 16,439; turn 15 = 23,629; turn 16 = 27,211; turn 17 = 33,832; turn 18 = 37,342; turn 19 = 44,496; turn 20 = 50,177. **Silver grows roughly 10–20% per turn.**
- Production units established by turn 11–15: lumberjacks (centaurs then orcs), farmers (humans), miners (humans, then orc-based), horse trainers (centaurs), fishing (high elves), herb lore (gnomes), entertainment (Otello and others).
- Lumberjack (1969) starts turn 3 with 3 centaurs studying lumberjack. By turn 11 (December Year 1), Lumberjack (3963) is producing ironwood (IRWD) — a high-value trade resource.
- Farmer (2663) starts turn 4 with 3 humans studying farming, producing livestock.
- Horse (2343) starts turn 4 as a 1-centaur horse training unit; by turn 9 giving horses to mages.
- Diplomat/Entertainer (2345) is a single goblin in Trasicy city, working or entertaining from turn 3 onward.

**Key economic levers (in priority order observed):**
1. TAX from large centaur and high-elf populations (most efficient)
2. PILLAGE selectively when vacating regions
3. PHANTASMAL ENTERTAINMENT (mages): generates ~$437–$527/cast by turns 8–17 per mage, escalating as ILLU/PHEN/FORC advance
4. Production: ironwood, livestock, horses, herbs, axes, picks

### Military Strategy

**Alliance: Joined forces with Brutals (50) for the city assault**

The most important military action in turns 1–20 was the assault on Mesengoa's City Guard (Turn 7, August Year 1):

- The One (904), Brutals faction leader, attacks City Guard (43) — 80 leaders + 80 swords — with a combined Brutals+Greywolf force.
- Greywolf contributed: Grey (887), Matt (1389), Timothy (1390), Charles (1391), Wilfred (1392) as mages casting fire; Otello (1400) with tactics 1; Lumberjack (1969) and farmers/runners as melee mass; Taxer (1393) 12 centaurs + Taxer (1967) 9 humans.
- The Brutals contributed: The One (904) with combat 3 + fire, The Two (1538), Three (1539), Four (1540) also casting fire; Siaghhath Gnolls (2079) 40 gnolls; Siaghhath Centaurs (1537) 39 centaurs; plus Brutal Raiders.
- Result: Round 1, mages killed 61 out of 80 guards via fireballs. Guard routed, free round cleared survivors. **City captured in 1 round.** Greywolf lost 22 units (primarily gnolls from Brutal side). Greywolf mages took no casualties (all behind + avoid).
- The city attack was pre-planned: Charles (1391) issued `attack 43` order in turn 6; other units moved to Mesengoa from surrounding regions.
- After capture: Mesengoa provides massive tax income. By turn 17, Mesengoa Guards (3738) is given to Greywolf (presumably city guard token), and taxer (4299) collects $3,950 from the town.

**Post-city military posture:**
- Greywolf is essentially non-aggressive after the city assault. All taxers have `guard 1` but no further city attacks in turns 8–20.
- Turn 19 (Aug Year 2): Charles (1391) attacks Hydra (712) in a jungle with allied Archon Dominion mages. This appears to be a joint monster hunt, not territorial expansion.
- Turn 20 (Sep Year 2): A Pride of Lions attacks Greywolf's Horse (6288) group in plain (18,54). The lions survive several rounds before being killed by sheer numbers. Demonstrates vulnerability: unarmed farmer/horse-training units in the same region as dangerous monsters.
- **No player vs player military aggression by Greywolf** is visible in turns 1–20.

**Military composition (by turn 10):**
- 48 centaurs across multiple taxer units (each group 3–12)
- Mage squad of 5 leaders (Grey + 4 apprentices) with fire combat spells
- Otello (1400): tactics + observation (not a combat mage, more a support role)
- No dedicated armored infantry; taxers rely on numbers and mage support

### Magic Development

Faction 33's magic investment is the defining strategic choice of the game. With Magic 4 faction type, they can field up to 5 mages (cap reached turn 1).

**Grey (887) — Head Mage:**
- Turn 1: observation 1, force 1, pattern 1, spirit 1, gate lore 1, fire 1, combat 3
- Teaches force to Matt/Timothy/Charles/Wilfred in turns 1–2
- Turn 3 orders: teaches fire to Matt/Timothy/Charles/Wilfred (all 4 simultaneously while studying pattern himself)
- Turn 4: studies pattern (teaching others)
- Turn 5: studies force (with Wilfred teaching Grey)
- Turn 6: studies earth lore — begins CAST EARTH_LORE orders (`@cast EART`)
- Turn 7: studies illusion
- Turn 8: studies spirit
- Turn 9: studies spirit (continuing)
- By turn 15: Grey gives horses to all mages (mounted mages for mobility)
- By turn 16+: Grey is casting earth lore in Mesengoa for passive silver income (~29 silver/turn — modest but zero-cost)

**Matt (1389), Timothy (1390) — Identical parallel path:**
- Turn 1: force 1
- Turn 2: force 1 + fire 1 (taught by Grey)
- Turn 3: fire → pattern (taught by Grey)
- Turn 4: pattern → force 2 (taught by Wilfred)
- Turn 5: force 2 → fire again
- Turn 6: fire → illusion (Charles diverges here)
- Turn 7: phen (Phantasmal Entertainment level 1)
- Turn 8: patt (continuing pattern advance)
- Turn 9: @cast PHEN (Matt/Timothy casting phantasmal entertainment each turn, generating ~$437/cast)
- By turn 17: each casting PHEN for ~$527 per mage per month
- **Matt and Timothy become the primary income mages.**

**Charles (1391) — Diverged slightly:**
- Turn 1: force 1
- Turn 2: force 1 + fire 1
- Turn 3: fire + pattern
- Turn 4: illusion 1 (diverged to study illusion while others study force)
- Turn 5: illusion 1, studying force
- Turn 6: phen (phantasmal entertainment)
- Turn 7: studying force more, casting PHEN
- Turn 8+: casting PHEN and growing pattern/illusion
- By turn 14 (Mar Year 2): Creates Phantasmal Demons (PHDE spell), generating actual demon units used in monster combat

**Wilfred (1392) — The Defender:**
- Turn 1: force 2 (advanced faster due to initial orders)
- Turn 2: fire 1 + force 2
- Turn 3: studies force more
- Turn 4: teaches force to Grey/Matt/Timothy
- Turn 5: studies energy shield (ESHI) — combat spell set to ESHI from turn 6 onward
- Turn 6: energy shield as combat spell
- By turn 15+: Wilfred transferred to Archon Dominion (53) as an ally — "gives unit to Archon Dominion." This is a diplomatic gesture, giving a trained mage to the allied faction.

**Otello (1400) — Support/Non-combat:**
- Turn 1: tactics 1
- Turn 2: observation 1 (taught by Grey)
- Turn 3: observation 2
- Turn 4: observation 2
- Turn 5: entertainment 1
- Turn 6: observation 3
- Turn 7: stealth (stea) — renamed to Cpt Estelle by turn 19
- Otello never becomes a combat mage; instead maxes observation and stealth. This is a spy/scout support role.

**Magic income timeline:**
- Turn 8: Charles casts PHEN for $436
- Turn 9: Matt $437, Timothy $437, Charles $437 = $1,311 from 3 mages per turn
- Turn 17: each casting PHEN for $527 = $1,581 from 3 mages per turn (Grey does EART instead)
- By turn 19: mages are moving to hunt a Hydra with 12 demons combined (allied with Archon Dominion)

**Teaching chain efficiency:**
- Grey teaches up to 4 students simultaneously (his teaching slots)
- Wilfred teaches Grey and 2 others when Grey is learning force
- This parallelizes skill acquisition: 4 mages study the same path simultaneously at 30-day rate
- Key error: Turn 3 report shows "COMBAT: Unit does not possess that skill" for Matt/Timothy/Charles/Wilfred — they tried to set combat spell to fire before having fire skill. Fixed next turn.
- Turn 9: teaching errors (Timothy trying to teach units not studying) — scheduling conflicts when mages diverge.

### Expansion Pattern

**Scouting (Turns 1–2):**
- 6 centaur scouts deployed from Mesengoa in all 6 directions on turn 1
- Scouts are `avoiding`, `behind`, `weightless battle spoils`, revealing faction
- Scouts continue moving outward each turn: by turn 3 they have explored Ginspan jungle (NE coast), Tinscillar jungle (W), Prucda plain (SW), Feltiuckfex desert (S — city Trasicy), Siaghhath plains in all directions
- Scout 1396 enters underworld shaft at plain (18,54) by turn 5 — active underworld exploration

**Controlled regions:**
- Turn 4: Regions: 2 (first taxed regions)
- Turn 5: Regions: 5
- Turn 6: Regions: 7
- Turn 7: Regions: 8
- Turn 8: Regions: 6 (dropped — city guard captured/count changed?)
- Turn 9: Regions: 9
- Turn 10: Regions: 9
- Turn 11: Regions: 9
- Turn 12: Regions: 9
- Turn 13: Regions: 10 (at cap for Martial 1, Magic 4 type)
- Turn 14: Regions: 10
- **Turn 16: Regions: 13** — faction type changed to Martial 2, Magic 3 (reallocated points)
- Turn 17: Regions: 15
- Turn 18: Regions: 17
- Turn 19: Regions: 18
- Turn 20: Regions: 20

The expansion from 10 to 20 regions in turns 13–20 coincides with the faction type reallocation to Martial 2 (25 region cap instead of 10).

**Geographic expansion footprint by turn 10:**
- Northern: jungle (19,47), jungle (19,49) Ginspan — gnome populations
- Central-north: jungle (15,53) Dernglen — orc populations
- Central cluster: plains (19,53), (18,54), (17,55), (18,56), (17,57 town), (19,57) — high elves, humans, centaurs
- Desert: (19,59) Phadtouy — humans + camel/iron/stone production
- Underworld: chasm (9,27), cavern (10,28), (11,29) — goblin populations
- Diplomatic observation post: desert (15,63) Trasicy city (Diplomat unit)

### Turn-by-Turn Summary

**Turn 1 (January Year 1) — Setup:**
- Orders: Grey enters city, sets `option template short`, reveals faction, sets combat fire. All options established: `avoid 1`, `share 1`, `reveal faction`, `consume faction`.
- Forms 12 new units: 4 mage leaders (Matt/Timothy/Charles/Wilfred), Taxer (centaurs), 6 centaur scouts (sent N, NE, S, SW, plus extended paths), Otello (tactics).
- Key first move: all scouts buy centaurs (`buy 1 ctau`) in Mesengoa then move. This gives them immediate mount for 4-hex/month movement.
- FACTION order sets Martial 1, Magic 4 allocation.

**Turn 2 (February Year 1) — Teaching begins:**
- Grey teaches force to Matt/Timothy/Charles/Wilfred simultaneously (four taught, Grey gets 5-day practice)
- Grey also teaches combat to Taxer (1393)
- Taxer moves north to (17,55), scouts continue exploration
- First diplomacy: declares friendly to Brutals (50), Archon Dominion (53), The Gaggle (22); Ally to Guardsmen (1)
- Grey studies fire, mages study force

**Turn 3 (March Year 1) — Fire teaching:**
- Grey teaches fire to Matt/Timothy/Charles/Wilfred (all 4 again)
- New lumberjack unit (3 centaurs) formed from Mesengoa
- Otello studies observation (switches from tactics focus)
- New taxer units formed at (19,53), (18,56), (19,57) — pushing tax expansion
- Scout 1396 blocked from entering E'e forest by Gaggle faction (border dispute)
- Scout 1399 reaches Trasicy (goblin city, Feltiuckfex) — spots Wistful Thinking already there

**Turn 4 (April Year 1) — Tax era begins:**
- Taxer (1393) and Taxer (1967) set to `guard 1` + `@tax` in (17,55)
- Taxer (1968) taxes (18,56)
- Matt/Timothy/Charles study pattern (taught by Grey)
- Wilfred studies force 2 (ahead of others)
- Wilfred teaches Grey/Matt/Timothy force in turn 4 orders
- First "Runner" units formed to carry silver between regions
- Diplomat (goblin) formed in Trasicy — intelligence/diplomacy outpost

**Turn 5 (May Year 1) — Expansion and pillage decision:**
- Charles studies illusion (first divergence from other mages)
- New runners deployed to carry silver from taxers to mage cluster
- Otello studies entertainment (support skill)
- Scout (1396) enters underworld shaft at (18,54)
- Scout 1395 moves to desert (19,59) for future tax point
- Lumberjack working (earns wages vs producing — not yet skilled enough)

**Turn 6 (June Year 1) — Pillage and income restructure:**
- Taxers 1967 and 1393 **PILLAGE** plain (17,55): extract $893 + $1,191 = $2,084 in one turn
- These taxers then give silver to new farmers formed in (17,55)
- Grey switches to studying earth lore (EART) for passive income spell
- New fishing unit formed in desert (19,59)
- Matthew/Timothy study fire (continuing parallel path)
- Charles studies PHEN (phantasmal entertainment) — revenue spell unlocked
- Wilfred studies energy shield — combat defense specialization
- Runner units navigate between regions, some borrowing maintenance silver from others

**Turn 7 (July Year 1) — City assault:**
- Charles issues `attack 43` (City Guard)
- The One (Brutals) leads assault on City Guard in Mesengoa
- Greywolf's mages (all 4 fire mages + energy shield from Wilfred) join the assault
- Result: 80-leader guard force destroyed in 1 round + free round
- Grey studies illusion
- Matt/Timothy study illusion (continuing path toward PHEN)
- Wilfred studies pattern (filling prerequisite gaps)
- New farming units formed in (18,56) — "Farmer LL" buying 6 high elves

**Turn 8 (August Year 1) — Post-victory consolidation:**
- All mages now in captured Mesengoa, casting spells and studying
- Taxers given 2 swords (Wilfred's earlier acquisition to improve Taxer 1967 combat)
- Runners carry silver from taxers to mage cluster each turn
- Grey gets 5 horses (from Brutals as spoils payment) and distributes one each to Matt/Timothy/Wilfred/Charles — mages now mounted
- Otello studies stealth (transition to spy role)
- Fishing unit begins studying fishing in desert (19,59)
- New miner unit formed in desert (19,59)

**Turn 9 (October Year 1) — Maturation of income streams:**
- Matt and Timothy each cast PHEN for $437 silver each
- Charles casts PHEN for $437
- Total PHEN income: $1,311/turn from 3 mages
- Grey casts Earth Lore for $29 (trivial but consistent)
- Three new region taxers fully operational
- Scout (3891) bought as lizardman in swamp (14,60) and moves 4 hexes — fast scout with new race
- Diplomat (2345) renamed Entertainer, begins entertaining in Trasicy city

**Turn 10 (November Year 1) — Scale-up:**
- Taxer (3274) collects $3,250 from Mesengoa alone (massive unit built from runners bringing troops)
- New taxer units formed in underworld cavern (11,29) — extending underground
- Total tax revenue visible in turn 10 events: over $7,500/turn
- Horse (2343) now producing horses every turn (horse training 2)
- Weapons unit formed — starts studying weaponsmithing (picks → axes)

**Turn 11 (December Year 1) — Treasury hits $9,931:**
- Lumberjack (3963) producing ironwood (IRWD) — high-value production online
- Runner (3961) gives $452 to Builders unit — construction investment begins
- Scout enters underworld shaft locations, establishing underground presence
- Shipbuilders being funded in jungle region — maritime plans forming

**Turn 12 (January Year 2) — Diversification accelerates:**
- Under dwarves (UDWA) appear in inventory — buying drow-type races for production
- Quarry units buying picks, producing stone
- Sailor units being formed for ship/sailing capability
- $13,831 in treasury silver

**Turn 13 (February Year 2) — Region cap hit (10/10):**
- Faction at 10/10 regions (Martial 1 cap = 10)
- Ironwood: 3 units, 7 wood, 6 picks already stockpiled
- Hammers appearing (weaponsmithing advancing)
- All production lines running: iron, wood, stone, grain, livestock, horses

**Turn 14 (March Year 2) — Faction reallocation triggered, mage combat event:**
- Nonentity (67) + Wistful Thinking (27) attack Trasicy city guard together
- Greywolf not involved but observes — city changing hands
- "4 imps" appear in faction inventory — Charles successfully cast Phantasmal Demons
- Its Wilfred (1392) given to Archon Dominion (53) — diplomatic mage transfer
- $20,345 in treasury

**Turn 16 (May Year 2) — Faction type change to Martial 2, Magic 3:**
- Region cap increases from 10 to 25
- Mage cap drops from 5 to 4 (Wilfred already transferred, so no net loss)
- Quartermaster cap increases from 2 to 5
- Regions jump to 13/25 — rapid expansion resumes
- Mages Matt/Timothy now casting PHDE (Phantasmal Demons) not just PHEN
- Multiple new taxer lines expanding in all directions

**Turn 17 (June Year 2) — 15 regions, full maturity:**
- Mesengoa city guards given to Greywolf by Brutals ("Mesengoa Guards" unit)
- 56 gnolls in inventory (bought from gnoll regions)
- 142 horses in inventory — massive horse stockpile
- 21 swords, 37 ironwood, 10 rootstone appearing
- Mages now casting PHDE demons for combat power
- PHEN income per mage: ~$527/turn

**Turn 18 (July Year 2) — 17 regions:**
- Sailors and shipbuilders established — naval capability developing
- Build (2790) constructing structures with rootstone
- 276 centaurs (maxed faction centaur count)
- $37,342 in treasury

**Turn 19 (August Year 2) — Monster hunt:**
- Its Charles attacks Hydra (712) in Dernglen jungle with 12 allied demons and Archon Dominion mages
- Combined force: 3 Greywolf mages + 12 demons (4 each) + 5 Archon Dominion mages + 4 demons each
- Shows deep military alliance with Archon Dominion (53)
- $44,496 in treasury

**Turn 20 (September Year 2) — 20 regions, lion attack:**
- Pride of Lions attacks Greywolf's Horse unit cluster in plain (18,54)
- Greywolf has massive defensive blob of farmer/horse/worker units — lions eventually die after 2 rounds
- 2 Quartermasters active (logistics advancing)
- $50,177 in treasury
- 298 centaurs, 255 high elves, 98 orcs, 153 gnomes — massive workforce

### Strengths & Weaknesses

**Strengths:**

1. **Exceptional mage investment**: 5 mages from turn 1, all on parallel study paths. By turn 9, three mages generate $1,311/turn from PHEN spells — income that scales with zero upkeep beyond mage maintenance. By turn 17 this grows to $1,581+.

2. **Coordinated city capture**: Joined Brutals (50) in a well-planned assault on Mesengoa's City Guard in turn 7, achieving the assault in 1 round. This unlocked the biggest tax region (~$3,900/turn from city alone) without having the military strength to do it alone.

3. **Rapid tax proliferation**: From 0 to 8 taxed regions in 6 turns, using a seeder-runner model where each taxer funds new taxers nearby. By turn 10, collecting $7,500+/turn.

4. **Faction type reallocation**: Switched from Martial 1/Magic 4 to Martial 2/Magic 3 at turn 16, expanding region cap from 10 to 25. Timed well — after mages were developed and needed territory more than more mage slots.

5. **Alliance management**: Effective diplomacy with Brutals (50) and Archon Dominion (53). Wilfred (a trained mage) given to Archon Dominion as a gift — a powerful diplomatic gesture.

6. **Underworld expansion**: Scout entered underworld shaft at turn 5; by turn 11 taxers are in underworld caverns.

7. **Diversified production**: Lumberjack → ironwood, farming → livestock, mining → iron, horse training → horses, herb lore → bags, weaponsmithing → axes/picks. Multiple revenue and resource streams.

**Weaknesses:**

1. **Slow start to actual taxing**: Taxers only begin taxing turn 4 (month 4). Turns 1–3 rely entirely on claimed startup silver and formation costs. The faction spends heavily on claims before income begins.

2. **Mage maintenance vulnerability**: Mages (leaders) cost 50 silver/month. With 5 leaders + 6 scouts in turn 2, the faction relies on claimed startup silver and MEAL withdrawals. In turn 5 reports, maintenance is being "borrowed" chain-style across units — a sign of tight cash flow early.

3. **Order errors indicating scheduling issues**: Multiple turns show "BUY: Unit attempted to buy more than it could afford" for newly formed units — the player sometimes over-commits expected income. Turn 3 shows mages failing to set fire combat spell because they hadn't yet acquired fire. Turn 9 shows teaching conflicts when mages diverge.

4. **No weapons/armor on tax units**: Taxers use only racial combat ability (no swords, no armor). Taxer 1393 (12 centaurs) does have some swords given in turn 8, but most taxers are pure bodies. Against well-armed opposition, the tax force would be vulnerable.

5. **Lion attack exposed vulnerable unit cluster**: Turn 20, a Pride of Lions attacks the Horse unit cluster (plain 18,54) which has no armored defense. The lions survive 2 rounds against hundreds of unarmed units before losing — the faction is not prepared for hostile creatures in production regions.

6. **Lumberjack never produces for most of the period**: Lumberjack (1969) "works" for wages rather than producing wood until high enough skill. Three centaurs at 30 silver cost earn 42 silver wages — barely profitable. Better to transition lumberjacks to orcs earlier (orcs can reach lumberjack level 5 vs centaurs level 2).

7. **Region cap hit at turn 13**: The faction is constrained at 10 regions for turns 13–15 before reallocating. If they had planned the Martial 2 switch earlier, they could have started expanding sooner.

---

## Section 2: AI Agent Strategy (Based on This Playstyle)

### What the AI Would Keep

1. **5-mage team from turn 1**: The Magic 4 allocation with 5 mages (at cap) is correct. The teaching chain — Grey teaches force → all 4 study force simultaneously — is optimal. Keep this structure.

2. **Centaur-based scouts in all 6 directions from turn 1**: Immediate map knowledge is essential. Buying centaurs in the starting town for $78 and sending them 4 hexes/month covers the map fast.

3. **PHEN income path for apprentice mages**: FORC 1 → FIRE 1 → PATT 1 → ILLU 1 → PHEN 1 takes 5 turns to unlock. By turn 9, three mages generate $1,311/month passively. This should be the default apprentice path.

4. **Seeder-runner tax expansion model**: Form taxers in the main town, buy more units using claim/tax income, then have each new taxer fund the next via GIVE NEW. The runner units carrying silver between taxers and mages are essential.

5. **Early alliance with dominant local faction**: Greywolf allied with Brutals who already had combat leaders at level 3. This let them punch above their weight for the city assault. Identify and ally with the strongest nearby faction immediately.

6. **Faction type reallocation from Martial 1/Magic 4 to Martial 2/Magic 3**: Once mages are developed (turn 12–15), this reallocation significantly increases region cap (10 → 25) and quartermaster cap (2 → 5), enabling logistics infrastructure. Time this when taxing existing 10 regions is fully saturated.

7. **Meal withdrawals for leader maintenance**: Using WITHDRAW MEAL to pre-pay 30 silver of the 50 silver leader maintenance cost is efficient. Keeps unclaimed silver available longer.

8. **SHARE 1 and CONSUME FACTION**: Setting these on all units from early turns prevents catastrophic maintenance failures. Let units pull from faction pool automatically.

### What the AI Would Change

1. **Start taxing sooner**: Faction 33 waits until turn 4 to tax. The AI should have taxer units in position by turn 3 at the latest. Form taxers at the same time as mages (turn 1), immediately buy combat units (centaurs/gnolls) and set `guard 1`. In turn 2, with taxer already guarding (17,55), begin taxing immediately.

2. **Switch lumberjacks to orcs earlier**: Centaurs cap at lumberjack level 2; orcs can reach level 5 (producing ironwood). Faction 33 doesn't switch to orc lumberjacks until turn 9–10. The AI should recruit orc lumberjacks by turn 5–6 once the jungle scout has identified orc-inhabited jungle regions. Ironwood production (from LUMB 3) generates much higher income per unit than basic wood.

3. **Fix the mage teaching schedule errors**: Faction 33's orders show errors in turns 3, 5, 9 due to teaching mismatches. The AI should validate: (a) only teach skills you can teach; (b) only set combat spells to skills the unit actually has; (c) when mages diverge to different skills, update TEACH orders immediately. Specifically, in turn 3, don't attempt `COMBAT fire` on mages who only have fire 1 from this turn's study (it works, but needs careful timing).

4. **Deploy a Diplomat unit to the nearest city earlier and more purposefully**: Faction 33's Diplomat is a single goblin doing WORK for 14 silver/turn in Trasicy city — negligible. The AI should instead use this unit to gather market intelligence each turn and consider buying expensive trade goods for resale or establishing entertainment.

5. **Avoid pillage when the region will continue to be used**: Faction 33 pillages plain (17,55) in turn 6 while still planning to tax there. Pillage permanently damages the peasant economy. Since (17,55) continues to be taxed for many subsequent turns, this was suboptimal — they lost future tax revenue. Only pillage regions being permanently vacated.

6. **Arm the taxer units earlier**: By turn 8, the main taxer (1393) has centaurs but no weapons. The two swords transferred to Taxer (1967) help but arrive late. The AI should buy swords for the main combat tax unit by turn 4–5, before any territorial dispute arises. The Mesengoa city guard has 80 swords — after capture, distribute some to taxers.

7. **Don't transfer a developed mage to allied faction**: Wilfred (1392) is given to Archon Dominion (53) at turn 15 with energy shield and force 2. This is a diplomatically generous but strategically costly move — losing one of 4 combat mages permanently. The AI should instead give silver, production units, or trade goods as diplomatic gifts rather than magic-capable leaders.

8. **Establish a Quartermaster earlier**: Faction 33 doesn't have a Quartermaster until turn 14 (March Year 2). Quartermasters enable TRANSPORT orders that let tax income flow automatically to the treasury pool without runner unit logistics. The AI should establish the first Quartermaster by turn 8–10 in the central hub (Mesengoa).

### Recommended Opening (Turns 1–5)

**Turn 1 (Nexus):**
- Set `option template short`, `avoid 1`, `behind 1`, `share 1`, `reveal faction`, `consume faction`, `combat fire` on Grey
- Set `FACTION MARTIAL 1 MAGIC 4`
- Form units: 4 mage leaders (Matt/Timothy/Charles/Wilfred) each claiming $889 (or appropriate amount) and studying FORC; 1 taxer with 12 centaurs (buy at $78 each = $936, claim $936) studying COMB; 6 centaur scouts (each claim $78, buy 1 centaur, move in 6 different directions); 1 Otello claiming ~$989 buying leader and studying TACT
- Grey: TEACH all 4 mage leaders force; WITHDRAW 1 MEAL
- All mage leaders: WITHDRAW 1 MEAL; study FORC

**Turn 2 (First taxer in position):**
- Taxer (centaurs): move to nearest high-population plain; set `guard 1`, `@tax`
- Grey: TEACH fire to all 4 mage leaders; study PATT
- Mage leaders: study FIRE (with teaching); WITHDRAW MEAL; CLAIM 100
- Otello: study OBSE (switches from tactics to observation for scouting support)
- Declare: Friendly to known allies, Neutral to Guardsmen, Unfriendly to Creatures
- Scouts: continue moving into unexplored regions

**Turn 3 (Tax begins; second taxer formed):**
- Taxer 1: TAX (collects first income); FORM new taxer unit, GIVE new 1 [silver to fund it], move it to next region
- Grey: TEACH pattern to mage leaders (those who now have FIRE 1 can receive)
- Mage leaders: study PATT (with teaching); set `@combat fire`
- Form Lumberjack unit: buy 3 orcs (if orc jungle found) or centaurs, study LUMB; find the correct terrain
- Otello: study OBSE
- Scouts: report and continue exploring

**Turn 4 (Expand tax, fire teaching complete):**
- Grey: study EART (begin working toward earth lore income spell) or FORC 2 depending on what's needed
- Mage leaders (Matt, Timothy, Charles): study ILLU (need FORC 1 + PATT 1, now have both); set `@combat fire`
- Wilfred: study ESHI (energy shield — the defensive combat spell)
- Taxers: TAX in 2–3 regions; FORM new buying unit funded by tax income; buy arms (swords) for main taxer
- Lumberjack: study LUMB; @work if not yet skilled enough to produce

**Turn 5 (Income stable; prepare city assault):**
- Grey: study FORC 2 (if not yet, else EART); @cast EART if available
- Matt/Timothy/Charles: study PHEN (need ILLU 1, now have it); set `@cast PHEN` from next turn onward
- Wilfred: study ESHI 2 or PATT; `@combat ESHI`
- Otello: @entertain or study STEA
- Taxers: TAX in 3–4 regions; continue FORM expansion
- If allied faction has military strength for city assault: position units at town hex; plan attack

### Mid-Game Plan (Turns 6–15)

**Magic income scaling (turns 6–10):**
- Matt, Timothy, Charles should be `@cast PHEN` every turn from turn 6 onward. At $437/cast each, three mages = $1,311/month passively. Do not interrupt this for more studying unless critical skill gap exists.
- Grey casts `@cast EART` every turn for minor income and skill practice. More importantly, Grey should pursue advanced magic: earth lore → weather lore or necromancy → more powerful area spells.
- Consider adding `@study fire` on specific turns to push mages from fire 1 to fire 2 (increases fireball damage significantly — turn 5 report shows fire 2 unlocked).

**Tax saturation (turns 6–12):**
- Target: every accessible region within 2–3 hexes has a taxer unit. Each taxer should have 10–20 race-matched units (centaurs in centaur regions, high elves in high-elf regions, etc.).
- Use the GIVE NEW funding model: tax income → immediately GIVE to new unit → new unit buys population → moves to next region → taxes next turn.
- Install a Quartermaster in Mesengoa by turn 8; use TRANSPORT orders for passive silver flow from remote taxers.

**Production specialization (turns 8–14):**
- Lumberjack with orcs: need 3 orcs at LUMB 3 to produce ironwood. Start this by turn 6 if jungle with orcs is within reach. Ironwood is needed for advanced shipbuilding and construction.
- Farmer with humans: humans can reach FARM 4, producing grain + livestock efficiently. Target 6–9 humans per farmer unit producing each turn.
- Horse trainer with centaurs: centaurs reach HORS 2. Produce horses each month; horses needed for mounted mages and cavalry taxers (increased mobility = 4 hexes vs 2).
- Mining with humans or orcs: iron → eventually used for swords, picks, armor.
- Consider gnomes for herb lore → bags (high-value trade item).

**Military capacity (turns 10–15):**
- Maintain the mage + centaur assault group (Grey + 3 combat mages + Wilfred ESHI + centaur/gnoll mass).
- By turn 12, mages should have fire 2+ — fireball damage scales significantly.
- Do not attack city guards alone. Only assault with allied forces or when total mage damage per round exceeds guard HP.
- Hunt monsters (hydra, lions, etc.) for loot using demon units created by Charles's PHDE spell. Coordinate with allied mages.

**Faction reallocation (turn 13–15):**
- When hitting the 10-region cap, evaluate: is Magic 3 sufficient? With 4 mages at PHEN producing $1,600+/turn, yes. Switch to Martial 2 for 25 regions.
- This costs 1 mage slot (5 → 4), but the mage already transferred to Archon Dominion plugs this gap diplomatically.
- Immediately begin claiming the next 15 regions in the expansion corridor.

### Adaptations for Dynamic Conditions

**If allied faction is weak or absent:**
- Do not attempt city assault in turns 5–8. Instead, max out taxing in rural regions and save silver for a larger combat force.
- Buy gnolls or orcs for combat (combat skill levels higher than centaurs in certain builds).
- Study weather lore or demon lore instead of PHEN — summoned demons can substitute for allied troops in combat.

**If a rival faction is blocking expansion:**
- Redirect scouts in their direction to assess force size.
- Negotiate (declare Friendly early, before conflict starts).
- If aggressive: concentrate tax force + mages in contested regions; don't leave undefended taxers in border hexes.
- If they pillage your regions: do not retaliate immediately; assess their mage count. Greywolf-style relies on fire mages being superior — only fight if you have the mage advantage.

**If the starting town is weak (small peasant population, low income):**
- Adjust scouts to prioritize finding large towns (look for hexes reporting "X peasants" > 5000).
- Start taxing the largest reachable town immediately even if it means delayed mage study.
- Consider shifting the mage cluster to the highest-income town rather than staying near the nexus start.

**If no allied faction is friendly:**
- Spend turns 1–8 building a pure tax income base; skip the city assault.
- By turn 10–12, with 5 fire mages at fire 2+ and 80+ centaur melee, solo city assault becomes viable.
- The key is having Otello (tactics 1) in the attack force and Wilfred casting energy shield — these provide the combat round advantage and damage mitigation.

**If production resources are scarce (no orc jungle nearby):**
- Focus on gnomes (entertainment, herb lore, crossbow) and high elves (longbow, fishing) instead.
- Gnome entertainers with ENTE 5 generate 5× 30 = 150 silver/gnome/month — superior to most production.
- High elf fishers produce fish for trade in coastal/desert cities (fish wanted in Trasicy at $48–$56 each).

**If attacked by a stronger faction:**
- Use the mage cluster's avoid + behind settings — avoid individual region captures.
- Retreat mages to a fortified region (building a tower would help but takes time).
- PHEN mages generating income behind lines while taxers and centaurs absorb contact.
- Negotiate immediately: offer silver tribute rather than risk mage losses.
