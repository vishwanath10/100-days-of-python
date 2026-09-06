"""
Day 1 Project - Band Name Generator
===================================
Ask the user two questions and join the answers into a band name.
Practices: print(), input(), string concatenation.

Run me:  python "Day 1/project_band_name_generator.py"
"""

print("Welcome to the Band Name Generator.")

# input() shows the prompt and waits for the user to type. It then returns
# the text the user entered. "\n" moves the cursor to a new line first.
city = input("Which city did you grow up in?\n")
pet = input("What is the name of a pet?\n")

# Build the final sentence by joining the fixed text with the two answers.
# The extra " " string adds a space between the city and the pet name.
print("Your band name could be " + city + " " + pet)
