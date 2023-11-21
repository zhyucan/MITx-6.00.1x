from py_tools import *

"""
## Problem 3:  
Implement a function that meets the specifications below.

def sum_digits(s):
    ''' assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. '''
    # Your code here

For example, sum_digits("a;35d4") returns 12.
"""


def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    res = 0
    is_digits = False
    for i in s:
        if i.isdigit():
            is_digits = True
            res += int(i)
    if not is_digits:
        raise ValueError(f'there are no digits in {s}')
    else:
        return res


# log(sum_digits("a;35d4"))
# log(sum_digits('asdgrioe'))


"""
## Problem 4:  
Implement a function that meets the specifications below.

def max_val(t): 
    ''' t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t ''' 
    # Your code here

For example:  
  
• max_val((5, (1,2), [[1],[2]])) returns 5.  

• max_val((5, (1,2), [[1],[9]])) returns 9.
"""


def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    if isinstance(t, int):
        return t
    return max([max_val(i) for i in t])


# log(max_val((5, (1, 2), [[1], [2]])))  # 5
# log(max_val((5, (1, 2), [[1], [9]])))  # 9

"""
## Problem 5:  
Implement a function that meets the specifications below.

def cipher(map_from, map_to, code):
    ''' map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. '''
    # Your code here

For example:  
  
• cipher("abcd", "dcba", "dab") returns ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
  
*(Note: order of entries in dictionary may not be the same)*
"""


def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """
    # key_code = {map_from[i]: map_to[i] for i in range(len(map_from))}
    key_code = {i: j for i, j in zip(map_from, map_to)}
    decoded = ''.join([key_code[i] for i in code])
    return key_code, decoded


# ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
# log(cipher("abcd", "dcba", "dab"))


'''
## Problem 6-1:  
You are given the following superclass. Do not modify this.

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

Write a class that implements the specifications below. Do not override any methods of Container.

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        # write code here

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # write code here

For example:  
  
d1 = Bag()
d1.insert(4)
d1.insert(4)
print(d1)
d1.remove(2)
print(d1)

Prints:

4:2
4:2

And

d1 = Bag()
d1.insert(4)
d1.insert(4)
d1.insert(4)
print(d1.count(2))
print(d1.count(4))

Prints:

0
3
'''


class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """

    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}

    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1

    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i) + ":" + str(self.vals[i]) + "\n"
        return s


class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        if e in self.vals:
            return self.vals[e]
        else:
            return 0

    def __add__(self, other):
        for i in other.vals:
            if i in self.vals:
                self.vals[i] += other.vals[i]
            else:
                self.vals += i

        return self


# d1 = Bag()
# d1.insert(4)
# d1.insert(4)
# print(d1)
# d1.remove(2)
# print(d1)
# # 4:2
# # 4:2
#
# d2 = Bag()
# d2.insert(4)
# d2.insert(4)
# d2.insert(4)
# print(d2.count(2))
# print(d2.count(4))
# # 0
# # 3


'''
## Problem 6-2:  
Write a method in Bag such that if b1 and b2 were bags
then b1+b2 gives a new bag representing the union of the two bags.

For example:  
  
a = Bag()
a.insert(4)
a.insert(3)
b = Bag()
b.insert(4)
print(a+b)

Prints:

3:1
4:2
'''

# a = Bag()
# a.insert(4)
# a.insert(3)
# b = Bag()
# b.insert(4)
# print(a+b)
# # 3:1
# # 4:2


'''
## Problem 6-3:  
Write a class that implements the specifications below. Do not override any methods of Container.
  
class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here
        
For Example:

d1 = ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
print(d1)

d1.remove(4)
print(d1)

Prints:

4:2 # from d1.remove(2) print

    # (empty) from d1.remove(4) print

And:

d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))

Prints:

True
True
False
'''


class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        try:
            self.vals.pop(e)
        except:
            pass

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        return e in self.vals


# d1 = ASet()
# d1.insert(4)
# d1.insert(4)
#
# d1.remove(2)
# print(d1)
#
# d1.remove(4)
# print(d1)
# # 4:2 # from d1.remove(2) print
# #
# #     # (empty) from d1.remove(4) print
#
#
# d1 = ASet()
# d1.insert(4)
# print(d1.is_in(4))
# d1.insert(5)
# print(d1.is_in(5))
# d1.remove(5)
# print(d1.is_in(5))
# # True
# # True
# # False
