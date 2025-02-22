from flask_restful import Resource
#
from db.db_connection import post_db
#
from bson import ObjectId

class SinglePost(Resource):
    def get(self, post_id):
        try:
            content = post_db.find_one({"_id": ObjectId(post_id)})
            content['_id'] = str(content['_id'])
            return content, 200
        except Exception as e:
            return {'error': str(e)}, 500