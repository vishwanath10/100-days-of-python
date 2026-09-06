# Day 1 — Printing, Variables & Input

> Course: *100 Days of Code: Python* (App Brewery) — Day 1

## What I learned

- **`print()`** displays text (a *string*) on the screen; each call starts a new line.
- **String concatenation**: `+` joins strings — but only strings, and spaces are not automatic.
- **Variables** are names that hold a value; you can reassign them freely.
- **`input()`** reads one line typed by the user and **always returns a string**.
- **`len()`** counts the characters in a string and returns an `int`.
- `\n` inside a string is a newline (line break).

## Key syntax

```python
print("Hello " + name + "!")     # concatenation
age = input("Your age?\n")       # always a string, even if they type digits
count = len("Vishwanath")        # -> 10
```

## Gotchas

- `input()` never returns a number — `input()` + `int()` is needed before doing math (see Day 2).
- `"Hello" + name` fails if `name` is not a string; wrap non-strings in `str(...)`.

## Files

| File | What it covers |
| --- | --- |
| [`concepts.py`](concepts.py) | print, strings, concatenation, variables, input, len |
| [`project_band_name_generator.py`](project_band_name_generator.py) | Mini-project: combine two inputs into a band name |

## Run

```bash
python "Day 1/concepts.py"
python "Day 1/project_band_name_generator.py"
```
