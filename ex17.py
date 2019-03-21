from sys import argv; from os.path import exists; script, from_file, to_file = argv; print(f"Copying from {from_file} to {to_file}"); in_file = open(from_file); indata = in_file.read(); print(f"The input file is {len(indata)} bytes long"); print(f"Does the output file exist? {exists(to_file)}"); print("Ready, hit RETURN to continue, CTRL-C to abort."); input(); out_file = open(to_file, 'w'); out_file.write(indata); print("Alright, all done.")

# This is my code on line long and below it will be the original

# from sys import argv
# from os.path import exists
# These are variables
# script, from_file, to_file = argv
# This print will substitute the variables that are inside the strings
# print(f"Copying from {from_file} to {to_file}")

# we could do these two one line, how?
# Add a ; for it to be on one line
# in_file = open(from_file); indata = in_file.read()
# Will tell you how many bytes there is
# print(f"The input file is {len(indata)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()
# This will open the file and write the data
# out_file = open(to_file, 'w')
# out_file.write(indata)

# print("Alright, all done.")
# If a program try to open the file it might not be able to thats I why you need to write out_file.close()
# out_file.close()
# in_file.close()