from flask import Blueprint, render_template, request, Response
import json


views = Blueprint('views', __name__)

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
			localStorage.getItem('email') ? window.location.replace('/home') : window.location.replace('/auth');
		</script>
	'''

@views.route('/home')
def home():
	return render_template('home.html')

@views.route('/gettasks', methods=['POST'])
def getTasks():
	req = request.get_json()
	return tasksToJSON(req['email'])

@views.route('/synctasks', methods=['POST'])
def syncTasks():
	req = request.get_json()
	DB.updateTasks(req['email'], req['taskList'])
	return Response(status=200)

@views.route('/getuser', methods=['POST'])
def getUser():
	req = request.get_json()
	user = DB.getUserDetails(req['email'])
	return json.dumps(user['fName'])
