from pass_manager import PasswordManager

pm = PasswordManager()

print(pm.set_password("gmail", "gmailpass"))
print(pm.check_password("gmail", "gmailpass"))