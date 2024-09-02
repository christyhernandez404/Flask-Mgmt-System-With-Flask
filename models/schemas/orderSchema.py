from . import ma
from marshmallow import fields

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    order_date = fields.Date(required=True)
    customer_id = fields.Integer(required=True)
    product_ids = fields.List(fields.Integer(), required=False)

    class Meta:
        fields = ("id", "order_date","customer_id", "product_ids")

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True) 

