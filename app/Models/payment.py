from app.database import Base
from sqlalchemy import Integer,String,Column,Text,TIMESTAMP,text,CheckConstraint,Numeric,ForeignKey,DECIMAL
from sqlalchemy.orm import relationship

class Payment(Base):
    __tablename__ = "payments"
 
    payment_id = Column(Integer, primary_key=True)
    transaction_id = Column(Text, nullable=False, unique=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False, unique=True)
    amount = Column(Numeric(8, 2))
    payment_method = Column(String(20))
    payment_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    payment_status = Column(String(15))
 
    order = relationship("Order", back_populates="payment")
 
    __table_args__ = (
        CheckConstraint("amount > 0", name="payments_amount_check"),
        CheckConstraint(
            "payment_method IN ('Card', 'UPI', 'Cash')",
            name="payments_method_check",
        ),
        CheckConstraint(
            "payment_status IN ('Successfully', 'Pending', 'Cancelled')",
            name="payments_status_check",
        ),
    )