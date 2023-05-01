import json
from pymongo import MongoClient
import pandas as pd
# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["academicworld"]

# Created or Switched to collection
Faculty = db["faculty"]

Publications = db["publications"]




#university = "santa"

def publication_count_by_year(university):
    # Query
    university_query = { "$regex": university, "$options": "i" }
    print("start query")
    count = db.faculty.aggregate([
        {"$match": {"affiliation.name": university_query}},
        {"$lookup": {"from": "publications", "localField": "publications", "foreignField": "id", "as": "temp"}},
        {"$unwind": "$temp"},
        {"$match":{ "temp.year": {"$gte":2020}}},
        {"$group": {"_id": "$affiliation.name", "pub_cnt": {"$sum": 1}}}
    ])
    df = pd.DataFrame(columns=["_id", "pub_cnt"])
    for record in count:
        df = df.append(record, ignore_index=True)
    print(df)
    return df
#count = publication_count_by_year(university)
#print(count)
