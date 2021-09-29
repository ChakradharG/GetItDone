from flask import Blueprint, render_template, request, Response
import json


views = Blueprint('views', __name__)

Email = {}

def initViewDB(dbObject):
	global DB
	DB = dbObject

def tasksToJSON(email):
	taskList = []
	dbResp = DB.getUserTasks(email)
	if dbResp:
		taskList = dbResp['taskList']
	return json.dumps(taskList)

@views.route('/')
def landing():
	return '''
		<script>
			localStorage.getItem('token') ? window.location.replace('/home') : window.location.replace('/auth');
		</script>
	'''

@views.route('/home')
def home():
	return render_template('home.html')

@views.route('/gettasks', methods=['POST'])
def getTasks():
	req = request.get_json()
	email = Email.get(req['token'])
	if email is not None:
		return tasksToJSON(email)
	else:
		return json.dumps({'logout': True})

@views.route('/synctasks', methods=['POST'])
def syncTasks():
	req = request.get_json()
	email = Email.get(req['token'])
	if email is not None:
		DB.updateTasks(email, req['taskList'])
		return Response(status=200)
	else:
		return json.dumps({'logout': True})

@views.route('/getuser', methods=['POST'])
def getUser():
	req = request.get_json()
	email = Email.get(req['token'])
	if email is not None:
		user = DB.getUserDetails(email)
		return json.dumps(user['fName'])
	else:
		return json.dumps({'logout': True})
