class Account:

    def __init__(self, number, holder, balance, limit):
        print("Building object ... {}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def statement(self):
        print("Balance of {} for account holder {}".format(self.__balance, self.__holder))

    def deposit(self, value):
        self.__balance += value

    def __can_withdraw(self, value_to_withdraw):
        available_withdrawal_value = self.__balance + self.__limit
        return value_to_withdraw <= available_withdrawal_value

    def withdraw(self, value):
        if(self.__can_withdraw(value)):
            self.__balance -= value
        else:
            print("The value {} exceeded the limit".format(value))

    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def get_holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def bank_codes():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
