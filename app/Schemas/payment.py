from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class payment(BaseModel):
    payment_id: int
    transaction_id: str
    order_id: int
    amount: Decimal
    payment_method: str
    payment_date: datetime
    payment_status: str

    model_config = ConfigDict(from_attributes=True)