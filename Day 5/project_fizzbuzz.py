"""
Day 5 Project - FizzBuzz
========================
Count from 1 to 100, but:
  - multiple of 3 AND 5  -> "FizzBuzz"
  - multiple of 3 only   -> "Fizz"
  - multiple of 5 only   -> "Buzz"
  - otherwise            -> the number itself
Practices: for + range(), the modulo operator %, the order of the
           if / elif / else tests.

Run me:  python "Day 5/project_fizzbuzz.py"
"""

for number in range(1, 101):
    # Check the "both" case FIRST. If you do not, the "% 3" branch matches a
    # number like 15, and Python never tests "% 5".
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
