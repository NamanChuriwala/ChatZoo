from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv

load_dotenv('./chatzoo.env')
SECRET_KEY = os.urandom(32)
DB_URI = os.environ.get('DB_URI')

db = SQLAlchemy()
login_manager = LoginManager()
rooms = ['coding', 'gaming', 'art', 'music']

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        import routes
        db.create_all()
    return app
