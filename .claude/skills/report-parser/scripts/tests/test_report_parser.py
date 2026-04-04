"""Tests for the Atlantis text report parser."""

import sys
import os

# Add parent directory to path so we can import the parser
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from report_parser import ReportParser


def make_parser():
    return ReportParser()


# ============================================================================
# Statistics
# ============================================================================

class TestStatistics:
    def test_parse_statistics(self):
        report = make_parser().parse(
            ";Treasury:\n"
            ";\n"
            ";Item                                      Rank  Max        Total\n"
            ";=====================================================================\n"
            ";3 leaders [LEAD]                          40    21         385\n"
            ";46 hill dwarves [HDWA]                    7     225        1194\n"
        )
        assert len(report['statistics']) == 2
        assert report['statistics'][0] == {
            'item_name': '3 leaders [LEAD]',
            'rank': 40,
            'max': 21,
            'total': 385,
        }
        assert report['statistics'][1] == {
            'item_name': '46 hill dwarves [HDWA]',
            'rank': 7,
            'max': 225,
            'total': 1194,
        }

    def test_empty_statistics(self):
        report = make_parser().parse("")
        assert report['statistics'] == []


# ============================================================================
# Report Header
# ============================================================================

class TestReportHeader:
    def test_parse_faction_name_and_number(self):
        report = make_parser().parse(
            "Atlantis Report For:\n"
            "SuperBober (14) (Martial 2, Magic 2)\n"
            "April, Year 2\n"
        )
        assert report['name'] == 'SuperBober'
        assert report['number'] == 14

    def test_parse_faction_type(self):
        report = make_parser().parse(
            "Atlantis Report For:\n"
            "SuperBober (14) (Martial 2, Magic 2)\n"
            "April, Year 2\n"
        )
        assert report['type'] == {'martial': 2, 'magic': 2}

    def test_parse_date(self):
        report = make_parser().parse(
            "Atlantis Report For:\n"
            "SuperBober (14) (Martial 2, Magic 2)\n"
            "April, Year 2\n"
        )
        assert report['date'] == {'month': 'April', 'year': 2}

    def test_parse_engine_version(self):
        report = make_parser().parse(
            "Atlantis Report For:\n"
            "Test (1)\n"
            "January, Year 1\n"
            "\n"
            "Atlantis Engine Version: 5.2.5 (beta)\n"
            "NewOrigins, Version: 3.0.0 (beta)\n"
        )
        assert report['engine'] == {
            'version': '5.2.5 (beta)',
            'ruleset': 'NewOrigins',
            'ruleset_version': '3.0.0 (beta)',
        }


# ============================================================================
# Faction Status
# ============================================================================

class TestFactionStatus:
    def test_parse_faction_status(self):
        report = make_parser().parse(
            "Faction Status:\n"
            "Regions: 8 (25)\n"
            "Quartermasters: 0 (5)\n"
            "Mages: 3 (3)\n"
            "Apprentices: 0 (5)\n"
            "\n"
        )
        assert report['status']['regions'] == {'current': 8, 'allowed': 25}
        assert report['status']['mages'] == {'current': 3, 'allowed': 3}
        assert report['status']['apprentices'] == {'current': 0, 'allowed': 5, 'name': 'Apprentice'}


# ============================================================================
# Errors
# ============================================================================

class TestErrors:
    def test_parse_errors_with_unit(self):
        report = make_parser().parse(
            "Errors during turn:\n"
            "scout (2354): ATTACK: Non-existent unit.\n"
            "\n"
        )
        assert len(report['errors']) == 1
        assert report['errors'][0]['message'] == 'ATTACK: Non-existent unit.'
        assert report['errors'][0]['unit'] == {'name': 'scout', 'number': 2354}

    def test_parse_errors_without_unit(self):
        report = make_parser().parse(
            "Errors during turn:\n"
            "Some global error message.\n"
            "\n"
        )
        assert len(report['errors']) == 1
        assert report['errors'][0]['message'] == 'Some global error message.'


# ============================================================================
# Events
# ============================================================================

