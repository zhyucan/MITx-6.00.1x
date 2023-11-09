from py_tools import *


# https://stackoverflow.com/questions/3323330/difference-between-object-and-instance

# There are other types of methods such as Static Methods and Class Methods. If you'd like to learn more about them:
#
#     https://realpython.com/blog/python/instance-class-and-static-methods-demystified/
#
#     http://stupidpythonideas.blogspot.com/2013/06/how-methods-work.html (thanks to: Kiwitrader)
#
#     https://docs.python.org/3.6/howto/descriptor.html (thanks to: Kiwitrader)


# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance(self, other):
#         x_diff_sq = (self.x - other.x) ** 2
#         y_diff_sq = (self.y - other.y) ** 2
#         return (x_diff_sq + y_diff_sq) ** 0.5
#
#     # def __str__(self):
#     #     return "<" + str(self.x) + "," + str(self.y) + ">"
#
#     # def __add__(self, num):
#     #     return self.x + num


# c = Coordinate(3,4)
# print(c)
# print(type(c))
# <__main__.Coordinate object at 0x00000291A19EE390>
# <class '__main__.Coordinate'>
# <3,4>
# <class '__main__.Coordinate'>

# print(isinstance(c, object))

# d = Coordinate(5, 4)
# log(d + 10)


# class Weird(object):
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#
#     def getX(self):
#         return x
#
#     def getY(self):
#         return y
#
#
# class Wild(object):
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#
#     def getX(self):
#         return self.x
#
#     def getY(self):
#         return self.y
#
#
# X = 7
# Y = 8


# • print representation
# • add, subtract
# • convert to a float
# class Fraction(object):
#     def __init__(self, numer, denom):
#         self.numer = numer
#         self.denom = denom
#
#     def getNumer(self):
#         return self.numer
#
#     def getDenom(self):
#         return self.denom
#
#     def __str__(self):
#         return '{}/{}'.format(self.getNumer(), self.getDenom())
#
#     def __add__(self, other):
#         numer1 = self.numer * other.denom + other.numer * self.denom
#         denom1 = self.denom * other.denom
#         return Fraction(numer1, denom1)
#
#     def __sub__(self, other):
#         numer1 = self.numer * other.denom - other.numer * self.denom
#         denom1 = self.denom * other.denom
#         return Fraction(numer1, denom1)
#
#     def convert_float(self):
#         return self.numer/self.denom
#
#
# f1 = Fraction(1, 3)
# f2 = Fraction(2, 5)
# log(f1 + f2)  # f1.__add__(f2)
# log(f1 - f2)
# log(f2 - f1)
# log(f1.convert_float())
# log(f2.convert_float())


# interface
# insert(e) – insert integer e into set if not there
# member(e) – return True if integer e is in set, False else
# remove(e) – remove integer e from set, error if not present


# class Intset(object):
#     def __init__(self):
#         self.vals = []
#
#     def __str__(self):
#         return '{}'.format(self.vals)
#
#     def insert(self, e):
#         if e not in self.vals:
#             self.vals.append(e)
#
#     def member(self, e):
#         """
#         dsa
#         :param e:
#         :return:
#         """
#         return e in self.vals
#
#     def remove(self, e):
#         try:
#             self.vals.remove(e)
#         except:
#             log('error')
#
#
# l = Intset()
# log(l)
# l.insert(1)
# l.insert(2)
# l.insert(3)
# log(l)
# log(l.member(2))
# log(l.member(4))
# l.remove(1)
# log(l)
# l.remove(4)
# log(l)


# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def getX(self):
#         # Getter method for a Coordinate object's x coordinate.
#         # Getter methods are better practice than just accessing an attribute directly
#         return self.x
#
#     def getY(self):
#         # Getter method for a Coordinate object's y coordinate
#         return self.y
#
#     def __str__(self):
#         return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
#
#     def __eq__(self, other):
#         assert type(self) == type(other)
#         return self.getX() == other.getX() and self.getY() == other.getY()
#
#     def __repr__(self):
#         # return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
#         return "Coordinate({},{})".format(str(self.getX()), str(self.getY()))
#
#
# c = Coordinate(1, 2)
# log(c.__repr__())


