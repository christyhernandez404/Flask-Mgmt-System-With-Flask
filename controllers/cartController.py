from flask import request, jsonify
from models.schemas.cartSchema import single_cart_schema, many_cart_schema

from services import cartService
from marshmallow import ValidationError
from utils.util import user_validation
from database import db
from models.product import Product


@user_validation
def add_items_to_cart(token_id):

    try:
        cart_data = single_cart_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400 
    
    try:
        added_products = cartService.add_items_to_cart(token_id, cart_data)
        return jsonify ({"message": "products added to cart"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_validation
def remove_item_from_cart(token_id):
    try:
        cart_data = request.json
        print(cart_data)
        if 'product_ids' not in cart_data:
            return jsonify({"error": "product_ids is required and cant be empty"}), 400
        cart_data = single_cart_schema.load(cart_data)
        print("after the single cart schema", cart_data)
    except ValidationError as e:
        return jsonify(e.messages), 400 
     
    try:
        cartService.remove_item_from_cart(token_id, cart_data)
        return jsonify({"message": "Product removed from cart"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
     

@user_validation
def view_cart(token_id):
    try:
        all_cart_items = cartService.view_cart(token_id)
        print(f"Items returned from service: {all_cart_items}")  # Add this line

    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify(all_cart_items), 200  # Return directly without schema

@user_validation
def empty_cart(token_id):
    try:
        cartService.empty_cart(token_id)
        return jsonify ({"message": "cart has been emptied"}), 200
    
    except ValueError:
        return jsonify({"error": str(e)}), 404
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_validation
def place_order(token_id):
    try:
        new_order = cartService.place_order(token_id)

        return jsonify({
            "message": "Order placed succesfully",
            "order_id": new_order.id,
            "order_date":new_order.order_date
        }),201
    
    except ValueError:
        return jsonify({"error": str(e)}), 404
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
