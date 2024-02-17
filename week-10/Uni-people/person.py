class Person:
	# static (or class) private attribute
	__next_id = 0

	def __init__(self, name):
		self.__pid = Person.__create_id()
		self.__name = name
		
	# static (or class) private function
	def __create_id():
		pid = "awkum-" + str(Person.__next_id)
		Person.__next_id += 1
		return pid
		
	def __repr__(self):
		return f"My Id is '{self.__pid}' and my name is '{self.__name}'."