class TestEvents:
    def test_parse_events_with_unit(self):
        report = make_parser().parse(
            "Events during turn:\n"
            "Unit (868): Casts Earth Lore, raising 24 silver.\n"
            "\n"
        )
        assert len(report['events']) == 1
        assert report['events'][0]['unit'] == {'name': 'Unit', 'number': 868}
        assert report['events'][0]['message'] == 'Casts Earth Lore, raising 24 silver.'
        assert report['events'][0]['category'] == 'spell'

    def test_parse_events_without_unit(self):
        report = make_parser().parse(
            "Events during turn:\n"
            "Times reward of 200 silver.\n"
            "\n"
        )
        assert report['events'][0]['message'] == 'Times reward of 200 silver.'
        assert report['events'][0]['category'] == 'reward'

    def test_multiline_event(self):
        report = make_parser().parse(
            "Events during turn:\n"
            "Unit (1850): Walks from volcano (6,50) in Inhead to mountain (7,51) in\n"
            "  Inhead.\n"
            "\n"
        )
        assert len(report['events']) == 1
        assert report['events'][0]['message'] == 'Walks from volcano (6,50) in Inhead to mountain (7,51) in Inhead.'


class TestEventCategories:
    def test_tax(self):
        p = make_parser()
        assert p._categorize_event('Collects $50 in taxes') == 'tax'

    def test_movement(self):
        p = make_parser()
        assert p._categorize_event('Walks from mountain (5,51) to mountain (5,53)') == 'movement'

    def test_study(self):
        p = make_parser()
        assert p._categorize_event('Studies combat at a cost of 100 silver [SILV].') == 'study'

    def test_produce(self):
        p = make_parser()
        assert p._categorize_event('Produces 5 livestock [LIVE] in mountain.') == 'produce'

    def test_give(self):
        p = make_parser()
        assert p._categorize_event('Gives 100 silver [SILV] to Unit (123).') == 'give'

    def test_take(self):
        p = make_parser()
        assert p._categorize_event('Takes 10 livestock [LIVE] from Unit (456).') == 'take'

    def test_buy(self):
        p = make_parser()
        assert p._categorize_event('Buys 2 humans [HUMN] at $39 each.') == 'buy'

    def test_sell(self):
        p = make_parser()
        assert p._categorize_event('Sells 2 livestock [LIVE] at $18 each.') == 'sell'

    def test_maintenance(self):
        p = make_parser()
        assert p._categorize_event('Consumes 10 silver [SILV] for maintenance.') == 'maintenance'
        assert p._categorize_event('Borrows 50 silver [SILV] from Unit (123) for maintenance.') == 'maintenance'

    def test_build(self):
        p = make_parser()
        assert p._categorize_event('Completes construction of Building [1]') == 'build'

    def test_guarding(self):
        p = make_parser()
        assert p._categorize_event('Forbids entry to Scout (3146), Lunaria (66).') == 'guarding'

    def test_theft(self):
        p = make_parser()
        assert p._categorize_event('Is caught attempting to steal from Unit (5812) in Inhead.') == 'theft'
        assert p._categorize_event('Has stolen 200 silver.') == 'theft'

    def test_work(self):
        p = make_parser()
        assert p._categorize_event('Earns 158 silver working in mountain.') == 'work'

    def test_entertain(self):
        p = make_parser()
        assert p._categorize_event('Earns 30 silver entertaining in plain.') == 'entertain'

    def test_idle(self):
        p = make_parser()
        assert p._categorize_event('Is idle.') == 'idle'


# ============================================================================
# Battles
# ============================================================================

