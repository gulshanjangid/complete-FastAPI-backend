from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()

security = HTTPBearer()


# Dependency
def authenticate_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    if token != "12345":
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return {
        "id": 1,
        "name": "Gulshan"
    }


# Public API
@app.get("/")
def home():
    return {
        "message": "Public API"
    }


# Protected API
@app.get("/profile")
def profile(user=Depends(authenticate_user)):
    return {
        "message": "Authenticated successfully",
        "user": user
    }


# Another protected API
@app.get("/orders")
def orders(user=Depends(authenticate_user)):
    return {
        "user": user,
        "orders": [
            "Laptop",
            "Mobile"
        ]
    }