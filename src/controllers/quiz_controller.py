# controller.py
from flask import request, make_response, json
from models.quiz_model import Question , Answer
from flask_jwt_extended import get_jwt
from utils.constants import HTTP_201_CREATED, QUESTION_CREATED_MESSAGE , ACCESS_FORBIDDEN , HTTP_405_FORBIDDEN , CORRECT_OPTION_MESSAGE , INCORRECT_OPTION_MESSAGE
import bson.json_util as json_util
from models.user_model import User

def create_question():
    body = json.loads(request.data)
    
    question = body['question']
    options = body['options']
    correct_option = body['correct_option']
    
    user_id = get_jwt()
    is_admin = User.is_admin(user_id["sub"])
    if not is_admin:
        return make_response({"message": ACCESS_FORBIDDEN}, HTTP_405_FORBIDDEN)
    
    questions = Question(question, options, correct_option)
    saved_questions = questions.save_question()
    
    json_version = json_util.dumps(saved_questions)
    return make_response({'message': QUESTION_CREATED_MESSAGE, 'question': json_version}, HTTP_201_CREATED)

def submit_answer():
    body = json.loads(request.data)
    userId = body['userId']
    questionId = body['questionId']
    selected_option = body['selected_option']
    answers = Answer(userId= userId , questionId= questionId , selected_option= selected_option)
    saved_answers = answers.save_answer()
    json_version = json_util.dumps(saved_answers)
    correct_answer = answers.is_correct()
    if correct_answer:
        response_message = CORRECT_OPTION_MESSAGE
    else:
        response_message = INCORRECT_OPTION_MESSAGE
    return make_response({'message': response_message , 'answer': json_version} , HTTP_201_CREATED)
    
    