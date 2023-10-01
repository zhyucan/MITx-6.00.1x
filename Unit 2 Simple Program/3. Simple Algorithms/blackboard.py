from py_tools import *

# EXAMPLE OF SQUARE ROOT

# low         guess            high
# 1           (1+n)/2           n


def square_root(n):
    epsilon = 0.01
    num_guesses = 0
    low = 1
    high = n
    guess = (low + high) / 2

    while abs(guess**2 - n) >= epsilon:
        num_guesses += 1
        if guess**2 < n:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
        log(guess)

    return 'num_guesses: {}, guess: {}'.format(num_guesses, guess)


# cube root
def cube_root(n):
    epsilon = 0.001
    num_guesses = 0
    low = 1
    high = n
    guess = (low + high) / 2

    while abs(guess ** 3 - n) >= epsilon:
        num_guesses += 1
        if guess ** 3 < n:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
        log(guess)


# n < 1
# low                     high
# 0.25           0.625          1
#
def square_root1(n):
    epsilon = 0.0001
    num_guesses = 0
    low = n
    high = 1
    guess = (low + high) / 2

    while abs(guess**2 - n) >= epsilon:
        num_guesses += 1
        if guess**2 < n:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
        log(guess)

    return 'num_guesses: {}, guess: {}'.format(num_guesses, guess)


def guess_num():
    log('Please think of a number between 0 and 100! ')

    low = 0
    high = 100
    guess = (low + high) // 2
    log('Is your secret number {}?'.format(guess))

    while True:
        check = input("""Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.\n""")
        if check == 'h':
            high = guess
            guess = (low + high) // 2
            log('Is your secret number {}?'.format(guess))
        elif check == 'l':
            low = guess
            guess = (low + high) // 2
            log('Is your secret number {}?'.format(guess))
        elif check == 'c':
            break
        else:
            log('Sorry, I did not understand your input.')

    log("Game over. Your secret number was: {}".format(guess))


def decimal_to_binary(n):
    if n > 0:
        result = '0b'
    elif n < 0:
        result = '-0b'
        n = -n
    else:
        result = '0b0'

    s = ''
    while n != 0:
        remainder = n % 2
        n = n // 2
        # log(n, remainder)
        s = str(remainder) + s

    return result + s


def test_decimal_to_binary():
    ensure_equal(decimal_to_binary(567), '0b1000110111', 'decimal_to_binary 1')
    ensure_equal(decimal_to_binary(24), '0b11000', 'decimal_to_binary 2')
    ensure_equal(decimal_to_binary(0), '0b0', 'decimal_to_binary 3')
    ensure_equal(decimal_to_binary(-23), '-0b10111', 'decimal_to_binary 4')


def __main():
    # square_root(25)
    # cube_root(27)
    # square_root1(0.25)
    # guess_num()
    test_decimal_to_binary()


__main()
