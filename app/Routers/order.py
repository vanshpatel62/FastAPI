from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import Schemas, Services
from app.database import get_db

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("/orders",response_model=list[Schemas.orders_data])
def get_orders(db:Session=Depends(get_db)):
    return Services.get_order(db)

@router.get("/orders/{ord_id}",response_model=list[Schemas.orders_data])
def search_orders_by_ord_id(ord_id: int,db: Session = Depends(get_db)):
    return Services.search_order_by_order_id(ord_id,db)

@router.get("/orders_by_cust_id/{cust_id}",response_model=list[Schemas.orders_data])
def search_orders_by_cust_id(cust_id: int,db: Session = Depends(get_db)):
    return Services.search_order_by_cust_id(cust_id,db)