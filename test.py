def create_account(account_number, holder, balance, limit):
    account = {"account_number": account_number, "holder": holder, "balance": balance, "limit": limit}
    return account

def deposit(account, amount):
    account["balance"] += amount

def withdraw(account, amount):
    account["balance"] -= amount

def extract(account):
    print("Balance {}".format(account["balance"]))