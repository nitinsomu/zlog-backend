from flask import Flask
from resources.routes import zlog_blueprint

app = Flask(__name__)
app.register_blueprint(zlog_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5000)