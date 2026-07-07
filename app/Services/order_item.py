from sqlalchemy.orm import Session

from app.Models import OrderItem


def get_order_items(db: Session):
    return db.query(OrderItem).all()