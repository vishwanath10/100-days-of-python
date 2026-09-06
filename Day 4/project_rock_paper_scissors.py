"""
Day 4 Project - Rock, Paper, Scissors
=====================================
Play one round against a random computer move.
Practises: the random module, lists as a lookup table, multi-line strings,
if / elif / else.

Run me:  python "Day 4/project_rock_paper_scissors.py"
"""

import random

# Triple-quoted strings can span several lines, so the newlines below are
# stored inside each string. The leading blank line keeps the art off the
# text printed just above it.
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

# The list acts as a lookup table: index 0 -> rock, 1 -> paper, 2 -> scissors.
game_images = [rock, paper, scissors]

user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

if user_choice < 0 or user_choice > 2:
    print("Invalid number - you lose!")
else:
    print("You chose:" + game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:" + game_images[computer_choice])

    # Every pairing of user (0-2) and computer (0-2):
    #   equal values             -> draw
    #   0 vs 2 / 1 vs 0 / 2 vs 1  -> user wins
    #   everything else           -> user loses
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
