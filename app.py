import os
#
from flask import Flask
from flask_cors import CORS
#
from resources.routes import zlog_blueprint

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(zlog_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5000)