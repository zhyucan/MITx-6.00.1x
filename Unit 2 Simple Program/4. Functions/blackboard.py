from py_tools import *


def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x


# x = 3
# z = f(x)
# log(z)


"""
def func_a():
    print('inside func_a')


def func_b(y):
    print('inside func_b')
    return y


def func_c(z):
    print('inside func_c')
    return z()


print(func_a())
# inside func_a
# None
print(5 + func_b(2))
# inside func_b
# 7
print(func_c(func_a))
# inside func_c
# inside func_a
# None
"""


"""
def f(y):
    x = 1
    x += 1
    print(x)


x = 5
f(x)
print(x)
# 2
# 5


def g(y):
    print(x)
    print(x + 1)


x = 5
g(x)
print(x)
# 5
# 6
# 5


def h(y):
    x = x + 1


x = 5
h(x)
print(x)
# 5
"""


# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print('in g(x): x =', x)
#     h()
#     return x
#
#
# x = 3
# z = g(x)
# log(z)
# in g(x): x = 4


def h(y):
    x = x + 1


x = 5
h(2)
# print x
"""
When you type x inside a function scope, 
the interpreter will first look inside that scope, 
and then look in any higher scopes. 
This come unstuck when you type a line beginning x =... though; 
that says "I'm giving you a new value for x in the current scope". 
So when the right hand side of that also references x, 
the interpreter has already decided that you mean local scope x, 
and so the definition becomes circular.
"""

def g(x):
    x = x + 1
    # print('in g(x): x =', x)
    # return x


x = 3
g(x)

