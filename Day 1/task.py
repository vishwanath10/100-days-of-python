# Day 1 - Greeting and string length
# Practises: input(), string concatenation, and the len() function

# Write your code below this line

# One-line version of the same idea, kept as a comment for reference:
# it feeds input() straight into print() without storing the name first.
# print("Hello " + input("Enter your name: ") + "!")

# Ask for the user's name. input() always returns a string.
name = input("Enter your name ")

# Join the greeting text with the name using +, then print it.
print("Hello " + name + "!")

# len() returns how many characters are in the string.
print(len(name))

# len() works on any string, not just user input.
firstname = "Vishwanath"
length = len(firstname)
print(length)
