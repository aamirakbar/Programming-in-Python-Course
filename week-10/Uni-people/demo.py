# This file has the main bolck of code

# importing the terminal color module
from termcolor import colored

# importing the required modules
from student import Student
from course import Course
from employee import Teacher, Staff

student = Student("Ali", [Course("OOP", 4), Course("Calculus"), Course("English")])
teacher = Teacher("Babar", "100000", [Course("OOP", 4), Course("Networking"), Course("AI", 4)])
staff = Staff("Fakhar", "150000", "Registrar")

print(colored(f"Description of student: {student} \n", "green"))
print(colored(f"Description of teacher: {teacher} \n", "yellow"))
print(f"Description of staff: {staff} \n")
