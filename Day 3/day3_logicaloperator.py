# Day 3 - Logical Operators in Python
# =====================================
# Python has 3 logical operators:  and   or   not
# They combine or flip True/False (boolean) values.
# Run this file top to bottom and read the printed output next to each example.


# -------------------------------------------------------------------
# 1. The building blocks: comparisons produce booleans (True / False)
# -------------------------------------------------------------------
print("---- Section 1: comparisons ----")
print(5 > 3)        # True
print(5 < 3)        # False
print(5 == 5)       # True   ( == means "is equal to" )
print(5 != 5)       # False  ( != means "is NOT equal to" )
print(5 >= 5)       # True
print(5 <= 4)       # False
print()


# -------------------------------------------------------------------
# 2. "and"  ->  True only when BOTH sides are True
# -------------------------------------------------------------------
# Think: "Do I need BOTH things to be true?"
print("---- Section 2: and ----")
print(True  and True)    # True
print(True  and False)   # False
print(False and True)    # False
print(False and False)   # False

age = 25
has_ticket = True
# Person can enter only if they are an adult AND they have a ticket.
can_enter = age >= 18 and has_ticket
print("can_enter:", can_enter)   # True
print()


# -------------------------------------------------------------------
# 3. "or"  ->  True when AT LEAST ONE side is True
# -------------------------------------------------------------------
# Think: "Is it enough for just ONE thing to be true?"
print("---- Section 3: or ----")
print(True  or True)     # True
print(True  or False)    # True
print(False or True)     # True
print(False or False)    # False

is_weekend = False
is_holiday = True
# You can sleep in if it's the weekend OR a holiday.
can_sleep_in = is_weekend or is_holiday
print("can_sleep_in:", can_sleep_in)   # True
print()


# -------------------------------------------------------------------
# 4. "not"  ->  flips the value (True becomes False, False becomes True)
# -------------------------------------------------------------------
print("---- Section 4: not ----")
print(not True)     # False
print(not False)    # True

is_raining = False
print("Go for a walk?", not is_raining)   # True  (not raining -> yes)
print()


# -------------------------------------------------------------------
# 5. Combining them - use brackets ( ) to make the order clear
# -------------------------------------------------------------------
# Precedence (order Python applies them):  not  ->  and  ->  or
# When unsure, add brackets so it reads the way you mean it.
print("---- Section 5: combining ----")

age = 20
country = "UK"

# Allowed if: adult AND from the UK or the US
allowed = age >= 18 and (country == "UK" or country == "US")
print("allowed:", allowed)   # True

x = 7
# Is x between 5 and 10 (inclusive)?  Both comparisons must hold.
in_range = x >= 5 and x <= 10
print("in_range:", in_range)  # True

# Python shortcut for the same idea - you can "chain" comparisons:
print("chained:", 5 <= x <= 10)  # True
print()


# -------------------------------------------------------------------
# 6. Truthy / Falsy - non-boolean values also count as True or False
# -------------------------------------------------------------------
# Falsy values:  0   0.0   ""(empty string)   []   {}   None
# Everything else is Truthy.
print("---- Section 6: truthy / falsy ----")
name = ""
if name:
    print("Name was given")
else:
    print("Name is empty")     # this runs, because "" is falsy

items = [1, 2, 3]
if items:
    print("List has", len(items), "items")   # runs, non-empty list is truthy
print()


# -------------------------------------------------------------------
# 7. Short-circuit evaluation (how Python stops early)
# -------------------------------------------------------------------
# "and": if the first part is False, Python already knows the whole thing
#        is False, so it never checks the second part.
# "or" : if the first part is True, Python stops - the result is True.
print("---- Section 7: short-circuit ----")

def check():
    print("  check() was called")
    return True

print("Testing 'and' with False first:")
result = False and check()   # check() is NOT called
print("  result:", result)

print("Testing 'or' with True first:")
result = True or check()     # check() is NOT called
print("  result:", result)
print()


# -------------------------------------------------------------------
# 8. PRACTICE - fill in the blanks, then run to check your answers
# -------------------------------------------------------------------
# Uncomment each block, write your condition, and see if it prints "Correct!".
print("---- Section 8: practice ----")

# Practice 1: A user can drive if they are 18 or older AND have a license.
user_age = 19
has_license = True
# TODO: replace False with your condition using "and"
can_drive = False
print("Practice 1:", "Correct!" if can_drive == (user_age >= 18 and has_license) else "Try again")

# Practice 2: Entry is free if you are under 5 OR 65 and over.
visitor_age = 70
# TODO: replace False with your condition using "or"
free_entry = False
print("Practice 2:", "Correct!" if free_entry == (visitor_age < 5 or visitor_age >= 65) else "Try again")

# Practice 3: A seat is available if it is NOT booked.
is_booked = False
# TODO: replace False with your condition using "not"
seat_available = False
print("Practice 3:", "Correct!" if seat_available == (not is_booked) else "Try again")

# Practice 4: A number n passes if it is between 1 and 100 (inclusive)
#             AND it is even.  (even means n % 2 == 0)
n = 42
# TODO: replace False with your condition
passes = False
print("Practice 4:", "Correct!" if passes == (1 <= n <= 100 and n % 2 == 0) else "Try again")