class TestBattles:
    def test_parse_attack_battle(self):
        report = make_parser().parse(
            "Battles during turn:\n"
            "Unit (100) attacks Unit (200) in plain (1,2) in Province!\n"
            "\n"
            "Attackers:\n"
            "Unit (100), human [HUMN].\n"
            "\n"
            "Defenders:\n"
            "Unit (200), orc [ORC].\n"
            "\n"
            "Total Casualties:\n"
            "Unit (200) loses 1.\n"
            "Unit (100) loses 0.\n"
            "\n"
            "\n"
        )
        assert len(report['battles']) == 1
        assert report['battles'][0]['type'] == 'battle'
        assert report['battles'][0]['report'][0] == 'Unit (100) attacks Unit (200) in plain (1,2) in Province!'

    def test_parse_assassination_battle(self):
        report = make_parser().parse(
            "Battles during turn:\n"
            "Unit (100) is assassinated in plain (1,2) in Province!\n"
            "\n"
            "\n"
        )
        assert len(report['battles']) == 1
        assert report['battles'][0]['type'] == 'assassination'

    def test_parse_assassination_attempt(self):
        report = make_parser().parse(
            "Battles during turn:\n"
            "Unit (408) attempts to assassinate Unit (5632) in plain (50,62) in\n"
            "  Province!\n"
            "\n"
            "Attackers:\n"
            "Unit (408), behind, human [HUMN].\n"
            "\n"
            "Unit (408) loses 0.\n"
            "\n"
            "\n"
        )
        assert len(report['battles']) == 1
        assert report['battles'][0]['type'] == 'assassination'

    def test_multiple_battles(self):
        report = make_parser().parse(
            "Battles during turn:\n"
            "Unit (1) attacks Unit (2) in plain (1,2) in P!\n"
            "\n"
            "Total Casualties:\n"
            "Unit (2) loses 1.\n"
            "\n"
            "Unit (3) attacks Unit (4) in plain (3,4) in Q!\n"
            "\n"
            "Total Casualties:\n"
            "Unit (4) loses 2.\n"
            "\n"
            "\n"
        )
        assert len(report['battles']) == 2


# ============================================================================
# Skill Reports
# ============================================================================

class TestSkillReports:
    def test_parse_skill_report(self):
        report = make_parser().parse(
            "Skill reports:\n"
            "\n"
            "riding [RIDI] 1: A unit with this skill may ride mounts.\n"
            "\n"
            "Item reports:\n"
        )
        assert len(report['skill_reports']) == 1
        assert report['skill_reports'][0] == {
            'name': 'riding',
            'tag': 'RIDI',
            'level': 1,
            'description': 'A unit with this skill may ride mounts.',
        }

    def test_multiline_skill_report(self):
        report = make_parser().parse(
            "Skill reports:\n"
            "\n"
            "riding [RIDI] 1: A unit with this skill, if possessing a mount, may\n"
            "  gain a bonus in combat.\n"
            "\n"
        )
        assert report['skill_reports'][0]['description'] == (
            'A unit with this skill, if possessing a mount, may gain a bonus in combat.'
        )


# ============================================================================
# Item Reports
# ============================================================================

class TestItemReports:
    def test_parse_item_report(self):
        report = make_parser().parse(
            "Item reports:\n"
            "\n"
            "wood [WOOD], weight 5, costs 75 silver to withdraw. This item is a\n"
            "  trade resource.\n"
            "\n"
        )
        assert len(report['item_reports']) == 1
        assert report['item_reports'][0]['tag'] == 'WOOD'
        assert 'trade resource' in report['item_reports'][0]['description']


# ============================================================================
# Object Reports
# ============================================================================

class TestObjectReports:
    def test_parse_object_report(self):
        report = make_parser().parse(
            "Object reports:\n"
            "\n"
            "Tower: This is a tall tower.\n"
            "  It provides defense.\n"
            "\n"
        )
        assert len(report['object_reports']) == 1
        assert report['object_reports'][0]['name'] == 'Tower'
        assert report['object_reports'][0]['description'] == 'This is a tall tower. It provides defense.'


# ============================================================================
# Attitudes
# ============================================================================

