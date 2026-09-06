"""
Day 5 - Concepts: for loops, range(), and aggregating with a loop
================================================================
Run me:  python "Day 5/concepts.py"
Read each comment next to the line it explains.
"""

# ---------------------------------------------------------------------------
# 1. Looping over a list
# ---------------------------------------------------------------------------
# "for <item> in <list>:" runs the indented block once per item, with <item>
# holding the current value each time round.
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")       # this line also runs on every pass


# ---------------------------------------------------------------------------
# 2. Finding a maximum by hand
# ---------------------------------------------------------------------------
# Keep a "best so far" variable, and update it whenever you see something bigger.
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
# 4. Adding up a list by hand (the pattern behind sum())
# ---------------------------------------------------------------------------
total = 0
for score in scores:
    total += score              # total = total + score
print(f"Total (manual): {total}")


# ---------------------------------------------------------------------------
# 5. range() - generate a sequence of numbers to loop over
# ---------------------------------------------------------------------------
# range(start, stop) counts from start up to BUT NOT INCLUDING stop.
# So range(1, 101) is 1, 2, 3, ... 100.
running_total = 0
for number in range(1, 101):
    running_total += number
print(f"Sum of 1..100: {running_total}")     # 5050
