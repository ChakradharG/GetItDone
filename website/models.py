from website import mongo


def get_user():
	"""
	Function to fetch the user_credentials.
	"""
	print(list(mongo.db.user_details.find({})))


def register_user():
	"""
	Function to register User into the database at the time of signup.
	"""
	pass

def verify_user():
	"""
	Function to verify the user according to the email ID.
	"""
	pass

def store_info():
	"""
	Function to store additional info about the user.
	"""
	pass

def get_user_details():
	"""
	Function to fetch the User's Details. To be Displayed on the Page.
	"""
	pass

def get_user_tasks():
	"""
	Function to fetch the tasks of the user.
	"""
	pass