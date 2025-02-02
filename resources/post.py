import jwt
import os
#
from db.db_connection import post_db
#
from dto.post import PostDTO
#
from flask import request
from flask_restful import Resource
#
class Post(Resource):
    def post(self):
        try:
            UPLOAD_FOLDER = 'static'
            file = request.files['file']
            if file:
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)
            else :
                file_path = os.path.join(UPLOAD_FOLDER, "default.png")
            title = request.form.get('title')
            summary = request.form.get('summary')
            content = request.form.get('content')
            if not title or not summary or not content:
                return {'error': 'Title, summary, and content cannot be empty'}, 400
            token = request.headers.get('Authorization')
            token = request.cookies.get('token')
            decoded_token = jwt.decode(token, 'thisisasamplesecretkeyforthezlogproject', algorithms=['HS256'])
            username = decoded_token.get('username')
            post = PostDTO(title=title, summary=summary, content=content, image=file.filename, username=username)
            post_document = post.to_dict()
            post_db.insert_one(post_document)
            return {'message': 'Post created successfully'}, 201
        except Exception as e:
            return {'error': str(e)}, 500   
    
    def get(self):
        try:
            posts = post_db.find()
            print(post for post in posts)
            posts_list = [{**post, '_id': str(post['_id'])} for post in posts]
            posts_list.sort(key=lambda x: x['_id'], reverse=True)
            return {'posts': posts_list}, 200
        except Exception as e:
            return {'error': str(e)}, 500
