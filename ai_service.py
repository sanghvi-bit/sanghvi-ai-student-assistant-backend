
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)

# Use the exact model ID available to your API key.
MODEL = "gemini-3.8-flash"


def generate_ai_summary(text: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=(
            "Summarize these study notes clearly. "
            "Use headings and bullet points where helpful.\n\n"
            + text
        ),
    )
    return response.text or ""


def generate_ai_quiz(text: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=(
            "Create 5 multiple-choice questions from these notes. "
            "Give four options and the correct answer for each.\n\n"
            + text
        ),
    )
    return response.text or ""


def generate_ai_chat(message: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=(
            "You are a friendly AI study tutor. "
            "Explain concepts simply and clearly.\n\n"
            + message
        ),
    )
    return response.text or ""
