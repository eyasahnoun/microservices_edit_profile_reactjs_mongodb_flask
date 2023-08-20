import jwt
from functools import wraps
from flask import jsonify, request
import os
from flask_jwt_extended import get_jwt_identity

SECRET_KEY = os.environ.get('SECRET_KEY', 'SDEFfsdA45sdze4AF44hdf8e')


def get_admin_id_from_token():
    current_user = get_jwt_identity()
    return current_user.get('_id') if current_user else None

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            auth_parts = auth_header.split(' ')

            if len(auth_parts) == 2 and auth_parts[0] == 'Bearer':
                token = auth_parts[1]

        if not token:
            return jsonify({'message': 'Token manquant'}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            # You can now use 'data' to access user information
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expiré'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token invalide'}), 401

        return f(*args, **kwargs)

    return decorated

