# Day 1 — Printing, Variables & Input

> Course: *100 Days of Code: Python* (App Brewery) — Day 1

## What I learned

- **`print()`** shows text (a *string*) on the screen. Each call starts a new line.
- **String concatenation**: `+` joins strings. Both sides must be strings. `+` does
  not add spaces for you.
- **Variables** are names that hold a value. You can give a variable a new value at
  any time.
- **`input()`** reads one line typed by the user. It always returns a string.
- **`len()`** counts the characters in a string. It returns an `int`.
- `\n` inside a string is a newline (a line break).

## Key syntax

```python
print("Hello " + name + "!")     # concatenation
age = input("Your age?\n")       # always a string, even if the user types digits
count = len("Vishwanath")        # -> 10
```

## Gotchas

- `input()` never returns a number. Convert it with `int()` before you do math
  (see Day 2).
- `"Hello" + name` fails if `name` is not a string. Put a non-string inside
  `str(...)` first.

## Files

| File | What it covers |
| --- | --- |
| [`concepts.py`](concepts.py) | print, strings, concatenation, variables, input, len |
| [`project_band_name_generator.py`](project_band_name_generator.py) | Mini-project: join two inputs into a band name |

## Run

```bash
python "Day 1/concepts.py"
python "Day 1/project_band_name_generator.py"
```
