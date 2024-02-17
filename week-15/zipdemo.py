# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Using zip to combine elements from lists into tuples
combined = zip(names, ages)

# Converting the zip object into a list of tuples
combined_list = dict(combined)

print(combined_list)  
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
