from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
import os


# Load .env
load_dotenv()

app = FastAPI()


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

print("Gemini API key loaded:", bool(api_key))


# Create Gemini client
client = genai.Client(api_key=api_key)


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "FastAPI + Gemini AI is running"
    }


@app.post("/ask")
def ask_ai(data: Question):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=data.question
    )

    return {
        "question": data.question,
        "answer": response.text
    }