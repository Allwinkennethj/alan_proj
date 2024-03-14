from flask import Flask
from flask_cors import CORS
from config import Config,db
from users.view import users
def create_app():
    app=Flask(__name__)
    app.register_blueprint(users)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app,origins="*")
    return app
