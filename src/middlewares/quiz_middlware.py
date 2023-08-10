from flask import json , make_response , request
from utils.constants import HTTP_400_BAD_REQUEST , QUESTION_INPUT_MISSING_ERROR , OPTIONS_MISSING_ERROR , CORRECT_OPTION_MISSING_ERROR , CREATE_QUESTION_ENDPOINT , USER_ID_MISSING_ERROR

def create_question_middleware():
    if request.endpoint == CREATE_QUESTION_ENDPOINT:
        body = json.loads(request.data)
        question = body['question']
        options = body['options']
        correct_option = body['correct_option']
        userId = body['userId']
        
        if not userId:
            return make_response({'message': USER_ID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        if not question:
            return make_response({'message': QUESTION_INPUT_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        if not options:
            return make_response({'message': OPTIONS_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        if not correct_option:
            return make_response({'message': CORRECT_OPTION_MISSING_ERROR} , HTTP_400_BAD_REQUEST)