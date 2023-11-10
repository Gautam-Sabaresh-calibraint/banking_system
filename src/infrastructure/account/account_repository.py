from src.application.account.account_repository import AbstractAccountRepository
from src.domain.account.account import Account

class AccountRepository(AbstractAccountRepository):
    next_account_id: int
    accounts: {}
    def __init__(self):
        # In-memory storage using a dictionary
        self.accounts = {}
        self.next_account_id = 0
        
    def save_account(self, account):
        # Save account data to the in-memory dictionary
        self.accounts[account.account_id] = {
            'customer_id': account.customer_id,
            'account_number': account.account_number,
            'balance': account.balance
        }
        return account

    def find_account_by_id(self, account_id):
        # Retrieve account data from the in-memory dictionary based on account_id
        account_data = self.accounts.get(account_id)
        if account_data:
            return Account(account_id, account_data['customer_id'], account_data['account_number'], account_data['balance'])
        return None

    def find_accounts_by_customer_id(self, customer_id):
        # Retrieve all accounts of a customer from the in-memory dictionary based on customer_id
        accounts = []
        for account_id, account_data in self.accounts.items():
            if account_data['customer_id'] == customer_id:
                accounts.append(Account(account_id, account_data['customer_id'], account_data['account_number'], account_data['balance']))
        return accounts
    
    def increment_and_get_id(self) -> int:
        # autoincrement account_id
        self.next_account_id += 1
        return self.next_account_id