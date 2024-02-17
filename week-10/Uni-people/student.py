#This file has the implementation of the Student class

from person import Person

class Student(Person):

	# constructor
	def __init__(self, name, courses=[]):
		super().__init__(name)
		self.courses = courses
		
	def __repr__(self):
		st = super().__repr__()
		return st + f" I am a student and my courses are {self.courses}"
