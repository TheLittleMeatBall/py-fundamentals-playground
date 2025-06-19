fruits = ["apple", "banana", "cherry"] # list

more_fruits = ["apple", "banana"] # another list

print(fruits == more_fruits)

more_fruits.append("cherry")

print(fruits == more_fruits)

# == "Value" comparison - are the values in the lists the same

print(fruits is more_fruits)
# is "Reference" comparison - are these the SAME ACTUAL THING
# do these variables have the same reference = do they have the same address in memory
# i.e. are they the same ACTUAL THING

# fruits      [a,b,c]
# more_fruits [a,b,c]

print(id(fruits))
print(id(more_fruits))

fruits = more_fruits # assign the PLACE IN MEMORY (reference) from more_fruits to fruits
print(fruits == more_fruits) # true
print(fruits is more_fruits) # true

print(id(fruits))
print(id(more_fruits))

# values and references
a = 10
b = 12

a = b # both 12

a = a + 1
# both 13?
print(a)
print(b)

fruits.append("date")

print(fruits)
print(more_fruits)

# some types are stored as values (e.g. numbers)
# some types are stored as references (e.g. lists, dictionaries, strings)
