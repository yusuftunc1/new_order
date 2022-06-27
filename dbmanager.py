from connection import connection


class dbmanager():
    def __init__(self):
        self.connection = connection
        self.cursor =self.connection.cursor()
    
    def __del__(self):
        self.connection.close()

