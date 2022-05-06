from sqlalchemy import Column, Integer, String, DateTime

from sqlalchemy_utils import create_database, database_exists

from app.db.session import Base, engine


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)


if __name__ == "__main__":
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)
