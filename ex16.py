from sys import argv
# Variables
script, filename = argv
# It is going to erase the filename that you put as your filename after 16.py
print(f"We're going to erase {filename}.")
# If you don't want to erase the file then all you have to do is hit CRTL-C
print("If you don't want that, hit CRTL-C (^C).")
# IF you want to erase it hit Enter
print("If you do want that, hit RETURN")
# You are going to give you the answer for the code above. so if you want to erase it hit Enter and if not hit CRTL-C
input("?")
# This will open the file that you put as the filename
print("Opening the file...")
target = open(filename, 'w')
# This will shorten the file size... I think
print("Truncating the file. Goodbye!")
target.truncate()
# After it deletes the file, its going to ask you what you want to type in the file
print("Now I'm going to ask you for three lines.")
# You have to put what you want (It can be a sentence) at the end, for example line1: I like Chicken Nuggets
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")
# It is going to put what you typed out for line1-3 and put it in the file that you typed in at the beginning of the  code
print("I'm going to write these to the files.")
# Using only one target.write to make 3 lines instead of 6
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# This will close the whole code, so you won't be able to do anything else unless you type in "python3.6 16.py 16sam.txt" again16
print("And finally, we close it.")
target.close()