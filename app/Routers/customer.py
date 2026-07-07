# from fastapi import FastAPI,HTTPException,Depends,Request
# # from fastapi.responses import HTMLResponse
# # from fastapi.staticfiles import StaticFiles
# # from fastapi.templating import Jinja2Templates
# from app import Services,Schemas,models
# from app.database import get_db,engine
# from sqlalchemy.orm import Session
# from pydantic import BaseModel
# from typing import Union
# from app.database import engine
# from app.models import Base


# # Customer list
# @   .get("/cust",response_model=list[Schemas.customer_data])
# def get_cust(db:Session=Depends(get_db)):
#     return Services.get_customre(db)

# # Search cudtomer with use id
# @app.get("/cust/{cust_id}",response_model=Schemas.customer_data)
# def search_cust(cust_id:int,db:Session=Depends(get_db)):
#     return Services.search_customer(cust_id,db)
    
# # add customer
# @app.post("/cust",response_model=Schemas.add_customre)
# def create_cust(cust:Schemas.add_customre,db:Session=Depends(get_db)):
#     return Services.create_customre(db,cust)

# @app.put("/cust/{cust_id}",response_model=Schemas.customer_data)
# def update_cust(cust:Schemas.customer_data,cust_id:int,db:Session=Depends(get_db)):
#     cust_update=Services.update_cust(cust_id,cust,db)
#     if not cust_update:
#         raise HTTPException(status_code=404,detail="Book Not Found")
#     return cust_update

# @app.delete("/delete_cust/{cust_id}",response_model=Schemas.customer_data)
# def delete_cust(cust_id:int,db:Session=Depends(get_db)):
#     delete_entry=Services.delet_cust(cust_id,db)
#     if delete_entry:
#         return delete_entry 
#     else:
#         raise HTTPException(status_code=404,detail="Customer Can Not Found")


from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session

from app import Schemas, Services
from app.database import get_db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/customer",
    tags=["Customer"]
)

@router.get("/cust", response_model=list[Schemas.customer_data])
def get_cust(db: Session = Depends(get_db)):
    try:
        # logging.info("customre API called")
        logger.info("    customre API called")
        # logger.critical("    Application Crashed")
        return Services.get_customre(db)
    except Exception as e:
        logger.error(f"Database Error : {e}")
        # raise HTTPException(status_code=500,detail="Error from api side")
        return {"Message":"Error"}


@router.get("/cust/{cust_id}", response_model=Schemas.customer_data)
def search_cust(cust_id: int, db: Session = Depends(get_db)):
    
    logger.info("     customre search  API calling.....")
    return Services.search_customer(cust_id, db)
    
    # logger.error(f"Error : {e}")
    # # raise HTTPException(status_code=500,detail="Error from api side")
    # return {"Message":"Error"}




@router.post("/cust", response_model=Schemas.add_customre)
def create_cust(cust: Schemas.add_customre, db: Session = Depends(get_db)):
    return Services.create_customre(db, cust)


@router.put("/cust/{cust_id}", response_model=Schemas.customer_data)
def update_cust(cust_id: int, cust: Schemas.customer_data, db: Session = Depends(get_db)):
    return Services.update_cust(cust_id, cust, db)


@router.delete("/delete_cust/{cust_id}", response_model=Schemas.customer_data)
def delete_cust(cust_id: int, db: Session = Depends(get_db)):
    return Services.delet_cust(cust_id, db)