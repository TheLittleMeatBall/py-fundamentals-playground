interests = ['coding', 'making polls']

# make a person - a new reference is created
lewis = { 
    "name": 'Lewis',
    "interests": interests
}

some_string = "blah"

# this is now impure
# it changes stuff outside of it
def add_impure_interest(person, interest):
    # no new person / interests list is created
    some_string = "something else"
    person['name'] = 'Sam'
    person['interests'].append(interest)
    return person

# this is a Pure Function
# it does NOT change stuff outside of it
# this is part of what's called "Functional Programming"
def add_interest(person, interest):
    # make a person - a new reference is created
    new_person = {
        'name': person['name'],
        # this makes a new list
        'interests': person['interests'] + [interest] # making a new list from the old one plus the new one
    }
    return new_person

cool_new_lewis = add_interest(lewis, "gardening")
print(cool_new_lewis == lewis) # are the values the same
print(cool_new_lewis is lewis)
print(lewis)
print(cool_new_lewis)

# functions shouldn't change other things
cool_new_lewis = some_library_function(lewis, "gardening")

# abdul = {
#     name: 'Abdul',
#     interests: ['cool stuff']
# }

# cool_new_abdul = add_interest(abdul, 'world cinema')

# when it comes to performance optimisation
# my advice is not to think about it!
# "premature optimisation is the root of all evil"
# first make it correct, then make it faster ONLY IF NECESSARY

# complexity is the MAIN ENEMY of developers