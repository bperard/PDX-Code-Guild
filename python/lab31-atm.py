'''
lab 31 - automatic teller machine machine
'''
transactions = []    # list of deposit/withdraw transactions

class ATM:    # atm class with rate and balance attribute defaults set
    def __init__(self, balance = 0, rate = 0.1):
        self.bal = balance
        self.rat = rate

    def __str__(self):    # format when returned as a string
        return 'BAL=' + str(self.bal) + '\nRAT=' + str(self.rat)

    def check_balance(self):    # return balance attribute
        return self.bal

    def deposit(self, amount):    # add deposit parameter to ATM balance attribute, add transaction to list
        self.bal += amount
        transactions.append('User deposited $' + str(amount))

    def check_withdrawal(self, amount):    # return True if balance greater than amount parameter
        return self.bal - amount >= 0

    def withdraw(self, amount):    # subtract parameter amount from balance attribute, add transaction, and return amount
        self.bal -= amount
        transactions.append('User withdrew $' + str(amount) + '\n')
        return amount

    def calc_interest(self):    # return interest rate
        return self.rat

    def print_transactions(self):    # print transaction history in separate lines
        for lines in transactions:
            print(lines)

print('Welcome, I am an ATM, feed me money!\n'    # intro and user input stored in teller variable
      'Just kidding, that was my humor function, hopefully I haven\'t offended you.\n'
      'Now that you are done laughing, what would you like to do?\n'
      'Enter "done" at any time to exit your account.')
teller = input('Choose "deposit", "withdraw", check "balance", and "history":')
account = ATM()    # account variable initialized as ATM type

while teller != 'done':    # while loop until teller == 'done'

    if teller.lower() == 'deposit':    # user input amount, call deposit function
        amount = int(input('Enter how much you would like to deposit: $'))
        account.deposit(amount)

    elif teller.lower() == 'withdraw':    # user input amount, call check_withdraw, call withdraw if True, notify user if False
        amount = int(input('Enter how much you would like to withdraw: $'))
        if account.check_withdrawal(amount):
            account.withdraw(amount)
        else:
            print('Can\'t withdraw $' + str(amount) + ', balance is $' + str(account.bal) + '.')

    elif teller.lower() == 'balance':    # show user balance
        print('Your balance is $' + str(account.bal) + '.')

    elif teller.lower() == 'history':    # call print_transactions
        account.print_transactions()

    if teller != 'done':    # ask user for new mode
        teller = input('Choose "deposit", "withdraw", check "balance", and "history":')

print('Work to live, don\'t live to work... okay, goodbye.')    # pass knowledge and love to user