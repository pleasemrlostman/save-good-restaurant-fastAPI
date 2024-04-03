from pymongo import MongoClient

class Database:
    _instance = None

    def __new__(cls, database_name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient("mongodb+srv://pleasemrlostman:@cluster0.c49glpk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
            cls._instance.db = cls._instance.client[database_name]
        return cls._instance

    def get_client(self):
        return self.client

    def get_database(self):
        return self.db