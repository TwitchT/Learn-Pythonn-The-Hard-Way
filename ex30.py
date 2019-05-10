people = 30 
cars = 40
trucks = 15

# There are more cars than people
if cars > people:
    print("We should take the cars.")
# If the if statement isnt true then it will check if the elif statement is true
elif cars < people:
        print("We should not take the cars.")
# It will check the else statement if the elif statement isnt true
else:
        print("We can't decide.")
# There are less trucks than cars but trucks are bigger
if  trucks > cars:
        print("That's too many trucks.")
# Check if this statement is true if if statement is not
elif trucks < cars:
        print("Maybe we could take the trucks.")
# Check else if elif is false
else:
        print("We still can't decide.")
# If this statement is false then it will check the else statement
if people > trucks:
        print("Alright, let's just take the trucks.")
else:
        print("Fine, let's stay home then.")