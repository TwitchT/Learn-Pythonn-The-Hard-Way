# 1-3 We created a variable for people, cats, and dogs
people = 20
cats = 30
dogs = 15

# Cats are greater than people, so the print statement will print
if people < cats:
    print("Too many cats! The world is doomed!")
# People are not greater than cats, so this print will not print at all
if people > cats:
    print("Not many cats! The world is saved!")
# Dogs are not greater so the print line will not print
if people < dogs:
    print("The world is drooled on!")
# People are greather than dogs so the print statement will pring
if people > dogs:
    print("The word is dry!")
# This addes +5 to the dogs variable so it went from 15 to 20
dogs += 5
# They are both equal or greater 
if people >= dogs:
    print("People are greater than or equal to dogs.")
# Both less or equal
if people <= dogs:
    print("People are less than or equal to dogs.")
# They are both equal
if  people == dogs:
    print("People are dogs.")