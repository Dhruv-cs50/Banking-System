from exceptions import NegativeAmountError, InsufficientFundsError

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError(amount)
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount, fee):
        if amount < 0:
            raise NegativeAmountError(amount)
        total_amount = amount + fee
        if self.balance >= total_amount:
            self.balance -= total_amount
            print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            raise InsufficientFundsError(self.balance, amount, fee)

    def check_balance(self):
        print(f"{self.name}'s balance: ${self.balance}")

    def __str__(self):
        return f"Account owner: {self.name}, Balance: ${self.balance}"

