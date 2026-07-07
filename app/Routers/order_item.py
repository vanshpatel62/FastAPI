from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import Schemas, Services
from app.database import get_db

router = APIRouter(
    prefix="/ordr_items",
    tags=["Order Items"]
)


@router.get("/order_items",response_model=list[Schemas.order_item])
def get_order_items(db:Session=Depends(get_db)):
    return Services.get_order_items(db)