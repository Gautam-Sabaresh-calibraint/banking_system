from src.infrastructure.account.account_repository import AccountRepository
from src.infrastructure.customer.customer_repository import CustomerRepository
from src.infrastructure.account.transaction_repository import TransactionRepository
from src.use_case.create_account import CreateAccountUseCase
from src.use_case.transaction_usecase import TransactionUseCase
from src.use_case.generate_account_statement import GenerateAccountStatementUseCase

def test_banking_scenario():
    __account_repo = AccountRepository()
    __customer_repo = CustomerRepository()
    __txn_repo = TransactionRepository()

    # Use cases
    account_use_case = CreateAccountUseCase(__account_repo, __customer_repo)
    transaction_use_case = TransactionUseCase(__txn_repo, __account_repo)
    account_statement_use_case = GenerateAccountStatementUseCase(__txn_repo, __account_repo)
    print('Creating New Accounts')
    account_use_case.create_account(1, 'Andrew', 'abc@gmail.com', '12345678')
    account_use_case.create_account(1, 'Halaand', 'sss@gmail.com', '12345678')
    account_use_case.create_account(2, 'Jacob', 'abcsad@gmail.com', '12345678')
    print('Listing the created Accounts')
    print(account_use_case.get_account(1))
    print(account_use_case.get_account(2))
    print('After a few transactions of deposit and withdrawal')
    transaction_use_case.make_transaction(1, 20000, 'deposit')
    transaction_use_case.make_transaction(2, 25000, 'deposit')
    transaction_use_case.make_transaction(2, 25000, 'deposit')
    transaction_use_case.make_transaction(2, 2130, 'withdraw')
    print(account_use_case.get_account(1))
    print(account_use_case.get_account(2))
    print('Exception - when withdrawal amount greater than account balance')
    transaction_use_case.make_transaction(2, 50030, 'withdraw')
    print('Fetching accounts of a customer_id')
    print(account_use_case.get_accounts_by_customer_id(1))
    print('Account statement of ID - 1')
    print(account_statement_use_case.generate_account_statement(1))
    print('Account statement of ID - 5')
    print(account_statement_use_case.generate_account_statement(5))
    print('Account statement of ID - 2')
    print(account_statement_use_case.generate_account_statement(2))

if __name__ == "__main__":
    test_banking_scenario()
