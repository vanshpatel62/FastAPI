from pydantic import BaseModel, ConfigDict


class produsts_data(BaseModel):
    p_id: int
    p_name: str
    category: str
    price: int
    stock: int
    brand: str

    model_config = ConfigDict(from_attributes=True)