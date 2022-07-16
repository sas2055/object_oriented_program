"""
# OOP:
    - Object Oriented Programming
    - to solve a programming problem is by creating objects.
    - it is focuses on creating reusable code.
    - it is also known as DRY (Don't Repeat Yourself).
-----------------------------------------------------------------

# Class:
    - A class is a collection of objects.
    - it is template, blueprint, structure, design for the object
    - which is composed of 2 things
- Properties ( Data Members/ variables )
- behavior ( Methods )
-------------------------------------------------------------

Example: Mobile
    - variables: RAM ROM Screensize, OS, Camera etc
    - behaviour: Power on, shutdown, silent (operations/actions)
----------------------------------------------------------------

class Icecream:
    var: ingredients
    action: boiling, mixing. etc
-------------------------------------------------------------


class Cake:
    sugar = 1
    milk = .5

    def baking(self):
        print('Its baking process')

    def icing(self):
        print('Icing process')

print(Cake().milk, Cake().sugar)
Cake().baking()
Cake().icing()
# calling of class Cake is important
# because it will give u can access to the members of a class
# can u able to call methods using class calling
# this calling make everything available outside the class
# call the methods inside a class
------------------------------------------------------------

# Rather than calling a class multiple times it will create multiple objects


class Cake:
    sugar = 1
    milk = .5

    def baking(self):
        print('Its baking process')

    def icing(self):
        print('Icing process')

#print(dir(Cake()))
print(id(Cake()))
print(id(Cake()))
a = Cake()
b = Cake()
print(id(a), id(b))
============================================================
# so we have an option for this


class Cake:
    sugar = 1
    milk = .5

    def baking(self):
        print('Its baking process')

    def icing(self):
        print('Icing process')

c1 = Cake()
print(c1.milk)
c1.baking()
print('-------------------------------')
c2 = Cake()
c2.milk = 2
c2.sugar = 2.5
c2.flavour = 'orange'
print(c2.milk, c2.sugar)
c2.icing()
# lets check directory structure of both objects
print('--------------------------')
print(dir(c1))
print(dir(c2))
print(c2.__dict__)  # used to check variables currently present in object
print('--------lets delete some variables-----')
del c2.sugar
print(c2.__dict__)
del c2.flavour
print(c2.flavour)
================================================================
"""