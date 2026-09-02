from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()


# This function will run in the background
def send_email(email: str):
    print(f"Starting email task for {email}")

    time.sleep(5)

    print(f"Email sent successfully to {email}")


@app.post("/send-email")
def send_email_api(
    email: str,
    background_tasks: BackgroundTasks
):
    # Add task to background
    background_tasks.add_task(send_email, email)

    return {
        "message": "Request received. Email will be sent in background.",
        "email": email
    }


@app.get("/")
def home():
    return {
        "message": "Background Task API is running"
    }