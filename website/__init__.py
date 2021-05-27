from flask import Flask
import json


with open('secret.json') as file:
	data = json.loads(file.read())

app = Flask(__name__)
app.config['SECRET_KEY'] = data['SECRET_KEY']
app.config['MONGO_URI'] = data['MONGO_URI']

from .views import views, initDB
from .auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')

initDB(app)
