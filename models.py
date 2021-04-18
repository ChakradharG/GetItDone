from website import mongo



class DatabaseModel:
	def __init__(self):
		pass

	def get_user(self, user_mail):
		"""
		Function to fetch the user_credentials.
		"""
		return list(mongo.db.user_details.find({"email": user_mail}))


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

	def authenticate_user(self, user_mail='', user_password=''):
		"""
		Function to authenticate the user.
		"""
		is_authorized = False
		try:
			print(self.get_user(user_mail))
		except:
			print("Error Occurred")