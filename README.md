# 100 Days of Python

My solutions, notes, and practice code for the **100 Days of Code: Python** course
(App Brewery). Each day is a self-contained folder I can re-open later and quickly
recall what was covered.

## How each day is organised

| File | Purpose |
| --- | --- |
| `README.md` | The day's notes: what I learned, key syntax, gotchas, and a file index |
| `concepts.py` | One organised, runnable walkthrough of the day's concepts |
| `<topic>_reference.py` | A deeper standalone reference, when a topic warrants it |
| `project_<name>.py` | The day's mini-project(s) |

Every `.py` file has a docstring at the top saying what it does and how to run it,
and inline comments explaining each step.

## Progress

| Day | Topic | Key concepts | Folder |
| --- | --- | --- | --- |
| 1 | Printing, Variables & Input | `print()`, string `+`, variables, `input()` (always a string), `len()` | [`Day 1/`](Day%201/) |
| 2 | Data Types, Numbers & f-strings | `str`/`int`/`float`/`bool`, `type()`, casting, `+ - * / // **`, `round()`, f-strings | [`Day 2/`](Day%202/) |
| 3 | Conditionals & Logical Operators | `if`/`elif`/`else`, nested `if`, comparisons, `and`/`or`/`not`, `in`, `is`, truthy/falsy, ternary, `%` | [`Day 3/`](Day%203/) |
| 4 | Lists, Randomisation & Modules | lists + methods, nested/2D lists, the `random` module, `import`, `__name__ == "__main__"` | [`Day 4/`](Day%204/) |
| 5 | Loops | `for ... in`, `range()`, loop aggregation (`sum`/`max` by hand), FizzBuzz | [`Day 5/`](Day%205/) |

## Running the code

```bash
# from the repo root
python "Day 3/operators_reference.py"
python "Day 5/project_fizzbuzz.py"
```

Some concept files call `input()` and will pause for typed input — that is
expected; they are demonstrating `input()` itself.

Tested with Python 3.11.

## Notes

Course PDFs and other copyrighted materials from App Brewery are intentionally
excluded from this repository (see [`.gitignore`](.gitignore)). Auto-generated
`__pycache__/` folders are ignored too.
