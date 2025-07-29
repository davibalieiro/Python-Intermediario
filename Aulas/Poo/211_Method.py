# Method vs @classmethod vs @staticmethod
# method = self, method de isinstance
# @classmethod - metodo de classe
# @staticmethod - method estatic(self not, cls not)

class Connection:
    # self é necessariamente usado para um metodo de intancias
    def __init__(self, host='localhost') -> None:
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def soma(x,y):
        return x + y

# conect = Connection()
# conect.set_user('Davi')
# conect.set_password(123)
# print(conect.user)
# print(conect.password)

conect = Connection.create_with_auth('Davi', 123)
