up_here_some_data = "Abdul"

def greeting_maker(greeting):
    name = 'Lord Horace Noodle IV' # strings are interned and remembered by python BUT don't worry about it!
    colours = ['red', 'green', 'yellow']

    colours.append('purple')

    def create_greeting():
        # greeting and name are "remembered" from the enclosing scope when this instance of this function is declared
        # this is called a "closure", but I prefer to think of it as them being remembered
        return f'{greeting} {name}'
    
    return create_greeting # greeting_maker returns a function, which makes it a higher-order function
    # we've finished with greeting_maker, so Python will "clean up" colours but remember greeting/name
    # the rule is, at the end of a scope/function Python cleans up whatever is only used in that scope

say_hello = greeting_maker("Hello")
say_hi = greeting_maker("Hi")

print(say_hello())
print(say_hi())
print(say_hi())
print(say_hello())

