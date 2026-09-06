# Day 3 — Conditionals & Logical Operators

> Course: *100 Days of Code: Python* (App Brewery) — Day 3

## What I learned

- **`if` / `elif` / `else`**: Python runs the **first** branch whose condition is
  `True`, then skips the rest. Indentation (4 spaces) defines a block.
- **Nested `if`**: an `if` inside another `if` for multi-step decisions.
- **Comparison operators**: `==  !=  >  <  >=  <=` (note: `=` assigns, `==` compares).
- **Logical operators**: `and`, `or`, `not` — precedence is `not` → `and` → `or`.
- **Short-circuiting**: `and` stops at the first `False`, `or` stops at the first `True`.
- **Chained comparisons**: `50 <= marks < 75`.
- **`in` / `not in`** (membership) and **`is` / `is not`** (identity — mainly for `None`).
- **Truthy / falsy**: `0`, `""`, `[]`, `None` act as `False`; most else acts as `True`.
- **Ternary expression**: `"adult" if age >= 18 else "minor"`.
- **Modulo `%`**: the remainder of a division; `n % 2 == 0` tests for even.

## Key syntax

```python
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "F"

allowed = age >= 18 and (country == "UK" or country == "US")
status  = "adult" if age >= 18 else "minor"
is_even = n % 2 == 0
```

## Gotchas

- `==` is case-sensitive: `"Y" == "y"` is `False`. Normalise with `.lower()`.
- `elif` branches are only checked if every branch above them was `False`.
- Use `is` only for `None`; use `==` to compare values.

## Files

| File | What it covers |
| --- | --- |
| [`operators_reference.py`](operators_reference.py) | Full reference: comparison, logical, membership, identity, truthy/falsy, ternary, modulo, + practice |
| [`project_rollercoaster.py`](project_rollercoaster.py) | Mini-project: ride eligibility + ticket pricing (nested `if`) |
| [`project_pizza_calculator.py`](project_pizza_calculator.py) | Mini-project: pizza order total (`and` / `or`) |
| [`project_treasure_island.py`](project_treasure_island.py) | Mini-project: branching text adventure (nested `if`) |

## Run

```bash
python "Day 3/operators_reference.py"
python "Day 3/project_rollercoaster.py"
python "Day 3/project_pizza_calculator.py"
python "Day 3/project_treasure_island.py"
```
