# Report Format Reference

## JSON Report Top-Level Keys

| Key | Type | Description |
|-----|------|-------------|
| `name` | string | Faction name |
| `number` | integer | Faction number |
| `engine` | object | `version`, `ruleset`, `ruleset_version`, `json_report_version` |
| `administrative` | object | `email`, `password`, `password_unset`, `show_unit_attitudes`, `times_sent`, optional `inactivity_deletion_turns`, `quit` |
| `date` | object | `month` (string), `year` (integer) |
| `type` | object | Faction type points: `martial`, `war`, `trade`, `magic` (conditional) |
| `status` | object | Faction limits: `regions`, `mages`, `apprentices`, `quartermasters`, `tacticians`, `activity`, `tax_regions`, `trade_regions` — each `{ current, allowed }` |
| `statistics` | array | Treasury/ranking per item type (conditional) |
| `errors` | array | Error messages with optional unit reference |
| `battles` | array | Battle reports (conditional) |
| `events` | array | Turn events with category, message, optional unit/region |
| `attitudes` | object | `default` + arrays for each attitude level |
| `unclaimed_silver` | integer | Faction treasury |
| `skill_reports` | array | New skill descriptions |
| `item_reports` | array | New item descriptions |
| `object_reports` | array | New structure type descriptions |
| `regions` | array | All visible regions with units and structures |

---

## Text Report Section Order

1. Treasury (statistics) — commented with `;` prefix
2. Report header: `Atlantis Report For:` / `FactionName (Number) (Type Points)` / `Month, Year N`
3. Engine version
4. Administrative messages (Times, password, inactivity, quit)
5. Faction Status: `Category: current (allowed)`
6. Errors during turn: `UnitName (Number): ErrorMessage`
7. Battles during turn (pre-formatted text)
8. Events during turn: `UnitName (Number): Message`
9. Skill reports: `skillname [TAG] level: description`
10. Item reports: item description paragraphs
11. Object reports: `ObjectType: description`
12. Declared Attitudes (default X): per-level faction lists
13. Unclaimed silver: N
14. Regions (with units and structures)

---

## Region Format

### Text
```
terrain (x,y) in Province, N peasants (race), $tax.
------------------------------------------------------------
  Wages: $rate (Max: $max).
  Wanted: items or none.
  For Sale: items or none.
  Entertainment available: $N.
  Products: items.

Exits:
  Direction : terrain (x,y) in Province.

There is a Gate here (Gate N of T).
```

Underworld: `terrain (x,y,label) in Province`

Weather: `The weather was X last month; it will be Y next month.`

### JSON Region Object
Key fields: `terrain`, `coordinates` (`x`, `y`, `z`, `label`), `province`, `settlement` (`name`, `size`), `population` (`amount`, `race`), `tax`, `wages` (`amount`, `max`), `markets` (`wanted`, `for_sale`), `entertainment`, `products`, `exits` (array of `direction` + `region`), `gate` (`number`, `open`, `total`), `weather` (`current`, `next`), `present` (boolean), `units`, `structures`.

---

## Unit Format

### Text
```
* UnitName (Number), FactionName (FactionNumber), flags, items. Weight: N.
  Capacity: fly/ride/walk/swim. Skills: list. Combat spell: name [TAG].
  Can Study: list; Description.
```

Prefix symbols: `*` own, `=` ally, `:` friendly, `-` neutral, `%` unfriendly, `!` hostile

Flag display order: `on guard`, `avoiding`, `behind`, `revealing unit/faction`, `holding`, `taxing`, `receiving no aid`, `sharing`, `consuming unit's/faction's food`, `won't cross water`, `TYPE battle spoils`

### JSON Unit Object
Own units include: `name`, `number`, `own_unit: true`, `faction`, `flags`, `items`, `weight`, `capacity`, `skills` (`known` + `can_study`), `combat_spell`, `readied`, `visited`, `orders`, optional `description`.

Foreign units include: `name`, `number`, `attitude`, conditional `faction`, partial `flags`, partial `items`.

