import hashlib

# open the file and get password hash
with open('password.txt', 'r') as file:
    pass_hash = file.readline()

# Ask user to enter the password
my_password = input("Enter your password: ")

# calculate the cryptographic hash (SHA-256)
sha = hashlib.sha256()
sha.update(my_password.encode('utf-8')) 
pass_sha = sha.hexdigest()

# check if the password enter was correct
if pass_hash == pass_sha:
    print("You have entered correct password")
else:
    print("You have entered wrong password")