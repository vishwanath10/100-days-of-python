# Day 6 - Functions, While Loops, and Conditionals

> Course: *100 Days of Code: Python* (App Brewery) - Day 6

## What I learned

- A **function** groups instructions under a name. Define it with `def`, then
  call it with parentheses.
- **`while condition:`** repeats an indented block while `condition` is `True`.
- A `while` loop needs a change inside the loop that can make its condition
  `False`. Otherwise, the loop does not stop.
- **`not`** reverses a Boolean value. For example, `not game_over` is `True`
  when `game_over` is `False`.
- **`if`**, **`elif`**, and **`else`** choose one path. You can put another
  `if` statement inside a path to make a more detailed decision.

## Key syntax

```python
def greet():
    print("Hello")

greet()

count = 1
while count <= 3:
    print(count)
    count += 1

if score >= 90:
    print("Grade A")
elif score >= 60:
    print("Pass")
else:
    print("Try again")
```

## Gotchas

- Python uses `elif`, not `elseif`.
- Indent every line that belongs inside a function, loop, or conditional block.
- Update the loop variable in a `while` loop. For example, use `count += 1`.
- `not []` is `True` because an empty list is false in a condition.

## Files

| File | What it covers |
| --- | --- |
| [`concepts.py`](concepts.py) | Functions, `while`, `not`, `if`/`elif`/`else`, and nested `if` statements |

## Run

```bash
python "Day 6/concepts.py"
```
