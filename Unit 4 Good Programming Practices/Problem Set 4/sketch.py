from py_tools import *
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


words_filename = 'words.txt'


def loadWords(filename):
    with open(filename) as f:
        words_list = []
        l = f.readlines()
        for line in l:
            words_list.append(line.strip().lower())
    log('Loading word list from file...\n   {} words loaded.'.format(len(words_list)))
    return words_list


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    d = {}
    for i in sequence:
        d[i] = d.get(i, 0) + 1
    return d


#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    result = 0
    for i in word:
        result += int(SCRABBLE_LETTER_VALUES[i])
    result *= len(word)
    if len(word) == n:
        result += 50
    return result


#
# Problem #2: Update a hand by removing letters
#


def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
        displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for k, v in hand.items():
        for i in range(v):
            log(k, end=' ')
    log()


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    vowels_number = n // 3
    hand = {}

    for i in range(vowels_number):
        letter = VOWELS[random.randrange(len(VOWELS))]
        hand[letter] = hand.get(letter, 0) + 1

    for i in range(vowels_number, n):
        letter = CONSONANTS[random.randrange(len(CONSONANTS))]
        hand[letter] = hand.get(letter, 0) + 1

    return hand


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    hand1 = hand.copy()
    for i in word:
        hand1[i] -= 1
    return hand1


# hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# displayHand(hand)  # a q l l m u i
# hand = updateHand(hand, 'quail')
# log(hand)  # {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
# displayHand(hand)  # l m


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand1 = hand.copy()
    wordList = wordList[:]
    word_freq = getFrequencyDict(word)

    if word not in wordList or word == '':
        return False

    for k, v in word_freq.items():
        if hand1.get(k) is None or v < hand[k]:
            return False

    return True


# log(isValidWord('hello', {'h': 1, 'e': 1, 'l': 2, 'o': 1}, ['he', 'll']))
log(isValidWord('hello', {'h': 1, 'e': 1, 'l': 2, 'o': 1}, ['hello', 'apple']))
