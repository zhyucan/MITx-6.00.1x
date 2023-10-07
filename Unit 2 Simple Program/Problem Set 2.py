from py_tools import *

# Problem 1
"""
balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

monthlyInterestRate = annualInterestRate / 12
miniMonthlyPayment = monthlyPaymentRate * balance
monthlyUnpaidBalance = balance - miniMonthlyPayment
interest = monthlyUnpaidBalance * monthlyInterestRate

balance = monthlyUnpaidBalance + interest
"""


def remain_balance(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        monthlyInterestRate = annualInterestRate / 12
        miniMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - miniMonthlyPayment
        interest = monthlyUnpaidBalance * monthlyInterestRate

        balance = monthlyUnpaidBalance + interest
        # log(round(balance, 2))
    log('Remaining balance: {}'.format(round(balance, 2)))


# remain_balance(42, 0.2, 0.04)
# Remaining balance: 31.38

# remain_balance(484, 0.2, 0.04)
# Remaining balance: 361.61


# Problem 2
"""
balance = 5000
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
miniFixedMonthlyPayment = ???
monthlyUnpaidBalance = balance - miniFixedMonthlyPayment
interest = monthlyUnpaidBalance * monthlyInterestRate

balance = monthlyUnpaidBalance + interest
"""


def lowest_pay(balance, annualInterestRate):
    balance1 = balance
    guess = 0
    num_guesses = 0
    while True:
        num_guesses += 1
        # log(balance1)
        for i in range(12):
            monthlyInterestRate = annualInterestRate / 12
            monthlyUnpaidBalance = balance1 - guess
            interest = monthlyUnpaidBalance * monthlyInterestRate
            balance1 = monthlyUnpaidBalance + interest
        guess += 10
        # log(num_guesses, balance1)

        if balance1 < 0:
            break

        balance1 = balance

        # log(guess, balance1)

    log('Lowest Payment: {}'.format(guess-10))


# lowest_pay(3329, 0.2)
# Lowest Payment: 310

# lowest_pay(4773, 0.2)
# Lowest Payment: 440

# lowest_pay(3926, 0.2)
# Lowest Payment: 360


# Problem 3 - bisection search
"""
balance = 5000
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
miniFixedMonthlyPayment = ???
monthlyUnpaidBalance = balance - miniFixedMonthlyPayment
interest = monthlyUnpaidBalance * monthlyInterestRate

balance = monthlyUnpaidBalance + interest


Monthly payment lower bound = balance / 12
Monthly payment upper bound = (balance x (1 + monthlyInterestRate)**12) / 12.0
"""


def lowest_pay1(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12
    lower = balance / 12
    upper = (balance * (1 + monthlyInterestRate)**12) / 12
    guess = (lower + upper) / 2
    epsilon = 0.01
    num_guesses = 0
    # guess = 30000

    balance1 = balance

    while abs(balance1) > 0.01:
        balance1 = balance
        num_guesses += 1

        for i in range(12):
            monthlyInterestRate = annualInterestRate / 12
            monthlyUnpaidBalance = balance1 - guess
            interest = monthlyUnpaidBalance * monthlyInterestRate
            balance1 = monthlyUnpaidBalance + interest

        if balance1 > 0:
            lower = guess
            guess = (lower + upper) / 2
        else:
            upper = guess
            guess = (lower + upper) / 2

    # log(num_guesses, guess, balance1)
    log('Lowest Payment: {}'.format(round(guess, 2)))


# lowest_pay1(320000, 0.2)
# Lowest Payment: 29157.09

# lowest_pay1(999999, 0.18)
# Lowest Payment: 90325.03

