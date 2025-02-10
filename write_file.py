# use the open function, giving the name of the file and path, and specifying the mode as append/a
# this creates the file automatically and lets us start writing to it
# output = open('pelican.txt', 'a')
output = open('pelican.txt', 'w')

# using the write method, add a line of text to the pelican txt file
# use \n to ensure proper line breaks in the file (otherwise would run on one continuous line and would be difficult to read)
pelican = output.write("A wonderful bird is the pelican. \n")

# confirming the string has been added to the text
print(pelican)

# append second line of the limerick using write method
pelican = output.write("His bill holds more than his belican. \n")

# confirming the string has been added to the text
print(pelican)

# create a list with the remaining lyrics, including \n at the end of each line
pelican_list = ["He can take in his beak, \n", "Enough food for a week, \n", "But I'm damned if I see how the helican. \n"]

# append list to the pelican file using writelines
# writelines doesn't return an end of line marker so we need to include \n in the pelican list variable
output.writelines(pelican_list)

# QUESTION - how do I stop it from adding constantly to the text? Changed from a to w