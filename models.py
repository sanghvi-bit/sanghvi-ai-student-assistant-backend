from pydantic import BaseModel, Field

class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=5, description="Study notes to summarize")

class QuizRequest(BaseModel):
    text: str = Field(..., min_length=5, description="Material to create quiz from")

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Question for the AI tutor")