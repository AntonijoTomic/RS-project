from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement


def connect_to_cassandra():
    cluster = Cluster(['127.0.0.1'])  
    session = cluster.connect()
    print("Connected to Cassandra!")
    return session


def create_keyspace_and_table(session):
    
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

def insert_product(session, product_id, name, quantity):
    insert_statement = session.prepare("""
        INSERT INTO products (product_id, name, quantity)
        VALUES (?, ?, ?)
    """)
    session.execute(insert_statement, (product_id, name, quantity))
    print(f"Product {name} added!")


def get_product_by_id(session, product_id):
    select_statement = session.prepare("""
        SELECT * FROM products WHERE product_id = ?
    """)
    result = session.execute(select_statement, (product_id,))
    return result


def main():
    session = connect_to_cassandra()
    create_keyspace_and_table(session)

    from uuid import uuid4
    product_id = uuid4()
    insert_product(session, product_id, 'Product A', 100)

    result = get_product_by_id(session, product_id)
    for row in result:
        print(f"Product ID: {row.product_id}, Name: {row.name}, Quantity: {row.quantity}")

if __name__ == "__main__":
    main()
