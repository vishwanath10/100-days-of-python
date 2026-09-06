"""
Day 4 - Concepts: importing modules
===================================
Run me from inside the Day 4 folder so Python can find the local import:
    cd "Day 4"
    python importing_modules.py
"""

# ---------------------------------------------------------------------------
# 1. Import a module from Python's standard library
# ---------------------------------------------------------------------------
import random
print("stdlib random:", random.randint(1, 6))


# ---------------------------------------------------------------------------
# 2. Import your own file
# ---------------------------------------------------------------------------
# The import runs dice.py once, from top to bottom. You can then use its
# names through the "dice." prefix.
import dice
print("dice.name       :", dice.name)
print("dice.roll()     :", dice.roll())
print("dice.roll(20)   :", dice.roll(20))


# ---------------------------------------------------------------------------
# 3. Import only the names you need
# ---------------------------------------------------------------------------
# Now you can call "roll" directly, without the "dice." prefix.
from dice import roll
print("roll() directly :", roll())


# ---------------------------------------------------------------------------
# Notes
# ---------------------------------------------------------------------------
# - The first import creates a __pycache__/ folder with a compiled .pyc copy.
#   This makes later imports faster. You can delete the folder safely. This
#   repo git-ignores it.
# - Code under  if __name__ == "__main__":  in dice.py does NOT run on import.
#   It runs only when you run dice.py directly.
