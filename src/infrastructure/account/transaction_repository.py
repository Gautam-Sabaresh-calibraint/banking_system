from dataclasses import dataclass
from src.application.account.transaction_repository import AbstractTransactionRepository

@dataclass
class TransactionRepository(AbstractTransactionRepository):
    transactions = []

    def save_transaction(self, transaction):
        # Save transaction data to the in-memory list
        self.transactions.append(transaction)

    def fetch_transactions_by_account_id(self, account_id):
        # Retrieve transactions for a given account_id from the in-memory list
        return [transaction for transaction in self.transactions if transaction.account_id == account_id]