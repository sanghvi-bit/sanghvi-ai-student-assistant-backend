from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import summaries_collection, quizzes_collection, chats_collection
from models import SummaryRequest, QuizRequest, ChatRequest
from ai_service import generate_ai_summary, generate_ai_quiz, generate_ai_chat

app = FastAPI(title="AI Study Assistant API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow()}

@app.post("/api/summarize")
def summarize_notes(payload: SummaryRequest):
    try:
        summary = generate_ai_summary(payload.text)
        record = {
            "type": "summary",
            "input": payload.text,
            "output": summary,
            "created_at": datetime.utcnow()
        }
        summaries_collection.insert_one(record)
        return {"success": True, "summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/quiz")
def create_quiz(payload: QuizRequest):
    try:
        quiz = generate_ai_quiz(payload.text)
        record = {
            "type": "quiz",
            "input": payload.text,
            "output": quiz,
            "created_at": datetime.utcnow()
        }
        quizzes_collection.insert_one(record)
        return {"success": True, "quiz": quiz}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat")
def chat_with_tutor(payload: ChatRequest):
    try:
        reply = generate_ai_chat(payload.message)
        record = {
            "type": "chat",
            "input": payload.message,
            "output": reply,
            "created_at": datetime.utcnow()
        }
        chats_collection.insert_one(record)
        return {"success": True, "reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/history")
def get_history():
    try:
        summaries = list(summaries_collection.find({}, {"_id": 0}).sort("created_at", -1).limit(10))
        quizzes = list(quizzes_collection.find({}, {"_id": 0}).sort("created_at", -1).limit(10))
        chats = list(chats_collection.find({}, {"_id": 0}).sort("created_at", -1).limit(10))
        
        return {
            "summaries": summaries,
            "quizzes": quizzes,
            "chats": chats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))