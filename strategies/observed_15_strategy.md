# Faction 15 Strategy Analysis

**Faction Name:** Distant Drummer (15)  
**Faction Type:** Martial 1, Magic 4 (changed from Magic 1 in turn 1 to Magic 4 by turn 3)  
**Data Coverage:** Turns 1–20 (reports from turn 2 onward, orders from turn 1)

---

## Section 1: Observed Playstyle (Turns 1–20)

### Starting Conditions

**Starting Location:** Nexus (nexus 0,0), then immediately gate-jumped to tundra (46,84) in Lipodou.

**Race / Units:**
- Starting mage (Grim, unit 869): Leader [LEAD], with an extraordinary pre-loaded skill set: observation 1, force 1, pattern 1, spirit 1, gate lore 1, fire 1, combat 3. This is the primary mage and gate-jumping scout.
- Initial units formed in turn 1 from the Nexus (all bought in tundra 46,84):
  - Glum (1258): leader — mage-in-training, force 1
  - Darkness (1259): leader — mage-in-training (assassinated by turn 7, reused unit number for the stealth unit "Darkness" = formerly Masked 1263)
  - Ghost (1260): leader — mage-in-training, force 1
  - Sagger Mord (1261): leader — necromancer-in-training
  - Masked (1262): leader — observation specialist
  - Masked (1263): leader — stealth specialist (later renamed Darkness)
  - Guards (1264): 11 gnomes — tax guard, home region (46,84)
  - Sea Scouts (1265): 10 gnomes — shipbuilding/sailing/combat multi-role, eventually placed on ship
  - Miners (1266): 3 gnomes — iron production, (later made into Guards/taxers)
  - Scout (1267): 1 gnome — scouted south to (46,86), became 2nd tax guard

**Starting Resources (turn 1 orders):**
- Claimed 100 silver from the game + 5790 silver from CLAIM command in Nexus
- Distributed: 800 each to mages (Glum, Darkness, Ghost, Sagger Mord), 750 to each Masked, 440 to Guards, 400 to Sea Scouts, 120 to Miners, 30 to Scout
- Each leader cost 700 silver; gnomes: 25–30 silver each
- After all purchases and study: ~4410 unclaimed silver remaining in turn 2 treasury

**Faction type change:** The player changed faction from Martial 1 / Magic 1 to Martial 1 / Magic 4 in turn 3, using the `FACTION MAGIC 4 MARTIAL 1` order — enabling 5 mages immediately.

---

### Economic Strategy

**Tax Income (primary revenue source):**

The faction establishes a consistent taxing operation across 3 surface regions plus an underworld region:

| Turn | Region | Tax Guard | Income |
|------|--------|-----------|--------|
| Turn 3 | tundra (46,84) Lipodou (gnome) | Guards (1264), 11 gnomes | $550 |
| Turn 4 | tundra (46,86) Lipodou (ice dwarf) | Guards (1267), 1 gnome | $50 |
| Turn 8 | mountain (43,85) Honvimo (hill dwarf) | Guards (1265), 3 gnomes | $150 |
| Turn 8 | mountain (43,85) Honvimo | Guards (1266), 3 gnomes | $150 |
| Turn 8 | mountain (43,85) Honvimo | Guards (2171), 3 gnomes | $150 |
| Turn 16 | forest (40,84) Tifufirth (wood elf) | Guards (3976), 10→22 wood elves | $500→$1100 |
| Turn 17 | underforest (21,45,underworld) Quabrook | Guards (5023), 13 gnomes | $649→$650 |

**Tax income progression:**
- Turn 3: ~$600/turn (Lipodou home base only)
- Turn 8: ~$1,000/turn (added Honvimo mountain with 3 guard units)
- Turn 16: ~$2,098/turn (added Tifufirth forest)
- Turn 17+: ~$2,748/turn (added underworld Quabrook)
- Turn 18+: ~$3,048–3,198/turn (stable five-region tax base)

**Treasury silver growth:**
- Turn 2: ~3,051 unclaimed
- Turn 4: ~2,424 unclaimed; total faction silver in game (from treasury rank): ~70,530
- Turn 5: ~1,994 unclaimed; total ~94,230
- Turn 6: ~1,634 unclaimed; total ~121,093
- Turn 8: ~1,296 unclaimed; total ~187,042
- Turn 11: total ~341,874
- Turn 12: total ~364,376
- Turn 13: total ~447,810
- Turn 14: total ~533,026
- Turn 15: total ~577,289
- Turn 19: total ~1,056,514
- Turn 20: total ~1,244,573

The silver accumulation is extraordinary — growing from ~$70k in turn 4 to over $1.2M by turn 20. Much of this is the faction's silver "in the world" (held by units) rather than unclaimed, but reflects massive ongoing income from taxes and the Times reward bonus.

**Times Rewards:** The faction collected a 200 silver Times reward every single turn (turns 2–20). This indicates they submitted short articles to the game Times each turn. A minor but consistent income source.

