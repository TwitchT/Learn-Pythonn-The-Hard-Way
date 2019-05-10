import sys
# Will make the code run on bash
script, input_encoding, error = sys.argv

# Defines the function to make it work later on
def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
        
# Defines this function to make it work when I use it again in the code
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
# This will print out '<===>' for every raw bytes that the txt have
    print(raw_bytes, "<===>", cooked_string)
    
# This will open the language.txt and it will encode something called a utf-8
languages = open("languages.txt", encoding="utf-8")
# Function that we define before
main(languages, input_encoding, error)