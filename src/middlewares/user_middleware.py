from flask import request , make_response , json
from models.user_model import User
from utils.constants import REGISTER_ENDPOINT , USERNAME_MISSING_ERROR , HTTP_400_BAD_REQUEST , PASSWORD_MISSING_ERROR , USERNAME_EXISTS_ERROR

def register_middleware():
    if request.endpoint == REGISTER_ENDPOINT:
        body = json.loads(request.data)
        username = body['username']
        password = body['password']

        if not username:
            return make_response({'message': USERNAME_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        if not password:
            return make_response({'message': PASSWORD_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        existing_user = User.find_by_username(username)
        if existing_user:
            return make_response({'message': USERNAME_EXISTS_ERROR})