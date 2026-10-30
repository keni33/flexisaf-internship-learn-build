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
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
     #this makes it a parent to the table tasks and if i delete a user it refereces it in the child
    task = relationship('Tasks', back_populates='user', cascade="all, delete-orphan")
£making relationships
class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(string(50), nullable=True)
    description = Column(string)
    user_id = Column(Integer, ForeignKey('user_id'))
    user = relationship('User', back_populates='tasks')


Base.metadata.create_all(engine)

#utility functions

