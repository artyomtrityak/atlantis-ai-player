# Faction 60 Strategy Analysis

## Section 1: Observed Playstyle (Turns 1–20)

### Starting Conditions

**Faction name:** Men In Tights (60)
**Faction type:** Martial 1, Magic 1 (upgraded to Martial 2, Magic 3 by turn 7)
**Starting location:** Plain (12,60) in Kuba region
**Starting units:**
- Rob in Hood (unit 914) — 1 leader with sword [SWOR], pre-trained: observation 1, force 1, pattern 1, spirit 1, gate lore 1, fire 1, combat 3, stealth 1. Combat spell set to fire [FIRE].
- 7 "Brother" units (1639–1645) formed in turn 1 — each 1 human bought from starting location.

**Starting resources:** Unclaimed silver 9,335 (turn 2 report). This is the faction's claim pool across the entire faction.

**Key starting skills on Rob in Hood (914):** Already has combat 3, gate lore 1, fire 1. This is a powerful starting mage-assassin.

**Allies at game start:** Nonentity (67) set as Friendly from turn 1.

---

### Economic Strategy

**Overall approach:** Extremely aggressive money-claiming and multi-hex tax empire from the beginning. The faction uses a large number of small units (1 man each) to rapidly spread across the map, each claiming silver and buying one local race unit, then continuing to expand.

**Turn 1 (January, Year 1 / turn 1 orders):**
- Rob in Hood (914) claims 100 silver, studies stealth, casts GATE Random to teleport away.
- No taxing yet; all 7 Brothers each claim 50 silver and buy 1 human each, then scatter in 6 different directions to explore and find new regions.

**Turn 2 (February, Year 1 / turn 2 orders):**
- Rob in Hood gate-jumps again. The 7 Brothers scatter further. Each new Brother forms new sub-units in new regions: Brother forms and buys 1 local race unit, moves on. This creates a self-replicating scouting web.
- Specific new units formed: 7 new Brothes (1639–1645 children) buying lizardmen, gnolls, wood elves, goblins from local markets in newly reached regions.

**Turn 3 (March, Year 1):**
- Father (2155) begins TAXING in jungle (12,56) Tinscillar with ~$241/turn.
- Unit 2167 (8 goblins) taxes swamp (56,76) in Powann for $400/turn. This remote location was reached via Rob in Hood's Gate Jump in turn 1.
- Production begins: Units 2507–2510 start studying farming, herb lore, lumberjack, shipbuilding at the Powann swamp base. This is a dedicated production cluster.

**Turn 5 (May, Year 1):**
- Tax income confirmed: Father (2155) collects $242 in Tinscillar; Unit 2506 collects $300 in Powann swamp (56,74); Unit 2167 collects $400 in Powann swamp (56,76).
- Treasury (turn 5 report header): 3,081 unclaimed silver with total faction silver pool of 94,230. Faction is ranked 9th globally in silver.

**Turn 7 (July, Year 1):**
- Tax income summary: Brother (1639) $50 (plain 11,53), Brother (2160) $50 (swamp 13,53), Brother (2163) $50 (jungle 14,54), Father (2155) $241 (jungle 12,56), Unit (2168) $50 (swamp 55,71), Unit (2828) $250 (swamp 56,72), Unit (2506) $600 (swamp 56,74), Unit (2167) $428 (swamp 56,76).
- Total monthly tax income at turn 7: ~$1,720/month from 8 regions.
- Treasury silver: 993 unclaimed; total pool 160,070. Ranked 42nd globally in per-unit silver.

**Turn 8 (August, Year 1):**
- New swamp tax region Cebo (10,50): Brothers (2158) collects $300.
- Abbey Refugees (3825) collects $450 in jungle (5,61) Bictmark.
- Tax income now exceeds $2,000/month.

**Turn 10 (October, Year 1):**
- Abbey Refugees (3825) $450 (Bictmark jungle 5,61); Brothers (2158) $300 (Cebo swamp 10,50); Father (2155) $240 (Tinscillar 12,56); Unit (2168) $300 (Powann 55,71); Unit (2828) $576 (Powann 56,72); Unit (2506) $600 (Powann 56,74); Unit (2167) $450 (Powann 56,76).
- Total confirmed tax: ~$2,916/month from 7 regions.
- Global treasury silver: 3,557 unclaimed; total 261,779. Ranked 29th in per-unit silver.

