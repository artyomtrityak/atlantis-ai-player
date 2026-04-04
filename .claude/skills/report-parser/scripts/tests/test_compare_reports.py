"""Tests for the compare_reports module."""

import os
import sys
import tempfile
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from compare_reports import (
    ReportPair,
    FieldResult,
    ComparisonResult,
    ComparisonSummary,
    find_report_pairs,
    sample_pairs,
    get,
    length,
    extract_fields,
    compare_fields,
    compare_report,
    run_comparison,
    status_label,
)


# ============================================================================
# Helper: get
# ============================================================================

class TestGet:
    def test_single_key(self):
        assert get({'a': 1}, 'a') == 1

    def test_nested_keys(self):
        assert get({'a': {'b': {'c': 3}}}, 'a', 'b', 'c') == 3

    def test_missing_key_returns_none(self):
        assert get({'a': 1}, 'b') is None

    def test_none_input(self):
        assert get(None, 'a') is None

    def test_non_dict_input(self):
        assert get(42, 'a') is None

    def test_intermediate_none(self):
        assert get({'a': None}, 'a', 'b') is None


# ============================================================================
# Helper: length
# ============================================================================

class TestLength:
    def test_list(self):
        assert length([1, 2, 3]) == 3

    def test_empty_list(self):
        assert length([]) == 0

    def test_none(self):
        assert length(None) == 0

    def test_non_list(self):
        assert length('hello') == 0

    def test_dict(self):
        assert length({'a': 1}) == 0


# ============================================================================
# extract_fields
# ============================================================================

class TestExtractFields:
    def test_full_data(self):
        data = {
            'name': 'Faction',
            'number': 7,
            'date': {'month': 'June', 'year': 5},
            'regions': [1, 2, 3],
            'events': [1],
            'errors': [],
            'battles': [1, 2],
            'statistics': [1, 2, 3, 4],
            'skill_reports': [1],
            'item_reports': [1, 2],
            'object_reports': [],
            'unclaimed_silver': 500,
        }
        fields = extract_fields(data)
        assert fields['name'] == 'Faction'
        assert fields['number'] == 7
        assert fields['date_month'] == 'June'
        assert fields['date_year'] == 5
        assert fields['region_count'] == 3
        assert fields['event_count'] == 1
        assert fields['error_count'] == 0
        assert fields['battle_count'] == 2
        assert fields['statistic_count'] == 4
        assert fields['skill_report_count'] == 1
        assert fields['item_report_count'] == 2
        assert fields['object_report_count'] == 0
        assert fields['unclaimed_silver'] == 500

    def test_missing_fields(self):
        fields = extract_fields({})
        assert fields['name'] is None
        assert fields['number'] is None
        assert fields['date_month'] is None
        assert fields['region_count'] == 0
        assert fields['unclaimed_silver'] is None

    def test_none_input(self):
        fields = extract_fields(None)
        assert fields['name'] is None
        assert fields['region_count'] == 0


# ============================================================================
# compare_fields
# ============================================================================

class TestCompareFields:
    def test_all_match(self):
        parsed = {'a': 1, 'b': 'hello'}
        expected = {'a': 1, 'b': 'hello'}
        results = compare_fields(parsed, expected)
        assert all(r.match for r in results)

    def test_mismatch(self):
        parsed = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 99}
        results = compare_fields(parsed, expected)
        by_field = {r.field: r for r in results}
        assert by_field['a'].match is True
        assert by_field['b'].match is False
        assert by_field['b'].parsed == 2
        assert by_field['b'].expected == 99

    def test_extra_key_in_parsed(self):
        parsed = {'a': 1, 'b': 2}
        expected = {'a': 1}
        results = compare_fields(parsed, expected)
        by_field = {r.field: r for r in results}
        assert by_field['b'].match is False
        assert by_field['b'].expected is None

    def test_extra_key_in_expected(self):
        parsed = {'a': 1}
        expected = {'a': 1, 'c': 3}
        results = compare_fields(parsed, expected)
        by_field = {r.field: r for r in results}
        assert by_field['c'].match is False
        assert by_field['c'].parsed is None

    def test_empty_dicts(self):
        results = compare_fields({}, {})
        assert results == []


# ============================================================================
# sample_pairs
# ============================================================================

class TestSamplePairs:
    def _make_pairs(self, n):
        return [ReportPair(f't{i}', f'j{i}', f'l{i}') for i in range(n)]

    def test_returns_requested_count(self):
        pairs = self._make_pairs(10)
        result = sample_pairs(pairs, 3)
        assert len(result) == 3

    def test_count_exceeds_available(self):
        pairs = self._make_pairs(3)
        result = sample_pairs(pairs, 10)
        assert len(result) == 3

    def test_deterministic_with_seed(self):
        pairs = self._make_pairs(20)
        r1 = sample_pairs(pairs, 5, seed=42)
        r2 = sample_pairs(pairs, 5, seed=42)
        assert [p.label for p in r1] == [p.label for p in r2]

    def test_different_seeds_differ(self):
        pairs = self._make_pairs(20)
        r1 = sample_pairs(pairs, 10, seed=1)
        r2 = sample_pairs(pairs, 10, seed=2)
        assert [p.label for p in r1] != [p.label for p in r2]

    def test_does_not_mutate_input(self):
        pairs = self._make_pairs(5)
        original_labels = [p.label for p in pairs]
        sample_pairs(pairs, 3, seed=1)
        assert [p.label for p in pairs] == original_labels


