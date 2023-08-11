from flask import make_response
from flask_jwt_extended import get_jwt
from models.user_model import User
from functools import wraps


def admin_only(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            user = User.is_admin(role)
            print(user)
            
            if user['role'] == 'admin':
                return fn(*args, **kwargs)
            else:
                return make_response({"message": "You are not allowed to access this endpoint."}, 405)
    
        return decorator
    return wrapper

