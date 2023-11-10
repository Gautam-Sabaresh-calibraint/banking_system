from dataclasses import dataclass

@dataclass
class Account:
    account_id: int
    customer_id: int
    account_number: str
    balance: float = 0.0
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal")
        self.balance -= amount

    def get_balance(self):
        return self.balance
