from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import date
from typing import List
from models.order_product import order_products


class Order(Base):
    __tablename__ = 'orders'   

    id: Mapped[int] = mapped_column(primary_key=True) 
    order_date: Mapped[date] = mapped_column(db.Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'),nullable=False)

    #relationship definitions
    #links each order to a customer
    #backpopulates in both customer and order establishes a two-way relaiontship
    customer: Mapped['Customer'] = db.relationship(back_populates="orders") 
    #link each order to a product
    products: Mapped[List['Product']] = db.relationship(secondary=order_products,back_populates='orders',overlaps="orders")
   
    

