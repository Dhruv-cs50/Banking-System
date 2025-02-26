class InsufficientFundsError(Exception):
    def __init__(self, balance, amount, fee):
        super().__init__(f"Insufficient funds: Balance is {balance}, but tried to withdraw {amount} with a fee of {fee}.")
        self.balance = balance

class NegativeAmountError(Exception):
    def __init__(self, amount):
        super().__init__(f"Invalid transaction: Amount {amount} cannot be negative.")
        self.amount = amount