import json
from pymongo import MongoClient

# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["academicworld"]

# Created or Switched to collection
Collection = db["faculty"]

Collection = db["publications"]



# Query
count = db.faculty.count_documents({"position": "Assistant Professor"})
print(count)