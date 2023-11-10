from dataclasses import dataclass
import datetime

@dataclass
class Transaction:
    transaction_id: str
    account_id: int
    amount: float
    transaction_type: str
    created_at: datetime.datetime.now().isoformat(sep=" ", timespec="seconds")