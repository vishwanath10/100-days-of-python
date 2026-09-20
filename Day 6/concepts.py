"""
Day 6 - Concepts: functions, while loops, and conditional statements
====================================================================
Run me:  python "Day 6/concepts.py"
Read each comment next to the line it explains.
"""

# ---------------------------------------------------------------------------
# 1. Functions and return values
# ---------------------------------------------------------------------------
# len() is a built-in function. It returns the number of characters in a string.
message = "Hello, World!"
number_of_characters = len(message)
print(f"Number of characters: {number_of_characters}")


# Define a function once. Call it whenever you want to run its instructions.
def say_goodbye():
    """Print a short goodbye message."""
    print("This is my function.")
    print("Bye")


say_goodbye()


# ---------------------------------------------------------------------------
# 2. Count up and count down with while
# ---------------------------------------------------------------------------
# A while loop runs while its condition is True.
number = 1
while number <= 5:
    print(number)
    # Update number. Without this line, the loop would never stop.
    number += 1

countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Go!")


# ---------------------------------------------------------------------------
# 3. Use not to reverse a Boolean value
# ---------------------------------------------------------------------------
game_over = False

# "not game_over" means "the game is not over".
while not game_over:
    print("The game is running.")
    game_over = True  # Change the condition so the loop stops.

print("The game is over.")


# An empty list is False in a condition. "not tasks" is True when it is empty.
tasks = []
while not tasks:
    print("There are no tasks yet.")
    tasks.append("Learn while loops")

print(tasks)


# ---------------------------------------------------------------------------
# 4. while with if, elif, else, and nested if statements
# ---------------------------------------------------------------------------
# Use an index to get one item from the list on each loop pass.
numbers = [4, -2, 0]
index = 0

while index < len(numbers):
    current_number = numbers[index]

    if current_number > 0:
        # This nested if checks whether a positive number is even or odd.
        if current_number % 2 == 0:
            print(f"{current_number} is a positive even number.")
        else:
            print(f"{current_number} is a positive odd number.")
    elif current_number < 0:
        print(f"{current_number} is a negative number.")
    else:
        print("The number is zero.")

    index += 1


# Give a grade for each score. Python uses "elif", not "elseif".
scores = [95, 72, 48]
index = 0

while index < len(scores):
    score = scores[index]

    if score >= 90:
        print(f"{score}: Grade A")
    elif score >= 60:
        # This nested if separates passing scores into two grade groups.
        if score >= 75:
            print(f"{score}: Grade B")
        else:
            print(f"{score}: Grade C")
    else:
        print(f"{score}: You need more practice.")

    index += 1


# Check access based on a person's age and membership status.
people = [(12, False), (16, True), (21, False)]
index = 0

while index < len(people):
    age, is_member = people[index]

    if age >= 18:
        if is_member:
            print("Adult member: free entry.")
        else:
            print("Adult visitor: buy a ticket.")
    elif age >= 13:
        print("Teenager: enter with an adult.")
    else:
        print("Child: entry is not available.")

    index += 1
