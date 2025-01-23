import os
#
from db.db_connection import post_db
#
from dto.post import PostDTO
#
from flask import request
from flask_restful import Resource
#
class CreatePost(Resource):
    def post(self):
        try:
            UPLOAD_FOLDER = 'images'
            file = request.files['file']
            if file:
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)
            else:
                file_path = 'images/default.jpg'
            title = request.form.get('title')
            summary = request.form.get('summary')
            content = request.form.get('content')
            if not title or not summary or not content:
                return {'error': 'Title, summary, and content cannot be empty'}, 400
            post = PostDTO(title=title, summary=summary, content=content, image=file_path)
            post_document = post.to_dict()
            post_db.insert_one(post_document)
            return {'message': 'Post created successfully'}, 201
        except Exception as e:
            return {'error': str(e)}, 500   