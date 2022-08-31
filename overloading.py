"""
# overloading:
    - it means a method/ operator/ constructor are same but behaves differently.
    - there are three types as follows
    1. operator overloading
    2. method overloading
    3. constructor overloading
---------------------------------------------------------------------------

1. operator overloading:
    - we can use same operator for multiple purpose which is nothing but operator overloading
    - we can implement different behaviour of an operator(+, -, *, /, %)
    - method with __ double underscore at the prefix and suffix side are
    used to indicate them as a special method then it is called as
    'DUNDER METHOD' or 'UNDERSCORE METHOD'.
    - also they are known as 'MAGIC METHOD'.
    - it is possible then python overloading
-----------------------------------------------------------------------------

# to check all magic method to use dir
print(dir(int(10)))
----------------------------------------------------------------------------


class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


a1 = Book(100)
a2 = Book(200)
print(a1 + a2)
===========================================================================


class Book:
    def __init__(self, pages):
        self.pages = pages

    def __mul__(self, other):
        return self.pages * other.pages


a1 = Book(100)
a2 = Book(200)
print(a1 * a2)
==========================================================================


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b


Ob1 = Complex(1, 2)
Ob2 = Complex(2, 3)
print(Ob1 + Ob2)
======================================================================

2. method overloading:
    - it is also known as method level polymorphism
    - if two or three method having same name but different type of attributes
    then this method said to be method overloading.
    - it is always consider last recent declaration or method from a class;
    - python can not perform or is not possible method overloading.
--------------------------------------------------------------------------------


class Sample:
    def m1(self):
        print('No arguments')

    def m1(self, a, b):
        print(a, ',', b, 'are two variables')


s = Sample()
# s.m1()   # type error
s.m1(12, 34)
======================================================================

3. constructor overloading:
    - it is also known as constructor level polymorphism
    - Constructor is not a return value.
    - if we define multiple constructor in class having same name but different
    type of attributes then we can say as constructor overloading.
    - it is always consider last recent declaration or method from a class;
    - python can not perform or is not possible constructor overloading.
-----------------------------------------------------------------------------------


class Sample:
    def __init__(self):
        print(0)

    def __init__(self, a, b, c):
        print(a, b, c)

    def __init__(self, x):
        print(x)


# Sample(1, 2, 3)  # type error
Sample(23)
============================================================================

"""
