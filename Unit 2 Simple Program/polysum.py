from py_tools import *
import math


def sum(n, s):
    return ((n/4)*(s**2))/(math.tan(math.pi/n))


def perimeter(n, s):
    return n * s


def polysum(n, s):
    return round(sum(n, s) + perimeter(n, s)**2, 4)