### Flags Detail
| Flag | Type | Values |
|------|------|--------|
| `guard` | boolean | on guard status |
| `avoid` | boolean | avoiding combat |
| `behind` | boolean | rear ranks |
| `reveal` | string | `"unit"` or `"faction"` |
| `holding` | boolean | won't follow allies |
| `taxing` | boolean | autotax |
| `no_aid` | boolean | refuses healing |
| `sharing` | boolean | shares for maintenance |
| `consume` | string | `"unit"` or `"faction"` |
| `no_cross_water` | boolean | won't cross water |
| `spoils` | string | `"all"`, `"weightless"`, `"flying"`, `"walking"`, `"riding"`, `"sailing"`, `"swimming"` |

### Skills
Known: `{ name, tag, level, skill_days, study_rate }` (study_rate only with REQUIRED_EXPERIENCE)
Can study: `{ name, tag }`

### Items in Units
`{ name, plural, tag, amount }` + optional `unfinished`, `needs`, `illusion`

---

## Structure Format

### Text — Building
```
+ StructureName [Number] : TypeName, needs N, about to decay, engraved with Runes of Warding.
```

### Text — Fleet
```
+ FleetName [Number] : ShipType; N% damaged; Load: cur/cap; Sailors: cur/req; MaxSpeed: N; Sail directions: dirs.
```

### JSON Structure Object
Buildings: `name`, `number`, `type`, `units`, optional `incomplete`, `inner_location`, `warding_runes`, `closed`, `decaying`, `needs_maintenance`, `sacrifice`, `grantskill`, `description`.

Fleets: above plus `fleet: true`, `ships`, `load`, `capacity`, `sailors`, `fleet_size`, `max_speed`, `damage_percent`, `sail_directions`.

---

## Battle Report

JSON: `{ type: "battle"|"assassination", report: [lines] }`

Text sections: location header, Attackers listing, Defenders listing, Round-by-round results, Round statistics, final outcome, Total Casualties, Damaged units.

---

## Event Categories

| Category | Description |
|----------|-------------|
| `buy` | Market purchases |
| `build` | Construction |
| `cast` | Spell casting on regions |
| `claim` | Silver from treasury |
| `combat` | Combat events |
| `combat_preparation` | Ready weapons/armor |
| `decay` | Item decay |
| `destroy` | Structure destruction |
| `drown` | Units drowning |
| `escape` | Monster escape |
| `evict` | Evictions |
| `find` | Faction finding |
| `forget` | Skill forgetting |
| `gameover` | Game end |
| `give` | Item transfers |
| `gm_gift` | GM gifts |
| `guarding` | Entry denial |
| `idle` | Idle notice |
| `join` | Fleet join failures |
| `maintenance` | Maintenance consumption/borrowing |
| `movement` | Unit movement |
| `practice` | Skill practice gains |
| `produce` | Item production |
| `quest` | Quest completion |
| `rename` | Renaming |
| `reward` | Times rewards |
| `sail` | Fleet sailing |
| `sell` | Market sales |
| `spell` | Spell casting (summon, enchant, etc.) |
| `study` | Skill study |
| `tax` | Tax/pillage collection |
| `teach` | Teaching |
| `theft` | Stealing/prevention |
| `withdraw` | Item withdrawal |
| `work` | Working for wages |
| `annihilate` | World annihilation |

---

## Orders Template

Included at end of report. Three formats:

**Short**: `unit NUMBER` + existing orders only.

**Long**: Region headers (`*** terrain (x,y) in Province ***`) + commented unit descriptions + orders.

**Map**: ASCII hex map with terrain symbols + economy data alongside region info.

Template always wraps with:
```
#atlantis FACTION_NUMBER "PASSWORD"
...
#end
```

### Map Terrain Fills
ocean: `~ ~`, plain: blank, forest: `^ ^`, mountain: `/\/\`, swamp: `v v`, jungle: `@ @`, desert: `. .`, tundra: `' '`
