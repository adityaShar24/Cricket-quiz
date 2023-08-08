from flask import make_response
from flask_jwt_extended import get_jwt
from functools import wraps

def admin_only():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            result = get_jwt()
            print(result)
            username = result["sub"]
            print(username)
            if username == "aditya":
                return fn(*args, **kwargs)
            else:
                return make_response({ "message": "You are not allowed to access this endpoint." }, 405)
    
        return decorator
    return wrapper
