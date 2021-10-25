from pymongo import MongoClient

client = MongoClient('mongodb://db/myTestDB')

db = client.myTestDB

collection = db.test_collection


def find_all():
    x = collection.find()
    return x


def stats():
    makes = collection.distinct('Make')
    a = count_by_make(makes)
    return a


def count_by_make(makes: list):
    return [count(make) for make in makes]


def count(make: str):
    amount = collection.find({'Make': make}).count()
    return {make: amount}

