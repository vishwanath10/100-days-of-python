# Day 4 — Lists, Random Numbers & Modules

> Course: *100 Days of Code: Python* (App Brewery) — Day 4

## What I learned

- **Lists**: ordered collections in `[ ]`. Index from `0`. Negative indexes count
  from the end. `len(list)` gives the count.
- **Modifying lists**: `list[i] = x`, `list.append(one_item)`,
  `list.extend([many, items])`.
  - `append(a_list)` nests the whole list as one item. `extend` does not.
- **Nested / 2D lists**: a list of lists. Index twice: `grid[row][col]`.
- **The `random` module** (standard library): `randint`, `random`, `uniform`,
  `randrange`, `choice`, `choices`, `sample`, `shuffle`, `seed`.
- **Modules**: any `.py` file is a module. `import name` runs it once and gives
  you its names as `name.thing`. `from name import thing` imports one name only.
- **`if __name__ == "__main__":`** makes a module's demo code run only on a direct
  run, not on import.
- `__pycache__/` holds compiled `.pyc` files. Python generates them. They are safe
  to delete.

## Key syntax

```python
fruits[1] = "Banana"
fruits.append("Mango")
fruits.extend(["Kiwi", "Melon"])
grid[0][2]                       # 2D indexing

import random
random.randint(1, 6)            # 1..6 inclusive
random.choice(["a", "b", "c"])  # one random item

import dice                     # your own dice.py
dice.roll()
```

## Gotchas

- `random.shuffle(x)` reorders the list **in place** and returns `None`. Never
  write `x = random.shuffle(x)`.
- `randint(a, b)` **includes** `b`. `randrange(a, b)` **excludes** `b`.
- Run `importing_modules.py` from **inside** the `Day 4/` folder so Python can
  find `import dice`.

## Files

| File | What it covers |
| --- | --- |
| [`lists.py`](lists.py) | Creating, indexing, modifying, and nesting lists |
| [`random_reference.py`](random_reference.py) | Full guide to the `random` module, plus a coin-flip experiment |
| [`dice.py`](dice.py) | A tiny module (a `roll()` function) that the next file imports |
| [`importing_modules.py`](importing_modules.py) | `import` styles, `__pycache__`, `__name__ == "__main__"` |
| [`project_rock_paper_scissors.py`](project_rock_paper_scissors.py) | Mini-project: one round against a random computer move |

## Run

```bash
python "Day 4/lists.py"
python "Day 4/random_reference.py"
cd "Day 4" && python importing_modules.py && cd ..
python "Day 4/project_rock_paper_scissors.py"
```
