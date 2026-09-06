"""
Day 5 - Concepts: for loops, range(), and adding values with a loop
==================================================================
Run me:  python "Day 5/concepts.py"
Read each comment next to the line it explains.
"""

# ---------------------------------------------------------------------------
# 1. Looping over a list
# ---------------------------------------------------------------------------
# "for <item> in <list>:" runs the indented block once per item. Each time,
# <item> holds the current value.
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")       # this line also runs on every pass


# ---------------------------------------------------------------------------
# 2. Find the largest value by hand
# ---------------------------------------------------------------------------
# Keep a "largest so far" variable. Update it whenever you find a larger value.
scores = [150, 120, 185, 119, 91, 76]
highest = 0
for score in scores:
    if score > highest:
        highest = score
print(f"Highest score (manual): {highest}")


# ---------------------------------------------------------------------------
# 3. The built-in shortcuts: sum() and max()
# ---------------------------------------------------------------------------
print("sum():", sum(scores))
print("max():", max(scores))


# ---------------------------------------------------------------------------
# 4. Total a list by hand (the pattern behind sum())
# ---------------------------------------------------------------------------
total = 0
for score in scores:
    total += score              # total = total + score
print(f"Total (manual): {total}")


# ---------------------------------------------------------------------------
# 5. range() - make a sequence of numbers for a loop
# ---------------------------------------------------------------------------
# range(start, stop) counts from start up to BUT NOT INCLUDING stop.
# So range(1, 101) is 1, 2, 3, ... 100.
running_total = 0
for number in range(1, 101):
    running_total += number
print(f"Sum of 1..100: {running_total}")     # 5050
