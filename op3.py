"""
# explore self:
    - it acts as pointer/ a reference variable which is responsible for
accessing everything inside class into a method
------------------------------------------------------------------


class Sample:
    def __init__(self, name, age, salary):
        # make instance variable
        self.name = name
        self.age = age
        self.Salary = salary

    def display(self):
        # fetch details from init and display here
        print(self.name, self.age, self.Salary)


s = Sample('Ajit', 22, 80000)
s.display()
# we can check instance variable using __dict__
print(s.__dict__)
==============================================================

# Que. If I want to change variable inside a method
->  yes it is possible using self.
    self makes variables as an instance and instance
variable are those whose value changes from object to object
===============================================================


class Sample:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.Salary = salary

    def display(self):
        self.name= 'Shubham'
        print(self.name, self.age, self.Salary)

s = Sample('Ajit', 22, 80000)
s.display()
# we can check instance var using __dict__
print(s.__dict__)
s2 = Sample('Shivansh', 24, 78000)
print(s2.__dict__)
# from outside change salary
s2.salary = 98000
print(s2.__dict__)
# shivansh want bonus
s2.bonus = 10000
print(s2.__dict__)
================================================================

# Types of variables in OOP:
    there are 4 type of variables in object-oriented programming
----------------------------------------------------------------

    1. Local: method level
    2. Global: outside class
    3. instance: inside instance method
    4. static/class level variable: inside a class and outside a method
==================================================================

1. Local variable:
    - local variable not accessible outside a class.
    - it is confined to it method area where it has been declared.
    - Variables declared inside a method can be used in the same method only.
-----------------------------------------------------------------


class Sample:
    def m1(self):
        x = 100     # local to m1
        print(x)

    def m2(self):
        print(x)    # wont be available in m2
        pass


s = Sample()
print(s.x)
====================================================================

2. Global variable:
    - Variables that are created outside a class
    - We declare a variable global by using the keyword global before a variable
------------------------------------------------------------------
x = 'global'


class Sample:
    print(x)

    def m1(self):
        print(x)


print(x)
s = Sample()
s.m1()
================================================================

3. instance variable:
    - inside an instance method
    - Inside a constructor using self.
    - Outside the class using object reference.
--------------------------------------------------------------------


class Sample:
    def m1(self):
        self.x = 12

    def m2(self):
        print(self.x)


s = Sample()
s.m1()
print(s.x)
s.m2()
=======================================================================

4. static/class level variable:
    - inside a class and outside a method or constructor
    - static variable will not be available inside an instance method
    - it can be accessed using Class name or Object reference.
    - Inside constructor and instance method using className.
    - From outside the class by using class name.
------------------------------------------------------------------------

# className:
    - it acts as a reference for a static variable.
    - which works inside a method and outside a class also
    - use className outside as well to access static variable
    - inside class method using class name or class variable.
--------------------------------------------------------------------------


class Sample:
    st = 'static'

    def m1(self):
        pass

    def m2(self):
        # to access st inside m2 take the help of className reference
        print(Sample.st)


s = Sample()
s.m2()
# can we access static var outside a class
print(s.st)
print(Sample.st)
------------------------------------------------------------------------

# lets try to change static variable using className as a ref.


class Bank:
    ifsc = 'SBI76523' # static var

    def m1(self):
        print(Bank.ifsc)
        # lets change ifsc
        Bank.ifsc = 'PNB45678'


print(Bank.ifsc)
b = Bank()
print(b.ifsc)
# now call m1
b.m1()
print(b.ifsc)
-----------------------------------------------------------------------

# lets try to change static variable using self as a ref.


class Bank:
    ifsc = 'SBI76523' # static var

    def m1(self):
        print(Bank.ifsc)
        # lets change ifsc using self.
        self.ifsc = 'BOI45678'


print(Bank.ifsc)
b = Bank()
print(b.__dict__)
b.m1()
print(b.__dict__)
# lets check ifsc using object
print(b.ifsc)
print(Bank.ifsc)
--------------------------------------------------------------------

class Bank:
    ifsc = 'SBI76523' # static var

    def m1(self):
        print(Bank.ifsc)
        Bank.ifsc = 'BOI45678'


b1 = Bank()
b1.m1()
print(b1.ifsc)
# lets check ifsc using second object
b2 = Bank()
print(b2.ifsc)
---------------------------------------------------------------

# not using calling then output


class Bank:
    print('hello')

    def m1(self):
        pass

    def m2(self):
        pass
-----------------------------------------------------------------


class Bank:
    print('hello')

    def m1(self):
        print('m1 called')

    def m2(self):
        print('m2 called')

b = Bank()
b.m1()
b.m2()
================================================================
"""
