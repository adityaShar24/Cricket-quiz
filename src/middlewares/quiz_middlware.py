from flask import make_response , request , json
from utils.constants import QUESTION_INPUT_MISSING_ERROR , HTTP_400_BAD_REQUEST , OPTIONS_MISSING_ERROR , CORRECT_OPTION_MISSING_ERROR



def create_question_middleware():
    body = json.loads(request.data)
    question = body['question']
    options = body['options']
    correct_option = body['correct_option']
    if not question:
        return make_response({'message': QUESTION_INPUT_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
    if not options:
        return make_response({'message': OPTIONS_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
    if not correct_option:
        return make_response({'message': CORRECT_OPTION_MISSING_ERROR} , HTTP_400_BAD_REQUEST)