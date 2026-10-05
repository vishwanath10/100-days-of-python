"""
Day 6 Exercise 2 - Sum of Numbers (Beginner)
============================================
Ask the user for numbers again and again. Add each number to a running total.
Stop when the user enters 0, then print the total.
Example: the inputs 5, 10, 3, 0 print "Total: 18".
Practices: a running total, a "sentinel" value (0) that stops the loop.

Run me:  python "Day 6/exercise_2_sum_of_numbers.py"
"""

# Start the running total at 0.
total = 0

# Ask for the first number before the loop, so the condition has a value to test.
input_number = int(input("Enter a number to add to the total (enter 0 to stop): "))

# The value 0 is the "stop" signal. Any other number goes into the total.
while input_number != 0:
    total += input_number
    # Ask for the next number. If the user enters 0, the loop stops.
    input_number = int(input("Enter a number to add to the total (enter 0 to stop): "))

print("Total:", total)
