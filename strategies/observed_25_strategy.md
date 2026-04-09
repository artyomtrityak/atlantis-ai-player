# Faction 25 Strategy Analysis

Faction: **Silver Hand (25)**
Game: Atlantis New Origins, Version 3.0.0 (beta)
Analysis covers turns 1–20 (January Year 1 – September Year 2)

---

## Section 1: Observed Playstyle (Turns 2–20)

### Starting Conditions

**Faction name:** Silver Hand (25)  
**Faction type:** Martial 1, Magic 1 at start; quickly upgraded to Martial 2, Magic 3 by turn 3  
**Starting race:** Leader (unit 879, named "The Elf", described "An old Elf with a staff")  
**Starting location:** Spawned in nexus (0,0), immediately cast "Random Gate Jump" in turn 1, landing at mountain (6,76) in Phigill — a mountain region with 1253 orc peasants, producing grain, iron, and stone. Wages $11.2/man.  
**Starting resources:** ~10,450 unclaimed silver after the jump  
**Initial skills on The Elf (unit 879):** observation 1, force 1, pattern 1, spirit 1, gate lore 1, fire 1, combat 3

The faction started with a single leader mage, no territory, and a large silver reserve in unclaimed funds. The gate jump was used immediately to reach the world.

---

### Economic Strategy

**Core economy: taxing + resource production + perfume trade**

The economic system was built in a highly systematic way across multiple regions:

**Phase 1 (Turns 2–4): Rapid force-entry into mountain regions**

The player immediately spent large sums (5,000+ silver) in turn 2 to create a full complement of specialized units, all bought at the starting mountain (6,76):
- Scouts (1 orc each) sent N, NW, SW, S to probe adjacent regions
- Workers (10 orcs) assigned farming
- Guards (6 orcs) for taxing
- Two Advisors (leaders) for magic study
- A building specialist unit (5 orcs, building skill)
- A quarrying specialist (5 orcs)
- A mining specialist (5 orcs)

All units immediately used `consume faction` and `reveal faction` — a pattern maintained for mages and leader units throughout.

**Phase 2 (Turns 3–6): Region capture and distributed economy**

By turn 4 (May Year 1), faction controlled 1 region; by turn 6 (July Year 1), 7 regions. The template was replicated in each region:
- 1 Guards unit (5 race-appropriate soldiers, combat skill) to tax and guard
- 1–2 Workers units with farming (produce grain/livestock for food maintenance)
- 1 Workers unit with mining (produce iron)
- 1 Workers unit with quarrying (produce stone)
- 1 Workers unit with the local race's specialty (e.g., lumberjack for goblins, weaponsmith, armorer)

Regions occupied (by turn 6):
- Mountain (4,74) Phigill — hill dwarves
- Mountain (6,74) Phigill — hill dwarves (first secondary region)
- Mountain (5,75) Phigill — hill dwarves
- Mountain (6,76) Phigill — orcs (starting hex, gate 657)
- Mountain (5,77) Phigill — humans
- Swamp (6,78) Filebom — goblins
- Swamp (6,80) Filebom — lizardmen

**Race hiring strategy:** The player hired whatever race was locally available rather than importing. Hill dwarves for mountains (mining/armoring specialty), goblins for swamps (lumberjack, weaponsmith), lizardmen for southern swamps. This minimized transportation cost.

**Tax income growth:**
- Turn 5 (June Y1): Guards collecting from 4 regions, ~$1,150/turn
- Turn 7 (Aug Y1): ~$1,650/turn from 5 regions
- Turn 8 (Sep Y1): Guards in (6,74) and (5,75) collecting $500 each after dwarf reinforcement — ~$2,200/turn
- Turn 11 (Dec Y1): ~$2,800/turn
- Turn 15 (Apr Y2): ~$3,000/turn (base regions)
- Turn 20 (Sep Y2): Base 5 regions ~$3,300/turn, plus newly captured city of E'egrad (5,79) generating $4,950/turn (3 guards units each taxing $1,500–1,750)

