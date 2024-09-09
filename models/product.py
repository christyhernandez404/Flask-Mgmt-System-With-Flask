from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from models.order_product import order_products
from typing import List

class Product(Base):
    __tablename__ = 'products'   

    id: Mapped[int] = mapped_column(primary_key=True) 
    product_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)

    #relationship definitions
    #linking orders to product
    orders: Mapped[List['Order']] = db.relationship(secondary=order_products,back_populates='products',overlaps="products")

    customers: Mapped[List["Customer"]]= db.relationship(secondary="customer_cart", back_populates='cart')
  
    

