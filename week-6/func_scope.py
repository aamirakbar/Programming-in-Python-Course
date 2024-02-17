def a_func():
    function_var = 99
    print(f"Inside the function - function_var:: {function_var}")

a_func()

# Uncommenting the next line would result in an error, 
# as function_var is not accessible here.
print(f"Outside the function - function_var: {function_var}")