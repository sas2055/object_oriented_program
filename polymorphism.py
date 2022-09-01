"""
# 4. polymorphism:
    ( poly - many,  morph - forms )
    - it is defines methods in the child class that have
    the same name as the methods in the parent class.
    - it is a very important concept in programming.
    - it is the condition of occurrence in different forms.
    - It refers to the use of a single type entity (method, operator or object)
    to represent different types in different scenarios.
---------------------------------------------------------------------------

# Using Polymorphism


class Parrot:

    def fly(self):
        print('Parrot can fly')

    def swim(self):
        print('Parrot can not swim')


class Penguin:

    def fly(self):
        print('Penguin can not fly')

    def swim(self):
        print('Penguin can swim')


# common interface
def flying_test(bird):
    bird.fly()


def swimming_test(bird):
    bird.swim()


p = Parrot()
q = Penguin()
flying_test(p)
flying_test(q)
swimming_test(p)
swimming_test(q)
p.voice = 'vithu-vithu'
print(p.__dict__)
print('parrot voice is', p.voice)
===============================================================

import statistics as s


class Sample:
    def __init__(self, *args):
        if len(args) == 3:
            print('Average is: ', s.mean(args))
        elif len(args) == 2:
            print('sum is: ', sum(args))
        elif len(args) == 1:
            print(args[0])


Sample(12, 40, 23)
Sample(23, 56)
Sample(4)
=============================================================


class Info:
    def __init__(self, *kwargs):
        if len(kwargs) == 2:
            print('my name and age is', kwargs)
        elif len(kwargs) == 1:
            print('place is', kwargs)


Info('shivansh', 23)
Info('pune')
===========================================================
"""
