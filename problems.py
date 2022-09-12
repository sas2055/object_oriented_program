"""
# Que.1 Get index in the list of objects by attribute


class X:
    def __init__(self, val):
        self.val = val


def index(ls, num=3):
    for ind, x in enumerate(ls):
        if x.val == num:
            return ind
    return -1


ls = [1, 2, 3, 4, 5, 6]
a = list()
for i in ls:
    a.append(X(i))
print(index(a))
===============================================================

# Que.2 How to create an empty class


class Sample:
    pass


s = Sample()
print(s)
========================================================

# Que.3 How to count number of instances of a class


class Sample:
    count = 0

    def __init__(self):
        Sample.count += 1


s = Sample()
s1 = Sample()
s2 = Sample()
print(Sample.count)
=================================================================

# Que.4 How to Change a Dictionary Into a Class?
class Dict(object):

    def __init__(self, d):
        for key in d:
            setattr(self, key, d[key])


d = {"Name": "Ajit", "Rank": "1223", "Subject": "Python"}
print("After Converting Dictionary to Class: ")
res = Dict(d)
print(res.Name, res.Rank, res.Subject)
print(type(Dict(d)))
================================================================

# Que.5 How to create a list of object in Python class


class Info:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
ls = []
ls.append(Info('Akash', 2))
ls.append(Info('Deep', 40))
ls.append(Info('Reva', 44))
for i in ls:
    print([i.name, i.roll_no], end=', ')

or


class Addition:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        print(self.x + self.y)


lt = []
lt.append(Addition(2, 3))
lt.append(Addition(12, 13))
lt.append(Addition(22, 33))
for j in lt:
    j.sum()
==================================================================

# Que.6 What is a clean, Pythonic way to have multiple constructors


class example:

    def __init__(self):
        print("One")

    def __init__(self):
        print("Two")

    def __init__(self):
        print("Three")


e = example()

or


class sample:
    def __init__(self, *args):
        if len(args) > 1:
            self.ans = 0
            for i in args:
                self.ans += i
        elif isinstance(args[0], int):
            self.ans = args[0] * args[0]
        elif isinstance(args[0], str):
            self.ans = 'Hello! ' + args[0] + '.'


s1 = sample(1, 2, 3, 4, 5)
print('Sum of list:', s1.ans)
s2 = sample(5)
print('Square of int:', s2.ans)
s3 = sample('Pythonist')
print('String:', s3.ans)
===========================================================

# Que.7 WAP to build flashcard using class


class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + ' ( ' + self.meaning + ' )'


flash = []
print('welcome to flashcard application')
while True:
    word = input('enter the name you want to add to flashcard: ')
    meaning = input('enter the meaning of the word: ')
    flash.append(Flashcard(word, meaning))
    option = int(input('enter 0 , if you want to add another flashcard: '))
    if option:
        break
print('\nYour flashcards')
for i in flash:
    print('>', i)

or
import random


class Flashcard:
    def __init__(self):
        self.fruits = {'apple': 'red',
                       'orange': 'orange',
                       'watermelon': 'green',
                       'banana': 'yellow'}

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print('What is the color of {}'.format(fruit))
            user_answer = input()
            if user_answer.lower() == color:
                print('Correct answer')
            else:
                print('Wrong answer')
            option = int(input("enter 0 , if you want to play again : "))
            if option:
                break


print('welcome to fruit quiz')
fc = Flashcard()
fc.quiz()
===============================================================
"""



