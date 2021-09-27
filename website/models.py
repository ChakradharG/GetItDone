from pymongo import MongoClient
from pymongo.message import query


class DataBaseHelpers:
	def __init__(self, url):
		self.db = MongoClient(url)['GetItDone']

	def getUserDetails(self, email):
		return self.db['user_details'].find_one({'email': email})

	def getUserCredentials(self, email):
		return self.db['user_credentials'].find_one({'email': email})

	def getUserTasks(self, email):
		return self.db['user_tasks'].find_one({'email': email})

	def registerUser(self, form):
		pwdHash = form['password']
		del form['password']
		self.db['user_details'].insert_one(form)
		self.db['user_credentials'].insert_one({'email': form['email'], 'pwdHash': pwdHash})

	def updateTasks(self, email, taskList):
		self.db['user_tasks'].update_one({'email': email}, {'$set': {'taskList': taskList}}, upsert=True)