class TestAttitudes:
    def test_parse_attitudes(self):
        report = make_parser().parse(
            "Declared Attitudes (default Unfriendly):\n"
            "Hostile : none.\n"
            "Unfriendly : Creatures (2).\n"
            "Neutral : none.\n"
            "Friendly : none.\n"
            "Ally : none.\n"
            "\n"
        )
        assert report['attitudes']['default'] == 'unfriendly'
        assert report['attitudes']['hostile'] == []
        assert report['attitudes']['unfriendly'] == [{'name': 'Creatures', 'number': 2}]
        assert report['attitudes']['ally'] == []

    def test_parse_multiple_factions(self):
        report = make_parser().parse(
            "Declared Attitudes (default Neutral):\n"
            "Hostile : none.\n"
            "Unfriendly : none.\n"
            "Neutral : none.\n"
            "Friendly : Foo (1), Bar (2).\n"
            "Ally : Baz (3).\n"
            "\n"
        )
        assert len(report['attitudes']['friendly']) == 2
        assert report['attitudes']['friendly'][0] == {'name': 'Foo', 'number': 1}
        assert report['attitudes']['friendly'][1] == {'name': 'Bar', 'number': 2}
        assert report['attitudes']['ally'] == [{'name': 'Baz', 'number': 3}]


# ============================================================================
# Unclaimed Silver
# ============================================================================

class TestUnclaimedSilver:
    def test_parse_unclaimed_silver(self):
        report = make_parser().parse("Unclaimed silver: 1149.\n")
        assert report['unclaimed_silver'] == 1149


# ============================================================================
# Region Header Parsing
# ============================================================================

class TestRegionHeader:
    def test_basic_region(self):
        report = make_parser().parse(
            "desert (5,49) in Wholtecla, 1358 peasants (gnolls), $461.\n"
            "------------------------------------------------------------\n"
            "\n"
        )
        assert len(report['regions']) == 1
        r = report['regions'][0]
        assert r['terrain'] == 'desert'
        assert r['coordinates'] == {'x': 5, 'y': 49, 'z': 1, 'label': 'surface'}
        assert r['province'] == 'Wholtecla'
        assert r['population'] == {'amount': 1358, 'race': 'gnolls'}
        assert r['tax'] == 461

    def test_region_with_settlement(self):
        report = make_parser().parse(
            "mountain (5,53) in Inhead, contains Sehe [town], 4946 peasants (hill\n"
            "  dwarves), $3165.\n"
            "------------------------------------------------------------\n"
            "\n"
        )
        r = report['regions'][0]
        assert r['settlement'] == {'name': 'Sehe', 'size': 'town'}
        assert r['population'] == {'amount': 4946, 'race': 'hill dwarves'}

    def test_region_with_label(self):
        report = make_parser().parse(
            "cavern (10,20,underworld) in DeepPlace, 100 peasants (dwarves), $50.\n"
            "------------------------------------------------------------\n"
            "\n"
        )
        r = report['regions'][0]
        assert r['coordinates'] == {'x': 10, 'y': 20, 'z': 2, 'label': 'underworld'}

    def test_ocean_region_no_population(self):
        report = make_parser().parse(
            "ocean (4,48) in Atlantis Ocean.\n"
            "------------------------------------------------------------\n"
            "\n"
        )
        r = report['regions'][0]
        assert r['terrain'] == 'ocean'
        assert 'population' not in r
        assert 'tax' not in r


# ============================================================================
# Region Body
# ============================================================================

