# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host= 'localhost'):
        self.host = host
        self.user = None
        self.password = None
    def set_user(self, user):
        self.user = user
    def set_password(self, password):
        self.password = password
        
    @classmethod
    def create_with_auth(cls, user, passaword):
        connection = cls()
        connection.user = user
        connection.password = passaword
        return connection