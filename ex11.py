# This print will ask how old you are, the "end= ' ')" thats where your answer would appear it will appear at the end of the sentence
print("How old are you?", end=' ')
# This is a variable where you would put your age "input ()" you would put yout answer in their
age = input()
# This print will ask how tall you are
print("How tall are you?", end=' ')
# We are creating a variable for height
height = input()
# Print would ask us how much you weigh
print("How much do you weigh?", end= ' ')
# Creating a variable for weight
weight = input()

# This print is going to gather all of our answers above and put it into a sentence using {}
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
