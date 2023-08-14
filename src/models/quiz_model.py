from database.mongo import questions_collection , answers_collection
from bson.objectid import ObjectId
class Question:
    def __init__(self , question, options , correct_option):
        self.question = question 
        self.options = options
        self.correct_option = correct_option
        
    def save_question(self):
        question_id = questions_collection.insert_one({'question':self.question , 'options': self.options , 'correct_option': self.correct_option}).inserted_id
        return question_id
    
class Answer():
    def __init__(self , questionId , selected_option , userId):
        self.questionId = ObjectId(questionId)
        self.selected_option = selected_option
        self.userId = ObjectId(userId)
        
    def save_answer(self):
        answer_id = answers_collection.insert_one({'questionId':self.questionId , 'selected_option':self.selected_option , 'userId':self.userId}).inserted_id
        return answer_id  
    
    def is_correct(self):
        question = questions_collection.find_one({'_id': self.questionId})
        correct_option = question['correct_option']
        is_correct = self.selected_option == correct_option
        return is_correct
