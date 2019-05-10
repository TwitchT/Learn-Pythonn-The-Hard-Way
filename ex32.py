the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears' , 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# This will loop the number and it will count till 5
for number in the_count:
    print(f"This is count {number}")
    
# same as above
# This will show all of the fruits in the variable that we label "fruits"
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# aslo we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
# List all of the word and number we label in variable "change"
for i in change:
    print(f"I got {i}")
    
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to  5 counts
# This will count within the range of 0-6
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")