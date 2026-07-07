from app.database import Base
from sqlalchemy import Integer,String,Column,Text,TIMESTAMP,text,CheckConstraint,Numeric,ForeignKey,DECIMAL
from sqlalchemy.orm import relationship

class OrderItem(Base):
    __tablename__ = "order_items"
 
    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True)
    items_id = Column(Integer, ForeignKey("products.p_id"), primary_key=True)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(8, 2))
 
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
 
    __table_args__ = (
        CheckConstraint("quantity > 0", name="order_items_quantity_check"),
        CheckConstraint("unit_price > 0", name="order_items_unit_price_check"),
    )