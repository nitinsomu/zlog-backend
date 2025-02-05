import jwt
import os
#
from bson import json_util
from flask import request, make_response, jsonify
from flask_restful import Resource
#
from db.db_connection import user_db
#
from services.hashing import Hashing

class Login(Resource):
    def __init__(self):
        self.hashing = Hashing()

    def post(self):
        try: 
            data = request.json
            username = data.get("username")
            password = data.get("password")
            if not username or not password:
                return {"error" : "Username or password cannot be empty"}, 400
            user = user_db.find_one({"username" : username})
            if not user:
                return {"error" : "User not found"}, 400
            valid = self.hashing.validate_password(password=password, hash=user.get("password"))
            if valid:
                token = jwt.encode({
                    'username': user.get("username"),
                    'id': str(user.get("_id"))
                }, "thisisasamplesecretkeyforthezlogproject", algorithm="HS256")
                resp = make_response(jsonify({"id": str(user.get("_id")), "username": user.get("username")}))
                resp.set_cookie("token", token)
                return resp
            else:
                return {"error" : "Wrong username or password"}, 400
        except Exception as e:
            return {"error" : str(e)}, 500

