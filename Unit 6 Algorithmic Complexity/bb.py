from py_tools import *
from random import shuffle


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


# log(genSubsets([1, 2, 3, 4]))


def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n - 1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii


# log(fib_iter(2500))


# LINEAR SEARCH ON SORTED LIST
# def search(L, e):
#     for i in range(len(L)):
#         if L[i] == e:
#             return True
#         if L[i] > e:
#             return False
#     return False


def bisect_search1(L, e):
    # log(L, len(L) // 2)
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)


def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        log(low, high, (low + high) // 2)
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
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


# L = [1, 3, 6, 7, 9, 10, 100, 101, 102]
# log(bisect_search2(L, 6))


def bogo_sort(L):
    num = 0
    while L != [1, 2, 3, 5, 7, 9, 18, 27]:
        num += 1
        shuffle(L)
    return num


# l = [2, 27, 9, 7, 18, 3, 1, 5]
# log(bogo_sort(l))


def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                swap = False
                l[i], l[i + 1] = l[i + 1], l[i]
        # log(l)


# l = [2, 27, 9, 7, 18, 3, 1, 5]
# bubble_sort(l)


def selection_sort(L):
    for i in range(0, len(L)):
        # log(L)
        for j in range(i, len(L)):
            if L[j] < L[i]:
                L[i], L[j] = L[j], L[i]


# l = [2, 27, 9, 7, 18, 3, 1, 5]
# selection_sort(l)
# log(l)


def mySort(L):
    clear = False
    while not clear:
        clear = True
        for i in range(1, len(L)):
            if L[i - 1] > L[i]:
                clear = False
                L[i], L[i - 1] = L[i - 1], L[i]


def newSort(L):
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]


# l = [2, 27, 9, 7, 18, 3, 1, 5]
# mySort(l)
# log(l)


def merge(left, right):
    res = []
    i1 = i2 = 0
    while True:
        # log(res)
        item1, item2 = left[i1], right[i2]
        if item1 < item2:
            res.append(item1)
            i1 += 1
        else:
            res.append(item2)
            i2 += 1

        if res[-1] == left[-1]:
            res.extend(right[i2:])
            break
        elif res[-1] == right[-1]:
            res.extend(left[i1:])
            break

    return res


# log(merge([1, 5, 12, 18, 19, 20], [2, 3, 4, 17]))


def merge_sort(L):
    if len(L) < 2:
        return L.copy()
    i = len(L) // 2
    return merge(merge_sort(L[:i]), merge_sort(L[i:]))


# l = [8, 4, 1, 6, 5, 9, 2, 0]
# log(merge_sort(l))

