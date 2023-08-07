class Account: 

    def __init__(self, account_number, holder, balance, limit):
        print("Building object ... {}".format(self))
        self.account_number = account_number
        self.holder = holder
        self.balance = balance
        self.limit = limit