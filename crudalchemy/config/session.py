import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_type = os.getenv("DB_TYPE")
database_name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
ip = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")


def get_db_uri():
    return f"{db_type}://{user}:{password}@{ip}:{port}/{database_name}"


SQLALCHEMY_DATABASE_URI = get_db_uri()
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

