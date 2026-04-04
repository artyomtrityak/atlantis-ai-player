# When to Mock

Mock at **system boundaries** only:

- External APIs (game engine server, email, etc.)
- File system (reading report files, writing order files)
- Time/randomness
- Network calls

Don't mock:

- Your own classes/modules
- Internal collaborators
- Anything you control

## Choosing the Right Tool

**`monkeypatch`** (pytest built-in) — best for simple attribute/env var replacement. Auto-reverts after test. Use for:
- Environment variables
- Simple function replacement
- Dictionary values

```python
# Replace an env var for the test
def test_load_config_from_env(monkeypatch):
    monkeypatch.setenv("GAME_DATA_DIR", "/tmp/test_game")
    config = load_config()
    assert config.data_dir == "/tmp/test_game"
```

**`unittest.mock.patch`** — best for replacing objects at import paths, tracking calls. Use for:
- Mocking external service calls
- Verifying interactions at system boundaries
- Complex replacement with `MagicMock`/`Mock`

```python
from unittest.mock import patch, Mock

# Mock an external API call at the system boundary
def test_submit_orders_sends_to_server():
    mock_response = Mock(status_code=200, json=lambda: {"accepted": True})
    with patch("app.client.requests.post", return_value=mock_response) as mock_post:
        result = submit_orders(faction_id=14, orders=["MOVE NORTH"])
        assert result.accepted is True
        mock_post.assert_called_once()
```

## Designing for Mockability

At system boundaries, design interfaces that are easy to mock:

**1. Use dependency injection**

Pass external dependencies in rather than creating them internally:

```python
# Easy to mock — caller controls the dependency
def parse_report(report_reader):
    """Parse a turn report using the provided reader."""
    raw_text = report_reader.read()
    return extract_sections(raw_text)

# Hard to mock — creates its own dependency
def parse_report(filepath):
    """Parse a turn report from a file path."""
    with open(filepath) as f:
        raw_text = f.read()
    return extract_sections(raw_text)
```

**2. Prefer specific interfaces over generic ones**

Create specific functions for each external operation instead of one generic function:

```python
# GOOD: Each function is independently mockable
class GameClient:
    def fetch_report(self, faction_id: int) -> str: ...
    def submit_orders(self, faction_id: int, orders: list[str]) -> bool: ...
    def get_game_status(self) -> dict: ...

# BAD: Mocking requires conditional logic inside the mock
class GameClient:
    def request(self, endpoint: str, **kwargs) -> dict: ...
```

The specific approach means:
- Each mock returns one specific shape
- No conditional logic in test setup
- Easier to see which operations a test exercises

## Fixtures for Shared Mocks

When multiple tests need the same mock, use a `conftest.py` fixture:

```python
# conftest.py
@pytest.fixture
def mock_game_client():
    """Provide a mock game client for tests that hit external APIs."""
    with patch("app.client.GameClient") as mock_cls:
        client = mock_cls.return_value
        client.fetch_report.return_value = "Atlantis Report For:\nTest (1)\n"
        yield client
```
