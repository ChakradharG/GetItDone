from pymongo import MongoClient
from pymongo.message import query


class DataBaseHelpers:
	def __init__(self, url):
		self.db = MongoClient(url)['GetItDone']

	def getUserDetails(self, username):
		"""
		write this
		"""
		return self.db['user_details'].find_one({'username': username})

	def getUserCredentials(self, username):
		"""
		write this
		"""
		return self.db['user_credentials'].find_one({'username': username})

	def getUserTasks(self, username):
		"""
		write this
		"""
		return self.db['user_tasks'].find_one({'username': username})
	
	def register_user(self):
		"""
		Function to register User into the database at the time of signup.
		"""
		pass

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