# Faction 10 Strategy Analysis

## Section 1: Observed Playstyle (Turns 2–20)

### Starting Conditions

**Faction:** Red Skulls (10)  
**Starting Type:** Martial 1, Magic 1  
**Starting Location:** mountain (44,26) in Dayiam, containing the village of Crinday — a human-populated mountain hex with 3,035 peasants, $971 tax base, $11.6 wages, wanted grain/livestock/fish, for sale 121 humans at $37, 24 leaders at $649.  
**Neighbors:** surrounded by mountain hexes (Dayiam region), a volcano (43,25), and within 1-2 hexes of a major city — Trie'enchbra [city] in plain (42,26) Furswudost (10,272 gnolls, $11,299 tax base).

**Initial Units (Turn 1 formation):**
- Gurgoth (864): Leader mage — starts with force 1, pattern 1, spirit 1, gate lore 1, fire 1, combat 3, farsight 1, observation 1. Combat spell: fire. This is the primary mage.
- Murgoth (1228): Leader — begins studying tactics immediately (goal: tactics 5)
- Disastroth (1238): Leader — begins studying force, then fire; second mage path
- workers (1233): 5 humans — mining study
- worker (1234): 1 human — mining
- worker (1235): 1 human — quarrying
- worker (1236): 1 human — farming
- workers (1237): 5 humans — building
- 9 scouts formed from Turn 1 orders, each buying 1 human at $37 from local market, deployed radially in all 6 directions from (44,26) plus extended paths; 5 of them also withdrew horses to gain mounted movement

**Starting Silver (Unclaimed):** 7,013 silver at Turn 2 start. Heavy use of CLAIM order to bootstrap all units.

**Allies:** Cone's Magicians (73) and Under Mirk Wood (18) — declared ally status from turn 3. These factions are co-located in Crinday village and their mages (Magician of Old 927 and SurfDudes) fight alongside Red Skulls in early battles.

---

### Economic Strategy

**Phase 1: Bootstrap through claims and market buying (Turns 1-2)**

Red Skulls spent down all unclaimed silver to recruit units. Every new unit CLAIM-ed its own funding. By Turn 2 report, 7,013 unclaimed silver had been deployed into 16+ units. This is a spend-everything-immediately approach — no hoarding.

**Core income mechanism: Taxation**

From Turn 3 onward, Red Skulls planted guard units in every region they scouted. The standard pattern:
- A small combat unit with `@GUARD 1` and `@TAX` was placed in each new region
- Guards collected taxes relative to their combat strength (5 silver per man-month at basic combat, more with better combat skill)
- The Crinday village home base (44,26) was the richest hex: guards (1835) collected $900 there in Turn 4, then guards (2469) collected $985-991 per turn by Turns 8-9

By Turn 8, taxes were being collected from 20+ regions simultaneously:
- mountain (45,25): ~$549 per turn
- mountain (44,26): ~$985 per turn
- mountain (46,28): ~$450 per turn
- jungle (48,28): $100-200 per turn
- plain (50,28): $1,250 per turn (large plain with high tax base)
- Multiple jungle regions in Dyni: $50-600 each
- forest (43,33) Bochunwood: $400 per turn
- Total tax income by Turn 8: approximately 4,000-5,000 silver per month

**Worker economy: Production alongside taxation**

In parallel with taxation, Red Skulls built a production workforce at the home base:
- Mining (iron): workers (1233), worker (1234) in (44,26) — producing iron from Turn 3
- Quarrying (stone): worker (1235), workers (1837) — producing stone
- Farming (livestock): worker (1236), workers (1836), and later workers (1466), (1982), (2223) at mountain (45,25)
- Building: workers (1237) — studied building to level 2 by Turn 4, then level 3 by Turn 10

Special resource discovery: The volcano (43,25) hex produces mithril. By Turn 9, Red Skulls had units producing mithril there (workers 1834, miners 2929, unit 2569). By Turn 10, 9 mithril were in treasury, growing to 33 by Turn 12, 65 by Turn 14, 175 by Turn 19. Mithril was transported via quartermaster system to a central hub.

**Trade and selling:**
- Livestock sold at Trie'enchbra city: worker (1227) stationed in plain (42,26) selling livestock every turn at $20 each. This city also had demand for grain and fish.
- Iron and grain sold locally to the Crinday village market at $22-23 per grain.

**Quartermaster system:** By Turn 10 (November Year 1), Red Skulls had 1 quartermaster. By Turn 14 (March Year 2), 2 quartermasters. By Turn 17 (June Year 2), 3 quartermasters. By Turn 18 (July Year 2), 4 quartermasters. By Turn 20 (September Year 2), 6 quartermasters. The quartermasters were used to transport mithril, stone, and other production resources from extractors to craft units.

**Craftsmen:** By Turn 12, workers were studying weaponsmith (WEAP), armorsmith (ARMO), and building skills. By Turn 17, mithril swords appeared in the treasury (12 mithril swords). By Turn 20, 68 mithril swords, 20 chain armor, 80 hammers, 141 picks, 64 axes, 110 picks.

**Entertainment:** One entertainer unit was placed in mountain (46,28) by Turn 6, earning $22/month. This was a minor income supplement.

