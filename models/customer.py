from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from models.cart import customer_cart,cart


class Customer(Base):
    __tablename__ = 'customers'   

    id: Mapped[int] = mapped_column(primary_key=True) 
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(db.String(20), nullable=False)
    username: Mapped[str] = mapped_column(db.String(255), nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    admin: Mapped[int] = mapped_column(db.Integer, nullable=False)


    #relationship definitions
    cart: Mapped[List['Product']] = db.relationship("Product", secondary="customer_cart", back_populates="customers")

    orders: Mapped[List['Order']] = db.relationship(back_populates='customer') 
    

