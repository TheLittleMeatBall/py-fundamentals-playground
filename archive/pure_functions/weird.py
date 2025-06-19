
# describe this object! 
primes = (2,3,5, ['numbers', 'are'])

# list inside a tuple
# tuple with 3 numbers and a list

# how many things are stored in this tuple?
# FOUR - 3 numbers, and a list

# specifically WHAT is stored in those four things:
# 1. the number 2
# 2. the number 3
# 3. the number 5
# 4. a REFERENCE to a list
#       a. "numbers"
#       b. "are"
#       c. "cool"

# primes[0] = 6 # 🚨 this is a problem! not allowed
primes[3].append("cool") # is this legal?

# can't modify a tuple?
# or can we?

print(primes)

