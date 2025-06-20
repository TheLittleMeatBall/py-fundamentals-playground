def log_username_before(func):
    def wrapper():
        print("Logging username...")
        func()       
    return wrapper

def log_timestamp_after(func):
    def wrapper():
        func()  
        print("Logging timestamp...")     
    return wrapper

@log_username_before
@log_timestamp_after
def say_hi():
    print("Hi!")

@log_timestamp_after
def do_something_else():
    print("I'm doing something else!")

say_hi()