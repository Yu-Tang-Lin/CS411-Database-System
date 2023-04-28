uri = "bolt://localhost:7687"
username = "neo4j"
password = "cs411cs411"

driver = GraphDatabase.driver(uri, auth=(username, password))


# Create a session
with driver.session(database='academicworld') as session:
    # Execute a read transaction
    result = session.run('MATCH (k:KEYWORD)-[:INTERESTED_IN]-(f:FACULTY)-[:AFFILIATION_WITH]-(I:INSTITUTE) WHERE I.name = "University of illinois at Urbana Champaign" RETURN count(distinct k) AS keyword_count')
    for record in result:
        print(record)

# Close the driver
driver.close()
