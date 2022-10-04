import re
import sys

def make_length_dictionary(file):
    length_dictionary = {}
    count = 0
    for line in file:
        word = line
        word = word.rstrip("\n")
        wordlength = len(word)
        try:
            length_dictionary[wordlength].append(word)
        except KeyError:
            length_dictionary[wordlength] = []
            length_dictionary[wordlength].append(word)
        count += 1
    print("Loaded %d words" % count)
    
    return length_dictionary

def make_regex(word):
    def place_fixed_metacharacter(character):
        fixed_metacharacter = None
        fixed_metacharacter = "[" + character + "]"
        return fixed_metacharacter
    def place_range_search():
         return "[a-z]"
    def join_list_to_string(regexlist):
        separator = ""
        regex_string = separator.join(regexlist)
        return regex_string
    
    regex = None
    characters = [char for char in word]
    for x in range(0,len(characters)):
        if characters[x] != '_':
            characters[x] = place_fixed_metacharacter(characters[x])
        elif characters[x] == '_':
            characters[x] = place_range_search()
    regex = join_list_to_string(characters)
    return regex

def find_match(regex, working_list):
    matches = []
    matchcount = 0
    for word in working_list:
        if regex.match(word) != None:
            matches.append(word)
            matchcount += 1
    print("Matches found: " + str(matchcount))
    return matches

def main():
    exitmessage = "Thank you for using Crossword Finder."
    f = open('english3.txt', 'r')
    length_dictionary = make_length_dictionary(f)
    runprogram = True
    getword = None
    wordlength = None
    working_list = None
    print("Input unknown word in the following format:")
    print("'_e_d', using _ for unknown characters.")
    print("Type 'quit' to exit.")
    print()
    while runprogram == True:
        getword = str(input("> "))
        if getword == 'quit':
            sys.exit()
            print(exitmessage)
        elif " " in getword:
            print("Words cannot have spaces = ' '. Please try another word.")
            getword = None
            working_list = None
            continue
        else:
            wordlength = len(getword)
            print("Input word: " + str(getword))
            print("Word length: " + str(wordlength))
            try:
                working_list = length_dictionary[wordlength]
            except KeyError:
                getword = None
                working_list = None
                print("I'm sorry, but the dictionary does not contain any words that long.\n Please try another (shorter) word.")
                continue
            regexstring = make_regex(getword)
            regex = re.compile(regexstring)
            matched_words = find_match(regex, working_list)
            for match in matched_words:
                print(match)

    print(exitmessage)

main()
