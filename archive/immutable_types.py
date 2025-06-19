# Immutable Types

# mutable = "can be changed"
# immutable = "can't be changed"

some_list = [2,3,5] # list
some_list[0] = 6 # [6, 3, 5]
some_list.append(12) # 6,3,5,12

# tuple
primes = (2,3,5)
# a collection of numbers that can't be changed
# (doesn't have to be numbers, could be other stuff)
# primes[0] = 6 # 'tuple' object does not support item assignment

# strings are immutable?
greeting = 'hello'
# greeting[0] = 'z' # 'str' object does not support item assignment

# but hold on...
# i've been lied to!

greeting = greeting + ' Javier!'
print(greeting)

# strings are SPECIFICALLY weird

other_greeting = 'hello'
another_greeting = 'hello' # these will all have the same reference
# this is called "string interning"

# HOWEVER I advise you not to care or think about this