**Food-maintenance system:** Early game, farming units produced grain/livestock to feed nearby mage/guard units. A `consume faction` + food-sharing borrowing system was used to route food to expensive units (leaders cost 50 silver or 2 food). This was an intentional cost optimization.

**Perfume trade (turns 7–20+):** A dedicated trade scout (unit 2660) with a horse was deployed to cycle between E'egrad city (sells perfume at 90–107 silver buy price) and selling regions (achieving 340–395 silver/unit). This scout bought 17–25 perfume per cycle for ~$2,000–3,000 investment and sold for ~$6,000–8,000 — a consistent 3x markup trade route. This trade route was operational from at least turn 7 onward.

A second trade scout (unit 2931) also traded perfume on a parallel route by turn 10–11.

**Quartermaster logistics (turns 9–15):** Worker (3088) was trained as a Quartermaster (studied 2 turns). Multiple production units used `transport 3088 all IRON/STON/CARM` to pool resources. However this unit was assassinated in turn 12, causing TRANSPORT errors for 3+ turns. The player recovered by continuing transport orders to the new quartermaster (unit 3091).

**Resource production pipeline (turn 14+):**
- Iron producers: Workers (3614), (3015), (2946), (2281) across multiple mountains
- Stone: Workers (3022), (3613), (3619)
- Mithril: Workers (3616) in mountain (6,74), Workers (3070) in mountain (5,75)
- Chain armor: Workers (3073) with armorer skill (hill dwarves)
- Picks: Workers (2927) with weaponsmith skill
- Crossbows: Workers (2596) with goblin weaponsmithing
- Wood: Workers (2592) in swamp

**City capture (turn 20):** E'egrad city (5,79 Febefe) was captured in an alliance with Trader Enclave (30). Combined forces (Silver Hand + Trader Enclave + Wandering Minstrels faction 70 mages) attacked the 120-leader City Guard. Silver Hand contributed Guards (4377) 35 gnomes/swords/chain armor, Guards (3650) 80 gnomes/90 crossbows, The Elf and two advisor mages (fireballs), Guards (5807) 35 gnomes/swords. The city previously had city taxes of ~$8,000+. Post-capture taxing in turn 20 shows three Silver Hand guard units each collecting $1,500–1,750 from the city.

---

### Military Strategy

**Philosophy:** Defense first via guards+tax, military units grow slowly, coordinated coalition attack for city capture.

**Guard units:** Each taxing region had a Guards unit (5 men with combat 1) that doubled as tax collectors. Guards were built with locally available races. By turn 8, some guards were being reinforced to 10 men to increase tax capacity (e.g., Guards 2277 in mountain 6,74 went from $250 to $500 tax).

**Combat unit development:** The player built dedicated combat units (Guards 4377, 3650) much later — these appear from turn 10 onward as gnome-based crossbow/sword forces funded through the trade profits.

**Guards (3650):** The main combat force. Built in the E'egrad city area with gnomes carrying crossbows (crossbow skill 2). By turn 14 this unit had 40 gnomes, by turn 18 it had 80 gnomes + 90 crossbows + 20 goblins.

**Guards (4377):** Secondary combat unit, 35 gnomes with swords + chain armor.

**Guards (5807):** Third combat unit, ~30–35 gnomes with swords + chain armor.

**Tactics specialist:** Dwarf general (4376) — a leader with tactics 2, serving as tactical coordinator for the main army.

**Alliance for city assault (turns 19–20):** Silver Hand joined Trader Enclave (30) in attacking E'egrad city. The Wandering Minstrels (faction 70, a friendly faction) contributed mage units (4427, 4432, 4438) casting fireballs. The combined attack killed the 120-leader City Guard in one round, with Silver Hand advisors casting fireballs for 13+4 kills each.

**Casualties:** Silver Hand took no losses at E'egrad in turn 19 (the allied attack). Turn 17: lost two explorer scouts to monsters (high elf scouts probing new territories killed by Undead and Lizard Men). Turn 9: Guards (1909) killed by a Dragon in mountain (5,77) — a single-orc guard with combat 1 was outclassed; the Dragon was a known hazard seen in turn 3.

