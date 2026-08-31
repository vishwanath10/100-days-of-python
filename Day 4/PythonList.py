# Day 4 - Modifying a list
# Practises: index assignment, .append(), and .extend()

# A list of the 46 U.S. states in the order they joined the Union.
# Each item has a position (index) starting at 0.
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma"]

# Replace the item at index 1 ("Pennsylvania") with a new value.
states_of_america[1] = "Pencil"

# .append() adds ONE new item to the end of the list.
states_of_america.append("New State")

# .extend() adds several items at once by unpacking the list you pass in.
# (Using .append(["State 1", "State 2", "State 3"]) would instead add the
# whole list as a single nested item.)
states_of_america.extend(["State 1", "State 2", "State 3"])

print(states_of_america)