# ============================================================================
# status_label
# ============================================================================

class TestStatusLabel:
    def test_full_match(self):
        assert status_label(100) == 'MATCH'

    def test_partial(self):
        assert status_label(75) == '~ PARTIAL'
        assert status_label(99) == '~ PARTIAL'

    def test_mismatch(self):
        assert status_label(74) == 'MISMATCH'
        assert status_label(0) == 'MISMATCH'


# ============================================================================
# run_comparison
# ============================================================================

class TestRunComparison:
    def test_empty_pairs(self):
        summary = run_comparison([])
        assert summary.total_reports == 0
        assert summary.full_match_count == 0
        assert summary.average_match_percent == 0


# ============================================================================
# find_report_pairs
# ============================================================================

class TestFindReportPairs:
    def test_finds_pairs(self, tmp_path):
        turn_dir = tmp_path / "1"
        turn_dir.mkdir()
        (turn_dir / "report.5").write_text("some report")
        (turn_dir / "report.5.json").write_text("{}")
        (turn_dir / "report.6").write_text("another report")
        # report.6 has no .json pair - should be skipped

        pairs = find_report_pairs(str(tmp_path))
        assert len(pairs) == 1
        assert pairs[0].label == '1/report.5'
        assert pairs[0].txt_path == str(turn_dir / "report.5")
        assert pairs[0].json_path == str(turn_dir / "report.5.json")

    def test_skips_json_files(self, tmp_path):
        turn_dir = tmp_path / "1"
        turn_dir.mkdir()
        (turn_dir / "report.5.json").write_text("{}")
        # No matching text report

        pairs = find_report_pairs(str(tmp_path))
        assert len(pairs) == 0

    def test_empty_directory(self, tmp_path):
        pairs = find_report_pairs(str(tmp_path))
        assert pairs == []

    def test_multiple_turns(self, tmp_path):
        for turn in ['10', '20']:
            d = tmp_path / turn
            d.mkdir()
            (d / "report.3").write_text("r")
            (d / "report.3.json").write_text("{}")

        pairs = find_report_pairs(str(tmp_path))
        assert len(pairs) == 2
        assert pairs[0].label == '10/report.3'
        assert pairs[1].label == '20/report.3'


# ============================================================================
# compare_report (integration with real parser)
# ============================================================================

class TestCompareReport:
    def _write_pair(self, tmp_path, txt_content, json_data):
        txt_path = str(tmp_path / "report.1")
        json_path = str(tmp_path / "report.1.json")
        with open(txt_path, 'w') as f:
            f.write(txt_content)
        with open(json_path, 'w') as f:
            json.dump(json_data, f)
        return ReportPair(txt_path, json_path, 'test/report.1')

    def test_perfect_match(self, tmp_path):
        txt = (
            "Atlantis Report For:\n"
            "Test (7)\n"
            "June, Year 5\n"
            "\n"
            "Unclaimed silver: 100.\n"
        )
        json_data = {
            'name': 'Test',
            'number': 7,
            'date': {'month': 'June', 'year': 5},
            'regions': [],
            'events': [],
            'errors': [],
            'battles': [],
            'statistics': [],
            'skill_reports': [],
            'item_reports': [],
            'object_reports': [],
            'unclaimed_silver': 100,
        }
        pair = self._write_pair(tmp_path, txt, json_data)
        result = compare_report(pair)
        assert result.match_percent == 100
        assert result.parse_error is None
        assert all(f.match for f in result.fields)

    def test_mismatch_detected(self, tmp_path):
        txt = (
            "Atlantis Report For:\n"
            "Test (7)\n"
            "June, Year 5\n"
            "\n"
            "Unclaimed silver: 100.\n"
        )
        json_data = {
            'name': 'Test',
            'number': 7,
            'date': {'month': 'June', 'year': 5},
            'regions': [],
            'events': [],
            'errors': [],
            'battles': [],
            'statistics': [],
            'skill_reports': [],
            'item_reports': [],
            'object_reports': [],
            'unclaimed_silver': 999,  # mismatch
        }
        pair = self._write_pair(tmp_path, txt, json_data)
        result = compare_report(pair)
        assert result.match_percent < 100
        by_field = {f.field: f for f in result.fields}
        assert by_field['unclaimed_silver'].match is False
        assert by_field['unclaimed_silver'].parsed == 100
        assert by_field['unclaimed_silver'].expected == 999

    def test_parse_error_handled(self, tmp_path):
        pair = ReportPair('/nonexistent/path', '/also/nonexistent', 'bad/report')
        result = compare_report(pair)
        assert result.match_percent == 0
        assert result.parse_error is not None
        assert result.fields == []
