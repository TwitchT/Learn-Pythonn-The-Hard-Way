# All of these brackets are place holders, so when you .fortmat it will put the code in the place holder
formatter = "{} {} {} {}"
# This print would be place in the place holder
print(formatter.format(1, 2, 3, 4))
# This print will also be in the place holder but it would be on the second line
print(formatter.format("one", "two", "three", "four"))
# This print is basically the same as the other two print that I just did, instead it would go on the 3rd line when you run it
print(formatter.format(True, False, False, True))
# This print is going to print out 16 {}
print(formatter.format(formatter, formatter, formatter, formatter))
# This print is just an open format, so you can put anything you like in it and it will appear on the console when you run it
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
# Found out if you only put two sentence or words then it will fill out only two place holder then the rest won't work and it would just end up in an error
print(formatter.format("Hello I am Quoc", "Nani", "No U", "Hello")) # Me being curious
#print(formatter.fortmat("Helo I am somebody that doensn't know the world")) <-- If u don't put a comma and fill up the spaces I gives you an error