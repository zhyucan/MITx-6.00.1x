from py_tools import *

"""
Note that problems 1 - 3 were multiple choice and excluded here.
"""


"""
Problem 4:
Write a function is_triangular that meets the specification below.
A triangular number is a number obtained by the continued summation of integers starting from 1.
For example, 1, 1+2, 1+2+3, 1+2+3+4, etc.,
corresponding to 1, 3, 6, 10, etc., are triangular numbers.

Test Cases:
1, 2, 3, 4,  5,  6,  7,  8,  9,  10
1, 3, 6, 10, 15, 21, 28, 36, 45, 55
"""


def is_triangular(n):
    triangular_list = []
    s = 0
    for i in range(1, n+1):
        s += i
        triangular_list.append(s)
        # log(triangular_list)
    return n in triangular_list


# def test_is_triangular():
#     ensure(is_triangular(1), 'test_is_triangular 1')
#     ensure(not is_triangular(2), 'test_is_triangular 2')
#     ensure(not is_triangular(5), 'test_is_triangular 3')
#     ensure(is_triangular(6), 'test_is_triangular 4')


# test_is_triangular()


"""
Problem 5:
Write a Python function that takes in a string and prints out a version of this string 
that does not contain any vowels, according to the specification below. 
Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

For example, if s = "This is great!" then print_without_vowels will print Ths s grt!. 
If s = "a" then print_without_vowels will print the empty string .
"""


def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([i for i in s if i not in vowels])


# log(remove_vowels("This is great!"))  # 'Ths s grt!'
# log(remove_vowels('A'))  # ''


"""
Problem 6:
Write a function that satisfies the following docstring:

def largest_odd_times(L):
    ''' Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None '''
    # Your code here

For example, if:

largest_odd_times([2,2,4,4]) returns None  
largest_odd_times([3,9,5,3,5,3]) returns 9
"""


def largest_odd_times(L):
    """
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number of times in L.
    If no such element exists, returns None
    """
    char_times = {}
    for i in L:
        char_times[i] = L.count(i)

    char_times1 = char_times.copy()
    for k, v in char_times1.items():
        if v % 2 == 0:
            del(char_times[k])

    if char_times == {}:
        return None
    else:
        return max(char_times.keys())


# log(largest_odd_times([2, 2, 4, 4]))  # None
# log(largest_odd_times([3, 9, 5, 3, 5, 3]))  # 9
# log(largest_odd_times([3, 9, 5, 3, 5, 3, 9]))  # 3


"""
Problem 7:
Write a function called dict_invert that takes in a dictionary 
with immutable values and returns the inverse of the dictionary. 
The inverse of a dictionary d is another dictionary 
whose keys are the unique dictionary values in d. 
The value for a key in the inverse dictionary is a sorted list 
(increasing order) of all keys in d that have the same value in d.

Here are two examples:

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
"""


def dict_invert(d):
    result = {}
    for k, v in d.items():
        if result.get(v) is None:
            result[v] = [k]
        else:
            result[v].append(k)
    return {k: sorted(v) for k in result.keys() for v in result.values()}


# log(dict_invert({1: 10, 2: 20, 3: 30}))  # {10: [1], 20: [2], 30: [3]}
# log(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))  # {10: [1], 20: [2], 30: [3, 4]}
# log(dict_invert({4: True, 2: True, 0: True}))  # {True: [0, 2, 4]}


"""
Problem 8:
Write a function called general_poly, that meets the specifications below. 
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 
because 1∗10^3+2∗10^2+3∗10^1+4∗10^0.
"""


def general_poly(l):
    def f(n):
        result = 0
        for i in l:
            result += i * n**(l[-1] - i)
        return result
    return f


# log(general_poly([1, 2, 3, 4])(10))  # 1234


"""
Problem 9:
Write a Python function that takes in two lists 
and calculates whether they are permutations of each other. 
The lists can contain both integers and strings. 
We define a permutation as follows:

- the lists have the same number of elements
- list elements appear the same number of times in both lists

If the lists are not permutations of each other, the function returns False.
If they are permutations of each other, 
the function returns a tuple consisting of the following elements:

- the element occuring the most times
- how many times that element occurs
- the type of the element that occurs the most times

If both lists are empty return the tuple (None, None, None). 
If more than one element occurs the most number of times, you can return any of them.


*For example: *

if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False  
  
if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] 
then is_list_permutation returns (1, 3, <class 'int'>) 
because the integer 1 occurs the most, 3 times, and the type of 1 is an integer 
(note that the third element in the tuple is not a string).
"""


def is_list_similar(l1, l2):
    result = False
    if len(l1) == len(l2):
        for i in l1:
            if i in l2:
                l2.remove(i)
    if not l2:
        result = True
    return result


def is_list_permutation(l1, l2):
    if l1 == l2 == []:
        return None
    elif is_list_similar(l1, l2):
        d = {k: l1.count(k) for k in l1}
        # log(d)
        n = max(d.values())
        item = next((k for k, v in d.items() if v == n), None)
        return item, n, type(item)
    else:
        return False


l1 = ['a', 'a', 'b']
l2 = ['a', 'b']
log(is_list_permutation(l1, l2))  # False

l1 = [1, 'b', 1, 'c', 'c', 1]
l2 = ['c', 1, 'b', 1, 1, 'c']
log(is_list_permutation(l1, l2))  # (1, 3, <class 'int'>)

