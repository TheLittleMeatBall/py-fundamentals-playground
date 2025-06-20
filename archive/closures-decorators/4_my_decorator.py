def my_decorator(func):
    def wrapper():
        print("Something before the function runs...")
        # log usernames and timestamps
        func()
        print("Something after the function runs...")
    return wrapper

def say_hi():
    # I don't want to add that functionality here
    print("Hi!")

def do_something_else():
    print("I'm doing something else!")

say_hi_decorated = my_decorator(say_hi)

say_hi_decorated()
say_hi()
say_hi()
say_hi()

do_something_else_decorated = my_decorator(do_something_else)

do_something_else_decorated()