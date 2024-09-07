from . import ma
from marshmallow import fields

#incoming order data
'''
{
    "customer_id": int,
    "product_ids": [ints] list of product ids that will be used to create the relationship from this order to all the products
}
'''

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    order_date = fields.Date(required=True)
    customer_id = fields.Integer(required=True)
    products = fields.Nested("ProductSchema", many=True)

    class Meta:
        fields = ("id", "order_date","customer_id", "product_ids", "products")

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True) 

