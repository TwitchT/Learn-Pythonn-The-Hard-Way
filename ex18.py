# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args; print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that tag *args is actually pointless, we can just do this
# This will combine 2 args in one line
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes on argument
# Separated the arg
def print_one(arg1):
    print(f"arg1; {arg1}")

# this one takes no argument
def print_none():
    print("I got nothin'.")
# This goes in order so it doesnt matter if you mess up the code order
# This is a Calling
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# def print_two(*args):                                       <<< This is my curiosity
    # arg1, arg2 = args; print(f"arg1: {arg1}, arg2: {arg2}") I found out you can make this one line with ;
                                                            # This only works if they have something like arg1, arg2 = arg
# def print_two(*args):; arg1, arg2 = args; print(f"arg1: {arg}, arg2: {arg2}") <<<< This will give you an error