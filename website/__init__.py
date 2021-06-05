from flask import Flask
import json
from .views import views, initViewDB
from .auth import auth, initAuthDB
from .models import DataBaseHelpers


with open('secret.json') as file:
	data = json.loads(file.read())

app = Flask(__name__)
app.config['SECRET_KEY'] = data['SECRET_KEY']
dbObject = DataBaseHelpers(data['MONGO_URI'])

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')

initViewDB(dbObject)
initAuthDB(dbObject)
