from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import Schemas, Services
from app.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/products",response_model=list[Schemas.produsts_data])
def get_produsts(db:Session=Depends(get_db)):
    return Services.get_product(db)

@router.get("/produsts/{product_id}",response_model=list[Schemas.produsts_data])
def search_product(product_id:int,db:Session=Depends(get_db)):
    return Services.search_product(product_id,db)