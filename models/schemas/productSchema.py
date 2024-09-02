from . import ma
from marshmallow import fields

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    product_name = fields.String(required=True)
    price = fields.Float(required=True)

    class Meta:
        fields = ("id", "product_name","price")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True) 

