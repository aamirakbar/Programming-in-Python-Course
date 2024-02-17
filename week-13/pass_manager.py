import hashlib
import json

class PasswordManager:
    def __init__(self):
        self.__pass_file = "passwords.json"
        self.__passwords = self.__get_pass_from_file()
        
    def __hash_pass(self, password):
        sha = hashlib.sha256()
        sha.update(password.encode('utf-8'))
        return sha.hexdigest()      
    
    def __get_pass_from_file(self):       
        try:
            with open(self.__pass_file, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Exception occured while getting the file: {e}")
            return None
        
    def __set_pass_file(self):
        try:
            with open(self.__pass_file, 'w') as file:
                json.dump(self.__passwords, file)
                return True
        except Exception as e:
            print(f"Exception occured while saving the file: {e}")
            return False
        
    def check_password(self, pass_for, password):
        if self.__passwords != None:
            return self.__passwords[pass_for] == self.__hash_pass(password)
        return False
    
    def set_password(self, pass_for, password):
        if self.__passwords != None:
            self.__passwords[pass_for] = self.__hash_pass(password)
            return self.__set_pass_file()
        return False
            