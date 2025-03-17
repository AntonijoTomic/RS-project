from cassandra.cluster import Cluster

def connect_to_cassandra():
    """ Kreira konekciju s Cassandra bazom. """
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    print("Connected to Cassandra!")
    return session

def create_keyspace_and_table(session):
    """ Kreira keyspace i tablicu 'products' ako ne postoje. """
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS warehouse
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
    """)
    session.set_keyspace('warehouse')

    session.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id UUID PRIMARY KEY,
            name TEXT,
            quantity INT
        )
    """)
    print("Keyspace and table created!")

# Pokrećemo konekciju odmah pri učitavanju modula
session = connect_to_cassandra()
create_keyspace_and_table(session)
