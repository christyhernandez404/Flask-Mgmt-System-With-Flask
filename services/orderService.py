from database import db 
from models.order import Order, Order
from models.order_product import OrderProducts
from sqlalchemy import select 


def save(order_data):

    new_order = Order(order_date=order_data['order_date'], customer_id=order_data['customer_id'])
    db.session.add(new_order)
    db.session.commit()

    product_ids = order_data.get('product_ids')

    for product_id in product_ids:
        order_product = OrderProducts(order_id=new_order.id, product_id=product_id)
        db.session.add(order_product)
    
    db.session.commit()
    return new_order

def find_all():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()

    return all_orders