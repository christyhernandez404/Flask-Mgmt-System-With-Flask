from database import db 
from models.product import Product
from models.customer import Customer
from models.order import Order
from models.order_product import order_products
from models.cart import customer_cart
from models.order_product import order_products
from sqlalchemy import select 
from datetime import date

def get_customer(customer_id):
    customer = db.session.query(Customer).get(customer_id)
    if not customer:
        raise ValueError("customer not found")
    return customer

def add_items_to_cart(customer_id, cart_data):

    customer = get_customer(customer_id)
    products_ids = cart_data['product_ids']

    customer = db.session.query(Customer).get(customer_id)
    if not customer:
        raise ValueError("Customer not found")

    for product_id in products_ids:
        product = db.session.query(Product).get(product_id)
        if not product:
            raise ValueError("Product id: {product_id}, not found. ")
        if product not in customer.cart:
            customer.cart.append(product)
            print(product.id, product.product_name, product.price)
       
    db.session.commit()

def remove_item_from_cart(customer_id, cart_data):
    customer = get_customer(customer_id)
    product_id = cart_data['product_id']

    customer = get_customer(customer_id)
    product = db.session.query(Product).get(product_id)

    if not product:
        raise ValueError("product not found")
    if product in customer.cart:
        customer.cart.remove(product)
        db.session.commit()

def view_cart(customer_id, page, per_page):
    query = select(customer_cart).where(customer_cart.c.customer_id == customer_id)
    all_cart_items = db.paginate(query, page=int(page), per_page=int(per_page))
    return all_cart_items

def empty_cart(customer_id):
    customer = get_customer(customer_id)
    customer.cart.clear()
    db.session.commit()

def place_order(customer_id):
    customer = get_customer(customer_id)

    if not customer.cart:
        raise ValueError ("Cart is empty")
    
    new_order = Order(customer_id=customer.id, order_date=date.today())

    for product in customer.cart:
        new_order.products.append(product)
    
    customer.cart.clear()
    
    db.session.add(new_order)

    db.session.commit()
    return new_order