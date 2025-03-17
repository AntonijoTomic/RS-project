from uuid import UUID

class Product:
    def __init__(self, product_id: UUID, name: str, quantity: int):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"Product(product_id={self.product_id}, name={self.name}, quantity={self.quantity})"

