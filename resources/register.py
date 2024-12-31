from flask import request
from flask_restful import Resource
#
from db.db_connection import user_db
#
from dto.user import UserDTO
#
from services.hashing import Hashing

class Register(Resource):
    def __init__(self):
        self.hashing = Hashing()

    def post(self):
        try:
            data = request.json
            username = data.get("username")
            password = data.get("password")
            hashed_password = self.hashing.hash_password(password=password)
            if not username or not password:
                return {"error" : "Username or password cannot be empty"}, 400
            
            if user_db.find_one({"username": username}):
                return {"error": "Username already exists"}, 400
            
            user = UserDTO(username=username, password=hashed_password.decode())
            user_document = user.to_dict()
            result = user_db.insert_one(user_document)
            return {"user_id" : str(result.inserted_id)}, 200
        
        except Exception as e:
            return {"error" : str(e)}, 500

    
