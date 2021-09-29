from flask import Blueprint, render_template, request
from passlib.context import CryptContext
import json
import random
import string


auth = Blueprint('auth', __name__)
encryptor = CryptContext(
	schemes=["pbkdf2_sha256"],
	default="pbkdf2_sha256",
	pbkdf2_sha256__default_rounds = 30000)

def initAuthDB(dbObject):
	global DB
	DB = dbObject

@auth.route('/', methods=['GET', 'POST'])
def logIn():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		form = request.get_json()
		try:
			pwdValid = encryptor.verify(
				form['password'],
				DB.getUserCredentials(form['email'])['pwdHash']
			)
		except TypeError:
			# When the email doesn't exist
			return json.dumps({'userExists': False, 'pwdValid': False})
		else:
			if pwdValid:
				token = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 27))
				Email[token] = form['email']
				return json.dumps({'userExists': True, 'pwdValid': True, 'token': token})
			else:
				return json.dumps({'userExists': True, 'pwdValid': False})

@auth.route('/signup', methods=['GET', 'POST'])
def signUp():
	if request.method == 'GET':
		return render_template('signup.html')
	elif request.method == 'POST':
		form = request.get_json()
		if DB.getUserDetails(form['email']):
			return json.dumps({'userExists': True})
		else:
			form['password'] = encryptor.hash(form['password'])
			DB.registerUser(form)
			return json.dumps({'userExists': False})

def initEmail(E):
	global Email
	Email = E
