# Day 4 — Lists, Randomisation & Modules

> Course: *100 Days of Code: Python* (App Brewery) — Day 4

## What I learned

- **Lists**: ordered collections in `[ ]`; index from `0`, negative indexes count
  from the end, `len(list)` gives the count.
- **Modifying lists**: `list[i] = x`, `list.append(one_item)`,
  `list.extend([many, items])`.
  - `append(a_list)` nests the whole list as a single item — `extend` does not.
- **Nested / 2D lists**: a list of lists; index twice — `grid[row][col]`.
- **The `random` module** (standard library): `randint`, `random`, `uniform`,
  `randrange`, `choice`, `choices`, `sample`, `shuffle`, `seed`.
- **Modules**: any `.py` file is a module. `import name` runs it once and
  exposes its names as `name.thing`; `from name import thing` imports just one.
- **`if __name__ == "__main__":`** keeps a module's demo code from running on import.
- `__pycache__/` holds compiled `.pyc` files — auto-generated, safe to delete.

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

- `random.shuffle(x)` reorders **in place** and returns `None` — never write
  `x = random.shuffle(x)`.
- `randint(a, b)` **includes** `b`; `randrange(a, b)` **excludes** `b`.
- Run `importing_modules.py` from **inside** the `Day 4/` folder so `import dice` resolves.

## Files

| File | What it covers |
| --- | --- |
| [`lists.py`](lists.py) | Creating, indexing, modifying, and nesting lists |
| [`random_reference.py`](random_reference.py) | Full tour of the `random` module + a coin-flip experiment |
| [`dice.py`](dice.py) | A tiny module (a `roll()` function) imported by the next file |
| [`importing_modules.py`](importing_modules.py) | `import` styles, `__pycache__`, `__name__ == "__main__"` |
| [`project_rock_paper_scissors.py`](project_rock_paper_scissors.py) | Mini-project: one round vs. a random computer move |

## Run

```bash
python "Day 4/lists.py"
python "Day 4/random_reference.py"
cd "Day 4" && python importing_modules.py && cd ..
python "Day 4/project_rock_paper_scissors.py"
```
