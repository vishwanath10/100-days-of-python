"""
Day 4 - A tiny module, used by importing_modules.py
==================================================
A "module" is just another .py file. Another file can import this file. It
then gets the names defined here (functions and variables).
"""

import random

# A module-level variable. Python creates it ONCE, when another file first
# imports this file.
name = "dice roller"


def roll(sides=6):
    """Return a random integer from 1 to `sides` (both ends included)."""
    return random.randint(1, sides)


# Python runs this block only when you run this file directly
# (python "Day 4/dice.py"). Python does not run it on import. This is the
# standard way to make demo code run only on a direct run.
if __name__ == "__main__":
    print(f"{name}: {roll()}")