class TestRegionBody:
    def test_wages(self):
        report = make_parser().parse(
            "plain (1,1) in Test, 100 peasants (humans), $50.\n"
            "------------------------------------------------------------\n"
            "  Wages: $13.2 (Max: $484).\n"
            "\n"
        )
        r = report['regions'][0]
        assert r['wages'] == {'amount': 13.2, 'max': 484}

    def test_wanted_and_for_sale(self):
        report = make_parser().parse(
            "mountain (1,1) in Test, 100 peasants (humans), $50.\n"
            "------------------------------------------------------------\n"
            "  Wanted: 170 grain [GRAI] at $20, 160 livestock [LIVE] at $18.\n"
            "  For Sale: 52 humans [HUMN] at $39, 10 leaders [LEAD] at $694.\n"
            "\n"
        )
        r = report['regions'][0]
        assert len(r['markets']['wanted']) == 2
        assert r['markets']['wanted'][0] == {'amount': 170, 'name': 'grain', 'tag': 'GRAI', 'price': 20}
        assert len(r['markets']['for_sale']) == 2

    def test_wanted_none(self):
        report = make_parser().parse(
            "plain (1,1) in Test, 100 peasants (humans), $50.\n"
            "------------------------------------------------------------\n"
            "  Wanted: none.\n"
            "  For Sale: none.\n"
            "\n"
        )
        r = report['regions'][0]
        assert r['markets']['wanted'] == []
        assert r['markets']['for_sale'] == []

    def test_entertainment(self):
        report = make_parser().parse(
            "plain (1,1) in Test, 100 peasants (humans), $50.\n"
            "------------------------------------------------------------\n"
            "  Entertainment available: $58.\n"
            "\n"
        )
        assert report['regions'][0]['entertainment'] == 58

    def test_products(self):
        report = make_parser().parse(
            "plain (1,1) in Test, 100 peasants (humans), $50.\n"
            "------------------------------------------------------------\n"
            "  Products: 12 grain [GRAI], 19 iron [IRON], 10 stone [STON].\n"
            "\n"
        )
        r = report['regions'][0]
        assert len(r['products']) == 3
        assert r['products'][0] == {'amount': 12, 'name': 'grain', 'tag': 'GRAI'}

    def test_multiline_products(self):
        report = make_parser().parse(
            "plain (1,1) in Test, 100 peasants (humans), $50.\n"
            "------------------------------------------------------------\n"
            "  Products: 39 livestock [LIVE], 17 wood [WOOD], 27 herbs [HERB], 13\n"
            "    furs [FUR].\n"
            "\n"
        )
        assert len(report['regions'][0]['products']) == 4


# ============================================================================
# Exits
# ============================================================================

class TestExits:
    def test_parse_exits(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "  South : mountain (1,2) in Hills, contains Town [city].\n"
            "\n"
        )
        r = report['regions'][0]
        assert len(r['exits']) == 2
        assert r['exits'][0]['direction'] == 'North'
        assert r['exits'][0]['region']['terrain'] == 'ocean'
        assert r['exits'][0]['region']['coordinates'] == {'x': 1, 'y': 0, 'z': 1, 'label': 'surface'}
        assert r['exits'][1]['region']['settlement'] == {'name': 'Town', 'size': 'city'}


# ============================================================================
# Gate
# ============================================================================

class TestGate:
    def test_parse_open_gate(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "There is a Gate here (Gate 622).\n"
            "\n"
        )
        assert report['regions'][0]['gate'] == {'number': 622, 'open': True}

    def test_parse_closed_gate(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "There is a closed Gate here.\n"
            "\n"
        )
        assert report['regions'][0]['gate'] == {'number': 0, 'open': False}


# ============================================================================
# Units
# ============================================================================

