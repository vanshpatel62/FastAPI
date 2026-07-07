from app.database import Base
from sqlalchemy import Integer,String,Column,Text,TIMESTAMP,text,CheckConstraint,Numeric,ForeignKey,DECIMAL
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "products"
 
    p_id = Column(Integer, primary_key=True)
    p_name = Column(String(50), nullable=False)
    category = Column(String(20))
    price = Column(Numeric(8, 2))
    stock = Column(Integer)
    brand = Column(String(20))
 
    order_items = relationship("OrderItem", back_populates="product")
 
    __table_args__ = (
        CheckConstraint("price > 0", name="products_price_check"),
        CheckConstraint("stock >= 0", name="products_stock_check"),
    )