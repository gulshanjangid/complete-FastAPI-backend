from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

app = FastAPI()


# Store connected users
users = {}


@app.get("/")
async def home():
    return FileResponse("index.html")


@app.websocket("/ws/{username}")
async def websocket_endpoint(
    websocket: WebSocket,
    username: str
):

    # Accept connection
    await websocket.accept()

    # Store user
    users[username] = websocket

    print(f"{username} connected")

    try:

        while True:

            # Receive message
            message = await websocket.receive_text()

            # Get receiver
            if username == "user1":
                receiver = "user2"
            else:
                receiver = "user1"

            # Check receiver is connected
            if receiver in users:

                await users[receiver].send_text(
                    f"{username}: {message}"
                )

    except WebSocketDisconnect:

        print(f"{username} disconnected")

        if username in users:
            del users[username]