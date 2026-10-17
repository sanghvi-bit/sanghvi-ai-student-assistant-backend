
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")

client = MongoClient(MONGODB_URL)
db = client["ai_study_assistant"]

summaries_collection = db["summaries"]
quizzes_collection = db["quizzes"]
chats_collection = db["chats"]