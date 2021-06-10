from pymongo import MongoClient
from pymongo.message import query


class DataBaseHelpers:
	def __init__(self, url):
		self.db = MongoClient(url)['GetItDone']

	def getUserDetails(self, email):
		"""
		write this
		"""
		return self.db['user_details'].find_one({'email': email})

	def getUserCredentials(self, email):
		"""
		write this
		"""
		return self.db['user_credentials'].find_one({'email': email})

	def getUserTasks(self, email):
		"""
		write this
		"""
		return self.db['user_tasks'].find_one({'email': email})
	
	def registerUser(self, form):
		"""
		Function to register User into the database at the time of signup.
		"""
		pwdHash = form['password']
		del form['password']
		self.db['user_details'].insert_one(form)
		self.db['user_credentials'].insert_one({'email': form['email'], 'pwdHash': pwdHash})
	
	def updateTasks(self, email, taskList):
		"""
		write this
		"""
		self.db['user_tasks'].update_one({'email': email}, {'$set': {'taskList': taskList}}, upsert=True)

	def verify_user(self):
		"""
		Function to verify the user according to the email ID.
		"""
		pass

	def store_info(self):
		"""
		Function to store additional info about the user.
		"""
		pass

	def authenticate_user(self, user_mail='', user_password=''):
		"""
		Function to authenticate the user.
		"""
		# is_authorized = False
		# try:
		# 	print(self.get_user(user_mail))
		# except:
		# 	print("Error Occurred")
		pass