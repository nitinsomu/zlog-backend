import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
user_db = db["users"]