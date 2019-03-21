# This will define cheese_and_crackers
# So we can have muliple sentence with the same words but different numbers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!") # This will tell us cheeses we have
    print(f"You have {boxes_of_crackers} boxes of crackers!") # Tell us how many box of crackers we will have
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give th function numbers directly:")
# This will substitute our cheese_count and boxes_of_crackers with 20 and 30
cheese_and_crackers(20, 30)


print("OR, we can use variables from out script:")
# Substitute our cheese_count and _boxes_of_crackers with 10 and 50
amount_of_cheese = 10
amount_of_crackers = 50
# These are function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# This will add up the cheese and the boxes of crackers
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# This will add 100 to the amount of cheese and it wil add 1000 to the boxe of crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# def cheese_and_crackers(cheese_count, boxes_of_crackers);print(f"You have {cheese_count} cheeses!"); print(f"You have {boxes_of_crackers} boxes of crackers!") ; print("Man that's enough for a party!"); print("Get a blanket.\n"); print("We can just give th function numbers directly:"); cheese_and_crackers(20, 30); print("OR, we can use variables from out script:"); amount_of_cheese = 10; amount_of_crackers = 50; cheese_and_crackers(amount_of_cheese, amount_of_crackers); print("We can even do math inside too:"); cheese_and_crackers(10 + 20, 5 + 6); print("And we can combine the two, variables and math:"); cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Above me my Curiosity
# putting it all in one line doesn't work, it will just give you an error and i think it doesn't work because of the command "def"
