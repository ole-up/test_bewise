from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.utils import get_questions
from app.questions import crud, schemas
from app.db.session import SessionLocal

router = APIRouter()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/api/", response_model=schemas.Question)
def question_response(questions_request: schemas.QuestionRequest,
                      db: Session = Depends(get_db)):
    questions_list = []
    penultimate_question = {} # предпоследний вопрос
    # получаем список вопросов с запрашиваемым количеством
    questions_list = get_questions(questions_request.questions_num)
    length_list = len(questions_list)
    for item in questions_list:
        # проверяем наличие вопроса в базе, если есть запрашиваем новый
        while crud.check_question(db=db, id=item['id']):
            item = get_questions(1)[0]
        # сохраняем вопрос в БД
        question = crud.create_question(db=db, id=item['id'], question=item['question'], answer=item['answer'],
                             created_at=item['created_at'])
        length_list -= 1
        # проверяем предпоследний ли вопрос в списке
        if length_list == 1:
            # если да, сохраняем для ответа
            penultimate_question = question
    return penultimate_question
