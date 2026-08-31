print("Welcome to Python Pizza Deliveries!")

bill = 0

size = input("What size pizza do you want? S, M, or L = ")

if size == "S":
    bill += 15
    print("Small size Pizza is for $15")
elif size == "M":
    bill += 20
    print("Medium size Pizza is for $20")
elif size == "L":
    bill += 25
    print("Large size Pizza is for $25")

pepperoni = input("Do you want pepperoni? Y or N = ")

if pepperoni == "Y" and size == "S":
    bill += 2
    print("You have to pay an extra $2 for pepperoni on small size pizza")
elif pepperoni == "Y" and (size == "M" or size == "L"):
    bill += 3
    print("You have to pay an extra $3 for pepperoni on medium or large size pizza")

extra_cheese = input("Do you want extra cheese? Y or N = ")
print("You have to pay an extra $1 for extra cheese")

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")