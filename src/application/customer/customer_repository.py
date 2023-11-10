from abc import ABC, abstractmethod
from src.domain.customer.customer import Customer

class AbstractCustomerRepository(ABC):

    @abstractmethod
    def save_customer(self, customer: Customer):
        pass
    
    @abstractmethod
    def find_customer_by_id(self, customer_id):
        pass