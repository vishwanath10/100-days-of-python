import random

# ============================================================
# THE random MODULE
# ------------------------------------------------------------
# "random" is part of Python's standard library, so there is
# nothing to install. You just "import random" once at the top
# of the file and then call functions on it with "random.xxx()".
#
# The numbers it produces are "pseudo-random": they come from a
# math formula, not from true physical randomness, but for games,
# simulations, and learning exercises they behave randomly enough.
# ============================================================


# ------------------------------------------------------------
# 1. random.randint(a, b)  ->  whole number (int)
# ------------------------------------------------------------
# Returns a random integer N where a <= N <= b.
# BOTH ends are included, so randint(1, 6) can return 1, 2, 3, 4, 5, or 6.
random_integer = random.randint(a=100, b=105)  # any of 100,101,102,103,104,105
print(random_integer)

# You do not have to name the arguments. This is the same thing:
dice_roll = random.randint(1, 6)
print("You rolled a", dice_roll)


# ------------------------------------------------------------
# 2. random.random()  ->  float from 0.0 up to (but not including) 1.0
# ------------------------------------------------------------
# Takes no arguments. The result is >= 0.0 and < 1.0.
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# Trick: multiply the 0-1 value to stretch it into a bigger range.
# random.random() * 5  -> float from 0.0 up to (not including) 5.0
random_float_0_to_5 = random.random() * 5
print(random_float_0_to_5)

# Add an offset to shift the range.
# This gives a float from 2.0 up to (not including) 7.0
random_float_2_to_7 = random.random() * 5 + 2
print(random_float_2_to_7)


# ------------------------------------------------------------
# 3. random.uniform(a, b)  ->  float between a and b
# ------------------------------------------------------------
# Like random.random(), but you pick the range directly instead
# of multiplying. Returns a float N where a <= N <= b.
random_float = random.uniform(1, 10)
print(random_float)


# ------------------------------------------------------------
# 4. random.randrange(start, stop, step)  ->  int from a range
# ------------------------------------------------------------
# Works like the built-in range(): "stop" is NOT included.
# randrange(0, 10) -> 0..9
random_from_range = random.randrange(0, 10)
print(random_from_range)

# With a step, you only get values that land on the step.
# randrange(0, 101, 10) -> 0, 10, 20, 30, ... 100
random_multiple_of_10 = random.randrange(0, 101, 10)
print(random_multiple_of_10)


# ------------------------------------------------------------
# 5. random.choice(sequence)  ->  one random item from a list/string/tuple
# ------------------------------------------------------------
foods = ["pizza", "sushi", "tacos", "pasta", "curry"]
dinner = random.choice(foods)
print("Tonight we eat:", dinner)

# It also works on a string (a string is a sequence of characters).
random_letter = random.choice("abcdefg")
print("Random letter:", random_letter)


# ------------------------------------------------------------
# 6. random.choices(population, k=n)  ->  list of n items, WITH repeats
# ------------------------------------------------------------
# Good for "draw n times, putting each pick back in the bag".
three_foods = random.choices(foods, k=3)
print("Three picks (repeats allowed):", three_foods)

# You can bias the outcome with weights. Here "heads" is 3x as likely.
weighted_flip = random.choices(["heads", "tails"], weights=[3, 1], k=1)
print("Weighted flip:", weighted_flip[0])


# ------------------------------------------------------------
# 7. random.sample(population, k=n)  ->  list of n items, NO repeats
# ------------------------------------------------------------
# Good for "deal a hand" or "pick 6 lottery numbers": each item
# can be chosen at most once.
lottery_numbers = random.sample(range(1, 50), k=6)
print("Lottery numbers:", lottery_numbers)


# ------------------------------------------------------------
# 8. random.shuffle(list)  ->  reorders a list IN PLACE
# ------------------------------------------------------------
# Important: it changes the original list and returns None,
# so do NOT write "cards = random.shuffle(cards)".
cards = ["A", "K", "Q", "J", "10"]
random.shuffle(cards)
print("Shuffled deck:", cards)


# ------------------------------------------------------------
# 9. random.seed(number)  ->  make randomness repeatable
# ------------------------------------------------------------
# Seeding "resets" the generator to a known starting point, so the
# same seed always produces the same sequence. This is very handy
# when you want to reproduce a bug or a test result.
random.seed(42)
print(random.randint(1, 100))  # always 82 with seed 42
print(random.randint(1, 100))  # always 15 with seed 42
random.seed()  # calling with no argument re-randomizes from the system clock


# ============================================================
# ORIGINAL EXERCISE: heads or tails
# ------------------------------------------------------------
# randint(0, 1) gives either 0 or 1. We treat 1 as "Heads".
# ============================================================
random_heads_or_tails = random.randint(a=0, b=1)
if random_heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")


# ------------------------------------------------------------
# MINI PRACTICE: flip a coin 10,000 times and check the split
# ------------------------------------------------------------
# A fair coin should land heads roughly 50% of the time. Running
# many trials and counting is a simple way to sanity-check that
# random.randint really is unbiased.
heads_count = 0
flips = 10000
for _ in range(flips):
    if random.randint(0, 1) == 1:
        heads_count += 1
print(f"Heads {heads_count} / {flips}  ({heads_count / flips:.2%})")