**Production:**
- Iron: Miners (1266) produced 3 iron/turn early, then Guards (1266) at Honvimo taxed rather than produced. Diggers (4290, 7 hill dwarves) began quarrying stone at Honvimo (turn 12), producing ~14 stone/turn at QUAR 1. They later study mining 2 (turn 19), producing ~21 iron/turn.
- Weapons: Smiths (2171, 3 gnomes) produced picks, hammers, swords alternately. By turn 5 they produced 3 picks (from iron), then 3 hammers, then 6 swords. Later they became tax guards at Honvimo.
- Wood: Sea Scouts (1265) withdrew 10 WOOD in turn 3 to build Longship [100].
- Fish: Sea Scouts (1265) briefly studied fishing (turn 5), but mainly the ship sailed for scouting/transport.

**Key economic decisions:**
- All mages funded through SHARE/borrow from the Guard tax units (Lipodou Guards fund the home mages; Honvimo Guards fund Grim and Diggers/Builders).
- By turn 9, Grim gives Guard (1265) a sword and the Smiths/Miners become taxers at Honvimo — converting production units to tax guards.
- At turn 14, Ghost (1260) produces 5 mithril swords via CAST Enchant_Swords (artifact lore 2, enchant swords 1), which are distributed to key mages and the home guard. A major one-time investment payoff.

---

### Military Strategy

**Combat forces are minimal in the first 20 turns.** The faction is not militarily aggressive. No cities are attacked. The strategy is purely "guard and tax," with combat skill developed passively.

**Guard Units:**
- Guards (1264): 11 gnomes, combat 1, on guard in Lipodou. Carries a mithril sword by turn 15.
- Guards (1267): 1→5 gnomes (combined in turn 6), on guard/taxing in (46,86). Receives skeleton support from Sagger Mord.
- Guards (1265/1266/2171): 3 gnomes each, taxing at Honvimo mountain.
- Guards (3976): 10→22 wood elves, on guard in Tifufirth forest (tax $1100/turn by turn 18).
- Guards (5023): 13 gnomes, on guard in underworld Quabrook ($650/turn).

**The Nekojin Empire (faction 26) probed the territory:** In turn 8, Guards (1264) forbids entry to Unit (2291), Nekojin Empire (26). In turn 11, Guards (1265) also forbids entry to Nekojin Unit (2291). This is a deliberate territorial defense response.

