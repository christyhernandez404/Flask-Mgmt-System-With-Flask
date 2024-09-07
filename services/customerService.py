from database import db #services interact directly with the db
from models.customer import Customer #need this to create customer objects
from sqlalchemy import select #so we can query our db

from utils.util import encode_role_token


def save(customer_data):

    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=customer_data['password'])
    db.session.add(new_customer)
    db.session.commit() #adding our new customer to our db

    db.session.refresh(new_customer)
    return new_customer

def find_all(page=1, per_page=10):
    query = select(Customer)
    all_customers = db.paginate(query,page=int(page), per_page=int(per_page ))

    return all_customers

def login(credentials):
    query = select(Customer).where(Customer.email == credentials['email']) #select the customer from the Customer table where the customer's email matches the one provided in the credentials.
    customer = db.session.execute(query).scalar_one_or_none()

    if customer and customer.password == credentials['password']:
        auth_token = encode_role_token(customer.id, customer.admin)
        return auth_token
    
    return None