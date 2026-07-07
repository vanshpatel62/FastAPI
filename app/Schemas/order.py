from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class orders_data(BaseModel):
    order_id: int
    cust_id: int
    order_date: datetime
    status: str
    total_amount: Decimal

    model_config = ConfigDict(from_attributes=True)