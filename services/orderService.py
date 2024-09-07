from database import db 
from models.order import Order
from models.product import Product
from models.order_product import order_products
from sqlalchemy import select 
from datetime import date


def save(order_data):

    new_order = Order(customer_id=order_data['customer_id'], order_date=date.today()) 

    for item_id in order_data['product_ids']:
        query = select(Product).where(Product.id==item_id) 
        item = db.session.execute(query).scalar()
        new_order.products.append(item) 
    db.session.add(new_order)
    db.session.commit()
  
    db.session.refresh(new_order)
    return new_order

def find_all(page=1, per_page=10):
    query = select(Order)
    all_orders = db.paginate(query, page=int(page), per_page=int(per_page))

    return all_orders