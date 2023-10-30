from sqlmodel import Session, create_engine, SQLModel
# from . import config
from .config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
import urllib.parse

connection = (
    "mariadb+pymysql://{username}:{password}@{hostname}:{port}/{database_name}?charset=utf8mb4"
)

engine = create_engine(
    connection.format(
        username=DB_USERNAME,
        password=urllib.parse.quote_plus(DB_PASSWORD),
        hostname=DB_HOST,
        port=DB_PORT,
        database_name=DB_NAME,
    ),
    echo=True,
    pool_pre_ping=True
)


def get_session():
    with Session(engine) as session:
        yield session
