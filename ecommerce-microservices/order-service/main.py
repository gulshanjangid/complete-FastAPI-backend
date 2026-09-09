from fastapi import FastAPI

app = FastAPI(title="Order Service")


@app.get("/")
def home():
    return {
        "message": "Order Service is running"
    }


@app.get("/orders")
def get_orders():
    return {
        "orders": [
            {
                "id": 1,
                "user_id": 1,
                "product_id": 1,
                "status": "confirmed"
            }
        ]
    }