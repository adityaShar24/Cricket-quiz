from database.mongo import questions_collection

class Question:
    def __init__(self , question, options , correct_option):
        self.question = question 
        self.options = options
        self.correct_option = correct_option
        
    def save_question(self):
        question_id = questions_collection.insert_one({'question':self.question , 'options': self.options , 'correct_option': self.correct_option}).inserted_id
        return question_id
    