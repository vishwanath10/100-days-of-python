# Day 5 — Loops

> Course: *100 Days of Code: Python* (App Brewery) — Day 5

## What I learned

- **`for item in list:`** runs the indented block once per item.
- **`range(start, stop)`** produces `start … stop - 1` (the stop value is
  **excluded**). `range(1, 101)` covers 1–100.
- **Aggregation with a loop**: keep a running variable and update it each pass —
  the pattern behind `sum()` (running total) and `max()` (best so far).
- **`sum(list)`** and **`max(list)`** are the built-in shortcuts.
- **FizzBuzz**: `%` (modulo) + `if` / `elif` ordering — test the combined
  `3 and 5` case **before** the individual cases.

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

- `range(1, 100)` stops at **99**, not 100 — the stop value is never included.
- In FizzBuzz, checking `n % 3 == 0` before `n % 3 == 0 and n % 5 == 0` makes 15
  print `"Fizz"` instead of `"FizzBuzz"`. Order matters.
- Indentation is what puts a line "inside" the loop.

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
