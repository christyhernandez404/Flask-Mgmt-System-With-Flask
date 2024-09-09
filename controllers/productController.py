from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError
from cache import cache


def save(): 

    try:
        product_data = product_schema.load(request.json)
        #request json : captures the incoming JSON data sent by the client in a POST request
        # schema deserializes the incoming json and validates it according to the product schema
    
    except ValidationError as e:
        return jsonify(e.messages), 400 
    
    product = productService.save(product_data)
    return product_schema.jsonify(product), 201 


# @cache.cached(timeout=30)
def find_all():
    try:
        page = request.args.get("page")
        per_page = request.args.get("per_page")
        page = 1 if not page else page
        per_page = 10 if not per_page else per_page
        all_products = productService.find_all(page, per_page)

    except ValueError:
        return jsonify({"error": "Invalid page or per_page parameter"}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return products_schema.jsonify(all_products), 200