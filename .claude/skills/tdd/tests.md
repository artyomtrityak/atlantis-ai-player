# Good and Bad Tests

## Good Tests

**Integration-style**: Test through real interfaces, not mocks of internal parts.

```python
# GOOD: Tests observable behavior through the public interface
def test_user_can_checkout_with_valid_cart():
    cart = Cart()
    cart.add(Product("Widget", price=9.99))
    result = checkout(cart, payment_method="card")
    assert result.status == "confirmed"
```

Characteristics:

- Tests behavior users/callers care about
- Uses public API only
- Survives internal refactors
- Describes WHAT, not HOW
- One logical assertion per test (multiple `assert` on the same result is fine)

## Bad Tests

**Implementation-detail tests**: Coupled to internal structure.

```python
# BAD: Tests implementation details — will break on any refactor
def test_checkout_calls_payment_service(mocker):
    mock_process = mocker.patch("app.checkout.payment_service.process")
    checkout(cart, payment="card")
    mock_process.assert_called_once_with(cart.total)
```

Red flags:

- Mocking internal collaborators
- Testing private methods (`_helper()`)
- Asserting on call counts/order of internal calls
- Test breaks when refactoring without behavior change
- Test name describes HOW not WHAT
- Verifying through external means instead of interface

```python
# BAD: Bypasses interface to verify via raw DB query
def test_create_user_saves_to_database(db_session):
    create_user(name="Alice")
    row = db_session.execute("SELECT * FROM users WHERE name = 'Alice'").fetchone()
    assert row is not None

# GOOD: Verifies through the public interface
def test_created_user_is_retrievable():
    user = create_user(name="Alice")
    retrieved = get_user(user.id)
    assert retrieved.name == "Alice"
```

## Pytest Best Practices

**Use plain `assert`** — pytest rewrites assertions to show rich diffs automatically. No need for `self.assertEqual` or helper methods.

```python
# pytest gives clear diffs on failure for all of these
assert result == expected
assert "error" in message
assert len(items) == 3
```

**Use `pytest.raises` for expected exceptions:**

```python
def test_checkout_rejects_empty_cart():
    cart = Cart()
    with pytest.raises(ValueError, match="cart is empty"):
        checkout(cart, payment_method="card")
```

**Prefer plain functions over test classes** unless you need to group related tests:

```python
# Simple — preferred for most cases
def test_add_item_to_cart():
    cart = Cart()
    cart.add(Product("Widget", price=9.99))
    assert len(cart.items) == 1

# Classes — for grouping related behaviors
class TestCartCheckout:
    def test_checkout_with_valid_cart(self):
        ...

    def test_checkout_rejects_empty_cart(self):
        ...
```

**Name tests after the behavior, not the method:**

```python
# BAD: named after method
def test_process():
    ...

# GOOD: named after behavior
def test_order_total_includes_tax():
    ...
```
