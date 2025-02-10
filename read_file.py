# use a context manager (starts with "with", which ensure the block automatically closes the file -- so other can use it)
with open('pelican.txt', 'rt') as output:
    # use a for loop to iterate over the entire file, one line at a time -- slurping
    for line in output:
        # prints the contents of the returned data, and using [:-1] excludes the \n at the end of each line:
        print(line[:-1])

# display the data type of the returned data -- here each line of the file is a string
print(f"Type of each line: {type(line)}")

print("\n")

# use splitlines to return the contents of the file as a list
with open('pelican.txt', 'r') as output:
    pelican_list = output.read().splitlines()

# print the file as a list
print(f"Pelican limerick as a list: {pelican_list}")

# display the data type of the returned data -- now it is a list
print(f"Type of 'pelican_list': {type(pelican_list)}")

# output the number of items within the list using the print and len functions
print(len(pelican_list))