**Notable: no offensive expansion through combat before turn 19.** All expansion was through sending scouts, finding unoccupied or lightly guarded regions, and placing guard units.

**Pirate threat (turn 18):** Workers (4348) — 3 lizardmen in ocean — destroyed by pirates. These were likely sea-exploration units caught in open water.

---

### Magic Development

**The Elf (879) — main mage:**
- Turn 1: force 1, pattern 1, spirit 1, gate lore 1, fire 1, combat 3
- Turn 2: force 2
- Turn 3–6: studying fire (reaching fire 2 by turn 6)
- Turn 7+: studying pattern
- Turn 9+: moved to E'egrad area with advisors, teaching spirit to advisors
- Turn 11: Teaches Earth Lore magic to advisor 1913
- Later: The Elf focused on force, pattern, spirit, fire trees for fireball capability
- Turn 20 combat: cast fireball in city battle (confirmed by practice: "force [FORC]")

**Advisor 1913 (Elven advisor -red-):**
- Turn 3: force 1 (taught by The Elf)
- Turn 4: force 2 (30-day teaching acceleration)
- Turn 5: fire 1 (taught)
- Turn 6: fire 2
- Turn 7: pattern 1 (taught)
- Turn 8–9: pattern skill continued
- Turn 10+: earth lore — casting "Earth Lore" raising 33–74 silver/cast as passive income
- Turn 19: Casts fireballs in city battle (kills 13 City Guard leaders in one cast)

**Advisor 1914 (Elven advisor -blue-):**
- Parallel to 1913, same teaching path: force → fire → pattern → spirit
- Turn 20: Casts fireball in city battle (kills 4 City Guard + 5 in second battle)

**Advisor 2286 (Elven advisor -green-):**
- Started one turn later (formed turn 3)
- Same path: force → fire → pattern → spirit
- Taught spirit by The Elf (turn 13–14)
- Turn 20: casts fireball

**Three mage units (4427, 4432, 4438) — new mages (turn 14):**
- These were formed in turn 14 from The Elf's teaching force (3 new leaders, each getting force 1 taught)
- These were Wandering Minstrels (faction 70) units that Silver Hand was funding with 150 silver/turn each
- By turn 19 these also cast fireballs in battle

**Magic progression summary:**
- Core path: force → fire → pattern → spirit (fireball requires force+fire+pattern+spirit all at appropriate levels)
- Earth lore (1913): passive income 33–74 silver/cast/turn as secondary
- No gate lore used after turn 1
- No combat spells other than fireball
- Teaching acceleration was consistently used: The Elf taught 3 advisors simultaneously each turn, giving 30-day teaching bonuses

**Key observation:** The player reached fire 2 + pattern 1 quickly (by turn 7–8) and then began teaching the advisors spirit while continuing to raise pattern. The fireball capability was operational by turn 19 (~2 full years).

---

### Expansion Pattern

**Geographic cluster:** All activity in a 4x4 hex cluster in Phigill/Filebom/Febefe, centered on mountain (6,76). The player did NOT expand beyond this home cluster until late mid-game.

**Scouting method:** Single-man orc scouts deployed from the starting hex in all 6 directions (turn 2). Each scout was sent to the next hex, then if empty, sent further. From turn 5, a horse-mounted scout (1910) sped up range.

**Early home cluster (turns 2–6):** Six adjacent mountains and swamps fully settled with guard+workers teams.

**City proximity:** E'egrad city at (5,79) was spotted in turn 3 (south of mountain 5,77). The city had a 120-leader guard, making direct capture impossible early. The player placed a scout in the city immediately but did not attempt capture until turn 19.

