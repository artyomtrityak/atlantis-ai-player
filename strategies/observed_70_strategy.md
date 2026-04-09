# Faction 70 Strategy Analysis

Faction: **The Wandering Minstrels (70)**
Turns analyzed: 1–20 (reports from turns 2–20, orders from turns 1–20)
Faction type at start: Martial 1, Magic 1 → expanded to Martial 1, Magic 4 by turn 4

---

## Section 1: Observed Playstyle (Turns 2–20)

### Starting Conditions

**Faction name:** The Wandering Minstrels (70)

**Starting unit:** Pied Piper (924) — a single leader with no troops.

**Starting skills (Turn 1 orders comment):**
- observation [OBSE] 1 (30)
- force [FORC] 1 (30)
- pattern [PATT] 1 (30)
- spirit [SPIR] 1 (30)
- gate lore [GATE] 1 (30)
- fire [FIRE] 1 (30)
- combat [COMB] 3 (180) — unusually high combat for a starting mage
- Can study: earthquake, force shield, energy shield, spirit shield, magical healing, farsight, mind reading, weather lore, earth lore, necromancy, demon lore, illusion, artifact lore

**Starting location:** Nexus → jumped via random gate to mountain (6,76) in Phigill (orc region) on turn 1. Then to forest (47,21) in Rhuvarstwun (wood elf village) on turn 2.

**Starting resources:** Unclaimed silver of ~10,000 at turn 2. By turn 3 reduced to 8,860 after rapid spending.

**Faction status progression:**
- Turn 2: Regions 0, Mages 1 (cap 2)
- Turn 4 (May Y1): Regions 0, Mages 1, Magic cap raised to 5
- Turn 6 (July Y1): Regions 1, Mages 1 (cap 5)
- Turn 7-8 (Aug-Sep Y1): Regions 2→4
- Turn 9-10 (Oct-Nov Y1): Regions 4→5
- Turn 12 (Jan Y2): Regions 7
- Turn 14 (Mar Y2): Regions 9, **Mages 4**
- Turn 15-16 (Apr-May Y2): Regions 10 (cap reached)
- Turn 19 (Aug Y2): **Mages 5** (cap reached)

**Allies and attitudes (declared over the turns):**
- Faction 2 (Creatures): Unfriendly (from turn 2)
- Faction 25 (Silver Hand): Friendly from turn 3, Ally by turn 13
- Faction 5 (Sunshine): Friendly from turn 4
- Faction 30 (Trader Enclave): Ally by turn 13
- Faction 10, 71: Friendly by turn 13
- Faction 36, 43: Friendly by turn 8, later declared ally

---

### Economic Strategy

**Phase 1: Initial capital deployment (Turns 1–3)**

Faction 70 started with a large unclaimed silver reserve (~10,000) and deployed it systematically. On turn 1 (orders), the single leader (924) did: CLAIM 400, study stealth, CAST GATE RANDOM. On turn 2, it formed 5 scout units (each buying 1 orc at $35 from the local market), sending them to adjacent hexes with 70-90 silver each for expenses. These scouts were named "Local Minstrel" with the flavor text "Strumming a Lute in the local bar for the joy of all" — providing geographic scouting and establishing a presence.

**Phase 2: Entertainment economy (Turns 3–6)**

