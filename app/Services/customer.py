from fastapi import HTTPException
from sqlalchemy.orm import Session

from app import Schemas
from app.Models import Customer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_customre(db: Session, data: Schemas.add_customre):
    customer_ins = Customer(**data.model_dump())
    db.add(customer_ins)
    db.commit()
    db.refresh(customer_ins)
    return customer_ins


def get_customre(db: Session):
    return db.query(Customer).all()


def search_customer(cust_id: int, db: Session):
    cust_details = db.query(Customer).filter_by(cust_id=cust_id).first()

    
    logger.info(" ...   ...   customre search  API calling.....")
    if cust_details:
        return cust_details
    else:
        raise HTTPException(status_code=404, detail="Customer Not Found")


def update_cust(cust_id: int, cust: Schemas.customer_data, db: Session):
    find_cust = db.query(Customer).filter_by(cust_id=cust_id).first()

    if find_cust:
        for key, value in cust.model_dump().items():
            setattr(find_cust, key, value)

        db.commit()
        db.refresh(find_cust)

    return find_cust


def delet_cust(cust_id: int, db: Session):
    delete_cust = db.query(Customer).filter_by(cust_id=cust_id).first()

    if delete_cust is None:
        raise HTTPException(status_code=404, detail="Customer Can Not Found")

    db.delete(delete_cust)
    db.commit()

    return delete_cust