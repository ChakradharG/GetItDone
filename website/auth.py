from flask import Blueprint, render_template, request
from passlib.context import CryptContext


auth = Blueprint('auth', __name__)
pwd_context = CryptContext(
	schemes=["pbkdf2_sha256"],
	default="pbkdf2_sha256",
	pbkdf2_sha256__default_rounds = 30000)

def encrypt_password(password):
	return pwd_context.encrypt(password)

def check_password(password, hashed_value):
	return pwd_context.verify(password, hashed_value)

@auth.route('/', methods=['GET', 'POST'])
def signIn():
	if request.method == 'GET':
		return render_template('signin.html')
	elif request.method == 'POST':
		# formData = dict(request.form)
		# check_password
		return '<script>window.location.replace("/home")</script>'

@auth.route('/signup', methods=['GET', 'POST'])
def signUp():
	if request.method == 'GET':
		return render_template('signup.html')
	elif request.method == 'POST':
		# formData = dict(request.form)
		return render_template('signin.html')
