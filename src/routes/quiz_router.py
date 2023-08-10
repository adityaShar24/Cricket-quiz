from flask import Blueprint
from controllers.quiz_controller import create_question
from flask_jwt_extended import jwt_required
from auth.admin import admin_only

quiz_bp = Blueprint('quiz_bp' , __name__)

@quiz_bp.post('/create_question')
@jwt_required()
@admin_only()
def create_question_wrapper():
    return create_question()
