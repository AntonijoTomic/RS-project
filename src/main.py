from cassandra_manager import connect_to_cassandra, create_keyspace_and_table, insert_product, get_product_by_id
from uuid import uuid4

def main():
    session = connect_to_cassandra()
    create_keyspace_and_table(session)

    product_id = uuid4()
    insert_product(session, product_id, 'Product A', 100)

  
    result = get_product_by_id(session, product_id)
    
    for row in result:
        print(f"Product ID: {row.product_id}, Name: {row.name}, Quantity: {row.quantity}")

if __name__ == "__main__":
    main()
