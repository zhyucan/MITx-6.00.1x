from py_tools import *


def oddTuples(aTup):
    result = ()
    for i in range(len(aTup)):
        n = aTup[i]
        if i % 2 == 0:
            result += (n,)
    return result


# a = ('I', 'am', 'a', 'test', 'tuple')
# log(oddTuples(a))
# ('I', 'a', 'tuple')


# https://docs.python.org/3/tutorial/datastructures.html


# def remove_dups(L1, L2):
#     for e in L1:
#         log(e, L1)
#         if e in L2:
#             L1.remove(e)
#
#     log('*******')
#     # log(L1)
#
#
# def remove_dups1(L1, L2):
#     L1_copy = L1[:]
#     for e in L1_copy:
#         log(L1)
#         if e in L2:
#             L1.remove(e)
#
#
# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# remove_dups(L1, L2)
# # remove_dups1(L1, L2)
# # log(L1, L2)


# def te(y):
#     x = 2
#
#
# x = 5
# te(x)
# log(x)
#
#
# def te(y):
#     l.append(4)
#
#
# l = [1, 2]
# te(l)
# log(l)

# def te(y):
#     l = 5
#
#
# l = [1, 2]
# te(l)
# log(l)


# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])
#
#
# testList = [1, -4, 8, -9]
#
#
# def f(a):
#     return a**2
#
#
# applyToEach(testList, f)
#
# log(testList)
# # [1, 16, 64, 81]

# list1 = []
# for i in range(15):
#     if i % 2 == 0:
#         list1.append(i)
#
# log(list1)
#
# list2 = [i for i in range(15) if i % 2 == 0]
#
# log(list2)


# 3 FUNCTIONS TO ANALYZE SONG LYRICS
# lyrics is a list of strings

# 1) create a frequency dictionary mapping str:int
def freq_lyrics(lyrics):
    result = {}
    for i in lyrics:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


ly = ['hello', 'world', 'happy', 'a', 'how', 'world', 'hello', 'a', 'hello', 'a']
# log(freq_lyrics(ly))


# 2) find word that occurs the most and how many times
def most_word(lyrics):
    freq_dict = freq_lyrics(lyrics)
    highest_freq = max(freq_dict.values())

    word_list = []
    for k, v in freq_dict.items():
        if v == highest_freq:
            word_list.append(k)
    return word_list, highest_freq


# log(most_word(ly))


# 3) find the words that occur at least X times

def any_word(lyrics, n):
    freq_dict = freq_lyrics(lyrics)

    word_list = []
    for k, v in freq_dict.items():
        if v == n:
            word_list.append(k)
    return word_list, n

# log(any_word(ly, 3))


def occur_freq(lyrics, x):
    freq_dict = freq_lyrics(lyrics)
    log(freq_dict)
    f = freq_dict.copy()
    nums = set()
    for k, v in f.items():
        if v < x:
            del(freq_dict[k])
        else:
            nums.add(v)
    # log(freq_dict, nums)

    # {'hello': 3, 'world': 2, 'a': 3}
    # [(['hello', 'a'], 3), (['world'], 2)]
    result = []
    for n in nums:
        result.append(any_word(lyrics, n))

    return result


# log(occur_freq(ly, 2))


def occur_freq1(lyrics, x):
    result = []

    while True:
        m = most_word(lyrics)
        if m[1] >= x:
            result += m
            for i in m[0]:
                lyrics = [j for j in lyrics if j != i]
        else:
            break

    log(result)


# occur_freq1(ly, 3)


def how_many(adict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for v in adict.values():
        result += len(v)
    return result


# animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
# how_many(animals)  # 6


def biggest(adict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = 0
    for value in adict.values():
        result = max(result, len(value))
    if result == 0:
        return None
    else:
        return result


# animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
# animals = {'a': []}
# log(biggest(animals))  # 'd'

# memoization
# FIBONACCI WITH A DICTIONARY

# do a lookup first in case already calculated the value
# modify dictionary as progress through function calls

def fib(n, b):
    log('n=', n, 'b=', b)
    if n in b:
        return b[n]
    else:
        ans = fib(n-1, b) + fib(n-2, b)
        b[n] = ans
        return ans


# b = {1: 1, 2: 2, }
# print(fib(4, b))
