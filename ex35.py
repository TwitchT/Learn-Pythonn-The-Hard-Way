# Imports exit command to bash
from sys import exit
# This will define gold room so we can use it on in our code from later on
def gold_room():
    print("This room is full of gold. How much do you take?")
    # We put how much gold we take
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    # We choose a number from 0-50    
    if how_much < 50:
        # Choose a low number then this print statement appears
        print("Nice, you're not greedy, you win!")
        exit(0)
        # Choose a high number then this print statement appears
    else:
        dead("You greedy bastard!")
        
# Define bear room so we can use it for later on in this game
def bear_room():
    # This print out all of the options you can do when you choose the bear room
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to the move the bear?")
    bear_moved = False
    # You type an answer from above
    while True:
        choice = input("> ")
            # Type "take honey" then a print statement will appear 
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
            # If you "taunt bear" then a print statement will appear 
        elif choice == "taunt bear" and not bear_moved:
            # This is what will happen when you choose the right answer
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
            # If you taunt the bear again then you will die
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
            # Choose open door then you go into a gold room
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
           
# This will define the other door and it will give you options            
def cthulu_room():
    print("Here you see the great evil Cthulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    # Input an option and it will show you what other options you have
    choice = input("> ")
    # These are the option it will print, if you choose the first one then you flee
    # If you choose anything other then flee then it will ignore it
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulu_room()
        
# This defines "why"
def dead(why):
    print(why, "Good job!")
    exit(0)
# Defines the start of room and it will tell you options that you can takr
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one of you take/")
    # Type in a option and other options will appear
    choice = input("> ")
    # "Left" and "Right" are the two options that will appear
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")
        
# The game will start        
start()