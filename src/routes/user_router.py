from flask import Blueprint
from controllers.user_controller import register
from flask_caching import Cache

cache = Cache()
auth_bp = Blueprint('auth_bp' , __name__)

@auth_bp.post('/register')
def register_user_wrapper():
    return register()

