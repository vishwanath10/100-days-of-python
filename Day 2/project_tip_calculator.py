"""
Day 2 Project - Tip Calculator
==============================
Split a restaurant bill (including tip) evenly between people.
Practises: input() + type casting, arithmetic, f-strings.

Run me:  python "Day 2/project_tip_calculator.py"
"""

print("Welcome to the tip calculator!")

# input() returns strings, so these must be converted before doing math.
total_bill = input("What was the total bill? = $")
tip = input("What percentage tip would you like to give? (e.g. 10, 12, 15) = ")
people = input("How many people to split the bill? = ")

# Step by step:
#   1. int(tip) / 100          -> tip percentage as a decimal (15 -> 0.15)
#   2. * float(total_bill)     -> the tip amount in currency
#   3. + float(total_bill)     -> bill plus tip
#   4. / int(people)           -> split evenly between everyone
tip_as_decimal = int(tip) / 100
bill_with_tip = float(total_bill) + float(total_bill) * tip_as_decimal
each_person_pays = bill_with_tip / int(people)

# round(..., 2) keeps it to 2 decimal places, like real money.
print(f"Each person should pay: ${round(each_person_pays, 2)}")
