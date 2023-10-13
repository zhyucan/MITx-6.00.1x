# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
from py_tools import *

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    pass


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    pass


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    pass
    

def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    l = len(secretWord)
    world_display = '_' * l
    log("Welcome to the game, Hangman!\nI am thinking of a word that is {} letters long.".format(l))
    guesses = 8
    avilable = 'abcdefghijklmnopqrstuvwxyz'
    log('-------------')

    while True:
        log("You have {} guesses left.".format(guesses))
        log("Available letters: {}".format(avilable))
        char = input('Please guess a letter: ')
        if char in avilable:
            if char in secretWord:
                s = ''
                for i in range(l):
                    n = secretWord[i]
                    if char == n:
                        s += char
                    else:
                        s += world_display[i]
                world_display = s
                log("Good guess: {}".format(world_display))
            else:
                log("Oops! That letter is not in my word: {}".format(world_display))
                guesses -= 1
            avilable = ''.join(avilable.split(char))
        else:
            log("Oops! You've already guessed that letter: {}".format(world_display))

        log('-------------')

        if world_display == secretWord:
            log('Congratulations, you won!')
            break
        elif guesses == 0:
            log('Sorry, you ran out of guesses. The word was else.')
            break


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
# secretWord = 'else'
hangman(secretWord)
