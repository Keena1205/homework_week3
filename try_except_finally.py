# try to open and read a file called imaginary_file
# fh_out = open('imaginary_file', 'r')

# including the file opening statement within the try block allows the exception to be caught
# otherwise an error in pycharm is noted before the try block is even entered
try:
    fh_out = open('imaginary_file', 'r')
    fh_out.write("Hello, world!")

# this exception comes into play if the file has been deleted/moved/doesn't exist and cannot be found
except FileNotFoundError as err:
    print("Sorry, file cannot be found.")

# this block tidies up by closing the file
finally:
    print("Executing finally block.")
    fh_out.close()
    # this doesn't work, I think because fh_out wasn't defined before the try block started?