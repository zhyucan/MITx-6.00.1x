from py_tools import *


def genSubsets(L):
    """
    get all subsets of a list
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


def fib(n, b):
    """
    memoization
    FIBONACCI WITH A DICTIONARY

    do a lookup first in case already calculated the value
    modify dictionary as progress through function calls
    :param n: 4
    :param b: {1: 1, 2: 2, }
    :return: 5
    """
    # log('n=', n, 'b=', b)
    if n in b:
        return b[n]
    else:
        ans = fib(n - 1, b) + fib(n - 2, b)
        b[n] = ans
        return ans


# O(n log n)
def bisect_search1(L, e):
    # log(L, len(L) // 2)
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1( L[:half], e)
        else:
            return bisect_search1( L[half:], e)


#  O(log n)
def bisect_search2(L, e):
    """keep the list, keep track of pointers"""
    def bisect_search_helper(L, e, low, high):
        # log(low, high, (low + high) // 2)
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] > e:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        elif L[mid] < e:
            return bisect_search_helper(L, e, mid + 1, high)
        else:
            return True
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

# testList = [1,2,3,5,7,9,18,27]