**Turn 11 (November, Year 1):**
- Regions: 9 controlled (cap 25).
- Tax income: same tax nodes plus additional sub-taxers from Bictmark.

**Turn 12 (December, Year 1):**
- Regions: 10 controlled.
- Treasury: 3,756 unclaimed silver; total pool 364,376.

**Turn 13 (January, Year 2):**
- Regions: 10. Quartermasters: 0 (cap 5).
- Treasury: 4,383 unclaimed; total pool 447,810.

**Turn 16 (May, Year 2):**
- Regions: 11. Quartermasters: 1.
- Treasury: 11,301 unclaimed; total pool 644,859.

**Turn 17 (June, Year 2):**
- Regions: 10. Quartermasters: 2.
- Treasury: 11,765 unclaimed; total pool 741,527.

**Turn 18 (July, Year 2):**
- Regions: 13. Quartermasters: 2.
- Treasury: 15,570 unclaimed; total pool 865,369.

**Turn 19 (August, Year 2):**
- Regions: 13. Quartermasters: 2.
- Treasury: 19,692 unclaimed; total pool 1,056,514.

**Turn 20 (September, Year 2):**
- Regions: 13. Quartermasters: 2.
- Treasury: 23,622 unclaimed; total pool 1,244,573.

**Economic growth trajectory:**
- Turn 5: ~94k total silver pool
- Turn 7: ~160k total silver pool
- Turn 10: ~262k total silver pool
- Turn 12: ~364k total silver pool
- Turn 14: ~533k total silver pool
- Turn 18: ~865k total silver pool
- Turn 20: ~1.24M total silver pool

**Entertainment income (supplemental):** 3 "Brother" entertainers in regions (1639=Kuba, 1641=Siaghhath, 1640=Kuba) each earning $30/month. A growing entertainer network adds ~$90–$300+ per month by mid-game.

**Production at Powann base:**
- Unit 2507: farms grain (5/turn → 15/turn by turn 7)
- Unit 2508: produces herbs → bags (5 bags/turn, each worth ~150 silver to withdraw)
- Unit 2509: produces wood
- Unit 2510: builds ships (completed first Longship at turn 7)
- Unit 2830: produces bags from herbs
- Unit 3500: produces spinning wheels

**Silver claiming pattern:** Every new scout unit claims silver to pay for itself plus fund one race purchase. The faction uses `@claim 50` and `give new 1 N silv` patterns extensively to bootstrap each sub-unit from the faction claim pool.

---

### Military Strategy

**Rob in Hood (914) — assassin mage:**
- Core military unit. Combat 3, Fire 1, Stealth 1→higher. Combat spell: fire [FIRE].
- Turn 1: teleports via GATE Random to Powann (far southeast).
- Turn 1 orders: had `combat FIRE` and `avoid 1` and `hold 1` set, but also `cast GATE Random`.
- Turn 2 (execute turn): tries to steal from self (practice), casts Random Gate.
- Turn 3: assassinates Windrunner (1648) of The Carnival of Shadows (61) in Enstan — kills 1 high elf with free fireball round.
- Turn 4: assassinates Unit (2274) of The Merry Magicians (24) in Prausmonaf — kills 1 wood elf.
- Turn 5: attempts assassination on The Lemon-Seeker (1694) of an unknown faction in Fe'eind — CAUGHT, no kill, gains stealth practice.
- Turn 6: assassinates Darkness (1259) of Distant Drummer (15) in Lipodou — kills leader, gains $50 silver.
- Turn 7: assassinates Unit (2374) of Shestoper (36) in Quaytre — kills leader.
- Turn 8: assassinates Unit (2755) of Stormbringer (46) in plain O'enbran — kills 1 of 5 high elves.
- Turn 9: assassinates Worker (3088) of Silver Hand (25) — kills leader.
- Every turn: casts Random Gate Jump to teleport to a new region.

**Pattern:** Rob in Hood is a dedicated assassin-mage. Each turn it teleports to a new region via gate and assassinates the first viable target. Targets appear to be single units or small units belonging to other factions — likely chosen by scanning units in the new region. The free fireball round one-shots almost any single-unit target.

**Stealth progression:** Rob in Hood studies stealth every turn (50 silver/month). By turn 2 it has stealth 2 (100 XP). By turn 5 it's approaching stealth 3 (failed assassination at 5 = possibly stealth check failing). No further study failures visible.

