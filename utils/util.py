import jwt
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import request, jsonify
#util foldker is only concerned with token generation and validation

SECRET_KEY = "a_very_secret_key"

def encode_token(user_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1), #expiration
        'iat': datetime.now(timezone.utc), #issued at
        'sub': user_id #subject
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]#extracts the token if token is there
                payload = jwt.decode
                print("Payload", payload)
            except jwt.ExpiredSignatureError: #raised if the token has expired
                return jsonify({"message":"Token has expired"}), 401
            except jwt.InvalidTokenError: #raised if the token is invalid 
                return jsonify({"message": "Invalid Token"}), 401
            return f(*args,**kwargs)
        else:
            return jsonify({"message": "Authentication token missing"}), 401
    return wrapper

#=============Role Based Access===============#

def encode_role_token(user_id, role_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1), #expiration
        'iat': datetime.now(timezone.utc), #issued at
        'sub': user_id, #subject
        'admin': role_id
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token