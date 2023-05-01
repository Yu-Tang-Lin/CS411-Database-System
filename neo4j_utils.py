uri = "bolt://localhost:7687"
username = "neo4j"
password = "cs411cs411"
from neo4j import GraphDatabase
driver = GraphDatabase.driver(uri, auth=(username, password))
import pandas as pd


def keyword_count(university):
    # Create a session
    with driver.session(database='academicworld') as session:
        university = university.capitalize()
        print("start query neo4j")
        results = []
        # Execute a read transactions
        sql='MATCH (k:KEYWORD)-[:INTERESTED_IN]-(f:FACULTY)-[:AFFILIATION_WITH]-(I:INSTITUTE) ''WHERE I.name CONTAINS "' + university + '" RETURN I.name AS name ,count(distinct k) AS keyword_count'
        result = session.run(sql)
        # Append each query result record as a dictionary to the results list
        for record in result:
            results.append(dict(record))
        df = pd.DataFrame(results)
    return df

#university = "California"
#count = keyword_count(university)
#Close the driver
#sql1 = 'MATCH (k:KEYWORD)-[:INTERESTED_IN]-(f:FACULTY)-[:AFFILIATION_WITH]-(I:INSTITUTE) WHERE I.name CONTAINS "California" RETURN I.name AS name ,count(distinct k) AS keyword_count'
#print("sql1: ", sql1)
#print(count)
#sql = 'MATCH (k:KEYWORD)-[:INTERESTED_IN]-(f:FACULTY)-[:AFFILIATION_WITH]-(I:INSTITUTE) ''WHERE I.name CONTAINS "' + university + '" RETURN I.name AS name ,count(distinct k) AS keyword_count'
#print("sql0: ", sql)

driver.close()
