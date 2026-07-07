from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class order_item(BaseModel):
    order_id: int
    items_id: int
    quantity: int
    unit_price: Decimal

    model_config = ConfigDict(from_attributes=True)