# this is a string, not a tuple (as there is no comma)
tup = "Hello"
# printing the length of tup simply gives the number of characters in the string
print(len(tup))

# with the addition of a comma, tup becomes a tuple
tup = "Hello",
# therefore, printing the length of the tuple will return 1 because there is only one element in the tuple - the string "Hello"
print(len(tup))