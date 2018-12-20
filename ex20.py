#import modules
from sys import argv

#arguments to bring in from terminal
script, input_file = argv

#defines a variable called print_all by using the string function 'read'
def print_all(f):
    print(">>> print_all: f=", f)
    print(f.read())
    print("<<< print_all: f=", f)

#defines a variable called rewind that will seek back to the zero point
def rewind(f):
    print(">>> rewind: f=", f)
    f.seek(0)
    print("<<< rewind: f=", f)

#defines a variable to print a line that passes two arguments for line count and f/string
def print_a_line(line_count, f):
    print(line_count, f.readline())

#sets the current file variable to the file that gets opened in the opening argument (input_file)
current_file = open(input_file)

#prints a string
print("First let's print the whole file:\n")

#prints the whole contents of the current file
print_all(current_file)

#prints a string
print("Now let's rewind, kind of like a tape.")

#rewinds location of current file to zero/starting point
rewind(current_file)

#prints a string
print("Let's print three lines:")

#sets the current line variable to 1
current_line = 1
#prints the 1st line from the current file we opened
print(">>> current_line: f=", current_line)
print_a_line(current_line, current_file)
print("<<< current_line: f=", current_line)

#sets the current line to the next in the sequence
current_line = current_line + 1
print(">>> current_line: f=", current_line)
print_a_line(current_line, current_file)
print("<<< current_line: f=", current_line)

#sets the print function to print the next line
current_line = current_line + 1
print(">>> current_line: f=", current_line)
print_a_line(current_line, current_file)
print("<<< current_line: f=", current_line)
