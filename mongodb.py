import json
from pymongo import MongoClient

# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["academicworld"]

# Created or Switched to collection
Faculty = db["faculty"]

Publications = db["publications"]



# Query
#count = db.faculty.count_documents({"position": "Assistant Professor"})
count = db.faculty.aggregate([
    {"$match": {"affiliation.name": "University of illinois at Urbana Champaign"}},
    {"$lookup": {"from": "publications", "localField": "publications", "foreignField": "id", "as": "temp"}},
    {"$unwind": "$temp"},
    { "$match":{ "temp.year": {"$gte":2020}}},
    {"$group": {"_id": "$affiliation.name", "pub_cnt": {"$sum": 1}}}
])

for result in count:
    print(result['pub_cnt'])
