from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

#results = mycol.find_one()

results = mycol.find()

for r in results:
    pprint(r)