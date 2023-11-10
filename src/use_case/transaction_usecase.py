import uuid
import datetime
from src.domain.account.transaction import Transaction
from src.domain.customer.customer import Customer
from src.application.account.transaction_repository import AbstractTransactionRepository
from src.application.account.account_repository import AbstractAccountRepository


class TransactionUseCase:
    def __init__(self, transaction_repository: AbstractTransactionRepository, account_repository: AbstractAccountRepository):
        self.transaction_repository = transaction_repository
        self.account_repository = account_repository

    def make_transaction(self, account_id: int, amount: float, transaction_type: str):
        try:
            account = self.account_repository.find_account_by_id(account_id)
            if account is None:
                raise ValueError("Invalid account_id")
            if transaction_type == "deposit":
                account.deposit(amount)
            elif transaction_type == "withdraw":
                account.withdraw(amount)
            else:
                raise ValueError("Invalid transaction type")
            self.account_repository.save_account(account)
            # generating receipt for the transaction
            tx_id = uuid.uuid4()
            txn_receipt = Transaction(tx_id, account_id, amount, transaction_type, datetime.datetime.now().isoformat(sep=" ", timespec="seconds"))
            return self.transaction_repository.save_transaction(txn_receipt)
        except Exception as e:
          print(f'An exception occurred - {e}')