**Horse training:** worker (1490) stationed at Trie'enchbra city (plain 42,26) studying horse training continuously from Turn 2 onward (goal: HORS level 5).

**Silver treasury growth:**
- Turn 4 (May Y1): 885 silver held
- Turn 5 (Jun Y1): 383 silver (post-city guard fight expenditure)
- Turn 7 (Aug Y1): 1,855 silver
- Turn 8 (Sep Y1): 3,954 silver
- Turn 9 (Oct Y1): 988 silver (expansion push)
- Turn 11 (Dec Y1): 546 silver
- Turn 12 (Jan Y2): 2,166 silver
- Turn 15 (Apr Y2): 2,428 silver
- Turn 17 (Jun Y2): 3,534 silver
- Turn 18 (Jul Y2): 5,920 silver
- Turn 19 (Aug Y2): 5,278 silver
- Turn 20 (Sep Y2): 8,368 silver

Silver in treasury was generally kept lean — reinvested heavily each turn. The unclaimed silver total (faction treasury) by Turn 20 was 1,244,573, showing massive faction wealth accumulated.

---

### Military Strategy

**Opening gambit: City Guard attack (Turn 4)**

The most striking early military action was a coordinated attack on City Guard (26) in Crinday village (mountain 44,26) at Turn 4. The guards had 40 leaders with swords and combat 1. Red Skulls attacked with:
- Gurgoth (mage, combat 3) — fire spells
- Disastroth (mage) — fire spells
- Magician of Old (927) from allied Cone's Magicians — fire spells (combat 3)
- Murgoth (tactics 1 tactician)
- 20+ human fighters

The city guard was destroyed, yielding 20 swords and 1,000 silver in spoils. This was the foundation move — capturing Crinday village to begin taxing the highest-tax hex. The swords were distributed to combat units.

**Turn 5: Monster clearing**

Red Skulls immediately began clearing creatures:
- Grizzly Bears (354) at mountain (45,27): destroyed by guards (1838) with mage support
- Family of Ogres (689) at mountain (44,28): attacked but repelled in Turn 5 — the demons were too strong (8 demons with combat 4/4 and 12 attacks). Red Skulls lost 37 men to the demon counter-attack (routed). 
- The ogres were eventually defeated by Turn 17 — workers (2103) with guards (2469) and Thane (2329) tactician + militia units.

**Standard military template:**
- Each new region: 1 guard unit (9-10 men at combat 1) placed on guard for taxation
- The guard unit's spoils setting was `spoils none` or `spoils walk` to avoid carrying heavy items
- Smaller 1-2 man units acted as scouts, then transitioned to tax collectors when placed behind a guard

**Expansion army composition (Turn 6-8):**
- Multiple units buying race-appropriate troops in each region (hill dwarves in mountains, orcs/lizardmen in jungles, wood elves in forests, high elves in plains)
- Guards studied combat continuously to level 2
- Thane (2329): a second tactics leader created in Turn 9 at mountain (44,26), studying tactics to level 2, funded by guard tax income

**Combat force quality:**
- Mithril swords produced and distributed to militia and guard units by Turns 17-20
- By Turn 20: 70 swords + 68 mithril swords in treasury, 20 chain armor, 7 pikes
- militia (3106): 7 hill dwarves with picks and mithril swords
- militia (3311): humans with picks and swords

**Enemy encounters:**
- Turn 9: Red Skulls scouts were attacked by Shestoper (36) faction in swamp regions (42,30) — guards (2505) with 5 men destroyed. This marked border conflict with a rival faction.
- Turn 13: Battle between Red Skulls lizardman scout (2365) and Shestoper goblin scout (2362) in swamp (40,26) — indecisive.
- Turn 14: Shestoper attacked Red Skulls unit (2265) with gnolls in plain (39,23) — indecisive.
- Turn 20: Red Skulls unit (5673) gnoll attacked by Shestoper's force (890 mage + 40+ orcs) in swamp (40,30) — Red Skulls unit destroyed. This shows ongoing border friction.

**Naval activity (late game):**
- By Turn 20, sailors unit (3429) existed with 2 high elves. Longships being built and transferred to fleets (Fleet 221, 222, 223). Sailors attacked in ocean (42,28) by Shestoper lizardman scouts — sailors won with help of 15-human escort unit.

---

### Magic Development

**Gurgoth (864) — Primary Mage:**
- Start: force 1, pattern 1, spirit 1, gate lore 1, fire 1, farsight 1, combat 3, observation 1
- Turn 2: Studies farsight (pushed to 100 silver/month study)
- Turn 3: Casts farsight on ocean (48,22) to scout remotely
- Turn 4: Studies force, casts farsight on (44,34) for further scouting
- Turn 5: Studies force, casts farsight on (40,30) — looking west/south
- Turn 6-7: Stationed at Crinday, studying force; casting farsight used for scouting; teaching Disastroth fire
- Gurgoth used as combat mage in all early battles with fire spell

**Disastroth (1238) — Second Mage:**
- Start: force 1
- Turn 2: Studies fire (taught by Gurgoth +30 days)
- Turn 3: Studies spirit
- Turn 4: Studies spirit (after getting fire 1 from teaching)
- Used fire spell in City Guard battle (Turn 4) and against bears/ogres
- By Turn 5 report: Disastroth has force 1, fire 1

