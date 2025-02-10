cheese = ['cheddar', 'stilton', 'cornish yarg']
cheese+= 'oke'
print(cheese)
# += operator with a list and a string, the string is treated as an sequence of characters
# each character in the string is added as a separate element to the list

cheese.append ('oke')
print(cheese)
# use of .append method to add a string to the list
# alternative is slicing, loop or concatenation
# from the internet: .extend

cheese.extend(['mozarella', 'feta'])
# the [] has to be used as it is modification of the list called cheese
print(cheese)

cheese[len(cheese):]=['mozarella', 'feta']
print(cheese)