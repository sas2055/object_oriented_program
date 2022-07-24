"""
# OOP Properties:
    - there are four Pillars of Object-Oriented Program
1. Inheritance
2. Encapsulation
3. Abstraction
4. Polymorphism
-------------------------------------------------------------------

1. Inheritance:
    - it allows us to define a class that inherits all the
    methods and properties from another class.
------------------------------------------------------------------------

# Building a parent and child relationship in which we have basically 2 classes
1. Parent class:
    - it is the class being inherited from, also known as Base/root class
-------------------------------------------------------------------------

2. Child class:
    - it is the class that inherits from another class, also known as Derived class
--------------------------------------------------------------------------

Syntax:
Class ParentClass:
    {Body}
Class ChildClass(ParentClass):
    {Body}
-----------------------------------------------------------------------------

# There are 4 different types of Inheritance:
1. Simple/single inheritance
2. Multilevel inheritance
3. Multiple inheritance
4. Hybrid inheritance
5. Hierarchical inheritance
=============================================================================

1. Simple inheritance:
    - When a child class inherits from only one parent class,
    it is called single inheritance.
    - in which we will have only one parent and one child
    - to build a relation we need to inherit parent class in child class
--------------------------------------------------------------------------


class Father:
    x = 100

    def money(self):
        print('Money of Father')


class Child(Father):
    pass


c = Child()
c.money()
print(c.x)
============================================================

# suppose child class only has money method
# and Father class has x, car method


class Father:
    x = 100

    def car(self):
        print('Fathers car')


class Child(Father):
    def money(self):
        print('Money of Child')


c = Child()
c.money()
c.car()
======================================================================

2. Multi-level inheritance:
    - When we have a child and grandchild relationship.
-------------------------------------------------------------------


class Central_gov: # super_parent
    def funds(self):
        print("central gov funds")


class State_gov(Central_gov): # Parent
    def s_funds(self):
        print('State gov fund')

    def funds(self):
        print('Central fund in State')
        super().funds()


class Local_gov(State_gov): # child
    pass


l = Local_gov()
l.funds()
l.s_funds()
=============================================================

# we can use a super() to access members of a super parent or parent
# if that method or member is already present
# super we can use inside a method


class PM:
    def help(self):
        print('Help from PM')


class CM(PM):
    def help(self):
        print('Help from CM')
        super(CM, self).help()


class MLA(CM):
    def fund(self):
        print('MLA fund')


m = MLA()
m.fund()
m.help()
------------------------------------------------------------------
# using super parent class in child class


class PM:
    def help(self):
        print('Help from PM')


class CM(PM):
    def help(self):
        print('Help from CM')


class MLA(CM):
    def fund(self):
        print('MLA fund')
        PM.help(self)


m = MLA()
m.fund()
m.help()
===================================================================


class Father:
    def home(self):
        print('this is fathers home')


class Mother(Father):
    def home(self):
        print('this is mothers home')
        super(Mother, self).home()


class Child(Mother):
    def home(self):
        print('this is child home')
        super(Child, self).home()


c = Child()
c.home()
====================================================================

# Method overriding:
    - If child and parent contains a method with same name,
    so method in child overrides method in parent and method in parent overriden in child
    - Overriding is completely a part of inheritance without inheritance its not possible
-----------------------------------------------------------------------


class Father:
    def info(self):
        print('Father info')


class Child(Father):
    def info(self):
        print('Self.info')


c = Child()
c.info()
=======================================================================
"""
