global_var = 42

def a_func():
    print(f"Inside the function, value = {global_var}")
    print(f"ID of global_var: {id(global_var)}")

a_func()

print(f"Outside the function, value = {global_var}")
print(f"ID of global_var: {id(global_var)}")