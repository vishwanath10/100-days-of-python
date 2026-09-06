"""
DAY 4 - THE random MODULE REFERENCE
==================================
"random" is part of Python's standard library, so there is nothing to
install. Import it once at the top of the file. Then call functions with
"random.xxx()".

The numbers it produces are "pseudo-random". They come from a math formula,
not from true physical randomness. For games, simulations, and learning
exercises, they are random enough.

Run me:  python "Day 4/random_reference.py"
"""

import random


# ---------------------------------------------------------------------------
# 1. random.randint(a, b)  ->  whole number (int), BOTH ends included
# ---------------------------------------------------------------------------
# randint(1, 6) can return 1, 2, 3, 4, 5, or 6.
random_integer = random.randint(a=100, b=105)   # any of 100..105
print(random_integer)

dice_roll = random.randint(1, 6)                # names are optional
print("You rolled a", dice_roll)


# ---------------------------------------------------------------------------
# 2. random.random()  ->  float from 0.0 up to (but not including) 1.0
# ---------------------------------------------------------------------------
print(random.random())

# Multiply the result to widen the range. Add a number to move it.
print(random.random() * 5)        # 0.0 up to (not including) 5.0
print(random.random() * 5 + 2)    # 2.0 up to (not including) 7.0


# ---------------------------------------------------------------------------
# 3. random.uniform(a, b)  ->  float between a and b
# ---------------------------------------------------------------------------
print(random.uniform(1, 10))


# ---------------------------------------------------------------------------
# 4. random.randrange(start, stop, step)  ->  int from a range
# ---------------------------------------------------------------------------
# Works like range(): "stop" is NOT included.
print(random.randrange(0, 10))          # 0..9
print(random.randrange(0, 101, 10))     # 0, 10, 20, ... 100


# ---------------------------------------------------------------------------
# 5. random.choice(sequence)  ->  one random item
# ---------------------------------------------------------------------------
foods = ["pizza", "sushi", "tacos", "pasta", "curry"]
print("Tonight we eat:", random.choice(foods))
print("Random letter:", random.choice("abcdefg"))   # a string is a sequence too

# Do the same thing manually with an index:
random_index = random.randint(0, len(foods) - 1)    # 0 .. last valid index
print("Manual pick:", foods[random_index])


# ---------------------------------------------------------------------------
# 6. random.choices(population, k=n)  ->  list of n items, WITH repeats
# ---------------------------------------------------------------------------
print("Three picks (repeats allowed):", random.choices(foods, k=3))

# weights change the odds. Here "heads" is 3 times as likely as "tails".
print("Weighted flip:", random.choices(["heads", "tails"], weights=[3, 1], k=1)[0])


# ---------------------------------------------------------------------------
# 7. random.sample(population, k=n)  ->  list of n items, NO repeats
# ---------------------------------------------------------------------------
print("Lottery numbers:", random.sample(range(1, 50), k=6))


# ---------------------------------------------------------------------------
# 8. random.shuffle(list)  ->  reorders a list IN PLACE
# ---------------------------------------------------------------------------
# It changes the original list and returns None, so do NOT write
# "cards = random.shuffle(cards)".
cards = ["A", "K", "Q", "J", "10"]
random.shuffle(cards)
print("Shuffled deck:", cards)


# ---------------------------------------------------------------------------
# 9. random.seed(number)  ->  make random numbers repeatable
# ---------------------------------------------------------------------------
# The same seed always produces the same sequence. This helps you reproduce
# a bug or a test result.
random.seed(42)
print(random.randint(1, 100))   # always 82 with seed 42
print(random.randint(1, 100))   # always 15 with seed 42
random.seed()                   # no argument -> seed again from the system clock


# ---------------------------------------------------------------------------
# 10. EXERCISE: heads or tails
# ---------------------------------------------------------------------------
# randint(0, 1) gives 0 or 1. Treat 1 as "Heads".
if random.randint(0, 1) == 1:
    print("Heads")
else:
    print("Tails")


# ---------------------------------------------------------------------------
# 11. MINI PRACTICE: flip a coin 10,000 times and check the split
# ---------------------------------------------------------------------------
# A fair coin should land heads roughly 50% of the time. If you run many
# trials and count the results, you can test that randint has no bias.
heads_count = 0
flips = 10_000
for _ in range(flips):
    if random.randint(0, 1) == 1:
        heads_count += 1
print(f"Heads {heads_count} / {flips}  ({heads_count / flips:.2%})")
