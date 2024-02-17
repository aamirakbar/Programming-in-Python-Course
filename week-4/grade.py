# Get the student ’s marks
marks = int ( input ("Enter the student ’s marks : "))

# Classify the marks into a grade category
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else :
    grade = "F"

# Print the grade
print (f"The student’s grade is {grade}")