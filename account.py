class Account: 

    def __init__(self, number, holder, balance, limit):
        print("Building object ... {}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def extract(self):
        print("Balance of {} of holder {}".format(self.__balance, self.__holder))

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def transfer(self, amount):
        self.withdraw(amount)
        self.deposit(amount)
