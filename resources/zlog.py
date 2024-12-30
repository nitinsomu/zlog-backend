from flask_restful import Resource

class Zlog(Resource):
    def get(self):
        return {"hello" : "world"}
    
