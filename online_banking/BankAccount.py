

class BankAccount:

    def __init__(self, account_number : int, balance : float ):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount : int):
        self.balance += amount

    def withdraw(self, amount : int):
        self.balance -= amount

user1 = BankAccount(1, 500)
user1.deposit(100)
user1.withdraw(88)
print(user1.balance)