# initial list of cheeses
cheese = ["Cheddar", "Stilton", "Cornish Yarg"]
print(cheese)

# += is a concatenation operator, it changes the variable on the left by adding the values on the right
# it can add a list to another list but when adding a string to a variable, it will treat each character separately (bc strings are iterable)
# hence, the following line of code would add O, k, e to the cheese list, not Oke
# cheese += "Oke"

# here, += is adding Oke as a list (not a string) to the initial cheese list because it's formatted as a list item
cheese += ["Oke"]
print(cheese)

# you can also use the append method, which adds one item to the end of a list
# cheese.append("Oke")
# print(cheese)

# use the extend method to add more than one item to the end of the list
cheese.extend(["Brie", "Gouda"])
print(cheese)