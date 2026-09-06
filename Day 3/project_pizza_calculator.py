"""
Day 3 Project - Python Pizza Order Calculator
=============================================
Take a pizza order and total the bill from the customer's choices.
Practices: if / elif, logical operators (and, or), a running total.

Run me:  python "Day 3/project_pizza_calculator.py"
"""

print("Welcome to Python Pizza Deliveries!")

# Running total. We add to this after each choice, then print it at the end.
bill = 0

# This stays text because we compare it to letters like "S", not to numbers.
size = input("What size pizza do you want? S, M, or L = ")

# if / elif runs the FIRST matching block. If the user types anything other
# than S, M, or L, none of these run and the price stays 0.
if size == "S":
    bill += 15                  # bill += 15 is shorthand for bill = bill + 15
    print("Small pizza: $15")
elif size == "M":
    bill += 20
    print("Medium pizza: $20")
elif size == "L":
    bill += 25
    print("Large pizza: $25")

pepperoni = input("Do you want pepperoni? Y or N = ")

# "and" is True only when BOTH sides are True: they asked for pepperoni
# AND chose the small pizza.
if pepperoni == "Y" and size == "S":
    bill += 2
    print("Pepperoni on a small pizza: +$2")
# The brackets group the "or", so Python checks it first. Python then
# combines the result with the "and". Reads as:
# pepperoni is "Y" AND (size is "M" OR size is "L").
elif pepperoni == "Y" and (size == "M" or size == "L"):
    bill += 3
    print("Pepperoni on a medium or large pizza: +$3")

extra_cheese = input("Do you want extra cheese? Y or N = ")
if extra_cheese == "Y":
    bill += 1
    print("Extra cheese: +$1")

# The f-string puts the value of bill where {bill} appears.
print(f"Your final bill is: ${bill}")
