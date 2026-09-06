"""
Day 1 - Concepts: printing, strings, variables, input, len()
===========================================================
Run me:  python "Day 1/concepts.py"
Read each comment next to the line it explains.
"""

# ---------------------------------------------------------------------------
# 1. print() - show text on the screen
# ---------------------------------------------------------------------------
print("Hello, world!")          # text wrapped in quotes is a "string"
print("Line one")
print("Line two")               # every print() call starts on a new line

# "\n" inside a string is a manual line break (a "newline" character).
print("First line\nSecond line")


# ---------------------------------------------------------------------------
# 2. String concatenation - glue strings together with +
# ---------------------------------------------------------------------------
# Both sides of + must be strings. Spaces only appear if you put them there.
print("Hello " + "Angela" + "!")


# ---------------------------------------------------------------------------
# 3. Variables - a name that stores a value for later
# ---------------------------------------------------------------------------
first_name = "Vishwanath"       # store a string in a variable
print("Hi " + first_name)

# A variable can be reassigned at any time; the most recent value wins.
first_name = "Vish"
print("Hi " + first_name)


# ---------------------------------------------------------------------------
# 4. input() - read one line typed by the user
# ---------------------------------------------------------------------------
# input() prints the prompt, waits for Enter, and hands back what was typed
# ALWAYS as a string. The "\n" pushes the cursor onto its own line.
name = input("What is your name?\n")
print("Hello " + name + "!")


# ---------------------------------------------------------------------------
# 5. len() - count the characters in a string
# ---------------------------------------------------------------------------
# len() returns an int (a whole number).
print(len(name))                # length of whatever the user typed
print(len("Vishwanath"))        # -> 10
