from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        super().withdraw(amount, 2)  # $2 withdrawal fee
