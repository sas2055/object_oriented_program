"""
# using class


class Tea:
    water = 1
    sugar = 0.5
    milk = 0.5
    tea_powder = 1

    def mixing(self):
        print('Its mixing process')

    def boiling(self):
        print('boiling process')

    def add_milk(self):
        print('milk adding process')

    def serv(self):
        print('its serving process')


print(Tea().milk, '\n', Tea().sugar)
print(Tea().water, '\n', Tea().tea_powder)
Tea().mixing()
Tea().boiling()
Tea().add_milk()
Tea().serv()
======================================================================

# using object


class Tv:
    pass

    def on_switch(self):
        print('Its tv on process')

    def change(self):
        print('its changing channel process')

    def watch(self):
        print('its tv watching process')


a = Tv()
a.on_switch()
a.change()
==========================================================



class Market:
    tomato = 2
    potato = 1
    flower = .5

    def buy(self):
        print('Its buying process')

    def money(self):
        print('its grant money process')

    def home(self):
        print('its back to home process')


m1 = Market()
print(m1.potato, '\n', m1.tomato)
m1.home()
print('------------------------------------')
m2 = Market()
m2.garlic = 1
m2.red_chilli = 1
print(m2.__dict__)
print(m2.garlic)
m2.buy()
print(dir(m1))
print(dir(m2))
print('--------lets delete some variables-----')
del m2.garlic
print(m2.__dict__)
print(m2.garlic)
==================================================================
# using __init__ method


class Person:
    def __init__(self, name, age):
        print('my name is', name, 'and age is', age)
        self.name = name
        self.age = age


p1 = Person('Kajal', 30)
print(p1.name)
print(p1.age)
==================================================================
# Creating Class and Object in Python


class Dog:
    a = 'mammal'

    def __init__(self):
        print('Dog is a mammal animal')

    def speak(self):
        pass


Dog()
=========================================================


class Dog:
    # class attribute
    attr1 = 'mammal'

    # Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('Dog is', Dog.attr1, 'animal')
        print('Dog name is', self.name, 'and age is', self.age)


d = Dog('tommy', 3)
d.bark()
d.name = 'raja'
print(d.__dict__)
print('Dog name is', d.name)
del d.age
print(d.__dict__)
=========================================================
# Creating methods


class Parrot:
    def __init__(self, name):
        self.name = name

    def sing(self, song):
        print(self.name, 'sings', song)

    def dance(self):
        print(self.name, 'is now dancing')


p = Parrot('Fig')
q = Parrot('Vasa')
p.dance()
print(p.__dict__)
q.sing('happy')
print(q.__dict__)
q.age = 45
print(q.__dict__)
print('Parrot age is', q.age)
del p.name
print(p.__dict__)
==================================================================
# use positional arguments:


class Bank:
    def __init__(self, name, bank_name, branch, ac_no):
        print('My name is: ', name)
        print('bank name is', bank_name, 'and branch is', branch)
        print('bank account number is', ac_no)


Bank('Ajit', 'Bank of India', 'Mumbai', 11000273416)
-----------------------------------------------------------------


class Bank:
    def __init__(self, name, bank_name, branch, ac_no):
        print('My name is: ', name)
        self.bank_name = bank_name
        self.branch = branch
        self.ac_no = ac_no

    def details(self):
        print('bank name is', self.bank_name, 'and branch is', self.branch)
        print('bank account number is', self.ac_no)


b = Bank('Shivansh', 'Bank of Maharashtra', 'Pune', 60273412566)
b.details()
print(b.__dict__)
b.ifsc = 'BOM12345'
print(b.__dict__)
print('bank ifsc is', b.ifsc)
del b.ac_no
print(b.__dict__)
==================================================================
# Use keyword argument:


class Bank:
    def __init__(self, name, bank_name, branch, ac_no):
        print('My name is: ', name)
        print('bank name is', bank_name, 'and branch is', branch)
        print('bank account number is', ac_no)


Bank('Ajit', branch='Mumbai', ac_no=11000273416, bank_name='State Bank of India')
------------------------------------------------------------------------------


class Bank:
    def __init__(self, name, bank_name, branch):
        self.name = name
        self.bank_name = bank_name
        self.branch = branch

    def details(self):
        print('My name is: ', self.name)
        print('bank name is', self.bank_name, 'and branch is', self.branch)


b = Bank('Vijay', branch='Mumbai', bank_name='State Bank of India')
b.details()
print(b.__dict__)
b.ifsc = 'BOM12345'
print('bank ifsc is', b.ifsc)
b.ac_no = 34251237687
print('bank account number is', b.ac_no)
print(b.__dict__)
del b.ac_no
del b.bank_name
print(b.__dict__)
===============================================================================
# Use default arguments


class Vegetable:
    def __init__(self, name, taste='bitter'):
        print('Name is', name, 'and test is', taste)


Vegetable('bitter gourd')
Vegetable('green chily', 'spicy')
Vegetable('carrot')
------------------------------------------------------------------
# Positional variable length argument:


class Laptop:
    def __init__(self, *args):
        print(args)


Laptop('Dell', 45000)
Laptop('Hp', 43000)
----------------------------------------------------------------
# Keyword variable length argument:


class Student:
    def __init__(self, **kwargs):
        print(kwargs)


Student(name='Deep', roll_no=22)
Student()
-------------------------------------------------------------------


class Sample:
    def info(self, name, roll_no, std):
        print('my name is', name, 'my roll number is', roll_no, 'and my standard is', std)


Sample().info('Ash,', 10, '8th')
=====================================================================
# Using static variable and instance variable


class Mobile:
    RAM = '8gb'
    EM = '256gb'

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def display(self):
        print(self.name, 'mobile then model number is', self.model)
        print('there are', Mobile.RAM, 'RAM and external memory is', Mobile.EM)
        self.RAM = '6gb'    # instance variable
        Mobile.RAM = '16gb' # class level variable


m = Mobile('Redmi', 'M2003J6')
m.display()
print(m.__dict__)
print('there are new RAM is', m.RAM)
m.display()
print(m.__dict__)
m.version = 12.4
print(m.__dict__)
del m.RAM
print(m.__dict__)
print(dir(m))
============================================================
"""

