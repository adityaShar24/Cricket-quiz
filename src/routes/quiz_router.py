from flask import Blueprint , render_template
from controllers.quiz_controller import create_question , submit_answer , random_questions

from flask_jwt_extended import jwt_required
from auth.admin import admin_only

quiz_bp = Blueprint('quiz_bp' , __name__)

@quiz_bp.post('/create_question')
@jwt_required()
@admin_only(role='admin')
def create_question_wrapper():
    return create_question()

@quiz_bp.route('/create_question.html', methods =['POST' , 'GET'])
def render_create_question():
    return render_template('./create_question.html')

@quiz_bp.post('/submit_answer')
def submit_answer_wrapper():
    return submit_answer()

@quiz_bp.get('/start_quiz')
def get_questions_wrapper():
    return random_questions()
