from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    WebSocket,
    WebSocketDisconnect
)

from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import User
from schemas import SignupRequest, LoginRequest

from auth import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token
)


app = FastAPI()


# Create database tables
Base.metadata.create_all(bind=engine)


# Connected users
users = {}

@app.get("/")
async def home():

    return FileResponse("index.html")

@app.post("/signup")
def signup(
    data: SignupRequest,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.username == data.username
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )


    hashed_password = hash_password(
        data.password
    )


    new_user = User(
        username=data.username,
        password=hashed_password
    )


    db.add(new_user)

    db.commit()

    db.refresh(new_user)


    return {
        "message": "Signup successful",
        "username": new_user.username
    }


@app.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == data.username
    ).first()


    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )


    if not verify_password(
        data.password,
        user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )


    access_token = create_access_token(
        user.username
    )


    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }


@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str
):

    try:

        payload = decode_access_token(token)

        username = payload.get("sub")

        if not username:

            await websocket.close(
                code=1008
            )

            return


    except Exception:

        await websocket.close(
            code=1008
        )

        return


    await websocket.accept()


    users[username] = websocket

    print(f"{username} connected")


    try:

        while True:

            message = await websocket.receive_text()


            # Example:
            # for now User 1 ↔ User 2

            if username == "user1":

                receiver = "user2"

            else:

                receiver = "user1"


            if receiver in users:

                await users[receiver].send_text(
                    f"{username}: {message}"
                )


    except WebSocketDisconnect:

        print(
            f"{username} disconnected"
        )


        if username in users:

            del users[username]