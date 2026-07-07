from app.database import Base
from sqlalchemy import Integer,String,Column,Text,TIMESTAMP,text,CheckConstraint,Numeric,ForeignKey,DECIMAL
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = "orders"
 
    order_id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey("customers.cust_id"), nullable=False)
    order_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    status = Column(String(10), nullable=False)
    total_amount = Column(Numeric(8, 2), nullable=False)
 
    # customer = relationship("Customer", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
    payment = relationship("Payment", back_populates="order", uselist=False)
 
    __table_args__ = (
        CheckConstraint(
            "status IN ('Pending', 'Shipped', 'Delivered', 'Cancelled')",
            name="orders_status_check",
        ),
        CheckConstraint("total_amount >= 0", name="orders_total_amount_check"),
    )