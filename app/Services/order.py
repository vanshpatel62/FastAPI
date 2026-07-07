from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.Models import Order


def get_order(db: Session):
    result = db.execute(text("select * from orders order by order_id"))
    return result.fetchall()


def search_order_by_order_id(ord_id: int, db: Session):
    order_details = db.query(Order).filter_by(order_id=ord_id).all()

    if order_details:
        return order_details

    raise HTTPException(status_code=404, detail="Order Not Found")


def search_order_by_cust_id(cust_id: int, db: Session):
    order_details = db.query(Order).filter_by(cust_id=cust_id).all()

    if order_details:
        return order_details

    raise HTTPException(status_code=404, detail="Order Not Found")