"""
Day 2 - Concepts: data types, type casting, math, f-strings
==========================================================
Run me:  python "Day 2/concepts.py"
Read each comment next to the line it explains.
"""

# ---------------------------------------------------------------------------
# 1. Strings and indexing
# ---------------------------------------------------------------------------
# A string is a sequence of characters. Index [0] is the first character.
# Negative indexes count from the end, so [-1] is the last character.
print("Hello"[-1])          # prints "o"


# ---------------------------------------------------------------------------
# 2. Numbers: int, float, and readable separators
# ---------------------------------------------------------------------------
print(12 + 12)              # int addition -> 24
print(123_445_444)          # Python ignores the underscores. They aid reading.
print(4.4)                  # a float (a number with a decimal point)


# ---------------------------------------------------------------------------
# 3. Booleans and type()
# ---------------------------------------------------------------------------
print(True)                 # a boolean value: True or False
# type() tells you the data type of a value.
print(type(True))           # <class 'bool'>
print(type("Hello"))        # <class 'str'>
print(type(233.33))         # <class 'float'>
print(type(420))            # <class 'int'>


# ---------------------------------------------------------------------------
# 4. Type conversion (casting): int(), float(), str()
# ---------------------------------------------------------------------------
# "1" and "100" are strings. Add them without a change and Python joins them
# into "1100". Convert them to int first to add them as numbers.
print(int("1") + int("100"))    # -> 101

name_of_the_user = input("What is your name?\n")   # input() -> always str
length_of_name = len(name_of_the_user)            # len() -> always int

print(type(name_of_the_user))   # <class 'str'>
print(type(length_of_name))     # <class 'int'>

print("Hello " + name_of_the_user)
# str() turns a non-string into a string. Then you can join it with +.
print("Number of letters in your name: " + str(length_of_name))


# ---------------------------------------------------------------------------
# 5. Arithmetic operators
# ---------------------------------------------------------------------------
print(7 - 3)     # subtraction    -> 4
print(3 * 2)     # multiplication -> 6
print(6 / 3)     # true division  -> 2.0  (always a float)
print(6 // 3)    # floor division -> 2    (rounds to the lower whole number)
print(2 ** 3)    # exponent       -> 8    (2 to the power of 3)

# PEMDAS: Parentheses, Exponents, Multiply/Divide, Add/Subtract (left to right).
print(2 + 3 / 3 * 3 + 3 - 2)
# 3/3 = 1.0 -> 1.0*3 = 3.0 -> 2 + 3.0 + 3 - 2 = 6.0


# ---------------------------------------------------------------------------
# 6. round()
# ---------------------------------------------------------------------------
bmi = 84 / 1.65 ** 2        # weight(kg) / height(m) squared
print(bmi)                  # the full value, with no rounding
print(round(bmi))           # nearest whole number
print(round(bmi, 2))        # 2nd argument = number of decimal places


# ---------------------------------------------------------------------------
# 7. Assignment operators and f-strings
# ---------------------------------------------------------------------------
score = 0
score += 1                  # shorthand for: score = score + 1
# An f-string (an f before the quote) puts a variable directly into text
# through { }.
print(f"Your score is {score}")
