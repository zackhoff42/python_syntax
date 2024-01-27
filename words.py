def print_upper_words(words):
    """
    Accepts a list and converts each word in the list to all caps.
    Then, prints each word on a new line.

    print_upper_words(['hello','goodbye','yesterday','tomorrow']) =>
    HELLO
    GOODBYE
    YESTERDAY
    TODAY
    """

    for word in words:
        print(word.upper())

print_upper_words(['hello', 'goodbye', 'yesterday', 'tomorrow'])

def print_upper_words_two(words):
    """
    Accepts a list and converts each word in the list to all caps if it begins with the letter 'e' or 'E'.
    
    print_upper_words_two(['hello','eggs','Echo','goodbye']) =>
    EGGS
    ECHO
    """

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

print_upper_words_two(['hello','eggs','Echo','goodbye'])

def print_upper_words_three(words, must_start_with):
    """
    Accepts a list and converts each word in the list to all caps if it begins with the the value passed in to must_start_with.
    
    must_start_with also accepts a list
    
    print_upper_words_three(['hello','goodbye','yo','yellow'], ['h','y']) =>
    HELLO
    YO
    YELLOW
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

print_upper_words_three(['hello', 'goodbye', 'yo', 'yellow'], ['h', 'y'])