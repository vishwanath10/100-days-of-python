"""
Day 4 - A tiny module, imported by importing_modules.py
======================================================
A "module" is just another .py file. Anything defined here (functions,
variables) becomes available to a file that imports it.
"""

import random

# A module-level variable. It is created ONCE, the moment this file is
# first imported.
name = "dice roller"


def roll(sides=6):
    """Return a random integer from 1 to `sides` (both ends included)."""
    return random.randint(1, sides)


# This block runs only when the file is executed directly
# (python "Day 4/dice.py"), NOT when it is imported. It is the standard
# way to keep a module's "demo" code from firing on import.
if __name__ == "__main__":
    print(f"{name}: {roll()}")
