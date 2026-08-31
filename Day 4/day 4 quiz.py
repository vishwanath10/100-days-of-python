# Import the "random" module so we can use its random-number functions.
import random

# A list of five names. Each item has an index: Kevin=0, Karen=1, Jim=2, Oscar=3, Toby=4.
friends  = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# random.choice() picks one item from the list at random and returns it directly.
print(random.choice(friends))

# Doing the same thing manually:
# len(friends) is 5, so len(friends) - 1 is 4 (the last valid index).
# random.randint(0, 4) returns a random whole number from 0 to 4, including both ends.
random_index = random.randint(0, len(friends) - 1)

# Use that random number as an index to look up and print the matching name.
print(friends[random_index])

fruits = ["Strawberry", "Apple", "Banana", "Orange", "Grape"]
vegetables = ["Spinach", "Kale", "Tomato", "Potato", "Carrot"]

combined_list = [fruits, vegetables]
print(combined_list)


