from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Sequence, Index, func

from app.db.session import Base, engine

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)
