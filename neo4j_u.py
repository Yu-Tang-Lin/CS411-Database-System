uri = "bolt://localhost:7687"
username = "neo4j"
password = "cs411cs411"
from neo4j import GraphDatabase
driver = GraphDatabase.driver(uri, auth=(username, password))
university = "University of illinois at Urbana Champaign"


def keyword_count(university):
    # Create a session
    with driver.session(database='academicworld') as session:
        # Execute a read transaction
        result = session.run('MATCH (k:KEYWORD)-[:INTERESTED_IN]-(f:FACULTY)-[:AFFILIATION_WITH]-(I:INSTITUTE) '
                             'WHERE I.name = "' + str(university) + '" RETURN count(distinct k) AS keyword_count')
        for record in result:
            print(record)
    return result
count = keyword_count(university)
# Close the driver
driver.close()
