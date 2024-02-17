# Decorator function
def decorator_function(func):
    def wrapper():
        print("Executing some code before the function")
        func()
        print("Executing some code after the function")
    return wrapper

# Function decorated with the decorator function
@decorator_function
def greet():
    print("Hello, world!")

# Calling the decorated function
greet()