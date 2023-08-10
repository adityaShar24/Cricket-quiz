from database.mongo import questions_collection
from bson.objectid import ObjectId
class Question:
    def __init__(self , question, options , correct_option , userId):
        self.question = question 
        self.options = options
        self.correct_option = correct_option
        self.userId = ObjectId(userId)
        
    def save_question(self):
        question_id = questions_collection.insert_one({'question':self.question , 'options': self.options , 'correct_option': self.correct_option , 'userId':self.userId}).inserted_id
        return question_id
    
