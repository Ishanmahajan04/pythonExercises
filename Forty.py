from random import randrange


def anagram(word_list, subject):
    # Choose a random word from the provided list
    w = word_list[randrange(0, len(word_list))]
    ana = ''

    # Create our anagram
    # This won't end until the anagram is the same length as the word
    while len(ana) < len(w):
        char = w[randrange(0, len(w))]  # Choose a random letter

        if char not in ana:  # If the letter isn't in the anagram yet
            # Insert it in the anagram the number of times it is found in the word
            for x in range(w.count(char)):
                ana += char
        if ana == w:  # This is to make sure the anagram is never the same as the word
            continue

    # The game
    print
    '%s word anagram: %s' % (subject.capitalize(), ana)
    while True:
        print
        'Guess the %s word!' % subject
        guess = raw_input()
        if guess == w:
            print
            'Correct!'
            break


# test
anagram(['brown', 'yellow', 'green', 'red', 'blue'], 'colour')
anagram(['Haiti', 'USA', 'France', 'Spain', 'China'], 'country')