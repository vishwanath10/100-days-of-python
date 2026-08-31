# Day 3 - Control Flow and Logical Operators
# This program is a roller coaster ticketing system.
# It decides if you can ride, then calculates your ticket price.

# print() shows text on the screen.
print("Welcome to the roller coaster!")

# input() always returns a string (text), so we wrap it in int() to convert it
# into a whole number that we can compare with < and > below.
height = int(input("What is your height in cm? "))

# if / else lets the program choose between two paths.
# The block indented under "if" runs only when the condition is True.
if height < 120:
    print("You cannot ride the rollercoaster")
else:
    # This block runs when height is NOT less than 120 (i.e. 120 or taller).
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    # if / elif / else checks several conditions in order, top to bottom.
    # As soon as one is True, its block runs and the rest are skipped.
    if age < 12:
        bill = 5          # under 12
    elif age <= 18:
        bill = 7          # 12 to 18 (we only get here if age was NOT < 12)
    else:
        bill = 12         # 19 and older

    # An f-string (the f before the quotes) lets us drop a variable straight
    # into text by putting it inside { }.
    print(f"You have to pay ${bill}")

    wants_photo = input("Do you want to have a photo taken? Type Y for Yes and N for No. = ")

    # == checks if two values are equal. This comparison is case-sensitive,
    # so lowercase "y" would NOT match "Y".
    if wants_photo == "Y":
        # bill += 3 is shorthand for: bill = bill + 3
        bill += 3
        print("You have to pay an extra $3")

    print(f"Your total bill is ${bill}")


# --- Notes / earlier practice (kept as comments so they don't run) ---

# The modulo operator % gives the remainder of a division.
# 10 % 3 is 1, because 10 / 3 is 3 with a remainder of 1.
#print(10%3)

# Odd/even check: a number is even when dividing by 2 leaves no remainder.
#number_to_check = int(input("What is the number you want to check? "))
#if number_to_check % 2 == 0:
#    print("This is an even number.")
#else:
#    print("This is an odd number.")
