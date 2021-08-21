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

@views.route('/api', methods=['POST'])
def getTasks():
	req = request.get_json()
	if req['sync']:
		DB.updateTasks(req['email'], req['taskList'])
		return Response(status=200)
	else:
		return tasksToJSON(req['email'])
