# Scope
# 4 types... we'll get to them!

def greet():
    # "name" is declared INSIDE the function
    name = "Alice"
  
    print("Hello, ", name)
    print(locals())
    
def do_something_else(): # this name is NOT CRAMP
    print(locals())
    people.append('hello')


greet()

people = ['Liam', 'Jini']
do_something_else()


numbers = [ 1,2,3,4,5]

print(globals())
print("Let's look at locals here instead:\n")
print(locals())
#print("Outside the function: ", name) # NameError: name 'name' is not defined


   
