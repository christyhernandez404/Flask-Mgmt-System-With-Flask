from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from cache import cache
from utils.util import token_required

@token_required
def save():

    try:
        order_data = order_schema.load(request.json)
    
    except ValidationError as e:
        return jsonify(e.messages), 400 
    
    order = orderService.save(order_data)
    return order_schema.jsonify(order), 201 

# @cache.cached(timeout=30)
def find_all():
    try:
        page = request.args.get("page")
        per_page = request.args.get("per_page")
        page = 1 if not page else page
        per_page = 10 if not per_page else per_page
        all_orders = orderService.find_all(page,per_page)

    except ValueError:
        return jsonify({"error": "Invalid page or per_page parameter"}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return orders_schema.jsonify(all_orders), 200