from sys import argv
# Stores The Variables
script, user_name = argv
prompt = '> '
# This will print out your user_name and the script
# The script is always the first thing that appears so 14.py and the user_name is what you type after 14.py
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
# This is gonna ask you a question and it will insert your name that you typed after 14.py
print(f"Do you like me {user_name}?")
# This allows you to type and answer to gather more information
likes = input(prompt)

print(f"Where do you live {user_name}?")
# You put an answer in and it will save the information
lives = input(prompt)

print("What kind of computer do you have?")
# Saves the information from the answer you give
computer = input(prompt)
# This will print out all of the information it saves and it will make it into a sentence
# f""" allows you to type as many line as you want and it allows you to put in variables
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")