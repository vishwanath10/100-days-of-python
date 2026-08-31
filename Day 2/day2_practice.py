# ============================================================
# DAY 2 PYTHON PRACTICE
# ============================================================

# --- Strings and indexing ---
# Strings are sequences of characters. [-1] means "last character".
# Negative indexes count backwards from the end of the string.
print("Hello"[-1])          # prints "o" (the last letter of "Hello")

# --- Basic arithmetic ---
print(12+12)                # simple addition -> 24

# --- Underscores in numbers ---
# Python lets you use underscores as visual separators in large numbers.
# They're ignored by Python and only there for readability.
print(123_445_444)          # prints 123445444

# --- Float ---
print(4.4)                  # a floating point (decimal) number

# --- Booleans ---
print(True)                 # a boolean value (True/False)

# --- type() function ---
# type() tells you what kind of data a value is (its data type).
print(type(True))           # <class 'bool'>
print(type("Hello"))        # <class 'str'>   (string)
print(type(233.33))         # <class 'float'> (decimal number)
print(type(420))            # <class 'int'>   (whole number)

# --- Type conversion (casting) ---
# int() converts a value into an integer.
# Here both "1" and "100" are strings, so we must convert them to
# integers before we can add them numerically. Without int(), Python
# would just glue the strings together: "1" + "100" -> "1100".
print(int("1") + int("100"))   # prints 101

# --- Getting user input ---
# input() always returns a string, no matter what the user types.
name_of_the_user = input("What is your name?\n")

# len() gives the number of characters in a string.
length_of_name = len(name_of_the_user)

print(type(name_of_the_user))    # <class 'str'>  -> input() always returns string
print(type(length_of_name))      # <class 'int'>  -> len() always returns an integer

# --- String concatenation ---
# You can join ("concatenate") strings using +
print("Hello " + name_of_the_user)

# str() converts a non-string value into a string so it can be
# joined with other strings using +.
print("Number of letters in your name " + str(length_of_name))

# --- More arithmetic operators ---
print(7 - 3)     # subtraction -> 4
print(3 * 2)     # multiplication -> 6
print(6/3)       # true division -> 2.0 (always returns a float)
print(6//3)      # floor division -> 2 (rounds DOWN to nearest whole number, returns int-like value)
print(2**3)      # exponent (power) -> 2 to the power of 3 = 8

# --- PEMDAS in Python ---
# Python follows standard order of operations:
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
# (left to right for operators of the same priority)
print(2 + 3 / 3 * 3 + 3 - 2)
# Step by step: 3/3 = 1.0 -> 1.0*3 = 3.0 -> 2 + 3.0 + 3 - 2 = 6.0

# --- BMI calculation example ---
# Formula: weight (kg) / height (m) squared
bmi = 84 / 1.65 ** 2
print(bmi)                  # prints the raw, unrounded BMI value

# --- round() function ---
print(round(bmi))           # rounds to the nearest whole number
print(round(bmi,2))         # rounds to 2 decimal places (2nd argument = number of decimals)

# --- Variables and += operator ---
score = 0
score += 1                  # shorthand for: score = score + 1
print(f"Your score is {score}")   # f-string: lets you insert variables directly into a string using {}

# ============================================================
# TIP CALCULATOR
# ============================================================
print("Welcome to the tip calculator!")

# input() always returns strings, so raw user input can't be used
# directly in math yet - it needs to be converted first.
total_bill = input("What was the total bill? = $")
tip = input("How much tip would you like to give? = ")
total_person_split = input("How many people to split the bill? = ")

# Breaking down the calculation:
# 1. int(tip) / float(100.0)   -> converts tip percentage (e.g. 15) into a decimal (0.15)
# 2. that decimal * float(total_bill) -> calculates the actual tip amount in currency
# 3. float(total_bill) + tip_amount   -> adds tip on top of the original bill
# 4. divide the whole total by float(total_person_split) -> splits the final amount evenly
each_person_pay = (float(total_bill) + ((int(tip) / float(100.0)) * float(total_bill))) / float(total_person_split)

# f-string again: inserts the calculated variable into the printed sentence
print(f"Each person should pay {each_person_pay}")