**Skeleton forces (Sagger Mord's necromancy branch):**
- Sagger Mord begins SUSK 1 in turn 8, summons 3 skeletons by turn 9.
- By turn 11 he has 4 skeletons; by turn 12 has 6 (SUSK 1 at 2×level/turn).
- Ungrateful Dead (4292): a dedicated skeleton carrier unit — skeletons decay at 8%/turn and are refreshed by Sagger Mord.
- By turn 20, Sagger Mord has SUSK 2 (summons 4/turn), and maintains a pool of ~9 skeletons (with decay).
- The skeletons are not deployed aggressively — they function as a latent threat/garrison pool.
- Grim (869) carries 9-11 skeletons as his battle force by turns 19-20.

**An assassination occurs (turn 7):** Darkness (1259) is assassinated in tundra (46,84) in Lipodou. The attacker was likely a thief from another faction (one of many units visible in the region reports). This is the only combat event in 20 turns involving faction 15 directly.

**Combat training:**
- Masked (1263)/Darkness and Masked (1262) develop stealth 5 and observation 5 respectively by turn 16.
- Masked (1262) studies riding 1→2 from turns 17-19.
- A new mage-tactics leader (Masked 5210) is recruited turn 19, immediately studying TACT (tactics 1 by turn 19, working on level 2 by turn 20).
- Grim studies TACT 1 by turn 19.
- 1st Contubernium (4479): 10 drow elves buying combat training (combat 1→2 over turns 18-20).
- 2nd Contubernium (6522): 10 drow elves, appearing in turn 20.

**The faction begins forming actual combat units from turn 18 onward** — buying drow elves at Cantswinkci village and training them in combat. This signals a transition toward military capability.

---

### Magic Development

This is the faction's defining strength. The player invested heavily in developing multiple mages simultaneously.

**Grim (869) — Primary Mage / Scout:**
- Starting skills: OBSE 1, FORC 1, PATT 1, SPIR 1, GATE 1, FIRE 1, COMB 3
- Turn 2: SPIR 2 (from STUDY SPIR)
- Turn 3: PATT 2 (studied), GATE 1 (35xp from gate jumping practice)
- Turn 4: PATT 2, GATE 1 (70xp)
- Turn 5: GATE 2 (studied to 100xp), PATT 2 (100xp)
- Turn 6: GATE 2 (100), PATT 2 (105), SPIR 2
- Turn 7: FARS 1 (studied), PATT 2 (110)
- Turn 8: FARS 2 (90xp) — teleportation now available
- Turn 9: FARS 2, TELE 1 (30xp)
- Turn 10: TELE 1 (60xp)
- Turn 11: TELE 2 (90xp) — can teleport up to 100 weight units
- Turn 12: FORC 1→2 (studied), TELE 2, PATT 2 (130xp)
- Turns 13-15: Continued FIRE 1→2 development, PATT 2 (145xp)
- Turn 16-18: OBSE 2 (95xp), FORC 2 (90), FIRE 2, PATT 2 (155-160xp), SPIR 2
- Turn 19: TACT 1 (studied)
- Turn 20: SPIR 2 (120xp), PATT 2 (170xp), TACT 1 (30xp)
- Final skills: OBSE 2, FORC 2, PATT 2, SPIR 2, GATE 2, FIRE 2, COMB 3, FARS 2, TELE 2, TACT 1

**Grim's role:** Used CAST GATE RANDOM every turn from turn 1 to turn 8 to scout the world. This is a strategic intelligence-gathering technique — landing in random regions and observing the surroundings. From turn 8 onward, used specific gate jumps (CAST GATE GATE 510) to return home, and later Teleportation for targeted travel.

**Glum (1258) — Secondary Mage / Farsight specialist:**
- Turn 2: FORC 1 (30xp, taught by self)
- Turns 3-4: PATT 1 (studied)
- Turn 5: SPIR 1 (taught by Sagger Mord)
- Turn 6: GATE 1 (30xp)
- Turn 7: FARS 1 (30xp)
- Turn 8: PATT 2 (studied to 90), SPIR 2 (90)
- Turn 9: PATT 2 (105), SPIR 2, GATE 1 (60), FARS 1 (35)
- Turn 10: PATT 2, GATE 1 (60), FARS 1 (75)
- Turn 11: GATE 2 (90xp), FARS 1 (40)
- Turn 12: GATE 2, FARS 2 (110xp) — now can cast Farsight at distance
- Turns 13-14: FARS 2 (studying), GATE 2
- Turn 15: TELE 1 (30xp, from studying)
- Turn 16: TELE 1 (60xp), FORC 2 (95)
- Turn 19: TELE 2 (90xp), FIRE 1 (30)
- Turn 20: Teleported from Lipodou to Honvimo
- Final skills: FORC 2, PATT 2, SPIR 2, GATE 2, FARS 2, TELE 2, FIRE 1

**Glum's primary role:** Casting Farsight every turn to systematically survey adjacent regions — building up a map of territory within range. By turn 12, FARS 2 allows range of 16 hexes. Systematically scanned ocean hexes, plains, and eventually the underworld via coordinated scanning with Grim.

**Ghost (1260) — Artifact / Enchant / Illusion specialist:**
- Turn 2: FORC 1 (30, taught)
- Turn 3: PATT 1 (studied), FORC 1 (60)
- Turn 4: PATT 1, SPIR 1 (60)
- Turn 5: ARTI 1 (studied) — enabled by FORC 1+PATT 1+SPIR 1
- Turn 7: FORC 2 (90)
- Turn 8: PATT 2 (studied)
- Turn 10: SPIR 2 (90)
- Turn 11: ARTI 2 (90)
- Turn 12: ESWO 1 (enchant swords — requires ARTI 2); enchants 5 mithril swords turn 13
- Turn 13-14: ILLU 1 (30, 60)
- Turn 15: ILLU 2 (90), ESWO 1 (35)
- Turn 17-18: Taught FIRE 1 by Sagger Mord; FIRE 1→2 (60→90xp) studied
- Turn 19-20: FARS 1 (30, studied), FIRE 2 (90)
- Final skills: FORC 2, PATT 2, SPIR 2, ARTI 2, ESWO 1, ILLU 2, FIRE 2, FARS 1

**Sagger Mord (1261) — Necromancer:**
- Turn 2: FORC 1 (taught)
- Turn 5: SPIR 1 (35, self-studied+practiced)
- Turn 6: NECR 1 (30, studied)
- Turn 7: SUSK 1 (summon skeletons), FORC 1 (60)
- Turn 8: FORC 2 (95), SPIR 1 (70)
- Turn 9: SPIR 2 (90, cast practice)
- Turn 12: NECR 2 (100), SPIR 2 (105), SUSK 1 (65)
- Turn 13: SUSK 2 (100) — summons 4 skeletons/turn
- Turn 17: Combat spell set to fire; FIRE 1 (30), SUSK 2 (100), NECR 2 (100)
- Turn 18-19: PATT 1 (studying — working toward full mage status)
- Turn 20: FORC 2 (120), PATT 1 (60), SPIR 2 (105), NECR 2, SUSK 2, FIRE 1 (30), in Infidel ship
- Taught FIRE to Darkness (1263) and Ghost (1260) in turn 18

**Masked (1262) — Observer (Observation maxed):**
- Spent every turn from 1-16 studying OBSE: OBSE 1→2→3→4→5
- By turn 11: OBSE 4 (300xp)
- By turn 16: OBSE 5 (450xp) — maximum
- Equipped with mithril sword from turn 15
- Studying riding from turn 17 (RIDI 1→2 by turn 20)

**Masked (1263) / Darkness — Stealthy Assassin:**
- Renamed "Darkness" after original Darkness (1259) was assassinated (turn 7)
- Spent every turn from 1-16 studying STEA: STEA 1→2→3→4→5
- By turn 16: STEA 5 (450xp) — maximum
- Actively steals from neutral factions: Lumen of the Heda (1714) in turn 12, Solaire of the Void (926) turn 13, Shar Ilbechin (1625) turn 14. All attempts yield 0 silver (targets are broke or well-protected)
- Equipped with mithril sword from turn 15
- By turn 18: Taught FIRE 1 by Sagger Mord; FORC 2 (90), FIRE 1→2 (60→90) by turn 20

**Masked (5210) — Tactics Specialist:**
- Appears in turn 19; bought as new leader
- Studies TACT immediately, TACT 1 by end turn 19, working toward TACT 2 by turn 20

**Mage count:** Hit cap of 4 mages (with Magic 4) by turn 3. The faction chose 4 mages + 1 Martial specifically. The original Darkness (1259) was lost to assassination in turn 7, reducing magic capacity. By turn 11, only 4 mages shown. In turn 17, Mages count goes back to 5 — possibly the Darkness/former Masked (1263) crosses some threshold or a new mage slot opens.

---

### Expansion Pattern

**Surface regions controlled (taxed):**
- Turn 3: 1 region (46,84 Lipodou) — home base
- Turn 3: (46,86) Lipodou southward — scouted by Scout (1267) turn 2, starts taxing turn 4
- Turn 4-5: Regions: 2
- Turn 8: mountain (43,85) Honvimo added — Longship "Infidel" sails south then west over ~8 turns, placing 3 guard units (1265, 1266, 2171) at Honvimo. Regions: 3
- Turn 16: forest (40,84) Tifufirth — reached by Infidel after extended sailing patrol (~turns 4-13 exploring); Guards (3976) with 10→22 wood elves placed here. Regions jump to 5 with underworld included.
- Turn 17: underworld (21,45) Quabrook — Guards (5023) with 13 gnomes. Established after Scout (1852) explored the underworld for 15+ turns.

**Underworld exploration:**
Scout (1852), an ice dwarf riding a horse, explored the underworld extensively from turn 6 onward. Starting in (12,44) underworld Silxidcact, moving through Marold, Quabrook regions. By turn 14 reached Cantswinkci village (21,43). By turn 15 settled in (21,45) Quabrook. Guards (5023) arrive in turn 16.

**Surface scouting via Grim's gate jumps (turns 1-8):**
- Turn 2: (21,89) Nenttheen (gate jump)
- Turn 3: (28,90) Co'e (gate jump)
- Turn 4: (21,89) Nenttheen again (returned via gate 496)
- Turn 5: (16,70) Fe'eind (mountain) — observes faction 68 E.V.I.L. territory
- Turn 6: (39,17) Cenintco (plain) — high elves, horses
- Turn 7: (4,12) Wammark (plain) — high elves, horses, Groo the Wanderer (71)
- Turn 8: Returns to home via Gate 510 (specific gate jump)

This reveals the scope of world exploration in just 8 turns using random gate jumping.

**Naval exploration (Infidel Longship):**
The Infidel sails a complex multi-turn patrol route:
- Turns 3-4: East and south from Lipodou
- Turns 5-7: West toward Honvimo mountain (43,85)
- Turns 8-10: North circuit (Onthead city, back)
- Turns 11-13: West and south to Tifufirth forest (40,84)
- Turns 14+: Stationed at Honvimo or Tifufirth, ferrying units

---

### Turn-by-Turn Summary

**Turn 1 (orders only):**
- Start in Nexus; CLAIM 100 + 5790 silver total
- Form 10 new units, all from tundra (46,84) Lipodou
- Grim casts GATE RANDOM and jumps; studies SPIR
- Glum/Darkness/Ghost/Sagger all buy leaders ($700 each)
- Guards buys 11 gnomes; Sea Scouts buys 10; Miners buys 3; Scout buys 1

**Turn 2 (March Year 1):**
- Faction type changed to Magic 4 (via orders turn 3, effect seen in report turn 3)
- Grim jumps to (21,89) Nenttheen via random gate
- Guards (1264) taxes $550 from Lipodou — first tax income
- Sea Scouts (1265) builds first Longship "Infidel" (10 wood withdrawn)
- Glum teaches Force to Darkness, Ghost, Sagger Mord (all get FORC 1)
- New units formed: Sea Scouts (1851, 4 gnomes, sailing), Scout (1852, 1 ice dwarf)

**Turn 3 (April Year 1):**
- Guards (1267) taxes (46,86) Lipodou: $50
- Smiths (2171) formed at Lipodou (3 gnomes, weaponsmith)
- Grim jumps to (28,90) Co'e via gate
- Infidel sails SE toward ocean
- Scout (1852) buys ice dwarf, moves toward Nenttheen
- Guards (2169, 4 gnomes, shipbuilding) formed — will move to (46,86)

**Turn 4 (May Year 1):**
- Infidel sails further south/southwest; Guard (2169) moves to (46,86) — handed off gnomes to the existing guard unit
- Smiths (2171) produces 3 picks from iron
- Grim studies GATE (hits GATE 2 by studying during random jumps)
- Sagger Mord begins teaching Spirit to other mages

**Turn 5 (June Year 1):**
- Sagger Mord teaches Spirit to Glum, Darkness, Ghost all get SPIR 1
- Smiths produces 3 hammers
- Grim jumps to (16,70) Fe'eind — observes faction 68 (E.V.I.L.) mining operations
- Sea Scouts (1265) studies Fishing (error: can't produce fish in this region)

**Turn 6 (July Year 1):**
- Grim jumps to (39,17) Cenintco — centaur territory
- Ghost and Darkness begin ARTI 1 study
- Smiths produces 3 hammers, then 6 swords
- Miners gives iron to Smiths; Smiths gives picks back
- Scout (1852) walks from (24,88) through underworld shaft to (12,44,underworld) Silxidcact
- Scout (2175) is killed by Ice Wurms in (29,91) Co'e — first combat loss

**Turn 7 (August Year 1):**
- **Darkness (1259) assassinated** in Lipodou — one mage lost
- Grim jumps to (4,12) Wammark (high elves)
- Ghost studies FORC 2 (force 2 reached)
- Observation/stealth units: Masked 1262 reaches OBSE 3, Masked 1263 reaches STEA 3
- Sagger Mord studies NECR 1
- Smiths produces 6 swords; these are distributed to mages as weapons in turn 8
- Scout (1852) withdraws a horse in the underworld and begins riding

**Turn 8 (September Year 1):**
- Grim casts CAST GATE GATE 510 — first **specific gate jump** home
- Grim arrives in Lipodou with FARS 2 (after study)
- Guards (1265) becomes guard at Honvimo — first tax expansion to second area
- Sagger Mord: SUSK 1 (summon skeletons)
- Smiths (2171)/Miners (1266) placed as guard units at Honvimo (tax $150 each)
- Guards (1264) forbids Nekojin Empire entry to region

**Turn 9 (October Year 1):**
- First skeleton summon: Sagger Mord summons 3 skeletons
- Error: Grim CAST GATE 510 fails (no such region from Wammark — already jumped)
- Miners/Smiths set to tax at Honvimo
- Ungrateful Dead (4292) formed to carry skeletons
- Grim studies TELE 1

**Turn 10 (November Year 1):**
- Grim studies TELE 1 (60xp)
- Sagger Mord summons 2 skeletons, 1 decays
- Glum casts Farsight on ocean hexes to NE (systematic mapping)
- Grim casts Farsight on Sweron/Trogwern
- Builders (2896, 7 hill dwarves) formed at Honvimo to build fort

**Turn 11 (December Year 1):**
- Glum reaches GATE 2 (90xp) — can detect/jump to specific gates
- Sagger Mord: SPIR 2 (105xp)
- Observation 4 and Stealth 4 reached by the Masked units
- Infidel sails north circuit
- Scout (1852) continues underworld exploration (turn 10-11: Marold region)

**Turn 12 (January Year 2):**
- Ghost reaches ARTI 2 — enables Enchant Swords (ESWO 1) next
- Grim reaches TELE 2 — full teleportation capability
- Diggers (4290, 7 hill dwarves, quarrying) formed at Honvimo
- Ungrateful Dead (4292) now holds 6 skeletons

**Turn 13 (February Year 2):**
- Ghost enchants 5 mithril swords (CAST ESWO) — major equipment milestone
- Builders (2896) begins construction of Fort at Honvimo
- Ghost studies ILLU 1, then 2
- Grim studies FORC 2 (studying fire)
- Sagger Mord: NECR 2 (100)
- Masked (1263) now at STEA 4 (365) — starts attempting theft from nearby units

**Turn 14 (March Year 2):**
- Mithril swords distributed: Glum, Masked (1262), Masked (1263), Guards (1264), Ghost all receive mithril swords
- Sea Scouts (1851) earns $520 from somewhere (possibly taxation error in Honvimo) → passed to Guards (3976, 10 wood elves, new unit)
- Guards (3976) buys 10 wood elves and begins taxing Tifufirth
- Builders (2896): Building 1 (Fort) at 60 skill, beginning construction
- Scout (1852) arrives at Cantswinkci village (underworld)
- Scout (3985, 1 gnome) appears in underworld — second underworld scout

**Turn 15 (April Year 2):**
- Regions jump from 3 to 5 — both Tifufirth and underworld Quabrook now counted
- Guards (5023) with 12 gnomes placed at underworld (21,45) Quabrook
- Guards (3976) taxes Tifufirth $500
- Sagger Mord: SUSK 2 (100) — summons 4/turn now
- Darkness (1263) renamed; steals 0 silver from factions (active but ineffective thievery)
- Ungrateful Dead: 9 skeletons; one decays

**Turn 16 (May Year 2):**
- Guards (3976) taxes $1000 from Tifufirth (bought more wood elves)
- Guards (5023) taxes $649 from underworld Quabrook
- Masked (1262): OBSE 5 max; Darkness (1263): STEA 5 max
- Sagger Mord: SUSK 2 complete; moves to surface (46,84)
- Ghost: ILLU 2 reached
- Building progress at Honvimo continues (fort needs 26 stone of work remaining)
- Builders: BUIL 2 (allows castle building)

**Turn 17 (June Year 2):**
- Mages count back to 5 — new mage Darkness (renamed from Masked 1263) now counts
- Sagger Mord now at Lipodou (moved from tundra 46,86)
- Ghost teaches Fire to Darkness and Glum
- Glum receives FORC 2 from Ghost's teaching
- Building at Honvimo: Fort needs 12 stone to complete
- Diggers: MINI 2 (90xp) — unlocked by also studying MINI
- Guards (5023): $519 accumulated from Quabrook taxing

**Turn 18 (July Year 2):**
- Fort completed at Honvimo! — mages can now study above level 2 there
- Diggers: MINI 2 complete → produce 21 iron/turn (3 gnomes × 7 picks at MINI 2)
- Sagger Mord teaches Fire to Darkness and Ghost in Lipodou
- 1st Contubernium (4479, 10 drow elves, combat 1) formed at underworld Quabrook
- Ungrateful Dead (4292) put on Infidel ship (with skeletons as cargo)
- Grim carries 9 skeletons (given from Ungrateful Dead)
- Glum has 6 skeletons (from Ungrateful Dead)

**Turn 19 (August Year 2):**
- Grim studies Tactics (TACT 1)
- Glum studies TELE 2 (hits 90xp)
- Ghost: FIRE 2 (90xp)
- Darkness: FORC 2 (90), FIRE 1 (60)
- Sagger Mord: starts PATT 1 (working toward full mage unlock)
- Masked (5210): New leader mage, buys with $739, studies TACT 1 immediately
- Glum teleports from Lipodou to Honvimo in turn 20's processing
- Guards (4477, 2 wood elves) at Tifufirth — another combat unit forming

**Turn 20 (September Year 2):**
- Fort at Honvimo confirmed — enables mage study above level 2
- Ghost in Infidel ship with Sagger Mord (being carried)
- 2nd Contubernium (6522, 10 drow elves) formed at underworld Quabrook
- Darkness (1263): FIRE 2 complete, FORC 2 — now a full fire mage
- Woodlot (6516, 10 wood elves) formed at Tifufirth studying Lumberjack
- Guards (3976): 22 wood elves taxing $1100
- Total faction silver in world: ~$1.24M
- Grim: OBSE 2, FORC 2, PATT 2, SPIR 2, GATE 2, FIRE 2, FARS 2, TELE 2, TACT 1, COMB 3

---

### Strengths & Weaknesses

**Strengths:**

1. **Exceptional intelligence gathering:** The combination of Grim's random gate jumping (turns 1-8) and Glum's systematic Farsight scanning (turns 8-20) gives Distant Drummer extraordinary information about the world map. By turn 20 they have a detailed understanding of surface and underworld regions across a large area.

2. **Magic faction priority:** Starting with Magic 1 and immediately upgrading to Magic 4 allowed 5 mages from turn 3 onward. This is a powerful multiplier — 4 leaders studying magic in parallel.

3. **Early tax engine:** The Guards (1264) unit taxing $550/turn from the home region in turn 3 is the financial backbone. All mage salaries come from this unit via SHARE. This was established immediately with the first formed gnome unit.

4. **Systematic mage specialization:** Each mage has a clear role: Grim = gate/teleport/tactical, Glum = farsight/gate/teleport, Ghost = artifact/enchant/illusion, Sagger Mord = necromancy/skeletons, Masked pair = observation+stealth. This prevents overlap and maximizes skill coverage.

5. **Underworld scouting via cavalry:** Using a single ice dwarf rider with a withdrawn horse (turns 6-15) to explore the underworld for ~10 turns before committing tax forces is efficient — low cost, high information.

6. **Fort construction at Honvimo:** Completing a Fort by turn 19 unlocks mage study above level 2 at a resource-rich mountain location. This positions the faction for significant power growth in turns 21+.

7. **Navy as logistics platform:** The Longship "Infidel" serves as both scout transport and unit ferry, moving forces across oceans to establish the Honvimo and Tifufirth taxing positions.

8. **Times rewards:** Consistent $200/turn from Times articles — small but reliable.

**Weaknesses:**

1. **Extremely slow territorial expansion:** After 20 turns, only 5 regions are controlled (3 surface + 2 underworld). Maximum faction limit is 10. With 5 regions at turn 20, expansion is well below capacity. The faction left major income on the table.

2. **No city captures:** The faction observed cities (Mowdorf, Plongculling, Onthead, Peonbai, Pli'atin, etc.) but made no attempt to capture any. City guards have 80-120 leaders + swords. Without a serious combat force, the faction cannot contest these high-value targets.

3. **Assassination vulnerability:** Darkness (1259) was assassinated turn 7 because mages stayed in the open in the same region as other factions. The mages have no protection (they use AVOID and BEHIND but no actual defenders around them). The stealth/observation pair (Masked 1262/1263) exists partly as counters to this threat but they have been ineffective at catching thieves.

4. **Stealth theft attempts yield nothing:** Masked (1263) consistently steals 0 silver in turns 12-15 from various visiting units. This wastes the unit's potential — either the targets are broke or immune.

5. **Necromancy is underutilized:** Sagger Mord has SUSK 2, NECR 2 by turn 20 but skeletons just sit as cargo (on Ungrateful Dead units). No combat deployments, no dungeon assaults. The skeletons could be deployed to clear monster lairs for treasure.

6. **No trade activity:** The faction ignores all trade routes despite having multiple towns within reach. Mowdorf wants fish/grain; Plongculling wants axes/spinning wheels; Peonbai wants axes/javelins. The Smiths unit could produce trade goods for significant profit.

7. **Combat army building starts very late:** Only in turns 18-20 does the faction begin acquiring drow elf combat units. After 20 turns, the faction has maybe 20-30 combat-trained soldiers — insufficient to threaten any fortified position.

8. **Fort provides only 1-2 mage study above level 2:** Grim and Glum (or Ghost and Sagger Mord) need to be at the Fort to study skills beyond level 2. With multiple mages needing this, time allocation becomes a bottleneck.

---

## Section 2: AI Agent Strategy (Based on This Playstyle)

### What the AI Would Keep

1. **Magic 4 faction type with immediate FACTION order change** — the upgrade from Magic 1 to Magic 4 is essential and should happen in turn 1 orders. Having 5 mages from the start is a huge multiplier.

2. **Random gate jumping for world scouting (turns 1-8):** The CAST GATE_LORE RANDOM on the primary mage each turn is excellent strategy. It reveals the world map, finds resources, identifies competition, and builds gate lore XP. Keep this pattern.

3. **SHARE-based financing via tax guard units:** The Guard unit with GUARD + AUTOTAX + SHARE feeding salaries to mages is elegant and scalable. Every new region gets a guard unit immediately.

4. **Systematic mage specialization:** Grim-type (gate/teleport/tactical), Observer, Stealth, Necromancer, Artifact/Enchant tracks all have high value and should be pursued in parallel.

5. **Underworld scouting via a mounted explorer:** A single cavalry unit exploring the underworld for 10-15 turns before committing resources is efficient. The ice dwarf + horse combination provides good mobility.

6. **Longship for logistics:** Building a Longship in turn 2 from withdrawn wood enables coastal expansion that land movement cannot match. The AI should continue this early shipbuilding.

7. **Fort construction at a resource-rich mountain:** The Honvimo mountain (30 iron, 14 stone naturally) is an excellent fort site — enables mage high-level study AND produces iron for equipment. Commit to fort construction early.

8. **Drow elves for underworld military:** Buying drow elves (combat 5 capable, cheap at $40) in underworld regions is good late-game military buildup.

### What the AI Would Change

1. **Accelerate territorial expansion (turns 1-5 priority):** The faction waits until turn 8 to establish Honvimo (3 regions) and turn 15-17 for Tifufirth/Quabrook. The AI should push for 4-5 regions by turn 8, not turn 17. Every turn without regional income is lost revenue. Specific improvement: send a combat-capable scout to Honvimo as early as turn 4-5 rather than waiting for the Infidel to complete its 5-turn sailing journey.

2. **Do not waste assassin attempts on poor targets (turns 12-15):** Masked (1263) steals 0 silver 4 times from visiting units with no silver. This wastes action economy. Instead, the stealth unit should conduct meaningful reconnaissance (enter monster lairs, count enemy units) or be moved to high-value theft targets.

3. **Eliminate monsters and clear dungeons for loot:** By turn 8, Grim has seen multiple monster lairs (Ice Caves, Ruin, Bog, Giant's Castle). With 10+ skeletons and Grim's fire combat spell (COMB 3 + FIRE 1), some monster clearance is viable. The faction ignores this entirely. Cleared monster lairs provide silver/items and territory.

4. **Establish trade routes earlier (turns 5-10):** The Smiths unit (3 gnomes, weaponsmith) could produce crossbows/spears/axes for local town markets. Mowdorf wanted 19 longbows at $111, Plongculling wanted 8 spinning wheels at $85, Peonbai wanted 18 crossbows at $104. This is passive income the faction abandoned.

5. **Build a second ship (turns 5-8):** Sea Scouts (1265) with shipbuilding 1 should build a second Longship once the first is complete. Two ships allows parallel coastal expansion — one exploring north/east while another scouts west/south.

6. **Use the observation unit for actual threat detection:** Masked (1262) at OBSE 5 should be placed in regions being contested by other factions, not sitting idle in Lipodou. High observation spots stealthy units and provides real strategic intelligence.

7. **Fort earlier (turns 8-12 rather than 17-19):** Construction of the Fort at Honvimo was started around turn 12-13 but not completed until turn 18-19. With 7 hill dwarves at building 2, it should take about 300/7 = ~43 turns of work divided by... actually at BUIL 2, each man contributes more effectively — the faction just needed more stone from Diggers. The AI should allocate Diggers to quarrying stone from turn 10 and prioritize fort completion by turn 14-15.

8. **Give skeletons work (combat deployment against monsters/towns):** By turn 15, Sagger Mord has SUSK 2 producing 4 skeletons/turn. With 10+ decaying but being refreshed, assembling an attacking force of 20+ skeletons is achievable. The AI should target undefended monster lairs or small creature groups for cleared resources and territory.

9. **Recruit more gnomes for more tax regions:** The faction buys gnomes only in turns 1-3 to establish initial tax guards. After that, gnome purchasing stops. But there are 10+ regions within sailing range with unclaimed territory. Each new gnome guard costs $30-40 and returns $50-200/turn depending on region size. This is highly profitable.

### Recommended Opening (Turns 1–5)

**Turn 1 (Nexus):**
- FACTION MAGIC 4 MARTIAL 1
- CLAIM maximum silver
- Form unit Grim: COMBAT FIRE, AVOID, BEHIND, CAST GATE_LORE RANDOM, STUDY SPIR (or PATT)
- Form 6 mage leaders (FORC study track for most), 2 gnome scout/guard units, 1 gnome miner, 1 gnome ship crew
- Budget: ~800 silver per leader mage, 400 for guards (11 gnomes), 120 for miners (3), 40 for scouts
- Note: start immediately with `DECLARE DEFAULT UNFRIENDLY`

**Turn 2 (home tundra):**
- Grim: CAST GATE RANDOM, STUDY PATT
- Primary mage Glum: TEACH FORC to 2-3 other mages, STUDY FORC
- Sea Scouts (10 gnomes): WITHDRAW 10 WOOD, BUILD LONGSHIP
- Miners (3 gnomes): PRODUCE IRON
- Guard (11 gnomes): GUARD 1, AUTOTAX 1, BEHIND 0, SHARE 1
- New scouts: BUY 2+ gnomes from local market, deploy S to next region
- Assign study: Pattern, Spirit, Gate, Force tracks to specific mages

**Turn 3:**
- Grim: CAST GATE RANDOM (from wherever he landed), STUDY GATE or PATT
- Sea Scouts: Build second Longship OR ENTER/SAIL first ship for scouting
- Second scout with 1 gnome: move to next adjacent unclaimed region, GUARD, AUTOTAX
- Mages: accelerate teaching — Sagger Mord TEACH SPIR to 2 mages
- Introduce stealth/observation mages to their study tracks

**Turn 4:**
- Begin moving combat-capable guard (11 gnomes, COMB 1) overland OR ship toward nearest mountain with iron
- Grim returns home via specific gate jump (CAST GATE GATE [home gate number])
- Miners produce iron for weaponsmith
- New weapon smithing: produce picks for miners, swords for mages

**Turn 5:**
- Primary ship heads to resource mountain region (Honvimo equivalent)
- Deploy 3+ gnome guard units from the ship when arriving
- Continue mage study: target FORC 2 and SPIR 2 on two mages by turn 6
- Start Artifact Lore on one mage (Ghost-equivalent) once FORC 1 + PATT 1 + SPIR 1 prerequisites are met

### Mid-Game Plan (Turns 6–15)

**Economic priorities:**
- Establish 6-7 taxing regions by turn 12 (not 5 as the original faction achieved)
- Target 3 surface + 3 underworld regions for diversity
- Ensure each region has a guard unit with enough troops to tax (COMB skill helps)
- Total tax income should reach $3,000+/turn by turn 12

**Magic priorities:**
- Grim: Gate 2 → Farsight 2 → Teleportation 2 (full mobility by turn 11)
- Glum: Gate 2 → Farsight 2 (scouting coverage) by turn 10
- Ghost: Artifact 2 → Enchant Swords (mithril swords for all mages by turn 13) → Illusion 2
- Sagger Mord: Necromancy 2 → SUSK 2 by turn 12 → begin Pattern/Force 2 for full mage status
- Observation/Stealth mages: max by turn 13 → pivot to riding or fire magic

**Military priorities:**
- Build Fort at mountain region by turn 13 (not 19)
- Assemble skeleton force: 15-20 skeletons available for dungeon clearing by turn 12
- Deploy skeleton + fire mage combo against monster lairs for loot
- Begin drow elf military in underworld from turn 11 (not 18)
- Target 1 city for seizure by turn 15-18

**Infrastructure:**
- Build 2nd ship by turn 8 for second front
- Build Castle at home region (46,84 or equivalent) if stone available by turn 15

### Adaptations for Dynamic Conditions

**If another faction occupies target regions:**
- Use Farsight and Observation to map their force composition before committing
- Default to avoiding contested regions for the first 15 turns — the tax base needs protection
- If threatened at home, recall Grim via teleportation — his FIRE combat spell + skeletons is a credible deterrent against small raiders

**If assassinated (like the Darkness incident):**
- Keep mages in BEHIND with combat-capable gnome guards in FRONT
- Deploy Masked (observation 5) in the same region as key mages to detect stealthy units
- Accept that one assassination may happen — have a replacement leader ready to study

**If underworld blocked by monsters:**
- Do not force through powerful monsters (trolls, dragons seen in turn 8 scout)
- Route around blocked paths — the underworld has many corridors
- Use skeletons to clear specific low-level obstacles (goblin hoards are clearable)

**If silver income is insufficient:**
- Prioritize ENTERTAIN over WORK for silver income units
- Exploit town markets: identify WANTED items and produce/buy them elsewhere
- Consider withdrawing iron or wood from the bank if critical deficit

**If a strong enemy expands toward key regions:**
- Establish a Fort as deterrent — even an incomplete fort signals commitment
- Form combat-ready unit with bought weapons (mithril swords from Ghost)
- Negotiate via Times if a diplomatic solution preserves income

**If magic caps are insufficient:**
- Magic 4 allows 5 mages total — carefully track who counts as a mage
- Plan mage deaths and replacements (recruitment of new leaders costs $700-800)
- Consider switching one mage to high combat (COMB 5 via a non-leader race) for physical power
