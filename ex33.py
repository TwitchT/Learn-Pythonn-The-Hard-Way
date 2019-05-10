# Created a variable and set it to the number 0
i = 0
# This will build a number list
numbers = []
# While is a loop control
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    # This will at +1 until it counts up to 6
    i = i + 1
    # this will tell you what the cuurent number is
    print("Numbers now:", numbers)
    # This will tell you what the current bottom number is now
    print(f"At the bottom i is {i}")
    
    
print("The numbers: ")
# This will print out all of the numbers in a list
for num in numbers:
    print(num)