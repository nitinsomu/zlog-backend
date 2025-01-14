from flask_restful import Resource
from flask import make_response

class Logout(Resource):
    def post(self):
        response = make_response({"status": "ok"})
        response.set_cookie('token', '')
        return response