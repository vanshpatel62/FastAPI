# from pydantic import 
from fastapi import FastAPI,HTTPException,Depends,Request
from app import models
from app.models import Customer,Product,Order,Payment
from sqlalchemy.orm import Session
from app import schemas
from app.schemas import customer_data
from sqlalchemy import text

# def create_customre(db:Session,gd:customer_data):
#     data = gd.model_dump()
#     customer_ins=Customres(data)

# 
def create_customre(db: Session, data: schemas.add_customre):
    customer_ins = Customer(**data.model_dump())
    db.add(customer_ins)
    db.commit()
    db.refresh(customer_ins)
    return  customer_ins

def get_customre(db:Session):
    return db.query(Customer).all()

# search cutomer
def search_customer(cust_id:int,db:Session):
    cust_details=db.query(Customer).filter_by(cust_id=cust_id).first()

    if(cust_details):
        return cust_details
    else:
        raise HTTPException(status_code=404,detail="Customer Not Found")


def get_product(db:Session):
    result=db.execute(text("select * from products order by p_id"))
    return result.fetchall()
    # return db.query(Product).all()

def get_order(db:Session):
    # return db.query(Order).all()
    # or
    result=db.execute(text("select * from orders order by order_id"))
    return result.fetchall()

def get_order_items(db:Session):
    return db.query(models.OrderItem).all()

def get_payments_details(db:Session):
    return db.query(Payment).all()