# Faction 30 Strategy Analysis

Faction: **Trader Enclave (30)**
Data range: Turns 1–20 (January Year 1 through September Year 2)

---

## Section 1: Observed Playstyle (Turns 1–20)

### Starting Conditions

**Faction name:** Trader Enclave (30)
**Faction type at start:** Martial 1, Magic 1 (Turn 1). Upgrades to Martial 3, Magic 2 by Turn 3 (April Year 1). By Turn 9 (October Year 1) transitions to Martial 4, Magic 1. By Turn 13 (February Year 2) reaches Martial 5 with only 1 Magic slot.

**Starting units (Turn 1 in nexus / Turn 2 visible in reports):**
- Unit 884 "Big Fat Trader": Leader, the primary mage. Starts with: observation 1, force 1, pattern 1, spirit 1, gate lore 1, fire 1, combat 3, and gains stealth 1 on turn 1. Combat spell: fire. Uses `CAST GATE RANDOM` every turn to jump between gates. Cost 50 silver/turn for maintenance.
- Unit 1373 "workers": 3 ice dwarves. Starting region tundra (4,82) in Febefe. Studies combat, guards and taxes.
- Unit 1374 "trader": 1 ice dwarf in tundra (4,84). Studies combat.
- Unit 1375 "trader": 1 ice dwarf in tundra (5,83). Studies combat.
- Unit 1376 "trader": 1 ice dwarf in tundra (5,81) — killed by Ice Wurms in Turn 3.

**Starting location cluster:** Tundra (4,82) in Febefe, near the gnome city E'egrad (5,79) and gnome city Meldorf (6,82). The starting area is ice dwarf territory. Turn 1 orders show Big Fat Trader at (4,82) which then gate-jumps to jungle (60,22) in Clafluspo.

**Starting silver:** ~10,032 unclaimed silver (Turn 2). The faction claims Times reward of 200 silver/turn throughout the game.

**Race mix at start:** Ice dwarves (combat/weaponsmith/mining to level 5) as the core labor force. Quickly supplemented by orcs (turn 3), gnomes (turn 3), gnolls (turn 3).

**Diplomatic stance:** Default Neutral. Explicitly unfriendly to Creatures (2). By turn 6, declares friendly to Silver Hand (25) and Carnival of Shadows (61). By turn 13 also friendly to trade group (11) and Fon (8). Never goes ally until very late game.

---

### Economic Strategy

Faction 30 employs a comprehensive, multi-pillar economic strategy that scales rapidly:

**Pillar 1: Tax Income via Regional Guards**
The primary early income mechanism. Starting as early as Turn 2 (March Year 1), units 1373, 1374, 1375 guard and tax their home regions. By Turn 4, workers (1373) collects $250/turn, workers (1953) collects $300/turn, trader (1947) collects $150/turn from swamp (59,21), workers (1946) collects $250/turn in jungle (60,22), trader (1949) collects $150/turn from jungle (60,24), and trader (1374) collects $50/turn from (4,84). Total tax income by Turn 5: ~$1,450/turn from approximately 7 regions.

By Turn 6 (July Year 1), regions controlled = 15 and growing rapidly. Tax income scales proportionally as each new region occupied gets a small guard unit taxing it. The pattern: one multi-man "workers" or "traders" unit guards each region and uses `@tax` with `share 1` to allow subsidiary units to use that income.

