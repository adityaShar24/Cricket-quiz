from database.mongo import users_collection

class User:
    def __init__(self , username , password , role='basic'):
        self.username = username
        self.password = password
        self.role = role
        
    def save_user(self):
        user_id = users_collection.insert_one({'username':self.username , 'password':self.password , 'role':self.role}).inserted_id
        return user_id
    
    def find_by_username(username):
        user = users_collection.find_one({'username':username})
        return user
    
    def get_all_users():
        users = users_collection.find()
        list_all_users = list(users)
        return list_all_users