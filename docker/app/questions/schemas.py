from datetime import datetime

from pydantic import BaseModel, Field

class QuestionRequest(BaseModel):
    questions_num: int = Field(description="Количество запрашиваемых вопросов")

class Question(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True
