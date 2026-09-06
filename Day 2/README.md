# Day 2 — Data Types, Numbers & f-strings

> Course: *100 Days of Code: Python* (App Brewery) — Day 2

## What I learned

- **Data types**: `str`, `int`, `float`, `bool`. `type(value)` reports which one.
- **Type casting**: `int()`, `float()`, `str()` convert between types.
- **String indexing**: `"Hello"[0]` is `"H"`, `"Hello"[-1]` is `"o"`.
- **Arithmetic**: `+  -  *  /  //  **` and operator precedence (PEMDAS).
  - `/` always gives a `float`; `//` floors to a whole number.
- **`round(x)`** and **`round(x, ndigits)`**.
- **Assignment operators**: `score += 1` means `score = score + 1`.
- **f-strings**: `f"Your score is {score}"` inserts variables into text.
- Underscores in number literals (`123_456`) are cosmetic only.

## Key syntax

```python
print(int("1") + int("100"))   # 101  (without int() -> "1100")
print(6 / 3)                    # 2.0
print(6 // 3)                   # 2
print(2 ** 3)                   # 8
print(round(3.14159, 2))        # 3.14
print(f"Total: {total}")        # f-string
```

## Gotchas

- `input()` is always a string — cast it before arithmetic.
- `"text" + number` raises `TypeError`; use `"text" + str(number)` or an f-string.
- `/` returns a float even for exact divisions (`4 / 2` -> `2.0`).

## Files

| File | What it covers |
| --- | --- |
| [`concepts.py`](concepts.py) | Data types, casting, arithmetic, `round()`, f-strings |
| [`project_tip_calculator.py`](project_tip_calculator.py) | Mini-project: split a bill + tip between people |

## Run

```bash
python "Day 2/concepts.py"
python "Day 2/project_tip_calculator.py"
```