# class intSet(object):
#     """An intSet is a set of integers
#     The value is represented by a list of ints, self.vals.
#     Each int in the set occurs in self.vals exactly once."""
#
#     def __init__(self):
#         """Create an empty set of integers"""
#         self.vals = []
#
#     def insert(self, e):
#         """Assumes e is an integer and inserts e into self"""
#         if not e in self.vals:
#             self.vals.append(e)
#
#     def member(self, e):
#         """Assumes e is an integer
#            Returns True if e is in self, and False otherwise"""
#         return e in self.vals
#
#     def remove(self, e):
#         """Assumes e is an integer and removes e from self
#            Raises ValueError if e is not in self"""
#         try:
#             self.vals.remove(e)
#         except:
#             raise ValueError(str(e) + ' not found')
#
#     def __str__(self):
#         """Returns a string representation of self"""
#         self.vals.sort()
#         return '{' + ','.join([str(e) for e in self.vals]) + '}'
#
#     def intersect(self, other):
#         """return a new intSet of integers that appear in both sets"""
#         result = intSet()
#         result.vals = [i for i in self.vals if other.member(i)]
#         return result
#
#     def __len__(self):
#         return len(self.vals)
#
#
# s1 = intSet()
# s2 = intSet()
# s1.insert(1)
# s1.insert(2)
# s2.insert(4)
# s2.insert(3)
# log(len(s1), len(s2))


# class Animal(object):
#     def __init__(self, age):
#         self.age = age
#         self.name = None
#
#     def get_age(self):
#         return self.age
#
#     def get_name(self):
#         return self.name
#
#     def set_age(self, newage):
#         self.age = newage
#
#     def set_name(self, newname=""):
#         self.name = newname
#
#     def __str__(self):
#         return "animal:" + str(self.name) + ":" + str(self.age)
#
#
# class Person(Animal):
#     def __init__(self, name, age):
#         """
#         如果子类和父类都写了init方法，那么父类的init方法就会被子类覆盖。
#         """
#         # Animal.__init__(self, age)
#         super().__init__(age)
#         # Animal.set_name(self, name)
#         self.set_name(name)
#         self.friends = []
#
#     def get_friends(self):
#         return self.friends
#
#     def add_friend(self, fname):
#         if fname not in self.friends:
#             self.friends.append(fname)
#
#     def speak(self):
#         print("hello")
#
#     def age_diff(self, other):
#         # alternate way: diff = self.age - other.age
#         diff = self.get_age() - other.get_age()
#         if self.age > other.age:
#             print(self.name, "is", diff, "years older than", other.name)
#         else:
#             print(self.name, "is", -diff, "years younger than", other.name)
#
#     def __str__(self):
#         return "person:" + str(self.name) + ":" + str(self.age)
#
#
# eric = Person('Eric', 45)
# john = Person('John', 55)
# eric.speak()
# # Hello
# eric.age_diff(john)
# # Eric is 10 years younger than John
# Person.age_diff(john,eric)
# # John is 10 years older than Eric


# class Spell(object):
#     def __init__(self, incantation, name):
#         self.name = name
#         self.incantation = incantation
#
#     def __str__(self):
#         return self.name + ' ' + self.incantation + '\n' + self.getDescription()
#
#     def getDescription(self):
#         return 'No description'
#
#     def execute(self):
#         print(self.incantation)
#
#
# class Accio(Spell):
#     def __init__(self):
#         Spell.__init__(self, 'Accio', 'Summoning Charm')
#
#     def getDescription(self):
#         return 'This charm summons an object to the caster, potentially over a significant distance.'
#
#
# class Confundo(Spell):
#     def __init__(self):
#         Spell.__init__(self, 'Confundo', 'Confundus Charm')
#
#     def getDescription(self):
#         return 'Causes the victim to become confused and befuddled.'
#
#
# def studySpell(spell):
#     print(spell)


# spell = Accio()
# spell.execute()
# studySpell(spell)
# studySpell(Confundo())


class A(object):
    def __init__(self):
        self.a = 1

    def x(self):
        print("A.x")

    def y(self):
        print("A.y")

    def z(self):
        print("A.z")


class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3

    def y(self):
        print("B.y")

    def z(self):
        print("B.z")


class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5

    def y(self):
        print("C.y")

    def z(self):
        print("C.z")


class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6

    def z(self):
        print("D.z")


# obj = D()
# print(obj.a)
# print(obj.b)
# print(obj.c)
# print(obj.d)
# obj.x()
# obj.y()
# obj.z()


# 2, 3, 5, 7, 11,...
# def Primes():
#     primes_list = [2]
#     i = 2
#     while True:
#         i += 1
#         is_prime = True
#         for prime in primes_list:
#             if i % prime == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield i
#             primes_list.append(i)


def Primes():
    primes_list = [2]
    i = 2
    while True:
        i += 1
        for prime in primes_list:
            if i % prime == 0:
                break
        else:
            yield i
            primes_list.append(i)


# genPrimes = Primes()
# for i in genPrimes:
#     log(i)

