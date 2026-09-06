"""
Day 4 - Concepts: lists, list methods, nested (2D) lists
=======================================================
Run me:  python "Day 4/lists.py"
Read each comment next to the line it explains.
"""

# ---------------------------------------------------------------------------
# 1. Creating and indexing a list
# ---------------------------------------------------------------------------
# A list holds an ordered collection of items inside [ ]. Each item has a
# position (index) that starts at 0.
fruits = ["Apple", "Peach", "Pear", "Grape"]
print(fruits[0])        # "Apple"  -> first item
print(fruits[2])        # "Pear"   -> third item
print(fruits[-1])       # "Grape"  -> last item (negative indexes count from the end)
print(len(fruits))      # 4        -> number of items


# ---------------------------------------------------------------------------
# 2. Changing items
# ---------------------------------------------------------------------------
fruits[1] = "Banana"    # replace the item at index 1
print(fruits)           # ["Apple", "Banana", "Pear", "Grape"]


# ---------------------------------------------------------------------------
# 3. Adding items: append() and extend()
# ---------------------------------------------------------------------------
fruits.append("Mango")             # append() adds ONE item to the end
print(fruits)

fruits.extend(["Kiwi", "Melon"])   # extend() adds SEVERAL items, one by one
print(fruits)

# Warning: append(a_list) nests the whole list as one item.
fruits.append(["x", "y"])
print(fruits[-1])                   # ["x", "y"]  -> a list inside the list
fruits.pop()                        # remove that last item again


# ---------------------------------------------------------------------------
# 4. Nested lists (a "2D" list - a list of lists)
# ---------------------------------------------------------------------------
row_fruits = ["Strawberry", "Apple", "Banana"]
row_veg = ["Spinach", "Kale", "Tomato"]

grocery = [row_fruits, row_veg]     # a list whose items are themselves lists
print(grocery)

# Index twice. First pick the inner list. Then pick an item from that list.
print(grocery[0])       # ["Strawberry", "Apple", "Banana"]
print(grocery[1][0])    # "Spinach"  -> inner list 1, item 0
print(grocery[0][2])    # "Banana"   -> inner list 0, item 2
