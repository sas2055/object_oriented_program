"""
syntax:
    class class_name:
        properties
        behaviour
-----------------------------------------------------------

# Convention:
    - Use class name in Title case if it is a single word
class Bank:
    pass
-------------------------------------------------------------
    - if its a combination of 2 words then use CamelCase
class BankDetails:
    pass
============================================================

class calling --> Constructor calling
-------------------------------------------------------

# constructor:
    - it is used for instantiating an object.
    - it is to initialize(assign values) to the data members of the class
    when an object of the class is created.
    - In Python the __init__() method is called the constructor
------------------------------------------------------------------

# Feature:
    - Constructor has same the name as that of class Name
    - it is used to allocate a memory
    - Constructor can be empty or parameterized
----------------------------------------------------------


class Bank:
    ifsc = 'BOiKID2324'

    def deposit(self):
        pass

    def withdraw(self):
        pass


b = Bank()
b.deposit()
print(dir())
----------------------------------------------------------

# Create an empty constructor


class Sample:
    def __init__(self):     # initializes memory
        print('Constructor method')

    def display(self):
        pass


Sample()
Sample().__init__()
===================================================================

# Types of constructors:
    there are two types of constructor are as follows
--------------------------------------------------------------------------

1. default constructor:
    - it is a simple constructor which does not accept any arguments.
    - It has only one argument which is a reference to the instance being constructed.
----------------------------------------------------------------------------------

2. Parameterized constructor:
    - constructor with parameters is known as parameterized constructor.
    - it takes its first argument as a reference to the instance being constructed known as self
    and the rest of the arguments are provided by the programmer
--------------------------------------------------------------------------------

# use positional arguments:


class Sample:
    def __init__(self, name, age):
        print('Name is: ', name, 'and age is: ', age)

Sample('Shiv', 25)
Sample(24, 'Kajal')
============================================================

# Use keyword argument:


class Sample:
    def __init__(self, name, age):
        print('Name is: ', name, 'and age is: ', age)

Sample(age=24, name='Raj')
===================================================

# Use default arguments


class Sample:
    def __init__(self, name, age=18):
        print('Name is: ', name, 'and age is: ', age)

# default age values is set to 18
Sample(name = 'Ajit')
Sample('Amit', 26)
==========================================================

# Variable length argument:
1. *args:
    - it is a positional arguments
    - it returns tuple always
----------------------------------------------------------


class Sample:
    def __init__(self, *args):
        print(args)


Sample('Suraj', 22)
Sample('Yash', 26, 'Pune')
--------------------------------------------------------

2. **kwargs:
    - it is a keyword arguments
    - it returns dict always
------------------------------------------------------


class Sample:
    def __init__(self, **kwargs):
        print(kwargs)


Sample(name='Deep', age=22)
Sample(name='Sunil', age=46, place='Pune')
Sample()
========================================================

# Que. Is the __init__ only option to supply arguments?
->  NO, We can supply arguments to any normal method
----------------------------------------------------------


class Sample:
    def info(self, roll_no, name, std):
        print(roll_no, name, std, sep ='\n')

Sample().info(12, 'Ash', 10)
---------------------------------------------------------

# roll_no and name are local to info
# we need to make them instance variables
# using self we can make it
# right way:
    - object-->Constructor--> info-->display
-------------------------------------------------------------


class Sample:
    def info(self, roll_no, name):
        self.roll_no = roll_no
        #(instance)    (local)
        self.name = name

    def display(self):
        print('Details provide by user: ')
        print(self.roll_no)
        print(self.name)

s = Sample()
s.info(10, 'Ajit')
s.display()
# s--> Sample()--> info--> display()
===============================================================

# We have 3 reference variables
    - self: inside a class+method
    - object: outside a class
    - className: inside a class method
---------------------------------------------------------------

# self parameter:
    - it works like a reference variable inside a class
    - it is active only inside a method
    - it won't work outside the method and class
    - Inside a method we can access and call any of the member of a class
----------------------------------------------------------------

# Object:
    - An object (instance) is an instantiation of a class.
    - it is only the description for the object
    - no memory or storage is allocated.
----------------------------------------------------------------

# className:
    - className acts as a reference for variables declared
    inside a class and outside a method
--------------------------------------------------------------------

# Task we can perform using self
1. add new instance variable using self:


class Test:
    pin = 415115

    def register(self, name):
        print(name)  # name is local to register method
        self.name = name

    def task(self):
        print('welcome', self.name, 'to a task')
        print(Test.pin)

    def task2(self):
        print(self.name)
        # let us add new variables
        # we add using self

        self.age = 45
        self.pincode = 411008


t = Test()
t.register('Shivansh')
t.task()
t.task2()
print(t.__dict__)
print(t.age)
print(t.pincode)
===================================================================
"""
