
import hashlib

class FileVerificator:

    def __init__(self):
        file = open('passwrd.txt')
        self.lines = file.readlines()
        file.close()

    def addUser(self, pseudo,password):
        password_hash = hashlib.sha1(str.encode(password)).hexdigest()
        line = str(pseudo) + '|' + password_hash +'\n'

        
        file = open('passwrd.txt', 'r')
        old_text = file.read()
        file.close()
        
        new_file = open('passwrd.txt', 'w')
        new_file.write(old_text+line)
        new_file.close()
    
    def validate(self, pseudo,password):
        for line in self.lines:

            line_splits = (line.replace('\n', '')).split('|')

            password_hash = hashlib.sha1(str.encode(password)).hexdigest()

            if line_splits[0].lower() == pseudo.lower() and line_splits[1] == password_hash:
                return line_splits
                break