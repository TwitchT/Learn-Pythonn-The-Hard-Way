# Defining the word add, so you can add variables later on 
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
# Subtract variables later on by defining it    
def substract (a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b
# Going to multiply later on by defining it    
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
# Will divide the variables by defining it     
def divide (a, b):
    print(f"DIVIDING {a} / {b}")
    return a /  b


print("Let's do some math with just functions!")
# Since we defined the functions it will
# do math and it will give you the answer
age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# Going to replac whats in the Curly Brackets with the number it got from doing math
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the etxra credit, type it in anyway.
print("Here is a puzzle.")
# Takes the answers from line 22-25 and uses it to do more math but its all in one line
what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")