# from fastapi import FastAPI,HTTPException,Depends,Header
# from jose import jwt
# from datetime  import datetime, timedelta,timezone

# app = FastAPI()

# SECRET_KEY ="mysecret"
# ALGORITHM = "HS256"


# #create Token
# def create_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.now(timezone.utc) + timedelta(minutes=30)
#     to_encode.update({
#         "exp" :expire
#     })
#     token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
#     return token

# #Login API (Token Genrate)

# @app.post("/login")
# def login(username:str,password:str):
#     if username != "admin" or password != "1234" :
#        raise HTTPException(
#            status_code = 401,
#            detail="Invalid username and password"
       
#     )
#     token = create_token({
#         "sub" :username
#     })
#     return {
#         "access_token" :token
#     }

# #Token varify

# def varify_token(token: str = Header(None)):

#     try:
#         payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
#         return payload

#     except:
#         raise HTTPException(
#             status_code=401,
#             detail="Invaild or Expired Token"
#         )

#     #Protected Route

# @app.get("/secure")
# def secure_data(user = Depends(varify_token)):
#         return{
#             "message" : "Secure data Accessed",
#             "user" :user
#         }




from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

app = FastAPI()

SECRET_KEY = "my-secret-key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# LOGIN
@app.post("/login")
def login(username: str, password: str):

    if username != "gulshan" or password != "123456":
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = jwt.encode(
        {"sub": username},
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# VERIFY TOKEN
def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


# PROTECTED API
@app.get("/employees")
def get_employees(
    current_user: str = Depends(get_current_user)
):

    return {
        "message": f"Welcome {current_user}",
        "employees": [
            "Rahul",
            "Gulshan",
            "Amit"
        ]
    }