class TestUnits:
    def test_own_unit_basic(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "* Militia (1253), on guard, SuperBober (14), behind, revealing\n"
            "  faction, receiving no aid, hill dwarf [HDWA], 130 silver [SILV].\n"
            "  Weight: 10. Capacity: 0/0/15/0. Skills: observation [OBSE] 1 (30),\n"
            "  combat [COMB] 2 (90).\n"
            "\n"
            "\n"
        )
        r = report['regions'][0]
        assert len(r['units']) == 1
        u = r['units'][0]
        assert u['name'] == 'Militia'
        assert u['number'] == 1253
        assert u['own_unit'] is True
        assert u['flags']['guard'] is True
        assert u['flags']['behind'] is True
        assert u['flags']['reveal'] == 'faction'
        assert u['flags']['no_aid'] is True
        assert u['faction'] == {'name': 'SuperBober', 'number': 14}
        assert len(u['items']) == 2
        assert u['items'][0] == {'amount': 1, 'name': 'hill dwarf', 'tag': 'HDWA'}
        assert u['items'][1] == {'amount': 130, 'name': 'silver', 'tag': 'SILV'}
        assert u['weight'] == 10
        assert u['capacity'] == {'flying': 0, 'riding': 0, 'walking': 15, 'swimming': 0}
        assert len(u['skills']['known']) == 2
        assert u['skills']['known'][0] == {'name': 'observation', 'tag': 'OBSE', 'level': 1, 'skill_days': 30}

    def test_alien_unit(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "- farmers (3952), Elder Tree Forests (32), avoiding, behind, 5 gnomes\n"
            "  [GNOM], 5 grain [GRAI].\n"
            "\n"
            "\n"
        )
        u = report['regions'][0]['units'][0]
        assert u['name'] == 'farmers'
        assert u['number'] == 3952
        assert u['attitude'] == 'neutral'
        assert u['faction'] == {'name': 'Elder Tree Forests', 'number': 32}
        assert u['flags']['avoid'] is True
        assert u['flags']['behind'] is True
        assert len(u['items']) == 2

    def test_unit_with_combat_spell(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "* Unit (2748), SuperBober (14), behind, revealing faction, leader\n"
            "  [LEAD], chain armor [CARM]. Weight: 11. Capacity: 0/0/15/0. Skills:\n"
            "  force [FORC] 2 (90), fire [FIRE] 1 (35). Combat spell: fire [FIRE].\n"
            "  Can Study: fire [FIRE], force shield [FSHI], energy shield [ESHI].\n"
            "\n"
            "\n"
        )
        u = report['regions'][0]['units'][0]
        assert u['combat_spell'] == {'name': 'fire', 'tag': 'FIRE'}
        assert len(u['skills']['can_study']) == 3
        assert u['skills']['can_study'][0] == {'name': 'fire', 'tag': 'FIRE'}
        assert u['skills']['can_study'][1] == {'name': 'force shield', 'tag': 'FSHI'}

    def test_unit_with_no_skills(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "* Unit (4991), SuperBober (14), revealing faction, 9 humans [HUMN].\n"
            "  Weight: 90. Capacity: 0/0/135/0. Skills: none.\n"
            "\n"
            "\n"
        )
        u = report['regions'][0]['units'][0]
        assert u['skills'] == {'known': []}

    def test_unit_flags(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "* Unit (1), Faction (1), on guard, avoiding, behind, holding, taxing,\n"
            "  sharing, receiving no aid, won't cross water, walking battle spoils,\n"
            "  consuming faction's food, revealing unit, human [HUMN].\n"
            "  Weight: 10. Capacity: 0/0/15/0. Skills: none.\n"
            "\n"
            "\n"
        )
        u = report['regions'][0]['units'][0]
        assert u['flags']['guard'] is True
        assert u['flags']['avoid'] is True
        assert u['flags']['behind'] is True
        assert u['flags']['holding'] is True
        assert u['flags']['taxing'] is True
        assert u['flags']['sharing'] is True
        assert u['flags']['no_aid'] is True
        assert u['flags']['no_cross_water'] is True
        assert u['flags']['spoils'] == 'walking'
        assert u['flags']['consume'] == 'faction'
        assert u['flags']['reveal'] == 'unit'

    def test_unit_with_description(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "* Unit (1), Faction (1), human [HUMN]. Weight: 10. Capacity:\n"
            "  0/0/15/0. Skills: none; This is my description.\n"
            "\n"
            "\n"
        )
        u = report['regions'][0]['units'][0]
        assert u['description'] == 'This is my description'

    def test_unit_multiple_items(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "* Unit (2782), on guard, SuperBober (14), revealing faction, 10 orcs\n"
            "  [ORC], 10 swords [SWOR], 10 chain armor [CARM], iron [IRON], 400\n"
            "  silver [SILV]. Weight: 125. Capacity: 0/0/150/0. Skills: combat\n"
            "  [COMB] 1 (45).\n"
            "\n"
            "\n"
        )
        u = report['regions'][0]['units'][0]
        assert len(u['items']) == 5
        assert u['items'][0] == {'amount': 10, 'name': 'orcs', 'tag': 'ORC'}
        assert u['items'][3] == {'amount': 1, 'name': 'iron', 'tag': 'IRON'}


# ============================================================================
# Structures
# ============================================================================

