from fastapi import APIRouter, HTTPException
from uuid import UUID
from app.models.product import Product
from app.services.product_service import insert_product, get_product_by_id, get_all_products, update_product_quantity, delete_product

# Kreiramo router za proizvode
router = APIRouter()

# Endpoint za dodavanje proizvoda
@router.post("/products/")
def add_product(name: str, quantity: int):
    product_id = uuid4()
    insert_product(product_id, name, quantity)
    return {"product_id": product_id, "name": name, "quantity": quantity}

@router.get("/products/")
def get_all_products_endpoint():
    result = get_all_products()
    if not result:
        raise HTTPException(status_code=404, detail="No products found")
    return result
# Endpoint za dohvaćanje proizvoda prema ID-u
@router.get("/products/{product_id}")
def get_product(product_id: UUID):
    result = get_product_by_id(product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return result[0]  # Vraćamo prvi (jedini) proizvod iz liste

# Endpoint za ažuriranje proizvoda
@router.put("/products/{product_id}")
def update_product(product_id: UUID, quantity: int):
    result = get_product_by_id(product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    update_product_quantity(product_id, quantity)
    return {"message": "Product updated", "product_id": product_id, "new_quantity": quantity}

# Endpoint za brisanje proizvoda
@router.delete("/products/{product_id}")
def delete_product_endpoint(product_id: UUID):
    result = get_product_by_id(product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    delete_product(product_id)
    return {"message": "Product deleted", "product_id": product_id}

