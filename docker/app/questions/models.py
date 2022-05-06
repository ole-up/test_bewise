from sqlalchemy import Column, Integer, String, DateTime

from app.db.session import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)