class TestStructures:
    def test_building_structure(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "+ Building [1] : Tower.\n"
            "\n"
            "\n"
        )
        s = report['regions'][0]['structures'][0]
        assert s['name'] == 'Building'
        assert s['number'] == 1
        assert s['type'] == 'Tower'
        assert s['units'] is None

    def test_building_with_units(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "+ Building [1] : Tower.\n"
            "  * Unit (2873), SuperBober (14), revealing faction, 5 hill dwarves\n"
            "    [HDWA], 3 stone [STON]. Weight: 230. Capacity: 0/0/75/0. Skills:\n"
            "    building [BUIL] 1 (40).\n"
            "\n"
            "\n"
        )
        s = report['regions'][0]['structures'][0]
        assert len(s['units']) == 1
        u = s['units'][0]
        assert u['name'] == 'Unit'
        assert u['number'] == 2873
        assert len(u['items']) == 2

    def test_road_structure(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "+ Building [1] : Road S.\n"
            "\n"
            "\n"
        )
        s = report['regions'][0]['structures'][0]
        assert s['type'] == 'Road S'

    def test_incomplete_building(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "+ Building [1] : Tower, needs 50.\n"
            "\n"
            "\n"
        )
        s = report['regions'][0]['structures'][0]
        assert s['type'] == 'Tower'
        assert s['incomplete'] == 50

    def test_closed_structure(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "+ Empowered Altar [1] : Empowered Altar, closed to player units.\n"
            "\n"
            "\n"
        )
        s = report['regions'][0]['structures'][0]
        assert s['closed'] is True

    def test_fleet_structure_single_ship(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "+ Ship [147] : Cog.\n"
            "\n"
            "\n"
        )
        s = report['regions'][0]['structures'][0]
        assert s['fleet'] is True
        assert s['type'] == 'Fleet'
        assert s['ships'] == [{'name': 'Cog', 'number': 1}]

    def test_fleet_structure_with_stats(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "+ Ship [156] : Raft; 0% damaged; Load: 75/450; Sailors: 0/2; MaxSpeed:\n"
            "  2.\n"
            "\n"
            "\n"
        )
        s = report['regions'][0]['structures'][0]
        assert s['fleet'] is True
        assert s['damage_percent'] == 0
        assert s['load'] == 75
        assert s['capacity'] == 450
        assert s['sailors'] == 0
        assert s['fleet_size'] == 2
        assert s['max_speed'] == 2

    def test_fleet_multi_ship(self):
        report = make_parser().parse(
            "plain (1,1) in Test.\n"
            "------------------------------------------------------------\n"
            "\n"
            "Exits:\n"
            "  North : ocean (1,0) in Sea.\n"
            "\n"
            "+ Smell of Victory [662] : Fleet, 4 Galleons, 4 Galleys.\n"
            "\n"
            "\n"
        )
        s = report['regions'][0]['structures'][0]
        assert s['fleet'] is True
        assert s['type'] == 'Fleet'
        assert len(s['ships']) == 2
        assert s['ships'][0] == {'name': 'Galleons', 'number': 4}
        assert s['ships'][1] == {'name': 'Galleys', 'number': 4}


# ============================================================================
# Multiple regions
# ============================================================================

class TestMultipleRegions:
    def test_two_regions(self):
        report = make_parser().parse(
            "desert (5,49) in Wholtecla, 1358 peasants (gnolls), $461.\n"
            "------------------------------------------------------------\n"
            "  Wages: $11.7 (Max: $212).\n"
            "  Wanted: none.\n"
            "  For Sale: 54 gnolls [GNOL] at $37.\n"
            "  Entertainment available: $26.\n"
            "  Products: 12 grain [GRAI].\n"
            "\n"
            "Exits:\n"
            "  North : ocean (5,47) in Atlantis Ocean.\n"
            "\n"
            "* Militia (1253), SuperBober (14), hill dwarf [HDWA]. Weight: 10.\n"
            "  Capacity: 0/0/15/0. Skills: none.\n"
            "\n"
            "\n"
            "mountain (7,49) in Inhead, 1178 peasants (humans), $0.\n"
            "------------------------------------------------------------\n"
            "  Wages: $9.6 (Max: $0).\n"
            "  Wanted: none.\n"
            "  For Sale: 47 humans [HUMN] at $30.\n"
            "  Entertainment available: $4.\n"
            "  Products: 20 grain [GRAI].\n"
            "\n"
            "Exits:\n"
            "  South : mountain (7,51) in Inhead.\n"
            "\n"
            "\n"
        )
        assert len(report['regions']) == 2
        assert report['regions'][0]['terrain'] == 'desert'
        assert report['regions'][1]['terrain'] == 'mountain'


