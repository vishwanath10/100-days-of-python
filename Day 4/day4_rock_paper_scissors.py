# Day 4 - Rock, Paper, Scissors
# =============================================================
# Uses the "random" module to pick the computer's move, and
# stores each hand shape as a multi-line string of ASCII art.
# =============================================================

import random


# -------------------------------------------------------------
# ASCII ART
# -------------------------------------------------------------
# Triple-quoted strings ( """ ... """ ) can span several lines,
# so the newlines you see below are stored inside the string.
# A leading "\n" adds one blank line before the drawing so the
# art does not stick to the text printed just above it.

rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose!")
else:
    print("You chose:\n" + game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{game_images[computer_choice]}")

    # Every possible pairing of user (0-2) and computer (0-2):
    #   equal values            -> draw
    #   0 vs 2 / 1 vs 0 / 2 vs 1 -> user wins
    #   everything else          -> user loses
    if user_choice == computer_choice:
        print("It's a draw.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("You lose.")