def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase"""

    for word in words:
        print(words.upper())

def print_upper_words2(words):
    """Turn that into a function, print_upper_words and dchange that function so that it only prints words that start with the letter 'e'(either upper or lowercase)"""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words):
    """Make your function more general: you be able to pass in a set of letters, and it only prints words that start with one of those letters"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break