**Pillar 2: Trade Good Arbitrage (Perfume)**
The most profitable single trade route. Unit 1951 "trader" (gnome with horse, riding in E'egrad city) buys 10 perfume at ~$103–105 each from E'egrad starting Turn 4, then rides to Meldorf (6,82) to sell. Report shows perfume sells for $390 each (Turn 5), yielding roughly $2,870 profit per 10 perfume (buy $1,030, sell $3,900). By Turn 7, the operation scales to 29 perfume bought at once, with two selling units. This single trade route generates ~$5,000–7,000 profit when running at full capacity.

The perfume trade continues as a recurring automated order (`@buy 25 perf` / `@sell all perf`) throughout the game. By Turns 17–20, the operation buys 25–30 perfume per turn and has two sell-side units in different cities, consistently generating massive margins.

**Pillar 3: Entertainment Income**
Units with entertainment skill entertain in cities. By Turn 4, "Trading outpost" (1950) earns $90/turn entertaining in Ma'i [town]. By Turn 5, trader (2325) earns $30/turn in E'egrad. Gnome units excel at this (entertainment to level 5). The entertainment income is a secondary stream complementing taxes.

**Pillar 4: Resource Production and Sale**
Starting Turn 5, units at Ma'i town in jungle (61,23) begin systematic resource production:
- workers (2317): farming (livestock production)
- trader (2318): lumberjack (wood production)
- trader (2320), (2321): herb lore
- trader (2319): weaponsmith

These production units output resources that are transported to market units or used internally. By Turn 12 (January Year 2), the faction holds 33 iron, 77 wood, 10 stone, 90 fish, 112 herbs — substantial production capacity.

**Pillar 5: TRANSPORT System (from Turn 12 onward)**
A key mid-game economic innovation: unit "Big Fat Trader (3558)" (a dedicated transport quartermaster) receives resources from scattered production units via the TRANSPORT order. Production units use `@transport 3558 all iron`, `@transport 3558 all fish`, etc. to centralize resources at the quartermaster. This allows mass selling of fish, herbs, and other trade goods in cities with demand. The TRANSPORT system enables economic efficiency across a large empire spanning 50+ regions.

**Silver Growth:**
- Turn 2 (March Y1): 10,032 unclaimed
- Turn 3 (April Y1): 9,334 unclaimed (expanding fast)
- Turn 5 (June Y1): treasury shows 159 silver held; expansion funded from claims
- Turn 6 (July Y1): 4,080 silver held, unclaimed still large; 121,093 game-wide silver
- Turn 7 (August Y1): 12,338 silver held; 160,070 game-wide
- Turn 8 (September Y1): 14,718 silver held; 187,042 game-wide
- Turn 9 (October Y1): 21,201 silver held; 222,948 game-wide
- Turn 10 (November Y1): 17,028 silver held; 261,779 game-wide
- Turn 11 (December Y1): 25,382 silver held; 341,874 game-wide
- Turn 12 (January Y2): 33,547 silver held; 364,376 game-wide
- Turn 13 (February Y2): 33,432 silver held; 447,810 game-wide
- Turn 14 (March Y2): 43,726 silver held; 533,026 game-wide
- Turn 15 (April Y2): 54,164 silver held; 577,289 game-wide
- Turn 16 (May Y2): 58,509 silver held; 644,859 game-wide
- Turn 17 (June Y2): 66,014 silver held; 741,527 game-wide
- Turn 18 (July Y2): 79,263 silver held; 865,369 game-wide
- Turn 19 (August Y2): 99,463 silver held; 1,056,514 game-wide
- Turn 20 (September Y2): 116,892 silver held; 1,244,573 game-wide

Silver growth is consistently ~15–25% per turn. The faction is #1 in silver holding by Turn 7 and maintains that lead through Turn 20.

**Key economic mistake:** Perfume trade unit (1951) buys 10 perfume in Turn 3 at E'egrad for $103 each — this is correct. However, errors appear: `trader (2319): STUDY: Not enough funds` in Turn 5, and various `BUY: Unit attempted to buy more than it could afford` errors throughout turns 7–20. These suggest imperfect silver allocation across scattered units, with some units under-funded. The SHARE mechanic with `share 1` on parent units partially compensates.

---

### Military Strategy

**Philosophy:** Overwhelm through numbers, not quality. The faction builds large armies of mediocre troops (combat 1) rather than elite units. Combat begins turning military from Turn 18 onward.

**Army Composition:**
- Core infantry: Orcs (combat to level 5) — primary frontline soldiers. By Turn 14, 111 orcs held in treasury; by Turn 20, 417 orcs.
- Ranged: Goblins with crossbows (crossbow to level 5, crossbow 2 combat skill). By Turn 20, multiple units of 9–18 goblins each with crossbows and swords.
- Mobile/fast: Centaurs (riding, 4 hexes/turn) for scouting and rapid deployment. 37 centaurs by Turn 20.
- Support: Pikes equip infantry (pike [PIKE] anti-cavalry weapon, piercing damage).
- Weapons issued: swords, pikes, crossbows. Crossbows especially effective (armor-piercing ranged).

**Guard units pattern:** Each region has 3–8 orcs or gnolls or ice dwarves on guard with `guard 1`, `hold 1`, `share 1`, `@tax`. These are not heavy combat units but serve as territory markers.

**Expeditionary Forces:** By Turn 20, specific "Enclave Expeditionary Forces" units appear:
- EEF (6241): 46 orcs, 18 pikes, 6 swords, combat 2
- EEF (5091), (6051), (6238), (7198): 9–18 goblins each, crossbow 2, with swords
- workers (7577): 60 orcs, combat 1

**Major Combat Event — Turn 20: Assault on City Guard (19) in Ma'i [town]**
The faction finally attacks the city guard (19) in jungle (61,23) — the town where they've had an outpost since Turn 3. This is a massive coordinated assault:
- Attacker: Trading outpost (1950) plus 11+ units (total ~200+ fighters)
- Tactics advantage: trader (6240) with tactics 2 provides +2 rounds
- The assault involves orcs (melee), goblins with crossbows (ranged behind), and sword-carrying units
- Result: City Guard (19) destroyed in 1 round. 27 leaders with swords eliminated. Spoils: 14 swords, 216 silver.

The faction clearly spent many turns building up forces specifically to take city guards. The timing (Turn 20) suggests this was delayed by military buildup requirements.

**Losses sustained:**
- Turn 3: trader (1376) destroyed by Ice Wurms — one unprotected unit in wild territory
- Turn 6: trader (2312) destroyed by Crocodiles in swamp
- Turn 7: trader guards (2637) loses 2 centaurs to Carnival of Shadows (61) attack (though faction declares friendly to Carnival)
- Ongoing: single-man scout units occasionally killed by creature attacks (dragons, undead)

**Defensive posture:** The faction uses `avoid 1` on most scouting units, meaning they won't participate in combat. All guard units are set `behind 1` initially. The `noaid 1` flag appears on production units like miners to prevent them being dragged into combat.

---

### Magic Development

**Single mage, slow development:** Big Fat Trader (884) is the only mage through Turn 20. The faction type swings between Magic 1 and Magic 2, but no second mage is trained within the first 20 turns.

**Skill progression of unit 884:**
- Turn 1: force 1 (30), pattern 1 (30), spirit 1 (30), gate lore 1 (30), fire 1 (30), combat 3 (180), observation 1 (30)
- Turn 2 (after studying): stealth 1 (60), pattern 1 (35)
- Turn 3: stealth 2 (90), pattern 1 (40)
- Turn 4: pattern study ordered — pattern 1 (40) → studying pattern
- Turn 5–6: pattern 2 (105), force 1 (30), spirit 1 (35)
- Turn 7: force 1 (30) → studying force
- Turn 8: force 2 (90)
- Turns 9–12: force 2 (90), pattern 2 (105), spirit 1 (55–70)
- Turn 12: gate lore 1 (30) — studying gate
- Turn 13: spirit study (to reach spirit 2 for higher gate cast?)
- Turn 14: studying gate lore → gate lore 2 presumably
- Turn 15: studying gate
- Turn 20: mage count = 0 (Big Fat Trader likely lost to TRANSPORT error or died; "Mages: 0 (1)" in Turn 20 report)

**Skill path rationale:**
- Stealth early: to avoid being targeted while random-gating
- Pattern: required pre-requisite for higher combat spells and gate casting
- Force: required for force shield and certain attack spells
- Gate lore: enables targeted gate jumps (not just random) and higher gate abilities
- The mage never reaches a combat casting level beyond fire 1 throughout turns 1–20

**Combat spell:** Fire [FIRE] from Turn 1. Used for battlefield fire spells, but the mage is always `avoiding`, `behind`, so it never fights in the first 20 turns.

**Magic income:** No magical income spells (like phantasmal entertainment). The faction's income is entirely mundane.

**Major failure:** The mage hits a wall on Turn 12 — `Big Fat Trader (884): STUDY: Doesn't have the pre-requisite skills to study that.` This confirms the player doesn't have the correct skill prerequisites ready when they try to advance (likely trying to learn a spell without the required sub-skill at required level). This wastes a turn's study.

---

### Expansion Pattern

**Expansion method:** Use Big Fat Trader's random gate jumps to land in a region, spawn 4–5 new single-race-appropriate units (traders) using FORM orders that immediately buy local race troops and spread out to adjacent hexes. Each scout forms 3–4 more units at the next destination, creating a fractal expansion pattern.

**Turn-by-turn region count:**
- Turn 2 (March Y1): 0 regions controlled
- Turn 3 (April Y1): 1 region (tundra 4,82 home base)
- Turn 4 (May Y1): 5 regions
- Turn 5 (June Y1): 8 regions
- Turn 6 (July Y1): 15 regions
- Turn 7 (August Y1): 22 regions
- Turn 8 (September Y1): 34 regions
- Turn 9 (October Y1): 39 regions (faction cap 60 reached soon after)
- Turn 10 (November Y1): 38 regions (some loss, cap still 60)
- Turn 11 (December Y1): 43 regions (cap expanded to 60)
- Turn 12 (January Y2): 51 regions
- Turn 13 (February Y2): 53 regions (cap now 90!)
- Turn 14 (March Y2): 59 regions
- Turn 15 (April Y2): 65 regions
- Turn 16 (May Y2): 72 regions
- Turn 17 (June Y2): 80 regions
- Turn 18 (July Y2): 82 regions
- Turn 19 (August Y2): 86 regions
- Turn 20 (September Y2): 85 regions (slight drop)

**Expansion geography:** The faction spreads from two beachheads:
1. Home tundra cluster in Febefe (ice dwarves, gnomes): expanded north to E'egrad city, southeast to Meldorf city, and surrounding rural hexes.
2. Clafluspo jungle cluster (orcs, lizardmen): expanded from jungle (60,22) south, east and west into Yhandew swamps and Clafluspo jungle chain, reaching the Ma'i [town] hub.
3. Enstan plains cluster (centaurs): Big Fat Trader's early jumps land at plain (15,21) and (16,24), spawning centaur scouts that ride 4 hexes/turn to expand rapidly into Enstan, Sawood, and Cioflen.
4. Underworld exploration: From Turn 4 onward, goblins enter shaft at (60,24) into underworld caverns. Turn 5 shows units moving through cavern (30,12) in Bro'abi. This is early underworld access.
5. Ocean swimming units (lizardmen): Turn 4-5, lizardman units swim through ocean hexes to reach far-off regions.

**Faction limits upgraded:** The faction upgrades its faction type aggressively:
- Turn 2: Martial 1 / Magic 1 (initial)
- Turn 3 (Turn 2 orders): `faction martial 3 magic 2` — cost paid
- Turn 9/10: Transitions to Martial 4, Magic 1
- Turn 13: Martial 5 with Magic back to 1 (traded away magic capacity for martial)

The massive martial capacity (90 regions at max) drives the expansion strategy.

**Quartermaster capacity:** Starts at 0. Reaches 1 by Turn 9, 2 by Turn 13, 3 by Turn 18, 4 by Turn 19. Quartermasters enable the TRANSPORT system that coordinates the economy.

---

### Turn-by-Turn Summary

**Turn 1 (orders only, no report):**
Unit 884 in nexus: claims 200, studies stealth, casts gate random. Workers unit (1373) forms with 3 ice dwarves, studies combat. Three trader units form with 1 ice dwarf each, move to adjacent hexes.

**Turn 2 (March Year 1): First Gate Jump**
Report available. Big Fat Trader jumps to jungle (60,22) in Clafluspo. Stealthy (avoiding, behind). Studies stealth more. Four trader units sit at home hexes. Unclaimed silver 10,032. Faction is at 0 regions but already has 5 units out.

**Turn 3 (April Year 1): Explosive Unit Creation**
Orders show massive unit spawning: 5 new trader units spawned in Clafluspo area (orc-buying), 7+ new units in Febefe. trader (1376) dies to Ice Wurms. Workers (1373) taxes 150 silver in home hex. Faction at 1 region controlled. Big Fat Trader lands at plain (15,21) in Enstan (centaur country). At this region, 2 centaur units immediately spawned. In orders: `faction martial 3 magic 2` raised — paying for 3 martial slots and 2 magic slots. Unclaimed silver 9,334. Total units probably 15+.

**Turn 4 (May Year 1): Region Control Established, Perfume Trade Begins**
Regions: 5. Big Fat Trader at mountain (35,37) in Ditro'en after 3rd random gate jump. Studies pattern. In Enstan, centaurs spawn to explore adjacent regions (forest/plains). In Clafluspo: workers (1946) taxes 150, and an assassination is noted (faction 5 member is killed elsewhere). Key: trader (1951) in E'egrad buys 10 perfume at $103 each (`withdraw 1 hors` to get a horse for riding) — the perfume trade begins. Perfume will be sold in Meldorf for ~$390/each. Ma'i town: "Trading outpost" (1950) forms to specialize in commerce and entertainment. Production units begin studying: farming, lumberjack, herb lore, weaponsmith.

**Turn 5 (June Year 1): Expansion Accelerates**
Regions: 8. Multiple new regions with lizardmen, goblins in swamps. Centaur scouts spread into Enstan plains. Lizardman swimmers (2311, 2312, 2313) exploring ocean routes. Goblin units enter underworld (caverns). Units in Yhandew swamps begin taxing. Error: trader (2319): Not enough funds for study — minor silver allocation issue. Big Fat Trader lands at forest (47,21) in Rhuvarstwun. Perfume trade: unit (1951) sells perfume and buys 10 more.

**Turn 6 (July Year 1): 15 Regions, Economic Engine Running**
Regions: 15. Massive treasury: 4,080 silver held, ranking 9th game-wide. 29 perfume bought this turn. Tax income from 7+ regions. Big Fat Trader now studying force. Key units: workers units in all major hubs with `guard 1`, `@tax`, `share 1`. Wood elves (3) appear in treasury — first forest race acquisition. Unit (2312) destroyed by crocodiles in swamp. Turn 5 orders show centaur expansion across Enstan plains (6+ centaur scouts moving 2 hexes each).

**Turn 7 (August Year 1): 22 Regions, Silver Explodes to 12,338**
Regions: 22. Silver #1 game-wide at 12,338 held. Perfume sells at ~$390/unit, buying 29/turn generating ~$8,300 in sales with ~$5,100+ profit. Wood elves at 25, high elf acquired. Gnomes at 74 — large gnome workforce. Resource production: 20 wood, 15 herbs, 2 axes, 1 net, 1 lasso produced. Big Fat Trader now at force 2. Errors: gnome unit (3228) has no name. Perfume trade fully automated. Unit (2570) (ivy) attacked by wolves in Enstan — must be another faction's unit sharing the region.

**Turn 8 (September Year 1): 34 Regions**
Regions: 34. Silver at 14,718, still #2 game-wide. Goblins in underworld encounter Dragon (1023) in Bro'abi — traders (2659) and unit (3266) destroyed by dragon breath. This shows the danger of unsupported underworld scouts. More wood elves (31), orcs (47), lizardmen (83) in treasury. Gnomes (97) — the gnome workforce is massive now. Production: 30 wood, 26 herbs, spinning wheels appear. Big Fat Trader in plain (4,12) in Wammark after gate jump.

**Turn 9 (October Year 1): 39 Regions, Faction Type Shift**
Regions: 39 (cap 60). Silver at 21,201, #1 game-wide. Critical shift: faction type changes to "Martial 4, Magic 1" — trades 1 magic slot for 1 martial slot. This is a strategic pivot toward expansion over magic. Orcs at 62, lizardmen at 135, gnomes at 107. Centaurs at 20. Drow elf acquired. Quartermaster count hits 1. New race: drow elf appears in treasury.

**Turn 10 (November Year 1): 38 Regions (slight decline)**
Regions: 38 (cap 60). Silver at 17,028 (slightly lower). Gnomes at 173. Centaurs at 15. Strongmen from Carnival of Shadows (61) attack trader (2637) in plain (15,23) in Enstan, destroying 2 centaurs. Despite being "friendly" to Carnival of Shadows (61), their attack triggers. This is noted but the faction continues declaring Carnival as friendly. TRANSPORT system starting to appear in orders for this period.

**Turn 11 (December Year 1): 43 Regions, Building Infrastructure**
Regions: 43 (cap 60). Silver at 25,382, #1 game-wide. High elves at 14. Resource stockpiles growing: 59 wood, 38 fish, 93 herbs. Building skills appear: `BUILD caravanserai` orders emerge. Orders for this period show explicit transport orders routing resources to Big Fat Trader (3558) — a second "Big Fat Trader" is created as dedicated quartermaster. Note errors: "Alias multiply defined", "END: without FORM" — sloppy orders formatting. Mining units now active: 30 gnomes producing iron at mountain (5,77), 10 gnomes quarrying stone.

**Turn 12 (January Year 2): 51 Regions, New Beachheads**
Regions: 51 (cap 60). Silver at 33,547. High elves at 66. Iron appears (33 units), stone (10 units) — mining and quarrying operational. Fish (90 units) — fishing operations running. TRANSPORT system fully deployed: units in mountains transport iron to central quartermaster; ocean units transport fish. Bug: Big Fat Trader (884) tries to study a spell without prerequisite — loses a turn. Big Fat Trader (3558) errors on TRANSPORT range.

**Turn 13 (February Year 2): 53 Regions, Martial 5 Achieved**
Regions: 53 (cap 90 — massive cap expansion). Faction type: "Martial 5" — pure military expansion focus. Magic capacity reduced to 1, with only 1 mage. Silver at 33,432. High elves at 141. Orcs at 92. Gnomes at 241 — the gnome workforce dominates. Fish at 100, herbs at 186, iron at 63. Note: the cap expansion from 60 to 90 unlocks substantial new territory, driving the next phase of expansion.

**Turn 14 (March Year 2): 59 Regions**
Regions: 59. Silver at 43,726. Wood elves at 293 — massive. High elves at 181. Orcs at 111 with weapons. Picks appear (mining tools). Production diversifies: hammers, axes. Crossbows (12). Errors: sea traders starve (4 die from maintenance cost) — sea units operating far from silver sources.

**Turn 15 (April Year 2): 65 Regions, Military Buildup**
Regions: 65. Silver at 54,164. Crossbows at 12, axes at 64. Wood elves at 399, high elves at 225. Fish at 227, herbs at 300 — production massive. Expeditionary forces forming. "Enclave Expeditionary Forces" units appearing with pikes and swords. Errors: GIVE to non-existent new units (orders referencing `new 18`, `new 48` which don't resolve properly).

**Turn 16 (May Year 2): 72 Regions**
Regions: 72. Silver at 58,509. Crossbows at 48, swords at 6. Pikes at 9. Gnomes at 382. Lizardmen at 401. A large-scale military unit (Tribe of Centaurs 176) attacks trader guards (4952) in plain (13,9) — 4 orcs defender. Shows frontier units still vulnerable to creature attacks.

**Turn 17 (June Year 2): 80 Regions**
Regions: 80. Silver at 66,014. Crossbows at 117, swords at 12. Pikes at 11. Orcs at 203. TRANSPORT errors multiplying — Big Fat Trader (3558) has frequent "Target does not exist" and "not a member of friendly faction" errors (trying to transport to FarmDudes faction 4274 who must have ended diplomatic relation). Sea traders (4975) starve (4 die).

**Turn 18 (July Year 2): 82 Regions**
Regions: 82. Silver at 79,263. Pikes at 67, crossbows at 150, axes at 127. Floater hides appear (14). Quartermasters at 3. The military equipment stockpile is now substantial. Production errors persist. TRANSPORT system has several dead targets.

**Turn 19 (August Year 2): 86 Regions**
Regions: 86. Silver at 99,463 (approaching six figures). Swords at 64, crossbows at 162, pikes at 105. Wood elves at 759, high elves at 463. Orcs at 330 — army growing. Quartermasters at 4. Final preparations for military action visible.

**Turn 20 (September Year 2): 85 Regions, City Assault**
Regions: 85 (down 1 from 86). Silver at 116,892 — faction is the richest in the game. Mages: 0 (Big Fat Trader 884 appears to have died or been removed). Major battle: **Trading outpost (1950) attacks City Guard (19) in jungle (61,23) in Ma'i [town]**. The assault involves 11+ units: ~183 combined fighters including 46 pikes + swords, 36 crossbow goblins behind. Result: City Guard (19) defeated in 1 round. 27 leaders with swords destroyed. Spoils: 14 swords, 216 silver. The faction takes its first city guard. TRANSPORT system plagued by errors (targets don't exist, range failures).

---

### Strengths and Weaknesses

**Strengths:**

1. **Explosive early expansion:** The gate-random + FORM-in-place strategy colonizes a new region every turn. By Turn 8, already 34 regions despite having essentially 0 controlled at Turn 2. The growth rate is exceptional.

2. **Silver generation:** The perfume trade route (buy in E'egrad, sell in Meldorf or Ma'i) generates extraordinary margins from Turn 4. Combined with tax income from 40+ regions and resource production, the faction becomes and stays the richest in the game from Turn 7 onward.

3. **Multi-race diversity:** Hiring the local race in each region (ice dwarves for tundra, orcs for jungle, lizardmen for swamp, gnomes for city, centaurs for plains) maximizes production and movement efficiency for each terrain type.

4. **Systematic resource production:** Mining, quarrying, fishing, farming, herbalism, lumberjacking — all developed simultaneously with dedicated unit cadres. The TRANSPORT system then centralizes these resources for sale.

5. **Centaur rapid scouting:** Centaurs move 4 hexes/turn, allowing extremely rapid exploration of plains and open terrain. Single centaur units with combat 1 can tax regions they enter.

6. **Strong economic foundation before military:** By Turn 15 when military buildup begins, the faction has overwhelming silver to equip armies.

**Weaknesses:**

1. **Magic stagnation:** Only 1 mage for 20 turns, and that mage barely advances past force 2 / pattern 2 / gate 1. No combat casting capability until late (fire 1 is not a major combat spell without higher force). The faction deliberately sacrifices magic for martial capacity (trading Magic 2 down to Magic 1 in Turn 9), leaving no magical economic tools like phantasmal entertainment.

2. **Vulnerability of scout units:** Single-man units with 1 troop are routinely killed by Ice Wurms, Crocodiles, Dragons, Pirates, Undead. Each loss is minor individually but represents lost investment and territory.

3. **TRANSPORT system errors:** By Turn 17–20, the TRANSPORT system generates numerous errors (wrong faction, target doesn't exist). These represent failed silver distributions and resource routing failures, wasting turns for many production units.

4. **Delayed military action:** Despite accumulating 100+ orcs and heavy military equipment by Turn 18, the first city guard assault doesn't happen until Turn 20. The faction spends 5+ turns with army-scale forces without using them offensively.

5. **Order management errors:** Frequent "Alias multiply defined", "END: without FORM", "GIVE: Nonexistant target" errors throughout Turns 10–20 indicate manual order management at scale is breaking down as the number of units exceeds easy manual tracking (200+ units by Turn 20).

6. **No mage backup:** With Big Fat Trader 884 dying (Turn 20 shows Mages: 0), the faction has zero magical capability. This is catastrophic — losing the only mage wastes all the magic skill investment.

7. **Sea unit starvation:** Units like sea traders (4975, 4976) repeatedly starve (4 die in Turn 13–14 reports). Ocean units far from silver sources don't get maintenance covered — a resource management failure.

---

## Section 2: AI Agent Strategy (Based on This Playstyle)

### What the AI Would Keep

1. **Gate-random expansion core:** Big Fat Trader using `CAST GATE RANDOM` every turn to find new regions globally, then spawning 3–5 new buying-units via FORM is an excellent, low-cost exploration strategy. Keep this as the primary expansion mechanism.

2. **Local-race hiring immediately:** Buying the local race on arrival to create mobile scouts/taxpayers is correct. Lizardmen for swamps (swim), centaurs for plains (fast), orcs for jungle/taxing, gnomes for cities (entertain). The AI should automate this: enter region → buy local race units → move them to adjacent hexes.

3. **Perfume arbitrage as primary income:** The E'egrad buy / Meldorf sell perfume route is exceptional. Maintain this automated with `@buy 25 perf` / `@sell all perf`. Scale to 30 perfume once silver allows. Extend to other luxury trade routes (pearls, cotton, silk, spices) when discovered.

4. **Multi-pillar economy (tax + production + trade):** All three pillars should run in parallel. Don't neglect production just because taxes are running — the two compound together.

5. **Aggressive faction type upgrades:** Buy Martial 3 / Magic 2 in Turn 2 orders (as the player does). Scale martial to 5 to maximize region capacity. The 90-region cap opens the entire world.

6. **SHARE pattern for sub-units:** Parent "workers" unit with `guard 1`, `@tax`, `share 1` funding child units studying combat. This is efficient — the child units don't need independent silver sources while training.

### What the AI Would Change

1. **Develop a second mage earlier.** The faction neglects to train any second mage for 20 turns. By Turn 5–6, a second leader should already be studying magic prerequisites. The economic output at that stage (10,000+ silver available) can easily support training a second mage. Target: second mage operational with fire 2 and pattern 2 by Turn 12. This enables phantasmal entertainment income (phantasmal entertainment = 500+ silver/turn per mage).

2. **Don't sacrifice magic capacity for martial.** The Turn 9 decision to swap from Martial 4 / Magic 1 to Martial 5 drops magic capacity from 2 to 1. With only 1 mage, this is defensible, but it blocks training the second mage. The AI should instead maintain Martial 4 / Magic 2 until a second mage is prepared, then upgrade both dimensions.

3. **Protect scout units with at least 3 troops.** Single-man scouts die constantly to creatures. Even 2–3 units makes the force "combat 1" vs. being defenseless. Rule: no unit with fewer than 3 troops enters wild regions without support.

4. **Fix TRANSPORT system before scaling.** The player builds the TRANSPORT network without testing it, resulting in many errors in Turns 12–20. The AI should verify transport chains work by checking unit IDs and distances. Only use `@transport` (conditional) once the channel is confirmed working.

5. **Attack city guards earlier.** The city of Ma'i [town] is accessible from Turn 3 onward. The faction waits until Turn 20 to assault the city guard. With 50+ orcs armed with weapons, a city guard assault is possible by Turn 15. Earlier capture = earlier tax income from town (much higher than rural hexes), earlier access to luxury goods sales, and earlier faction region count boost.

6. **Deploy crossbow goblins earlier.** Goblin crossbow units (crossbow 2) appear by Turn 15 in reports, but the player seems to be building them up rather than deploying. Goblins with crossbows and combat 2 are excellent ranged units. These should be deployed to contested regions or creature-infested areas by Turn 10.

7. **Fix sea unit maintenance.** Sea units starving 4 per turn is avoidable. Ensure sea-operating units have silver either via direct claiming or SHARE from a hub unit that accumulates from fishing income.

8. **Plan mage skill path more carefully.** The Big Fat Trader attempts to study a spell without prerequisites in Turn 12, wasting a full turn. The AI should calculate skill prereqs before issuing study orders. Given the skill list: force 2 → force 3 (need pattern 2) → combat 4 / fireball. Or: gate lore 2 → gate lore 3 → portal lore.

### Recommended Opening (Turns 1–5)

**Turn 1 (Orders only, nexus):**
- Big Fat Trader: `claim 200`, `study stea`, `@cast gate random`
- Spawn workers unit: claim 150, buy 3 local-race troops, study combat
- Spawn 3 trader units: claim 40 each, buy 1 local-race, move to adjacent hexes (N, NE, SE)

**Turn 2 (After first gate jump — Big Fat Trader in unknown region):**
- Big Fat Trader: `@cast gate random`, `study stea` (again — reach stea 2 for safety)
- Spawn 4 new units in new gate location: buy appropriate local race (orcs/centaurs/lizardmen), move to 4 adjacent hexes
- Pay for faction upgrade: `faction martial 3 magic 2` (spend ~$200 upgrade cost)
- Workers unit in home hex: `guard 1`, `@tax`, `share 1` — begin taxing home region
- Trader units on edges: `guard 1`, `@tax` — begin taxing adjacent regions

**Turn 3 (After second gate jump):**
- Big Fat Trader: `@cast gate random`, `study patt` — begin pattern prerequisite
- In E'egrad or nearest city: buy perfume trader unit immediately (`form`, `buy 10 perf`, `move to selling city`)
- In Clafluspo/Ma'i vicinity: spawn `Trading outpost` unit: `buy 3 orc`, `study ente`, stabilize this as a long-term hub
- Expand: each scout unit from Turn 2 spawns 3 more units using FORM
- Hire a second leader for magic training if affordable

**Turn 4 (After third gate jump):**
- Big Fat Trader: `@cast gate random`, `study patt` (continuing)
- Perfume trade: if trading unit at buy location, issue `@buy 10 perf` and move to sell; sell unit issues `sell all perf`
- Begin entertainment study: gnome units in E'egrad city should study entertainment (to level 3 for $90/turn each)
- Centaur units in Enstan: begin riding out to all 6 adjacent hexes each turn

**Turn 5:**
- Big Fat Trader: `@cast gate random`, `study forc` — begin force prerequisite for shield/fire upgrade
- Perfume trade running on autopilot with `@` commands
- Tax income now from 8+ regions
- Begin: mining (gnomes studying mining in mountain hexes), fishing (lizardmen with fishing skill in ocean)
- Form second mage: buy a leader unit, begin studying `patt`, `forc`, `spir` in sequence — 3-turn investment before magic is useful

### Mid-Game Plan (Turns 6–15)

**Turns 6–8: Economic Consolidation**
- Maintain gate-random jumps, spawning 4–5 new units per jump per turn
- Scale perfume trade: 25+ perfume per cycle (buy/sell same turn or across turns if horses available for riding)
- Expand tax base: every new region gets a guard unit immediately. Target 30 regions by Turn 8.
- Begin TRANSPORT planning: designate 1 quartermaster unit (Big Fat Trader 3558 equivalent) as the hub, and configure @transport chains from production units — verify the chains are correct before using `@transport`.
- Second mage: studies pattern 2, force 2 by Turn 8. Then target `phantasmal entertainment` (requires pattern 3 + spirit 2 or specific prerequisite chain depending on game rules). If available, cast PHEN for $450–500/turn additional income per mage.

**Turns 9–12: Faction Cap Expansion**
- Upgrade: `faction martial 5` — immediately expands to 90 regions. Do this by Turn 10.
- Do NOT sacrifice magic — maintain at least Magic 2 for the second mage slot.
- Quartermaster: gain 1 quartermaster ASAP by building caravanserai via BUILD order with gnome builders (building to level 2+ required). Caravanserai enables TRANSPORT.
- Military: begin crossbow training for goblin units (crossbow to level 2). Begin pike training for orcs. Target 30 goblins with crossbows and 30 orcs with pikes by Turn 12.
- City assault planning: by Turn 12, the faction should have 80+ combat-ready troops. Identify the weakest city guard (typically 27–40 guards) and plan assault.

**Turns 13–15: Military Activation**
- Assault the first city (Ma'i or another trade town with weak guard): coordinate 10+ units, use tactics unit for +2 advantage, ranged goblins behind, melee orcs in front.
- After capture: immediately station guards in city, begin taxing city at higher rates.
- Continue TRANSPORT optimization — fix any dead references.
- Scale crossbow production: goblins with crossbow 2 are devastating against unarmored targets.
- Build ships: orcs (shipbuilding to level 5) can build galleons for ocean reach.

### Adaptations for Dynamic Conditions

**If nearest city has a strong guard (80+ units with swords):**
Scale up military before attacking. Need 2x force ratio plus tactics and ranged advantage. Delay assault until Turn 16–18 if the guard is truly strong. Focus economic expansion meanwhile.

**If another faction contests nearby regions:**
Maintain `avoid 1` on scout units to avoid triggering combat. Move guards into place before the other faction arrives. Use the `forbid` order to block hostile entry. Only fight if the economic value justifies the cost.

**If perfume trade route is exhausted (buying price rises, selling price falls):**
Switch to the next available luxury. Monitor all city "Wanted" lists for high-price demand items. Trade in: silk, pearls, cotton, spices, gems — any item where the buy-here vs. sell-there spread exceeds 2x. Use TRANSPORT to route bulk trade goods to where they sell high.

**If Big Fat Trader dies:**
Immediately promote or train another leader as mage replacement. Don't let the magic capability stay at 0 for more than 1 turn. The gate-jump exploration mechanism is critical — without it, expansion slows dramatically.

**If underworld is heavily creature-populated:**
Don't invest in underworld until armies are strong (Turn 15+). Send only 3+ man units with combat 2 as scouts. Kill dragons and undead groups with coordinated 50+ man armies, not single-man units.

**If facing a hostile faction militarily:**
The Trader Enclave's strength is economic. Avoid direct war before Turn 15. Declare unfriendly to block their units from entering owned regions. Fortify city guards. Use diplomacy (ally/friendly declarations) to build defensive coalitions with neighboring factions.
