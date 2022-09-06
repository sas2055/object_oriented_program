"""
# Multiple inheritance:
  - means more than one parent
  - derived class separate base class names with commas
-----------------------------------------------------------------

syntax:


class Mother:
    pass


class Father:
    pass


class Child(Mother, Father):
    pass
-------------------------------------------------------------------------------


class A:
  def m1(self):
    print('m1 of A')


class B:
  def m1(self):
    print('m1 of B')


class C:
  def m1(self):
    print('m1 of C')


class Child(C, B, A):
  pass


ob = Child()
ob.m1()
==============================================================================

# i need to find out hierarchy of method to be searched in class then use mro
----------------------------------------------------------------------------

# MRO(Method Resolution Order):
    - mro is a concept used in inheritance.
    - it resolves a method or attribute.
    - It is the order in which a method is searched for in a classes hierarchy
    and is especially useful in Python because Python supports multiple inheritance.
    - the MRO is from bottom to top and left to right.
    - it can be viewed as the __mro__ attribute it returns a tuple
     and the mro() method it returns a python list.
    - mro attribute in a class that is involved in python multiple inheritance.
    - it is supports and followed an order by multiple inheritance.
------------------------------------------------------------------------------------


class A:
  def m1(self):
    print('m1 of A')


class B:
  def m1(self):
    print('m1 of B')


class C:
  def m1(self):
    print('m1 of C')


class Child(C, B, A):
  pass


ob = Child()
print(Child.mro())
print(Child.__mro__)
=========================================================================


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.__mro__)
print(M.mro())
===============================================================


class View:
    pass


class AuthView(View):
    pass


class FormView(View):
    pass


class AuthFormView(AuthView, FormView):
    pass


print(AuthFormView.__mro__)
print(AuthFormView.mro())
============================================================


class A:
    pass


class B(A):
    pass


class M(B, A):
    pass


print(M.__mro__)
print(M.mro())
===================================================================


class A:
    pass


class B(A):
    pass


class C(B, A):
    pass


class Start(C, A):
    pass


print(Start.__mro__)
print(Start.mro())
==========================================================


class D:
    pass


class E:
    pass


class F:
    pass


class B(D, E):
    pass


class C(D, F):
    pass


class A(B, C):
    pass


print(A.mro())
print(A.__mro__)
==========================================================================

# mro fail example


class A:
    pass


class B(A, C):  # NameError: name 'C' is not defined
    pass


class C(B, A):
    pass


class Start(B, A):
    pass


print(Start.__mro__)
print(Start.mro())
======================================================================

"""


