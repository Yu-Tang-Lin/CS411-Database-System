from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
username = "neo4j"
password = "cs411cs411"

driver = GraphDatabase.driver(uri, auth=(username, password))


# Create a session
with driver.session(database='academicworld') as session:
    # Execute a read transaction
    result = session.run('MATCH (f:FACULTY) WHERE f.position = "Assistant Professor" RETURN count(f) AS faculty_count')
    for record in result:
        print(record)

# Close the driver
driver.close()