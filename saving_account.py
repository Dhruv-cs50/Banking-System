from bank_account import BankAccount

class SavingAccount(BankAccount):
    def withdraw(self, amount):
        super().withdraw(amount, 1)  # $1 withdrawal fee