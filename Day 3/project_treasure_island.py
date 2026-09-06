"""
Day 3 Project - Treasure Island
===============================
A text adventure that branches the story with nested if / elif / else.
Practises: nested conditionals, .lower() to normalise input, string joins.

Run me:  python "Day 3/project_treasure_island.py"
"""

print("Welcome to Treasure Island. Your mission is to find the treasure.")

# .lower() converts the answer to lowercase so "Left", "LEFT" and "left"
# are all treated the same way.
choice1 = input('You\'re at a cross road. Type "left" or "right": ').lower()

# Only "left" continues the adventure; anything else is a losing path.
if choice1 == "left":
    # The backslash (\) joins the string across lines so the long prompt
    # stays readable in the source code.
    choice2 = input("You come to a lake with an island in the middle. " \
                    "Type 'wait' to wait for a boat, " \
                    "'swim' to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("You reach the island. A house has 3 doors. " \
                        "Type 'red', 'blue' or 'yellow': ").lower()
        # Only the yellow door wins; the others end the game.
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You picked a door that doesn't exist. Game over.")
    else:
        # Reached when the player typed "swim" (or anything that isn't "wait").
        print("You get attacked by an angry trout. Game over.")
else:
    # Reached when the first answer wasn't "left".
    print("You fell into a hole. Game over.")
