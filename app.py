from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from database import db
from models.schemas import ma
from limiter import limiter
from cache import cache

#models
from models.customer import Customer
from models.order import Order
from models.product import Product
from models.order_product import order_products




#blueprints
from routes.customerBP import customer_blueprint
from routes.orderBP import order_blueprint
from routes.productBP import product_blueprint
from routes.orderProductBP import order_product_blueprint
from routes.cartBP import cart_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'  

swagger_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Ecommerce API"})

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    blueprint_config(app)
    rate_limit_config(app)
    cache.init_app(app)

    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix="/customers")
    app.register_blueprint(order_blueprint, url_prefix="/orders")
    app.register_blueprint(product_blueprint, url_prefix="/products")
    app.register_blueprint(order_product_blueprint, url_prefix="/order_products")
    app.register_blueprint(cart_blueprint, url_prefix="/cart")
    app.register_blueprint(swagger_blueprint, url_prefix="/api/docs")




def rate_limit_config(app):
    limiter.init_app(app)
    limiter.limit("100/hour")(customer_blueprint)
    limiter.limit("100/hour")(order_blueprint)
    limiter.limit("100/hour")(product_blueprint)
    limiter.limit("100/hour")(order_product_blueprint)
    limiter.limit("10 per second")(swagger_blueprint)







if __name__ == '__main__':

    app = create_app('DevelopmentConfig')

    with app.app_context():
        db.create_all()

    app.run()