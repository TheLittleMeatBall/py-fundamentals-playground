
def power_factory(base):
    # base lives in the PARENT (power_factory) scope
    def power(x):
        # base is USED in a child/enclosed/inner function
        # therefore Python "closes over" base... i.e. it REMEMBERS it
        return base**x # base to the power of x
    return power

pow2 = power_factory(2) # this is going to raise the base to the power of 2
pow3 = power_factory(3) # this is going to raise the base to the power of 3

print(pow2(4)) # 16
print(pow3(4)) # 81
print(pow3(2)) # 9

pow17 = power_factory(17)

print(pow17(9))