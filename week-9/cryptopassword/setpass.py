import hashlib

password = input("Set your password: ")

sha = hashlib.sha256()
sha.update(password.encode('utf-8'))
pass_sha = sha.hexdigest()

with open('password.txt', 'w') as file:
    file.write(pass_sha)

print("Your password has been set and hashed\n\n")