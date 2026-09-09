from fastapi import FastAPI

app  =  FastAPI(title="User Service")

@app.get("/")
def home():
    return {
        "message" : "User Service is  running"
    }

@app.get("/users")
def get_users():
    return {
        "users": [
            {
                "id": 1,
                "name": "Gulshan"
            },
            {
                "id": 2,
                "name": "Rahul"
            }
        ]
    }