from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import date

class Order(Base):
    __tablename__ = 'orders'   

    id: Mapped[int] = mapped_column(primary_key=True) 
    order_date: Mapped[date] = mapped_column(db.Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'),nullable=False)
   
    