**Land forces:**
- Very minimal direct combat capability for the main body.
- Father (2155) guards jungle (12,56) in Tinscillar with lizardman troops.
- Unit (2167) guards Powann swamps with goblin troops.
- Unit (2828) guards Powann swamp (56,72) with orc troops. Collects $450+ in taxes.
- Unit (2506) guards Powann swamp (56,74) with gnoll troops. Collects $600 in taxes.
- Brothers (2158) guards swamp (10,50) Cebo with lizardman troops.
- Abbey Refugees (3825) guards jungle (5,61) Bictmark with lizardman troops.

**Combat units at tax nodes:** Each taxing "hub" unit accumulates same-race troops by forming new units that buy local races and study combat. Pattern: each turn, the taxing hub forms a new sub-unit, gives it buy money, it buys 3–9 troops, studies combat 1 turn, then merges back or stays.

**Unit (2828) Powann (56,72):** Accumulates orcs — 3 orcs turn 5, 4 orcs turn 6, 5 orcs turn 7, growing each turn. Studies combat on subunits.
**Unit (2506) Powann (56,74):** Accumulates gnolls — grows from 6 gnolls to 10+ gnolls, studies farming/hunting (for combat upgrades?).
**Unit (2167) Powann (56,76):** Accumulates goblins and trains sailors.

**Turn 7 combat losses:** Unit (2505) — 1 gnoll — destroyed by Undead monsters in Powann swamp. Shows vulnerability of single-man scout units to monster attacks.

**Brother (2162) in Siaghhath:** Destroyed in turn 4 by Siaghhath Centaurs (1537) attacking it (1 gnoll vs 34 centaurs + 35 gnolls). Showed a scout with no combat ability is very exposed.

**No direct offensive military campaigns** against other player factions. All territorial acquisition is passive (moving into unoccupied or weakly guarded regions). Military is purely defensive taxation protection.

---

### Magic Development

**Rob in Hood (914):**
- Starting skills: observation 1, force 1, pattern 1, spirit 1, gate lore 1, fire 1, combat 3.
- Turn 1 orders: study STEA (stealth).
- Each turn continues studying STEA; Rob never studies any magic beyond what it started with during turns 1–11.
- By turn 2: stealth 2 (100 XP). By turn 3: stealth 2 (170 XP).
- Keeps combat spell: fire [FIRE].
- Can study: earthquake, force shield, energy shield, spirit shield, magical healing, farsight, mind reading, weather lore, earth lore, necromancy, demon lore, illusion, artifact lore — but never does so in turns 1–11.
- Fire 1 is sufficient for the assassin role since the fireball free round kills 1-man units and small groups.

**Faction magic limits:** Faction status shows Mages: 1 (cap 2 → cap 4 from turn 7). Rob in Hood is the only mage. No apprentices are ever recruited (cap 0 → 7 from turn 7).

**No magic expansion:** Despite the faction cap being increased to 4 mages and 7 apprentices by turn 7, no additional mages or apprentices are recruited through turn 20. Magic remains exclusively Rob in Hood's domain.

**Unit (3501) — observer:** In turn 8 orders, Unit (3501) studies observation 2. This provides reconnaissance at a Powann sub-unit.

---

### Expansion Pattern

**Geographic spread:**
- Turn 1: Starting at plain (12,60) Kuba. 7 scouts disperse to adjacent hexes.
- Turn 2 (report): 0 controlled regions (not yet 50+ men in any).
- Turn 3 (report): 0 controlled regions.
- Turn 4 (report): 2 controlled regions (Tinscillar jungle 12,56 and Powann swamp 56,76).
- Turn 5: 3 regions.
- Turn 6: 5 regions.
- Turn 7: 8 regions (faction cap raised to 25, Martial 2, Magic 3).
- Turn 8: 7 regions (lost one from monster attack + border changes).
- Turn 9–10: 7 regions.
- Turn 11: 9 regions.
- Turn 12: 10 regions.
- Turn 13–15: 10 regions.
- Turn 16: 11 regions.
- Turn 17: 10 regions (lost one).
- Turn 18–20: 13 regions.

**Two main geographic clusters:**
1. **Home cluster** (Kuba/Tinscillar/Celcuhfo/Siaghhath area, ~x=10-16, y=50-70): Father (2155) taxes jungle (12,56). Multiple Brothers scattered through adjacent hexes, most without tax capability (just working or entertaining). Brothers (1642, 1645) mounted on horses, exploring north using riding skill.

