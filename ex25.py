# This will break down the sentence that you type
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
# This will sort the words that I broke 
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
# Print out the first word that you broke down
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
# Print down the last word that you broke down
def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print(word)
# This will sort the whole sentence that you typed out
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
# Give you both first and last word in your sentence
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
# Print out first and last word but it will sort the word a the same time
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)