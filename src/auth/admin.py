from flask import make_response
from flask_jwt_extended import get_jwt
from functools import wraps

def admin_only():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            result = get_jwt()
            print(result)
        return decorator
    return wrapper()