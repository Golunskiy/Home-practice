# Problem Set 2, hangman.py
# Name: Golinskiy Denis
# Group: KM-02
# Hangman Game
# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters_guessed = set(letters_guessed)
    new_set = set()
    for symbol in secret_word:
        new_set.add(symbol)
    if letters_guessed | new_set == letters_guessed:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    new_list = []
    for symbol in secret_word:
        if symbol in letters_guessed:
            new_list.append(symbol)
        else:
            new_list.append('_ ')
    str = ''.join(new_list)
    return str


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    al = str(string.ascii_lowercase)
    new_list = []
    for symbol in al:
        new_list.append(symbol)

    for symbol in letters_guessed:
        new_list.remove(symbol)
    str_not_used_letters = ''.join(new_list)
    return str_not_used_letters


def score(secret_word, letters_guessed):
    letters_guessed = set(letters_guessed)
    new_set = set()
    for symbol in secret_word:
        new_set.add(symbol)
    length = len(new_set)
    return length


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''


    def letters_in_secret_word(secret_word):
        letters_in_secret_word = []
        for letters in secret_word:
            if letters in letters_in_secret_word:
                continue
            letters_in_secret_word.append(letters)
        return letters_in_secret_word

    letters_in_secret_word = letters_in_secret_word(secret_word)
    list_of_en_golos = ["a", "e", "i", "o", "u"]
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have 3 warnings left")
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    while True:
        print("--------------------------------------")
        if guesses_left <= 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)
            break
        print("You have", guesses_left, "guesses left")
        get_available_letters(letters_guessed)
        print("Available letters:", get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter: ")

        if guessed_letter.isalpha():
            guessed_letter = guessed_letter.lower()
        else:
            if warnings_left == 0:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have", warnings_left, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
                continue

        if guessed_letter in letters_guessed:
            if warnings_left == 0:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                warnings_left -= 1
                print("Oops! You've already guessed that letter. You have", warnings_left, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
                continue
        else:
            letters_guessed.append(guessed_letter)

        if guessed_letter in letters_in_secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            if guessed_letter in list_of_en_golos:
                guesses_left -= 2
            else:
                guesses_left -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses_left * score(secret_word, letters_guessed)
            print("Congratulations, you won! Your total score for this game is:", total_score)
            break


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word_list = []
    other_word_list = []

    for x in my_word:
        if x == ' ':
            continue
        my_word_list.append(x)

    for x in other_word:
        other_word_list.append(x)

    if len(my_word_list) != len(other_word_list):
        return False

    for x in range(0, len(my_word_list)):
        if my_word_list[x] == '_' or my_word_list[x] == other_word_list[x]:
            continue
        else:
            return False

    my_word_list_without_gaps = []
    for x in my_word_list:
        if x == '_':
            continue
        else:
            my_word_list_without_gaps.append(x)

    my_word_list = my_word_list_without_gaps

    for x in range(0, len(my_word_list)):
        z = my_word_list.count(my_word_list[x])
        y = other_word_list.count(my_word_list[x])
        if z == y:
            continue
        else:
            return False

    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    hint_list = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            hint_list.append(other_word)
    if hint_list == []:
        print("No matches found")
    else:
        print("Possible word matches are:", ' '.join(hint_list))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    secret_word_list = [secret_word[i:i + 1] for i in range(0, len(secret_word))]
    tries = 6
    warnings = 3
    letters_guessed_list = []
    letters = []
    text = ""
    vowels_list = ["a", "e", "i", "o", "u"]
    check = "_ " * len(secret_word)
    print("Welcom to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings, "warnings left.")
    print('You have also 1 hint. Enter "*" to use it.')
    while True:
        print("-" * 13)
        print("You have", tries, "guesses left.")
        print("Available letters:", get_available_letters(letters))
        letters_guessed = str(input("Please guess a letter: ")).lower()
        if len(letters_guessed) == 1:
            if letters_guessed in letters:
                if warnings > 0:
                    warnings -= 1
                else:
                    warnings = "no"
                    text = " so you lose one guess"
                    tries -= 1
                if letters_guessed == "*":
                    print("Oops! You've already used your hint. You have", warnings, "warnings left" + text + ":",
                          check)
                else:
                    print("Oops! You've already guessed that letter. You have", warnings, "warnings left" + text + ":",
                          check)
            elif letters_guessed == "*":
                show_possible_matches(check)
            elif letters_guessed not in string.ascii_lowercase:
                if warnings > 0:
                    warnings -= 1
                else:
                    warnings = "no"
                    text = " so you lose one guess"
                    tries -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:", check)
            elif letters_guessed in secret_word_list:
                letters_guessed_list.append(letters_guessed)
                check = get_guessed_word(secret_word, letters_guessed_list)
                print("Good guess:", check)
            elif letters_guessed not in secret_word_list:
                if letters_guessed in vowels_list:
                    tries -= 2
                else:
                    tries -= 1
                check = get_guessed_word(secret_word, letters_guessed_list)
                print("Oops! That letter is not in my word:", check)
            letters.append(letters_guessed)
        elif len(letters_guessed) < 1:
            if warnings > 0:
                warnings -= 1
            else:
                warnings = "no"
                text = " so you lose one guess"
                tries -= 1
            print("Oops! Don't leave a blank line. You have", warnings, "warnings left:", check)
        else:
            if warnings > 0:
                warnings -= 1
            else:
                warnings = "no"
                text = " so you lose one guess"
                tries -= 1
            print("Oops! Don't enter more than one symbol. You have", warnings, "warnings left:", check)
        if tries == 0:
            print("-" * 13)
            print('Sorry, you ran out of guesses. The word was "' + secret_word + '".')
            break
        if secret_word == check:
            score = tries * len(set(secret_word))
            print("-" * 13)
            print("Congratulations, you won! Your total score for this game is:", score)
            break
    return


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)