**Waldemar (3243) — Third Mage:**
- Appeared by Turn 15 in battle at plain (42,26) — identified as a Red Skulls leader. Participated in the Cone's Magicians attack on City Guard (25) at Trie'enchbra.
- By Turn 19: getting funding but insufficient funds noted (STUDY: Not enough funds)

**Key Magic observations:**
- Magic was used primarily for Farsight scouting in early turns (Gurgoth casting Farsight 1-2 times in turns 2-5)
- Fire spell was used in all early battles as the primary combat spell (5 attacks per cast at level 1)
- The faction had 2 mage slots for the first year (Magic 1 → Magic 2 rating). Faction type changed from "Martial 1, Magic 1" to "Martial 3, Magic 2" by Turn 5 (June Year 1) after spending unclaimed silver to upgrade.
- By Turn 20, the faction had downgraded to "Martial 4, Magic 1" — suggesting a deliberate reallocation of faction points toward martial expansion.
- Apprentices: always 0 throughout (0 of 3/5 slots used) — Red Skulls never pursued apprentices despite the available slots.

**Magic gap:** Despite having mages from turn 1, magic development was slow and primarily combat-focused. No advanced spells beyond fire are evident in the battle logs through Turn 20. The mages appear to have been mostly studying other skills (force, spirit, pattern) and using farsight, rather than developing new offensive spells.

---

### Expansion Pattern

**Turn 2 (March Y1):** 0 regions controlled. 9 scouts deployed in radial pattern from home hex.

**Turn 3 (April Y1):** 1 region (Crinday village). Scouts reach: mountain (44,24) N, mountain (45,25) NE, jungle (47,27) NE-far, mountain (44,28) S, mountain (45,29) SE, volcano (44,30) further S, mountain (46,30) further SE, volcano (43,25) NW, plain (42,26) NW (city). Immediate purchase of dwarves for guards in mountains, buying race-specific troop types in each region.

**Turn 4 (May Y1):** 6 regions. Guards placed in mountains: (44,24), (45,25), (44,26), (45,27), (44,28), (45,29). Multiple new FORM'd units creating guard/worker pairs for each region.

**Turn 5 (June Y1):** 6 regions — consolidating. New units in Dyni jungles (47,27, 48,28, 46,32). Scouts pushed to Darun plains (50,28, 50,30) and more Dyni jungles.

**Turn 6 (July Y1):** 8 regions. Continued push into Dyni jungle chain and Darun plains. Scout (2170) swimming in ocean to reach distant regions (Cedid mountain at 49,25).

**Turn 7 (August Y1):** 13 regions. Major push: guards established in plain (50,28) Darun (large tax base), jungle regions (47,33), (46,34), (45,35), (47,35), forest (43,33) Bochunwood.

