# This file has the implementation of the Course class

class Course:
	def __init__(self, name, ch=3):
		self.name = name
		self.ch = ch
		
	def __repr__(self):
		return f"Course Name: {self.name}, Course Credit Hrs: {self.ch}"
