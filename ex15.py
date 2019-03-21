from sys import argv
# These will store the variables
script, filename = argv
# Creating a variable to open the file with a .txt at the end of it
txt = open(filename)
# This will substitute the variable "filename" with something else, if you named your file "15.txt" then the filename will be 15.txt
print(f"Here's your file {filename}:")
# This will read the file that you put as the filename
print(txt.read())
# This will tell you to type out the file again
print("Type the filename again:")
# You will put the file name again
file_again = input("> ")
# This will open the file that you type in
txt_again = open(file_again)
# This will print out whats in the file that you type out
print(txt_again.read()) # Is it possible to make a python command that closes the file? <<<<<<<<<<<<< Curiosity

# If you remove line 10-15 the code will still run but you won't be able to open up the file a second time
# Unless you type the whole code again "python3.6 15.py 15sam.txt" instead of just typing "15sam.txt"
# And being to see whats in the text again