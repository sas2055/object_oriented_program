"""
# Types of methods:
    there are 3 type of methods in object-oriented programming
-----------------------------------------------------------------------

    1. Instance method
    2. Class method
    3. Static method
==================================================================

1. Instance method:
    - all default methods in python are instance method
    - A method with self is an instance method
-----------------------------------------------------------------


class Sample:
    def m1(self):
        print('m1 method')
    def m2(self):
        print('m2 method')

    # call m1 and m2 in m3 using self reference
    def m3(self):
        self.m1()
        self.m2()
# instance methods are accessible inside and outside
# using self and object ref respectively

s = Sample()
s.m3()
s.m2()
s.m1()
==========================================================================

2. class method:
    - a method used to access class level variables/static variables
----------------------------------------------------------------------

Rules to create a class method:
    - instead of self 'cls' is preferred as a reference variable
    - decorate a method using @classmethod decorator
-------------------------------------------------------------------


class Bank:
    IFSC = 'SBI9898'
    MICR = 5466678

    @classmethod
    def access(cls):
        # now use cls reference to access static variables
        print(cls.IFSC, cls.MICR)
        cls.IFSC = 'BOI767'           # it not an instance variable
        # it is a way to change value of static variable using cls

    def normal(self):
        print(self.IFSC)

b = Bank()
b.access()
print(b.IFSC)
print(b.__dict__)
b.normal()

b2 = Bank()
print(b2.IFSC)
-------------------------------------------------------------------


class Bank:
    pin = 1234

    @classmethod
    def change(cls):
        cls.pin = 4545

    def show(self):
        print('Current pin:', self.pin)

b1 = Bank()
b1.show()

b2 = Bank()
b2.change()
b2.show()

b3 = Bank()
b3.show()
==================================================================

3. Static method:
    - A normal method we can make static using @staticmethod decorator
    - Static method uses constant values those are only available for that method
    - self is not required or any other reference variable is not required
-------------------------------------------------------------------


class Sample:

    # static
    @staticmethod
    def add(a, b):
        print('static method', a+b)

    def m1(self):
        # try to access add method
        self.add(1, 2)

s = Sample()
s.add(10, 20)
s.m1()
------------------------------------------------------------------

class Sample:
    def m1(self, x, y):
        # here x, y are local to m1
        print(x*y)
        # in order to share x, y : make it instance
        self.x = x  # self.x (instance), x(local)
        self.y = y

    def m2(self):
        print(self.x + self.y)

s = Sample()
s.m1(2, 4)
s.m2()
-------------------------------------------------------

# How to supply values through a constructor

class Bank:
    # constructor method
    # dunder method
    # magic method
    def __init__(self): # a method of constructor
        print('Constructor called')

b1 = Bank()
b2 = Bank()
b3 = Bank()
print(dir())

s = 'python'
# print(len(s))
# Dunder method: starts with __ double underscore and ends with __
print(s.__len__())
print(s.__dir__())
-------------------------------------------------------------


class Bank:
    # lets supply some args in a constructor
    def __init__(self, name, balance):
        print('Welcome:', name)
        print('Your current balance is Rs:', balance)


Bank('Amit', 120000)
=================================================================

# Supply the values to init and display in other method


class Bank:
    # lets supply some args in a constructor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show(self):
        print('Welcome:', self.name)
        print('Your current balance is Rs:', self.balance)


# b = Bank('Amit', 120000)
# b.show()
for i in range(5):
    name = input('Enter customer name: ')
    amt = float(input('Enter amount in Rs: '))
    b = Bank(name, amt)
    b.show()
==============================================================
"""