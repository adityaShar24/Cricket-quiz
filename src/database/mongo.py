from pymongo import MongoClient
from utils.constants import CONNECTED_TO_MONGODB , CONNECTION_FAILED

MONGO_CONNECTION_STRING = 'mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/?retryWrites=true&w=majority'

mongo_client = MongoClient(MONGO_CONNECTION_STRING)

database = mongo_client['Cricket-quiz']
users_collection = database['Users']


try:
    mongo_client.server_info()
    print(CONNECTED_TO_MONGODB)
except Exception as e:
    print(e , CONNECTION_FAILED)
    