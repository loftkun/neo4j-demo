from neo4j import GraphDatabase, basic_auth

endpoint = 'bolt://172.17.0.2:7687'
user = 'neo4j'
password = 'neo4j'

# connect
auth = basic_auth(user, password)
driver = GraphDatabase.driver(endpoint, auth=auth)
session = driver.session()

# search
records = session.run("MATCH (n) RETURN n")
for record in records:    
    # Node : https://neo4j.com/docs/api/python-driver/current/types/graph.html#neo4j.types.graph.Node
    node = record["n"]
    
    # id labels
    print("{} {}".format(node.id, node.labels))
    
    # properties
    keys = node.keys()
    for key in keys:
        val = node.get(key)
        if type(val) is str:
            val = str(val.encode('utf-8'))
        print("  {} : {}".format(key, val))

session.close()