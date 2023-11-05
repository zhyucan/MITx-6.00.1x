from functools import reduce
from py_tools import *


# str -> int
# '12359' -> 12359
# str -> float
# '123.456' -> 123.456

def str2int(s):
    """
    :param s: '12359'
    :return: 12359
    """
    def f(x, y):
        return x * 10 + y
    return reduce(f, map(int, s))


"""
x * 0.1 + y * 0.1
0.6 5
0.56
0.56 4
0.456
"""


def str2float(s):
    """
    :param s: '456'
    :return: 0.456
    """
    def f(x, y):
        return x * 0.1 + y * 0.1
    l = list(map(int, s[::-1]))
    l[0] *= 0.1
    return reduce(f, l)


def str2num(s):
    if '.' in s:
        i = s.index('.')
        return str2int(s[:i]) + str2float(s[i+1:])
    else:
        return str2int(s)


def test_str2num():
    ensure_equal(str2num('12359'), 12359, 'test int')
    ensure_equal(str2num('123.456789'), 123.456789, 'test float')


# test_str2num()


# 用filter求回数
def is_palindrome(n):
    result = True
    s = str(n)
    l = len(s)

    for i in range(l // 2):
        if s[i] != s[l-i-1]:
            result = False
            break

    return result


# 04 13
# log(is_palindrome(919))

# log(list(filter(is_palindrome, range(1, 1000))))


# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    return t[1]


# L2 = sorted(L, key=by_score)
# print(L2)


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


# f = lazy_sum(1, 3, 5, 7, 9)
# log(f())  # 25


# x = 0
# def fn():
#     # nonlocal x
#     x = x + 1
#     return x

# fn()


# def logo(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# def now(year):
#     print('{}-3-25'.format(year))


# logo(now)(2022)


# def logo(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# @logo
# def now(year):
#     print('{}-3-25'.format(year))


# now(2022)


class Student(object):

    def __init__(self):
        self._score = None

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# s1 = Student()
# s1.set_score(50)
# log(s1.get_score())


class Student1(object):

    def __init__(self):
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# s2 = Student1()
# s2.score = 50
# log(s2.score)


# 请利用 @property 给一个 Screen 对象加上 width 和 height 属性，
# 以及一个只读属性resolution
class Screen(object):
    def __init__(self):
        self.width = None
        self.height = None

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def resolution(self):
        return self.width * self.height

    @width.setter
    def width(self, w):
        self._width = w

    @height.setter
    def height(self, h):
        self._height = h


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')



