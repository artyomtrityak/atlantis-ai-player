# Test Organization (pytest)

## Directory Structure

```
project/
├── src/
│   ├── parser.py
│   └── orders.py
├── tests/
│   ├── conftest.py          # shared fixtures
│   ├── test_parser.py       # mirrors src/parser.py
│   └── test_orders.py       # mirrors src/orders.py
└── pytest.ini               # or pyproject.toml [tool.pytest.ini_options]
```

Convention: `tests/test_<module>.py` mirrors `src/<module>.py`. Keep tests close to what they test.

## conftest.py and Fixtures

`conftest.py` files are auto-discovered by pytest. Fixtures defined there are available to all tests in the same directory and below — no imports needed.

```python
# tests/conftest.py — example fixtures (adapt to your actual project)

import pytest

@pytest.fixture
def sample_report_text():
    """A minimal report string for parser tests."""
    return (
        "Atlantis Report For:\n"
        "TestFaction (1) (Martial 1, Magic 1)\n"
        "January, Year 1\n"
    )

@pytest.fixture
def parsed_region():
    """A pre-built region dict for order generation tests."""
    return {
        "name": "plain",
        "coordinates": (10, 20, 1),
        "units": [{"name": "Scout", "number": 101, "items": ["horse"]}],
    }
```

### Fixture Scoping

```python
@pytest.fixture(scope="session")
def expensive_resource():
    """Created once for the entire test session."""
    return load_large_dataset()

@pytest.fixture(scope="module")
def per_module():
    """Created once per test file."""
    ...

@pytest.fixture  # default scope="function"
def per_test():
    """Created fresh for each test — safest default."""
    ...
```

Use `scope="function"` (default) unless setup is genuinely expensive. Wider scopes risk shared mutable state leaking between tests.

## Parametrize

Use `@pytest.mark.parametrize` when the same logic needs testing with multiple inputs. Ideal for parsers and data transformations.

```python
# Example: testing a parser across multiple input variations
@pytest.mark.parametrize("input_line, expected", [
    ("3 leaders [LEAD]", {"name": "leaders", "abbr": "LEAD", "count": 3}),
    ("1 sword [SWOR]", {"name": "sword", "abbr": "SWOR", "count": 1}),
    ("100 silver [SILV]", {"name": "silver", "abbr": "SILV", "count": 100}),
])
def test_parse_item(input_line, expected):
    result = parse_item(input_line)
    assert result == expected
```

Use `pytest.param` with `id=` for clearer test names:

```python
@pytest.mark.parametrize("text, expected_count", [
    pytest.param("Events during turn:\n", 0, id="empty-events"),
    pytest.param("Events during turn:\nUnit arrived.\n\n", 1, id="single-event"),
])
def test_parse_events(text, expected_count):
    result = parse_events(text)
    assert len(result) == expected_count
```

## Markers

Tag tests for selective execution:

```python
# pytest.ini or pyproject.toml
# [tool.pytest.ini_options]
# markers = [
#     "slow: marks tests as slow (deselect with '-m \"not slow\"')",
#     "integration: tests that hit real files or external systems",
# ]

@pytest.mark.slow
def test_parse_full_game_history():
    """Parses all reports across 20 turns — takes a few seconds."""
    ...

@pytest.mark.integration
def test_orders_roundtrip_through_engine():
    ...
```

Run subsets: `pytest -m "not slow"` or `pytest -m integration`.

## tmp_path for File Tests

pytest provides `tmp_path` (per-test temporary directory) built-in:

```python
def test_write_orders_to_file(tmp_path):
    orders_file = tmp_path / "orders.3"
    write_orders(orders_file, faction_id=3, commands=["MOVE NORTH"])
    content = orders_file.read_text()
    assert "#atlantis 3" in content
    assert "MOVE NORTH" in content
```
