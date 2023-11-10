from abc import ABC, abstractmethod
from src.domain.account.account import Account

class AbstractAccountRepository(ABC):

    @abstractmethod
    def save_account(self, account: Account):
        pass
    
    @abstractmethod
    def find_account_by_id(self, account_id):
        pass
    
    @abstractmethod
    def find_accounts_by_customer_id(self, customer_id):
        pass
    
    @abstractmethod
    def increment_and_get_id(self):
        pass