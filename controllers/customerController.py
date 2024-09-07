from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema, customer_login
from services import customerService
from marshmallow import ValidationError
from cache import cache


def save(): #name the controller the same as the service it recruites

    try:
        customer_data = customer_schema.load(request.json)
    
    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    
    customer = customerService.save(customer_data)
    return customer_schema.jsonify(customer), 201 #send them the customer object with a 201 successful creation status


# @cache.cached(timeout=30)
def find_all():
    try:
        page =  request.args.get("page")
        per_page = request.args.get("per_page")
        page = 1 if not page else page
        per_page = 10 if not per_page else per_page
        all_customers = customerService.find_all(page, per_page)
    
    except ValueError:
        return jsonify({"error": "Invalid page or per_page parameter"}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return customers_schema.jsonify(all_customers), 200
    
def login():
    try:
        credentials = customer_login.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    token = customerService.login(credentials)

    if token:
        response = {
            "status": "success",
            "message": "successfully logged in",
            "token": token
        }

        return jsonify(response), 200

    else:
        return jsonify({"status":"error","mesage":"invalid username or password"}), 404

