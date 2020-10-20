import sqlite3
from sqlite3 import Error

class SQLite3():
    
    def __init__(self, dbName):
        self.dbName = dbName
        self.conn = self.createConnection()
    
    def createConnection(self):
        """
        create database connection
        """
        conn = None
        db_file = self.dbName #"klscp.sqlite"
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        return conn