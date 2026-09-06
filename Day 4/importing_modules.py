"""
Day 4 - Concepts: importing modules
===================================
Run me from inside the Day 4 folder so the local import is found:
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
# Importing runs dice.py once, top to bottom, then gives you access to its
# names through the "dice." prefix.
import dice
print("dice.name       :", dice.name)
print("dice.roll()     :", dice.roll())
print("dice.roll(20)   :", dice.roll(20))


# ---------------------------------------------------------------------------
# 3. Import only the names you need
# ---------------------------------------------------------------------------
# Now "roll" can be called directly, without the "dice." prefix.
from dice import roll
print("roll() directly :", roll())


# ---------------------------------------------------------------------------
# Notes
# ---------------------------------------------------------------------------
# - The first import creates a __pycache__/ folder holding a compiled .pyc
#   copy so future imports are faster. It is safe to delete and is
#   git-ignored in this repo.
# - Code guarded by  if __name__ == "__main__":  in dice.py does NOT run on
#   import - only when dice.py is run directly.
