# Day 1 - Band Name Generator
# Practises: print(), input(), and joining strings with +

# print() displays a line of text on the screen.
print("Welcome to the Band Name Generator.")

# input() shows the prompt, waits for the user to type, then hands back
# whatever they typed as a string. The "\n" inside the prompt just moves
# the cursor to a new line so the user types below the question.
city = input("Which city did you grow up in?\n ")
pet = input("What is the name of a pet? \n")

# Build the final sentence by concatenating (joining) the fixed text with
# the two answers. The extra " " strings add spaces between the words.
print("Your band name could be " + city + " " + pet)
