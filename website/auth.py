from flask import Blueprint


auth = Blueprint('auth', __name__)

@auth.route('/')
def signIn():
	return '<h1>signin</h1>'

@auth.route('/signup')
def signUp():
	return '<h1>signup</h1>'
