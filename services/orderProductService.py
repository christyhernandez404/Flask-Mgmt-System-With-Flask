from database import db 
from models.order_product import order_products 
from sqlalchemy import select 



def find_all():
    query = select(order_products)
    all_order_products = db.session.execute(query).scalars().all()

    return all_order_products