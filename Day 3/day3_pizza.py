# Day 3 - Python Pizza order calculator
# Practises: if / elif, logical operators (and, or), and a running total.

print("Welcome to Python Pizza Deliveries!")

# Running total. We keep adding to this as the customer makes choices,
# then print it at the end.
bill = 0

# input() returns a string. We keep it as text because we compare it to
# letters like "S", not to numbers.
size = input("What size pizza do you want? S, M, or L = ")

# if / elif runs the FIRST matching block. If the user types anything
# other than S, M, or L, none of these run and the price stays 0.
if size == "S":
    bill += 15                      # bill += 15 is shorthand for bill = bill + 15
    print("Small size Pizza is for $15")
elif size == "M":
    bill += 20
    print("Medium size Pizza is for $20")
elif size == "L":
    bill += 25
    print("Large size Pizza is for $25")

pepperoni = input("Do you want pepperoni? Y or N = ")

# "and" is True only when BOTH sides are True: they must have asked for
# pepperoni AND chosen the small pizza.
if pepperoni == "Y" and size == "S":
    bill += 2
    print("You have to pay an extra $2 for pepperoni on small size pizza")
# The brackets group the "or" so it is checked first, then combined with
# the "and". Reads as: pepperoni is "Y" AND (size is "M" OR size is "L").
elif pepperoni == "Y" and (size == "M" or size == "L"):
    bill += 3
    print("You have to pay an extra $3 for pepperoni on medium or large size pizza")

extra_cheese = input("Do you want extra cheese? Y or N = ")
# This message prints even when the answer is N - ideally it would sit
# inside the if block below.
print("You have to pay an extra $1 for extra cheese")

if extra_cheese == "Y":
    bill += 1

# f-string: the value of bill is inserted where {bill} appears.
print(f"Your final bill is: ${bill}")
