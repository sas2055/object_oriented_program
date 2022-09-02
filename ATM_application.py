# ATM application using OOP:
import random


class ATM:
    bank_name = 'BANK OF INDIA'

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def account_detail(self):
        print('----------------ACCOUNT DETAIL-------------------')
        print('Account Holder: ', self.name)
        print('Account Number:', self.account_number)
        print('Available balance Rs. ', self.balance)

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print('Current account balance Rs. ', self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print('Insufficient fund!')
            print('Your balance is Rs. ', self.balance, 'only.')
            print('Try with lesser amount than balance.')
            print()
        else:
            self.balance = self.balance - self.amount
            print('Rs.', self.amount, 'withdrawal successful!')
            print('Current account balance Rs.', self.balance)
            print()

    def check_balance(self):
        print('Available balance Rs. ', self.balance)
        print()

    def transaction(self):
        print("""-----TRANSACTION------
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************""")
        while True:
            print('------------------------------------------------')
            choice = input('Enter your choice: ')
            if choice == '1':
                atm.account_detail()
            elif choice == '2':
                atm.check_balance()
            elif choice == '3':
                amount = int(input('How much you want to deposit Rs.'))
                atm.deposit(amount)
            elif choice == '4':
                amount = int(input('How much you want to withdraw Rs. '))
                atm.withdraw(amount)
            elif choice == '5':
                print(f"""-----------printing receipt---------------
                ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** 
                Transaction is now complete.
                Transaction number: {random.randint(10000, 1000000)}
                Account holder: {name}
                Account number: {account_number}
                Available balance Rs. {self.balance}

                Thanks for choosing us as your bank
                ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **""")
                exit()


print('----------------ACCOUNT CREATION--------------------')
name = input('Enter your name: ')
account_number = input('Enter your account number: ')
print('Congratulations! Account created successfully')
atm = ATM(name, account_number)
while True:
    print('------------------------------------------------')
    print('Hello', name, 'Welcome to', ATM.bank_name)
    print('------------------------------------------------')
    print('Which operation would you like to perform')
    print('1.Account Detail\n2.Check Balance\n3.Deposit\n4.Withdraw\n5.Exit')
    print('------------------------------------------------')
    trans = input('Do you want to do any transaction?(y/n): ')
    if trans == 'y':
        atm.transaction()
    elif trans == 'n':
        print("""------------------------------
        | Thanks for choosing us as your bank |
        | Visit us again!                     |
        --------------------------------------""")
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for no.\n")
