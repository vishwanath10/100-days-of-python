"""
Day 5 Project - FizzBuzz
========================
Count from 1 to 100, but:
  - multiple of 3 AND 5  -> "FizzBuzz"
  - multiple of 3 only   -> "Fizz"
  - multiple of 5 only   -> "Buzz"
  - otherwise            -> the number itself
Practises: for + range(), the modulo operator %, if / elif / else ordering.

Run me:  python "Day 5/project_fizzbuzz.py"
"""

for number in range(1, 101):
    # Check the "both" case FIRST - otherwise the "% 3" branch would catch
    # numbers like 15 before we ever test for "% 5" as well.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
