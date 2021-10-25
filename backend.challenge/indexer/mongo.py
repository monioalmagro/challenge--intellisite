from pymongo import MongoClient


client = MongoClient('mongodb://db/myTestDB')

db = client.myTestDB

collection = db.test_collection


def index_to_database(message):
    try:
        collection.insert_one(message)
    except Exception as e:
        print("ERROR :", e)
