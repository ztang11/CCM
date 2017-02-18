from bson.json_util import dumps, loads
from pymongo import MongoClient

data = None

with open('data.json', 'r') as f:
    data = loads(f.read())

connection = MongoClient()

db = connection.ccm

db.monte_carlo.insert_many(data)

print (db.monte_carlo.count())