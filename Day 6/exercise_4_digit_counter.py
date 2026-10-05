"""
Day 6 Exercise 4 - Digit Counter and Sum (Medium)
=================================================
Ask for a positive integer. Use a while loop to count its digits and
calculate their sum. Do not convert the number to a string.
Example: 4729 prints "Digits: 4" and "Total Sum: 22".
Practices: % 10 (get the last digit), // 10 (remove the last digit).

Run me:  python "Day 6/exercise_4_digit_counter.py"
"""

number = int(input("Enter a positive integer: "))

# Ask again until the number is not negative.
while number < 0:
    number = int(input("That is a negative number. Enter a positive number: "))

digit_count = 0
digit_sum = 0

# The loop below does not run for 0, but 0 has 1 digit. Count it here.
if number == 0:
    digit_count = 1
else:
    # Each pass takes the last digit off the number.
    # Example for 4729: 9, then 2, then 7, then 4. Then number is 0.
    while number > 0:
        last_digit = number % 10   # 4729 % 10 is 9.
        digit_sum += last_digit
        digit_count += 1
        number = number // 10      # 4729 // 10 is 472.

print("Digits:", digit_count)
print("Total Sum:", digit_sum)
