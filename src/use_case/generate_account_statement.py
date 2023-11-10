from src.domain.account.account import Account
from src.domain.customer.customer import Customer
from src.application.account.account_repository import AbstractAccountRepository
from src.application.account.transaction_repository import AbstractTransactionRepository

class GenerateAccountStatementUseCase:
    def __init__(self, transaction_repository: AbstractTransactionRepository, account_repository: AbstractAccountRepository):
        self.transaction_repository = transaction_repository
        self.account_repository = account_repository
    
    def generate_account_statement(self, account_id):
        # Fetch account transactions from repository and generate statement string
        try:
            account = self.account_repository.find_account_by_id(account_id)
            if account is None:
                raise ValueError("Not a valid account_id")
            transactions = self.transaction_repository.fetch_transactions_by_account_id(account_id)
            statement = "Account Statement:\nID\tDate\t\t\tType\tAmount\n"
            for transaction in transactions:
                statement += f"{transaction.account_id}\t{transaction.created_at}\t{transaction.transaction_type} - {transaction.amount}\n"
            return statement
        except Exception as e:
            print(f'{e}')