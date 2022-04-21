from pymongo.collection import Collection
from pymongo import MongoClient


class MongoHandler:
    def __init__(self, database: str, connection_retries=3):
        self.connection = MongoClient("mongodb://root:example@localhost:27017")
        self.database = self.connection[database]
        connection_ok_flag = True if self.database.command('ping')['ok'] == 1.0 else False

        while connection_retries > 0 and connection_ok_flag is False:
            self.connection = MongoClient("mongodb://root:example@localhost:27017")
            connection_ok_flag = True if self.database.command('ping')['ok'] == 1.0 else False
            connection_retries -= 1

        print("Connection successful" if connection_ok_flag else "Failed to connect")

    def get_collection(self, collection_name: str) -> Collection:
        return self.database[collection_name]
