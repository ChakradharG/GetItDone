from flask import Blueprint, render_template
import json
import re
from website.security import encrypt_password, check_password


views = Blueprint('views', __name__)
regExOb = re.compile(r'\[(x?)\] <(.*)> (.*)')

def parseAsTask(taskOb):
	task = {'done': False, 'class': taskOb.group(2), 'cont': taskOb.group(3)}
	if (taskOb.group(1) == 'x'): task['done'] = True
	return task

def tasksToJSON():
	tasksList = []
	# if todo: 
	with (open('.todo', 'r')) as file:
		for i in file.readlines():
			taskOb = regExOb.match(i)
			if taskOb:
				tasksList.append(parseAsTask(taskOb))
	return json.dumps(tasksList)
				

@views.route('/')
def landing():
	return '<script>window.location.href="/auth"</script>'

@views.route('/home')
def home():
	user_mail = "mishraharsh27@gmail.com"
	user_password = "Harsh@123$"
	hashed = encrypt_password(password=user_password)
	print("Hashed Value:  ", hashed)
	print(check_password(password="harsh@123$", hashed_value=hashed))
	# DatabaseModel().authenticate_user(user_mail=user_mail, user_password=user_password)
	return render_template('home.html')

@views.route('/api')
def getTasks():
	return tasksToJSON()
