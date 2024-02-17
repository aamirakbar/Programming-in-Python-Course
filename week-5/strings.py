# Sample string
my_string = "   Hello, World!   "

# 1. len(my_string) - Returns the length of the string.
string_length = len(my_string)
print(f"Length of the string: {string_length}")

# 2. my_string.upper() - Converts the string to uppercase.
uppercase_string = my_string.upper()
print(f"Uppercase string: {uppercase_string}")

# 3. my_string.lower() - Converts the string to lowercase.
lowercase_string = my_string.lower()
print(f"Lowercase string: {lowercase_string}")

# 4. my_string.strip() - Removes leading and trailing whitespace.
stripped_string = my_string.strip()
print(f"Stripped string: '{stripped_string}'")

# 5. my_string.split(delimiter) - Splits the string into a list of substrings using the specified delimiter.
split_string = my_string.split(",")
print(f"Split string: {split_string}")

# 6. my_string.find(substring) - Returns the index of the first occurrence of the substring (or -1 if not found).
substring_index = my_string.find("World")
print(f"Index of 'World': {substring_index}")

# 7. my_string.replace(old, new) - Replaces all occurrences of the old substring with the new substring.
replaced_string = my_string.replace("World", "Python")
print(f"Replaced string: '{replaced_string}'")
