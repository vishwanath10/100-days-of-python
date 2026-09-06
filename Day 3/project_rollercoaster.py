"""
Day 3 Project - Roller Coaster Ticketing
========================================
Decide whether the visitor can ride, then calculate the ticket price step
by step.
Practices: if / else, nested if / elif / else, == comparison, bill += n.

Run me:  python "Day 3/project_rollercoaster.py"
"""

print("Welcome to the roller coaster!")

# input() is text, so wrap it in int() to compare it with < and > below.
height = int(input("What is your height in cm? "))

# if / else chooses between two paths. The indented block under "if" runs
# only when the condition is True.
if height < 120:
    print("Sorry, you cannot ride the roller coaster.")
else:
    # Python runs this block when height is NOT less than 120 (that is, 120
    # or taller).
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))

    # if / elif / else checks conditions in order, top to bottom. As soon as
    # one is True, its block runs and Python skips the rest.
    if age < 12:
        bill = 5          # child
    elif age <= 18:
        bill = 7          # 12 to 18 (Python gets here only if age was not < 12)
    else:
        bill = 12         # adult

    print(f"Your ticket costs ${bill}.")

    wants_photo = input("Do you want a photo taken? Type Y for Yes, N for No: ")

    # == is case-sensitive, so lowercase "y" would NOT match "Y".
    if wants_photo == "Y":
        bill += 3         # shorthand for: bill = bill + 3
        print("A photo adds $3.")

    print(f"Your total bill is ${bill}.")
