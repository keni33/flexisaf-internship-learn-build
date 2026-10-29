# Connection and sessions
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

#create database
engine = create_engine("sqlite:///tasks.db", echo=False)
Base = declarative_base()
session = sessionmaker()
session = Session()

#Define models(users/tasks)
class user(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    task = relationship()

class 