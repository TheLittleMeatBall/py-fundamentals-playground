def swap(func):
    def wrap_func(a, b):
        return func(b, a)
    return wrap_func

@swap
def subtract(a,b):
    return a-b

@swap
def add(a,b):
    return a + b

print(subtract(7,3)) # this actually does 3-7
print(add("Hello ", "Abdul"))

# this is a great evil that we have delivered to the world