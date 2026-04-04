# Interface Design for Testability

Good interfaces make testing natural:

1. **Accept dependencies, don't create them**

   ```python
   # Testable — caller injects the dependency
   def generate_orders(game_state, strategy):
       """Generate turn orders from parsed game state using the given strategy."""
       return strategy.decide(game_state)

   # Hard to test — creates its own dependency
   def generate_orders(report_path):
       """Parse report and generate orders internally."""
       game_state = ReportParser().parse(open(report_path).read())
       strategy = DefaultStrategy()
       return strategy.decide(game_state)
   ```

2. **Return results, don't produce side effects**

   ```python
   # Testable — returns a value you can assert on
   def calculate_tax(region) -> dict:
       """Calculate tax owed for a region based on its income."""
       return {"region": region.name, "tax": region.income * region.tax_rate}

   # Hard to test — mutates state, nothing to assert on return
   def apply_tax(region) -> None:
       """Mutate region in place."""
       region.treasury -= region.income * region.tax_rate
   ```

3. **Small surface area**
   - Fewer methods = fewer tests needed
   - Fewer params = simpler test setup
   - Use `typing.Protocol` to define narrow interfaces at boundaries

   ```python
   from typing import Protocol

   class ReportReader(Protocol):
       """Narrow interface — only what consumers need."""
       def read(self, faction_id: int) -> str: ...

   # Any object with a matching read() method satisfies this,
   # making it trivial to substitute in tests.
   class FakeReportReader:
       def __init__(self, text: str):
           self.text = text

       def read(self, faction_id: int) -> str:
           return self.text
   ```
