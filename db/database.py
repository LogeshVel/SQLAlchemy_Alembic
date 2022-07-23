from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_URL = "sqlite:///C:/Users/L/PycharmProjects/SQLAlchemy_Alembic/data.db"
# data.db is the file where the data will be stored

sql_engine = create_engine(
    SQLALCHEMY_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sql_engine)

Base = declarative_base()