**Turn 8 (September Y1):** 17 regions. Tax collection now occurring in 20+ locations. Scouts probing swamp regions to the west (Ceo'ow/Quaytre). Guards at mountain (49,25) Cedid.

**Turn 9 (October Y1):** 16 regions (slight contraction — some scouts lost to combat). First hostile engagement with Shestoper (36) faction in swamp regions.

**Turn 11 (December Y1):** 14 regions. Consolidation phase — some outer regions apparently lost or voluntarily abandoned.

**Turn 12 (January Y2):** 17 regions. Mages count: 1 (first mage completing some skill to threshold). Quartermasters: 1.

**Turn 13 (February Y2):** 16 regions.

**Turn 14 (March Y2):** 17 regions. Second mage and second quartermaster.

**Turn 15 (April Y2):** 20 regions. Joined Cone's Magicians attack on City Guard (25) at Trie'enchbra city — allied faction takes the city. Scout (2271) probing far western regions (swamp 42,20, ocean regions). Scout (2170) "wanderer" roaming widely in northern ocean/tundra regions.

**Turn 16 (May Y2):** 22 regions.

**Turn 17 (June Y2):** 27 regions. Third quartermaster. Mithril production fully operational.

**Turn 18 (July Y2):** 28 regions. Fourth quartermaster.

**Turn 19 (August Y2):** 36 regions. Approaching region cap of 40. Faction points upgraded — limit appears to have been raised (60 regions at Turn 20 suggests Martial 4 faction upgrade).

**Turn 20 (September Y2):** 37 regions. Faction type: Martial 4, Magic 1. Region cap: 60. Quartermaster cap: 14. Mage cap: 2.

**Expansion method:**
1. Scout wave: 1-2 man scouts deployed in all directions simultaneously, buying race-appropriate troops in each new region
2. Guard formation: `FORM` a combat unit in each region, buy local race troops, study combat, set `@GUARD 1 @TAX`
3. Worker formation: `FORM` a worker unit alongside guard, buy race-appropriate troops, study farming/mining
4. The guard unit funded the worker units through `GIVE` or shared income
5. Each established region then spawned more scouts going further out

**Race matching strategy:** Red Skulls consistently bought the local dominant race for each region type:
- Mountains (Dayiam): hill dwarves (HDWA) — best for mining/quarrying/weaponsmith/armorsmith
- Jungles (Dyni): lizardmen (LIZA), wood elves (WELF), orcs (ORC)
- Plains (Darun/Furswudost): gnolls (GNOL), high elves (HELF)
- Forests: wood elves (WELF), high elves (HELF)
- Swamps: goblins (GBLN), lizardmen (LIZA)
- Cedid mountains: orcs (ORC)

---

### Turn-by-Turn Summary

**Turn 1 (January Y1, no report):** Single unit Gurgoth exits nexus to mountain (44,26). Orders show extensive formation of initial units via CLAIM and BUY — total of 16 units formed from unclaimed silver in the nexus region before entering the world.

**Turn 2 (February Y1) — March Y1 report:** 
- 9 scouts deployed radially from home hex (44,26)
- Two mages (Gurgoth, Disastroth) studying magic skills
- Murgoth studying tactics
- Workers studying mining, quarrying, farming, building
- Gurgoth teaching Disastroth fire spell
- 885 silver in treasury after unit purchases
- Ally declarations: Cone's Magicians (73), Under Mirk Wood (18)

**Turn 3 (March Y1) — April Y1 report:**
- Gurgoth casts Farsight on ocean (48,22) for scouting
- Guards formed in mountains (45,25): 9 hill dwarves buying combat
- Workers in mountains: 3 hill dwarves mining
- Scouts reach plain (42,26), jungle (47,27)
- New FORM units: 20 human guards at (44,26), 25 human farmers, 10 human quarriers, 6 human guards at (45,27)
- Gurgoth teaches Disastroth, SurfDudes from faction 18

**Turn 4 (May Y1) — KEY TURN:**
- **City Guard attack and victory** — Cone's Magicians (Magician of Old 927) leads combined attack on City Guard (26) at Crinday village
- Spoils: 20 swords, 1,000 silver
- 6 regions controlled
- Scouts reach Dyni jungles, Darun plains
- 885 silver treasury

**Turn 5 (June Y1) — Two battles:**
- Grizzly Bears defeated at (45,27) — clean win with mage support
- Family of Ogres at (44,28) — REPELLED. Demons killed 37+ Red Skulls troops in rout. Important lesson: some creature lairs are too strong for initial attacks.
- Faction upgraded to Martial 3, Magic 2 by spending unclaimed silver
- Lizardmen and wood elves purchased in new jungles
- Scout (1227) stationed at Trie'enchbra city to study farming/horse training
- Workers begin building Caravanserai (faction-level building)

**Turn 6 (July Y1):**
- 8 regions
- Guards placed across 20+ regions now collecting taxes
- Silver generation takes off — unclaimed faction wealth growing fast
- Many units buying race-appropriate troops in newly reached regions
- Workers (1834), (2014) move to volcano (43,25) to begin mithril production prep

**Turn 7 (August Y1):**
- 13 regions — major expansion through Dyni jungle chain
- Hill dwarves heavily recruited for skilled production (weaponsmith, armorsmith)
- Anacondas attack and kill guards (1615) — a 1-man guard unit lost to jungle predators
- Second tactics leader (Thane 2329) being funded and studied

**Turn 8 (September Y1):**
- 17 regions
- Tax income from 20+ locations
- Guards (2505) destroyed by Shestoper (36) forces — first inter-faction combat loss
- Hill dwarves now accumulating: 72 in treasury (rank 1 globally)
- Mithril mining operational at volcano (43,25): 9 mithril in treasury
- Production workforce: miners, quarriers, farmers, woodcutters all studying

**Turn 9 (October Y1):**
- 16 regions — small contraction after frontier losses
- Weaponsmith, armorsmith, observation skill units being trained at mountain (45,25) hub
- First quartermaster being established

**Turn 10 (November Y1):**
- 14 regions (consolidation)
- Mithril production accelerating: 30 iron and 44 stone in treasury
- Thane (2329) with tactics 1 established as battle commander
- Building skill level 3 being studied — enables Tower/Fort construction

**Turn 11 (December Y1):**
- 14 regions
- Mages: 0 counted — suggests Gurgoth/Disastroth lost or demoted? (Error in faction type accounting)
- Mithril picks, hammers appearing in treasury
- Guards transferring mithril to central production hub via transport

**Turn 12 (January Y2):**
- 17 regions. Mages: 1
- Picks, hammers produced from mithril — these are superior production tools
- 33 mithril in treasury
- Workers buying high elves (HELF) in plain (50,28) Darun for skills
- Observation units trained for enhanced scouting

**Turn 13 (February Y2):**
- 16 regions. Mages: 1
- Border skirmish with Shestoper lizardman and goblin scouts in swamp (40,26) — indecisive fight

**Turn 14 (March Y2):**
- 17 regions. Mages: 2. Quartermasters: 2
- Shestoper (36) attacks Red Skulls gnoll unit (2265) in plain (39,23) — indecisive
- Cone's Magicians attack City Guard (25) at Trie'enchbra city with allied forces
- Red Skulls Waldemar (3243) and builders (1869) participate in the city assault
- Mithril swords being produced (workers 2797)
- Bags, lassoes, axes, picks, hammers all in production

**Turn 15 (April Y2):**
- 20 regions. Mages: 2. Quartermasters: 2
- Under Mirk Wood (18) forces battle Sea Dogs (Shestoper) at Furswudost city
- Red Skulls continuing to expand northwest (swamp regions, plains)
- Centaurs being purchased in forest (50,24)
- Magic wagons (MWAG) appear in treasury — advanced transport items

**Turn 16 (May Y2):**
- 22 regions. Mages: 2. Quartermasters: 2
- Workers at swamp hub (42,22) studying lumberjack and observation
- Guards at mountain (48,24) Cedid adding orc farmers
- High elves produced in Darun plain region for specialized workers
- 124 mithril in treasury — production fully mature

**Turn 17 (June Y2):**
- 27 regions. Mages: 2. Quartermasters: 3
- Family of Ogres (44,28) finally defeated — workers (2103) and guards (2469) with Thane and militia
- Mithril sword production: 12 mithril swords in treasury
- Ironwood appearing in treasury (specialized wood from some region)
- Naval activity beginning: sailors being trained

**Turn 18 (July Y2):**
- 28 regions. Mages: 2. Quartermasters: 4
- Shestoper attacks Red Skulls scout (3719) in forest (49,23) — Red Skulls loses
- 146 mithril in treasury; 12 mithril swords, 64 swords
- 76 horses — cavalry force being built
- Gnolls accumulated: 49 in treasury (growing rapidly)

**Turn 19 (August Y2):**
- 36 regions. Mages: 2. Quartermasters: 4
- Approaching old region cap of 40 — faction upgrades to Martial 4 to increase cap to 60
- Shestoper (36) force attacks Red Skulls gnoll (5673) at swamp (40,30) — loses to Shestoper mage with fireball
- 178 mithril, 48 mithril swords
- Magic wagons (5) in treasury — transport optimization
- 211 humans, 110 lizardmen, 109 gnolls — large multi-race force

**Turn 20 (September Y2):**
- 37 regions. Martial 4, Magic 1. Region cap: 60. Quartermaster cap: 14. Mage cap: 2
- Multiple battle logs: sailors defending at sea against Shestoper
- Red Skulls unit (5673) destroyed by Shestoper mage in swamp
- Large production economy: 80 hammers, 141 picks, 64 axes, 129 nets, 123 lassoes
- 70 swords + 68 mithril swords in distribution
- Active fleet building: longships being built and transferred to fleets
- Cotton (8) in treasury — trade goods appearing

---

### Strengths and Weaknesses

**Strengths:**

1. **Aggressive, well-organized early expansion.** From Turn 2, scouts were deployed in all 6 directions simultaneously. Each scout immediately bought local race troops and formed guard/worker sub-units. This created a rapid territorial claim wave.

2. **Tax income scaling.** The tax model — plant a combat guard, collect taxes — scaled linearly with the number of regions captured. By Turn 8, 20+ tax collection points existed. The home base (Crinday village) alone yielded ~$985/turn.

3. **Race-matching.** Buying the locally available race in each region maximized both market volume (you can buy more of them) and skill ceiling (hill dwarves can mine/weaponsmith to level 5; wood elves for herbalism).

4. **Mithril access from Turn 1.** The volcano (43,25) in the starting neighborhood produces mithril, giving a significant material advantage. By Turn 12, mithril picks and hammers were enabling higher production rates across the economy.

5. **Allied coordination.** The alliance with Cone's Magicians (73) provided a powerful mage (Magician of Old) who dealt more damage in the Turn 4 city guard fight than Gurgoth and Disastroth combined. Under Mirk Wood (18) also contributed significantly.

6. **Sharing + fractional funding.** The `share 1` order and explicit `GIVE X Y SILV` patterns meant that large guard units funded adjacent worker/specialist units without requiring separate income streams. This reduced complexity.

7. **Worker specialization by race.** By Turn 9-12, weaponsmith (hill dwarves), armorsmith, lumberjack (lizardmen), farming (humans/orcs), mining (hill dwarves) were all being studied simultaneously in appropriate locations.

8. **Quartermaster logistics.** The transport system for mithril and production goods was established early (Turn 8 references transport orders), growing to 6 quartermasters by Turn 20. This enabled centralized craft production.

**Weaknesses:**

1. **Late magic development.** Despite having 2 mage slots and Gurgoth with strong starting skills, magic advanced slowly. Gurgoth appeared to be studying force primarily (not advancing combat spells). Disastroth studied spirit and pattern rather than pushing fire to higher levels. By Turn 20, still using basic fire spell. No advanced spells (earthquake, force shield, weather lore, etc.) were evident in battle logs through Turn 20.

2. **No apprentices trained.** 0 of 3-5 available apprentice slots were filled through Turn 20. Apprentices could have been trained to serve as additional combat mages or skill teachers.

3. **Tactical errors — attacking too early.** The Family of Ogres (44,28) in Turn 5 was attacked prematurely — the Demon companions (8 demons, combat 4/4) were far beyond the ability of Turn 5 forces to handle. 37+ men were lost in the rout. The ogres weren't defeated until Turn 17 (12 turns later), suggesting this lair was a persistent drain on military planning.

4. **Spreading too thin vs. Shestoper.** Red Skulls had single-man scout units in swamp/western regions adjacent to Shestoper territory. These were easily picked off (guards 2505 destroyed in Turn 9). Red Skulls' response was not to concentrate force but to continue expansion, leading to ongoing piecemeal losses.

5. **Silver management inconsistencies.** Several turns had `TAX: Unit cannot tax` errors, suggesting newly-formed units were given tax orders before they were combat-ready. Also, multiple `BUY: Unit attempted to buy more than it could afford` errors, especially in Turns 5-7, suggesting funding allocation was imprecise.

6. **Ordering errors.** Many minor order errors: `wname is not a valid order`, `withraw` instead of `withdraw`, `-1 is not a valid order`, `xxx is not a valid order`. These indicate rushed or poorly proofread orders and some turn-over problems.

7. **Delayed Fort construction.** Building skill was studied from Turn 1 but Fort construction wasn't ordered for the main base (44,26) until Turn 5 (workers 1237 ordered `build caravanserai`). A Fort would have allowed mages to study above level 2 — this delay limited Gurgoth's development.

---

## Section 2: AI Agent Strategy (Based on This Playstyle)

### What the AI Would Keep

1. **Radial scout wave on Turn 2.** The immediate deployment of 9 scouts in all directions is the correct move. Scouts with horses can cover 2 moves, reaching hexes 2 away. AI should replicate this with at least 6 scouts, each buying 1 local troop to carry information back.

2. **FORM+BUY workers in every region from Turn 2-3.** Creating guard and worker sub-units inside the scout units using FORM, with `share 1` so the guard funds the worker, is efficient and self-sustaining. AI should use this pattern.

3. **Tax collection as primary income.** The `@GUARD 1 @TAX` pattern on all combat units is correct. It provides consistent per-turn income without requiring player-side silver management. Scale this to every captured region immediately.

4. **Race-appropriate buying.** AI should check regional for-sale items and buy the best available race for the planned skill. Hill dwarves for mining/production mountains, orcs/lizardmen for jungles, high elves for forests/plains.

5. **Mithril and special resource extraction.** Identifying and immediately deploying miners to volcano/special hexes is correct. AI should scan for non-standard PRODUCE items (mithril, rootstone, ironwood) in every region and assign appropriate miners.

6. **Livestock farming and selling.** Farming livestock in high-wage plains and selling at nearby cities is a reliable secondary income. AI should place at least 1 farmer unit at each city access point.

7. **Quartermaster logistics from mid-game.** Setting up a central production hub with quartermaster transport is sound. AI should designate a hub hex and route all raw materials there for processing.

8. **Alliance maintenance.** Declaring ally status early on Cone's Magicians and Under Mirk Wood (18) gave Red Skulls a powerful mage (Magician of Old) in battles from Turn 3. AI should seek out allied mages and coordinate attacks.

9. **Building skill investment.** Building to level 3 enables Forts which allow mages above level 2. AI should start this investment on Turn 2.

### What the AI Would Change

1. **Magic development should be the top priority, not an afterthought.**
   - Red Skulls delayed mage advancement and never developed Gurgoth's full potential. Gurgoth had access to earthquake, force shield, energy shield, spirit shield, magical healing, weather lore, earth lore, necromancy, demon lore, and more from Turn 2.
   - AI should push Gurgoth to study fire to level 3 (5 attacks → much more powerful) and then either earthquake or force shield by Turn 8.
   - Disastroth should have been pushed to fire 2 faster by teaching more aggressively.
   - Recommendation: Gurgoth studies fire → force (to unlock) → force shield → earthquake. This gives both defensive (force shield blocks melee) and offensive (earthquake hits all non-behind units) capability by mid-game.

2. **Build Fort at home base by Turn 4, not Turn 5+.**
   - A Fort at Crinday costs 40 stone (quarrying from turn 1 should accumulate this by Turn 3-4).
   - Forts allow mages to study above level 2. Red Skulls had quarriers producing stone from Turn 3 and builders studying building from Turn 1 — there is no reason they couldn't have built a Fort by Turn 4.
   - AI should prioritize: 1 builder unit, quarry stone, build Fort as soon as builders hit level 2 and 40 stone are available.

3. **Train apprentices.**
   - Red Skulls used 0 of 3-5 apprentice slots through Turn 20. Apprentices are leaders with magic skills who can serve as teachers, additional combat mages, or specialists.
   - AI should designate 2-3 leaders as apprentices immediately — buy them from the market (24 leaders available in Crinday at $649) and have Gurgoth teach them basic magic skills (fire, force, pattern, spirit) so they can reach apprentice qualification.
   - Having 3 apprentices allows teaching larger groups and accelerates skill development across all mage-line units.

4. **Attack creatures more carefully — assess before engaging.**
   - Red Skulls attacked the Family of Ogres (44,28) at Turn 5 when they had no way to know demons were also in the lair. This cost 37+ men.
   - AI should use CAST Farsight to view a region before attacking if there are monsters there. If the lair appears to have multiple powerful creature types, wait until mage fire level is higher or build a proper attack force.
   - Rule: Do not attack monsters with combat 3+ unless the attack force includes a mage with fire 2+ or force shield.

5. **Secure borders before over-expanding.**
   - Red Skulls expanded rapidly but left single-man units on the Shestoper border which were easily destroyed. This created a recurring drain.
   - AI should establish a defensive line (3-5 man guard units on the border, not 1-2 man) when entering contested territory. Only expand beyond that line after the border is secured.

6. **Eliminate FORM+BUY errors through silver pre-allocation.**
   - Multiple turns had `BUY: Unit attempted to buy more than it could afford` — units were told to buy troops they couldn't afford.
   - AI should calculate: (guard silver) - (maintenance cost) = available for buying. Ensure GIVE orders to sub-units happen before BUY orders in the same hex.

7. **Use Farsight more aggressively for scouting.**
   - Gurgoth cast Farsight only 2-3 times in the first 10 turns despite having the skill from Turn 1.
   - Farsight at level 1 can reach regions up to 4 hexes away; at level 2, up to 16 hexes. This is far more efficient than sending scouts across ocean/hostile territory.
   - AI should cast Farsight every turn Gurgoth is not in combat, targeting the edges of the known map to plan expansion routes.

8. **Pursue entertainment income earlier.**
   - One entertainer was placed in mountain (46,28) by Turn 6. Entertainment income is passive and grows with skill level.
   - AI should place 1-2 entertainment units in high-population hexes (cities or large villages) from Turn 3. Bards (entertainment + music or other skills) can earn significant passive income.

9. **Upgrade faction type to Martial 3 earlier.**
   - Red Skulls upgraded from Martial 1/Magic 1 to Martial 3/Magic 2 by Turn 5 (June Y1) — this gave 40 region slots, 9 quartermaster slots, 3 mage slots, 5 apprentice slots.
   - AI should plan this upgrade by Turn 3-4 when silver reserves are sufficient. The faction point cost should be calculated before spending on units.
   - Also: switching to Martial 4/Magic 1 later (as Red Skulls did by Turn 20) increases the region cap significantly but cuts mage slots. AI should carefully evaluate this tradeoff — keeping Magic 2 longer is preferable if mage spells are being developed.

10. **Produce and distribute weapons earlier.**
    - Mithril swords didn't appear until Turn 17 despite mithril being mined since Turn 7-8. Weaponsmiths were not trained until Turn 9.
    - AI should start weaponsmith training (hill dwarves) from Turn 3 at the first available mountain hex. Mithril weapons in the hands of guards by Turn 12-13 would significantly improve combat effectiveness.

---

### Recommended Opening (Turns 1–5)

**Turn 1 (Nexus → World):**
- Move Gurgoth out of nexus to starting hex
- Set combat spell: fire
- In the starting hex, FORM all initial units from unclaimed silver:
  - FORM 1: Murgoth (leader, buy with claim) — study tactics, goal level 5
  - FORM 2: Disastroth (leader, buy with claim) — study force, will become second mage
  - FORM 3: workers × 5 (5 humans) — study mining, goal level 5
  - FORM 4: builders × 5 (5 humans) — study building, goal level 2 then 3
  - FORM 5: farmers × 5 (5 humans) — study farming
  - FORM 6-11: scouts (1 human each + 1 horse each) — move N, NE, SE, S, SW, NW + extended scouts (NW×2, NE×2, SE×2)

**Turn 2 (First region report):**
- Gurgoth: study fire (to get to fire 2 faster); teach Disastroth force and fire simultaneously
- Murgoth: study tactics
- Disastroth: study force (to enable fire shield and energy shield branches)
- Workers: buy more humans locally, study mining
- Builders: buy more humans locally, study building
- Farmers: buy locally, study farming
- All scouts: upon arriving in new regions, FORM guard (buy local race, study combat) and FORM worker (buy local race, study appropriate skill)
- In home hex: FORM 20-man human guard unit, study combat; FORM 25-man farming unit; FORM 10-man quarrying unit
- Declare Ally: known allied factions (if Cone's Magicians and Under Mirk Wood are present)

**Turn 3:**
- Gurgoth: CAST Farsight on 2-3 target regions ahead of scouts; study fire (continue)
- Disastroth: study fire (50% faster due to teaching)
- Start building stockpile: quarriers should have 5-10 stone; miners have 5-10 iron
- Builders: when building skill reaches 2, order BUILD Tower (10 stone), then accumulate 40 stone for Fort
- Each new region guard: `@GUARD 1 @TAX @spoils walk`
- FORM new mining/farming units at established regions

**Turn 4 (City guard attack if Crinday-equivalent):**
- If an allied mage (Cone's Magicians equivalent) is available, coordinate attack on city guard
- Gurgoth: fight with fire spell; set `spoils walk` so mage can move freely after battle
- Distribute sword spoils to combat units immediately
- If no city attack possible, continue studying magic
- Order Fort construction if 40 stone accumulated

**Turn 5:**
- Evaluate all monster lairs via Farsight before attacking
- Do NOT attack lairs with demon-type units until Gurgoth has fire 2+ or force shield 1+
- Upgrade faction type if silver permits (Martial 3, Magic 2 minimum)
- Begin apprentice recruitment: have Gurgoth teach basic magic (force 1, pattern 1, spirit 1) to 1-2 purchased leaders — declare them apprentices when they qualify

---

### Mid-Game Plan (Turns 6–15)

**Regions: Target 20+ by Turn 10, 30+ by Turn 15**

1. **Magic:**
   - Gurgoth: fire → force shield → earthquake by Turn 12. This makes Gurgoth nearly untouchable in melee (force shield blocks physical attacks) and devastating in area (earthquake hits all non-hidden enemies).
   - Disastroth: fire 2 by Turn 8 (through teaching). Then push to fire 3 if possible.
   - Apprentices: Have 2-3 apprentices studying fire and pattern, preparing to become independent combat mages.

2. **Economy:**
   - Establish 2 quartermaster hubs: one at home base, one at a mid-distance production center
   - Route mithril, stone, iron to hub for weaponsmith/armorsmith output
   - Target: 5 mithril sword units produced per month by Turn 10
   - Maintain livestock selling at 1-2 city markets for supplementary income
   - Entertainment: 3+ bard units in high-population hexes

3. **Military:**
   - Each guard unit: combat 2 by Turn 10 (hill dwarves with 5 months of study)
   - Equip all guards with at minimum 1 sword each; priority to mithril swords
   - Thane (tactics leader): develop to tactics 3 by Turn 12 for maximum battle bonus
   - Fleet building: start constructing rafts/longships by Turn 12 for ocean exploration and distant region access

4. **Territorial:**
   - Secure a defensive border against rival factions by Turn 8: 5+ man guard units on contested hexes
   - Expand into ocean islands and tundra regions using swimming lizardmen and boat-capable units
   - Avoid attacking city guards directly without allied mage support — coordinate with allies for city captures

5. **Production tree completion:**
   - Hill dwarves: weaponsmith 5, armorsmith 5, mining 5 by Turn 12
   - Humans: farming 5, building 5, quarrying 3
   - Wood elves: herbalism 5 (herbs for alchemy), lumberjack 5
   - High elves: study advanced skills accessible only to high elves
   - Orcs: farming 4, mining 3

---

### Adaptations for Dynamic Conditions

**If starting location has no mithril access:**
- Substitute iron for weapons production; prioritize buying iron from nearby markets
- Send scouts specifically looking for volcano hexes (they produce stone + iron at higher rates, and often mithril)
- Use picks (produced from iron at smithing) to increase mining output per man-month

**If an enemy faction borders your starting area early:**
- Pull back single-man scouts; establish 5-man minimum guards on the border
- Cast Farsight on their territory each turn to monitor military buildup
- Do not attack their guards unless you have clear force superiority (mage + 2x their numbers)
- Seek diplomatic resolution if they have mages and you don't yet have force shield

**If allied factions are absent:**
- Red Skulls relied heavily on Cone's Magicians' Magician of Old for the city guard fight. Without this ally, the Turn 4 attack might have failed or been much more costly.
- If no allies, AI should delay city guard attacks until Gurgoth reaches fire 2 (5 attacks per cast) and Disastroth reaches fire 2. This may push the city attack to Turn 6-7.
- Alternatively, build up a large human army (50+ fighters) to overwhelm the city guard through numbers.

**If high-value hex is distant from start:**
- If the nearest large city or mithril volcano is 3+ hexes away, prioritize getting a mounted scout there by Turn 2
- Deploy workers with the scout immediately to establish production
- Consider the "wanderer" pattern: Red Skulls used unit 2170 as a long-range explorer (swimming across oceans, entering underground via `move 1 in`). Lizardmen with swimming capacity are ideal for this.

**If faction points are limited:**
- Red Skulls went from Martial 1/Magic 1 → Martial 3/Magic 2 early, which is expensive in faction points.
- If unclaimed silver is low, prioritize Martial rating over Magic rating: more regions = more tax income = more silver = can eventually afford mage development.
- However, do not drop below Magic 1 (minimum 1 mage slot) — having at least 1 mage with fire is essential for creature clearing and city guard fights.

**If creature lairs contain high-tier monsters:**
- Do not attack caves with dragons, lairs with rocs, or ruins with ogre+demon combos until Gurgoth has fire 2 and force shield 1.
- Use Farsight to assess lair contents before each potential attack.
- Demons (combat 4/4, 12 attacks each) require multiple fireballs per round to kill — this demands fire level 2+ or combined mage attack.
- Giant birds (rocs) and anacondas can be avoided by simply not entering their hex; focus expansion in other directions.

**Resource diversification:**
- If mithril becomes unavailable (exhausted), pivot to ironwood (from forest hexes with lumberjacks) and rootstone (from underworld/cave hexes via underground move).
- These alternative special materials can also produce high-quality items.
- Maintain both a surface expansion and an underworld exploration thread — Red Skulls used `move 1 in` to enter underground areas, which have unique resources and safe exploration space away from rival factions.

**If the game reaches Turn 15+ with 30+ regions:**
- At this stage, the primary constraint shifts to quartermaster capacity and unit upkeep cost.
- AI should consolidate by merging small single-man units into full-sized groups (5-10 per unit)
- Focus production on goods that can be sold at city markets (luxury items, weapons, food) for silver income beyond just taxation
- Develop a naval force for sea-lane control — Red Skulls built longships starting around Turn 19-20; this should happen earlier (Turn 12-14) to enable island region capture.
