"""
Day 6 Exercise 1 - Countdown (Beginner)
=======================================
Ask the user for a positive integer. Count down to 1, then print "Liftoff!".
Example: the input 3 prints 3, 2, 1, Liftoff!
Practices: input validation with while, a countdown with while.

Run me:  python "Day 6/exercise_1_countdown.py"
"""

print("Welcome to Exercise 1 - While Loop Practice!")

count = int(input("Please enter a positive integer to start the countdown: "))

# Loop 1: Ask again until the user gives a number that is more than 0.
while count <= 0:
    print("Please enter a positive integer.")
    count = int(input("Please enter a positive integer to start the countdown: "))

# Loop 2: Print the number, then make it 1 less.
# When count becomes 0, the condition is False and the loop stops.
while count > 0:
    print(count)
    count -= 1

print("Liftoff!")
