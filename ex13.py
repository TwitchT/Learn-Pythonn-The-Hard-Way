from sys import argv
# Read the WYSS section for how to run this
# These will store the variables
script, first, second, third = argv
# Script will put the first thing that comes to the line, 13.py is the first thing
# So script will put it 13.py and it will be the variable
print("The script is called:", script)
# If you put Kiwi after the 13.py then kiwi will be the varaible and it will replace first
print("Your first variable is called:", first)
# What ever you put after kiwi then it would turn it into a variable so if you put mango then
# Mango would be the second variable
print("Your second variable is called:", second)
# Your last and third variable is whatever you out after Mango so if you put Watermelon
# Then third would be replace with watermelon
print("Your third variable is called:", third)
# It tells me that there is too many values to unpack
#print("Your fourth variable is called:", fourth)

# One study drill
# The errors says "not enough values to unpack "