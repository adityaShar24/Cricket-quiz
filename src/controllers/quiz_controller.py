from flask import request, make_response, json
from models.quiz_model import Question
from utils.constants import HTTP_201_CREATED, QUESTION_CREATED_MESSAGE , ACCESS_FORBIDDEN , HTTP_405_FORBIDDEN
import bson.json_util as json_util
from models.user_model import User

def create_question():
    body = json.loads(request.data)
    user_id = body['userId']
    is_admin = User.is_admin(user_id)
    if not is_admin:
        return make_response({"message": ACCESS_FORBIDDEN}, HTTP_405_FORBIDDEN)
    
    question = body['question']
    options = body['options']
    correct_option = body['correct_option']
    questions = Question(question, options, correct_option, user_id)
    saved_questions = questions.save_question()
    json_version = json_util.dumps(saved_questions)
    return make_response({'message': QUESTION_CREATED_MESSAGE, 'question': json_version}, HTTP_201_CREATED)
