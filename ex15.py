#import modules from sys
from sys import argv

#sets two arguments to be passed at command line
script, filename = argv

#opens the contents of our text file
txt = open(filename)

#prints the variable passed by commmand line of our filename
print(f"Here's your file {filename}:")
#prints the contents of the text file
print(txt.read())

#prints a prompt for user to type their filename again
print("Type the filename again:")
#sets a varialbe called file_again
file_again = input(">")

#sets a variable called textagain that will open our text file
txt_again = open(file_again)

#prints the contents of the text file
print(txt_again.read())
