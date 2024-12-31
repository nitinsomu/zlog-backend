import bcrypt

class Hashing():
    def __init__(self):
        self.salt = bcrypt.gensalt()

    def hash_password(self, password: str):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), self.salt)
        return hashed_password
    
    def validate_password(self, password: str, hash: str):
        return bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8'))

