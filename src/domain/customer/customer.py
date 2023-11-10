from dataclasses import dataclass

@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    phone_number: str
    
    def get_name(self, customer_id):
        return self.name