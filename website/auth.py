from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/')
def signIn():
	return render_template('signin.html')

@auth.route('/signup')
def signUp():
	return '<h1>signup</h1>'