# ============================================================================
# Orders Template stops parsing
# ============================================================================

class TestOrdersTemplate:
    def test_stops_at_orders_template(self):
        report = make_parser().parse(
            "Unclaimed silver: 100.\n"
            "\n"
            "Orders Template (Long Format):\n"
            ";*** Orders Template ***\n"
            "#atlantis 14 \"password\"\n"
        )
        assert report['unclaimed_silver'] == 100
        # Should not try to parse orders template content


# ============================================================================
# Full integration: a minimal complete report
# ============================================================================

class TestFullReport:
    def test_minimal_report(self):
        content = (
            ";3 leaders [LEAD]                          40    21         385\n"
            "\n"
            "Atlantis Report For:\n"
            "TestFaction (7) (Trade 3)\n"
            "June, Year 5\n"
            "\n"
            "Atlantis Engine Version: 5.2.5 (beta)\n"
            "NewOrigins, Version: 3.0.0 (beta)\n"
            "\n"
            "Faction Status:\n"
            "Regions: 2 (10)\n"
            "Mages: 1 (2)\n"
            "\n"
            "Errors during turn:\n"
            "Unit (100): MOVE: Can't move there.\n"
            "\n"
            "Events during turn:\n"
            "Times reward of 50 silver.\n"
            "Unit (100): Walks from plain (1,1) to plain (2,2).\n"
            "\n"
            "Skill reports:\n"
            "\n"
            "combat [COMB] 1: Units with combat skill fight better.\n"
            "\n"
            "Item reports:\n"
            "\n"
            "sword [SWOR], weight 1. A sharp blade.\n"
            "\n"
            "Declared Attitudes (default Neutral):\n"
            "Hostile : none.\n"
            "Unfriendly : none.\n"
            "Neutral : none.\n"
            "Friendly : Allies (5).\n"
            "Ally : none.\n"
            "\n"
            "Unclaimed silver: 500.\n"
            "\n"
            "plain (1,1) in TestProv, 200 peasants (humans), $100.\n"
            "------------------------------------------------------------\n"
            "  Wages: $10.0 (Max: $200).\n"
            "  Wanted: none.\n"
            "  For Sale: 10 humans [HUMN] at $30.\n"
            "  Entertainment available: $20.\n"
            "  Products: 5 grain [GRAI].\n"
            "\n"
            "Exits:\n"
            "  South : plain (1,2) in TestProv.\n"
            "\n"
            "* Leader (100), TestFaction (7), leader [LEAD], 50 silver [SILV].\n"
            "  Weight: 10. Capacity: 0/0/15/0. Skills: combat [COMB] 1 (30).\n"
            "\n"
            "\n"
            "Orders Template (Long Format):\n"
            "#atlantis 7\n"
        )
        report = make_parser().parse(content)

        assert report['name'] == 'TestFaction'
        assert report['number'] == 7
        assert report['type'] == {'trade': 3}
        assert report['date'] == {'month': 'June', 'year': 5}
        assert report['engine']['version'] == '5.2.5 (beta)'
        assert len(report['statistics']) == 1
        assert len(report['errors']) == 1
        assert len(report['events']) == 2
        assert len(report['skill_reports']) == 1
        assert len(report['item_reports']) == 1
        assert report['attitudes']['friendly'] == [{'name': 'Allies', 'number': 5}]
        assert report['unclaimed_silver'] == 500
        assert len(report['regions']) == 1
        assert report['regions'][0]['province'] == 'TestProv'
        assert len(report['regions'][0]['units']) == 1
