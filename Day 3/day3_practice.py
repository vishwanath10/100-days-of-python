# Treasure Island - a text-based adventure game that uses nested if/else
# statements to branch the story based on the player's choices.

# Intro message shown to the player when the game starts.
print("Welcome to Treasure Island. Your mission is to find the treasure.")

# First decision point. input() pauses the program and waits for the player
# to type something; .lower() converts their answer to lowercase so that
# "Left", "LEFT" and "left" are all treated the same way.
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" = ').lower()

# Only "left" continues the adventure; anything else is a losing path.
if choice1 == "left":
    # Second decision point. The backslash (\) at the end of each line joins
    # the string across multiple lines so the long prompt stays readable.
    choice2 = input("You have come to the a lake there is and island in the middle of the lake. " \
                    "Type 'wait' to wait for a boat. " \
                    "Type 'swim' to swim across. = ").lower()
    if choice2 == "wait":
        # Third decision point: pick one of the three doors.
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. " \
                        "Type 'red' to enter the red door. " \
                        "Type 'blue' to enter the blue door. " \
                        "Type 'yellow' to enter the yellow door. = ").lower()
        # Only the yellow door wins; the other two doors end the game.
        if choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        # (Typing anything other than red/blue/yellow ends the program with no message.)
    else:
        # Reached when the player typed "swim" (or anything that isn't "wait").
        print("You get attacked by an angry trout. Game Over.")
else:
    # Reached when the player's first answer wasn't "left".
    print("You fell into a hole. Game Over.")
