# from fastapi import FastAPI, Depends,Header, HTTPException

# app = FastAPI()

# def varify_token(token :str = Header(None)):
#     if(token !="mysecrettoken"):
#         raise HTTPException(
#             status_code=401,
#             detail= "Unauthorized"
#         )
#     return {
#         "User":"Authorized user"
#     }

# @app.get("/secure-data")
# def secure_data(user = Depends(varify_token)):
#     return {
#         "message" : "Secure data accessed",
#         "user" : user
#     }


#Global Dependencies

# from fastapi import FastAPI, Depends

# def check_user():
#     print("Checking user...")

# app = FastAPI(
#     dependencies=[Depends(check_user)]
# )


# @app.get("/")
# def home():
#     return {"message": "Home"}


# @app.get("/students")
# def students():
#     return {"message": "Students"}


#Security Dependencies
from fastapi import FastAPI, Depends

app = FastAPI()


def get_token():
    return "my-token"


def get_current_user(token=Depends(get_token)):
    return {
        "name": "Gulshan",
        "token": token
    }


@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user