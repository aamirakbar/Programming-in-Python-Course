# Sample list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 1. len(my_list) - Returns the number of elements in the list.
list_length = len(my_list)
print(f"Number of elements in the list: {list_length}")

# 2. my_list.append(element) - Adds an element to the end of the list.
my_list.append(7)
print(f"List after appending 7: {my_list}")

# 3. my_list.insert(index, element) - Inserts an element at the specified index.
my_list.insert(3, 8)
print(f"List after inserting 8 at index 3: {my_list}")

# 4. my_list.remove(element) - Removes the first occurrence of the specified element.
my_list.remove(5)
print(f"List after removing the first occurrence of 5: {my_list}")

# 5. my_list.pop(index) - Removes and returns the element at the specified index (or the last element if index is not provided).
popped_element = my_list.pop(2)
print(f"Popped element at index 2: {popped_element}, List after popping: {my_list}")

# 6. my_list.index(element) - Returns the index of the first occurrence of the specified element (or raises an error if not found).
element_index = my_list.index(9)
print(f"Index of the first occurrence of 9: {element_index}")

# 7. my_list.count(element) - Returns the number of occurrences of the specified element in the list.
element_count = my_list.count(3)
print(f"Number of occurrences of 3 in the list: {element_count}")

# 8. my_list.sort() - Sorts the list in ascending order.
my_list.sort()
print(f"Sorted list in ascending order: {my_list}")

# 9. my_list.reverse() - Reverses the order of elements in the list.
my_list.reverse()
print(f"Reversed list: {my_list}")
