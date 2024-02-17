#Add code to swap variables a and b (so that a refers to the value previously referred to by b and vice versa)

a = 5
b = 8

print ("a = " + str(a))
print ("b = " + str(b))

#1. We can swap values in python only with one line code as follow.
#a, b = b, a

#2. Also, we can swap values with the help of a temporary variable as:
temp = b
b = a
a = temp

print ("a = " + str(a))
print ("b = " + str(b))
