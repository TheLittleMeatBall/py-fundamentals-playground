# global is HERE
banana = 6

def outer():
   
    num = 5 # this area here is the LOCAL scope for outer, and the ENCLOSING scope for inner
    def inner():
        # UnboundLocalError: cannot access local variable 'num' where it is not associated with a value
        nonlocal num
        num = num + 3
        print(num)
    inner()
outer()