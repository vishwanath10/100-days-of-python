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
- **`break`** stops a loop immediately, even when the loop condition is still
  `True`.
- A **sentinel value** (for example, `0`) is a special input that tells a loop
  to stop.

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
- Ask for the first input before a `while` loop. Then the condition has a
  value to test on the first pass.
- `int(input(...))` stops the program with a `ValueError` when the user types
  text that is not a number.

## Files

| File | What it covers |
| --- | --- |
| [`concepts.py`](concepts.py) | Functions, `while`, `not`, `if`/`elif`/`else`, and nested `if` statements |
| [`exercise_1_countdown.py`](exercise_1_countdown.py) | Exercise 1: Check the input, then count down to "Liftoff!" |
| [`exercise_2_sum_of_numbers.py`](exercise_2_sum_of_numbers.py) | Exercise 2: Keep a running total until the user enters 0 |
| [`exercise_3_password_retry.py`](exercise_3_password_retry.py) | Exercise 3: Give 3 password attempts with `break` |

## Practice exercises

| # | Exercise | Level | Status |
| --- | --- | --- | --- |
| 1 | **Countdown:** Ask for a positive integer. Count down to 1, then print "Liftoff!". | Beginner | Done |
| 2 | **Sum of Numbers:** Total the numbers that the user enters. Stop at 0 and print the total. | Beginner | Done |
| 3 | **Password Retry:** Give the user a maximum of 3 attempts to guess a secret password. | Beginner to Easy-Medium | Done |
| 4 | **Digit Counter and Sum:** Ask for a positive integer. Use a `while` loop to count its digits and calculate their sum. Do not convert the number to a string. Hint: use `% 10` and `// 10`. Example: `4729` prints `Digits: 4, Sum: 22`. | Medium | To do |
| 5 | **Number Guessing Game:** The program picks a random number from 1 to 50 with `random.randint`. The user guesses until the guess is correct. Print "Too high" or "Too low" after each wrong guess. At the end, print the number of attempts. Bonus: let the user type `q` to quit, and do not crash on text input. | Medium | To do |

## Run

```bash
python "Day 6/concepts.py"
python "Day 6/exercise_1_countdown.py"
python "Day 6/exercise_2_sum_of_numbers.py"
python "Day 6/exercise_3_password_retry.py"
```
