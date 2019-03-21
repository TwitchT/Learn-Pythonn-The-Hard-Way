name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# The print is tell me what his name is by using the special {} and putting in the first code above "name"
print(f"Let's talk about {name}.")
# Print is going to tell me what his height is by putting "height" in the special {}
print(f"He's {height} inches tall.")
# This print is going to tell me how much he weighs by putting the code "my_weight" in the special {}
print(f"He's {weight} pounds heavy.")
# This is just going to tell me that 180 kilograms isn't that heavy
print(f"Actually that's not too heavy.")
# Going to tell me his eye color and his hair color by putting "eyes" and "hair" in the special {}
print(f"He's got {eyes} eyes and {hair} hair.")
# Telling me that his teeth by putting "teeth" in the special {} and how it changes depending on what coffee he drinks
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
# This is going to add up how old he is, his weight, and his height
print(f"If I add {age}, {height}, and {weight} I get {total}.")

total = height * 2.54                                # This
print(f"My height in centimeters is {height*2.54}.") # Is my
total = weight / 2.205                               # Study
print(f"My weight in kilograms is {weight/2.205}.")  # Drills