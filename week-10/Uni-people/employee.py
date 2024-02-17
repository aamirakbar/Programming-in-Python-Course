# This file the implementation of three classes

from person import Person

class Employee(Person):
	def __init__(self, name, sal):
		super().__init__(name)
		self.__salary = sal
		
	def __repr__(self):
		st = super().__repr__()
		return st + f" I am an employee and my salary is '{self.__salary}'."
		
class Teacher(Employee):
	def __init__(self, name, sal, courses):
		super().__init__(name, sal)
		self.__courses = courses
		
	def __repr__(self):	
		st = super().__repr__()
		return st + f" I teach: {self.__courses}."
		
class Staff(Employee):
	def __init__(self, name, sal, pos):
		super().__init__(name, sal)
		self.__pos = pos
		
	def __repr__(self):
		st = super().__repr__()
		return st + f" My position is '{self.__pos}'."
