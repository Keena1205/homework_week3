
# Open the file in append mode (a)
# with - controls the operation on the code
# file_handle is the way of referring to the file
# "hand holding a folder (file)"

with open('pelican.txt', 'a') as file_handle:
    # Append the first line
    file_handle.write("a wonderful bird is the pelican\n")
    # Append the second line
    file_handle.write("his bill holds more than his belican\n")

# Creating the list with the multiple strings
# but next line \n has to be added manually
    lines = [
        "he can take in his beak,\n",
        "enough food for a week,\n",
        "But I am damned if I see how the helican.\n"
    ]

# Append the list to the file using writelines method
# write a list of strings to the file
# instead of adding single line by .write()

    file_handle.writelines(lines)