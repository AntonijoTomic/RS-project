 
from uuid import UUID
from app.models.product import Product
from cassandra.query import SimpleStatement
from app.config.database import session

def insert_product(product_id: UUID, name: str, quantity: int):
    """ Ubacuje proizvod u bazu. """
    insert_statement = session.prepare("""
        INSERT INTO products (product_id, name, quantity)
        VALUES (?, ?, ?)
    """)
    session.execute(insert_statement, (product_id, name, quantity))
    print(f"Product '{name}' added!")
    
def update_product_quantity(product_id: UUID, new_quantity: int):
    """ Ažurira količinu proizvoda u bazi. """
    update_statement = session.prepare("""
        UPDATE products
        SET quantity = ?
        WHERE product_id = ?
    """)
    session.execute(update_statement, (new_quantity, product_id))
    print(f"Product {product_id} updated with new quantity: {new_quantity}")    

def get_product_by_id(product_id: UUID):
    """ Dohvaća proizvod po ID-u. """
    select_statement = session.prepare("""
        SELECT * FROM products WHERE product_id = ?
    """)
    result = session.execute(select_statement, (product_id,))
    
    # Pretvaramo svaki redak u Product objekt
    products = [Product(row.product_id, row.name, row.quantity) for row in result]
    
    return products

def delete_product(product_id: UUID):
    """ Briše proizvod iz baze prema ID-u. """
    delete_statement = session.prepare("""
        DELETE FROM products WHERE product_id = ?
    """)
    session.execute(delete_statement, (product_id,))
    print(f"Product {product_id} deleted.")
    
def get_all_products():
    """ Dohvaća sve proizvode iz baze. """
    select_statement = session.prepare("""
        SELECT * FROM products
    """)
    result = session.execute(select_statement)
    
    # Pretvaramo svaki redak u Product objekt
    products = [Product(row.product_id, row.name, row.quantity) for row in result]
    
    return products
