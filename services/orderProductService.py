from database import db 
from models.order_product import OrderProducts 
from sqlalchemy import select 



def find_all():
    query = select(OrderProducts)
    all_order_products = db.session.execute(query).scalars().all()

    return all_order_products