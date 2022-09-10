"""
# 2. Encapsulation
    - Means its Data hiding
    - Members of a program are bind inside a container
--------------------------------------------------------------------------


class Sample:
    x = 10
    y = 'simba'

    def m1(self):
        print('sample class method m1')
# m1() and x, y presents inside a class
# those are not accessible outside directly
# bcz they are encapsulated inside a container and that container is a class


s = Sample()
s.m1()
print(s.y)
print(s.x)
==============================================================================

# Access modifiers:
    - these are 3 types of access modifier
    - public, private, protected
------------------------------------------------------------------

1. Public:
    - these variables or methods available anywhere within the program and
to its subclass as well.
----------------------------------------------------------------------

2. Private:
    - these variables or methods are available only within the class
outside the class it won't be available.
---------------------------------------------------------------------

3. Protected:
    - these variables or methods are available within the same class and to its
subclass.
=====================================================================

# Que. Do python have access modifiers?
==> NO, But we can implement it using _ underscore convention
===================================================================


class Sample:
    x = 'public'
    _y = 'protected'
    __z = 'private'

    def m1(self):
        print(Sample.__z)


Sample().m1()


class Test:
    print(Sample.x)
    print(Sample._y)
=================================================================


class Sample:
    x = 'public'        # directly anywhere
    _y = 'protected'    # indirectly anywhere
    __z = 'private'


s  = Sample()
print(s.x)      # accessible
print(s._y)     # accessible indirectly
print(s.__z)    # not accessible
========================================================================

# Methods:


class Sample:
    def m1(self):
        print('public method')

    def _m2(self):
        print('Protected method')

    def __m3(self):
        print('Private method')

# try to access using object


s = Sample()
# public and protected methods will be available
s.m1()
s._m2()
# but private not
s.__m3()
=========================================================================

# Still if i want to access private method outside
then use 'Name Mangling technique'
    - It is used to store a private variable in dir structure
    and same is used to access private members outside a class
    - it helps to access the class variables from outside the class.
    - The class variables can be accessed by adding _className to it.
    - it is closest to private not exactly private.
    - the process was done by the Interpreter.
-----------------------------------------------------------------

ex. _className__variableName
    _className__methodName()
----------------------------------------------------------------


class Sample:
    a = 40
    b = 60
    __x = 'private variable'

    def __m1(self):
        print('Private method')


s = Sample()
print(dir(Sample))
print(s._Sample__x)
s._Sample__m1()
========================================================================
# Using Data Encapsulation


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print('Selling Price: {}'.format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()
# change the price
c.__maxprice = 1000
c.sell()
# using setter function
c.setMaxPrice(1000)
c.sell()
==========================================================================
"""