from abc import ABC, abstractmethod
from src.domain.account.transaction import Transaction

class AbstractTransactionRepository(ABC):

    @abstractmethod
    def save_transaction(self, account: Transaction):
        pass
    
    @abstractmethod
    def fetch_transactions_by_account_id(self, account_id):
        pass