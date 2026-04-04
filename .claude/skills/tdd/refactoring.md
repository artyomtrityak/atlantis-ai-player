# Refactor Candidates

After TDD cycle, look for:

- **Duplication** → Extract function/class
- **Long methods** → Break into private helpers (keep tests on public interface)
- **Shallow modules** → Combine or deepen
- **Feature envy** → Move logic to where data lives
- **Primitive obsession** → Introduce dataclasses or value objects
- **Implicit interfaces** → Extract `typing.Protocol` for dependency injection boundaries
- **Existing code** the new code reveals as problematic

## Python-Specific Refactors

- Replace raw dicts with `@dataclass` or `NamedTuple` when the shape is stable and used in multiple places
- Use `typing.Protocol` instead of abstract base classes when you only need structural subtyping (duck typing with type safety)
- Extract `conftest.py` fixtures when test setup is duplicated across files