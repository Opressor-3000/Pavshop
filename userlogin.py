

class UserLogin:
    def __init__(self, dbuser):
        self.__dbuser = dbuser

    def get_user_id(self, userid):
        self.__user = self.__dbuser.query.filter_by(userid)
        return self
    
    def create(self, user):
        self.__user = user
        return self
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def anounymous(self):
        return False
    
    def get_id(self):
        return str(self.__user['id'])