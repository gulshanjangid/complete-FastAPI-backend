from fastapi import FastAPI

app = FastAPI(title="Product Service")


@app.get("/")
def home():
    return {
        "message": "Product Service is running"
    }


@app.get("/products")
def get_products():
    return {
        "products": [
            {
                "id": 1,
                "name": "Laptop",
                "price": 50000
            },
            {
                "id": 2,
                "name": "Mobile",
                "price": 20000
            }
        ]
    }