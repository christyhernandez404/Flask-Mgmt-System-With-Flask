from . import ma
from marshmallow import fields

class CustomerSchema(ma.Schema): #inherting our instance of Marshmallow
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    admin = fields.Integer(required=True)


    class Meta:
        fields = ("id", "name","email", "phone","username","password","admin")

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True, exclude=["password"]) 
customer_login = CustomerSchema(exclude=["name", "phone", "username","id","admin"])
