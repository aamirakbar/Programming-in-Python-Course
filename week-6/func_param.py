def a_func(function_var):
    # when we change the value of the function variable inside the function
    # scope, it is no longer associated with the global variable.
    # Uncomment the below line to see the ids changes
    function_var = function_var + 1
    print(f"Inside the function - id of function_var: {id(function_var)}")

global_var = 22
a_func(global_var)

print(f"Outside the function - id of global_var: {id(global_var)}")