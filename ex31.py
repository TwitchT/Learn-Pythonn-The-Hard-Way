# This is going to ask you what door you would choose
print("""You enter a dark room with two doors.
Do you go through the #1 or door #2?""")
# You put the door number
door = input("> ")
# If you choose door 1 and it will give you options on what you want to do
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take hee cake.")
    print("2. Scream at the bear.")
    # You choose what you want to do in the door
    bear = input("> ")
    # If you choose one it will tell you what will happen
    if bear == "1":
        print("The bear eats your face off. Goob job!")
    # If you choose 2 then it will ignore one and it will tell you what happens
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    # You can do something else other than those 2 options
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bears runs away.")
    #If you choose door 2 it will give you options to choose from
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothepins.")
    print("3. Understanding resolvers yellow melodies.")
    # You choose number 1-3 and it will tells you what happenes
    insanity = input("> ")
    # If you choose 1 or 2 then it will say that you survive
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
        # If  you choose 3 then you die
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
      
else:
    print("You stumble around and fall ona knife and die. Good job!")