2. **Powann cluster** (far southeast, ~x=55-57, y=70-80): Unit (2167), (2828), (2506), (2168) — a dense tax empire with 4 nodes. Remote — reached only via Rob in Hood's gate jump in turn 1. This is the economic engine.

**Bictmark cluster** (west, ~x=4-5, y=60-65): Abbey Refugees (3825) taxes jungle (5,61) for $450/turn. Established by turn 8 after scouts swam the ocean.

**Cebo cluster** (northwest, x=10, y=50): Brothers (2158) taxes swamp for $300/turn from turn 10.

**Scout web:** 20+ lizardman/orc/gnoll scouts swimming oceans and exploring remote regions, most of them single-man units looking for unguarded territories. Several refused entry (blocked by other factions' guards) showing competition for territory.

**Riding scouts:** Brothers (1642, 1645, 1644) use horses and study riding to cover 4+ hexes per turn, rapidly scouting the north of the home cluster.

**Swimming lizardmen:** Units (3490, 3491, 3492, 4137, 4138, 4139, 2158, 2159, 2157, 2156, 4141, 4872) — lizardman scouts swim oceans to reach coastal regions. Lizardmen have swimming capacity, making them ideal for ocean-crossing scouts.

---

### Turn-by-Turn Summary

**Turn 1 (January Y1) — Setup and scatter:**
- Rob in Hood claims 100, studies stealth, casts Gate Random (teleports to Powann swamp 56,76).
- 7 Brothers formed: each claims 50, buys 1 human, scatters in all directions from Kuba.
- Key orders: `combat FIRE`, `avoid 1`, `hold 1`, `reveal`, `cast GATE Random`.

**Turn 2 (February Y1) — First expansion wave:**
- Rob in Hood at Powann: forms 7 more sub-units, each claims 45-51, buys local race (lizardmen from Tinscillar, gnolls from Siaghhath, wood elves from Blodo, goblins from Powann). Sub-units scatter further.
- Rob in Hood studies stealth, casts Gate Random again.
- Total units created: ~15+ by end of turn.

**Turn 3 (March Y1) — Production and entertainment setup:**
- 3 Brothers already in Kuba study ENTE (entertainment 1).
- Rob in Hood forms 8 new units: 1 with 8 goblins studying COMB (combat army seed), 1 with 1 goblin moving north.
- Rob in Hood casts Gate Random, teleports to Enstan (plain 15,21).
- Multiple Brothers spreading in Celcuhfo, Dernglen, Blodo, Crillversqui directions.

**Turn 4 (April Y1) — First kill and first taxes:**
- Rob in Hood assassinates Windrunner (1648) of Carnival of Shadows (61) in Enstan. Free fireball kills 1 high elf. Gains $20.
- Father (2155) placed on guard/tax in Tinscillar (12,56): collects $50 (first tax collection).
- Unit (2167) taxes Powann (56,76) for $400 — largest single region.
- Stealth studying continues. Rob jumps to Fe'eind (mountain 16,70).
- Unit (2506) formed in Powann with 6 gnolls, studies combat.
- Units (2507-2510) start: farming, herb lore, lumberjack, shipbuilding.

**Turn 5 (May Y1) — Combat losses and first production:**
- Rob catches attempt on The Lemon-Seeker (1694) in Fe'eind — CAUGHT, no kill (stealth check failed or target was guarded).
- Brother (2162) destroyed by Siaghhath Centaurs — over-extended scout into hostile territory.
- Tax income: Father $242 (Tinscillar), Unit (2506) $300 (swamp 56,74), Unit (2167) $400 (swamp 56,76).
- Unit (2507) starts producing grain; Unit (2508) produces herbs; Unit (2509) produces wood.
- Rob jumps to forest (6,26) Prausmonaf, finds The Merry Magicians (24) units there.

**Turn 6 (June Y1) — Assassination of Merry Magicians:**
- Rob assassinates Unit (2274) of The Merry Magicians (24) — 1 wood elf killed (they were building a Raft, 5 WE unit).
- Faction now at 5 regions.
- Tax income reaches 5 nodes: Brother (1639) $50 (Celcuhfo), Father (2155) $241 (Tinscillar), Unit (2828) $150 (Powann 56,72), Unit (2506) $500 (Powann 56,74), Unit (2167) $400 (Powann 56,76) = ~$1,341/month.
- Rob jumps to tundra (46,84) Lipodou.

**Turn 7 (July Y1) — Faction upgrade, Longship completed:**
- Unit (2163) issues `faction martial 2 magic 3` order — faction cap raised to 25 regions, 4 mages, 7 apprentices, 5 quartermasters.
- Rob assassinates Darkness (1259) of Distant Drummer (15) — kills leader, gains $50.
- First Longship completed at Powann (56,76) — Sailors (3499) begin sailing SW.
- Unit (2168) starts taxing swamp (55,71) for $50/month.
- Tax nodes: 8 regions, ~$1,720/month total.
- Total silver pool: 160,070.

**Turn 8 (August Y1) — Ship sailing, new bases:**
- Rob fails to find valid target (ASSASSINATE: Invalid unit given error) in turn 8 orders; catches attempt in Quaytre (stealth practice).
- Ship [108] sails SW from Powann toward remote regions.
- Brother (1642) reaches Shickpesh with horse (riding study progressing).
- Abbey Refugees (3825) established in Bictmark jungle (5,61) — begins taxing $450/month.
- Brothers (2158) established at Cebo swamp (10,50) — begins taxing $300/month.
- Tax income: 9 nodes, ~$2,500+/month.

**Turn 9 (September Y1) — Remote expansion:**
- Rob assassinates Unit (2374) of Shestoper (36) in Quaytre — kills leader.
- Sailors (3499) destroyed by Pirates (464) in ocean — 4 goblins lost to 10 pirates.
- Unit (4136) destroyed in Tinscillar jungle by Anacondas — 2 lizardmen lost.
- Unit (2505) (gnoll) destroyed by Undead in Powann swamp — monsters a constant threat.
- Ship [115] built in Powann, begins sailing north toward home cluster.

**Turn 10 (October Y1) — City attacks observed:**
- Rob assassinates Unit (2755) of Stormbringer (46) in O'enbran.
- Adjacent factions (Copy & Bara Union, Shestoper) observed fighting city guards in desert regions.
- Faction silver: 261,779 total pool.

**Turn 11 (November Y1) — Observation network:**
- Rob assassinates Worker (3088) of Silver Hand (25) in Phigill mountain.
- Brothers studying observation (1639, 2160, 1643, 1641, 1640, 2166) — 6 units pivot to OBSE study. This suggests planning for observation rings or mage support.
- Regions: 9.

**Turn 12 (December Y1) — City assault observed:**
- The Merry Magicians (24) attack City Guard (21) in Prausmonaf — 59 casualties among attackers, city guard loses 10. Attack routed. Rob in Hood is positioned nearby (was there turn 5).
- Rob assassinates Worker (3088) — continuing assassin runs.
- Faction silver: 364,376 total pool, 10 regions.

**Turn 13 (January Y2):**
- Merry Magicians attack City Guard (38) in Dernglen — 5 mages with fireballs + infantry overwhelm guard.
- Copy & Bara Union attack city guard in desert (Blecishchan).
- Faction gains Quartermaster 1.
- Silver: 447,810 total, 10 regions.

**Turn 14 (March Y2):**
- Copy & Bara Union attacks city guard in Blecishchan with massive force (100+ goblins, longbow gnomes, cavalry).
- Faction silver: 533,026 total, 10 regions, 1 quartermaster.

**Turn 15 (April Y2):**
- Silver: 577,289 total, 10 regions.

**Turn 16 (May Y2):**
- Regions: 11, 1 quartermaster.
- Silver: 644,859 total.

**Turn 17 (June Y2):**
- Regions: 10, 2 quartermasters.
- Silver: 741,527 total.

**Turn 18 (July Y2):**
- Regions: 13, 2 quartermasters.
- Nonentity (67) captures city in Blodo (observed).
- Silver: 865,369 total.

**Turn 19 (August Y2):**
- Regions: 13.
- Nonentity (67) captures city in Blodo with massive orc + gnome + crossbow army.
- Silver Hand (25) attacks city in Febefe tundra.
- Silver: 1,056,514 total.

**Turn 20 (September Y2):**
- Regions: 13, 2 quartermasters.
- Silver: 1,244,573 total.
- Fon (8) captures city in Crillversqui jungle (15,69) with mithril sword orcs.
- Silver Hand captures city in tundra.

---

### Strengths & Weaknesses

**Strengths:**

1. **Gate mage as map-wide scout and assassin** (evidence: turns 2–12+): Rob in Hood teleports to a new region every turn, killing enemy units and gathering map intelligence across the entire world. This costs only ~$100/month (stealth study + maintenance claim) and generates enormous disruption.

2. **Rapid early expansion via single-unit scouts** (evidence: turns 1–5): Forming many 1-man units, each self-funded via claim, lets the faction establish 8+ taxing nodes within 7 turns. The claim mechanism removes the normal cash constraint on expansion.

3. **Powann cluster as high-yield isolated base** (evidence: turns 4–20): By gate-jumping to Powann in turn 1, the faction established a 4-node tax cluster ($1,450+/month) in a remote area far from other factions' starting zones. The cluster was uncontested for many turns.

4. **Diverse race purchases matching local production skills** (evidence: turns 3–7): Lizardmen for swimming scouts, gnolls for farming/hunting, goblins for shipbuilding/entertainment, wood elves for lumberjack/entertainment, orcs for mining/combat. Each race is matched to what the local region can best produce.

5. **Entertainment units provide passive income** (evidence: turns 3–11): 3+ entertainers generate $30/month each in active regions, with Brother (2165) reaching $210/month in jungle (11,67) Blodo by turn 11.

6. **Silver growth compounding**: The unclaimed silver pool grows from 6,641 (turn 4) to 23,622 (turn 20), showing the faction keeps accumulating faster than it spends.

**Weaknesses:**

1. **Magic development stagnation** (evidence: turns 1–20): Rob in Hood never advances beyond starting magic skills. Gate lore 1 is the only gate magic; fire 1 casts only weak fireballs. The mage never studies farsight, earth lore, or any combat amplification magic. With 4 mage slots available from turn 7 and millions in silver, this is a critical missed opportunity.

2. **No second mage recruited** (evidence: turns 7–20): Despite faction cap allowing 4 mages, only 1 mage operates the entire game. A second mage with different specialization (necromancy, earthquake, weather) would multiply combat and economic effectiveness.

3. **No combat army built** (evidence: turns 1–20): The faction has no coordinated attack force capable of taking a city. While individual tax-guards accumulate a few orcs or gnolls, there is no unified army. Every city capture observed in turns 12–20 belongs to other factions.

4. **Scout unit losses to monsters** (evidence: turns 7, 9, 10): Single-man or tiny-unit scouts are repeatedly destroyed by creature stacks in occupied regions. This wastes investment and silver.

5. **Stealth study for Rob is very slow for returns**: Spending 50 silver/month to level stealth (eventually reaching level 3 after ~9 months) when Rob could instead advance its combat magic to fire 2 or study farsight for strategic reconnaissance.

6. **Observation study investment unclear** (evidence: turn 11): 6 Brothers suddenly study observation, but there's no follow-on magic network visible in later turns. This looks like wasted study time for units with no magic progression.

7. **Errors in orders every turn** (evidence: multiple turns): Recurring GIVE: Not enough errors suggest poor silver flow planning. The faction frequently over-allocates in give chains and fails, requiring sub-units to borrow at maintenance time.

---

## Section 2: AI Agent Strategy (Based on This Playstyle)

### What the AI Would Keep

1. **Gate mage as assassin-explorer**: The opening Gate Random cast is excellent. A leader mage with fire, gate lore, and combat 3 can kill 1-man units across the entire world every turn for very low cost. Keep this core concept.

2. **Multi-scout expansion from turn 1**: Creating 6–7 scouts immediately, each self-funded via claim, and spreading in every direction is highly efficient. This maximizes early map coverage and region acquisition.

3. **Powann remote base via gate**: Establishing a high-income cluster in a remote area discovered via gate jump is a brilliant opening. The gate mage should jump on turn 1, assess the landing zone, and if it has reasonable taxing regions nearby, commit sub-units there.

4. **Claim + buy pattern for sub-unit bootstrapping**: The `claim 50`, `buy 1 RACE` pattern for each new sub-unit is extremely efficient. Each unit pays for itself from the faction pool.

5. **Race specialization for production**: Match goblin units to shipbuilding/entertainment, lizardmen to swimming scouts, gnolls to farming/hunting production, wood elves to lumberjack/entertainment.

6. **Multi-node Powann tax cluster**: The 4-node Powann cluster generating $1,450+/month by turn 7 is the correct economic model. Find isolated regions where multiple hexes can be taxed without competition.

7. **Mounted scouts for rapid home-area coverage**: Brothers (1642, 1645) study riding and use horses to cover 4+ hexes per turn. This is efficient for mapping a home cluster.

### What the AI Would Change

1. **Mage development — never stagnate at Fire 1** (turns 7–20 wasted): The faction never advances Rob's combat magic. Fire 1 caps at 1 fireball per round with 1 kill. Studying fire to level 2 would double kill output. Earth lore → earthquake would allow area attacks. The AI should invest at minimum 3–4 turns studying fire 2 after establishing assassination rhythm. By turn 8, with $50 maintenance covered and stealth already at 3, switch stealth budget to fire 2 study.

2. **Recruit a second mage by turn 7–8**: The faction had cap for 4 mages from turn 7 and over 160k silver. Recruiting a second leader unit and buying it gate lore + a combat school (pattern/force/spirit for force shield, or spirit/pattern for healing, or force/spirit for necromancy) would have opened a second assassination lane and provided far better combat support.

3. **Build a combat army by turn 10**: With $2,500+/month income and millions in savings, the faction should have dedicated 200–400 silver/month to accumulating a 50–80 man army near the home base. By turn 12 when other factions attack cities, Men In Tights could be doing the same. The AI should set a target of building one army group of 40–60 gnolls or orcs with combat training by turn 10.

4. **Eliminate GIVE errors through better order structure** (every turn): The AI should track exact silver flows. Never issue give orders that exceed available silver. Use `@give` (conditional) with fallback amounts, or calculate precise amounts from income before issuing transfers.

5. **Scout unit protection** (turns 7, 9, 10 showed losses): Single-man scouts in swamp/jungle/mountain regions with active creature stacks are frequently destroyed. The AI should issue `avoid 1` and `behind 1` on all scouts, and when possible send pairs of units to reduce loss impact.

6. **Don't study observation without a magic plan**: The turn 11 pivot where 6 Brothers study observation was never followed up. Observation is useful for mage circles or spy networks, but if there's no follow-through with actual mages, it wastes study time. The AI should only study supporting skills when there is an explicit plan to use them.

7. **Turn Rob's assassination toward high-value strategic targets**: Rob kills random leaders and small units throughout turns 1–12. A better strategy is to identify enemy taxmen, enemy mages, or enemy commanders guarding important cities and assassinate those specifically. Rob has map-wide reach via gate — use it for strategic disruption rather than random opportunism.

---

### Recommended Opening (Turns 1–5)

**Turn 1:**
- Rob in Hood (914): `claim 100`, `study STEA`, `withdraw 1 SWOR`, `cast GATE Random`. Set `combat FIRE`, `avoid 1`, `behind 1`.
- Form 6 Scouts from Rob's location. Each: `claim 50`, `buy 1 HUMN`, then move in a different direction (N, NE, S, SE, SW, NW).
- Give Rob a meal for maintenance: `consume unit`.

**Turn 2 (after gate jump):**
- Rob at remote gate location: Form 1 hub unit. Hub: `claim [region_tax_silver]`, `buy [local_race] N` (enough to tax), `guard 1`, `tax`. Rob continues `study STEA` and `cast GATE Random`.
- Each Scout from home area: in its new region, form a sub-scout. Sub-scout: `claim 50`, `buy 1 [local_race]`, move further out. Parent scout: moves on.
- Key: immediately establish one taxing hub in the remote gate-jump location if the region allows.

**Turn 3:**
- Rob: `study STEA`, `cast GATE Random`, attempt assassination on best target at current gate location.
- Home area: identify 2–3 regions with good tax potential. Assign one unit per region to `guard 1`, `tax`.
- Powann cluster (if gate landed near good swamp): spawn 4 production units studying farming/herbalism/lumberjack/shipbuilding.
- Begin entertainment: 2–3 Brothers in high-wage regions switch to `@entertain`.

**Turn 4:**
- Rob: continue assassination pattern. `TURN`/`ENDTURN` block with `steal 914 SILV` for stealth practice if no target; otherwise `assassinate [target_id]`.
- Expand home tax nodes to 3–4 regions.
- Father unit (combat study): `buy 3-4 LIZA`, `study COMB`. Start building first combat nucleus.
- Study `faction martial 2 magic 3` when you can afford the upgrade (check required regions/income).

**Turn 5:**
- Rob: `cast GATE Random`, continue. Now start considering `study FIRE` instead of STEA if stealth >= 2.
- Home cluster should have 5 tax nodes operational.
- Begin recruiting riding scouts with horses.
- Review silver flow — fix any give-chain errors. Simplify by using `share 1` on hub units instead of manual give amounts.

---

### Mid-Game Plan (Turns 6–15)

**Economic priorities:**
- Maintain 8+ taxing nodes by turn 8, 12+ by turn 12.
- Target $3,000+/month tax income by turn 10.
- Identify city locations from Rob's gate travels — note which cities have weaker guards (12-30 leaders) vs stronger (80 leaders).
- Build Quartermasters (1–2) by turn 12 to enable silver transport from Powann to home cluster.

**Military development:**
- By turn 8: one combat group with 20+ orcs/gnolls studying combat (combat 1), armed with available weapons.
- By turn 10: 40+ man combat group; consider targeting a smaller city (12-leader guard) for capture.
- By turn 12: second combat group. Plan city capture with 60–80 man army.
- Gates: Rob should use gate awareness to scout city guard strengths before committing armies.

**Magic development:**
- Turn 6–8: Rob studies `FIRE` (fire 2) instead of STEA (stealth 2 is sufficient for assassinations).
- Turn 8–10: Rob studies `EQUA` (earthquake) or continue fire 3. Earthquake allows area damage against large armies.
- Turn 10–12: Recruit second mage (leader unit). Study gate lore 1 for gate access. Choose specialty: necromancy (raises undead armies), or weather lore (disrupts enemy ships), or mind reading (intelligence).
- Turn 12–15: Third mage if financially viable. Each mage costs ~$50/month maintenance but provides enormous strategic value.

**Expansion direction:**
- Prioritize isolated remote regions reachable only via swimming or gate — less faction competition.
- Use lizardman swimming scouts to cross oceans and find uncontested island regions.
- Avoid expansion into areas with strong factions (Archon Dominion 53, Copy & Bara Union 56 seen blocking scouts in turns 5–6).

---

### Adaptations for Dynamic Conditions

**If threatened militarily:**
- The main vulnerability is the Powann cluster — isolated and far from home support.
- If an enemy faction enters Powann, immediately redirect Rob to assassinate their taxmen.
- Build defensive combat stack: 30+ gnolls with hunting skill (gnolls can study hunt 5) at the most valuable Powann node.
- Use ship to transport combat units from home cluster to Powann if overland route is blocked.

**If gate mage Rob is caught and fails assassinations repeatedly:**
- Catching = stealth is too low. Study stealth further (level 3+ required for harder targets).
- Alternative: use Rob as a pure gate scout rather than assassin. Observe enemy positions and report back.
- If Rob is destroyed: this is catastrophic. Recruit second leader with gate lore immediately as backup.

**If faction cap limits are hit before expansion:**
- Buy faction upgrades (Martial + Magic) as soon as income supports them. Each upgrade costs silver from the pool.
- Prioritize reaching Martial 2, Magic 3 by turn 7 as faction 60 did — the increased caps enable the second economic explosion.

**If ally Nonentity (67) requests help:**
- Faction 60 had Nonentity as Friendly throughout. Nonentity is observed capturing cities by turn 18–19. Maintain friendly status for potential trade or mutual aid. Provide silver gifts if the ally faces pressure.
- Never go Ally status unless mutual defense pact is negotiated — Ally pulls you into their wars automatically.

**If Rob in Hood finds strong city guards:**
- Single fireball kills 1 target. Against 80-leader guards, Rob cannot solo. Retreat and find weaker targets.
- Assassinate the enemy's quartermasters or key production leaders instead — economically damaging even without territory capture.

**If production base is disrupted:**
- The Powann production cluster (grain, herbs, bags, wood, ships) is self-sustaining but isolated.
- If goblins are killed, re-buy locally (Powann has goblins at $27).
- Backup production: establish a secondary production cluster near the home area for redundancy.

**If silver income collapses (pirates, monsters, faction expulsion):**
- The faction demonstrated resilience — when Sailors (3499) was destroyed by pirates, it simply rebuilt a second ship and continued.
- Always maintain 2,000+ unclaimed silver as emergency reserve.
- Entertainment units provide income even without taxing rights — always keep 3+ entertainers operational.
