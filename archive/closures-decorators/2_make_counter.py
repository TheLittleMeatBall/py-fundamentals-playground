

def make_counter():
    # we can store STATE using closures
    # state is whatever my app cares about - the data I want to remember
    # we can store state in lots of different ways
    # so far, we have stored "state" in just variables
    # we may store them in classes (we'll look at this next week!)

    # here we can use a CLOSURE to store some state
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

my_counter = make_counter()
print(my_counter())  # 1
print(my_counter())  # 2
print(my_counter())  # 3

second_counter = make_counter()
print(second_counter())
print(second_counter())
print(my_counter())  # 4
print(my_counter())  # 5
print(second_counter())