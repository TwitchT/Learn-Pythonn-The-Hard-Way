from sys import argv
# Store variables
script, input_file = argv
# Line 5-12 will define the functionss; gives error if you remove those lines
def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())
# This will open the current file that we typed in
current_file = open(input_file)

print("First let's print the whole file:\n")
# This will print out whats in the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# This will repeat whats in the file
rewind(current_file)

print("Let's print out three lines:")       
# Going to print out three lines and say whats in the first three lines of the file
current_line = 1; print_a_line(current_line, current_file); current_line = current_line + 1; print_a_line(current_line, current_file); current_line = current_line +1; print_a_line(current_line, current_file)
# I made the code shorter by putting it in 1 line