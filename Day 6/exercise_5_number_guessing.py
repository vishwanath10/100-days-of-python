"""
Day 6 Exercise 5 - Number Guessing Game (Medium)
================================================
The program picks a random number from 1 to 50 with random.randint.
The user guesses until the guess is correct.
  - After each wrong guess, print "Too high" or "Too low".
  - At the end, print the number of attempts.
  - Bonus: the user can type q to quit. Text input does not crash the program.
Practices: while True, break, continue, str.isdigit(), the random module.

Run me:  python "Day 6/exercise_5_number_guessing.py"
"""

import random

# randint(1, 50) can return 1, 50, or any whole number between them.
secret_number = random.randint(1, 50)
attempts = 0

print("Guess the number between 1 and 50 (type q to quit)")

# "while True" repeats forever. A break statement stops the loop.
while True:
    # strip() removes spaces at the start and end. lower() changes "Q" to "q".
    user_input = input("Your guess: ").strip().lower()

    if user_input == "q":
        print("You quit, the number was", secret_number)
        break

    # isdigit() is True only when every character is a digit (0-9).
    # continue skips the rest of this pass and starts the next pass.
    # int() does not get text such as "abc", so the program does not crash.
    if not user_input.isdigit():
        print("Please enter a whole number or q.")
        continue

    # Change the text to a number. Python cannot compare text with a number.
    guess = int(user_input)
    attempts += 1

    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct you got it in", attempts, "attempts")
        break
