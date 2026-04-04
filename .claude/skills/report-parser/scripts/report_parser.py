#!/usr/bin/env python3
"""
Atlantis PBEM text report parser.

Parses text-format turn reports into structured JSON data.
Usage: python report_parser.py <report-file>
"""

import json
import re
import sys
from typing import Any, Dict, List, Optional, Tuple


class ReportParser:
    def __init__(self):
        self.lines: List[str] = []
        self.pos: int = 0

    def parse(self, content: str) -> Dict[str, Any]:
        self.lines = content.split('\n')
        self.pos = 0

        report: Dict[str, Any] = {
            'name': '',
            'number': 0,
            'date': {'month': '', 'year': 0},
            'statistics': [],
            'errors': [],
            'battles': [],
            'events': [],
            'skill_reports': [],
            'item_reports': [],
            'object_reports': [],
            'regions': [],
        }

        while self.pos < len(self.lines):
            line = self.lines[self.pos]

            if line.startswith(';'):
                self._parse_statistics(report)
                continue

            if line.startswith('Atlantis Report For:'):
                self.pos += 1
                self._parse_report_header(report)
                continue

            if line.startswith('Atlantis Engine Version:'):
                self._parse_engine_version(report, line)
                self.pos += 1
                continue

            if line.startswith('NewOrigins, Version:'):
                if 'engine' not in report:
                    report['engine'] = {'version': '', 'ruleset': '', 'ruleset_version': ''}
                report['engine']['ruleset'] = 'NewOrigins'
                report['engine']['ruleset_version'] = line.replace('NewOrigins, Version: ', '').strip()
                self.pos += 1
                continue

            if line == 'Faction Status:':
                self.pos += 1
                self._parse_faction_status(report)
                continue

            if line == 'Errors during turn:':
                self.pos += 1
                self._parse_errors(report)
                continue

            if line == 'Battles during turn:':
                self.pos += 1
                self._parse_battles(report)
                continue

            if line == 'Events during turn:':
                self.pos += 1
                self._parse_events(report)
                continue

            if line == 'Skill reports:':
                self.pos += 1
                self._parse_skill_reports(report)
                continue

            if line == 'Item reports:':
                self.pos += 1
                self._parse_item_reports(report)
                continue

            if line == 'Object reports:':
                self.pos += 1
                self._parse_object_reports(report)
                continue

            if line.startswith('Declared Attitudes ('):
                self._parse_attitudes(report, line)
                continue

            if line.startswith('Unclaimed silver:'):
                m = re.match(r'Unclaimed silver:\s*(\d+)', line)
                if m:
                    report['unclaimed_silver'] = int(m.group(1))
                self.pos += 1
                continue

            if line.startswith('Orders Template'):
                break

            if self._is_region_header(line):
                self._parse_region(report)
                continue

            self.pos += 1

        return report

    # -----------------------------------------------------------------------
    # Statistics (;Treasury section at top)
    # -----------------------------------------------------------------------
    def _parse_statistics(self, report: Dict[str, Any]) -> None:
        while self.pos < len(self.lines) and self.lines[self.pos].startswith(';'):
            line = self.lines[self.pos][1:].strip()
            m = re.match(r'^(.+?)\s{2,}(\d+)\s+(\d+)\s+(\d+)\s*$', line)
            if m:
                report['statistics'].append({
                    'item_name': m.group(1).strip(),
                    'rank': int(m.group(2)),
                    'max': int(m.group(3)),
                    'total': int(m.group(4)),
                })
            self.pos += 1

    # -----------------------------------------------------------------------
    # Report header: faction name, number, type, date
    # -----------------------------------------------------------------------
    def _parse_report_header(self, report: Dict[str, Any]) -> None:
        if self.pos >= len(self.lines):
            return
        faction_line = self.lines[self.pos]
        m = re.match(r'^(.+?)\s+\((\d+)\)\s*(.*)$', faction_line)
        if m:
            report['name'] = m.group(1)
            report['number'] = int(m.group(2))

            type_str = m.group(3)
            if type_str:
                type_map = {
                    'Martial': 'martial',
                    'War': 'war',
                    'Trade': 'trade',
                    'Magic': 'magic',
                }
                type_match = re.search(r'\(([^)]+)\)', type_str)
                if type_match:
                    report['type'] = {}
                    parts = type_match.group(1).split(',')
                    for part in parts:
                        pm = re.match(r'\s*(\w+)\s+(\d+)', part.strip())
                        if pm and pm.group(1) in type_map:
                            report['type'][type_map[pm.group(1)]] = int(pm.group(2))
        self.pos += 1

        # Date line: "December, Year 2"
        if self.pos < len(self.lines):
            date_line = self.lines[self.pos]
            dm = re.match(r'^(\w+),\s*Year\s+(\d+)', date_line)
            if dm:
                report['date'] = {'month': dm.group(1), 'year': int(dm.group(2))}
            self.pos += 1

    # -----------------------------------------------------------------------
    # Engine version
    # -----------------------------------------------------------------------
    def _parse_engine_version(self, report: Dict[str, Any], line: str) -> None:
        if 'engine' not in report:
            report['engine'] = {'version': '', 'ruleset': '', 'ruleset_version': ''}
        m = re.match(r'Atlantis Engine Version:\s*(.+)', line)
        if m:
            report['engine']['version'] = m.group(1).strip()

    # -----------------------------------------------------------------------
    # Faction Status
    # -----------------------------------------------------------------------
    def _parse_faction_status(self, report: Dict[str, Any]) -> None:
        report['status'] = {}
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if line.strip() == '':
                self.pos += 1
                break
            m = re.match(r'^(\w+):\s*(\d+)\s*\((\d+)\)', line)
            if m:
                key = m.group(1).lower()
                entry: Dict[str, Any] = {
                    'current': int(m.group(2)),
                    'allowed': int(m.group(3)),
                }
                if key == 'apprentices':
                    entry['name'] = 'Apprentice'
                report['status'][key] = entry
            self.pos += 1

    # -----------------------------------------------------------------------
    # Errors
    # -----------------------------------------------------------------------
    def _parse_errors(self, report: Dict[str, Any]) -> None:
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if line.strip() == '':
                self.pos += 1
                break

            full_line = self._read_multi_line()
            unit_match = re.match(r'^(.+?)\s+\((\d+)\):\s+(.+)$', full_line)
            if unit_match:
                report['errors'].append({
                    'message': unit_match.group(3),
                    'unit': {
                        'name': unit_match.group(1),
                        'number': int(unit_match.group(2)),
                    },
                })
            else:
                report['errors'].append({'message': full_line})

    # -----------------------------------------------------------------------
    # Events
    # -----------------------------------------------------------------------
    def _parse_events(self, report: Dict[str, Any]) -> None:
        while self.pos < len(self.lines):
            line = self.lines[self.pos]

            if line.strip() == '':
                self.pos += 1
                break

            if self._is_section_header(line):
                break

            full_line = self._read_multi_line()
            unit_match = re.match(r'^(.+?)\s+\((\d+)\):\s+(.+)$', full_line)

            event: Dict[str, Any] = {'message': ''}

            if unit_match:
                event['unit'] = {
                    'name': unit_match.group(1),
                    'number': int(unit_match.group(2)),
                }
                event['message'] = unit_match.group(3)
            else:
                event['message'] = full_line

            event['category'] = self._categorize_event(event['message'])
            report['events'].append(event)

    def _categorize_event(self, message: str) -> str:
        msg = message.lower()
        if 'times reward' in msg:
            return 'reward'
        if 'combat spell set' in msg:
            return 'combat_preparation'
        if 'forbids entry' in msg:
            return 'guarding'
        if 'gets' in msg and 'practice' in msg:
            return 'practice'
        if re.match(r'^takes\s', msg):
            return 'take'
        if re.match(r'^receives\s', msg):
            return 'give'
        if re.match(r'^gives\s', msg):
            return 'give'
        if 'collects $' in msg or 'pillages' in msg:
            return 'tax'
        if re.match(r'^creates?\s', msg):
            return 'spell'
        if 'enchants' in msg:
            return 'spell'
        if re.match(r'^casts?\s', msg):
            return 'spell'
        if re.match(r'^buys?\s', msg):
            return 'buy'
        if re.match(r'^sells?\s', msg):
            return 'sell'
        if any(w in msg for w in ('walks', 'rides', 'flies', 'swims')):
            if ' from ' in msg:
                return 'movement'
        if any(w in msg for w in ('forbidden entry', 'advance:', 'insufficient movement', 'discovers that')):
            return 'movement'
        if re.match(r'^enters\s', msg):
            return 'movement'
        if 'jumps through a gate' in msg or 'gate' in msg:
            if 'jumps through' in msg:
                return 'spell'
        if 'teaches' in msg:
            return 'teach'
        if ('helps' in msg and 'construction' in msg) or \
           'completes construction' in msg or 'performs construction' in msg:
            return 'build'
        if re.match(r'^earns?\s.*entertaining', msg):
            return 'entertain'
        if re.match(r'^earns?\s.*working', msg):
            return 'work'
        if re.match(r'^studies\s', msg) or 'completes study' in msg:
            return 'study'
        if re.match(r'^produces?\s', msg):
            return 'produce'
        if 'transports' in msg:
            return 'transport'
        if 'shares' in msg:
            return 'share'
        if 'borrows' in msg and 'maintenance' in msg:
            return 'maintenance'
        if 'consumes' in msg and 'maintenance' in msg:
            return 'maintenance'
        if 'claims' in msg and 'maintenance' in msg:
            return 'maintenance'
        if 'starve' in msg:
            return 'maintenance'
        if 'sails from' in msg:
            return 'sail'
        if 'claims' in msg:
            return 'claim'
        if 'forgets' in msg:
            return 'forget'
        if 'drowned' in msg or 'drowning' in msg:
            return 'drown'
        if 'destroyed' in msg:
            return 'destroy'
        if 'quest' in msg:
            return 'quest'
        if 'renamed' in msg:
            return 'rename'
        if 'withdrew' in msg or 'withdraws' in msg:
            return 'withdraw'
        if 'idle' in msg:
            return 'idle'
        if 'is caught attempting to steal' in msg or 'has stolen' in msg:
            return 'theft'
        return 'combat'

    # -----------------------------------------------------------------------
    # Battles
    # -----------------------------------------------------------------------
    def _parse_battles(self, report: Dict[str, Any]) -> None:
        while self.pos < len(self.lines):
            line = self.lines[self.pos]

            if self._is_section_header(line) and not line.strip().startswith('- '):
                break

            if (' attacks ' in line or
                    ' is assassinated in ' in line or
                    ' attempts to assassinate ' in line):
                battle = self._parse_single_battle()
                report['battles'].append(battle)
                continue

            self.pos += 1

    def _is_battle_start(self, line: str) -> bool:
        return (not line.startswith(' ') and
                (' attacks ' in line or
                 ' is assassinated in ' in line or
                 ' attempts to assassinate ' in line))

    def _parse_single_battle(self) -> Dict[str, Any]:
        report_lines: List[str] = []
        is_assassination = ('is assassinated' in self.lines[self.pos] or
                            'attempts to assassinate' in self.lines[self.pos])

        blank_count = 0
        first_line = True
        while self.pos < len(self.lines):
            line = self.lines[self.pos]

            # After the first line, check if a new section or battle starts
            # without a blank line separator
            if not first_line and line.strip() != '':
                if self._is_section_header(line) or self._is_battle_start(line):
                    break

            if line.strip() == '':
                blank_count += 1
                if blank_count >= 2:
                    self.pos += 1
                    break
                if self.pos + 1 < len(self.lines):
                    next_line = self.lines[self.pos + 1]
                    if (self._is_section_header(next_line) or
                            self._is_region_header(next_line) or
                            self._is_battle_start(next_line)):
                        self.pos += 1
                        break
                report_lines.append('')
                self.pos += 1
            else:
                blank_count = 0
                first_line = False
                full_line = self._read_multi_line()
                report_lines.append(full_line)

        # Trim trailing empty lines
        while report_lines and report_lines[-1] == '':
            report_lines.pop()

        return {
            'type': 'assassination' if is_assassination else 'battle',
            'report': report_lines,
        }

    # -----------------------------------------------------------------------
    # Skill Reports
    # -----------------------------------------------------------------------
    def _parse_skill_reports(self, report: Dict[str, Any]) -> None:
        while self.pos < len(self.lines):
            line = self.lines[self.pos]

            if self._is_section_header(line):
                break

            if line.strip() == '':
                self.pos += 1
                continue

            m = re.match(r'^(\S+(?:\s+\S+)*?)\s+\[(\w+)\]\s+(\d+):\s*(.*)$', line)
            if m:
                self.pos += 1
                description = m.group(4)
                while self.pos < len(self.lines):
                    cont_line = self.lines[self.pos]
                    if cont_line.startswith('  ') and cont_line.strip() != '':
                        description += ' ' + cont_line.strip()
                        self.pos += 1
                    else:
                        break

                report['skill_reports'].append({
                    'name': m.group(1),
                    'tag': m.group(2),
                    'level': int(m.group(3)),
                    'description': description.strip(),
                })
            else:
                self.pos += 1

    # -----------------------------------------------------------------------
    # Item Reports
    # -----------------------------------------------------------------------
    def _parse_item_reports(self, report: Dict[str, Any]) -> None:
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if self._is_section_header(line):
                break
            if line.strip() == '':
                self.pos += 1
                continue

            text = ''
            while self.pos < len(self.lines):
                l = self.lines[self.pos]
                if l.strip() == '':
                    break
                if self._is_section_header(l):
                    break
                if text:
                    text += ' '
                text += l.strip() if l.startswith('  ') else l
                self.pos += 1

            if text:
                tag_match = re.search(r'\[(\w+)\]', text)
                report['item_reports'].append({
                    'tag': tag_match.group(1) if tag_match else '',
                    'description': text,
                })

    # -----------------------------------------------------------------------
    # Object Reports
    # -----------------------------------------------------------------------
    def _parse_object_reports(self, report: Dict[str, Any]) -> None:
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if self._is_section_header(line):
                break
            if line.strip() == '':
                self.pos += 1
                continue

            m = re.match(r'^(\S+(?:\s+\S+)*):\s+(.*)$', line)
            if m:
                self.pos += 1
                description = m.group(2)
                while self.pos < len(self.lines):
                    l = self.lines[self.pos]
                    if not l.startswith('  ') or l.strip() == '':
                        break
                    description += ' ' + l.strip()
                    self.pos += 1
                report['object_reports'].append({
                    'name': m.group(1),
                    'description': description.strip(),
                })
            else:
                self.pos += 1

    # -----------------------------------------------------------------------
    # Attitudes
    # -----------------------------------------------------------------------
    def _parse_attitudes(self, report: Dict[str, Any], header_line: str) -> None:
        def_match = re.search(r'Declared Attitudes \(default (\w+)\)', header_line)
        default_attitude = def_match.group(1).lower() if def_match else 'neutral'

        report['attitudes'] = {
            'default': default_attitude,
            'hostile': [],
            'unfriendly': [],
            'neutral': [],
            'friendly': [],
            'ally': [],
        }

        self.pos += 1

        attitude_keys = ['hostile', 'unfriendly', 'neutral', 'friendly', 'ally']

        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if line.strip() == '':
                self.pos += 1
                break

            matched = False
            for key in attitude_keys:
                prefix = key[0].upper() + key[1:]
                if line.startswith(prefix + ' :'):
                    full_line = self._read_multi_line()
                    rest = full_line[full_line.index(':') + 1:].strip()
                    if rest != 'none.':
                        report['attitudes'][key] = self._parse_faction_list(rest)
                    matched = True
                    break

            if not matched:
                self.pos += 1

    def _parse_faction_list(self, text: str) -> List[Dict[str, Any]]:
        result = []
        for m in re.finditer(r'([^,(]+?)\s+\((\d+)\)', text):
            result.append({
                'name': m.group(1).strip(),
                'number': int(m.group(2)),
            })
        return result

    # -----------------------------------------------------------------------
    # Region Parsing
    # -----------------------------------------------------------------------
    def _is_region_header(self, line: str) -> bool:
        return bool(re.match(r'^\w[\w\s]*\(\d+,\d+', line))

    def _parse_region(self, report: Dict[str, Any]) -> None:
        header_line = self._read_multi_line()
        region = self._parse_region_header(header_line)
        if not region:
            return

        # Skip separator line "----..."
        if self.pos < len(self.lines) and self.lines[self.pos].startswith('---'):
            self.pos += 1

        # Parse region body
        self._parse_region_body(region)

        # Parse exits
        if self.pos < len(self.lines) and self.lines[self.pos].strip() == 'Exits:':
            self.pos += 1
            self._parse_exits(region)

        # Parse gate
        if self.pos < len(self.lines) and self.lines[self.pos].startswith('There is a')  and 'Gate' in self.lines[self.pos]:
            self._parse_gate(region)

        # Parse units and structures
        self._parse_units_and_structures(region)

        report['regions'].append(region)

    def _parse_region_header(self, line: str) -> Optional[Dict[str, Any]]:
        coord_match = re.match(r'^(.+?)\s+\((\d+),(\d+)(?:,([^)]+))?\)\s+in\s+(.+)', line)
        if not coord_match:
            return None

        terrain = coord_match.group(1).strip()
        x = int(coord_match.group(2))
        y = int(coord_match.group(3))
        label = coord_match.group(4) or 'surface'
        rest = coord_match.group(5)

        if label == 'underworld':
            z = 2
        elif label == 'underdeep':
            z = 3
        elif label != 'surface':
            z = 2
        else:
            z = 1

        region: Dict[str, Any] = {
            'terrain': terrain,
            'coordinates': {'x': x, 'y': y, 'z': z, 'label': label},
            'province': '',
            'present': True,
            'units': [],
            'structures': [],
            'exits': [],
        }

        rest_clean = rest.rstrip('.')
        parts = [p.strip() for p in rest_clean.split(',')]

        region['province'] = parts[0]

        for i in range(1, len(parts)):
            part = parts[i]

            settlement_match = re.match(r'contains\s+(.+?)\s+\[(\w+)\]', part)
            if settlement_match:
                region['settlement'] = {
                    'name': settlement_match.group(1),
                    'size': settlement_match.group(2),
                }
                continue

            pop_match = re.match(r'(\d+)\s+peasants?\s+\((.+?)\)', part)
            if pop_match:
                region['population'] = {
                    'amount': int(pop_match.group(1)),
                    'race': pop_match.group(2),
                }
                continue

            tax_match = re.search(r'\$(\d+)', part)
            if tax_match:
                region['tax'] = int(tax_match.group(1))
                continue

        return region

    def _parse_region_body(self, region: Dict[str, Any]) -> None:
        while self.pos < len(self.lines):
            line = self.lines[self.pos]

            if not line.startswith('  ') or line.strip() == '':
                if line.strip() == '':
                    self.pos += 1
                break

            trimmed = line.strip()

            # Wages
            wage_match = re.match(r'Wages:\s+\$([\d.]+)\s+\(Max:\s+\$(\d+)\)', trimmed)
            if wage_match:
                region['wages'] = {
                    'amount': float(wage_match.group(1)),
                    'max': int(wage_match.group(2)),
                }
                self.pos += 1
                continue

            # Wanted / For Sale
            if trimmed.startswith('Wanted:'):
                if 'markets' not in region:
                    region['markets'] = {'wanted': [], 'for_sale': []}
                if 'none' not in trimmed:
                    full_line = self._read_multi_line_indented()
                    region['markets']['wanted'] = self._parse_market_items(
                        full_line.replace('Wanted:', '').strip()
                    )
                else:
                    self.pos += 1
                continue

            if trimmed.startswith('For Sale:'):
                if 'markets' not in region:
                    region['markets'] = {'wanted': [], 'for_sale': []}
                if 'none' not in trimmed:
                    full_line = self._read_multi_line_indented()
                    region['markets']['for_sale'] = self._parse_market_items(
                        full_line.replace('For Sale:', '').strip()
                    )
                else:
                    self.pos += 1
                continue

            # Entertainment
            ent_match = re.match(r'Entertainment available:\s+\$(\d+)', trimmed)
            if ent_match:
                region['entertainment'] = int(ent_match.group(1))
                self.pos += 1
                continue

            # Products
            if trimmed.startswith('Products:'):
                if 'none' not in trimmed:
                    full_line = self._read_multi_line_indented()
                    region['products'] = self._parse_products(
                        full_line.replace('Products:', '').strip()
                    )
                else:
                    self.pos += 1
                continue

            self.pos += 1

    def _read_multi_line_indented(self) -> str:
        result = self.lines[self.pos].strip()
        self.pos += 1
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if line.startswith('    ') and line.strip() != '':
                result += ' ' + line.strip()
                self.pos += 1
            else:
                break
        return result

    def _parse_market_items(self, text: str) -> List[Dict[str, Any]]:
        items = []
        clean_text = text.rstrip('.')
        for m in re.finditer(r'(?:(\d+)\s+)?(.+?)\s+\[(\w+)\]\s+at\s+\$(\d+)', clean_text):
            amount = int(m.group(1)) if m.group(1) else 1
            name_str = m.group(2)
            items.append({
                'amount': amount,
                'name': name_str,
                'tag': m.group(3),
                'price': int(m.group(4)),
            })
        return items

    def _parse_products(self, text: str) -> List[Dict[str, Any]]:
        products = []
        clean_text = text.rstrip('.')
        for m in re.finditer(r'(\d+)\s+(.+?)\s+\[(\w+)\]', clean_text):
            amount = int(m.group(1))
            name_str = m.group(2)
            products.append({
                'amount': amount,
                'name': name_str,
                'tag': m.group(3),
            })
        return products

    # -----------------------------------------------------------------------
    # Exits
    # -----------------------------------------------------------------------
    def _parse_exits(self, region: Dict[str, Any]) -> None:
        while self.pos < len(self.lines):
            line = self.lines[self.pos]

            if not line.startswith('  ') or line.strip() == '':
                if line.strip() == '':
                    self.pos += 1
                break

            full_line = self._read_multi_line_indented()
            trimmed = full_line.strip()

            m = re.match(
                r'^(North|Northeast|Southeast|South|Southwest|Northwest)\s*:\s*(.+)',
                trimmed
            )
            if m:
                direction = m.group(1)
                exit_text = m.group(2).rstrip('.')
                exit_region = self._parse_exit_region(exit_text)
                if exit_region:
                    region['exits'].append({'direction': direction, 'region': exit_region})

    def _parse_exit_region(self, text: str) -> Optional[Dict[str, Any]]:
        m = re.match(r'^(.+?)\s+\((\d+),(\d+)(?:,([^)]+))?\)\s+in\s+(.+)', text)
        if not m:
            return None

        terrain = m.group(1).strip()
        x = int(m.group(2))
        y = int(m.group(3))
        label = m.group(4) or 'surface'
        rest = m.group(5)

        if label == 'underworld':
            z = 2
        elif label == 'underdeep':
            z = 3
        elif label != 'surface':
            z = 2
        else:
            z = 1

        exit_region: Dict[str, Any] = {
            'terrain': terrain,
            'coordinates': {'x': x, 'y': y, 'z': z, 'label': label},
            'province': '',
        }

        parts = [p.strip() for p in rest.split(',')]
        exit_region['province'] = parts[0]

        for i in range(1, len(parts)):
            part = parts[i]
            settlement_match = re.match(r'contains\s+(.+?)\s+\[(\w+)\]', part)
            if settlement_match:
                exit_region['settlement'] = {
                    'name': settlement_match.group(1),
                    'size': settlement_match.group(2),
                }

        return exit_region

    # -----------------------------------------------------------------------
    # Gate
    # -----------------------------------------------------------------------
    def _parse_gate(self, region: Dict[str, Any]) -> None:
        line = self.lines[self.pos]
        if 'closed Gate' in line:
            region['gate'] = {'number': 0, 'open': False}
        else:
            m = re.search(r'Gate\s+(\d+)(?:\s+of\s+(\d+))?', line)
            if m:
                region['gate'] = {
                    'number': int(m.group(1)),
                    'open': True,
                }
                if m.group(2):
                    region['gate']['total'] = int(m.group(2))
        self.pos += 1
        if self.pos < len(self.lines) and self.lines[self.pos].strip() == '':
            self.pos += 1

    # -----------------------------------------------------------------------
    # Units and Structures
    # -----------------------------------------------------------------------
    def _parse_units_and_structures(self, region: Dict[str, Any]) -> None:
        current_structure: Optional[Dict[str, Any]] = None

        while self.pos < len(self.lines):
            line = self.lines[self.pos]

            if line.strip() == '':
                self.pos += 1
                if self.pos < len(self.lines) and self.lines[self.pos].strip() == '':
                    self.pos += 1
                    break
                continue

            if self._is_region_header(line):
                break
            if self._is_section_header(line):
                break

            # Structure line
            if line.startswith('+ '):
                full_struct_line = self._read_structure_line()
                current_structure = self._parse_structure(full_struct_line)
                region['structures'].append(current_structure)
                continue

            # Unit line (not indented)
            unit_prefix = self._get_unit_prefix(line)
            indented_unit_prefix = self._get_unit_prefix(line.strip()) if line.startswith('  ') else None

            if unit_prefix:
                unit = self._parse_unit(line, False)
                if unit:
                    region['units'].append(unit)
                continue

            if indented_unit_prefix and current_structure is not None:
                unit = self._parse_unit(line.strip(), True)
                if unit:
                    if current_structure['units'] is None:
                        current_structure['units'] = []
                    current_structure['units'].append(unit)
                continue

            self.pos += 1

    def _get_unit_prefix(self, line: str) -> Optional[str]:
        for prefix in ('* ', '- ', '= ', ': ', '% ', '! '):
            if line.startswith(prefix):
                return prefix[0]
        return None

    def _parse_structure(self, line: str) -> Dict[str, Any]:
        structure: Dict[str, Any] = {
            'name': '',
            'number': 0,
            'type': '',
            'units': None,
        }

        m = re.match(r'^\+\s+(.+?)\s+\[(\d+)\]\s*:\s*(.+)', line)
        if not m:
            return structure

        structure['name'] = m.group(1)
        structure['number'] = int(m.group(2))

        rest = m.group(3).rstrip('.')

        is_fleet = (
            structure['name'] == 'Ship' or
            structure['name'] == 'Fleet' or
            rest.startswith('Fleet') or
            self._is_fleet_rest(rest)
        )

        if is_fleet:
            self._parse_fleet_structure(structure, rest)
        else:
            self._parse_building_structure(structure, rest)

        return structure

    def _is_fleet_rest(self, rest: str) -> bool:
        semi_idx = rest.find(';')
        if semi_idx < 0:
            return False
        after_semi = rest[semi_idx + 1:].lstrip()
        return bool(re.match(r'^\d+%\s*damaged', after_semi))

    def _parse_building_structure(self, structure: Dict[str, Any], rest: str) -> None:
        main_part = rest
        semi_idx = rest.find(';')
        if semi_idx >= 0:
            desc_text = rest[semi_idx + 1:].strip()
            if desc_text:
                structure['description'] = desc_text
            main_part = rest[:semi_idx].strip()

        parts = [p.strip() for p in main_part.split(',')]
        structure['type'] = parts[0]

        for i in range(1, len(parts)):
            part = parts[i]
            needs_match = re.search(r'needs\s+(\d+)', part)
            if needs_match:
                structure['incomplete'] = int(needs_match.group(1))
                continue
            if part == 'contains an inner location':
                structure['inner_location'] = True
                continue
            if part == 'needs maintenance':
                structure['needs_maintenance'] = True
                continue
            if part == 'closed to player units':
                structure['closed'] = True
                continue

    def _parse_fleet_structure(self, structure: Dict[str, Any], rest: str) -> None:
        semi_parts = [p.strip() for p in rest.split(';')]
        structure['fleet'] = True

        # First part: ship type(s)
        type_part = semi_parts[0]
        comma_parts = [p.strip() for p in type_part.split(',')]

        if len(comma_parts) > 1 and not re.match(r'^\d', comma_parts[0]):
            structure['type'] = comma_parts[0]
            structure['ships'] = []
            for i in range(1, len(comma_parts)):
                ship_match = re.match(r'^(\d+)\s+(.+)$', comma_parts[i])
                if ship_match:
                    amount = int(ship_match.group(1))
                    name = ship_match.group(2)
                    structure['ships'].append({
                        'name': name,
                        'number': amount,
                    })
        else:
            structure['type'] = 'Fleet'
            structure['ships'] = [{
                'name': comma_parts[0],
                'number': 1,
            }]

        # Parse semicolon-separated fields
        for i in range(1, len(semi_parts)):
            part = semi_parts[i]

            dmg_match = re.search(r'(\d+)%\s*damaged', part)
            if dmg_match:
                structure['damage_percent'] = int(dmg_match.group(1))
                continue

            load_match = re.search(r'Load:\s*(\d+)/(\d+)', part)
            if load_match:
                structure['load'] = int(load_match.group(1))
                structure['capacity'] = int(load_match.group(2))
                continue

            sailor_match = re.search(r'Sailors:\s*(\d+)/(\d+)', part)
            if sailor_match:
                structure['sailors'] = int(sailor_match.group(1))
                structure['fleet_size'] = int(sailor_match.group(2))
                continue

            speed_match = re.search(r'MaxSpeed:\s*(\d+)', part)
            if speed_match:
                structure['max_speed'] = int(speed_match.group(1))
                continue

            sail_dir_match = re.search(r'Sail directions:\s*(.+)', part)
            if sail_dir_match:
                structure['sail_directions'] = {}
                dirs = [d.strip() for d in sail_dir_match.group(1).split(',')]
                for d in dirs:
                    if d:
                        structure['sail_directions'][d] = True

    # -----------------------------------------------------------------------
    # Unit Parsing
    # -----------------------------------------------------------------------
    def _parse_unit(self, first_line: str, in_structure: bool) -> Optional[Dict[str, Any]]:
        prefix = self._get_unit_prefix(first_line)
        if not prefix:
            return None

        text_start = first_line[2:]  # skip "* " or "- " etc
        self.pos += 1
        full_text = text_start

        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            indent = 4 if in_structure else 2
            if (line.startswith(' ' * indent) and
                    line.strip() != '' and
                    not self._get_unit_prefix(line.strip()) and
                    not line.strip().startswith('+ ')):
                full_text += ' ' + line.strip()
                self.pos += 1
            else:
                break

        return self._parse_unit_text(full_text, prefix)

    def _parse_unit_text(self, text: str, prefix: str) -> Dict[str, Any]:
        is_own = prefix == '*'
        unit: Dict[str, Any] = {
            'name': '',
            'number': 0,
            'flags': {
                'guard': False,
            },
            'items': [],
        }

        if is_own:
            unit['flags']['avoid'] = False
            unit['own_unit'] = True
        else:
            attitude_map = {
                '-': 'neutral',
                '=': 'ally',
                ':': 'friendly',
                '%': 'unfriendly',
                '!': 'hostile',
            }
            unit['attitude'] = attitude_map.get(prefix, 'neutral')

        # Split description part (after last ";") from the main data
        main_text = text
        description = ''
        desc_idx = self._find_description_semicolon(text)
        if desc_idx >= 0:
            description = text[desc_idx + 1:].strip()
            main_text = text[:desc_idx]
            if description.endswith('.'):
                description = description[:-1]

        # Extract "Can Study:" section
        can_study_text = ''
        can_study_idx = main_text.find('Can Study:')
        if can_study_idx >= 0:
            can_study_text = main_text[can_study_idx + len('Can Study:'):].strip()
            main_text = main_text[:can_study_idx]
            if can_study_text.endswith('.'):
                can_study_text = can_study_text[:-1]

        # Extract "Has visited" section
        visited: Optional[List[str]] = None
        visited_marker = 'Has visited '
        for source_name in ('can_study', 'main'):
            src = can_study_text if source_name == 'can_study' else main_text
            idx = src.find(visited_marker)
            if idx >= 0:
                remaining = re.sub(r'\.\s*$', '', src[:idx]).strip()
                province_text = re.sub(r'\.\s*$', '', src[idx + len(visited_marker):]).strip()
                visited = self._parse_visited_list(province_text)
                if source_name == 'can_study':
                    can_study_text = remaining
                else:
                    main_text = remaining
                break

        # Extract "Combat spell:" section
        combat_spell_text = ''
        combat_spell_idx = main_text.find('Combat spell:')
        if combat_spell_idx >= 0:
            after_cs = main_text[combat_spell_idx + len('Combat spell:'):].strip()
            combat_spell_text = after_cs.split('.')[0]
            main_text = (
                main_text[:combat_spell_idx] +
                main_text[combat_spell_idx + len('Combat spell:') + len(combat_spell_text) + 1:]
            )

        # Extract Skills: section
        skills_text = ''
        skills_idx = main_text.find('Skills:')
        if skills_idx >= 0:
            after_skills = main_text[skills_idx + len('Skills:'):]
            end_idx = after_skills.find('.')
            if end_idx >= 0:
                skills_text = after_skills[:end_idx].strip()
                main_text = main_text[:skills_idx] + after_skills[end_idx + 1:]
            else:
                skills_text = after_skills.strip()
                main_text = main_text[:skills_idx]

        # Extract Capacity: section
        capacity_text = ''
        cap_idx = main_text.find('Capacity:')
        if cap_idx >= 0:
            after_cap = main_text[cap_idx + len('Capacity:'):]
            end_idx = after_cap.find('.')
            if end_idx >= 0:
                capacity_text = after_cap[:end_idx].strip()
                main_text = main_text[:cap_idx] + after_cap[end_idx + 1:]
            else:
                capacity_text = after_cap.strip()
                main_text = main_text[:cap_idx]

        # Extract Weight: section
        weight: Optional[int] = None
        weight_match = re.search(r'Weight:\s*(\d+)', main_text)
        if weight_match:
            weight = int(weight_match.group(1))
            main_text = re.sub(r'Weight:\s*\d+\.?\s*', '', main_text)

        # Extract readied items
        readied: List[Dict[str, str]] = []
        for pattern_str in [
            r'Ready weapon:\s+(.+?)\s+\[(\w+)\]',
            r'Ready armor:\s+(.+?)\s+\[(\w+)\]',
            r'Ready item:\s+(.+?)\s+\[(\w+)\]',
        ]:
            for rm in re.finditer(pattern_str, main_text):
                readied.append({'name': rm.group(1), 'tag': rm.group(2)})
            main_text = re.sub(pattern_str, '', main_text)

        # Clean up mainText
        main_text = re.sub(r'\.\s*$', '', main_text).strip()

        # Parse name, faction, flags, items from mainText
        self._parse_unit_main_section(unit, main_text)

        # Apply extracted data
        if weight is not None:
            unit['weight'] = weight

        if capacity_text:
            cap_parts = capacity_text.split('/')
            if len(cap_parts) == 4:
                unit['capacity'] = {
                    'flying': int(cap_parts[0]) if cap_parts[0].strip() else 0,
                    'riding': int(cap_parts[1]) if cap_parts[1].strip() else 0,
                    'walking': int(cap_parts[2]) if cap_parts[2].strip() else 0,
                    'swimming': int(cap_parts[3]) if cap_parts[3].strip() else 0,
                }

        if skills_text and skills_text != 'none':
            if 'skills' not in unit:
                unit['skills'] = {'known': []}
            unit['skills']['known'] = self._parse_skills_list(skills_text)
        elif is_own:
            if 'skills' not in unit:
                unit['skills'] = {'known': []}

        if combat_spell_text:
            cs_match = re.match(r'(.+?)\s+\[(\w+)\]', combat_spell_text)
            if cs_match:
                unit['combat_spell'] = {'name': cs_match.group(1), 'tag': cs_match.group(2)}

        if can_study_text:
            if 'skills' not in unit:
                unit['skills'] = {'known': []}
            unit['skills']['can_study'] = self._parse_can_study(can_study_text)

        if readied:
            unit['readied'] = readied

        if description:
            unit['description'] = description

        if is_own:
            if 'orders' not in unit:
                unit['orders'] = []
            unit['visited'] = visited if visited is not None else []

        return unit

    def _find_description_semicolon(self, text: str) -> int:
        bracket_depth = 0
        last_semicolon = -1
        for i, ch in enumerate(text):
            if ch == '[':
                bracket_depth += 1
            elif ch == ']':
                bracket_depth -= 1
            elif ch == ';' and bracket_depth == 0:
                last_semicolon = i
        return last_semicolon

    def _parse_unit_main_section(self, unit: Dict[str, Any], text: str) -> None:
        name_match = re.match(r'^(.+?)\s+\((\d+)\)', text)
        if not name_match:
            return

        unit['name'] = name_match.group(1)
        unit['number'] = int(name_match.group(2))

        rest = text[len(name_match.group(0)):]
        parts = self._split_comma_parts(rest)

        faction_parsed = False

        for part in parts:
            trimmed = part.strip()
            if not trimmed:
                continue

            # Flags
            if trimmed == 'on guard':
                unit['flags']['guard'] = True
                continue
            if trimmed == 'avoiding':
                unit['flags']['avoid'] = True
                continue
            if trimmed == 'behind':
                unit['flags']['behind'] = True
                continue
            if trimmed == 'revealing unit':
                unit['flags']['reveal'] = 'unit'
                continue
            if trimmed == 'revealing faction':
                unit['flags']['reveal'] = 'faction'
                continue
            if trimmed == 'holding':
                unit['flags']['holding'] = True
                continue
            if trimmed == 'taxing':
                unit['flags']['taxing'] = True
                continue
            if trimmed == 'receiving no aid':
                unit['flags']['no_aid'] = True
                continue
            if trimmed == 'sharing':
                unit['flags']['sharing'] = True
                continue
            if trimmed == "consuming unit's food":
                unit['flags']['consume'] = 'unit'
                continue
            if trimmed == "consuming faction's food":
                unit['flags']['consume'] = 'faction'
                continue
            if trimmed == "won't cross water":
                unit['flags']['no_cross_water'] = True
                continue
            if trimmed.endswith('battle spoils'):
                spoils_match = re.match(r'^(\w+)\s+battle spoils$', trimmed)
                if spoils_match:
                    unit['flags']['spoils'] = spoils_match.group(1)
                continue

            # Faction
            if not faction_parsed:
                faction_match = re.match(r'^(.+?)\s+\((\d+)\)$', trimmed)
                if faction_match:
                    unit['faction'] = {
                        'name': faction_match.group(1),
                        'number': int(faction_match.group(2)),
                    }
                    faction_parsed = True
                    continue

            # Items
            self._parse_item_part(unit, trimmed)

    def _split_comma_parts(self, text: str) -> List[str]:
        parts = []
        current = ''
        bracket_depth = 0

        for ch in text:
            if ch == '[':
                bracket_depth += 1
            elif ch == ']':
                bracket_depth -= 1
            elif ch == ',' and bracket_depth == 0:
                parts.append(current)
                current = ''
                continue
            current += ch

        if current.strip():
            parts.append(current)
        return parts

    def _parse_item_part(self, unit: Dict[str, Any], text: str) -> None:
        trimmed = text.strip().rstrip('.')
        if not trimmed:
            return

        multi_match = re.match(r'^(\d+)\s+(.+?)\s+\[(\w+)\]$', trimmed)
        if multi_match:
            amount = int(multi_match.group(1))
            name_str = multi_match.group(2)
            unit['items'].append({
                'amount': amount,
                'name': name_str,
                'tag': multi_match.group(3),
            })
            return

        single_match = re.match(r'^(.+?)\s+\[(\w+)\]$', trimmed)
        if single_match:
            name_str = single_match.group(1)
            unit['items'].append({
                'amount': 1,
                'name': name_str,
                'tag': single_match.group(2),
            })

    def _parse_skills_list(self, text: str) -> List[Dict[str, Any]]:
        skills = []
        for m in re.finditer(r'(.+?)\s+\[(\w+)\]\s+(\d+)\s+\((\d+)(?:\+\d+)?\)', text):
            skills.append({
                'name': m.group(1).strip().lstrip(',').strip(),
                'tag': m.group(2),
                'level': int(m.group(3)),
                'skill_days': int(m.group(4)),
            })
        return skills

    def _parse_visited_list(self, text: str) -> List[str]:
        return [p.strip() for p in text.replace(' and ', ',').split(',') if p.strip()]

    def _parse_can_study(self, text: str) -> List[Dict[str, str]]:
        skills = []
        for m in re.finditer(r'(.+?)\s+\[(\w+)\]', text):
            skills.append({
                'name': m.group(1).strip().lstrip(',').strip(),
                'tag': m.group(2),
            })
        return skills

    # -----------------------------------------------------------------------
    # Multi-line reading utilities
    # -----------------------------------------------------------------------
    def _read_multi_line(self) -> str:
        result = self.lines[self.pos]
        self.pos += 1

        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if line.startswith('  ') and line.strip() != '':
                result += ' ' + line.strip()
                self.pos += 1
            else:
                break

        return result

    def _read_structure_line(self) -> str:
        result = self.lines[self.pos]
        self.pos += 1

        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if not line.startswith('  ') or line.strip() == '':
                break
            trimmed = line.strip()
            if self._get_unit_prefix(trimmed) or trimmed.startswith('+ '):
                break
            result += ' ' + trimmed
            self.pos += 1

        return result

    def _is_section_header(self, line: str) -> bool:
        return (
            line.startswith('Atlantis Report For:') or
            line.startswith('Faction Status:') or
            line == 'Errors during turn:' or
            line == 'Battles during turn:' or
            line == 'Events during turn:' or
            line == 'Skill reports:' or
            line == 'Item reports:' or
            line == 'Object reports:' or
            line.startswith('Declared Attitudes (') or
            line.startswith('Unclaimed silver:') or
            line.startswith('Orders Template')
        )


def parse_report_file(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as f:
        content = f.read()
    parser = ReportParser()
    return parser.parse(content)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python report_parser.py <report-file>', file=sys.stderr)
        sys.exit(1)

    result = parse_report_file(sys.argv[1])
    print(json.dumps(result, indent=2))
