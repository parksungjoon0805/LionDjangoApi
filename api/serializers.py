import json

def serialize_product(product):
    return {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": str(product.price),
        "in_stock": product.in_stock
    }