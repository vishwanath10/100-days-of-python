"""
DAY 3 - OPERATORS & CONTROL FLOW REFERENCE
=========================================
"Control flow" means deciding WHICH lines run, and in what order.
The operators below all produce True/False values, and Python uses those
to choose a path through your program.

Run me top to bottom (python "Day 3/operators_reference.py") and read the
comments next to the output. Section 11 has practice questions.
"""

# ---------------------------------------------------------------------------
# 1. COMPARISON OPERATORS  ->  ask a question, answer True or False
# ---------------------------------------------------------------------------
# ==   equal to            !=   not equal to
# >    greater than        <    less than
# >=   greater or equal    <=   less or equal

age = 18
print(age == 18)   # True  -> "is age exactly 18?"
print(age != 18)   # False -> "is age different from 18?"
print(age > 21)    # False
print(age < 21)    # True
print(age >= 18)   # True  -> greater OR equal, so 18 counts
print(age <= 17)   # False

# IMPORTANT: one "=" assigns a value, two "==" compares values.
x = 5          # assignment: put 5 into x
print(x == 5)  # comparison: is x equal to 5?  -> True


# ---------------------------------------------------------------------------
# 2. USING COMPARISONS IN if / elif / else
# ---------------------------------------------------------------------------
# Python runs the FIRST branch whose condition is True, then skips the rest.
# Indentation (4 spaces) tells Python which lines belong to a branch.

score = 75
if score >= 90:
    print("Grade: A")
elif score >= 70:          # only checked if the line above was False
    print("Grade: B")      # this one runs because 75 >= 70
elif score >= 50:
    print("Grade: C")
else:                      # runs only if every condition above was False
    print("Grade: F")


# ---------------------------------------------------------------------------
# 3. LOGICAL OPERATORS: and / or / not
# ---------------------------------------------------------------------------
#   A and B  -> True only if BOTH A and B are True
#   A or  B  -> True if AT LEAST ONE of A or B is True
#   not A    -> flips True to False and False to True

temperature = 22
is_raining = False

if temperature > 15 and not is_raining:      # every part must be True
    print("Good weather for a walk.")

day = "Sunday"
if day == "Saturday" or day == "Sunday":     # one True part is enough
    print("It's the weekend!")

logged_in = False
if not logged_in:                            # invert a condition
    print("Please log in first.")

# Truth table reference (LEFT operator RIGHT -> result)
print(True  and False)  # False
print(True  or  False)  # True
print(not   True)       # False

# Precedence when you mix them:  not  ->  and  ->  or
# When in doubt, add brackets so it reads the way you mean it.
country = "UK"
allowed = age >= 18 and (country == "UK" or country == "US")
print("allowed:", allowed)


# ---------------------------------------------------------------------------
# 4. SHORT-CIRCUIT EVALUATION (a useful detail of and / or)
# ---------------------------------------------------------------------------
# Python stops as soon as the answer is certain:
#   - "and": if the first part is False, the rest is skipped (result False).
#   - "or" : if the first part is True,  the rest is skipped (result True).

def check():
    print("  check() was called")
    return True

print("False and check():", False and check())   # check() is NOT called
print("True or check():", True or check())        # check() is NOT called

# This lets you guard against errors:
name = ""
# If name is empty the left side is False, so name[0] is never reached
# and we avoid an "index out of range" crash.
if name != "" and name[0] == "A":
    print("Name starts with A")
else:
    print("No name, or it doesn't start with A")


# ---------------------------------------------------------------------------
# 5. CHAINED COMPARISONS
# ---------------------------------------------------------------------------
marks = 65
if 50 <= marks < 75:          # same as: marks >= 50 and marks < 75
    print("You passed, but there's room to improve.")


# ---------------------------------------------------------------------------
# 6. MEMBERSHIP OPERATORS: in / not in
# ---------------------------------------------------------------------------
vowels = ["a", "e", "i", "o", "u"]
letter = "e"
if letter in vowels:
    print(f"'{letter}' is a vowel")
if "z" not in vowels:
    print("'z' is not a vowel")

sentence = "the quick brown fox"
if "quick" in sentence:                       # substring check on a string
    print("Found the word 'quick'")


# ---------------------------------------------------------------------------
# 7. IDENTITY OPERATORS: is / is not
# ---------------------------------------------------------------------------
# "==" asks: are the two values equal?
# "is" asks: are they the exact same object in memory?
# Use "==" almost always; use "is" when comparing to None.

result = None
if result is None:
    print("No result yet")

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  -> same contents
print(a is b)   # False -> two separate lists in memory


# ---------------------------------------------------------------------------
# 8. TRUTHY AND FALSY VALUES
# ---------------------------------------------------------------------------
# An if-condition need not be a real True/False. Some values act like False:
#   Falsy: False, None, 0, 0.0, "" (empty string), [] {} () (empty containers)
#   Truthy: basically everything else

items = []
if items:                       # empty list is falsy
    print("Cart has items")
else:
    print("Your cart is empty")

username = "neo"
if username:                    # non-empty string is truthy
    print(f"Hello, {username}")


# ---------------------------------------------------------------------------
# 9. CONDITIONAL (TERNARY) EXPRESSION
# ---------------------------------------------------------------------------
# One-line choice between two values:
#   value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult


# ---------------------------------------------------------------------------
# 10. THE MODULO OPERATOR: %
# ---------------------------------------------------------------------------
# % gives the REMAINDER of a division. 10 % 3 is 1 (10 / 3 is 3 remainder 1).
print(10 % 3)                    # 1
number = 8
if number % 2 == 0:             # no remainder -> divisible by 2 -> even
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# ---------------------------------------------------------------------------
# 11. PRACTICE - predict the result, then run the file to check
# ---------------------------------------------------------------------------
# Practice 1: A user can drive if they are 18 or older AND have a licence.
user_age = 19
has_licence = True
print("Practice 1 (expect True):", user_age >= 18 and has_licence)

# Practice 2: Entry is free if you are under 5 OR 65 and over.
visitor_age = 70
print("Practice 2 (expect True):", visitor_age < 5 or visitor_age >= 65)

# Practice 3: A seat is available if it is NOT booked.
is_booked = False
print("Practice 3 (expect True):", not is_booked)

# Practice 4: n passes if it is between 1 and 100 inclusive AND even.
n = 42
print("Practice 4 (expect True):", 1 <= n <= 100 and n % 2 == 0)
