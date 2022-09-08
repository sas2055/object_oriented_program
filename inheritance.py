"""
# 1. Inheritance:
    - it is defined as inheriting the properties of the base class to the child class.
--------------------------------------------------------------------------

# Advantages of Inheritance:
    - it improves code re-usability
    - it improves code readability
    - reduces the programmer efforts
---------------------------------------------------------------------------

# Types of Inheritance in Python:
1. Single Inheritance:
    - it is the inheritance of the “Derived” class from the “Base” class.
----------------------------------------------------------------------------


class Country:
    msg = 'welcome to country'

    def ShowCountry(self):
        print('this is INDIA')


class State(Country):
    def ShowState(self):
        print('this is Maharashtra')


st = State()
print(st.msg)
st.ShowCountry()
st.ShowState()
==============================================================================

2. Multi-level inheritance:
     - it gets documented each time a derived class inherits another derived class.
     - there is no limit to the number of derived classes
--------------------------------------------------------------------------


class Animal:
    def speak(self):
        print('Animal speaking')


class Dog(Animal):
    def bark(self):
        print('dog barks')


class DogChild(Dog):
    def eat(self):
        print('eating a bread')


d = DogChild()
d.speak()
d.bark()
d.eat()
===============================================================================


class A:
    def m1(self):
        print('m1 A')


class B(A):
    def m1(self):
        print('m1 B')


class C(B):
    def m2(self):
        super().m1()
        A.m1(self)


c = C()
c.m2()
============================================================================

3. Multiple Inheritance:
    - its inherit multiple functionalities and properties
    from different base classes into a single derived class.
--------------------------------------------------------------------------------


class Cal1:
    def addition(self, a, b):
        return a+b


class Cal2:
    def Multiply(self, a, b):
        return a*b


class Div(Cal1, Cal2):
    def Divided(self, a, b):
        return a/b


d = Div()
print(d.addition(10, 20))
print(d.Multiply(10, 20))
print(d.Divided(10, 20))
==============================================================================


class A:
    def m1(self):
        print('m1 is A')


class B:
    def m1(self):
        print('m1 is B')


class C:
    def m2(self):
        print('m2 is C')


class Child(B, A, C):
    pass


ob = Child()
ob.m1()
ob.m2()
---------------------------------------------------------------------------


class A:
    def m1(self):
        print('m1 is A')


class B:
    def m1(self):
        print('m1 is B')

    def m2(self):
        print('m2 is B')


class C:
    def m2(self):
        print('m2 is C')


class Child(B, A, C):
    pass


ob = Child()
ob.m1()
ob.m2()
==================================================================================

4. Hybrid inheritance:
    - Inheritance consisting of multiple types of inheritance is called hybrid inheritance.
    - A derived class can access properties of the base class.
------------------------------------------------------------------------------


class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


ob = Student3()
ob.func1()
ob.func2()
print(ob.__doc__)
ob.func4()
=================================================================================

5. Hierarchical Inheritance:
    - When more than one derived class are created from a single
    base this type of inheritance is called hierarchical inheritance.
    - we have one parent (base) class and two child (derived) classes.
---------------------------------------------------------------------------------



class Parent:
    def func1(self):
        print("This function is in parent class.")


class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")


class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")


ob1 = Child1()
ob2 = Child2()
ob1.func1()
ob1.func2()
ob2.func1()
ob2.func3()
=============================================================================
"""
