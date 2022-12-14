# 1.For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

list_of_words = ['Hey', 'Im', 'learning','Python']
for word in list_of_words:
    print(word.upper())


# 2.Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)


def print_upper_words(words):
    '''For a list of words, print put each word on a separate line all in uppercase'''
    for word in words:        
        print(word.upper())


# 3.Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

def must_start_with_e(words):
    '''Prints out words that stat with the letter "e"'''

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

# 4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters

def print_set_of_letters(words, must_start_with):
    '''Prints words that start with one of the passed in letter'''
    for word in words:
        for char in must_start_with:
            print(word.upper())
            break