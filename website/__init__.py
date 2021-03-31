import json

from flask import Flask
from dotenv import load_dotenv
import os

from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')


with open("./website/static/secret.json") as file:
    data = json.loads(file.read())
app.config['MONGO_URI'] = data['mongo_uri']
mongo = PyMongo(app)
