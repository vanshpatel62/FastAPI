from datetime import datetime, timezone
from pydantic import BaseModel, ConfigDict, Field


class customer_data(BaseModel):
    cust_id: int
    name: str
    email: str
    city: str
    join_date: datetime
    model_config = ConfigDict(from_attributes=True)


class add_customre(BaseModel):
    name: str
    email: str
    city: str
    join_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))