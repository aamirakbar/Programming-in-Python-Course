# Sample set
my_set = {1, 2, 3, 4, 5}

# 1. len(my_set) - Returns the number of elements in the set.
set_length = len(my_set)
print(f"Number of elements in the set: {set_length}")

# 2. element in my_set - Checks if an element is present in the set (returns a boolean).
is_present = 3 in my_set
print(f"Is 3 present in the set? {is_present}")

# 3. my_set.add(element) - Adds an element to the set.
my_set.add(6)
print(f"Set after adding 6: {my_set}")

# 4. my_set.remove(element) - Removes the specified element from the set (raises an error if not found).
#my_set.remove(7)

# 5. my_set.discard(element) - Removes the specified element from the set (no error if not found).
my_set.discard(4)
print(f"Set after discarding 4: {my_set}")
