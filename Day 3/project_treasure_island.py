"""
Day 3 Project - Treasure Island
===============================
A text adventure that branches the story with nested if / elif / else.
Practices: nested conditionals, .lower() to normalize input, string joins.

Run me:  python "Day 3/project_treasure_island.py"
"""

print("Welcome to Treasure Island. Your mission is to find the treasure.")

# .lower() changes the answer to lowercase. Python then treats "Left",
# "LEFT" and "left" the same way.
choice1 = input('You\'re at a cross road. Type "left" or "right": ').lower()

# Only "left" continues the adventure. Anything else is a losing path.
if choice1 == "left":
    # The backslash (\) joins the string across lines so the long prompt
    # stays readable in the source code.
    choice2 = input("You come to a lake with an island in the middle. " \
                    "Type 'wait' to wait for a boat, " \
                    "'swim' to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("You reach the island. A house has 3 doors. " \
                        "Type 'red', 'blue' or 'yellow': ").lower()
        # Only the yellow door wins. The other doors end the game.
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You picked a door that doesn't exist. Game over.")
    else:
        # Python runs this when the player typed "swim" (or anything that is
        # not "wait").
        print("You get attacked by an angry trout. Game over.")
else:
    # Python runs this when the first answer was not "left".
    print("You fell into a hole. Game over.")
