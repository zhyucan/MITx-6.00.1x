from py_tools import *


# MULTIPLICATION
# “multiply a * b” is equivalent to “add a to itself b times”
def mult_iter(a, b):
    result = 0
    while b >= 1:
        result += a
        b -= 1
    return result

# log(mult_iter(2, 8))


def mult(a, b):
    if b == 1:
        return a
    return a + mult(a, b-1)


# log(mult(2, 999))


# FACTORIAL
# n! = n*(n-1)*(n-2)*(n-3)* … * 1
def fac_iter(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result


# log(fac_iter(5))


def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


# log(fac(5))


# 最大公约数
def gcd_iter(a, b):
    n = min(a, b)
    while n >= 1:
        if a % n == 0 and b % n == 0:
            return n
        n -= 1


# log(gcd_iter(17, 12))


def gcd_recur(a, b):
    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)


# log(gcd_recur(12, 37))


def pure_str(s):
    """
    :param s: Are we not drawn onward, we few, drawn onward to new era?
    :return: convert the string to just lower characters
    """
    result = ''
    for i in s:
        if i.isalpha():
            result += i
    return result.lower()


# s = 'Are we not drawn onward, we few, drawn onward to new era?'
# log(pure_str(s))

# s = pure_str(s)


# palindrome
def is_palindrome(s):
    l = len(s)
    if l in [0, 1]:
        return True
    # log(s)
    return s[0] == s[-1] and is_palindrome(s[1:-1])


# log(is_palindrome(s))


def isIn(char, s):
    """
    char: a single character
    s: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    l = len(s)
    if l == 0:
        return False
    elif l == 1:
        return char == s
    else:
        l = l//2
        middle_char = s[l]
        # log(middle_char)
        if char == middle_char:
            return True
        elif char > middle_char:
            return isIn(char, s[l+1:])
        else:
            return isIn(char, s[:l])


# log(isIn('h', 'abdegkmnpqrtvwz'))


# file1 = open('1to10', 'w')
# for i in range(1, 11):
#     file1.write(str(i) + '\n')
# file1.close()

# file2 = open('1to10', 'r')
# for i in file2:
#     log(i)
# file2.close()
