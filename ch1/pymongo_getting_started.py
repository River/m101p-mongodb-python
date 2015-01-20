import pymongo
from pymongo import MongoClient

# connect to database
connection = MongoClient('127.0.0.1', 27017)

db = connection.test

#handle to names collection
names = db.names
item = names.find_one()

print item['name']
