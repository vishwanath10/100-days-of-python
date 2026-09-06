# 100 Days of Python

My solutions, notes, and practice code for the **100 Days of Code: Python** course
(App Brewery). Each day is a separate folder. I can open a folder again later and
see what I learned.

## How I organize each day

| File | Purpose |
| --- | --- |
| `README.md` | The day's notes: what I learned, key syntax, gotchas, and a file index |
| `concepts.py` | One guide you can run. It covers the day's concepts. |
| `<topic>_reference.py` | A larger reference for one topic, when the topic needs it |
| `project_<name>.py` | The day's mini-project or projects |

Every `.py` file starts with a docstring. The docstring says what the file does
and how to run it. Inline comments explain each step.

## Progress

| Day | Topic | Key concepts | Folder |
| --- | --- | --- | --- |
| 1 | Printing, Variables & Input | `print()`, string `+`, variables, `input()` (always a string), `len()` | [`Day 1/`](Day%201/) |
| 2 | Data Types, Numbers & f-strings | `str`/`int`/`float`/`bool`, `type()`, casting, `+ - * / // **`, `round()`, f-strings | [`Day 2/`](Day%202/) |
| 3 | Conditionals & Logical Operators | `if`/`elif`/`else`, nested `if`, comparisons, `and`/`or`/`not`, `in`, `is`, truthy/falsy, ternary, `%` | [`Day 3/`](Day%203/) |
| 4 | Lists, Random Numbers & Modules | lists + methods, nested/2D lists, the `random` module, `import`, `__name__ == "__main__"` | [`Day 4/`](Day%204/) |
| 5 | Loops | `for ... in`, `range()`, totals in a loop (`sum`/`max` by hand), FizzBuzz | [`Day 5/`](Day%205/) |

## Running the code

```bash
# from the repo root
python "Day 3/operators_reference.py"
python "Day 5/project_fizzbuzz.py"
```

Some concept files call `input()`. They stop and wait for you to type. This is
normal. These files show how `input()` works.

Tested with Python 3.11.

## Notes

The `.gitignore` file keeps the App Brewery course PDFs and other copyrighted
material out of this repository. It also ignores the auto-generated `__pycache__/`
folders.
