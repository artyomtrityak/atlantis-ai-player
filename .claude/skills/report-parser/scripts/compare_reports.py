#!/usr/bin/env python3
"""
Compare text-parsed reports against JSON reports for validation.

Usage: python compare_reports.py [count] [--seed=N]
"""

import json
import os
import random
import sys
from typing import Any, Dict, List, Optional, Tuple

from report_parser import parse_report_file


# ============================================================================
# Types / data structures
# ============================================================================

class ReportPair:
    def __init__(self, txt_path: str, json_path: str, label: str):
        self.txt_path = txt_path
        self.json_path = json_path
        self.label = label


class FieldResult:
    def __init__(self, field: str, match: bool, parsed: Any, expected: Any):
        self.field = field
        self.match = match
        self.parsed = parsed
        self.expected = expected


class ComparisonResult:
    def __init__(self, label: str, match_percent: int, fields: List[FieldResult],
                 parse_error: Optional[str] = None):
        self.label = label
        self.match_percent = match_percent
        self.fields = fields
        self.parse_error = parse_error


class ComparisonSummary:
    def __init__(self, results: List[ComparisonResult], average_match_percent: int,
                 total_reports: int, full_match_count: int):
        self.results = results
        self.average_match_percent = average_match_percent
        self.total_reports = total_reports
        self.full_match_count = full_match_count


# ============================================================================
# File discovery
# ============================================================================

def find_report_pairs(game_examples_dir: str) -> List[ReportPair]:
    pairs = []

    for dir_name in sorted(os.listdir(game_examples_dir)):
        dir_path = os.path.join(game_examples_dir, dir_name)
        if not os.path.isdir(dir_path):
            continue

        for file_name in sorted(os.listdir(dir_path)):
            if not file_name.startswith('report.') or file_name.endswith('.json'):
                continue
            json_path = os.path.join(dir_path, file_name + '.json')
            if os.path.exists(json_path):
                pairs.append(ReportPair(
                    txt_path=os.path.join(dir_path, file_name),
                    json_path=json_path,
                    label=f'{dir_name}/{file_name}',
                ))

    return pairs


def sample_pairs(pairs: List[ReportPair], count: int, seed: Optional[int] = None) -> List[ReportPair]:
    copy = list(pairs)
    if seed is not None:
        # Deterministic shuffle using simple LCG (matching TS behavior)
        s = seed
        for i in range(len(copy) - 1, 0, -1):
            s = (s * 1664525 + 1013904223) & 0xFFFFFFFF
            j = s % (i + 1)
            copy[i], copy[j] = copy[j], copy[i]
    else:
        random.shuffle(copy)
    return copy[:count]


# ============================================================================
# Field extraction helpers
# ============================================================================

def get(obj: Any, *keys: str) -> Any:
    cur = obj
    for k in keys:
        if cur is None or not isinstance(cur, dict):
            return None
        cur = cur.get(k)
    return cur


def length(obj: Any) -> int:
    if not isinstance(obj, list):
        return 0
    return len(obj)


def extract_fields(data: Any) -> Dict[str, Any]:
    return {
        'name': get(data, 'name'),
        'number': get(data, 'number'),
        'date_month': get(data, 'date', 'month'),
        'date_year': get(data, 'date', 'year'),
        'region_count': length(get(data, 'regions')),
        'event_count': length(get(data, 'events')),
        'error_count': length(get(data, 'errors')),
        'battle_count': length(get(data, 'battles')),
        'statistic_count': length(get(data, 'statistics')),
        'skill_report_count': length(get(data, 'skill_reports')),
        'item_report_count': length(get(data, 'item_reports')),
        'object_report_count': length(get(data, 'object_reports')),
        'unclaimed_silver': get(data, 'unclaimed_silver'),
    }


# ============================================================================
# Core comparison
# ============================================================================

def compare_fields(parsed: Dict[str, Any], expected: Dict[str, Any]) -> List[FieldResult]:
    all_keys = set(list(parsed.keys()) + list(expected.keys()))
    results = []

    for field in sorted(all_keys):
        p = parsed.get(field)
        e = expected.get(field)
        results.append(FieldResult(field=field, match=(p == e), parsed=p, expected=e))

    return results


def compare_report(pair: ReportPair) -> ComparisonResult:
    try:
        parsed = parse_report_file(pair.txt_path)
    except Exception as err:
        return ComparisonResult(
            label=pair.label,
            match_percent=0,
            fields=[],
            parse_error=str(err),
        )

    with open(pair.json_path, 'r') as f:
        expected = json.load(f)

    parsed_fields = extract_fields(parsed)
    expected_fields = extract_fields(expected)
    fields = compare_fields(parsed_fields, expected_fields)

    match_count = sum(1 for f in fields if f.match)
    match_percent = round((match_count / len(fields)) * 100) if fields else 100

    return ComparisonResult(label=pair.label, match_percent=match_percent, fields=fields)


def run_comparison(pairs: List[ReportPair]) -> ComparisonSummary:
    results = [compare_report(pair) for pair in pairs]
    total_reports = len(results)
    average_match_percent = (
        round(sum(r.match_percent for r in results) / total_reports)
        if total_reports > 0 else 0
    )
    full_match_count = sum(1 for r in results if r.match_percent == 100)
    return ComparisonSummary(
        results=results,
        average_match_percent=average_match_percent,
        total_reports=total_reports,
        full_match_count=full_match_count,
    )


# ============================================================================
# CLI formatting
# ============================================================================

def status_label(pct: int) -> str:
    if pct == 100:
        return 'MATCH'
    if pct >= 75:
        return '~ PARTIAL'
    return 'MISMATCH'


def print_result(r: ComparisonResult) -> None:
    if r.parse_error:
        print(f'\n[ERROR] {r.label}: {r.parse_error}')
        return
    print(f'\n[{status_label(r.match_percent)}] {r.label} ({r.match_percent}%)')
    for f in r.fields:
        if f.match:
            print(f'  {f.field}: OK ({json.dumps(f.parsed)})')
        else:
            print(f'  {f.field}: FAIL  parsed={json.dumps(f.parsed)}  expected={json.dumps(f.expected)}')


def print_summary(summary: ComparisonSummary) -> None:
    print(f'\n{"=" * 60}')
    print(f'Full matches: {summary.full_match_count}/{summary.total_reports}  |  '
          f'Average: {summary.average_match_percent}%')


# ============================================================================
# CLI entry point
# ============================================================================

if __name__ == '__main__':
    args = sys.argv[1:]
    count = 10
    seed = None

    for arg in args:
        if arg.startswith('--seed='):
            seed = int(arg.split('=')[1])
        elif arg.isdigit():
            count = int(arg)

    game_examples = os.path.join(os.getcwd(), 'game-examples')
    all_pairs = find_report_pairs(game_examples)
    sample = sample_pairs(all_pairs, count, seed)

    print(f'Comparing {len(sample)} reports ({len(all_pairs)} total available)...\n')
    summary = run_comparison(sample)
    for r in summary.results:
        print_result(r)
    print_summary(summary)
