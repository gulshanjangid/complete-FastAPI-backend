# from fastapi import FastAPI, Request

# app = FastAPI()


# @app.middleware("http")
# async def my_middleware(request: Request, call_next):

#     print("Request received")

#     response = await call_next(request)

#     print("Response sent")

#     return response


# @app.get("/home")
# async def home():
#     return {"message": "Hello World"}

from fastapi import FastAPI, Request
import time

app = FastAPI()


@app.middleware("http")
async def logging_middleware(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    print(
        f"{request.method} "
        f"{request.url.path} "
        f"{response.status_code} "
        f"{process_time:.4f}s"
    )

    return response


@app.get("/")
async def home():
    return {"message": "Hello World"}


@app.get("/students")
async def students():
    return {"students": ["Gulshan", "Rahul"]}