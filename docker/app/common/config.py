import os

from dotenv import load_dotenv

env_path = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, os.pardir, '.env'))
load_dotenv(dotenv_path=env_path)

# Адрес и параметры внешнего сервиса вопросов
API_URL = 'https://jservice.io/api/random'
PARAM_COUNT = 'count'

# Параметры базы данных
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

SQLALCHEMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

if __name__ == "__main__":
    print(env_path)