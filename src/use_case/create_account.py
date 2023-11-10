import random
from src.domain.account.account import Account
from src.domain.customer.customer import Customer
from src.application.account.account_repository import AbstractAccountRepository
from src.application.customer.customer_repository import AbstractCustomerRepository


class CreateAccountUseCase:
    def __init__(self, account_repository: AbstractAccountRepository, customer_repository: AbstractCustomerRepository):
        self.account_repository = account_repository
        self.customer_repository = customer_repository

    def create_account(self, customer_id: int, name: str, email: str, phone_number: str) -> Account:
        """ Creates a new account for customer
            Assuming a customer can have multiple accounts.
        """
        try:            
            customer = self.customer_repository.find_customer_by_id(customer_id)
            if customer is None:
                customer_data = Customer(customer_id, name, email, phone_number)
                self.customer_repository.save_customer(customer_data)
            account_number = self.generate_account_number()
            account_id = self.account_repository.increment_and_get_id()
            account = Account(account_id=account_id, customer_id=customer_id, account_number=account_number, balance=0.0)

            return self.account_repository.save_account(account)
        except Exception as e:
            print(f"Error in create_account: {e}")
            raise

    def get_account(self, account_id: int) -> Account:
        """Returns customer Account if present or else AccountNotFoundException is thrown
        :param account_id: customer account_id
        :return: Account
        """
        account = self.account_repository.find_account_by_id(account_id)
        if account is None:
            raise AccountNotFoundException()
        return account

    def get_accounts_by_customer_id(self, customer_id: int) -> [Account]:
        return self.account_repository.find_accounts_by_customer_id(customer_id)

    @staticmethod
    def generate_account_number():
        # Bank-specific prefix (adjust as needed)
        prefix = "ABC"
        # Generate a random sequence (you can customize the length)
        random_digits = ''.join(str(random.randint(0, 9)) for _ in range(10))
        # Combine prefix and random sequence
        account_number = f"{prefix}{random_digits}"
        # You might want to add a checksum or other validation logic here
        return account_number
    