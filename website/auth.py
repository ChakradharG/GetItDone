from flask import Blueprint, render_template, request
from passlib.context import CryptContext


auth = Blueprint('auth', __name__)
encryptor = CryptContext(
	schemes=["pbkdf2_sha256"],
	default="pbkdf2_sha256",
	pbkdf2_sha256__default_rounds = 30000)

def initAuthDB(dbObject):
	global DB
	DB = dbObject

# encryptor.hash(password)

@auth.route('/', methods=['GET', 'POST'])
def signIn():
	if request.method == 'GET':
		return render_template('signin.html')
	elif request.method == 'POST':
		formData = dict(request.form)
		isValid = encryptor.verify(
			formData['password'],
			DB.getUserCredentials(formData['username'])['pwdHash']
		)
		if isValid:
			return f'<script>localStorage.setItem("username", "{formData["username"]}"); window.location.replace("/home")</script>'
		else:
			return render_template('signin.html', message='Invalid credentials, please try again\n')

@auth.route('/signup', methods=['GET', 'POST'])
def signUp():
	if request.method == 'GET':
		return render_template('signup.html')
	elif request.method == 'POST':
		# formData = dict(request.form)
		return render_template('signin.html')
