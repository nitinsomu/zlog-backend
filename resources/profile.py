import jwt
#
from flask import request
from flask_restful import Resource

class Profile(Resource):
    def get(self):
        try:
            cookie = request.cookies.get('token')
            data = jwt.decode(cookie, "thisisasamplesecretkeyforthezlogproject", algorithms=["HS256"])
            return data, 200
        except Exception as e:
            return {"error" : str(e)}, 500