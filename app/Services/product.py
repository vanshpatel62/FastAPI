from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.Models import Product


def get_product(db: Session):
    result = db.execute(text("select * from products order by p_id"))
    return result.fetchall()


def search_product(p_id: int, db: Session):
    product_details = db.query(Product).filter_by(p_id=p_id).all()

    if product_details:
        return product_details

    raise HTTPException(status_code=404, detail="Product Not Found")