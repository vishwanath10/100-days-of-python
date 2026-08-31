"""
CONTROL FLOW OPERATORS IN PYTHON
================================

"Control flow" means deciding WHICH lines of code run, and in what order.
The operators below produce True/False values, and Python uses those
True/False values to choose a path through your program.

Run this file top to bottom (python control_flow_operators.py) and read
the comments alongside the output.
"""

# ---------------------------------------------------------------------------
# 1. COMPARISON OPERATORS  ->  they ask a question and answer True or False
# ---------------------------------------------------------------------------
# ==   equal to
# !=   not equal to
# >    greater than
# <    less than
# >=   greater than or equal to
# <=   less than or equal to

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
# Indentation (4 spaces) is what tells Python which lines belong to a branch.

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
# They combine or flip True/False values.
#
#   A and B  -> True only if BOTH A and B are True
#   A or  B  -> True if AT LEAST ONE of A or B is True
#   not A    -> flips True to False and False to True

temperature = 22
is_raining = False

# and: every part must be True
if temperature > 15 and not is_raining:
    print("Good weather for a walk.")

# or: it's enough for one part to be True
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# not: invert a condition
logged_in = False
if not logged_in:
    print("Please log in first.")

# Truth table reference (read as: LEFT operator RIGHT -> result)
print(True  and False)  # False
print(True  or  False)  # True
print(not   True)       # False


# ---------------------------------------------------------------------------
# 4. SHORT-CIRCUIT EVALUATION (a useful detail of and / or)
# ---------------------------------------------------------------------------
# Python stops evaluating as soon as the answer is certain:
#   - with "and", if the first part is False the result must be False,
#     so the second part is never checked.
#   - with "or", if the first part is True the result must be True,
#     so the second part is never checked.
# This lets you guard against errors:

name = ""
# If name is empty, the left side is False, so name[0] is never reached
# and we avoid an "index out of range" crash.
if name != "" and name[0] == "A":
    print("Name starts with A")
else:
    print("No name, or it doesn't start with A")


# ---------------------------------------------------------------------------
# 5. CHAINED COMPARISONS
# ---------------------------------------------------------------------------
# Python lets you write a range check the way you would in math.

marks = 65
if 50 <= marks < 75:          # same as: marks >= 50 and marks < 75
    print("You passed, but there's room to improve.")


# ---------------------------------------------------------------------------
# 6. MEMBERSHIP OPERATORS: in / not in
# ---------------------------------------------------------------------------
# Check whether a value appears inside a string, list, tuple, or set.

vowels = ["a", "e", "i", "o", "u"]
letter = "e"

if letter in vowels:
    print(f"'{letter}' is a vowel")

if "z" not in vowels:
    print("'z' is not a vowel")

# Works on strings too (substring check):
sentence = "the quick brown fox"
if "quick" in sentence:
    print("Found the word 'quick'")


# ---------------------------------------------------------------------------
# 7. IDENTITY OPERATORS: is / is not
# ---------------------------------------------------------------------------
# "==" asks: are the two values equal?
# "is" asks: are they the exact same object in memory?
# In everyday code you almost always want "==", EXCEPT when comparing to None,
# where the convention is to use "is".

result = None
if result is None:
    print("No result yet")

if result is not None:
    print("We have a result")   # skipped, because result is None

# Why "is" can surprise you:
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  -> same contents
print(a is b)   # False -> two separate lists in memory


# ---------------------------------------------------------------------------
# 8. TRUTHY AND FALSY VALUES
# ---------------------------------------------------------------------------
# An if-condition doesn't have to be a real True/False. Python treats some
# values as "falsy" (act like False) and everything else as "truthy".
#
# Falsy: False, None, 0, 0.0, "" (empty string), [] {} () (empty containers)
# Truthy: basically everything else

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
# A one-line way to choose between two values.
# Form:  value_if_true if condition else value_if_false

age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult


# ---------------------------------------------------------------------------
# 10. PUTTING IT TOGETHER: a small login check
# ---------------------------------------------------------------------------
stored_user = "admin"
stored_pass = "1234"

entered_user = "admin"
entered_pass = "1234"
account_locked = False

if account_locked:
    print("Account is locked. Contact support.")
elif entered_user == stored_user and entered_pass == stored_pass:
    print("Login successful.")
elif entered_user == stored_user and entered_pass != stored_pass:
    print("Wrong password.")
else:
    print("Unknown user.")
