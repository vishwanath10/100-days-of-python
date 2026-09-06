"""
Day 1 - Concepts: printing, strings, variables, input, len()
===========================================================
Run me:  python "Day 1/concepts.py"
Read each comment next to the line it explains.
"""

# ---------------------------------------------------------------------------
# 1. print() - show text on the screen
# ---------------------------------------------------------------------------
print("Hello, world!")          # text inside quotation marks is a "string"
print("Line one")
print("Line two")               # every print() call starts on a new line

# "\n" inside a string is a manual line break (a "newline" character).
print("First line\nSecond line")


# ---------------------------------------------------------------------------
# 2. String concatenation - join strings with +
# ---------------------------------------------------------------------------
# Both sides of + must be strings. A space appears only where you put one.
print("Hello " + "Angela" + "!")


# ---------------------------------------------------------------------------
# 3. Variables - a name that stores a value for later
# ---------------------------------------------------------------------------
first_name = "Vishwanath"       # store a string in a variable
print("Hi " + first_name)

# You can give a variable a new value at any time. Python keeps the most
# recent value.
first_name = "Vish"
print("Hi " + first_name)


# ---------------------------------------------------------------------------
# 4. input() - read one line typed by the user
# ---------------------------------------------------------------------------
# input() prints the prompt and waits for Enter. It then returns your text,
# always as a string. The "\n" puts the cursor on its own line.
name = input("What is your name?\n")
print("Hello " + name + "!")


# ---------------------------------------------------------------------------
# 5. len() - count the characters in a string
# ---------------------------------------------------------------------------
# len() returns an int (a whole number).
print(len(name))                # length of the text the user typed
print(len("Vishwanath"))        # -> 10