From turn 3 onward, the faction began recruiting race-specialized entertainers at each scout location. Notable choices:
- Wood elves (WELF) → study entertainment or lumberjack (forest regions at 47,21 and 47,19)
- Hill dwarves (HDWA) → study entertainment (mountain regions)
- Goblins (GBLN) → study entertainment (swamp regions)
- Gnomes (GNOM) → study entertainment (city of E'egrad)
- Ice dwarves (IDWA) → study entertainment (tundra)
- High elves (HELF) → study entertainment and combat
- Lizardmen (LIZA) → study entertainment

Each newly formed unit was given just enough silver to buy 1 troop + cover maintenance. Many units were set to auto-entertain (`@entertain`), providing passive income from each hex. Entertainment income was small per hex (e.g., 20-40 silver per region) but across dozens of units it accumulated.

**Phase 3: Farming and resource extraction (Turns 4–6)**

By turn 5 (June Y1), a 7-wood-elf farming unit (Unit 2532) was studying FARM to produce grain for sale. A woodcutting unit (2859) was producing WOOD. By turn 8, Unit 2532 was regularly: `produce grai`, `sell all grai` — selling ~14 grain at $24 each per turn (~$336/turn from grain alone).

**Tax-based "IPS" system (Turns 6–14)**

The single most important economic innovation: faction 70 planted large multi-person combat units in regions to collect taxes. These were named "*IPS*" (Income Production Scheme):
- **Unit 2858** (30 wood elves, combat 1): Plain/Forest IPS taxing forest (47,19) for $1,136–$1,169/turn from turn 6 onward.
- **Unit 4183 "Plain IPS"** (10+ humans, combat 1): taxing plain (47,9) for $500–$1,712/turn from turn 9 onward.
- **Mountain IPS (3174)**: taxing mountain (48,16) for $100–$224/turn.
- **Mountain IPS (4928)**: taxing mountain (50,16) for $100–$150/turn.
- **Mountain IPS (5423)**: taxing mountain (49,17) for $200–$317/turn.
- **Waypoint (5778)**: taxing plain (45,15) for $250–$937/turn.
- **Circus Troope (3551)**: taxing underforest in Tahimmo (underground) for $476–$500/turn.
- **Forest IPS (2683)**: taxing forest (47,17) for $150–$846/turn.
- **Tundra IPS (7148)**: taxing tundra (47,11) for $686/turn (by turn 17).

By turn 18 (July Y2), tax income per turn likely exceeded 6,000–7,000 silver from all IPS units combined, supplemented by entertainment (hundreds more), grain sales, and fish sales.

**Total silver rank:**
- Turn 2: ~3,629 silver on hand (rank 2 of 2038 max)
- Turn 14: ~14,122 silver on hand (rank 15 of 43,726 max)
- Turn 20: ~29,857 silver on hand (rank 13 of 116,892 max)

The faction's silver was consistently mid-tier relative to all factions, suggesting rapid reinvestment rather than hoarding.

**Perfume trading (Unit 2220 "Dandy"):**
By turn 13, unit 2220 was renamed "Dandy" and buying perfume at the city to resell. By turn 19, "Dandy" was buying 11 perfume at $146 each (from the city for sale) and selling; Local Minstrel (2863) supplied her with 15 perfume sourced somewhere. This was a small but profitable trade route.

**Fish production (Turns 11+):**
Sea Dogs (3869) and unit 6193 produced fish for sale at $44 each (e.g., 12 fish = $528/turn from 6193).

---

### Military Strategy

**Philosophy: Avoid combat, use economic dominance for taxation.**

Pied Piper (924) was always set to `behind 1` and `avoid 1` — the faction avoided direct combat with its mage. The "combat" units existed primarily to enable taxation, not active warfare.

**Combat unit construction:**

From turn 5 onward, faction 70 systematically built up large wood-elf combat units for IPS taxation:
- Unit 2858: grew from 10 welf combat studs to 30 welf by turn 12 then renamed "Forest IPS" or "Town Guard"
- Unit 4183 (Plain IPS): humans studying combat, growing 6–10 per turn from turn 9
- Town Guard (5424): 10+ wood elves with pikes and leather armor
- Town Guard (5782): 10+ wood elves with pikes
- By turn 17: unit 2858 had 30 welf combat 1, backed by Forest IPS 2683 with 20 high elves combat 1

**Weapon and armor production:**
- Unit 2860 (5 welf, weaponsmith): produced axes initially, then switched to pikes (iron needed)
- Unit 5425 (weaponsmith): produced longbows by turn 20
- Unit 4186 (armorer): produced leather armor (8 larm by turn 18)
- Units Town Guard 5424 and 5782 were equipped with pikes + leather armor (turn 18)

**Underworld presence (from Turn 6):**
- Unit 3184 ("Underground Womble" → "Minstrel Underground troope"): entered underworld via Shaft, used goblins, later drow elves (DRLF), taxing underforest (7,41) for $476–$500/turn.
- Unit 3551 ("Circus Troope"): taxed underworld for $500/turn.
- Drow elves were recruited for mining, weaponsmithing, quarrying in the underground.

**Losses to monsters (minor):**
- Turn 7 (Aug Y1): Local Minstrel (3186) — 1 gnome killed by Evil Warriors (770)
- Turn 17 (Jun Y2): 11 wood elves killed from Unit 2858 by Kobold Pack (353) in forest, but the unit survived (had 30 welf to absorb it)
- Turn 19 (Aug Y2): 1 orc unit 6703 killed by Ice Wurms; 1 high elf (5426) killed by Living Trees
- Turn 20: 2 lizardmen lost to Pirates and Undead (isolated scouts in ocean/swamp)

**Attitude toward combat:** Primarily defensive. Units were set to `avoid 1` when scouting. The faction engaged in combat at E'egrad city (turn 19) alongside Trader Enclave (30) and Silver Hand (25) allies to destroy a city guard, which may have been a coordinated faction-sanctioned action to take control of the city.

---

### Magic Development

**Pied Piper (924) — primary mage:**

Magic study path (observed through reports):
- Turn 1: Random Gate Jump (exploring)
- Turn 2: Study stealth [STEA] → reached level 2
- Turn 3-4: Study stealth (continued), set combat spell to fire [FIRE]
- Turn 5: Study pattern [PATT] → level 1 → 45 XP
- Turn 6: Study force [FORC] → (from orders `study forc`)
- Turn 7: Continue study force
- Turn 8: Study artifact lore [ARTI] (orders: `study arti`)
- Turns 9-10: Continue gate lore, then other magic foundations
- Turn 11: Study gate [GATE]
- Turn 13: Study fire [FIRE] (from orders)
- Turn 14 (Mar Y2): Pied Piper skills: observation 1, force 2, pattern 2, spirit 2, gate lore 2, fire 1, combat 3, stealth 2, artifact lore 1. Teaching gate lore to Chatterer (897) from ally faction.
- Turn 19 (Aug Y2): force 2, pattern 2, spirit 2, gate lore 2, fire 2, combat 3, stealth 2, artifact lore 2, enchant swords 1. Can now study: enchant swords (ESWO), enchant armor (EARM), enchant shields (ESHD), create gate crystal (CRGC).

**Strategy:** The main mage diversified broadly in foundation skills (force, pattern, spirit, gate lore, fire) reaching level 2 in all of them by turn 14, rather than specializing deeply. This unlocks multiple advanced spells but keeps the mage below level 3 in any single combat spell. Artifact lore was studied to unlock weapon enchanting (enchant swords reached level 1 by turn 19), providing a long-term endgame plan for creating magical items.

**Gate Lore usage:** The mage used `CAST Gate_Lore RANDOM UNITS 924` every turn from 1 through approximately turn 12, using gate teleportation to explore the map rapidly. This was the primary scouting and mobility tool. Pied Piper visited: mountain (6,76), forest (47,21), tundra (13,85), plain (11,33), forest (47,19), and other locations — covering vast territory in the first year.

**New mages (Units 4427, 4432, 4438 — from Turn 12):**
These three leaders were given to faction 70 (likely from ally Silver Hand or recruited) by turn 12. By turn 14, they were ordered `study forc` (force). By turn 17, they had force [FORC] 2 (125), pattern [PATT] 2 (120), fire [FIRE] 2 (120) with combat spell set to fire. By turn 19, they were actively casting Fireballs in the battle at E'egrad (killing 7 and 5 enemies respectively), demonstrating that the mages became militarily effective by turn 19.

Their skills by turn 19: observation 1, force 2, pattern 2, fire 2. Combat spell: fire [FIRE]. Mage type appears to be combat fire mages being developed in parallel.

**Faction magic cap:**
- Turn 3-4: 1 mage cap 2, raised to cap 5 via faction points
- Turn 14: 4 mages, cap 5
- Turn 19: 5 mages, cap 5 (fully loaded)

---

### Expansion Pattern

**Turn 1-2 (March-April Y1):** Single mage jumps gates to explore. 5 orc scouts sent to 5 adjacent hexes from starting mountain hex.

**Turn 3-4 (April-May Y1):** Scouts dispersed further — goblins to swamp regions, hill dwarves to different mountains, gnomes to city E'egrad, wood elves to forest. At least 10+ units active across 6+ hexes. No regions owned yet.

**Turn 5-6 (May-June Y1):** Large wood elf recruits at forest (47,21) — 30+10+5+5 welf combat units formed. Unit 2531 began traveling north via horse. First region claimed (turn 6): forest (47,19) in Rhuvarstwun where Unit 2858 began taxing.

**Turn 6-7 (June-July Y1):** Expansion in multiple directions simultaneously:
- North: Unit 2531 moving toward plains (47,9)
- South: Unit 3541 moving through mountains
- Underground: Unit 3184 descended into underworld via shaft
- Far west: Ship started for coastal exploration

**Turn 7-8 (Aug-Sep Y1):** Regions 2→4. First ship (longship) under construction. Unit 3870 explored via sailing. Two tax regions established.

**Turn 9-10 (Oct-Nov Y1):** Regions 4→5. Longship completed. Ships sailing to new coastal areas. Unit 4183 established in plain (47,9) for taxation.

**Turn 12 (Jan Y2):** Regions 7. Multiple IPS units collecting in overlapping regions.

**Turn 14-15 (Mar-Apr Y2):** Regions 9→10 (cap reached). All 10 region slots filled. Faction stopped expanding geographically — all further effort focused on deepening production within owned regions.

**Geographic footprint by turn 14-15:**
- Coastal area: forest 47,17 and 47,19, plain 47,9 (core home territory)
- Mountains: 48,16, 49,17, 50,16 in Tracas/Swa'ing area
- Plain 45,15 in Prestan (reached by ship)
- Underground: underforest 7,41 in Tahimmo
- Multiple explorer/scout units in distant hexes not counting toward region cap

---

### Turn-by-Turn Summary

**Turn 1 (March Y1) — Orders only:**
Single unit (924) in nexus. Orders: CAST Gate_Lore RANDOM, study stealth, CLAIM 400, name unit "Pied Piper". Faction magic bumped via `faction magic 4` (done in turn 4 orders but reflected in turn 3 report).

**Turn 2 (April Y1) — First report:**
924 landed at mountain (6,76) in Phigill. Formed 5 Local Minstrel units, gave each 70-90 silver, bought 1 orc each, sent them to 5 adjacent hexes. One studied entertainment. Pied Piper random-gated to forest (47,21) Rhuvarstwun. 9,600 unclaimed silver. Ally Silver Hand (25) visible at starting hex.

**Turn 3 (May Y1):**
Major expansion: formed 5+ new units. Wood elves purchased at forest village — 3+1+7 welf in separate units for entertainment, lumberjack, farming, and future combat. Gnomes bought at E'egrad city. 8,860 unclaimed. Faction type bumped to Magic 4. Pied Piper gate-jumped to tundra (13,85) Wune.

**Turn 4 (June Y1):**
Large recruitment wave: 30 welf combat unit, 10 welf lumberjack, 5 welf weaponsmith, 5 welf shipbuilder at forest 47,21. 10 gnomes bought at E'egrad for entertainment. Lizardman, 4x ice dwarves bought at tundra. Pied Piper gated to plain (11,33) Fro'agate. Pattern studied. Combat spell set to fire.

**Turn 5 (July Y1):**
Unit 2858 (30 welf) and Unit 2859 began taxing forest (47,19) — first taxation! Collected $1,136. New formation of orc scouts in north. High elves bought at plain (11,33) for future use. Various skill studies locked in (weaponsmith, shipbuilding, lumberjack, carpenter). First region claimed.

**Turn 6 (August Y1):**
2 regions. Unit 3184 entered underworld. Battle: 1 gnome scout killed by Evil Warriors (goblin pack problem in plain 15,87). Unit 2858 continued taxing forest. Pied Piper studying force. High elves and gnomes recruited for entertainment. Ships started. Unit 3174 established mountain tax.

**Turn 7 (September Y1):**
4 regions. Ice Dragon attack on Optimates (54) faction — visible in report but not affecting faction 70. Faction 70 unaffected. Sailors being trained. Unit 2861 building longship. Unit 2532 farming + selling grain. Unit 3541 moving toward mountains. Underground unit 3551 taxing underworld.

**Turn 8 (October Y1):**
5 regions. Sea Dogs (3868, 3869, 3870) sailing ships. Grain farming producing 14/turn sold at $24. Unit 3541 taxing mountain 48,16 for $50. Underground Womble/Circus Troope taxing underworld $500.

**Turn 9 (November Y1):**
5 regions. Ships sailing to coastal plains. Unit 4183 taxing plain 47,9 for $500. Multiple IPS units active. Faction declared friendly with Trader Enclave (30) and squirrels (43).

**Turn 10 (December Y1):**
5 regions. Ship TWM Deliverance and TWM Eastern Explorer named. Grain farming, wood production, longship under construction. Pied Piper studying gate. Underworld operations expanding with drow elves (DRLF) for mining/weaponsmith/quarrying.

**Turn 11 (January Y2):**
7 regions. Three new leaders (4427, 4432, 4438) given to faction (from ally). Battle: Local Minstrel (2867) attacked by pride of lions but survived due to allies (squirrels faction 43 helped defend). Tax income increasing. Unit 2858 declared ally with faction 43 (squirrels). Mountain IPS 4928 added. Waypoint (5778) established in plain (45,15) via ship.

**Turn 12 (February Y2):**
7 regions. Assassination: Unit 2860 (5 welf weaponsmith) killed in forest (47,21)! Likely by enemy stealth unit. Faction 70 lost a production unit. Silver income from ally Taxers (1704) received ($1,000) — likely inter-faction transfer. Multiple mountain IPS taxing. Faction 70 declared alliance with Silver Hand (25) and Trader Enclave (30).

**Turn 13 (March Y2):**
9 regions. Mages: 4. Pied Piper now studying fire (turned from gate to combat magic). Chatterer (897) from ally being taught gate lore by Pied Piper. Forest IPS 2683 established. Multiple town guards formed (5782, 5424) with pikes. Magic wagon production begun (Unit 3176 carpenter built 6 magic wagons).

**Turn 14 (April Y2):**
10 regions (cap). Units 4427/4432/4438 studying force. Faction at maximum region count. Sea lanes named (Western Sea Lane [121], TWM Eastern Explorer [109]). Shipbuilding producing cog. Income from 8+ tax regions.

**Turn 15 (May Y2):**
10 regions. Fully loaded magic cap (still 4 mages). Ship 3870 exploring. High elf combat units built. Ice dwarves formed as mining/quarrying workers. Horse breeder (2531, now horse training). Riding/cavalry preparations.

**Turn 16 (June Y2):**
10 regions. 4 mages. New tundra IPS (7148) established. Ice dwarf miners, quarriers, herbalists being trained. Shipyards unit (7149) building cog. Fish production from 2 separate units.

**Turn 17 (July Y2):**
10 regions. 4 mages. Combat spell activated for 4427/4432/4438. Kobold attack on Unit 2858 — 11 wood elves lost but faction survived. Various starving units mentioned (farmers without enough silver). Farmers/Yew Smiths dying from starvation — sign of cash flow management issues. Armor (LARM) production, longbow production active.

**Turn 18 (August Y2):**
10 regions. 4 mages → 5 mages (cap reached). Magic wagons (16 total) held. Multiple skill specializations complete. Equipment: 9 swords, 12 longbows, 16 leather armor, 93 pikes distributed. Tax income from 8+ regions. Samas (7441) given 200 silver — possible inter-faction support.

**Turn 19 (August Y2):**
5 mages. Faction 70 mages (4427, 4432, 4438) joined combined attack on city guard at E'egrad alongside Trader Enclave and Silver Hand. Fireballs killed 12 enemies. Magic wagons transferred to guards (5 mwag to unit 1833 — ally). 93 pikes in inventory. Dandy (2220) trading perfume profitably ($2,000 received).

**Turn 20 (September Y2):**
10 regions, 5 mages. Pirates killed 1 lizardman swimmer. Undead killed 1 lizardman swimmer. Guards (6095) / Silver Hand attacked City Guard at E'egrad city. Ship 3870 recruiting more combat high elves. Building operations ongoing (cog nearly complete). Ice dwarves specializing in weap/quarry/mining.

---

### Strengths and Weaknesses

**Strengths:**

1. **Rapid early deployment:** Started with a single mage and substantial unclaimed silver, immediately deployed dozens of single-person scout/entertainer units across the map. This gave broad geographic awareness and multiple income streams from day 1.

2. **IPS taxation system:** Building large combat units (10–30 men) to hold regions for taxation was the core economic engine. Regions taxing at $500–$1,700/turn each, with 8+ regions taxed simultaneously, generated the majority of income.

3. **Multi-alliance diplomacy:** Firmly allied with Silver Hand (25), Trader Enclave (30), and friendly with squirrels (43) and Sunshine (5). These alliances provided security, combat support, and silver transfers.

4. **Diversified production:** Grain farming, wood production, fish, furs, axes, pikes, longbows, leather armor, magic wagons — production was diversified and production units were correctly staffed with appropriate races.

5. **Gate teleportation scouting:** Pied Piper used CAST Gate_Lore RANDOM every turn for the first ~12 turns to scout enormous portions of the map cheaply. This provided intelligence on dozens of regions.

6. **Underworld expansion:** Established underground operations in Tahimmo from turn 6, providing access to drow elves, rare materials, and an additional tax region outside the surface limit.

7. **Mage expansion:** Reached 5 mages (cap) by turn 19, with three fire-mage combat casters ready for warfare.

**Weaknesses:**

1. **Slow magic development:** The primary mage (Pied Piper) spent turns 1–5 on stealth and gate, not developing combat magic until much later. Fire mages (4427/4432/4438) only became combat-ready around turn 18–19, over a year into the game. An AI could accelerate this significantly.

2. **Starvation incidents:** By turn 17, farmers and smiths were starving — sign that the silver distribution system had gaps. Some newly formed units ran out of silver before studying or producing.

3. **Vulnerable scouts:** Single-man scouts (1 orc, 1 goblin, etc.) were repeatedly killed by monsters (Evil Warriors, Pirates, Undead, Living Trees, Ice Wurms). These units had no survival capability.

4. **Assassination vulnerability:** Unit 2860 (5 welf weaponsmith) was assassinated (turn 13). Production units were not guarded. The faction had no stealth units guarding its productive core.

5. **Overcomplicated logistics:** Dozens of small units with complex give/receive chains made order management error-prone. Multiple `GIVE: Not enough` and `BUY: Can't afford` errors appeared in almost every turn's error log.

6. **Delayed weaponization:** The faction didn't start arming its combat units with pikes and armor until turns 17–18. An earlier push into weapon production would have improved tax security.

7. **One location mage bottleneck:** Pied Piper randomly gated to far-flung locations, sometimes landing in hostile/useless areas, wasting the turn's teleportation. Directed gate travel (CAST Gate_Lore GATE X) would be more efficient once gates are mapped.

---

## Section 2: AI Agent Strategy (Based on This Playstyle)

### What the AI Would Keep

1. **The IPS taxation architecture.** Building large combat units (10–30 troops) to hold regions for taxation is the strongest income model observed. The AI should replicate this immediately and systematically.

2. **Race-specialized workforce.** Wood elves for lumberjack, entertainment, combat; hill dwarves for quarrying/mining/building; ice dwarves for quarrying/mining; high elves for lumberjack/entertainment/combat; goblins for entertainment/crossbow; gnomes for entertainment. Faction 70 correctly chose race based on region and task.

3. **Diplomatic posture.** Declaring friendly/ally with neighboring peaceful factions from turn 3 onward (especially Silver Hand) provided safety, intelligence, and cooperative taxation. The AI should do the same.

4. **Gate teleportation for scouting.** Using the mage's Gate Lore each turn to explore the map for free while simultaneously studying another skill is very efficient. The AI should continue this for the first 10+ turns.

5. **Magic cap investment.** Faction 70 upgraded from Magic 1 to Magic 4 immediately (turn 4 orders). The AI should do the same turn 1 — prioritize buying magic faction points before unclaimed silver runs out.

6. **Underworld expansion.** The underground provides an extra tax region outside the surface cap. Deploying one unit down a shaft to hold an underworld region adds significant income.

7. **Named unit organization.** Naming units by function ("Plain IPS", "Forest IPS", "Tundra IPS", "Sea Dogs", "Town Guard") makes order management cleaner. The AI should adopt a similar naming convention.

### What the AI Would Change

1. **Accelerate mage combat skill development.** Faction 70 delayed building combat mages until turn 12 (when the three new leaders arrived) and they only became combat-ready at turn 18. The AI should start training fire mages on force → pattern → fire from turn 1 with the primary mage. Target: fire level 2 by turn 10 (currently reached ~turn 19). If 3 new leaders arrive mid-game, immediately set them on force → pattern → fire track.

2. **Start weapon production earlier.** Faction 70 began pike production around turn 12-13. By turn 7, the AI should have a weaponsmith and armorer running continuously. Equipping combat units with pikes raises tax collection power and survivability.

3. **Eliminate single-man scouts.** The faction lost numerous 1-man scout units to monsters. Instead, the AI should send groups of 3–5 men to scout new territory, or only send scouts to areas verified safe. The carrying cost is low (3 orcs cost $105 vs $35) but survival is far better.

4. **Use CAST Gate_Lore GATE X once gates are mapped, not RANDOM.** Faction 70 used RANDOM for 12+ turns. Once the mage has found 2–3 gates, using directed gate jumps to reach specific strategic locations (e.g., where to plant a new IPS) is more efficient than random teleportation.

5. **Dedicate silver reserve tracking.** Multiple `BUY: Can't afford` errors show the faction had silver distribution bugs. The AI should explicitly budget: IPS troops cost (price × count + monthly maintenance) calculated before issuing gives.

6. **Earlier armor and equipment distribution.** Faction 70 didn't distribute pikes and armor to its combat units until turn 17-18. The AI should equip its first IPS unit with basic weapons by turn 8–9, reducing vulnerability to kobold/monster attacks.

7. **Add at least 1 stealth unit for counter-espionage.** Faction 70's weaponsmith was assassinated at turn 13. The AI should maintain 1–2 high-stealth units to detect enemy assassins (raising observation on the protective unit).

8. **Plan ship production earlier.** Faction 70 started building ships around turn 7–8 (completing a longship around turn 10–11). The AI should plan 2 longships simultaneously — one for east/west exploration, one for troop transport. Dedicate 4 welf (sailing) + 1 welf (shipbuilding) groups from turn 5.

---

### Recommended Opening (Turns 1–5)

**Turn 1 (in Nexus):**
- CLAIM maximum silver available from unclaimed pool
- Set faction points: `faction magic 4 martial 1` (upgrade magic cap immediately)
- Buy 1 orc from market if available
- CAST Gate_Lore RANDOM UNITS (to explore)
- Name unit "Pied Piper", set `BEHIND 1`, `AVOID 1`
- Form 1 new unit: `buy 1 orc`, `study stea` (stealth scout), give 50 silver

**Turn 2 (landed in starting region):**
- Observe region type and available races
- CLAIM 400-600 silver
- Form 5 orc/local-race scouts with 70 silver each, send to all 6 adjacent hexes (some may fail if ocean)
- CAST Gate_Lore RANDOM (explore more map)
- Study stea (stealth on mage — reaches level 2 quickly and provides mage safety)
- Declare faction 2 (Creatures): Unfriendly

**Turn 3 (Turn 2 report received):**
- Read all 6 scout reports. Identify which adjacent regions have which races for sale
- Based on race availability: buy 3-5 units optimized for each region
  - Forest: 3 welf (1 study entertainment, 2 study lumberjack)
  - Mountain: 2 hdwa (study entertainment then quarry/mining)
  - City/town: 5-10 gnomes (study entertainment)
  - Swamp: 2 gbln (study entertainment)
- Buy 10-30 welf at nearest forest for first combat/IPS unit
- CAST Gate_Lore RANDOM on mage
- Study combat foundations: mage switches to `study forc` (force)

**Turn 4 (combat/IPS unit in forest):**
- First IPS unit: 30 welf, set `GUARD 1`, `AUTOTAX 1`, `BEHIND 0` (needs to be visible to tax)
- Buy 2 welf shipbuilding, 2 welf sailing (begin ship prep)
- Buy 4 hdwa weaponsmith (start weapons)
- CAST Gate_Lore GATE [known gate number] to travel to high-value region
- Study force (continues)
- Declare friendly to visible allied factions

**Turn 5 (IPS collecting first taxes):**
- IPS unit taxing: expected $800-1200 first collection
- Mage switches to `study patt` (pattern — needed for fire)
- Buy 2 hdwa mining (for iron production)
- Launch 1 lumberjack welf unit `produce wood`
- Form farming unit: 7 welf `study farm`
- Begin second IPS unit formation at next forest/plain region
- Entertainment units all set to `@entertain`

---

### Mid-Game Plan (Turns 6–15)

**Economic targets:**
- By turn 8: 3+ IPS units taxing for total $2,000+/turn
- By turn 10: grain farming + wood + fish + entertainment contributing $500+/turn passive
- By turn 12: 6+ IPS units covering all region slots, $5,000+/turn combined tax
- Ship(s) deployed for coastal exploration and troop transport by turn 11

**Magic targets:**
- Turn 6-7: Mage reaches force 2, pattern 2
- Turn 8-9: Mage studies fire → fire 2 (combat-ready with fireball by turn 9–10)
- Turn 10-12: Mage studies artifact lore (for enchanting endgame)
- When new mage leaders arrive: immediately assign force → pattern → fire track
- Target: 2 combat fire mages active by turn 12, 4 by turn 15

**Military targets:**
- All IPS units equipped with pikes by turn 10 (weaponsmith unit producing continuously)
- Armorers producing leather armor distributed to combat units by turn 11
- By turn 14: each IPS has 30 men, pikes, armor = can resist monster attacks

**Production targets:**
- Shipyard: 2 longships by turn 12
- Woodcutters: 3 welf lumb3 units producing max ironwood
- Carpenters: 3 welf carp3 for magic wagon production (very high value)
- Miners: 5 hdwa mini3 producing iron for weapons
- Quarriers: 5 hdwa/idwa quar3 producing stone for buildings

**Underworld:**
- Identify shaft entrance on map (visible in reports)
- Send 1 goblin/drow scout unit down by turn 7
- Establish taxation unit by turn 9
- Recruit drow elves locally for specialized production

**Diplomacy:**
- By turn 5: Declare friendly to all visible nearby factions except known hostile
- By turn 10: Identify key alliance targets (Silver Hand equivalent) and declare ally
- Never attack another player without provocation; maintain cooperative posture

---

### Adaptations for Dynamic Conditions

**If starting region has no forest (no wood elves available):**
Use the dominant local race as the core IPS troop. Ice dwarves (combat to 2) work in tundra. Goblins for crossbow units. Scale up magic budget if military units are weaker.

**If early turns encounter aggressive neighbors:**
- Immediately set all scouts to `AVOID 1`
- Accelerate combat mage training — skip stealth on the primary mage, go straight to force → pattern → fire
- Build IPS units faster, preferring size (30 troops) over diversification
- Seek ally declarations with all nearby non-hostile factions for mutual defense

**If gate teleportation is blocked or useless (no gates in starting region):**
- Focus the mage on force → pattern → fire immediately (no gate scouting)
- Deploy orc scouts via movement instead (send 2–3 at a time)
- Save gate lore study for later when the mage can use it for tactical movement

**If silver income is slow (starting in poor region):**
- Prioritize entertainment economy: 10 gnome entertainers at a city provide $300/turn
- Delay combat unit construction by 2–3 turns
- Focus on a single well-chosen IPS region rather than spreading too thin

**If the faction cap is hit early (10 regions):**
- Immediately focus on deepening productivity of existing regions
- Build larger IPS units (30+ troops) in each existing region to maximize tax
- Invest in production buildings if available
- Focus magic research on artifact production and enchanting

**If allies fight among themselves:**
- Remain neutral unless directly threatened
- Faction 70 never issued hostile declarations against player factions in turns 1–20
- If asked to contribute troops to ally battles, send 1-2 combat mages (high value, low cost)

**If an IPS region is attacked:**
- If overrun: retreat main combat unit (it has `AVOID 1` backup option)
- Immediately reinforce with nearby combat units
- Request ally support
- Do not attempt to hold a region against a significantly stronger enemy — evacuate and rebuild elsewhere

**If the mage is threatened (low stealth vs. enemy observation):**
- The mage always stays `BEHIND 1` and `AVOID 1`
- Keep the mage in a controlled region, never in unscouted territory
- If enemy is known to have assassins: add observation units to the mage's hex (higher observation detects assassins)
