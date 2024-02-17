# Iterate through the range and identify numbers
for num in range (1 , 31):
    if num % 3 == 0 and num % 5 == 0:
        print (f"{num} is a multiple of both 3 and 5")
    else :
        print (f"{num} is not a multiple of both 3 and 5")