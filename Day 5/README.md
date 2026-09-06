# Day 5 — Loops

> Course: *100 Days of Code: Python* (App Brewery) — Day 5

## What I learned

- **`for item in list:`** runs the indented block once per item.
- **`range(start, stop)`** produces `start … stop - 1`. It does **not** include the
  stop value. `range(1, 101)` covers 1–100.
- **Totals in a loop**: keep a running variable and update it on each pass. This is
  the pattern behind `sum()` (a running total) and `max()` (the best value so far).
- **`sum(list)`** and **`max(list)`** are the built-in shortcuts.
- **FizzBuzz**: `%` (modulo) plus the order of the `if` / `elif` tests. Test the
  combined `3 and 5` case **before** the single cases.

## Key syntax

```python
for name in names:
    print(name)

total = 0
for n in numbers:
    total += n

for n in range(1, 101):   # 1 .. 100
    ...
```

## Gotchas

- `range(1, 100)` stops at **99**, not 100. `range` never includes the stop value.
- If you test `n % 3 == 0` before `n % 3 == 0 and n % 5 == 0`, then 15 prints
  `"Fizz"`, not `"FizzBuzz"`. Order matters.
- Indentation puts a line "inside" the loop.

## Files

| File | What it covers |
| --- | --- |
| [`concepts.py`](concepts.py) | Looping over lists, `range()`, manual `sum`/`max`, built-ins |
| [`project_fizzbuzz.py`](project_fizzbuzz.py) | Mini-project: the classic FizzBuzz 1–100 |

## Run

```bash
python "Day 5/concepts.py"
python "Day 5/project_fizzbuzz.py"
```
