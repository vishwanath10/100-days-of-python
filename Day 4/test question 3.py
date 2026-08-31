# Day 4 - Nested lists and indexing
# Practises: putting a list inside a list, then reaching an item with [ ][ ]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen holds two items: the fruits list at index 0 and the
# vegetables list at index 1.
dirty_dozen = [fruits, vegetables]

# Read it left to right:
#   dirty_dozen[1]      -> the vegetables list
#   dirty_dozen[1][1]   -> item at index 1 of that list -> "Kale"
print(dirty_dozen[1][1])
