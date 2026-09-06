"""
Day 5 Practice 1
100 Days of Code - Python Practice
Topics: loops, lists, conditionals, aggregation (sum/max), FizzBuzz
"""

# --- Basic print statement ---
print("Start small. Ship something.")

# --- Looping through a list of strings ---
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")   # concatenate string with each fruit name

print("end")


# --- Finding the maximum value manually (without built-in max()) ---
students_score = [150, 120, 185, 119, 91, 76]

max_score = 0
for score in students_score:
    if score > max_score:
        max_score = score

print(f"Maximum number is = {max_score}")


# --- Using built-in functions for sum and max ---
total_score = sum(students_score)
print(total_score)

max_score = max(students_score)
print(max_score)


# --- Calculating total manually using a loop ---
total_score = 0
for score in students_score:
    total_score += score

print(total_score)


# --- Summing numbers from 1 to 100 using range() ---
total_sum = 0

for number in range(1, 101):
    total_sum += number

print(total_sum)


# --- FizzBuzz challenge (1 to 100) ---
# Rules:
# - Multiple of 3 and 5 -> "FizzBuzz"
# - Multiple of 3 only  -> "Fizz"
# - Multiple of 5 only  -> "Buzz"
# - Otherwise           -> the number itself
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
