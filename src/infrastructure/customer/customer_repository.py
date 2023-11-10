from src.application.customer.customer_repository import AbstractCustomerRepository
from src.domain.customer.customer import Customer


class CustomerRepository(AbstractCustomerRepository):

    def __init__(self):
        # In-memory storage using a dictionary
        self.customers = {}
        
    def save_customer(self, customer):
        # Save account data to the in-memory dictionary
        self.customers[customer.customer_id] = {
            'customer_id': customer.customer_id,
            'name': customer.name,
            'email': customer.email,
            'phone_number': customer.phone_number
        }
    
    def find_customer_by_id(self, customer_id):
        # Retrieve account data from the in-memory dictionary based on account_id
        customer_data = self.customers.get(customer_id)
        if customer_data:
            return Customer(customer_id, customer_data['name'], customer_data['email'], customer_data['phone_number'])
        return None
