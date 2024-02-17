# Sample phone book dictionary
phone_book = {
    "Ali": "0300-123456",
    "Babar": "0345-9876543",
    "Nauman": "0333-112233445"
}

# 1. len(phone_book) - Returns the number of key-value pairs in the dictionary.
num_entries = len(phone_book)
print(f"Number of entries in the phone book: {num_entries}")

# 2. key in phone_book - Checks if a key is present in the dictionary (returns a boolean).
is_present = "Ali" in phone_book
print(f"Is 'Ali' in the phone book? {is_present}")

# 3. phone_book[key] - Accesses the value associated with a key.
babar_number = phone_book["Babar"]
print(f"Babar's phone number: {babar_number}")

# 4. phone_book.keys() - Returns a list of all keys in the dictionary.
all_keys = phone_book.keys()
print(f"All keys in the phone book: {list(all_keys)}")

# 5. phone_book.values() - Returns a list of all values in the dictionary.
all_values = phone_book.values()
print(f"All values in the phone book: {list(all_values)}")

# 6. phone_book.items() - Returns a list of key-value pairs as tuples.
all_items = phone_book.items()
print(f"All items in the phone book: {list(all_items)}")

# 7. phone_book.update(other_dict) - Updates the dictionary with key-value pairs from another dictionary.
new_entries = {"Dawood": "0301-7771111", "Azlan": "0302-2225555"}
phone_book.update(new_entries)
print(f"Updated phone book: {phone_book}")

# 8. phone_book.pop(key) - Removes the key-value pair with the specified key.
removed_number = phone_book.pop("Azlan")
print(f"Removed Azlan's number: {removed_number}")
print(f"Phone book after removing Charlie: {phone_book}")
