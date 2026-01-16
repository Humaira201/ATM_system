# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import json
def load_accounts():  # this function reads the file and converts json->python dictionary
    try:
        with open('accounts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def save_accounts(accounts):  # this function writes python dictionary->json file
    with open('accounts.json', 'w') as file:
        json.dump(accounts, file, indent=4)
accounts = load_accounts()
def create_account():
    acc_no = int(input('enter new account number'))
    if acc_no in accounts:
        print('account already exists')
        return
    name = input('enter your account name')
    pin = input('set 4-digit pin')
    type=input('enter your account type')
    accounts[acc_no] = {
        'name': name,
        'type':type,
        'pin': pin,
        'balance': 0,
        'transactions': []}
    save_accounts(accounts)
    print('account created successfully')
def login():
    acc_no=int(input('enter your account number'))
    pin=input('pin: ')
    if acc_no in accounts and pin==accounts[acc_no]['pin']:
        return acc_no
    else:
        print('invalid credentials')
        return None

class ATM:
    def __init__(self,acc_no):
        self.__acc_no=acc_no
        self.__menu()
    def __menu(self):
        user_input=int(input("""Enter your choice:
        1.enter 1 to deposit
        2.enter 2 to withdraw
        3.enter 3 to check balance
        4.enter 4 to transfer money
        5.enter 5 to exit: """))
        if user_input==1:
             self.deposit()
        elif user_input==2:
            self.withdraw()
        elif user_input==3:
            self.check_balance()
        elif user_input==4:
            self.transfer()
        elif user_input==5:
            print('bye')
    def transaction_history(self,action,amount):
        print('action:',action,
              '\namount:',amount,
              '\nBalance After:',accounts[self.__acc_no]['balance'])
    def deposit(self):
        amount=int (input('enter your amount'))
        accounts[self.__acc_no]['balance']+=amount
        save_accounts(accounts)
        print('deposited successfully\n')
        self.transaction_history("deposit",amount)
        self.__menu()
    def withdraw(self):
        amount = int(input('enter your amount'))
        if amount <= accounts[self.__acc_no]['balance']:
            accounts[self.__acc_no]['balance']-=amount
            save_accounts(accounts)
            print('withdrawn successfully\n')
            self.transaction_history("withdraw",amount)
        else:
            print('insufficient funds\n')
        self.__menu()
    def check_balance(self):
        print('your balance is: ',accounts[self.__acc_no]['balance'])
        self.__menu()
    def transfer(self):
        sender=self.__acc_no
        receiver=int(input('enter receivers account number'))
        amount=int(input('enter your amount'))
        if sender in accounts and receiver in accounts:
            if amount <= accounts[sender]['balance']:
                accounts[sender]['balance']-=amount
                accounts[receiver]['balance']+=amount
                save_accounts(accounts)
                print('transferred successfully\n')
                self.transaction_history("transfer",amount)
                print('To:',accounts[receiver]['name'])
            else:
                print('insufficient funds\n')
        else:
            print('account does not exist\n')
        self.__menu()
while True:
    print('1.create account')
    print('2.login')
    print('3.exit')
    choice=int(input('enter your choice: '))
    if choice==1:
        create_account()
    elif choice==2:
        user=login()
        if user:
            atm=ATM(user)
    elif choice==3:
        exit()