**Second expansion wave (turns 9–15):** Scouts were sent south via the Febefe corridor (tundra (5,81), (5,83), (6,82)). A sea-swimming lizardman scout (2951) explored the eastern continent (Gawdylcre/Lerrot) starting turn 12. High elf scouts (5383, 5398, 5411, 5447, etc.) were bought in turns 15–17 to explore more distant regions (Goo'ecy, Attprorspa). Several of these were lost to monsters.

**New taxing regions (turn 16–18):** Regions opened in:
- Plain (10,80) in Goo'ecy — Guards (4547) collecting $600/turn by turn 20
- Additional regions in Febefe area

**Volcano (3,75) in Phigill:** Spotted turn 5, reached by scout. Produces iron+stone but no wages or peasants. Workers eventually assigned here (turn 17+) for resource extraction. Guards (4768) assigned to move to volcano turn 19–20 for territorial control.

**Continent exploration:** Scout (2951) reached forest (Gawdylcre) via swimming, then plain (9,79 Lerrot). Wood elf units were acquired by turn 13 from this region (scout bought 1 wood elf). This appears to be scouting/intelligence rather than active colonization.

---

### Turn-by-Turn Summary

**Turn 1 (Jan Y1):** Unit 879 claims 100 silver, studies force, casts Random Gate Jump — lands at mountain (6,76). This was a planned start strategy.

**Turn 2 (Mar Y1):** Report shows turn 2 results. The Elf attempted gate cast to escape nexus but failed. Faction upgraded to Martial 2, Magic 3 immediately.

**Turn 3 (Apr Y1):** Mass formation event — 9 new units formed in one turn: 4 scouts, 2 worker teams, 2 advisors, 1 guard team. Total silver claimed: ~$3,500. All units assigned long-term roles with `@` (permanent) orders. Scouts deployed to 4 adjacent hexes. Mining, farming, building, quarrying skills all begun simultaneously.

**Turn 4 (May Y1):** Second wave formations in mountain (6,74) — 3 hill-dwarf units (combat, mining, farming). Formation in swamp (6,78) — 3 goblin units (combat, lumberjack, farming). Scout reached E'egrad city (5,79). First region controlled (mountain 6,74 or 5,75 likely).

**Turn 5 (Jun Y1):** 7 regions visible. Horseback scout (1910) deployed with horse withdraw for faster movement. Fire combat spell set on advisors. Workers 2594 studying weaponsmith. Guard units in 4 regions collecting taxes. Advisor 2286 begins fire study.

**Turn 6 (Jul Y1):** The Elf, Advisors 1913/1914 move to swamp 6,78 then to E'egrad (5,79) — likely for gate access or economic opportunity. Guard 2595 had a guarding conflict with another unit. Scout 2660 formed in E'egrad with horse — this becomes the dedicated perfume trade unit.

**Turn 7 (Aug Y1):** All three advisors study pattern (The Elf teaching). Trade scout 2660 buys 3 perfume in E'egrad, moves to Filebom region to sell. Workers begin producing iron (2285), stone (2284), and building (2283). Quartermaster training begins (Worker 3088 starts studying).

**Turn 8 (Sep Y1):** Major economic scaling. Guards in mountains (6,74) and (5,75) now collecting $500/turn each (up from $250) after reinforcement. Trade scout sells perfume. Mining/quarrying/building skill workers at level 2 begin producing iron and stone. Advisors withdraw horses.

**Turn 9 (Oct Y1):** Dragon kills Guards (1909) in mountain (5,77). The player moves The Elf and advisors from mountain (6,76) to E'egrad (5,79) to rebase. New worker unit (3088) studying quartermaster. Trade Scout 2931 begins operating. New scouts (2935, 2937) explore south.

**Turn 10 (Nov Y1):** Quartermaster Worker 3088 reaches QM level 1. TRANSPORT commands begin routing resources. Armorer workers produce chain armor. Mithril mining begins (workers 3616 in mountain 6,74). First mithril produced: 5 mithril. Guards 3650 forming in E'egrad area with 20 gnomes.

**Turn 11 (Dec Y1):** Advisor 1913 casts Earth Lore for 33 silver (first cast). Trade routes actively cycling. Perfume sold by Scout 2660 for $373 each. Scout 1908 caught stealing — a deliberate stealth skill-raising attempt.

**Turn 12 (Jan Y2):** Quartermaster (3088) **assassinated** in mountain (6,76). This caused TRANSPORT errors for multiple turns. New leader unit (3091) begins training as replacement quartermaster. City guard unit 1526 attempted entry to mountain (5,75) and (6,76) — forbidden entry by Silver Hand guards.

**Turn 13 (Feb Y2):** Advisor 2286 begins teaching spirit to advisors 1913 and 1914. The Elf teaches pattern to The Elf (self-practice via teaching). Scouts 4348, 4349, 4360, 4362 formed with lizardmen to explore seas. Scout 2951 reaches continent Gawdylcre.

**Turn 14 (Mar Y2):** Three new mage units formed (4427, 4432, 4438) — The Elf teaches force to all three simultaneously. These are allied Wandering Minstrels (70) leaders funded by Silver Hand at 150 silver/turn each. Wood elf units acquired. Guards 4377 formed with 35 gnomes for military use.

**Turn 15 (Apr Y2):** Multiple high elf scouts (5383, 5398, 5411, 5447, 5465, 5467, 5488) each buying 1 high elf from city market — these are exploration probes for distant territories. Region count stays at 6 but scout radius expands massively. Guards 3650 now at 40 gnomes, buying more.

**Turn 16 (May Y2):** Guards 1916 has 200 silver stolen (enemy stealth action). Worker 3091 becomes quartermaster (finally). TRANSPORT commands working again. High elf scouts being lost to border-blocking factions. Two new leader units (4547, 4549) formed — possibly for mage apprentices.

**Turn 17 (Jun Y2):** Two high elf scouts killed by monsters (Undead in swamp 10,78; Lizard Men in swamp 11,79). Region count reaches 8. Swords production begins from Workers 2927 (weaponsmith with iron). Fish production/trade visible. Army begins consolidating at E'egrad.

**Turn 18 (Jul Y2):** Dragon kills Trader Enclave miners in mountain (5,77) — Silver Hand is not involved but sees it in report. Workers (4348) with lizardmen destroyed by pirates in ocean. Scout 2951 reaches Lerrot continent. New formations for the army: Guards 4835, 4882 likely forming military units. Workers 2927 produces 15 swords delivered to quartermaster.

**Turn 19 (Aug Y2):** **First major battle.** Allied forces (Silver Hand + Trader Enclave + Wandering Minstrels) attack City Guard (68) in E'egrad. 120-leader city guard killed in one round — a devastating fireball barrage from 5 mage units. Silver Hand takes 12 casualties from city guard counterattack (absorbed by Guards 4377). Silver Hand advisors 1913 and 2286 each fire 13+ fireballs killing 13 and 4 respectively in the first battle.

**Turn 20 (Sep Y2):** Second city battle — Guards 6095 attacks City Guard 8652 (a respawned replacement city guard of only 12 leaders). Silver Hand wins decisively in one round, advisor 1914 kills 4 with fireball. City now fully controlled. Three Silver Hand guard units collecting $1,500–1,750 each from E'egrad. Total faction tax income jumps dramatically. Faction building mines in mountain (4,74). Region count 10. Scouts reaching Wuydilberg continent far away.

---

### Strengths and Weaknesses

**Strengths:**

1. **Excellent template replication:** Each region gets the same economic unit set (guard + mining + farming + specialty workers). This is scalable and self-funding through taxes.

2. **Fast faction upgrade:** Martial 2 Magic 3 declared on turn 2, allowing more mages and regions immediately.

3. **Magic advancement through teaching:** The Elf taught 3 advisors simultaneously every turn, massively accelerating their development via 30-day teaching bonuses. By turn 7, all three advisors had force 2 + fire 2 — faster than solo study.

4. **Perfume trade route:** Established extremely early (turn 6–7) and maintained for 13+ turns. The 3x markup on perfume generated consistent 4,000–7,000 silver per cycle, which funded the entire magic development and military buildup.

5. **Alliance leverage:** Friendly relations with Wandering Minstrels (70) and Trader Enclave (30) were leveraged for city capture. Silver Hand funded the Minstrel mage units (150 silver/turn each) to accelerate their development, then used them as allies in battle.

6. **Resource self-sufficiency:** Iron, stone, wood, mithril, grain, livestock all produced locally. Chain armor, swords, crossbows, picks all manufactured. No dependency on external sources.

7. **Avoid/behind flags on workers:** Nearly all worker units set `avoid 1` and `behind 1`, protecting them from attacks.

**Weaknesses:**

1. **Delayed military buildup:** Dedicated combat units (beyond local tax guards) only appear in turns 10+. The faction was vulnerable to attack for the first 8 turns.

2. **Quartermaster assassinated (turn 12):** The single quartermaster was killed, disrupting the logistics pipeline for 3+ turns. No backup QM or building to protect the QM.

3. **No fortifications built early:** Building units studied building/quarrying skills but no tower or fort was completed for mage study protection until later. This meant mages couldn't study above level 2 freely (warning seen turn 15 for Advisor 2286).

4. **Exposed scouts lost to monsters:** Several high elf scouts were killed probing hostile regions. These were single-man units with no combat ability.

5. **Guards (1909) lost to Dragon:** The 1-orc guard unit in mountain (5,77) was visible to a known dragon and was killed. The player should have seen this coming.

6. **TRANSPORT errors for 3+ turns:** After QM assassination, orders kept referencing the dead unit (3088). Better error recovery needed.

7. **Slow territorial expansion:** Only 6 regions held for most of year 1 and much of year 2. The player could have expanded faster given their silver reserves.

---

## Section 2: AI Agent Strategy (Based on This Playstyle)

### What the AI Would Keep

1. **Random Gate Jump start:** The gate jump from nexus is fast, cheap, and bypasses the slow 1-region start. The Elf's starting skills (combat 3, force 1, fire 1, etc.) are strong enough to survive anywhere. Keep this approach.

2. **Immediate faction upgrade to Martial 2 Magic 3:** Declare this in the first order (using `@FACTION MARTIAL 2 MAGIC 3`) to unlock 4 mages and 25 regions from the start. The cost is reasonable.

3. **Template-based region settlement:** The guards+mining+farming+specialty pattern is highly efficient. Replicate it in every region without overthinking. The AI should have pre-defined templates for mountains (hill dwarves: combat+mining+quarrying+armorer), swamps (goblins: combat+lumberjack+weaponsmith+farming), tundra (gnomes: combat+herb lore+crossbow+farming).

4. **Perfume trade route:** Buy perfume at E'egrad (or equivalent city), sell elsewhere. This is the best early-game silver multiplier. Establish it by turn 4–5 with a dedicated horse-mounted scout.

5. **Teaching acceleration for mages:** The Elf should always be teaching 3 other mage units simultaneously. 30-day teaching is twice as fast as solo study. Budget 100 silver/mage/turn for this.

6. **Consume faction + food production:** Workers producing grain/livestock for faction food consumption is cheaper than paying 50 silver maintenance per leader. This pattern should be automated.

7. **Avoid+Behind on workers:** Every worker/production unit should have `avoid 1 behind 1` to protect against opportunistic attacks.

8. **Alliance diplomacy:** Establish Friendly relations immediately (Trader Enclave 30 and Wandering Minstrels 70 were marked Friendly by turn 5). Fund allied mage units — it pays off in combined military actions.

### What the AI Would Change

1. **Build fortifications EARLIER.** Faction 25 didn't build towers or forts to protect mage study above level 2, causing a cut to study rate (warned in turn 15). The AI should build a Tower (10 stone) or Stockade (60 wood) in the main base by turn 6–7. Once quarrying workers produce stone, assign building workers to construct a Fort immediately. This protects the main mage hub and enables level 3+ study.

2. **Train a backup quartermaster / protect the QM.** The assassination of Worker 3088 (the first QM) disrupted logistics for 3+ turns. The AI should: (a) have the QM inside a fortification to reduce assassination risk, (b) begin training a second QM in parallel, (c) avoid referencing the QM in TRANSPORT orders until they have reached QM level 1 (the player had TRANSPORT errors for 3 turns because orders referenced a dead target).

3. **Don't place single-man guards in monster-visible hexes.** The 1-orc Guards (1909) in mountain (5,77) was killed by the known Dragon. The AI should either (a) not guard a region with a dragon cave, (b) use a stronger force, or (c) set `noaid 1` to avoid drawing monster attention.

4. **Establish mage path more decisively.** Faction 25 spent turns 5–8 studying fire on The Elf before switching to pattern. The AI should commit to the fireball path (force → fire → pattern → spirit) and plan the full sequence from turn 1, targeting when each mage reaches each level. The AI should also note that mages need a fort/castle to study above level 2.

5. **Expand territory faster in turns 5–10.** With $3,000–5,000 unclaimed silver available throughout year 1, the AI could establish 2 additional regions per turn instead of 1. Each new region adds $250–500/turn in tax revenue. Faster territorial expansion compounds the advantage.

6. **Don't attempt stealth theft (failed turn 11).** Scout 1908 was caught stealing from Sunshine (5), a neutral faction. This gains stealth XP but risks diplomatic damage. The AI should not steal unless deliberately building a thief unit as a deliberate capability.

7. **Plan quartermaster logistics from turn 5, not turn 9.** The player started training a QM only in turn 9. The TRANSPORT system enables efficient resource pooling (iron/stone/armor all funneled to one point). Starting this earlier enables weapon/armor production sooner, which means a military force capable of city capture by turn 15 instead of turn 19.

8. **Military units should have weapons and armor.** Guards (4377) with 35 gnomes + swords + chain armor were very effective at E'egrad. The AI should start building such units from turn 10 (once iron, weapons, and armor production is running) rather than relying on unequipped guards.

### Recommended Opening (Turns 1–5)

**Turn 1:**
- Unit 879: `@claim 100` (or appropriate amount), study force, cast gate lore random jump, `avoid 1`, `name unit "The Elf"`, `describe unit "An old Elf with a staff"`
- Declare `@FACTION MARTIAL 2 MAGIC 3` immediately

**Turn 2 (after gate jump, now in new region):**
- Analyze the starting region: what race sells here, what's available for sale (leaders, race units), what resources produce?
- The Elf: study force (continue), teach any already-present units
- Form scouts (1 local race unit each) in all 6 directions with `move [direction]` and `@reveal faction`, `avoid 1`
- Form 1 Guards unit (5–6 local race) for taxing next turn: `study "combat"`, `avoid 0`, `behind 0`
- Form 2 Workers units (5–10 local race) for production: assign `@produce [primary product]` and `@produce [secondary product]`
- Form 2 Advisors (buy 1 leader each): study force with teaching accelerator from The Elf: `teach [advisor1] [advisor2]` on The Elf's orders

**Turn 3 (first full production turn):**
- Guards unit: `guard 1`, `@tax`, `hold 1` — begin taxing
- Workers: begin producing resources
- The Elf: `teach [advisor1] [advisor2] [advisor3]` — accelerate magic
- Form more units in newly scouted adjacent regions: replicate the Guards+Workers template in each region a scout confirmed safe
- Advisors: `@study "force"` (with teaching)

**Turn 4:**
- Form a dedicated trading scout: `buy 1 [local race]` or `WITHDRAW 1 "horse"`, assign to buy perfume at nearest city and sell for profit
- Continue teaching chain: by now advisors should have force 2
- Claim silver strategically to fund remaining units
- Declare faction attitudes: `declare 70 Friendly` (Wandering Minstrels), `declare 30 Friendly` (Trader Enclave) if observed

**Turn 5:**
- Advisors transition to studying fire (with The Elf teaching)
- Set `combat "fire"` on all mage units
- Place building + quarrying workers in base region to produce stone for future fort
- Expand Guards into 2 more regions if scouts found empty hexes
- Begin studying `quartermasters` on a leader unit (`@study "quartermaster"`) — this takes 2 turns to reach QM 1

### Mid-Game Plan (Turns 6–15)

**Magic priority:**
- Force → Fire → Pattern → Spirit on all 3 advisors (using teaching each turn)
- Reach fire 2 by turn 7–8, pattern 1 by turn 9, spirit 1 by turn 11
- Once all three advisors have fire 2 + pattern 1 + spirit 1, they can cast fireballs
- The Elf should also develop earth lore for passive income (teach earth lore to one advisor as secondary)

**Economic priority:**
- Establish perfume trade route by turn 5, increase to 2 traders by turn 8
- Quartermaster becomes operational by turn 7 — begin TRANSPORT chain for iron → armor → military
- Each region should be at near-maximum tax capacity (upgrade guards from 5 to 10 men as treasury allows)
- Build armorer workers for chain armor production (hill dwarves ideal)
- Build weaponsmith workers for swords + picks production

**Military build:**
- Turn 6–8: Form first gnome combat unit (buy gnomes from city if available, or available race with crossbow access)
- Turn 10: Begin equipping combat unit with crossbows or swords + chain armor (once production is running)
- Turn 12: Second combat unit formed
- Turn 14–15: Military force ready for city assault (need 3+ combat units plus 3 mages for fireball)

**Infrastructure:**
- Build Tower or Fort in main base by turn 7 (enable mage level 3+ study)
- Build Mine in key mining region to boost iron production
- Keep QM inside a fortification to prevent assassination

**Diplomacy:**
- Fund allied mage units (Wandering Minstrels) 150 silver/turn — they become fireball mages who fight alongside you
- Maintain Friendly status with Trader Enclave — they provide combined military force for city assaults

**City assault planning:**
- Identify target city by turn 4 (scout it)
- Build 3+ fireball mages to ~fire 2 + pattern 1 + spirit 1 (turn 11–12)
- Build 2–3 combat units with 30–40 men each
- Coordinate with allied faction to attack simultaneously (their mages + your mages)
- Assault city at turn 14–16 rather than waiting to turn 19 as faction 25 did

### Adaptations for Dynamic Conditions

**If gate jump lands in a poor region (low wages, hostile races):**
- Immediately move the gate jump unit again using any gate in the region (gate lore 1 already known)
- Or: accept the region, assess what's nearby, focus on scouting before committing resources

**If the starting region has competition (another faction already guarding):**
- Set attitude to Neutral (default unfriendly is too aggressive early)
- Avoid placing own guard to prevent confrontation
- Send scouts in all 6 directions to find uncontested regions

**If monster attacks guards early:**
- Lose the guard, replace it — don't try to fight monsters with tax guards
- Use the loss as information (dragon here, undead there) to avoid those hexes or bring fireballs

**If perfume trade route is blocked or prices collapse:**
- Switch to herb lore trade (gnome-produced herbs have a trade route)
- Try livestock or grain selling at cities
- Pivot to silk, chocolate, or other city demanded goods if available

**If a faction attacks:**
- Guards units behind their own guards can avoid initial combat
- Mages should withdraw to fortified positions
- Firewall (using combat "fire") as defensive fallback
- Request ally support (Wandering Minstrels, Trader Enclave)

**If the faction falls behind on mage development:**
- Prioritize getting a Fort built (needed for level 3+ study)
- Consider withdrawing a horse and giving it to mages so they can relocate quickly
- Focus on teaching — The Elf should always be teaching, never studying alone

**If the Quartermaster is killed again:**
- Don't send TRANSPORT to the dead QM's unit number for even one more turn
- Have a pre-trained backup already studying quartermaster
- Place next QM inside a building with guards

---

*Analysis based on turns 1–20 (January Year 1 – September Year 2). All observations verified against report events and orders files.*
