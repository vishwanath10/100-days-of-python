"""
Day 6 Exercise 3 - Password Retry (Beginner to Easy-Medium)
===========================================================
The code keeps a secret password. The user has a maximum of 3 attempts to
guess it.
  - If the guess is correct, print "Access granted" and stop.
  - After each wrong guess, show the number of remaining attempts.
  - If the user uses all attempts, print "Account locked".
Practices: a counter in a while loop, break, nested if / else.

Run me:  python "Day 6/exercise_3_password_retry.py"
"""

secret_password = "python123"

max_attempts = 3
attempts = 0  # The number of wrong guesses so far.

while attempts < max_attempts:
    guess = input("Enter the password: ")

    if guess == secret_password:
        print("Access granted")
        # break stops the loop immediately. The user does not get more prompts.
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        # This nested if shows a different message after the last wrong guess.
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Account locked.")
