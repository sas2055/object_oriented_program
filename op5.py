"""
3. Multiple inheritance:
    -  When a child class inherits from multiple parent classes,
    it is called multiple inheritances
    - We have more than one parent and from these parent we can create a child class
    - In case of multiple inheritance we must need to follow
    hierarchy means class are to be prioritised
    - This priority we can manage by supplying parent class
    sequence in child class from left to right
---------------------------------------------------------------------------


class Mother:
    def m1(self):
        print('Access mother')

    def common(self):
        print('M - common')


class Father:
    def m2(self):
        print('Access Father')

    def common(self):
        print('F - common')


class Child(Mother, Father):
    def m3(self):
        super().common()
        Father.common(self)


c = Child()
c.m1()
c.m2()
c.common()
c.m3()
------------------------------------------------------------------------------


class Mother:
    def m1(self):
        print('Access mother')

    def common(self):
        print('M - common')


class Father:
    def m2(self):
        print('Access Father')

    def common(self):
        print('F - common')


class Child(Mother, Father):
    def m3(self):
        super().common()
        Father.common(self)


c = Child()
# i want to execute common method from both classes
Father.common(c)
Mother.common(c)
==========================================================================

# without inheritance also we can access member from other class


class Mother:
    def m1(self):
        print('Access mother')

    def common(self):
        print('M - common')


class Father:
    def m2(self):
        print('Access Father')

    def common(self):
        print('F-common')

class Child():
    pass


c = Child()
Father.common(c)
Mother.common(c)
========================================================================
# we have multiple calling options


class Bank:
    def debit(self):
        print('Debit operation')

Bank().debit()
--------------------------------------------------------------------------


class Bank:
    def debit(self):
        print('Debit operation')


b = Bank()
b.debit()
------------------------------------------------------------


class Bank:
    def debit(self):
        print('Debit operation')


sbi = Bank()
Bank.debit(sbi)
===========================================================================
"""