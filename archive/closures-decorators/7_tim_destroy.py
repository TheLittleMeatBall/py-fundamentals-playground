def tim_destroy(func):
    def inner_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result) + " meow!!"
    return inner_func

@tim_destroy
def subtract(a,b):
    return a - b

print(subtract(5, 3))