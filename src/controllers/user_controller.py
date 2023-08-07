from flask import request , make_response , json
from flask_jwt_extended import create_access_token
from models.user_model import User
import bson.json_util as json_util
from utils.constants import HTTP_201_CREATED , HTTP_400_BAD_REQUEST , USER_REGISTERED_MESSAGE , USER_MISSING_ERROR , INVALID_PASSWORD_ERROR
import datetime

def register():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    user = User(username , password)
    saved_user = user.save_user()
    json_version = json_util.dumps(saved_user)
    return make_response({'message': USER_REGISTERED_MESSAGE , 'user':json_version} , HTTP_201_CREATED)
    
def login():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    user = User(username , password)
    
    if not user:
        return make_response({'message': USER_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
    
    if password != user['password']:
        return make_response({'message':INVALID_PASSWORD_ERROR} , HTTP_400_BAD_REQUEST)
    
    access_token = create_access_token(identity=username , fresh=datetime.timedelta(minutes=30))
    return make_response({'message':{'access_token':access_token}} , HTTP_201_CREATED)