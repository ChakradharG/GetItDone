from flask import Blueprint, render_template, request, Response
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

def tasksToJSON(email, todo=False):
	taskList = []
	if todo: 
		with (open('.todo', 'r')) as file:
			for i in file.readlines():
				taskOb = regExOb.match(i)
				if taskOb:
					taskList.append(parseAsTask(taskOb))
	else:
		dbResp = DB.getUserTasks(email)
		if dbResp:
			taskList = dbResp['taskList']
	return json.dumps(taskList)

@views.route('/')
def landing():
	return '''
		<script>
			localStorage.getItem('email') ? window.location.replace('/home') : window.location.replace('/auth');
		</script>
	'''

@views.route('/home')
def home():
	return render_template('home.html')

@views.route('/api', methods=['POST'])
def getTasks():
	req = request.get_json()
	if req['sync']:
		DB.updateTasks(req['email'], req['taskList'])
		return Response(status=200)
	else:
		return tasksToJSON(req['email'])
