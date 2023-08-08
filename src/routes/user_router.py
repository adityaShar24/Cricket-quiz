from flask import Blueprint
from controllers.user_controller import register , login , get_all_users
from flask_caching import Cache
from flask_jwt_extended import jwt_required
cache = Cache()
auth_bp = Blueprint('auth_bp' , __name__)

@auth_bp.post('/register')
def register_user_wrapper():
    return register()

@auth_bp.post('/login')
def login_user_wrapper():
    return login()
    
@auth_bp.get('/all-users')
@cache.cached(timeout=5)
@jwt_required()
def get_all_users_wrapper():
    return get_all_users()
