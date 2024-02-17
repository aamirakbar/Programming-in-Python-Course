def a_func(function_list):
    # when we alter a mutible data structure (defind globally) inside the function
    # scope, it remains the same.
    # Uncomment the below line to see the ids changes
    function_list.append(100)
    print(f"Inside the function - id of function_list: {id(function_list)}")

global_list = [22, 24, 28, 50]
a_func(global_list)

print(f"Outside the function - id of global_var: {id(global_list)}")