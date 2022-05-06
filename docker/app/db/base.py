# Import all the models, so that Base has them before being imported by Alembic

from app.db.session import Base  # noqa
from app.questions.models import Question  # noqa
