# This code is  telling me how many type of people their is
types_of_people = 10
# This code is going to tell me how many type of people but in a sentence by using the special {} and using the command
# in the second line, Line 2
x = f"There are {types_of_people} types of people." # <--------- String put inside another string

# This is another code that im going to use and make it into a sentence
binary = "binary"
# This code is going to turn do_not into don't
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # <--------- String put inside another string
# This is going to make the console say line 5
print(x)
# This is going to make the console say line 10
print(y)

# This print is going to say what ever "x" said in line 5
print(f"I said: {x}") # <--------- String put inside another string
# This print is going to say what ever the "y" said in line 10
print(f"I also said: {y}") # <--------- String put inside another string

# This code will make the word hilarious turn into False
hilarious = False

# This code will make the two word "joke_evaluation" turn into "Isn't that joke so funny?!"
joke_evaluation = "Isn't that joke so funny?! {}"
# This print ask if the joke is funny and the double () at the end makes it separate from "joke_evaluation"
print(joke_evaluation.format(hilarious)) # <--------- String put inside another string

w = "This is the left side of..."
e = "a string with a right side."

# The reason why this would make a string long because you are adding to code into one string, so if you do that
# then it would just double the size so it would be longer
print(w + e)

a = "Hello this is me,"
b = "this is not me,"
c = "now this is the real me."

print(a + b + c)