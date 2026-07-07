from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import Schemas, Services
from app.database import get_db

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)



@router.get("/peyment",response_model=list[Schemas.payment])
def get_payments(db:Session=Depends(get_db)):
    return Services.get_payments_details(db)