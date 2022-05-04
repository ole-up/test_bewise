from datetime import datetime

from sqlalchemy.orm import Session

from app.questions import models, schemas


def check_question(db: Session, id: int):
    if db.query(models.Question).filter(models.Question.id == id).count():
        return True
    else:
        return False


def create_question(db: Session, id: int, question: str, answer: str, created_at):
    question_row = models.Question(id=id, question=question, answer=answer, created_at=created_at)
    db.add(question_row)
    db.commit()
    return schemas.Question.from_orm(question_row)
