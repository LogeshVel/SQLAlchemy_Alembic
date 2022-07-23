from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    active_user = Column(Boolean, default=False)
