from flask import Blueprint, render_template, request
import json
import re


views = Blueprint('views', __name__)
regExOb = re.compile(r'\[(x?)\] <(.*)> (.*)')

def initViewDB(dbObject):
	global DB
	DB = dbObject

def parseAsTask(taskOb):
	task = {'done': False, 'class': taskOb.group(2), 'cont': taskOb.group(3)}
	if (taskOb.group(1) == 'x'):
		task['done'] = True
	return task

def tasksToJSON(username, todo=False):
	taskList = []
	if todo: 
		with (open('.todo', 'r')) as file:
			for i in file.readlines():
				taskOb = regExOb.match(i)
				if taskOb:
					taskList.append(parseAsTask(taskOb))
	else:
		taskList = DB.getUserTasks(username)
	return json.dumps(taskList)

@views.route('/')
def landing():
	return '<script>window.location.href="/auth"</script>'

@views.route('/home')
def home():
	return render_template('home.html')

@views.route('/api', methods=['POST'])
def getTasks():
	return tasksToJSON(request.get_json()['username'])
