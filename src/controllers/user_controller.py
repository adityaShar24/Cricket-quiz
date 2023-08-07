from flask import request , make_response , json
from flask_jwt_extended import create_access_token
from models.user_model import User
import bson.json_util as json_util
from utils.constants import HTTP_201_CREATED , HTTP_400_BAD_REQUEST , USER_REGISTERED_MESSAGE

def register():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    user = User(username , password)
    saved_user = user.save_user()
    json_version = json_util.dumps(saved_user)
    return make_response({'message': USER_REGISTERED_MESSAGE , 'user':json_version} , HTTP_201_CREATED)
    