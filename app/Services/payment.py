from sqlalchemy.orm import Session

from app.Models import Payment


def get_payments_details(db: Session):
    return db.query(Payment).all()