
class Person():
	"""Store Person Info"""
	def __init__(self, name, gender, avatar):
		self.name = name
		self.gender = gender
		self.avatar_url = avatar

class Director(Person):
	"""Store Director Info"""
	def __init__(self, name, gender, avatar):
		Person.__init__(self, name, gender, avatar)

class Actor(Person):
	"""Store Actor Info"""
	def __init__(self, name, gender, avatar):
		Person.__init__(self, name, gender, avatar)