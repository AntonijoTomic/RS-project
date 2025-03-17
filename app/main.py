from fastapi import FastAPI
from app.routes.product_routes import router as product_router

app = FastAPI()

# Registriramo rute za proizvode
app.include_router(product_router)

