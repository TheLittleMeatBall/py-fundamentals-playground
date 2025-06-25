# Write a function which calls a given function multiple times.
# This function should call the given function however many times is specified,
# It should pass in the given argument each time.

# Args: INPUT
#   1. func: (function) any function
#   2. call_count: (int) how many times to call it
#   3. arg_to_pass: (any) the argument to pass to the given function

# Returns: OUTPUT
#   None

def repeater(func, call_count, arg_to_pass):
    for _ in range(call_count):
        func(arg_to_pass)
    return None

# repeater(send_data_to_warehouse, 10, warehouse_data)
# repeater(email_customer, 5, email_data)
# repeater(abduls_func, 10, abduls_specific_data)
