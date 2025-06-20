from random import choice

def needless_chaos(func):
    outputs = []
    def wrapper(*args, **kwargs):
        outputs.append(func(*args, **kwargs))
        return choice(outputs)
    return wrapper