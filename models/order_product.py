from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class OrderProducts(Base):
    __tablename__ = 'order_products'   

    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'), primary_key=True) 
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), primary_key=True)

   
    

