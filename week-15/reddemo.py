from functools import reduce

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce to find the product of numbers
product = reduce(multiply, numbers)

print(product)  # Output: 120 (1 * 2 * 3 * 4 * 5)