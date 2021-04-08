from flask import Blueprint, render_template, request


auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def signIn():
	if request.method == 'GET':
		return render_template('signin.html')
	elif request.method == 'POST':
		data = dict(request.form)
		print("LOGIN")
		return render_template('home.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signUp():
	if request.method == 'GET':
		return render_template('signup.html')
	elif request.method == 'POST':
		data = dict(request.form)
		print("SIGNUP")
		return render_template('signin.html')
