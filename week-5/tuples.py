# Sample tuple
my_tuple = (1, 2, 3, "apple", "banana", 2, "apple")

# 1. len(my_tuple) - Returns the number of elements in the tuple.
tuple_length = len(my_tuple)
print(f"Number of elements in the tuple: {tuple_length}")

# 2. my_tuple.index(element) - Returns the index of the first occurrence of the specified element.
element_index = my_tuple.index("apple")
print(f"Index of the first occurrence of 'apple': {element_index}")

# 3. my_tuple.count(element) - Returns the number of occurrences of the specified element in the tuple.
element_count = my_tuple.count(2)
print(f"Number of occurrences of '2': {element_count}")

# Attempting to modify a tuple (Immutable - Will raise an error)
my_tuple[0] = 10

# Creating a new tuple with updated elements (Reassigning)
new_tuple = my_tuple + (4, 5, "cherry")
print(f"New tuple after adding elements: {new_tuple}")
