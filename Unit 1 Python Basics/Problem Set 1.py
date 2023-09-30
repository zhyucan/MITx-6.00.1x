# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 09:14:49 2023

@author: zhyuc
"""

from py_tools import *


# Problem 1

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', 
# your program should print: Number of vowels: 5

# s = 'azcbobobegghakl'
# vowels = 'aeiou'
# num = 0

# for i in s:
#     if i in vowels:
#         num += 1

# print('Number of vowels: ' + str(num))

# Problem 2

# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', 
# then your program should print Number of times bob occurs is: 2

# s = 'azcbobobegghakl'
# l = len(s)
# num = 0

# for i in range(l-2):
#     if s[i:i+3] == 'bob':
#         num += 1

# print('Number of times bob occurs is: {}'.format(num))


# Problem 3
# 0.0/15.0 points (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s 
# in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. 
# For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc


def alphastr(s):
    s = 'azcbobobegghakl'
    alphas = 'abcdefghijklmnopqrstuvwxyz'

    li = []
    l = len(s)
    s1 = s[0]
    while l > 1:
        for i in range(1, l):
            n1, n2 = s[i-1], s[i]
            index1, index2 = alphas.find(n1), alphas.find(n2)
            if index2 > index1:
                s1 += n2
            else:
                s = s[i:]
                break
        log(s1)
        s1 = ''
        # li.append(s1)
    # log(li)


alphastr('azcbobobegghakl')


def test_alpha():
    ensure_equal(alphastr('azcbobobegghakl'), 'beggh', 'alpha 1')
    ensure_equal(alphastr('abcbcd'), 'abc', 'alpha 2')


def __main():
    # test_alpha()
    pass


__main()






























