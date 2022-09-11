"""
# Student management system in Python
# Que. WAP to build a simple Student Management System using Python
which can perform the following operations:
    1. Accept
    2. Display
    3. Search
    4. Delete
    5. Update

solution -


class Student:
    def __init__(self, name, roll_no, m1, m2):
        self.name = name
        self.roll_no = roll_no
        self.m1 = m1
        self.m2 = m2

    def accept(self, Name, Roll_no, marks1, marks2):
        ob = Student(Name, Roll_no, marks1, marks2)
        ls.append(ob)

    def display(self, ob):
        print('Name: ', ob.name)
        print('Roll_No: ', ob.roll_no)
        print('Marks1: ', ob.m1)
        print('Marks2: ', ob.m2)

    def search(self, rn):
        for i in range(ls.__len__()):
            if ls[i].roll_no == rn:
                return i

    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]

    def update(self, rn, no):
        i = obj.search(rn)
        roll = no
        ls[i].roll_no = roll


ls = []
obj = Student('', 0, 0, 0)
print('Operations used: ')
print('\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n'
      '4.Delete Details of Student\n5.Update Student Details\n6.Exit')
# ch = int(input("Enter choice: "))
# if ch == 1:
obj.accept('A', 1, 100, 100)
obj.accept('B', 2, 90, 90)
obj.accept('C', 3, 80, 80)
# elif ch == 2:
print('\nList of Students')
for i in range(ls.__len__()):
    obj.display(ls[i])
# elif ch == 3:
print('\n Student Found: ')
s = obj.search(2)
obj.display(ls[s])
# elif ch == 4:
obj.delete(2)
print(ls.__len__())
print('List after deletion')
for i in range(ls.__len__()):
    obj.display(ls[i])
# elif ch == 5:
obj.update(3, 2)
print(ls.__len__())
print('List after updation')
for i in range(ls.__len__()):
    obj.display(ls[i])
# else:
print('Thank You !')
==================================================================================
"""
