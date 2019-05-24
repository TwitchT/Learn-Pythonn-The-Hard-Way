ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")
# Created some variables that is going to be use later in the code
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", 
              "Corn", "Banana", "Girl", "Boy"]
# This code will add mroe stuff from the "more_stuff" variable 
# It will keep adding stuff until it reaches the number 10
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
# This will print out all of the 10 items we now have
print("There we go; ", stuff)

print("Let's do some things with stuff.")
# This will take whats in the first spot
print(stuff[1])
# This will take the last item on the list and print it out
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
# This will join whats in the 3rd and 5th spot on the list
print('#'.join(stuff[3:5])) # super stellar!