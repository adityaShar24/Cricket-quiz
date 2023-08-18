HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400
HTTP_405_FORBIDDEN = 405

USERNAME_MISSING_ERROR = 'Please enter username'
PASSWORD_MISSING_ERROR = 'Please enter password'
USER_ID_MISSING_ERROR = 'userId should not be empty'
QUESTION_ID_MISSING_ERROR = 'questionId should not be empty'
SELECTED_OPTION_MISSING_ERROR = 'selected option should not be empty'
USERNAME_EXISTS_ERROR = 'username already exists, please enter a unique username'
USERNAME_NOT_EXISTS_ERROR = 'username does not exists, please enter a valid username'
QUESTION_INPUT_MISSING_ERROR = 'Please enter a question.'
OPTIONS_MISSING_ERROR = 'Please enter options.'
CORRECT_OPTION_MISSING_ERROR = 'Please specify the correct option for the question.'
USER_MISSING_ERROR = "No user found."
INVALID_PASSWORD_ERROR = "Invalid password."


REGISTER_ENDPOINT = 'auth_bp.register_user_wrapper'
LOGIN_ENDPOINT = 'auth_bp.login_user_wrapper'
CREATE_QUESTION_ENDPOINT = 'quiz_bp.create_question_wrapper'
SUBMIT_ANSWER_ENDPOINT = 'quiz_bp.submit_answer_wrapper'


USER_REGISTERED_MESSAGE = "user {username} has been registered successfully!"
QUESTION_CREATED_MESSAGE = 'Question created successfully.'
FETCHED_QUESTIONS_MESSAGE ="Question Fetched Successfully!"

CORRECT_OPTION_MESSAGE = 'Correct! Your answer is correct.'
INCORRECT_OPTION_MESSAGE ='Your answer is incorrect.'

CONNECTED_TO_MONGODB = 'Connection to MongoDb Successful!'
CONNECTION_FAILED = 'Failed to Connect'

ACCESS_FORBIDDEN = "You are not allowed to access this endpoint."

