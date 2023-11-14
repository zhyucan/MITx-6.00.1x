from py_tools import *


def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        los(i, result)
        result = digits[i % 10] + result
        i = i // 10
    return result


# log(intToStr(13269))


def genSubsets(L):
    """
    get all subsets
    :param L: [1, 2, 3]
    :return: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    """
    if len(L) == 0:
        return [[]]  # list of empty list
    smaller = genSubsets(L[:-1])  # all subsets without last element
    extra = L[-1:]  # create a list of just last element
    new = []
    for small in smaller:
        new.append(small + extra)  # for all smaller solutions, add one with last element
    return smaller + new  # combine those with last element and those without


log(genSubsets([1, 2, 3, 4]))



