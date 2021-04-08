from flask_pymongo import PyMongo


class MongoDB:
	def __init__(self, app):
		self.mongo = PyMongo(app)

	def get_user(self):
		"""
		Function to fetch the user_credentials.
		"""
		return(list(self.mongo.db.user_details.find({})))

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

	def get_user_details(self):
		"""
		Function to fetch the User's Details. To be Displayed on the Page.
		"""
		pass

	def get_user_tasks(self):
		"""
		Function to fetch the tasks of the user.
		"""
		pass