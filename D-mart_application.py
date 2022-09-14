# D-Mart application using OOP:
import time


class DMart:
    msg = 'Welcome to D-mart'

    def __init__(self, gst, total=0.0):
        self.GST = gst
        self.total = total

    def cloths(self, total):
        self.total += total
        time.sleep(2)
        print('cloths bill are: ', self.total)

    def grocery(self, total):
        self.total += total
        time.sleep(2)
        print('groceries product bill are: ', self.total)

    def footwear(self, total):
        self.total += total
        time.sleep(2)
        print('footwear bill are: ', self.total)

    def packaged_foods(self, total):
        self.total += total
        time.sleep(2)
        print('packaged_food product bill are: ', self.total)

    def self_care(self, total):
        self.total += total
        time.sleep(2)
        print('self_care product bill are: ', self.total)

    def billing(self, total, discount=0.10):
        self.discount = discount
        self.total += total + self.GST - self.discount
        print('all product bill are: ', self.total)
        if self.total > 1000:
            print('discount of 10 %')
        else:
            print('no discount')


d = DMart(0.18)
while True:
    print('------------------------------------------------')
    print('----------------Hello', DMart.msg, '------------------')
    print('------------------------------------------------')
    time.sleep(2)
    print('Which option would you like to shopping')
    time.sleep(2)
    print('------------------------------------------------')
    print('1.Cloths\n2.Glocery\n3.footwear\n4.packaged_foods\n5.self_care\n6.Bill\n7.Exit')
    print('------------------------------------------------')
    time.sleep(2)
    choice = input('Enter your choice: ')
    if choice == '1':
        print('you have selected Cloths option')
        print('------------------------------------------------')
        time.sleep(2)
        pro_name = input('Please enter the product_name is: ')
        prizes = int(input('enter the prize is: '))
        quan = int(input('enter the quantity is: '))
        amount = prizes * quan
        time.sleep(2)
        d.cloths(amount)
    elif choice == '2':
        print('you have selected glocery option')
        time.sleep(2)
        print('------------------------------------------------')
        pro_name = input('Please enter the product_name is: ')
        prizes = int(input('enter the prize is: '))
        quan = int(input('enter the quantity in kg.: '))
        amount = prizes * quan
        time.sleep(2)
        d.grocery(amount)
    elif choice == '3':
        print('you have selected footwear option')
        time.sleep(2)
        print('------------------------------------------------')
        pro_name = input('Please enter the product_name is: ')
        prizes = int(input('enter the prize is: '))
        quan = int(input('enter the quantity is: '))
        amount = prizes * quan
        time.sleep(2)
        d.footwear(amount)
    elif choice == '4':
        print('you have selected packaged_food option')
        time.sleep(2)
        print('------------------------------------------------')
        pro_name = input('Please enter the product_name is: ')
        prizes = int(input('enter the prize is: '))
        quan = int(input('enter the quantity is: '))
        amount = prizes * quan
        time.sleep(2)
        d.packaged_foods(amount)
    elif choice == '5':
        print('you have selected self_care option')
        time.sleep(2)
        print('------------------------------------------------')
        pro_name = input('Please enter the product_name is: ')
        prizes = int(input('enter the prize is: '))
        quan = int(input('enter the quantity is: '))
        amount = prizes * quan
        time.sleep(2)
        d.self_care(amount)
    elif choice == '6':
        print('you have selected billing option')
        time.sleep(2)
        print('------------------------------------------------')
        d.billing(d.total)
        print('all product bill are: ', d.total)
    else:
        print('Thank you for your time')
        print('Visit again...!!!!!')
        exit()
